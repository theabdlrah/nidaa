// Lightweight role gate for the verification endpoint.
//
// This is the interim security control that closes the previously-open
// /api/verify route. It is deliberately small and swappable: when Nidaa
// moves to Auth.js v5 (Phase 3 of the roadmap) this module is replaced,
// but the 401/200 contract stays identical.
//
// Authorization is via a Bearer token (or x-api-key header) validated
// against server-side secrets. Tokens are NEVER guessable and are scoped:
//   - NIDAA_ADMIN_TOKENS    -> admin  (can verify + manage verifiers)
//   - NIDAA_VERIFIER_TOKENS -> verifier (can verify)
//   - NIDAA_USER_TOKENS     -> user   (cannot verify -> 401)
//   - no / unknown token    -> anon   (cannot verify -> 401)
//
// A verifier token must be issued out-of-band to a trusted actor and stored
// as a server secret (e.g. in .env.local). It is NOT derivable from the client.

export type Role = "anon" | "user" | "verifier" | "admin";

function envList(name: string): string[] {
  const v = process.env[name];
  if (!v) return [];
  return v
    .split(",")
    .map((s) => s.trim())
    .filter(Boolean);
}

export function getRole(req: Request): Role {
  const auth = req.headers.get("authorization") || "";
  let token = "";
  if (auth.toLowerCase().startsWith("bearer ")) {
    token = auth.slice(7).trim();
  }
  if (!token) {
    const apiKey = req.headers.get("x-api-key");
    if (apiKey) token = apiKey.trim();
  }

  if (!token) return "anon";

  const admins = envList("NIDAA_ADMIN_TOKENS");
  if (admins.includes(token)) return "admin";

  const verifiers = envList("NIDAA_VERIFIER_TOKENS");
  if (verifiers.includes(token)) return "verifier";

  // A presented-but-non-verifier token is a regular user: explicitly denied.
  const users = envList("NIDAA_USER_TOKENS");
  if (users.includes(token)) return "user";

  // Unknown token: treat as anonymous (cannot verify).
  return "anon";
}

export function canVerify(role: Role): boolean {
  return role === "verifier" || role === "admin";
}
