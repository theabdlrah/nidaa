# Nidaa — Assumption Tracker & Post-Conversation Process

**Purpose:** prevent rationalizing feedback. We are collecting *evidence*, not
testimonials. The first five conversations are an attempt to **falsify** Nidaa's
core thesis, not validate it.

**Rule:** Update this tracker after EVERY conversation, *before* discussing next
steps. Do not write "they liked it," "interesting conversation," or "positive
meeting." Write what the evidence did to each assumption.

---

## The 7 Core Assumptions

Status vocabulary: `Untested` · `Strengthened` · `Weakened` · `Falsified`
Confidence: `High` · `Medium` · `Low`

### Two-dimensional confidence rule (governing, 2026-07-24)
Distinguish two separate dimensions — do NOT conflate them:
1. **Evidence quality** — how trustworthy THIS piece of evidence is (named? original-language
   primary source? verbatim archived? audit trail preserved?). A single high-quality source
   can score High on evidence quality.
2. **Hypothesis confidence** — how strongly the OVERALL assumption/hypothesis is supported,
   which depends on the QUANTITY, INDEPENDENCE, and DIVERSITY of evidence, not just one source's
   quality. Improving one source's quality raises that source's evidence-quality, but does NOT
   by itself raise hypothesis confidence to the same degree.
Application (Day 12): Omar Ghazal's transcript = High evidence quality (named + original Arabic
+ verbatim + audit trail). G1/G2 records = High-quality evidence (n=1). A2 = High because it is
STRONGLY SUPPORTED via MULTIPLE independent sources (Adam E., Abdelrahman S., Omar, + Mones on
related points) — diversity-based, not a source-quality carry-over. A6b = Medium–High overall:
strong convergence (Mones formal + Omar community/informal) but rests on a limited number of
independent practitioners; awaiting broader replication / operational validation. This rule
prevents auto-promoting a hypothesis when only source quality improved.

### Standard decision process for every new piece of evidence (applies the rule)
Evaluate each incoming evidence item with this same sequence — do not skip steps:
1. **Did this improve the quality of an existing source?** If yes → upgrade the
   EVIDENCE QUALITY of that source/record (e.g., named, original-language, verbatim,
   audit trail). This does NOT by itself change hypothesis confidence.
2. **Did this add an independent line of corroboration or contradiction?** If yes →
   consider whether HYPOTHESIS CONFIDENCE should change (more/independent/diverse
   corroboration raises it; a practitioner critique or disconfirming case tests it).
3. **Has operational validation occurred?** If yes → may justify a further increase
   in hypothesis confidence beyond practitioner testimony alone (e.g., a dated
   operational case study where the mechanisms clearly succeeded or failed).
Record which step(s) applied in the evidence journal entry so any future reviewer
can reproduce WHY a confidence moved (or did not).

| # | Assumption | Evidence For | Evidence Against | Confidence | Status |
|---|------------|--------------|-----------------|------------|--------|
| 1 | Coordination is a priority problem. | MSF coord. (Mones, 2026-07-17): "Information sharing is one of the most important elements of operational success" + daily cross-dept/external coordination with named owners. | — | Medium | Strengthened |
| 2 | Information/matching is a significant bottleneck. | Resident interview (Adam E., 2026-07-14): info access depends on connectivity; outage cut family's access to food-distribution info. | Omar Ghazal (2026-07-24, named practitioner, original Arabic + translation): "the main challenge is not communication itself, but organizing the flow of information, verifying it, defining responsibilities" — bottleneck is info FLOW/VERIFY, not mere exchange. Independent of Mones. | High | Strengthened |
| 3 | Offline capability materially matters. | Resident interview (Adam E., 2026-07-14): connectivity outages cut access to aid info AND digital payments/transfers; incumbent tools' failure mode is connectivity itself. | — | Medium | Strengthened |
| 4 | Verification materially matters. | MSF coord. (Mones, 2026-07-17): "we rely on verifying information from trusted and specific sources before adopting or sharing it." | — | Medium | Strengthened |
| 5 | Existing tools are insufficient for at least some communities. | Resident interview (Adam E., 2026-07-14): WhatsApp/Telegram/FB work only when connectivity exists; they fail exactly during outages, when needed most. | — | Medium | Strengthened |
| 6 | Organizations would trust designated verifiers. | MSF (Mones, 2026-07-17): structured, owned, tooled coordination w/ satellite backup that survives outages; explicit verify-from-trusted-sources behavior. Strengthens OWNER/MANDATE branch only. Omar Ghazal (2026-07-24, named practitioner, original Arabic + translation): initiatives work "when they have trusted individuals, clearly defined roles, direct communication channels with the relevant institutions, and a simple mechanism for verifying and updating information" — second NAMED, different-background source describing the SAME owner/verify precondition (convergence with Mones). [Refined 2026-07-24:
 both independently identify structured information management—clear ownership,
 verification, defined responsibilities, and institutional linkage—as central to
 effective coordination despite operating in different humanitarian contexts.] | Loose-informal branch (G2) NOW PRESENT at pattern level (2026-07-24, Omar Ghazal — named practitioner): collapse occurred exactly where owner/mandate + docs ABSENT (single-person reliance, weak documentation, conflicting info, burnout). First real G2, from a named source. | Medium-High | Strengthened (conditional) |
| 7 | Communities would adopt a new workflow if it solved the problem. | MSF coord. (Mones, 2026-07-17): active use of Teams/Google Earth/internal IM/WhatsApp/Telegram = coordinators DO adopt tooled workflows (A7a). | A7b (beneficiary adoption) still untested. | Medium | Strengthened (A7a) |

---

## Pivot Rule (do not ignore)

If assumptions **1, 2, or 5** are **strongly falsified by multiple
conversations**, we must explicitly consider one of:

- **Pivot** — redirect the problem we're solving.
- **Narrow scope** — target a smaller, verified sub-problem.
- **Stop** — discontinue Nidaa before further investment.

This is a hard gate, not a suggestion. Falsification is success — it saves us
from building the wrong thing.

---

## Post-Conversation Template (complete after EVERY interview)

Copy the block below per conversation. File naming:
`pilot/assumption-log/<ORG>-<DATE>.md` (e.g. `SameerProject-2026-07-20.md`).

```
### Conversation: <ORG / ROLE> — <DATE>

1. What problem did they describe?
   -

2. What tools do they currently use?
   -

3. What failed recently?
   -

4. Was the bottleneck information, verification, coordination, logistics,
   supply, trust, or something else?
   -

5. Would Nidaa have helped?
   -

6. Why?
   -

7. Why not?
   -

8. What assumption took the biggest hit?
   -

--- EVIDENCE LEDGER (required) ---

For each assumption that was touched, record the evidence and update the
tracker table above. Do NOT write impressions; write what was said/observed.

- Assumptions tested this conversation:
- Assumptions strengthened (with the specific evidence):
- Assumptions weakened (with the specific evidence):
- Assumptions falsified (with the specific evidence):
- What surprised us (something we did not predict):
- What should change because of this evidence:

```

---

## How to update the tracker (process)

After pasting the template and filling the Evidence Ledger:

1. For each assumption referenced, add the concrete evidence to `Evidence For`
   and/or `Evidence Against`.
2. Set `Status`:
   - new supporting evidence with no contrary → `Strengthened`
   - new contrary evidence → `Weakened`
   - contrary evidence strong enough to reject the assumption → `Falsified`
   - no new evidence → leave as `Untested`
3. Set `Confidence` based on cumulative evidence (not hope).
4. Re-check the **Pivot Rule** against assumptions 1, 2, 5.
5. Only THEN discuss next steps.

---

## Conversation index (log of completed interviews)

| # | Org / Role | Date | A1 | A2 | A5 | Biggest-hit assumption | Pivot triggered? |
|---|------------|------|----|----|----|------------------------|------------------|
| 1 | Adam Elijilah (Resident) | 2026-07-14 | U | S | S | A3 (offline = connectivity failure mode) | no |
| 2 | Mones (MSF Field Coordinator Support, Gaza) | 2026-07-17 | S | S | S | A6b owner-branch / A4 (verification behavior) | no |
| 3 | Omar Ghazal (named practitioner, Gaza, translated, relayed) | 2026-07-24 | S | S | S | A2 (bottleneck = info flow/verify) + FIRST NAMED G1+G2 material; convergence with Mones | no |

(A1/A2/A5 = status of those assumptions after the call: S=Strengthened,
W=Weakened, F=Falsified, U=Untested. "Pivot triggered?" = yes only if the Pivot
Rule fired.)

---

## Working Hypothesis (NOT a conclusion)

**New hypothesis (2026-07-15, post red-team + tool research):** Nidaa may be a
*coordinator-led information-management and coordination tool* rather than a
*civilian-first platform*. The morning's tool research (Ushahidi→deployment owner,
HOTOSM→validators, ReliefWeb→OCHA editors, HDX→org data managers) showed mature
systems always have an owner. A7 split into A7a (coordinators publish — now less
risky) and A7b (beneficiaries use — still untested). This points the primary user at
the coordinator / info officer, not the lone beneficiary.

Treat this strictly as a hypothesis. It is falsifiable by the conversations below, not
settled by the research. Reality still gets the vote.

---

## Potential Failure Modes

| # | Failure mode | Current evidence | Confidence | Next person/org to test | Strengthens if… | Falsifies if… |
|---|--------------|------------------|------------|-------------------------|-----------------|---------------|
| F1 | Coordinator overload / lack of administrative bandwidth | None direct. Adam (resident) noted aid info is pushed to phones, implying someone already pushes — but no org-side bandwidth data yet. | Low | Ops/coordination leads at Sameer, White Helmets, ERRs, REACH | A coordinator says "yes we'd post, but we have no one free to maintain it" or describes an existing system collapsing under admin load | A coordinator says maintaining the board is trivial vs their current load, or already staffs an info focal point with spare capacity |
| F2 | Coordination is not actually a top-priority operational problem | None. Adam did NOT raise coordination as a top pain — he described info-access during outages (A2/A3). A1 still Untested. | Low | Field/ops coordinators; ask "is coordination even a priority vs fuel/access/security?" | Orgs rank coordination below supply/access/security consistently; "coordination is fine, X is the real problem" | Orgs name coordination as a top-3 pain; recent incident where coordination failure had visible cost |
| F3 | Organizations reject decentralized information (verification / liability / governance) | None direct. HOTOSM validates mapping work (suggests orgs accept designated verifiers), but aid-info truth/liability is different. | Low | MAP, Al-Haq, PCRF, White Helmets (orgs with hierarchy + liability exposure) | Org refuses to post into a shared board citing liability, false-info harm, or "we control our own comms" | Org already shares unvetted info openly and welcomes a verifier role |
| F4 | Civilians do not access or trust the resulting information | None. A7b entirely untested. Adam used WhatsApp/Telegram push — suggests civilians expect info pushed, not pulled from a board. | Low | Beneficiary-adjacent voices (We Are Not Numbers, resident referrals); observe actual info-seeking behavior | Beneficiaries say they never open such boards / rely solely on WhatsApp forwards / distrust unknown sources | Beneficiaries already use a similar board or actively seek centralized info |
| F5 | Structured workflows (Requested → Claimed → Fulfilled) do not match real field behavior | None. This workflow is an untested design assumption, not observed behavior. | Low | Ops coordinators who run aid matching today (Sameer, ERRs, mutual-aid) | Coordinator says "we don't work in request/claim/fulfil stages, it's X" or the stages don't map to how aid is actually allocated | Coordinator says "yes, that's exactly our pipeline" or already uses a near-identical staged workflow |

---

## Interview Objective Shift

Do **not** use future conversations to validate Nidaa. Use them to **falsify** these
assumptions (and A1/A6/A7). The goal is to discover whether the thesis survives
contact with reality — not to confirm it.

For Omar, Shaima, and future contacts, prioritize **behavioral evidence over opinions**.

Prefer:
- "Tell me about the last time…"
- "What actually happened?"
- "Who did you contact?"
- "How did information move?"
- "What did you do when the plan failed?"

Avoid:
- "Would you use Nidaa?"
- "Do you like this idea?"
- Feature discussions.

---

## Highest Priority Unknowns

1. Do coordinators already maintain structured information during operations?
2. Is coordination / information flow a top-tier operational pain point, or are
   fuel, access, security, and logistics overwhelmingly dominant?
3. Who actually owns information in the field today?
4. What happens during the worst communication breakdowns?
5. How do organizations currently verify and trust information?

---

## Guidance (frozen scope)

- **Freeze all new architecture discussions** (mesh, LoRa, CRDTs, civilian portals,
  etc.) until evidence from organization-level conversations arrives.
- The current bottleneck is **not** technical uncertainty. It is **lack of field
  evidence**.
- Success metric unchanged: obtain organization-level evidence that either
  **strengthens or weakens A1, A6, and A7**.
- Next conversations aim to falsify, not confirm. The thesis survives only if reality
  does not kill it.
