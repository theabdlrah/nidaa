# Nidaa — Do-No-Harm & Security Summary (Plain Language)

This is the one-page answer to "is it safe to put our information here?"

## What data is collected?
- Posts you choose to create: a need or an offer (e.g. medical, food, water,
  shelter), a title, a description, a city, and a category.
- Whether a trusted verifier has confirmed the post.
- An audit log of every verification (who, when, what changed) — for accountability.

## What data is optional?
- Contact details and exact location are **optional** and off by default.
- You never have to share your name, phone, or precise coordinates.
- Posts can be made with no personal identifier at all.

## Who can verify?
Only accounts issued a **verifier or admin token** by the deploying organization.
Ordinary users and anonymous visitors **cannot** verify anything. The verification
endpoint rejects them (HTTP 401).

## How is verification controlled?
Verifier tokens are secret, server-side, and issued only to trusted actors. A post
stays "unverified / unconfirmed" until a real verifier acts. Verification is always
visible in the audit log.

## What happens if a verifier is compromised?
Every verification is **logged and reversible**. A compromised or mistaken verification
can be undone and traced to the actor. Tokens can be revoked immediately by the admin.

## Can users export data?
Yes. All data is exportable in standard format, and the project is open source — you
are never locked in.

## Can organizations self-host?
Yes. Nidaa runs anywhere Node runs with no proprietary dependency. You can host it on
infrastructure you control; your data stays with you.

## Known limitations (stated honestly)
- The verification endpoint must be behind auth (it now is). Do not deploy with it open.
- The server is a single JSON store today; for scale it moves to SQLite/Postgres.
- Device-to-device (mesh) sync during a total server blackout is **not yet built**;
  sync requires the server to be reachable.
- Location precision should be kept at city level to avoid targeting risk.
- This is a prototype maturing toward field use — it has not yet been deployed with a live partner.
