# Daily Habit — Project Synchronization (Standing Practice)

Adopted Day 13 (2026-07-25). Recorded here so it does not live only in chat.
Deliberately NOT part of `Nidaa-Build-Governance.md` (governance stays stable;
fold into governance only if repeated experience justifies it). This is the
canonical end-of-session routine.

Every Nidaa work session ends by synchronizing both the project and its records.

## 1. Synchronize GitHub
- Commit all intentional Nidaa changes.
- Push to the remote repository.
- Verify the remote matches the local repository (verify resulting state — do not
  rely on the push message alone).

## 2. Synchronize Project Records
- Update **`pilot/EVIDENCE-JOURNAL.md`** with the day's engineering and evidence
  events. This is the canonical factual record.
- Update **`Nidaa-Journal.docx`** with the day's narrative (mission, successes,
  failures, lessons, decisions, current state, and next objective). This journal
  exists **for personal reference and reflection** and complements, but does not
  duplicate, the repository records. Use the captain's-log structure.

## 3. Confirm Completeness
- Ensure no important decision or lesson exists only in chat.
- Ensure every maintained project artifact has been:
  - updated,
  - intentionally left unchanged, or
  - explicitly retired.
- Only after these checks pass is the day considered closed.

## Standing Principle
> Every work session ends by synchronizing the repository and the journals. GitHub
> preserves the project's technical history; the journals preserve both the
> project's factual record and my understanding of that history.

## Why this exists / provenance
Adopted from the project lead's explicit Day-13 instruction, refined to distinguish
the two journals' roles. It closes the Day-12–Day-13 gap, where the narrative
`.docx` drifted four days behind because it was silently outside the pre-day review
scope (the review's "journal" implicitly meant only `pilot/EVIDENCE-JOURNAL.md`).
The `.docx` is now a named item here and in `docs/PRE-DAY-REVIEW.md`, so it cannot
silently drift again. Foundation: the Day-12 discipline ("don't trust writes; verify
resulting state") — verification at day-open only catches drift the previous close
left behind; a close-time gate forces a day's work out of chat and into artifacts.
