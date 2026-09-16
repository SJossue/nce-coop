"""CLI for nce-coop.

  python -m nce_coop ingest <file>          # NOT YET IMPLEMENTED, see ingest.py
  python -m nce_coop list [--status new|pending|active|expired|actioned|all]
  python -m nce_coop show <id-prefix>
  python -m nce_coop label <id-prefix>      # re-apply the eligibility rule
  python -m nce_coop mark <id-prefix> <status>
  python -m nce_coop export                 # NOT YET IMPLEMENTED, Bus Dev columns unknown
"""
import argparse
import sys

from . import ingest, rules, store


def _print_row(r: dict) -> None:
    elig = "✓" if r.get("eligible") else " "
    print(f"[{r['status']:>9}] {elig} {r.get('employer', '')[:28]:<28} "
          f"{r.get('title', '')[:52]:<52} {r['id']}")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="nce_coop", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    ip = sub.add_parser("ingest")
    ip.add_argument("file")
    lp = sub.add_parser("list")
    lp.add_argument("--status", default="new")
    for name in ("show", "label"):
        sp = sub.add_parser(name)
        sp.add_argument("id")
    mp = sub.add_parser("mark")
    mp.add_argument("id")
    mp.add_argument("status", choices=store.STATUSES)
    sub.add_parser("export")
    args = p.parse_args(argv)

    if args.cmd == "ingest":
        postings = ingest.from_file(args.file)
        records = store.load()
        records, fresh = store.merge(records, postings)
        store.save(records)
        print(f"ingest: {fresh} new · {len(records)} tracked")
        return 0

    records = store.load()

    if args.cmd == "list":
        status = None if args.status == "all" else args.status
        listed = [r for r in records.values() if status is None or r["status"] == status]
        if not listed:
            print(f"no postings with status={args.status!r}, try `ingest` or `--status all`")
        for r in sorted(listed, key=lambda r: r.get("posted_at", ""), reverse=True):
            _print_row(r)
        return 0

    if args.cmd == "show":
        rec = store.find(records, args.id)
        for k, v in rec.items():
            print(f"{k:>16}: {v}")
        return 0

    if args.cmd == "label":
        rec = store.find(records, args.id)
        rec["eligible"] = rules.label(
            rec.get("job_type", ""), rec.get("employment_type", ""),
            rec.get("title", ""), rec.get("engineering_only", False),
        )
        store.save(records)
        print(f"{rec['id']} -> eligible={rec['eligible']!r}")
        return 0

    if args.cmd == "mark":
        rec = store.set_status(records, args.id, args.status)
        store.save(records)
        print(f"{rec['id']} -> {args.status}")
        return 0

    if args.cmd == "export":
        print("export: not yet implemented, Bus Dev sheet columns unknown, see docs/questions.md")
        return 1
    return 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (KeyError, ValueError, FileNotFoundError, NotImplementedError) as e:
        print(f"error: {e}", file=sys.stderr)
        raise SystemExit(1)
