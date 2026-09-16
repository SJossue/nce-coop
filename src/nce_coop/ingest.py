"""Ingestion for Handshake posting data: NOT YET IMPLEMENTED.

Deliberately left as a stub: as of 2026-09-16 Jossue doesn't have Handshake access yet, and
the real export/paste format Handshake gives a user has never been seen. Building a parser
before that would be guesswork. See docs/questions.md (ask about an official API first, before
anything else) and docs/roadmap.md Phase 1 (manual paste-and-diff is the first real ingestion
path once access exists).

Once real data exists, this should take whatever format is actually available (copy-pasted
search-results table, CSV export, API response, depending on the Phase 0 answer) and return a
list of dicts shaped for store.merge():
    {"id": ..., "title": ..., "employer": ..., "job_type": ..., "employment_type": ...,
     "url": ..., "posted_at": ..., "engineering_only": ...}
"""


def from_file(path: str) -> list[dict]:
    raise NotImplementedError(
        "Handshake ingestion isn't built yet: no access or sample data to design against. "
        "See docs/questions.md and docs/roadmap.md Phase 1."
    )
