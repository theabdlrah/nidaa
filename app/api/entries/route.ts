import { NextRequest, NextResponse } from "next/server";
import { listEntries, upsertEntry } from "@/lib/store";
import { NidaaEntry } from "@/lib/types";

export const dynamic = "force-dynamic";

function uuid(): string {
  if (typeof crypto !== "undefined" && "randomUUID" in crypto) {
    return crypto.randomUUID();
  }
  return "id-" + Math.random().toString(36).slice(2) + Date.now().toString(36);
}

// GET /api/entries — returns all entries (used by client sync pull)
export async function GET() {
  const entries = await listEntries();
  return NextResponse.json({ entries, serverTime: new Date().toISOString() });
}

// POST /api/entries — upsert a single entry from a client (offline-first sync push)
export async function POST(req: NextRequest) {
  let payload: NidaaEntry;
  try {
    payload = (await req.json()) as NidaaEntry;
  } catch {
    return NextResponse.json({ error: "invalid json" }, { status: 400 });
  }

  if (!payload || !payload.clientId || !payload.type || !payload.titleAr) {
    return NextResponse.json(
      { error: "missing required fields (clientId, type, titleAr)" },
      { status: 400 }
    );
  }

  const entry: NidaaEntry = {
    id: payload.id || uuid(),
    clientId: payload.clientId,
    type: payload.type,
    category: payload.category || "other",
    titleAr: payload.titleAr,
    titleEn: payload.titleEn || payload.titleAr,
    bodyAr: payload.bodyAr || "",
    bodyEn: payload.bodyEn || "",
    city: payload.city || "unknown",
    contact: payload.contact,
    lat: payload.lat,
    lng: payload.lng,
    authorRole: payload.authorRole || "unknown",
    verified: payload.verified ?? false,
    createdAt: payload.createdAt || new Date().toISOString(),
    syncedAt: new Date().toISOString(),
  };

  const saved = await upsertEntry(entry);
  return NextResponse.json({ entry: saved }, { status: 201 });
}
