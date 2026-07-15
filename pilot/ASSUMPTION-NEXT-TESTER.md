# Nidaa — Assumption Table: Evidence · Confidence · Next Tester

**Purpose:** make knowledge gaps obvious at a glance. Pair with ASSUMPTION-TRACKER.md
(the ledger of movement). This table says WHERE we are and WHO should move each
assumption next. It is updated after every conversation and when the pipeline changes.

Status vocabulary: `Untested` · `Strengthened` · `Weakened` · `Falsified`
Confidence: `High` · `Medium` · `Low`

| # | Assumption | Evidence so far | Confidence | Next person / role to test |
|---|------------|----------------|------------|----------------------------|
| A1 | Coordination is a priority problem | None yet. Resident (Adam) did not raise coordination as a top pain — he described info-access during outages (A2/A3). | Low | **Ops/field coordinator at an NGO** (Sameer Project, White Helmets, Sudan Relief Fund, REACH). Someone whose job IS coordination. |
| A2 | Information/matching is a significant bottleneck | Adam (resident): info access depends on connectivity; outage cut a family's access to food-distribution info. | Medium (1 resident) | **PMER / MEAL officer** (iMMAP, REACH, ACAPS) — they measure whether people get the right info. Plus a 2nd resident/org. |
| A3 | Offline capability materially matters | Adam (resident): outages cut aid info AND digital payments; incumbent tools' failure mode IS connectivity loss. | Medium (1 resident) | **Field/ops staff** (White Helmets, ERRs, HOTOSM volunteer) — do they experience the same outage failure modes, or different ones? |
| A4 | Verification materially matters | None yet. | Low | **MEAL / verification lead** (iMMAP, REACH, MAP, Al-Haq) — who confirms "this is real" today, and does a mark change behavior? |
| A5 | Existing tools insufficient for some communities | Adam (resident): WhatsApp/Telegram/FB work only with connectivity; fail during outages. | Medium (1 resident) | **Community-led groups** (White Helmets, ERRs, mutual-aid) — are current tools "good enough" or is there a real gap? |
| A6 | Organizations would trust designated verifiers | None yet. | Low | **Org with a hierarchy** (MAP, Al-Haq, PCRF, White Helmets) — name a person/body they'd accept as verifier, or reject the concept. |
| A7 | Communities would adopt a new workflow | None yet. Adam raised the publishing-step doubt (Nidaa only helps if info is posted in first). | Low | Split into A7a/A7b below. |

### A7 split — the morning's key thesis shift

Research into mature tools (see COORDINATION-TOOLS-RESEARCH.md) reframed A7. The
dangerous question was never "will beneficiaries post?" — it was "does the partner
org already have someone who OWNS information flow?" Every mature system has an owner:

- Ushahidi → deployment owner
- HOTOSM → validators
- ReliefWeb → OCHA editors
- HDX → org data managers

So A7 splits:

| # | Assumption | Evidence so far | Confidence | Next tester |
|---|------------|----------------|------------|-------------|
| A7a | Coordinators / info officers will publish into Nidaa | None yet, but tool research says orgs ALREADY staff this role (editor/validator/focal point). Fitting into an existing role is far more plausible than creating new behavior. | Medium→Low (plausible by analogy) | **Any partner with an info focal point** (Sameer, REACH, iMMAP, White Helmets, ERRs) — "who owns posting today?" |
| A7b | Beneficiaries will open / use the information | None yet. Still largely untested. | Low | **Beneficiary-adjacent voice** (We Are Not Numbers, a resident referral) — do people actually open coordination info, or rely on push (WhatsApp)? |

**Implication:** A7a is now LESS risky than it looked this morning — we are fitting into
an existing role, not inventing one. The real unknown is A7b (demand-side). Pilot design
should target the *coordinator/info-officer* as the primary user, with a bridge (a
coordinator who forwards from WhatsApp) for communities without a formal focal point.
Do NOT design for the lone beneficiary posting.

## The "who posts?" sub-question (most dangerous assumption)

Not a standalone A# — it gates A7 and the whole adoption thesis. Already partly
answered by studying existing tools (see COORDINATION-TOOLS-RESEARCH.md):

- **Ushahidi**: anyone can submit (SMS/web/social); a *deployment owner* triages.
  Someone always owns the deployment. → Nidaa needs a deployment owner too.
- **HOTOSM**: mappers draw, *validators* (a separate role) approve. Clear two-role split.
  → mirrors Nidaa's verifier concept; orgs already accept "validator" roles.
- **ReliefWeb**: OCHA editors curate 4,000+ sources. Professional editors own posting.
  → in institutional coordination, posting is a *staffed* function, not crowd-sourced.
- **HDX**: data is *contributed by organizations*, curated by OCHA data managers.
  → "who posts" = the org's data/info focal point, not the beneficiary.

**Implication for Nidaa:** the publishing step is owned in mature workflows by a
*designated role* (deployment owner, validator, info focal point, editor). The risk
is NOT "nobody posts" — it is "a grassroots group with no such role won't post."
Target partners who ALREADY have an info focal point (NGOs, coordinated response
rooms). For pure resident networks, Nidaa needs a bridge (e.g. a coordinator who
forwards from WhatsApp into Nidaa), not a lone beneficiary posting.

Next evidence needed: in Conversation #2, ask Q13 (publishing step). If the answer is
"our info officer / coordinator handles that," A7 risk drops. If "nobody / it's ad hoc,"
we must design a bridge or narrow scope.
