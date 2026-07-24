# Nidaa — Day 8 Hermes Skill & Resource Upgrade Review

Type: OPERATIONS SUPPORT / meta-review (Day 8). Does NOT perform outreach, discover
leads, conduct literature review, or modify project assumptions. Focus stage:
"Convert practitioner conversations into evidence."

Source inputs: skills_list (122 skills), nidaa/docs/* (17 files), nidaa/pilot/* (~40
files), Nidaa-Six-Questions.md, Nidaa-A6b-Evidence-Ledger.md, Day6-Brief.md, the
four Day 8 artifacts produced this session.

==================================================================
1. INVENTORY
==================================================================

--- 1A. EXISTING SKILLS USED FOR NIDAA (core) ---
- nidaa-load (software-development) — NIDAA-LOAD auto-routing skill; enforces
  artifact-first continuity before any Nidaa reasoning.
- evidence-first-continuity (research) — evidence-first continuity-artifact
  pattern (E/H/A/OQ split, source-of-truth artifact, anti-drift).
- evidence-lead-discovery (research) — find EVIDENCE-BEARING humans when the
  primary channel is blocked; "blocked method != completed objective."
- problem-validation (research) — falsification-mode discipline for early-stage
  hypotheses.
- research-synthesis (research) — honest literature synthesis (hypothesis-vs-proof
  framing, confidence grading, access-limit disclosure).
- terminal-web-research (research) — retrieve live sources via curl when
  web_search/web_extract are absent (used for Solnit + Stress-Test).
- hermes-agent-skill-authoring (software-development) — author/validate SKILL.md.
Available but NOT Nidaa-core: arxiv, verified-web-research, osint-investigation,
evidence-first-legal-research, research-fanout, llm-wiki, etc. (kept in reserve).

--- 1B. EXISTING RESOURCES ---
docs/ (continuity + analysis):
- Nidaa-Day6-Brief.md — SOURCE OF TRUTH (650+ lines, append-only addenda).
- Nidaa-A6b-Evidence-Ledger.md — A6b/G1/G2/OQ-1/OQ-2 scaffold + engaged contacts.
- Nidaa-A6b-Six-Questions.md — the ONLY script that can close G1/G2.
- Nidaa-A6b-Outreach-Dossier(-v2).md — exhausted-contact routing.
- Nidaa-A6b-Lead-Discovery-Report(-v2).md + Memo — lead discovery.
- Nidaa-Stress-Test-Memo.md — per-OQ disconfirming literature search (analysis).
- Nidaa-A6b-Solnit-Lit-Note.md + Edition-Verification.md — literature eval.
- Humanitarian-Coordination-Failure-Patterns.md — P1–P10 pattern map.
- Nidaa-PLAN.md — build roadmap (deferred; product phase).
- [Day 8 new] Dispatch-Audit, Referral-Register, Pipeline-Status, OQ2-Memo.
pilot/ (~40 files, operational layer):
- Evidence campaigns: A1-/A6-/A6b-/A6b-RESOLUTION-CAMPAIGN, A6-FIELD-LOG,
  A6-GRASSROOTS-HUNT.
- Outreach/contact: OUTREACH-LEDGER, OUTREACH-CONTACTS, CONTACT-STATUS,
  outreach-list, OUTREACH-TARGETS, first-touch-messages, AFTERNOON-SEND-PACKAGE.
- Assumption: ASSUMPTION-TRACKER, ASSUMPTION-NEXT-TESTER, PREDICTIONS.
- Intake/scoring: EVIDENCE-INTAKE-TEMPLATE, EVIDENCE-CONVERGENCE-SCOREBOARD.
- Prep: HISEM-WHITE-HELMETS-PREP, INTERVIEW-REPLY-PREP, target-acquisition/,
  A6B-TARGET-ACQUISITION.
- Governance: governance-playbook, do-no-harm, NIDAA-REDTEAM-CRITIQUE.
- Backlog/FAQ: pilot-readiness-backlog, RESEARCH-BACKLOG, NIDAA-FAQ-OVERVIEW,
  STAKEHOLDER-QUESTIONNAIRE, partner-brief, demo-script.

--- 1C. EXISTING TEMPLATES ---
- Six-Questions (gate script, verbatim).
- EVIDENCE-INTAKE-TEMPLATE (pilot) — exists but NOT wired to the ledger.
- ASSUMPTION-TRACKER format (pilot).
- first-touch-messages (outreach drafts).
- [Day 8 new] Dispatch-Audit / Referral-Register / Pipeline-Status (candidate
  recurring templates).

--- 1D. EXISTING OPERATIONAL WORKFLOWS ---
- NIDAA-LOAD routing rule (auto-load artifact before any Nidaa msg).
- E/H/A/OQ separation discipline.
- Six-Question gate (only mechanism that closes G1/G2).
- Stress-Test falsification (per-OQ disconfirming search).
- Day-log append (addendum to Day6-Brief).
- [Day 8 new] Dispatch-Audit; Referral-Register.

==================================================================
2. GAP ANALYSIS (six target capabilities)
==================================================================

(2.1) EVIDENCE MANAGEMENT — GAP: no normalized case record.
The Ledger is a monolithic scaffold mixing seed rows, engaged contacts, OQ-1/2,
and the Aaron-call-held note. EVIDENCE-INTAKE-TEMPLATE exists in pilot/ but is
NOT wired to the ledger. A six-question reply is currently pasted as freeform
markdown. No mandatory field set (source / org / case_type / formal-coexist
verdict / confidence / verbatim quotes / gate_status). Risk: G1/G2 evidence
drifts, convergence cannot be computed.

(2.2) PRACTITIONER INTERVIEW TRACKING — GAP: state is redundant + desynced.
Interview/gate state is spread across Ledger "ENGAGED CONTACTS", Day8
Pipeline-Status, pilot CONTACT-STATUS, and OUTREACH-CONTACTS. The Mohammed
desync (header "contacted" vs ledger "not yet contacted") is a symptom. No single
per-contact record of which of the six questions were answered and whether the
gate passed.

(2.3) REFERRAL TRACKING — GAP: no chain linkage / desync auto-flag.
Referral-Register just created (manual). No referrer→referred→contacted?→outcome
chain, and no automatic flag when a downstream fact contradicts the upstream
(e.g., a referral logged "contacted" while the ledger says "seed, not contacted").

(2.4) OUTREACH LEDGER MAINTENANCE — GAP: no enforced send-state; redundant files.
THREE+ outreach files (OUTREACH-LEDGER, OUTREACH-CONTACTS, CONTACT-STATUS) plus
the Ledger's ENGAGED block. The Day 8 Dispatch-Audit exposed "prepared but send
unconfirmed" (Steve/Ekzayez) — there is no send-state enum preventing "prepared"
from silently equalling "reached."

(2.5) ASSUMPTION-EVIDENCE LINKAGE — GAP: narrative, not machine-checkable.
ASSUMPTION-TRACKER + Ledger OQ-1/2 exist, but linkage is prose. No map:
assumption → required evidence type → which ledger rows satisfy it → auto
Open/Pressure/Resolved. Status changes depend on manual reinterpretation each load.

(2.6) DAY-LOG CONTINUITY — GAP: monolithic growth, no state-delta convention.
Day6-Brief is 650+ lines append-only; every NIDAA-LOAD re-reads the whole file;
desync risk compounds (Mohammed). No standardized daily state-delta or desync
register, so loads get slower and contradictions harder to spot.

==================================================================
3. PROPOSED ADDITIONS (categories A–E)
==================================================================

--- A. EVIDENCE OPERATIONS ---
A1. nidaa-evidence-intake (SKILL)
  Purpose: parse a six-question reply into a normalized G1/G2 case record; emit a
    ledger row with mandatory fields {source, org, role, case_type (G1/G2/other),
    formal_coexist_verdict, confidence, verbatim_quotes, gate_status}.
  Expected benefit: turns conversations→evidence consistently; no info lost in
    freeform; enables convergence scoring (A2).
  Complexity: Medium.

A2. nidaa-evidence-convergence (SKILL/RESOURCE)
  Purpose: given all G1/G2 rows, compute convergence (n independent sources
    agreeing, context-diverse) and auto-flip validation status at a defined
    threshold; emit disconfirming-evidence count.
  Expected benefit: replaces "I feel validated" with an objective threshold;
    exposes single-source bias (the Aaron n=1 risk).
  Complexity: Medium.

--- B. RESEARCH OPERATIONS ---
B1. nidaa-falsification-run (SKILL)
  Purpose: repeatable per-OQ disconfirming search (templated Stress-Test);
    outputs a pressure score + sourced list per OQ; appends (not overwrites) so
    pressure is tracked over time.
  Expected benefit: keeps confirmation bias in check per open question; comparable
    pressure scores across sessions.
  Complexity: Medium.

--- C. HUMANITARIAN CONTEXT ---
C1. nidaa-context-card (RESOURCE, one-pager)
  Purpose: reference for Gaza/oPt Health Cluster structure, OCHA cluster system,
    CCCM, Community Coordinator roles, and formal/coexist vocabulary.
  Expected benefit: lets a practitioner reply be correctly classified into an
    OQ-2 verdict (formal fail vs coexist/absorb) instead of mis-tagged.
  Complexity: Low.

--- D. REPOSITORY INTELLIGENCE ---
D1. nidaa-artifact-sync (SKILL)
  Purpose: lint Day6-Brief ↔ Evidence-Ledger ↔ Outreach-Ledger ↔
    Referral-Register ↔ Contact-Status for desync (e.g., "referral says
    contacted, ledger says seed"); report contradictions as a desync register.
  Expected benefit: auto-detects the Mohammed-style desync before it hardens;
    protects source-of-truth integrity.
  Complexity: Medium.

--- E. NIDAA PROJECT MEMORY ---
E1. nidaa-daylog-template (RESOURCE / TEMPLATE)  [seeded this session]
  Purpose: standardized daily log — E/H/A/OQ split, STATE-DELTA vs last load,
    dispatch-audit block, referral-delta, desync register.
  Expected benefit: faster NIDAA-LOADs, less monolithic growth, enforced
    structure; directly supports the current "convert conversations→evidence"
    stage.
  Complexity: Low.  (File: Nidaa-Day-Log-Template.md, written Day 8.)

E2. nidaa-state-snapshot (SKILL)
  Purpose: regenerate the one-page pipeline status + evidentiary score
    automatically from the ledger (like Day8 Pipeline-Status but scripted).
  Expected benefit: removes manual re-derivation; always consistent with ledger.
  Complexity: Medium.

==================================================================
4. PRIORITY RANKING
==================================================================
Ranked by: (1) immediate usefulness to Nidaa now, (2) long-term usefulness,
(3) effort required, (4) deliverable. Combined priority = immediate × long-term
÷ effort.

RANK | ID  | NAME                     | IMMED | LONG | EFFORT | DELIVERABLE
1    | E1  | nidaa-daylog-template    | High  | Med  | Low    | Template (DONE Day8)
2    | D1  | nidaa-artifact-sync      | High  | High | Medium | SKILL.md + linter
3    | A1  | nidaa-evidence-intake    | High  | High | Medium | SKILL.md + intake schema
4    | C1  | nidaa-context-card       | Med   | Med  | Low    | One-pager resource
5    | A2  | nidaa-evidence-convergence| Med  | High | Medium | SKILL.md + threshold
6    | B1  | nidaa-falsification-run  | Med   | Med-H| Medium | SKILL.md (templated)
7    | E2  | nidaa-state-snapshot     | Med   | Med  | Medium | SKILL.md (scripted)

Rationale: E1 first because it is Low effort and prevents the exact desync/load-
bloat we hit today. D1 and A1 next — they directly serve "convert conversations→
evidence" and fix the two most damaging gaps (desync detection, normalized intake).
C1 is a quick classification win. A2/B1 pay off once cases exist / periodically.
E2 is automation comfort, deferrable until the manual process is stable.

==================================================================
5. KEEP / IMPROVE / ADD / DEFER MEMO
==================================================================

KEEP (working, do not disturb):
- nidaa-load routing rule + evidence-first-continuity + E/H/A/OQ discipline.
- Six-Questions gate (the only G1/G2 closer).
- Stress-Test falsification method.
- terminal-web-research (source retrieval on the filtered host).

IMPROVE (refactor existing, no new assumption):
- Split Evidence-Ledger into normalized case records; stop mixing seed/engaged/
  OQ/Aaron-call in one table.
- Collapse OUTREACH-LEDGER + OUTREACH-CONTACTS + CONTACT-STATUS + Ledger ENGAGED
  into ONE dispatch-verified ledger.
- Add a mandatory send-state enum (prepared / sent-unconfirmed / sent-verified /
  bounced / replied) so "prepared" can NEVER imply "reached" (closes the
  Steve/Ekzayez dispatch leak).

ADD (the A–E list above, build order per Section 4):
- E1 (done Day 8) → D1 → A1 → C1 → A2 → B1 → E2.

DEFER (explicitly OUT of scope for this stage — not evidence-acquisition):
- Product/architecture build skills (offline-first-pwa already exists; no new
  build skills needed now).
- Lead discovery / outreach automation / new-target generation (blocked by the
  Day 8 task constraints and not evidence-acquisition).
- Pilot-readiness / demo-video / partner-brief tooling (product adoption, not
  evidence).
- Multi-region, auth, sync, conflict-resolution (product development phase).

No project assumptions modified. No outreach, discovery, or literature work
performed. Review is ops/meta only.
