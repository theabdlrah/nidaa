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
  verified: boolean;     // verified by an NGO/admin after sync
  source?: string;      // e.g. "hdx:hotosm_syr_health_facilities" or "user"
  region?: "gza" | "wb" | "syr" | "other"; // deployment region scoping
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
