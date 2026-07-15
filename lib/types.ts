export type EntryType = "need" | "offer";

export type Lang = "ar" | "en";

export interface NidaaEntry {
  id: string;            // server-assigned canonical id (uuid)
  clientId: string;      // client-generated id (stable across retries)
  type: EntryType;
  category:
    | "medical"
    | "food"
    | "water"
    | "shelter"
    | "education"
    | "transport"
    | "other";
  titleAr: string;
  titleEn: string;
  bodyAr: string;
  bodyEn: string;
  city: string;          // e.g. "Aleppo", "Damascus", "Homs", "Idlib", "Daraa"
  contact?: string;      // phone / channel (optional, shown with care)
  lat?: number;
  lng?: number;
  authorRole: "individual" | "ngo" | "volunteer" | "unknown";
  // verified = a human/organisation verifier marked this true AFTER a real
  // check. Imported HDX/OSM facility data is NOT human-verified — it carries
  // provenance instead (source + sourceDate). Never set verified:true on import.
  verified: boolean;     // verified by a designated verifier after sync (user posts only)
  source?: string;      // e.g. "hdx:hotosm_syr_health_facilities" or "user"
  sourceDate?: string;   // capture date of the source data (provenance)
  region?: "gza" | "wb" | "syr" | "other"; // deployment region scoping
  // Location precision: imported dataset features are exact points from OSM.
  // To reduce targeting risk in active conflict, the default for user posts is
  // "neighborhood" (city/area shown, exact coordinates withheld unless opted in).
  precision?: "exact" | "neighborhood";
  createdAt: string;     // ISO
  syncedAt: string | null; // null while pending on a client
}

export interface VerificationAudit {
  entryId: string;
  clientId: string;
  actorRole: string;
  action: "verify" | "unverify";
  priorVerified: boolean;
  newVerified: boolean;
  at: string; // ISO timestamp
}

export interface DbShape {
  entries: NidaaEntry[];
}
