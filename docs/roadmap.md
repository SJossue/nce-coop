# Roadmap

Phased on purpose — the highest-leverage move costs nothing to build and might make most of the
rest unnecessary.

## Phase 0 — ask before building (do this first)
Ask Nayelli/IT whether NJIT has official Handshake API or bulk-export access for school admins.
If it exists, it replaces scraping entirely and sidesteps any ToS question. This is a five-
minute question that could save weeks of scraping work — see `questions.md`.

## Phase 1 — paste-and-diff MVP
Buildable as soon as Jossue has any Handshake access at all, official API or not. He runs the
existing manual search process himself and pastes/exports the results; `ingest.py` parses that
into `store.py`'s schema; the tool diffs against the last run to compute new / still-pending /
expired postings, and auto-applies the `rules.py` co-op-eligibility rule. Zero authentication
risk beyond what he already has as a user — no scraping, no session automation.

## Phase 2 — authenticated scraping (only if Phase 0 comes back negative)
Evaluate carefully, and confirm explicitly with Nayelli/IT first that automated/session-based
access is acceptable — a distinct question from "can I build my own tooling," worth a direct
yes rather than an assumption. Only worth doing if the Phase 1 manual-paste cadence turns out to
be the actual bottleneck.

## Phase 3 — sheet-ready export
Once the Bus Dev sheet's real columns are known (onboarding task 2, still pending), make
`export` produce a paste-ready CSV/markdown table matching them exactly — removes the manual
reformatting step even without a Google Sheets API integration.

## Phase 4 — stretch, later
Not started until 1–3 are proven out:
- A weekly digest summarizing new/expired/labeled postings.
- Cross-referencing employer collections (Indeed/LinkedIn) per the onboarding email's Bus Dev
  revamp step.
