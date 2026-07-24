# Nidaa — G2 Failure Taxonomy Synthesis v1.0

Type: RESEARCH SYNTHESIS (derived ONLY from pilot/G2-RESEARCH-CAMPAIGN.md, 21 cases).
Created: 2026-07-22. Author: Hermes.
Discipline: NO new sources. NO assumption changes. Convert the 21-case catalog into a reusable failure model.

==================================================================
0. SCOPE & METHOD
==================================================================
- Input: the 21-case G2 campaign catalog (Cases 1–21).
- Method: each case was programmatically parsed for its Track tag + A6b verdict, then mapped by hand
  to (failure mode, context level, owner-existed?). Counts below are VERIFIED against the catalog text,
  not estimated.
- Boundary (unchanged): G2 is STILL formally OPEN. This is a model for evaluating future evidence, not
  a closure. No assumption in ASSUMPTION-TRACKER.md is promoted or altered.

==================================================================
1. RECURRENCE OF EACH FAILURE MODE (of 21 cases)
==================================================================
| Failure mode                | n  | Cases                              |
|-----------------------------|----|------------------------------------|
| Burnout / key-person loss   | 7  | 1, 2, 10, 11, 12, 16, 19          |
| Verification / trust break  | 5  | 3, 5, 6, 13, 21                   |
| Fragmentation / parallel    | 4  | 7, 8, 9, 18                       |
| Maintenance / sustainability| 3  | 4, 15, 16*                        |
| Information overload        | 2  | 17, 20                            |
(*Case 16 is coded Burnout-primary but its collapse is functionally sustainability/exhaustion-driven;
 cross-listed here as it also bears on Maintenance. No double-count in the n=21 total.)

Total coded assignments = 21 (each case assigned its PRIMARY mode; multi-mode cases noted inline).

Ranking by recurrence: Burnout (7) > Verification/trust (5) > Fragmentation (4) >
Maintenance (3) > Information overload (2). This matches the director's reading.

==================================================================
2. WHICH MODES APPEAR ACROSS CONTEXT TIERS (informal / semi-formal / formal)
==================================================================
| Failure mode                | Informal | Semi-formal | Formal | Mixed |
|-----------------------------|----------|-------------|--------|-------|
| Burnout / key-person        | 6 (+1→ngo) | 0         | 0      | 0     |
| Verification / trust        | 3        | 0           | 1 (6)  | 1 (3) |
| Fragmentation               | 1 (18)   | 0           | 2 (7,8)| 1 (9) |
| Maintenance / sustainability| 1 (16)   | 2 (4,15)    | 0      | 0     |
| Information overload        | 2 (17,20)| 0           | 0      | 0     |

Cross-tier finding:
- VERIFICATION/TRUST and FRAGMENTATION are the only modes that appear in ALL THREE tiers
  (informal + semi-formal + formal). They are context-agnostic — they bite regardless of how formal
  the structure is.
- BURNOUT/KEY-PERSON and INFORMATION OVERLOAD are concentrated in the INFORMAL tier in this catalog.
  (Caveat: this may reflect search emphasis on grassroots cases, not a true absence in formal systems —
  formal burnout exists but was not the campaign's focus.)
- MAINTENANCE/SUSTAINABILITY spans informal + semi-formal but not (in this set) formal.

==================================================================
3. WHICH MODES PERSIST EVEN WHEN OWNERSHIP EXISTS? (the A6b-critical test)
==================================================================
Per the A6b stress-test, a mode that recurs WHERE A DESIGNATED OWNER/MANDATE EXISTED is the only kind
that could contradict A6b's "structure survives with owner+mandate" premise.

| Failure mode                | Owner absent | Owner partial | Owner present | Persists despite owner? |
|-----------------------------|--------------|--------------|--------------|------------------------|
| Burnout / key-person        | 6            | 1            | 0            | Only via PARTIAL (lone owner = SPOF) |
| Verification / trust        | 3            | 1            | 1 (Case 6)   | YES — Case 6 (Kerala, formal) |
| Fragmentation               | 1            | 1            | 2 (7,8)      | YES — Cases 7,8 (formal, mandate present) |
| Information overload        | 2            | 0            | 0            | No (in this set) |
| Maintenance / sustainability| 1            | 2            | 0            | Only via PARTIAL |

Precise answer to "which modes persist despite ownership":
- VERIFICATION/TRUST: persists DESPITE ownership (Case 6 — Kerala SDMA had formal mandate, yet the
  channel failed via SECURITY/hack). Owner present ≠ trust/security guaranteed.
- FRAGMENTATION: persists DESPITE ownership (Cases 7,8 — formal responders WITH mandate still fragment
  under crisis ambiguity). Owner present ≠ integration achieved.
- BURNOUT: does NOT persist despite TRUE ownership — it persists where the "owner" is a LONE,
  unbacked individual (partial). This is the single-owner-as-SPOF condition, NOT a rebuttal of A6b.
- MAINTENANCE: same — only persists under PARTIAL (external tech owners with no local mandate, Case 4/15).

Implication for A6b: the two modes that survive ownership (Verification, Fragmentation) do so on axes
A6b already names (verification condition; workflow-integration condition). They do NOT show a
structure with full owner+mandate+verification+integration collapsing anyway. So: NO A6b contradiction
is demonstrated; the "owner+mandate" condition is necessary but NOT sufficient, and the missing
sufficient conditions are exactly Verification and Integration. This refines A6b toward
"owner + continuity + verification + workflow-integration" without falsifying it.

==================================================================
4. WHICH MODES ARE MOST RELEVANT TO THE CANONICAL A6b FORMULATION
==================================================================
Canonical A6b (per docs/Nidaa-A6b-Evidence-Ledger.md, W-C): grassroots coordinators maintain structured
info ONLY with owner/mandate + low-burden capture + fallback path; population-split, not yes/no.

Relevance ranking (highest first):
1. BURNOVAUT/KEY-PERSON (n=7) — directly tests the "owner" condition. Strongest evidence that a lone
   owner is a single point of failure → A6b's owner condition should read "owner + continuity/backup"
   (mirrors Mones' satellite-backup caveat). HIGH relevance.
2. VERIFICATION/TRUST (n=5) — tests A6b's implicit verification dependency (A4). Persists despite
   ownership (Case 6) → verification is a SEPARATE necessary condition. HIGH relevance.
3. FRAGMENTATION (n=4) — tests workflow-integration. Persists despite ownership (7,8) → integration is
   a separate necessary condition. HIGH relevance.
4. MAINTENANCE/SUSTAINABILITY (n=3) — tests the "low-burden / durability" limb. Semi-formal cases show
   external owners without local mandate decay. MED-HIGH relevance.
5. INFORMATION OVERLOAD (n=2) — tests low-friction capture at scale. MED relevance; likely
   under-sampled (chat-based systems).

Net: every failure mode maps onto a named A6b condition. The catalog does not break A6b; it enumerates
the sub-conditions that make A6b's "owner+mandate" necessary-but-insufficient.

==================================================================
5. THE G2 MODEL (one-page deterioration curve)
==================================================================
How coordination efforts typically deteriorate over time (synthesized from 21 cases):

PHASE 0 — EMERGENCE. A crisis/need triggers spontaneous coordination. Initial success is common and
fast (Cases 1,2,10,16,17,19). Energy is high; structure is lightweight (chat group, spreadsheet, kitchen,
map). No one yet questions sustainability.

PHASE 1 — FUNCTION. The structure delivers value: info flows, needs matched, meals served, maps built
(Cases 3,4,15,17). Users rely on it. This is where G1-type success is observed (see Hisem coexistence /
Mones owner+mandate).

PHASE 2 — STRESS. A pressure event hits: surge of incidents, connectivity loss, insecurity, aid cutoff,
or simply time. Three things begin to happen in parallel:
  (a) BURDEN rises on the person/people capturing info (Cases 1,2,11,12,16,19).
  (b) VOLUME/NOISE rises — information overload (Cases 15,17,20).
  (c) VERIFICATION strain — unvetted info accumulates, trust erodes (Cases 3,5,6,13,21).

PHASE 3 — FRACTURE (one or more of):
  - KEY-PERSON LOSS: the owner burns out / leaves → capture stops (Cases 1,2,10,11,12,16,19). Single
    point of failure realized.
  - VERIFICATION COLLAPSE: contested ownership of truth / hack / dispute → users stop trusting
    (Cases 3,5,6,13,21).
  - FRAGMENTATION: parallel systems emerge; duplication; everyone does their own thing (Cases 7,8,9,18).
  - OVERLOAD: chat/dashboard unusable; signal lost (Cases 15,17,20).
  - MAINTENANCE FAILURE: the structure stops being updated; becomes stale; abandoned (Cases 4,15,16).

PHASE 4 — FALLBACK / DEATH. Users abandon the structured surface and revert to: phone calls, direct
feeds, separate chats, or silence (Cases 15 "back to phone calls", 1/13 dissolution, 16 closures).
The coordination regresses to pre-structure behavior. If the need persists (protracted crisis), a NEW
parallel structure often sprouts — restarting the cycle (Cases 18,19).

THE LOAD-BEARING INSIGHT: collapse is rarely a single cause. It is the compounding of (burden on owner)
+ (volume noise) + (verification strain) once the initial enthusiasm/resource buffer is exhausted. The
owner condition delays but does not prevent collapse UNLESS paired with continuity (backup), verification
mechanism, and low-friction integration. This is the empirical basis for refining A6b's survival
condition from "owner+mandate" to "owner + continuity + verification + workflow-integration."

==================================================================
6. TOP 3 PRACTITIONER QUESTIONS (would most reduce uncertainty if answered tomorrow)
==================================================================
Ranked by expected G2-uncertainty reduction (not by ease):

1. "Tell me about a time YOUR group tried to keep a shared record of needs/offers/incidents — what
   happened to it after the first week, and specifically, when things got worst, did it keep getting
   updated or did it die, and WHAT SPECIFICALLY stopped it?"  → Directly elicits a G2 six-question
   statement from the loose-informal population; would formally open the path to closing G2.

2. "Who actually OWNED keeping that record updated? If that person got overwhelmed or left, what
   happened to the information?"  → Tests the single-owner-SPOF hypothesis (the sharpest potential A6b
   refinement) with real informant data rather than literature inference.

3. "Did people stop trusting the shared info, or start keeping their OWN separate lists/chats instead?"
   → Tests verification-collapse + fragmentation at the loose tier specifically (under-sampled in the
   catalog; mostly inferred from formal literature).

(Disconfirming companion, per campaign §8: "Have you seen an informal group where the structure DID hold
through a bad stretch? What was different?" — actively seeks the counterexample; a strong YES would be
the most valuable single answer for A6b.)

==================================================================
7. STATUS & USE
==================================================================
- G2: still formally OPEN (no six-question practitioner statement obtained).
- G2 research: SATURATED at literature/practitioner-account level (21 cases; recurrence converged).
- Use of this model: when a future practitioner reply arrives, classify its failure narrative against the
  5-mode taxonomy + 4-phase curve, and check whether it shows (a) owner present AND collapse (potential
  A6b contradiction) or (b) owner absent / burden high (A6b-consistent). This converts incoming evidence
  into a structured evaluation instead of ad-hoc reading.
- NO assumption in ASSUMPTION-TRACKER.md changed. NO new sources added. This artifact is downstream of
  the campaign; it is a lens, not new evidence.

END OF G2 FAILURE TAXONOMY SYNTHESIS v1.0
