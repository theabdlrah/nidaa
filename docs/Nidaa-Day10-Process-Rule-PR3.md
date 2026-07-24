# Nidaa — Process Rule PR-3 (Day 10 daily preservation-record rule)

Type: PROCESS RULE (Day 10 deliverable). Companion to PR-1 (evidence ingestion) and PR-2
(evidence preservation). PR-3 preserves the STATE OF THE PROJECT ITSELF, so a future auditor
can reconstruct what happened, what changed, why, and what remains unknown — without chat
history, model memory, or external notes.

PR-1 ensures evidence ENTERS the system.
PR-2 ensures evidence is PRESERVED (verbatim primary).
PR-3 ensures the PROJECT STATE is preserved (daily record).

==================================================================
PR-3 — DAILY PRESERVATION RECORD
==================================================================

WHEN: once before closing every project day. The day is NOT closed until PR-3 is done.

OUTPUT: docs/YYYY-MM-DD-DayX-Preservation-Record.md — one file per day. NEVER overwrite
previous records. Append corrections only via dated addenda. (This is why Day 9's record,
created retroactively on Day 10, is a separate file and the two-version discrepancy is
preserved inside it, not erased.)

REQUIRED SECTIONS (11):
1. Day Summary (number/date/objective/outcome/verdict)
2. Project State (A1–A6b, canonical wording only: Established/Strengthened/Conditional/
   Missing/Falsified — no invented categories)
3. Evidence Movement (received / processed / gaps: G1, G2, disconfirming)
4. Contact Movement (state changes only: Contacted/Replied/Interviewed/Referred/Closed/
   Artifact Gap)
5. Assumption Movement ("No assumption state changed." if none)
6. Governance Movement (rules/templates/audits/controls/source-of-truth changes; "No
   governance changes." if none)
7. Discrepancies Discovered (contradictions/missing/ingestion/preservation/classification;
   include resolution + status + carry-forward; NEVER delete historical discrepancies)
8. Lessons Learned (operational/research/governance; from observed events only)
9. Carry Forward (evidence gaps / operational tasks / governance tasks, separated)
10. Audit Snapshot (Collection / Preservation / Traceability / Governance / Audit Readiness)
11. Final Day Verdict ("What uncertainty was reduced today?" + "What uncertainty remains?")

CORE PRINCIPLE: a future auditor reconstructs what happened / changed / why / what's unknown
from the record alone. PR-3 exists to preserve project state the way PR-1 preserves intake
and PR-2 preserves evidence integrity.

==================================================================
GOVERNANCE WIRING
==================================================================
- Referenced from: Nidaa-Day6-Brief.md (NIDAA COMMAND ROUTING RULE section).
- Companion: Nidaa-Day10-Process-Rule-PR1.md (ingestion) + Nidaa-Day10-Process-Rule-PR2.md
  (preservation) + Nidaa-Source-of-Truth-Hierarchy.md. PR-1 + PR-2 + PR-3 = full integrity
  governance: ENTER (PR-1) -> PRESERVE (PR-2) -> RECORD STATE (PR-3).
- First instantiations: docs/2026-07-22-Day10-Preservation-Record.md (Day 10) and
  docs/2026-07-21-Day9-Preservation-Record.md (Day 9, created retroactively).

END OF PR-3.
