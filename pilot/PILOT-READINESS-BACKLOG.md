# Nidaa — Pilot-Readiness Backlog (Track B, secondary)

**Status:** PLANNING DOCUMENT ONLY. No implementation until evidence from
Conversation #1 exists. The tracker (`ASSUMPTION-TRACKER.md`) remains the source
of truth. This backlog is ranked by usefulness across outcomes, NOT by feature
appeal.

**Constraint (from operating instruction):** exclude anything that assumes A1
(coordination priority), A2 (info/matching bottleneck), or A5 (existing tools
insufficient). Excluded by rule: mesh networking, federation, AI features,
reputation systems, advanced moderation, cross-community coordination,
large-scale infrastructure.

**Ranking logic:** an item ranks high if it is valuable in proceed / narrow /
pivot scenarios, low-assumption, and cheap. "Stop" invalidates all engineering,
so it is not a ranking criterion — only a reminder that evidence may end the
project.

---

## Items (assumption-light, outcome-resilient)

| # | Item | Proceed | Narrow | Pivot | Assumes | Cost |
|---|------|---------|--------|-------|---------|------|
| 1 | **Verifier Identity Management** — replace env tokens with real accounts (create / revoke / permission / rotate) | Yes | Yes | Partial* | A6 | Med |
| 2 | **Audit-log integrity** — append-only, tamper-evidence, export | Yes | Yes | Yes** | A4 | Med |
| 3 | **Data export / deletion (DPIA prerequisite)** — GDPR-style export + delete API | Yes | Yes | Yes** | none | Low |
| 4 | **Self-host packaging** — Docker / one-command deploy for non-technical orgs | Yes | Yes | Yes*** | none | Med |
| 5 | **Stale-data provenance banner** — map facilities show source + capture date + "may be outdated" | Yes | Yes | Yes** | none | Low |
| 6 | **Coordinate-precision control** — city/neighborhood default; precise opt-in + "may be unsafe" label | Yes | Yes | Yes** | none | Low |

\* Pivot only if the pivoted solution still uses a trusted-verifier concept.
\** Survives any scenario where a board/map is shown.
\*** Survives even if the target community changes (any deployer benefits).

---

## Priority order

1. **Verifier Identity Management** — highest leverage for any pilot; the one
   question every serious pilot conversation eventually asks ("who are the
   verifiers, how are accounts made/revoked?"). Assumption-light (A6 only).
2. **Audit-log integrity** — pairs with #1; the trust backbone. Assumption-light.
3. **Data export / deletion** — the DPIA/agreement prerequisite we already said
   pilots require. Needed for any responsible deployment.
4. **Self-host packaging** — closes the "promised, not built" honesty gap we
   admitted in the docs; survives a community change.
5. **Stale-data provenance banner** — cheap fix for a red-team finding.
6. **Coordinate-precision control** — cheap fix for the primary ethical risk.

---

## Build-first item (when evidence permits)

**Verifier Identity Management** — but as a *design*, not code, until
Conversation #1. It survives proceed (required) and narrow (required); it is the
cleanest item to scope without assuming A1/A2/A5. Caveat: value is contingent on
A6 not being falsified.

---

## Explicit non-action

- No mesh / federation / AI / reputation / advanced-moderation / cross-community
  work. These depend on unvalidated assumptions.
- **No implementation of any item until a real conversation updates the tracker.**
- Primary action remains outreach (send Message #1). This document is the only
  Track B output authorized before evidence.
