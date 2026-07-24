# Nidaa — Day-Close Checklist (Standing Practice)

Standing practice adopted Day 13 (2026-07-25), recorded here so it does not live
only in chat. Deliberately NOT part of `Nidaa-Build-Governance.md` (governance stays
stable; this is a working practice — fold into governance only if repeated experience
justifies it).

Runs at the END of each Nidaa day, before the day is declared closed. Mirrors the
Day-12 Operational Integrity Review but at close rather than open, and — critically —
it is the gate that catches work that exists ONLY in chat.

Before declaring a day closed, answer ALL of the following. If any answer is
unsatisfactory, resolve it (record or correct) BEFORE closing the day:

1. **Repository committed and pushed?**
   `git status` clean-or-intentional; `git log`/remote confirms the day's work is
   persisted and pushed (not just local).

2. **Evidence Journal updated?**
   `pilot/EVIDENCE-JOURNAL.md` reflects the day's evidence events (or explicitly
   records "no evidence event" for engineering-only days).

3. **Narrative journal updated?**
   `C:\Users\theab\Desktop\Nidaa-Journal.docx` — IF it is still an active project
   artifact. As of Day 13 it IS in scope. Any narrative-relevant work from the day
   that is not yet mirrored there must be added before close. (This item was the
   Day-12–Day-13 gap: the `.docx` was silently excluded from review scope and the
   engineering phase was discovered stale several days later. Do not let it recur.)

4. **Tracker / specs / governance synchronized?**
   `docs/MILESTONES.md`, frozen specs under `docs/specs/`, and
   `Nidaa-Build-Governance.md` all reflect the day's actual state. No stale cells,
   no tracker entry contradicting the repo.

5. **Anything still exists only in chat?**
   Scan the day's conversation for decisions, findings, bug fixes, or state changes
   that were reasoned through in chat but never written to a durable artifact (repo,
   journal, tracker, or doc). If found, persist it before close.

Pass: "Day X close verified — repo pushed, journals synced, nothing left in chat."
Fail: list the gap; close the gap (or, if genuinely deferring, record the deferral
with a reason) before declaring the day closed.

## Why this exists
The Day-12 discipline proved "don't trust writes; verify resulting state." But
verification at day-open only catches drift that the PREVIOUS close left behind. A
close-time checklist is the complementary gate: it is the moment a day's work is
forced out of chat and into artifacts. A fact that lives only in chat is a fact that
will not survive the next context window.
