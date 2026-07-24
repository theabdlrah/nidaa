import { NextRequest, NextResponse } from "next/server";
import { setAssignment, readAssignAudit } from "@/lib/store";
import { getRole, canVerify } from "@/lib/auth";

export const dynamic = "force-dynamic";

// GET /api/assign — read-only transparency trail of all assignment actions.
// Intentionally unauthorized: the audit log is meant to be auditable/visible.
export async function GET() {
  const log = await readAssignAudit();
  return NextResponse.json({ audit: log });
}

// POST /api/assign  { id, owner?, assignedTo? } — a trusted coordinator (verifier/
// admin token, same gate as /api/verify) sets the accountable owner and/or the
// responsible assignees for an entry. Mirrors /api/verify: role-gated, partial
// update (only provided fields change), fully audited and reversible in the store.
export async function POST(req: NextRequest) {
  const role = getRole(req);
  if (!canVerify(role)) {
    return NextResponse.json(
      { error: "unauthorized: assignment requires a verifier or admin token" },
      { status: 401 }
    );
  }

  let payload: { id?: string; owner?: string; assignedTo?: string[] };
  try {
    payload = await req.json();
  } catch {
    return NextResponse.json({ error: "invalid json" }, { status: 400 });
  }
  if (!payload.id) {
    return NextResponse.json({ error: "missing id" }, { status: 400 });
  }

  const patch: { owner?: string; assignedTo?: string[] } = {};
  if (typeof payload.owner === "string") patch.owner = payload.owner;
  if (Array.isArray(payload.assignedTo)) {
    patch.assignedTo = payload.assignedTo.map(String);
  }

  const entry = await setAssignment(payload.id, patch, role);
  if (!entry) {
    return NextResponse.json({ error: "not found" }, { status: 404 });
  }
  return NextResponse.json({ entry });
}
