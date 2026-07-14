### Conversation: Adam Elijilah (Resident perspective) — 2026-07-14

1. What problem did they describe?
   - During connectivity outages, lost access to aid-distribution information and to digital
     payments/transfers. The channel that normally delivers aid info (pushed directly to his
     phone) simply stops when the network drops.

2. What tools do they currently use?
   - WhatsApp, Telegram, and Facebook as primary information channels. Aid information is commonly
     sent directly to beneficiaries' phones.

3. What failed recently?
   - Connectivity outages: could not access information about aid/services; digital payments and
     transfers became unavailable; in at least one case a family was unable to access
     food-distribution information because of the outage.

4. Was the bottleneck information, verification, coordination, logistics, supply, trust, or something else?
   - Information access + the channel itself (the outage cuts the pipe). Downstream this becomes a
     logistics/access failure (can't reach distribution). Not primarily a verification problem.

5. Would Nidaa have helped?
   - Possibly, specifically during the outage window — IF the aid-distribution info had been posted
     into a local-first board before / independent of the outage.

6. Why?
   - A local-first store means info already on the device survives an outage; WhatsApp/Telegram
     require connectivity to receive/refresh. This is exactly the A3 failure mode Nidaa is built around.

7. Why not?
   - Beneficiaries receive info pushed to them; Nidaa requires someone to POST that info into Nidaa
     first. That publishing step is a dependency incumbent push-channels don't have. If the info
     never lands in Nidaa, it helps nothing. Adoption/entry friction is real (touches A7).

8. What assumption took the biggest hit?
   - None weakened. A3 (offline) is the biggest STRENGTHENED — but the precise lesson is sharper than
     "offline is nice": the failure mode of incumbent tools IS connectivity loss.

--- EVIDENCE LEDGER (required) ---

- Assumptions tested this conversation: A2, A3, A5
- Assumptions strengthened (with the specific evidence):
  - A3 (offline capability materially matters) — STRONGLY. Direct observation: outages cut access to
    aid info AND digital payments/transfers; a family lost access to food-distribution info. The tool
    failure mode is connectivity itself.
  - A2 (information/matching is a significant bottleneck) — MODERATELY. Info access depends on
    connectivity; when it drops, info access is the binding constraint for receiving aid.
  - A5 (existing tools insufficient for at least some communities) — MODERATELY. WhatsApp/Telegram/FB
    work only when connectivity exists; they are insufficient precisely during outages, when needed most.
- Assumptions weakened (with the specific evidence): none.
- Assumptions falsified (with the specific evidence): none.
- What surprised us (something we did not predict): the framing "WhatsApp is insufficient" is
  imprecise. The real, more precise failure mode is connectivity itself — tools work when connectivity
  exists, fail when it doesn't. Also: digital payments/transfers also fail during outages (wider blast
  radius than coordination alone).
- What should change because of this evidence: re-scope A3 from "offline matters" to "offline matters
  specifically because the failure mode of incumbent tools IS connectivity loss" — sharper thesis, not
  just 'offline is nice.' Flag the publishing/entry dependency: Nidaa only helps during an outage if
  aid info is posted into it first (connects to A7 adoption and to a workflow question: who posts?).
