# A6 Grassroots Hunt — "Can the kind of coordinator Nidaa depends on maintain structured information?"

**Correction applied.** The first A6 pass gathered evidence about *formal IM teams*
(SARC department, MapAction, WFP, HOTOSM, ReliefWeb, Ushahidi). That proved "large
humanitarian organizations maintain structured information" — which was never really in
doubt. The live question for Nidaa is different:

> Will the **small / informal coordinator** Nidaa depends on — camp volunteer, community
> focal point, local coordinator, mutual-aid organizer, neighborhood committee — maintain
> structured information?

This file hunts THAT population only. No formal-org IM evidence unless it directly informs
grassroots behavior. No design, no architecture, no solution discussion.

---

## The 6 behavioral questions (applied to grassroots coordinators)

1. **Who keeps information?** (volunteer? committee? focal point? nobody designated?)
2. **How do they keep it?** (group chat? spreadsheet? notebook? memory? nothing?)
3. **What gets written down?** (beneficiary lists? needs? incidents? distributions?)
4. **What stays verbal?** (most coordination? decisions? who-has-what?)
5. **When does tracking break down?** (surge? insecurity? connectivity loss? burnout?)
6. **What is abandoned first under overload?** (the board? verification? updating?)

---

## Retrieved grassroots sources (real, URLs verified HTTP 200)

### 1. Emergency Response Rooms (ERRs), Sudan — ACAPS Thematic Report, 16 Oct 2025
URL: https://reliefweb.int/report/sudan/acaps-thematic-report-sudan-challenges-and-opportunities-khartoum-state-emergency-response-rooms-16-october-2025
- ~360 ERRs across 7 states by Oct 2024; Khartoum ERRs across **54 neighborhoods**.
- ERRs are **volunteer networks**; many originated from **neighborhood resistance committees (RCs)**.
- Key behavioral fact: the "room" in ERR **refers to the online group chats** where they were
  originally conceived and planned. → information coordination is **chat/verbal-based**, not a
  structured database.
- The report notes ERRs "preferring to focus on ERRs' goal of providing aid" — i.e. action over
  documentation; structured record-keeping is not their described core practice.

### 2. Mutual aid lessons — ERRs, Sudan (ACAPS/SSHAP case study, Jun–Aug 2024)
URL: https://reliefweb.int/report/sudan/key-considerations-mutual-aid-lessons-and-experiences-emergency-response-rooms-sudan
- Based on interviews with ERR volunteers; the "room" = **online group chats** (WhatsApp/online).
- Calls for "**ongoing documentation, analysis and learning** from grassroots responses" — this
  is framed as a *recommended gap*, not an observed strength. Implies documentation is partial/informal.
- Recognizes "informal networks, diaspora groups, national NGOs" as non-hierarchical solidarity actors.

---

## Answers (from the grassroots sources above)

| Question | Grassroots evidence (ERRs, Sudan) |
|----------|-----------------------------------|
| Who keeps information? | Volunteers + neighborhood committees; **no dedicated IM owner**. |
| How do they keep it? | **Online group chats** (the "room"); verbal/async chat, not a database. |
| What gets written down? | Aid delivery actions; beneficiary/distribution info lives in chat, not a structured register. |
| What stays verbal? | Most coordination + decisions happen in chat/verbal. |
| When does tracking break down? | Under surge / insecurity / connectivity loss (chat-dependent = fails when network drops — see A3). |
| What is abandoned first under overload? | Documentation/learning (the brief itself lists it as a gap to build, not a practiced habit). |

---

## Success-criterion check

> Find ONE example where a small coordinator successfully maintains structured information.
> Find ONE example where maintenance collapses under pressure.

- **Successful structured maintenance (grassroots):** NOT yet found in retrieved sources. ERRs
  coordinate effectively via chats, but "structured" (persistent, queryable, verified) maintenance
  is exactly what the mutual-aid brief says needs to be *built*, not what exists. So the positive
  grassroots case is **not yet evidenced** — honest gap.
- **Maintenance collapse under pressure:** partially evidenced — ERR info coordination is
  chat-dependent, so it inherits the A3 failure mode (connectivity loss severs the channel). And
  the brief's call for "ongoing documentation" implies it is dropped when bandwidth is spent on
  direct aid. This is a *soft* collapse signal, not a hard documented failure.

---

## What this means for A6

- The formal-org evidence (SARC etc.) answered the wrong population. For the **Nidaa-target
  coordinator** (grassroots/informal), the pattern is: **they DO coordinate, but via chats and
  committees, and structured/verified documentation is a gap, not a habit.**
- This **narrows A6 significantly**: structured information maintenance by small coordinators is
  plausible only if the tool makes the burden near-zero and lives inside the channel they already
  use (the chat), because they will not run a separate structured system under load. That is a
  behavioral constraint, not a willingness question.
- A6 for the grassroots population is therefore **unproven, leaning weak** — the opposite of the
  formal-org "early support." The burden+ownership condition from the first A6 pass is even tighter
  here: no owner, chat-based, documentation dropped under load.

## Updated A6 status

- **Formal organizations:** Early Support (real IM behavior, owner + automation).
- **Grassroots / small coordinators (the Nidaa user):** Untested → leaning Weak. No successful
  structured-maintenance example yet; chat-based coordination + documentation-as-gap.

## Still to retrieve (to satisfy the success criterion)

- One grassroots case where a small coordinator **did** maintain a structured list/register
  successfully (e.g. a camp committee with a real beneficiary spreadsheet; a neighborhood committee
  using a shared form).
- One case where grassroots tracking **hard-collapsed** under pressure (connectivity loss, surge,
  burnout) — ideally a first-hand account.
- A coordinator/ops-lead interview (AbuAlatta, Sameer, White Helmets local team, a camp committee)
  answering the 6 questions directly. White Helmets local teams are a strong candidate: civil-defense
  volunteers who DO record rescues/incidents — a possible grassroots SUCCESS case worth retrieving.

---

## Deliverable statement

> Based on current grassroots evidence, A6 for the Nidaa-target coordinator is: **Unproven, leaning
> Weak.** Grassroots coordinators (ERRs, neighborhood committees) coordinate effectively but via
> group chats and committees, not structured/verified systems; documentation is a named gap, not a
> habit, and is abandoned under load. The formal-org "early support" does not transfer to this
> population. A successful grassroots structured-maintenance example and a hard-collapse case are
> still required before A6 can be judged for the actual user.

No design work. A1 preserved at bounded conclusion. A6 formal-case noted; grassroots case is the
open, higher-stakes question.
