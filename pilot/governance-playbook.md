# Nidaa — Governance & Verification Playbook

One page. Adoptable by any deploying organization without custom code.

## Verifier Roles
- **User** — can post and read. Cannot verify. (Default for everyone.)
- **Volunteer** — can post and read; may help moderate within a community. Cannot verify.
- **Verifier** — trusted actor (NGO coordinator, committee member) authorized to mark
  entries verified via an issued token.
- **Admin** — issues/revokes verifier tokens, oversees the verifier set, can reverse any verification.

## Verification Rules
- **Who can verify?** Only Verifier or Admin token holders. Anonymous and regular users receive 401.
- **When should verification occur?** When the verifier has independent confidence the
  entry is accurate (they witnessed it, cross-checked a trusted source, or it came from
  a known local actor). Verify promptly — slow verification erodes trust in the board.
- **How is it revoked?** Any verification can be reversed by a Verifier/Admin; the change
  is logged. A token can be revoked by an Admin at any time, instantly disabling that verifier.

## Audit Rules
- Every verification and reversal is **logged**: actor, timestamp, entry id, prior state,
  new state.
- Every verification is **reversible**: the prior state is stored, so a mistake or
  compromise is correctable and traceable.

## Escalation Rules
- **Disputed entry:** if an entry is challenged, an Admin reviews the audit trail and the
  conflicting reports, then confirms, reverses, or removes it with a reason recorded.
- **Suspected fabricated verification:** revoke the verifier token immediately; review that
  verifier's full audit history; notify the deploying organization.
- **Spam / harmful post:** any Verifier or Admin can flag for removal; removal is logged.
- **Principle:** when safety and convenience conflict, the default favors safety. Nidaa is a
  civilian aid tool and must never become a targeting or misinformation vector.
