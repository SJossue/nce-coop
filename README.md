# nce-coop

Tooling for Jossue's part-time role as **Program Assistant, Undergraduate Engineering Co-op**
at NJIT Career Services / Newark College of Engineering (started 2026-09-16, manager: Nayelli
Perez). Supports monitoring Handshake for new/expired Engineering co-op and full-time-internship
postings, applying the office's co-op-eligibility labeling rule, and maintaining the "NCE Bus
Dev" Google Sheet.

**Not the same thing as** `pancake/co-op-tracker/` — that's Jossue's own, personal internship
application tracker (his job search). This repo is NJIT institutional tooling, built for the
co-op *office's* pipeline, kept separate on purpose since it touches an employer's systems and
data, not personal context. Personal notes on this job (contacts summary, log) still live in
`pancake/workspaces/coop-office/` — this repo is where the actual tooling and institutional
process docs live.

## Status (2026-09-16)
- Handshake access: not yet granted (pending Koustubh, matched to Mitchell's permissions).
- Bus Dev sheet: linked but not yet reviewed (fields/tabs unknown).
- No postings data ingested yet — `ingest.py` is a documented stub until real access exists.

## Layout
- `docs/contacts.md` — who's who
- `docs/process.md` — the manual monitoring process this tooling should eventually encode
- `docs/questions.md` — running open questions for Nayelli
- `docs/roadmap.md` — phased build plan, ask-before-build first
- `src/nce_coop/` — the tool itself (rules, state store, CLI, ingestion stub)
- `tests/` — unit tests (currently: the labeling rule, the one fully-specified piece)
- `data/postings.json` — local state store

## Setup
```
python -m venv .venv && source .venv/bin/activate
pip install -e .   # stdlib only for now, no third-party deps
pytest
python -m nce_coop --help
```
