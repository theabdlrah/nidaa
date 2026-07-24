# Nidaa — Process Rule PR-2 (Day 10 evidence-preservation rule)

Type: PROCESS RULE (Day 10 deliverable). Companion to PR-1. Source of truth for evidence
PRESERVATION (PR-1 covers INGESTION). Triggered by the Day-10 Evidence Preservation Audit,
which found a SECOND failure class beyond ingestion:

  PR-1 question: "Can evidence fail to ENTER the system?" -> Yes (Hisem, ingestion failure).
  PR-2 question: "Can evidence ENTER the system and still become UNRECOVERABLE?" -> Also yes
  (Aaron, Abdelrahman, Adam: ingested but only as SUMMARY; verbatim original lost).

PR-2 converts that second-order failure into a standing control.

==================================================================
PROCESS RULE PR-2 — PRIMARY-SOURCE PRESERVATION
==================================================================

For EVERY practitioner source, the following are REQUIRED (not optional):
  1. RAW TRANSCRIPT / MESSAGE — the verbatim original, stored in
     pilot/raw-transcripts/<SOURCE>-<DATE>.md. No paraphrase, no edit, no summary.
  2. EVIDENCE INTAKE — pilot/EVIDENCE-INTAKE-TEMPLATE.md, citing the raw transcript file.
  3. ASSUMPTION LINKAGE — pilot/ASSUMPTION-TRACKER.md, citing the raw transcript file.

The following are OPTIONAL secondary layers (they may summarize, but never replace):
  - Journal summary (pilot/EVIDENCE-JOURNAL.md)
  - Brief summary (docs/Nidaa-Day6-Brief.md and derivatives)

CORE PRINCIPLE (the rule in one line):
  No assumption may cite a summary when a primary source exists. The citation must always
  point back to the PRIMARY artifact (the raw transcript), not to a summary of it.

PROHIBITED:
- Treating a summary as the evidence itself. A summary may SUPPORT an assumption; it is not
  the evidence. (Ban summary-as-evidence.)
- Writing an Assumption Tracker / Brief entry that paraphrases a reply without citing the raw
  transcript file.
- Deleting or overwriting a raw transcript with a summary.

CARRY-FORWARD (from the Preservation Audit):
- Aaron, Abdelrahman, Adam: verbatim originals MISSING (summary-only on record). When
  re-engaged, capture raw transcript per PR-1 + PR-2. Until then, their assumption links must
  be explicitly flagged "summary-only, primary missing" (already done in Preservation Audit).
- Hisem: not ingested at all (PR-1 Artifact Gap). When located, ingest per PR-1 then preserve
  per PR-2.
- Mones: the model — verbatim preserved; migrate a copy to raw-transcripts/.

==================================================================
GOVERNANCE WIRING
==================================================================
- Referenced from: Nidaa-Day6-Brief.md (NIDAA COMMAND ROUTING RULE section).
- Referenced from: docs/Nidaa-A6b-Evidence-Ledger.md "HOW TO FILL" (verbatim requirement).
- Referenced from: pilot/ASSUMPTION-TRACKER.md "Post-Conversation Template" (cite primary).
- Companion: Nidaa-Day10-Process-Rule-PR1.md (ingestion). PR-1 + PR-2 = the evidence
  integrity chain (enter -> preserve). The authoritative artifact ordering is declared in
  Nidaa-Source-of-Truth-Hierarchy.md (raw transcript > intake > field log > tracker >
  ledger > journal > briefs). PR-3 (Nidaa-Day10-Process-Rule-PR3.md) closes each day with a
  Preservation Record (docs/YYYY-MM-DD-DayX-Preservation-Record.md) so project state itself
  is preserved against model-memory / context / personnel loss.

==================================================================
HEALTH IMPACT (post-mitigation target)
==================================================================
Collection: Moderate -> Good (PR-1 same-session intake).
Traceability: Good (unchanged; every assumption linked to a named source).
Preservation: Weak -> Strong (PR-2 verbatim-primary requirement; raw-transcripts/ store).
Audit Readiness: Conditional -> Audit-Ready (once Mones migrated + gaps flagged + journal live).

END OF PR-2.
