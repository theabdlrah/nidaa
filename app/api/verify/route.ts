import { NextRequest, NextResponse } from "next/server";
import { setVerified } from "@/lib/store";

export const dynamic = "force-dynamic";

// POST /api/verify  { id, verified } — NGO/admin marks an entry verified.
// In a real deployment this must be gated behind auth. This build leaves it
// open for the demo but documents the requirement clearly.
export async function POST(req: NextRequest) {
  let payload: { id?: string; verified?: boolean };
  try {
    payload = await req.json();
  } catch {
    return NextResponse.json({ error: "invalid json" }, { status: 400 });
  }
  if (!payload.id) {
    return NextResponse.json({ error: "missing id" }, { status: 400 });
  }
  const entry = await setVerified(payload.id, Boolean(payload.verified));
  if (!entry) {
    return NextResponse.json({ error: "not found" }, { status: 404 });
  }
  return NextResponse.json({ entry });
}
