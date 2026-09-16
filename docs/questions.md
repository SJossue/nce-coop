# Questions for Nayelli

> Running doc, newest/most-important on top. Nayelli explicitly asked for exactly this: "keep
> notes on questions, areas that need clarification, and ideas for eventually automating the
> posting-monitoring process."

## Ask first, before building anything beyond the manual-paste MVP
- **Does NJIT/Handshake offer an official API or bulk-export for school admins?** Many campus
  Handshake deployments have a partner/admin API. If one exists, it replaces scraping entirely
  and sidesteps any ToS question — worth asking before investing in any scraping approach.
  See `roadmap.md` Phase 0.
- **Is automated/session-based access to Handshake actually okay**, distinct from "can I build
  my own tooling"? Worth a direct yes from her or IT rather than an assumption, if Phase 0 comes
  back empty and scraping becomes the only option.

## Process clarifications
- How is this role actually measured? No stated KPI/cadence in the onboarding email — worth
  asking what "good" looks like (postings-per-day added? turnaround time on expired follow-ups?
  something else?).
- What does the H4 label track? Referenced in the expired-postings follow-up step but not
  defined.
- Where does Zac's outreach list live?
- Bus Dev sheet column definitions — need to actually open the sheet (onboarding task 2) before
  `export` can target real columns.
- The filtered Handshake URL from the onboarding email had corrupted query-param encoding —
  need a clean working link once access is granted.
- If/when automation output exists, what format is most useful to her — direct sheet write, a
  CSV to paste in, or a plain list? (No Sheets API is wired up yet, so this shapes what
  `export` should produce first.)
