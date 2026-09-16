# The manual monitoring process (spec for the tooling)

Transcribed from Nayelli Perez's onboarding email, 2026-09-16 ("Program Assistant -
Undergraduate Engineering Co-op onboarding and first tasks"). This is her own workflow,
documented here as the spec `src/nce_coop/` should eventually encode. It isn't automated
end-to-end yet; see `roadmap.md`.

## Day 1-3 onboarding tasks
1. Review onboarding materials (job description PDF, 2 historical/engagement slides, NCE Co-op
   strategic plan doc, see `contacts.md` for the link).
2. Get acquainted with the NCE Bus Dev Google Sheet: its fields/tabs. **Still pending.** The
   actual column schema this tooling's `export` command should target is unknown until this
   happens.
3. Get Handshake permissions via Koustubh, matching Mitchell's access. **Still pending.**
4. Run the posting-monitoring process (below).
5. Keep a running notes/questions doc (see `questions.md`).
6. Explicit ask from Nayelli: figure out how to automate generating the list of new NCE Co-op /
   FT Internship postings from Handshake and other sources. This repo is that effort.

## "MONITOR ENG CO-OP AND INTERNSHIP FULL TIME JOBS": Nayelli's process
- **Search terms:** co-op, coop, co op, fall, sept, spring, jan, feb, winter, plus checking
  local postings.
- **Filtered Handshake URL:** job type = Cooperative Education + Internship, employment type =
  Full-Time, filtered to a specific list of major codes. The URL pasted in the original email
  had corrupted query-param encoding; a clean working link is needed once Handshake access
  exists.
- **Pending postings:** check them; put relevant ones in the Bus Dev sheet tab; note when they
  become approved.
- **New postings:** check what was posted yesterday and today; add to the sheet.
- **Co-op-eligible labeling rule:** apply "[most current] co-op eligible" so only co-op-approved
  students can apply, when:
  - job type is Cooperative Education (if engineering-only), **or**
  - job type is Full-Time Internship **and** the title says "co-op" **and** it's
    engineering-only.
  (This is `src/nce_coop/rules.py`, the one part of this process that's fully specified and
  already implemented and tested.)
- **Expired postings:** find which jobs expired yesterday; move those to a follow-up tab; note
  any with the co-op-eligible label; check for an H4 label (meaning still unclear, see
  `questions.md`); look up co-op eligibility for the rest.
- **Bus Dev doc/file revamp:** cross-reference Nayelli's summer outreach list + Zac's outreach
  list against Handshake's employer section: the "expressed interest in your school" homepage
  view, and the all-employers tab with filters.
- **Ongoing:** monitor labor-market news and outside postings for timely employer outreach.
- **Job search alerts:** set up alerts for eng co-op roles as part of the Bus Dev revamp.
- **Collections:** build collections of postings; find employers on Indeed and LinkedIn, post as
  an employer page for Bus Dev; create a saved-search collection of co-op postings (narrow to
  Cooperative Education job type, "co-op" in title).

## Last known state (as of the onboarding email)
Nayelli last checked 9/4-9/12. Jossue picks up from there once he has access.
