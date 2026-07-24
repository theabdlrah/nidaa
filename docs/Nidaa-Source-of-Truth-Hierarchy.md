# Nidaa — Source-of-Truth Hierarchy (governance declaration)

Type: GOVERNANCE. Created Day 10, 2026-07-22 (final logic-consistency sweep). Declares the
authoritative ordering of Nidaa's evidence artifacts so future audits cannot disagree on
which file wins when two conflict. This directly answers the Day-10 question: "What is the
authoritative source-of-truth hierarchy?" — previously implicit, now explicit.

==================================================================
AUTHORITATIVE HIERARCHY (highest authority first)
==================================================================

1. RAW TRANSCRIPT / MESSAGE  (pilot/raw-transcripts/<SOURCE>-<DATE>.md)
   - The verbatim primary source. Practitioner's own words, unedited.
   - HIGHEST authority on WHAT WAS SAID. If a summary conflicts with the raw transcript,
     the raw transcript wins.

2. EVIDENCE INTAKE  (pilot/EVIDENCE-INTAKE-TEMPLATE.md)
   - Structured extraction citing the raw transcript. Secondary to the raw transcript.

3. FIELD LOG  (pilot/A6-FIELD-LOG.md)
   - Per-contact row (Reality A/B, owner/mandate, pressure outcome). Cites raw transcript.

4. ASSUMPTION TRACKER  (pilot/ASSUMPTION-TRACKER.md)
   - Maps evidence -> assumption status. Must cite raw transcript, NOT a summary (PR-2).
   - Authority on assumption STATUS; the evidence behind it traces to 1–3.

5. EVIDENCE LEDGER  (docs/Nidaa-A6b-Evidence-Ledger.md)
   - Canonical A6b formulation + engaged-contact index. Authority on A6b WORDING
     (canonical = W-C, per Nidaa-Day10-A6b-Canonical-v1.0.md) and on contact evidence state.

6. JOURNAL  (pilot/EVIDENCE-JOURNAL.md)
   - Running record of evidence events + audit series. Narrative/secondary. May summarize
     but never overrides 1–5. The Day-10 audit series is the journal-of-record.

7. BRIEFS / DAY LOGS  (docs/Nidaa-Day6-Brief.md, Nidaa-Day-Log-Template.md, etc.)
   - Operational status + decisions. LOWEST authority on evidence content; a brief mentioning
     a reply (e.g. Day-6 Brief L783 Hisem EVENT) is NOT evidence until ingested via 1–4.

==================================================================
CONFLICT RESOLUTION RULES
==================================================================
- Two artifacts disagree on WHAT A PRACTITIONER SAID -> raw transcript (1) wins.
- Two artifacts disagree on ASSUMPTION STATUS -> Assumption Tracker (4), traced to 1–3.
- Two artifacts disagree on A6b WORDING -> Evidence Ledger canonical block / canonical v1.0 (5).
- A brief (7) mentions a reply but no 1–4 artifact exists -> that is an INGESTION GAP (PR-1),
  not evidence. The reply is "replied in reality, Artifact Gap" until ingested.
- "No artifact" is a routing signal, NOT a conclusion about reality (Constitution).

==================================================================
PRIMARY-SOURCE PRINCIPLE (PR-2)
==================================================================
No assumption may cite a summary when a primary source (1) exists. Citations point to the
raw transcript, not a downstream summary. This hierarchy exists so that principle is
enforceable: the raw transcript is always the top of the chain.

==================================================================
WIRING
==================================================================
- Referenced from: Nidaa-Day6-Brief.md (NIDAA COMMAND ROUTING RULE section).
- Referenced from: Nidaa-Day10-Process-Rule-PR2.md (preservation).
- Companion: Nidaa-Day10-Process-Rule-PR1.md (ingestion). PR-1 (enter) + PR-2 (preserve) +
  this hierarchy = the full evidence-integrity governance.

END OF SOURCE-OF-TRUTH HIERARCHY.
