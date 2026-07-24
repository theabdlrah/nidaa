# Nidaa — Dual Independent Pre-Day Review

Standing practice adopted Day 12 (2026-07-24). Recorded here so it does not live
only in chat. Deliberately NOT part of `Nidaa-Build-Governance.md` (governance stays
stable; this is a working practice — fold into governance only if repeated experience
justifies it).

Before any new project day begins, two INDEPENDENT reviews are performed.
Neither review assumes the other is sufficient. The day begins only when both pass.

## Hermes — Operational Integrity Review

Objective: **verify that the project's recorded state matches the repository's
actual state.** ("Is the project recorded correctly?")

Checks: git status / push state / remote verification; tracker ↔ repo consistency;
journal ↔ repo consistency — where "journal" means BOTH the repo Evidence Journal
(`pilot/EVIDENCE-JOURNAL.md`) AND the narrative journal
(`C:\Users\theab\Desktop\Nidaa-Journal.docx`); frozen specs + governance consistency;
chat-only decisions; documentation drift; stale tracker or journal entries.

NOTE (2026-07-25, Day 13): the narrative `.docx` journal was added to scope on this
date per a standing Day-Close reminder. It had previously been **silently excluded**
from the review — a scope omission (the review's "journal" implicitly meant only the
repo Evidence Journal), not a rule violation. That omission is itself now a checklist
item so it cannot recur.

Pass: "Project state verified. Safe to begin Day X."
Fail: list the inconsistencies; resolve them before today's objective begins.

## Project lead + external reviewer — Epistemic Review

Objective: **verify that the project's conclusions remain justified by its evidence,
specifications, and methodology.** ("Is the project thinking correctly?")

The reviewer challenges the PROJECT'S REASONING wherever it originated — an
implementation, a research assumption, a governance decision — and may equally
confirm that claims are proportionate and well supported.

Checks: implementation claims vs available verification; research claims vs
available evidence; does today's objective follow from current state; methodology
drift; governance proportionality; spec internal consistency; assumption/evidence
separation; narrative coherence.

Pass: "Project reasoning reviewed. I don't see any methodological blockers.
Safe to begin Day X."
Fail: list the reasoning/methodology issues; resolve them before today's objective.

## Why both exist

The two reviews catch different failure classes. Operational review cannot catch a
claim that is stronger than its evidence; epistemic review cannot efficiently catch
a stale tracker cell or an unpushed commit. Independence plus complementary scope is
stronger than either alone — and mirrors the project's own philosophy: evidence
before confidence, verification before claims, independent review before progression.
