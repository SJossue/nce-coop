"""The co-op-eligibility labeling rule.

Verbatim from Nayelli Perez's onboarding email (2026-09-16): apply the "co-op eligible" label
so only co-op-approved students can apply, when:
  - job type is Cooperative Education (and the posting is engineering-only), OR
  - job type is Internship + employment type is Full-Time, AND the title says "co-op",
    AND the posting is engineering-only.

This is the one piece of the whole process that's fully specified independent of what
Handshake data actually looks like once ingestion exists; see docs/process.md and
docs/questions.md for what's still unresolved.
"""

LABEL = "co-op eligible"


def is_co_op_eligible(job_type: str, employment_type: str, title: str, engineering_only: bool) -> bool:
    if not engineering_only:
        return False
    jt = (job_type or "").strip().lower()
    et = (employment_type or "").strip().lower()
    if jt == "cooperative education":
        return True
    if jt == "internship" and et == "full-time" and "co-op" in (title or "").lower():
        return True
    return False


def label(job_type: str, employment_type: str, title: str, engineering_only: bool) -> str | None:
    return LABEL if is_co_op_eligible(job_type, employment_type, title, engineering_only) else None
