import { NextRequest, NextResponse } from "next/server";
import { setVerified, readAudit } from "@/lib/store";
import { getRole, canVerify } from "@/lib/auth";

export const dynamic = "force-dynamic";

// GET /api/verify — read-only transparency trail of all verification actions.
// Intentionally unauthorized: the audit log is meant to be auditable/visible.
export async function GET() {
  const log = await readAudit();
  return NextResponse.json({ audit: log });
}

// POST /api/verify  { id, verified } — a trusted verifier/admin marks an entry
// verified (or reverses it). This endpoint is now ROLE-GATED: anonymous users,
// regular users, and unknown tokens all receive 401. Only Verifier/Admin tokens
// (server-side secrets) may act. Every action is logged and reversible in the store.
export async function POST(req: NextRequest) {
  const role = getRole(req);
  if (!canVerify(role)) {
    return NextResponse.json(
      { error: "unauthorized: verification requires a verifier or admin token" },
      { status: 401 }
    );
  }

  let payload: { id?: string; verified?: boolean };
  try {
    payload = await req.json();
  } catch {
    return NextResponse.json({ error: "invalid json" }, { status: 400 });
  }
  if (!payload.id) {
    return NextResponse.json({ error: "missing id" }, { status: 400 });
  }

  const entry = await setVerified(payload.id, Boolean(payload.verified), role);
  if (!entry) {
    return NextResponse.json({ error: "not found" }, { status: 404 });
  }
  return NextResponse.json({ entry });
}
