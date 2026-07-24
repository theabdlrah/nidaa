# Nidaa — Process Rule PR-1 (Day 10 evidence-pipeline fix)

Type: PROCESS RULE (Day 10 deliverable). Source of truth for evidence ingestion.
Triggered by: the Hisem incident — a substantive practitioner reply existed in reality
(LinkedIn transcript reported with M&E Dept / KoboToolbox / data triangulation / hard-to-
reach answers) but was NEVER written into any project artifact, so the evidence system
showed "Awaiting Response" while reality was "Replied." Day-10 Reply-Classification Audit
and the user's closeout both identified this as the single most valuable Day-10 finding:
a reply can exist in reality and still fail to enter the source of truth.

This rule converts a one-off ingestion failure into a permanent pipeline improvement.
It is a PROCESS rule, not evidence, not an assumption. No A6b/G1/G2 status changes.

==================================================================
PROCESS RULE PR-1 — SAME-SESSION INGESTION
==================================================================

Any practitioner reply received via LinkedIn, email, screenshot, paste, export, or chat
log MUST be converted into an evidence artifact during the SAME session it is received.

A reply is NOT considered ingested until it exists in ALL of:
  1. EVIDENCE INTAKE — logged via EVIDENCE-INTAKE-TEMPLATE.md (verbatim quote/story/fact,
     source, path, consumer, bottleneck, workaround).
  2. FIELD LOG — an A6-FIELD-LOG.md row (if it bears on A6b / the six questions), tagged
     Reality A or B, with the owner/mandate condition and pressure-event outcome.
  3. ASSUMPTION TRACKER — ASSUMPTION-TRACKER.md updated (if the reply touches any
     assumption), with the specific evidence and a status change per the rubric.

If a reply arrives but cannot be fully processed that session (e.g. needs the six-question
follow-up), it MUST still be (a) recorded in the Evidence Ledger / CONTACT-STATUS as
"Received — pending intake" and (b) written to a raw artifact (paste the transcript into a
dated file under pilot/assumption-log/ or docs/) so it is never lost to conversation history.

PROHIBITED:
- Recording "Awaiting Response" in any artifact while a real reply exists only outside the
  files. Absence of an artifact is a routing signal, not a conclusion (Day-6 Constitution).
- Treating a pasted/recalled/exported reply as "documented" without a file artifact. A reply
  in chat is NOT ingested.
- Closing a session with a known reply un-filed.

THE SIX-LAYER TRACE TEST (detection criterion for ingestion failure)
------------------------------------------------------------------
Per Nidaa conventions, a normally-processed practitioner reply leaves a trace in ALL of
these layers. Absence across ALL of them is the signature of an ingestion failure (not a
classification error — a misclassification would still leave a trace in at least one layer):

  1. BRIEF layer      — status flips out of "Awaiting" in CONTACT-STATUS / Day-8 Pipeline /
                        Evidence Ledger engaged row.
  2. EVIDENCE layer   — an EVIDENCE-INTAKE record (verbatim quote/story/fact).
  3. FIELD-LOG layer  — an A6-FIELD-LOG row (Reality A/B, owner/mandate, pressure outcome).
  4. ASSUMPTION layer — at least one ASSUMPTION-TRACKER row touched (e.g. A6b / A4).
  5. LEDGER layer     — a citation from the engaged-contact row.
  6. JOURNAL layer    — a milestone/lesson mention.

HISEM CASE (Day 10 finding): ZERO of the six traces exist.
- No transcript file anywhere in the tree (full-file inventory: none).
- No evidence-intake record.
- No field-log row.
- No assumption-tracker note.
- No journal mention.
- No ledger citation beyond "awaiting response."
- Hisem-specific strings (Kobo / triangulation / hard-to-reach / M&E) appear ONLY in the
  Day-10 audit + Day-6 brief, never in a reply artifact.
Conclusion: the total absence across all six layers proves the response never entered the
pipeline — an INGESTION FAILURE, not a classification issue. This is exactly what PR-1 fixes.
If a future reply shows the same zero-trace pattern, treat it as the same class of failure
and locate/ingest before any status conclusion.

WHY THIS MATTERS (the actual Day 10 lesson)
------------------------------------------------------------------
"A reply can exist in reality and still fail to enter the source of truth." The Hisem
incident is valuable precisely because the pipeline left no trace of it — that silence is
the signal that exposed the weakness. PR-1 converts the silence into a standing control.
- Hisem Derviş = ARTIFACT GAP. The reported LinkedIn transcript must be located and ingested
  before any A6b/Hisem state is finalized. Until then Hisem is "Received — pending intake,"
  never "Awaiting Response."
- A standing search at session start for un-ingested replies: grep the tree for reply
  signatures (KoboToolbox, triangulation, hard-to-reach, transcript markers) and for any
  paste/export file not referenced by an evidence artifact.

==================================================================
WHERE PR-1 LIVES (governance wiring)
==================================================================
- Referenced from: Nidaa-Day6-Brief.md (NIDAA COMMAND ROUTING RULE section + Operating
  Constitution) as a standing process rule.
- Referenced from: docs/Nidaa-A6b-Evidence-Ledger.md "HOW TO FILL" block.
- Companion audit: docs/Nidaa-Day10-Reply-Classification-Audit.md (Hisem = Artifact Gap).

==================================================================
DAY 10 RESIDUAL INGESTION SWEEP (rigor check, 2026-07-22)
==================================================================
Full-tree scan performed before declaring Day 10 complete:
- Inventory: all non-node_modules files under C:\Users\theab\nidaa enumerated. No stray
  transcript / export / paste files outside the known logs exist.
- Recursive grep for Hisem reply signatures (Kobo / triangulation / hard-to-reach /
  Monitoring and Evaluation): hits ONLY in the Day-10 audit, the Day-6 brief, and unrelated
  research-day5 literature HTML — never in a standalone Hisem reply artifact.
- Conclusion: the Hisem reply is confirmed absent from the source of truth (ingestion
  failure real). No OTHER un-ingested practitioner reply was found in the tree.

DAY 10 STATUS: COMPLETE AND SUCCESSFUL (per user closeout).
- No new assumptions. No feature drift. Better evidence integrity. One process
  vulnerability (ingestion failure) identified and mitigated by PR-1.
- Next meaningful movement depends on incoming testimony — especially anything that moves
  G2 (informal collapse) or supplies a genuine loose-informal coordination case.

END OF PR-1.
