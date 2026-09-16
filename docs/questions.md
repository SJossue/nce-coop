# Questions for Nayelli

> Running doc, newest/most-important on top. Nayelli explicitly asked for exactly this: "keep
> notes on questions, areas that need clarification, and ideas for eventually automating the
> posting-monitoring process."

## Ask first, before building anything beyond the manual-paste MVP
- **The strategic plan reveals NJIT already runs a "Co-op approval automation system using
  Registrar and Handshake data for mass co-op approval labeling"** (25-26 Goal 2, Tactic 3,
  piloted Fall 2025/Spring 26, in effect for Summer/Fall 26). That's *student*-eligibility
  labeling, not *posting*-eligibility labeling, so it's not a drop-in fix for this project, but
  it proves NJIT already has some Registrar-Handshake data integration. **Ask directly whether
  that pipeline (or the access behind it) could extend to posting labeling**, before building
  anything from scratch. This is now the single highest-leverage question, ahead of the generic
  API question below. See `strategic-plan.md`.
- **Does NJIT/Handshake offer an official API or bulk-export for school admins**, beyond
  whatever powers the system above? If one exists, it replaces scraping entirely and sidesteps
  any ToS question. See `roadmap.md` Phase 0.
- **Is automated/session-based access to Handshake actually okay**, distinct from "can I build
  my own tooling"? Worth a direct yes from her or IT rather than an assumption, if the above
  comes back empty and scraping becomes the only option.

## Process clarifications
- How is this role actually measured? No stated KPI/cadence in the onboarding email. The
  strategic plan's Goal 3 assessment plan (26-27) names "processing and approval timelines" and
  "data quality and reporting capabilities" as office-level metrics, likely the closest thing to
  a real answer, but worth confirming whether those apply to this specific work or are
  higher-level. See `strategic-plan.md` Goal 3 and Goal 5.
- What does the H4 label track? Referenced in the expired-postings follow-up step but not
  defined.
- Where does Zac's outreach list live?
- Bus Dev sheet column definitions: need to actually open the sheet (onboarding task 2) before
  `export` can target real columns.
- The filtered Handshake URL from the onboarding email had corrupted query-param encoding; need
  a clean working link once access is granted.
- If/when automation output exists, what format is most useful to her: direct sheet write, a
  CSV to paste in, or a plain list? (No Sheets API is wired up yet, so this shapes what `export`
  should produce first.)
