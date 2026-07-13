export type EntryType = "need" | "offer";

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
  createdAt: string;     // ISO
  syncedAt: string | null; // null while pending on a client
}

export interface DbShape {
  entries: NidaaEntry[];
}
