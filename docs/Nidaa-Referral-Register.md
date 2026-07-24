# Nidaa — Referral Register

Type: OPERATIONS SUPPORT artifact (Day 8). Maintained ledger of referrals.
Rule: no new people identified; no outreach generated from this register.
"Confirmed" = referral stated by a reached practitioner. "Potential" = source may
hold referrals but contacts are unknown / unverified.

==================================================================
CONFIRMED REFERRALS
==================================================================

1. Emma Fitzpatrick  ->  Mohammed Aghaalkurdi
   - Source: Emma auto-reply, 2026-07-20 (Day 8 Pipeline Event).
   - Emma named him as a Gaza Health Cluster point of contact (PoC).
   - Status: CONFIRMED referral.
   - Contact status: REACHED (sent-verified). Email dispatched 2026-07-20 via
     Emma referral routing (user-confirmed). Awaiting response. DESYNC RESOLVED
     2026-07-20 (D1 run) — see resolution note in DESYNC FLAG section below.

2. Emma Fitzpatrick  ->  Naomi Morris
   - Source: same Emma auto-reply, 2026-07-20.
   - Named alongside Mohammed as a Gaza Health Cluster PoC.
   - Status: CONFIRMED referral.
   - Contact status: per ledger, NOT yet contacted at last update.

==================================================================
POTENTIAL REFERRALS
==================================================================

3. Jess  ->  unknown contacts
   - Status: POTENTIAL referral source.
   - Contacts: UNKNOWN. No names, orgs, or channels identified.
   - Action: verify whether Jess holds real referral contacts before logging any
     named rows. Do NOT generate names (Day 8 ops constraint: no new people).

==================================================================
DESYNC FLAG — RESOLVED 2026-07-20 (D1 nidaa-artifact-sync run)
==================================================================
ORIGINAL DESYNC: The Day 8 task header stated "Mohammed Aghaalkurdi has been
contacted via Emma Fitzpatrick referral," but the continuity artifact
(Day6-Brief L630–632, 644–645) stated Mohammed was a SEED row, "referred, NOT
yet contacted," with Day 8 contact "planned ... NOT dispatched tonight."

RESOLUTION: User confirmed (2026-07-20) that the email to Mohammed WAS sent.
Ground truth = REACHED (sent-verified). The artifacts were consistent with each
other but STALE relative to reality (the dispatch fact existed only in user
confirmation, not yet written to any file). Per the constitution, the artifact
is source of truth for CONCLUSIONS; a factual dispatch event confirmed by the
user is synchronized in, not overridden. Mohammed row updated to REACHED across
Evidence-Ledger, Day6-Brief (Day 8 sync addendum), and Pipeline-Status.

Naomi Morris remains a SEED row (contact was conditional on Mohammed being
unresponsive; only Mohammed's send was confirmed). No change to Naomi.

No evidence layer change. Register is relationship/pipeline tracking, not A6b.
