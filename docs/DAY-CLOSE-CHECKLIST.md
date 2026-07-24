# Nidaa — Daily Habit: Project Synchronization (Standing Practice)

Adopted Day 13 (2026-07-25). Recorded here so it does not live only in chat.
Deliberately NOT part of `Nidaa-Build-Governance.md` (governance stays stable;
fold into governance only if repeated experience justifies it). This is the
canonical end-of-session routine — it refines the earlier Day-Close draft into the
form the project lead specified.

At the end of EVERY Nidaa work session, before declaring the day closed:

## 1. Synchronize GitHub
- Commit all intentional Nidaa changes.
- Push to the remote repository.
- **Verify the remote matches local** — `git fetch` + compare HEAD; do not rely on
  the push message alone.

## 2. Synchronize the Project Records
- Update **`pilot/EVIDENCE-JOURNAL.md`** with the day's engineering/evidence events,
  following the "one fact, one home" principle.
- Update **`Nidaa-Journal.docx`** with the day's narrative (mission, successes,
  failures, lessons, decisions, project state, next objective). This journal exists
  **for the project lead's own reference and reflection**, not as the canonical
  engineering record. Use the captain's-log structure: it complements the repo
  artifacts instead of duplicating them.
  - Evidence Journal → what changed (factual record).
  - Milestones (`docs/MILESTONES.md`) → project status.
  - Specs (`docs/specs/`) → design decisions.
  - Captain's Log (`Nidaa-Journal.docx`) → the story: why the project evolved.

## 3. Confirm Completeness
- No important decision or lesson exists only in chat.
- Every maintained project artifact is either: **updated**, **intentionally left
  unchanged**, or **explicitly retired**.
- Only after these checks pass is the day considered closed.

## Standing Principle
> Every work session ends by synchronizing the repository and the journals.
> GitHub preserves the project's history; the journal preserves my understanding
> of that history.

## Why this exists / provenance
Adopted from the project lead's explicit Day-13 instruction. It closes the
Day-12–Day-13 gap, where the narrative `.docx` drifted four days behind because it
was silently outside the pre-day review scope (the review's "journal" implicitly
meant only `pilot/EVIDENCE-JOURNAL.md`). The `.docx` is now a named item here and in
`docs/PRE-DAY-REVIEW.md`, so it cannot silently drift again. The Day-12 discipline
("don't trust writes; verify resulting state") is the foundation: verification at
day-open only catches drift the previous close left behind; a close-time gate is the
complementary checkpoint that forces a day's work out of chat and into artifacts.
