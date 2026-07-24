# Nidaa — Day 11 Pilot Definition (Experiment Design, NOT a Build Spec)

Type: PILOT DEFINITION (falsification experiment design). Created: 2026-07-22.
Author: Hermes (per director transition directive).
Companion: pilot/ASSUMPTION-TRACKER.md (Pilot Definition section), pilot/CURRENT-EVIDENCE-STATE.md.

==================================================================
0. TRANSITION STATEMENT (why this exists)
==================================================================
Director (2026-07-22): the A6-Trust Literature Campaign moved Nidaa from
"Interesting idea needing evidence" → "Evidence-backed hypothesis deserving a pilot."

Justification to BUILD a narrow pilot (NOT scale):
- Mones interview (org-side coordinator signal; A6b-strong branch)
- Aaron evidence
- Abdelrahman evidence
- Hisem evidence (OQ-2 coexistence, observation-only)
- A6-Trust Literature Campaign (21 cases; conditional support + disconfirming)
- G2 collapse campaign (21 cases; failure taxonomy)
- Existing coordination literature

Evidence-count discipline (explicit): these are NOT 21 practitioner responses. They are
3–4 practitioner data points + 2 literature campaigns + prior coordination literature.
Enough to BUILD a narrow pilot. NOT enough to scale. Literature cases are never counted as
practitioner responses.

A6-trust is now LOCKED: Conditional / Literature-Supported / Practitioner-Unverified.
G1 = OPEN. G2 = OPEN. No assumption promoted to conclusion.

==================================================================
1. THE EXPERIMENT QUESTION (the real A6b question)
==================================================================
> Can a locally legitimate coordinator maintain a structured board that others
> actually consult and update?

This is the load-bearing hypothesis. Everything below is designed to falsify or support it.
If a locally legitimate coordinator CAN maintain a consulted/updated board under realistic
friction, A6b (W-C) + A6-trust (conditional) are supported in practice. If they cannot, we
learn WHY (burden? verification? trust? consultation gap?) — and that failure mode maps to the
G2 taxonomy or the A6-Trust failure taxonomy.

==================================================================
2. SCOPE LOCK (smallest possible)
==================================================================
- NOT a full Nidaa platform. NOT a mesh/LoRa/CRDT/portal spec. (Frozen-scope architecture ban
  from tracker Guidance REMAINS in force for product/feature talk; this is experiment design.)
- Prototype surface: ONE board, ONE coordinator-owner, a small set of consulted actors.
- Duration: short, bounded (weeks, not months).
- Setting: one real coordinator context if obtainable; otherwise a realistic role-play/simulation
  with a practitioner acting as the coordinator (still yields behavioral signal, not opinion).
- Success metric = LEARNING whether the mechanism works, not shipping a product.

==================================================================
3. WHAT TO OBSERVE (not how to build it)
==================================================================
Variables to instrument (the friction axes from the campaigns):
- OWNER BURDEN (G2 Burnout / A6b "low-burden capture"): time-to-update per entry; does the
  coordinator sustain updates past the first week? (G2 Phase 3 key-person loss test.)
- VERIFICATION (A6-Trust anchor + A4): how does the coordinator mark info verified/unverified?
  Do consulted actors trust the verification marker? (C5/C6 workflow-as-anchor.)
- CONSULTATION (A6-trust "would others consult it?"): do other actors actually open/query the
  board when they need info, or fall back to calls/chats? (G2 Phase 4 fallback test.)
- TRUST ANCHOR (A6-Trust): is trust driven by the coordinator's LOCAL LEGITIMACY, or by the
  board's existence? If the coordinator is unknown, does consultation collapse? (C8/C19 disconfirming
  guard: source legitimacy > content.)
- MAINTENANCE (G2 Maintenance failure): does the board go stale after the acute phase? (Cases 4/15/16.)

==================================================================
4. HYPOTHESES TO FALSIFY (not confirm)
==================================================================
H1 (A6b-W-C): a coordinator with mandate + low-burden capture maintains the board through a stress event.
  - Falsifies if: board abandoned within days, or only updated when coerced, or others never consult it.
H2 (A6-trust conditional): others consult the board BECAUSE the coordinator is locally legitimate.
  - Falsifies if: board ignored despite correct info (C8), or only consulted when content is verified
    by an external brand, or consulted only by the coordinator's direct ties.
H3 (G2 guard): the structure survives longer than an unowned one.
  - Falsifies if: it collapses identically to the G2 cases despite having an owner (would indicate
    owner alone insufficient — refining A6b toward owner+continuity+verification).

==================================================================
5. RESPONSES REQUIRED
==================================================================
- To START building the pilot: ZERO additional practitioner responses (evidence base sufficient).
- To VALIDATE the pilot: 3–5 more practitioner conversations, ideally:
  (1) one coordinator,
  (2) one information-management person,
  (3) one grassroots/community actor.
  These supply the triangulation that turns the pilot's behavioral signal into evidence.

==================================================================
6. DAY 11 DIRECTION (locked)
==================================================================
1. A6-trust = Conditional / Literature-Supported / Practitioner-Unverified.  [DONE in tracker]
2. G1 = OPEN (loose-informal case still missing).                          [NO CHANGE]
3. G2 = OPEN (informal collapse case still missing; campaign saturated).    [NO CHANGE]
4. Obtain 1–3 more practitioner testimonies (toward the 3–5 validation set).
5. Begin defining the smallest possible pilot around the coordinator-maintained board hypothesis.
   [This artifact = that definition.]

==================================================================
7. NEXT STATE-CHANGE TRIGGERS
==================================================================
- A real coordinator stating they would/wouldn't maintain + consult such a board → moves A6-trust
  from Practitioner-Unverified toward Verified/Refuted.
- A pilot run producing behavioral data → feeds A6b (W-C) + A6-trust + G2 taxonomy.
- 3–5 validation conversations completing → unlocks pilot validation milestone.
- G1/G2 remain open until their respective first-hand statements arrive (see G2 campaign §8 / Day-10
  closure doc).

Discipline: literature ≠ practitioner response. Pilot = experiment. No assumption promoted.
==================================================================
END OF DAY 11 PILOT DEFINITION
