"""State for the NCE co-op posting monitor: data/postings.json.

One record per posting ever seen, keyed by a Handshake posting id (or a derived id if
Handshake's export doesn't expose one directly — see docs/questions.md). The file is meant to
be committed so the seen-set rides git history, same convention as pancake's
agent/jobs/store.py.

Statuses: new (just ingested) -> pending (awaiting NJIT approval) | active (approved, live)
-> expired (no longer posted) -> actioned (expired posting's follow-up is done).
"""
import datetime as _dt
import json
from pathlib import Path

from . import rules

STATUSES = ("new", "pending", "active", "expired", "actioned")
_FILE = Path(__file__).resolve().parent.parent.parent / "data" / "postings.json"
_MERGE_FIELDS = ("title", "employer", "job_type", "employment_type", "url", "posted_at")


def load() -> dict:
    """id -> record. Missing file means first run."""
    if not _FILE.exists():
        return {}
    return json.loads(_FILE.read_text(encoding="utf-8"))


def save(records: dict) -> None:
    _FILE.parent.mkdir(parents=True, exist_ok=True)
    _FILE.write_text(json.dumps(records, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def merge(records: dict, postings: list[dict]) -> tuple[dict, int]:
    """Fold a batch of postings in (however ingest.py eventually produces them). New ids
    arrive as status=new with eligibility computed via rules.label(); known ids keep their
    status but refresh title/employer/job_type/employment_type/url/posted_at and last_seen."""
    today = _dt.date.today().isoformat()
    fresh = 0
    for p in postings:
        eligible = rules.label(
            p.get("job_type", ""), p.get("employment_type", ""),
            p.get("title", ""), p.get("engineering_only", False),
        )
        prev = records.get(p["id"])
        if prev is None:
            fresh += 1
            records[p["id"]] = {
                **p, "status": "new", "eligible": eligible,
                "first_seen": today, "last_seen": today,
            }
        else:
            prev.update({k: p[k] for k in _MERGE_FIELDS if k in p})
            prev["eligible"] = eligible
            prev["last_seen"] = today
    return records, fresh


def set_status(records: dict, posting_id: str, status: str) -> dict:
    """Flip one record's status. posting_id may be a unique prefix of the full id."""
    if status not in STATUSES:
        raise ValueError(f"unknown status {status!r}; use one of {', '.join(STATUSES)}")
    rec = find(records, posting_id)
    rec["status"] = status
    return rec


def find(records: dict, posting_id: str) -> dict:
    """Exact id or unique prefix. Raises KeyError with a helpful message otherwise."""
    if posting_id in records:
        return records[posting_id]
    hits = [k for k in records if k.startswith(posting_id)]
    if len(hits) == 1:
        return records[hits[0]]
    if not hits:
        raise KeyError(f"no posting matches {posting_id!r} — run `ingest`, check `list`")
    raise KeyError(f"{posting_id!r} is ambiguous ({len(hits)} matches): " + ", ".join(sorted(hits)[:5]))
