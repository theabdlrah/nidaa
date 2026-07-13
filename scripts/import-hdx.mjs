// scripts/import-hdx.mjs
// Phase 1: seed Nidaa with REAL facility data from HDX / HOT OSM.
// Downloads GeoJSON zips, maps OSM tags -> NidaaEntry, writes data/db.json.
// Idempotent: clientId = `${dataset}:${osmId}` so re-runs never duplicate.
//
// Usage:  npm run import-hdx
// Needs network on first run. Pure-JS (fflate) so it stays zero-native-deps.

import { gunzipSync, unzipSync } from "fflate";
import { promises as fs } from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.join(__dirname, "..");
const DB_PATH = path.join(ROOT, "data", "db.json");

// HDX / HOT OSM GeoJSON zip endpoints (verified July 2026).
// Gaza-first deployment: PSE (Palestine/Gaza) datasets are PRIMARY/active;
// Syria (SYR) datasets are secondary/secondary region. Both are real OSM data.
const DATASETS = [
  {
    key: "hotosm_pse_health_facilities",
    label: "Palestine (Gaza/West Bank) — Health Facilities [PRIMARY]",
    url: "https://production-raw-data-api.s3.amazonaws.com/ISO3/PSE/health_facilities/hotosm_pse_health_facilities_osm_geojson.zip",
    category: "medical",
    primary: true,
    region: "gza",
  },
  {
    key: "hotosm_pse_education_facilities",
    label: "Palestine (Gaza/West Bank) — Education Facilities [PRIMARY]",
    url: "https://production-raw-data-api.s3.amazonaws.com/ISO3/PSE/education_facilities/hotosm_pse_education_facilities_osm_geojson.zip",
    category: "education",
    primary: true,
    region: "gza",
  },
  {
    key: "hotosm_syr_health_facilities",
    label: "Syria — Health Facilities [secondary]",
    url: "https://production-raw-data-api.s3.amazonaws.com/ISO3/SYR/health_facilities/hotosm_syr_health_facilities_osm_geojson.zip",
    category: "medical",
    primary: false,
    region: "syr",
  },
  {
    key: "hotosm_syr_education_facilities",
    label: "Syria — Education Facilities [secondary]",
    url: "https://production-raw-data-api.s3.amazonaws.com/ISO3/SYR/education_facilities/hotosm_syr_education_facilities_osm_geojson.zip",
    category: "education",
    primary: false,
    region: "syr",
  },
];

// Map an OSM feature's tags to a Nidaa category override (default = dataset category).
function categoryFromTags(tags, fallback) {
  const a = (tags.amenity || tags.healthcare || tags.building || "").toLowerCase();
  if (/hospital|clinic|doctors|health|dentist/.test(a)) return "medical";
  if (/school|university|college|kindergarten/.test(a)) return "education";
  if (/pharmacy/.test(a)) return "medical";
  return fallback;
}

function pickName(tags) {
  const ar = tags["name:ar"] || tags["name_ar"] || "";
  const en = tags["name:en"] || tags["name_en"] || tags.name || "";
  const any = tags.name || en || ar;
  return {
    titleAr: ar || any,
    titleEn: en || any,
    fallback: any,
  };
}

// Point -> [lng, lat]; Polygon/MultiPolygon -> centroid of first ring.
function centroid(geom) {
  if (!geom) return { lat: undefined, lng: undefined };
  if (geom.type === "Point") {
    const [lng, lat] = geom.coordinates;
    return { lat, lng };
  }
  if (geom.type === "Polygon") {
    const ring = geom.coordinates[0];
    let x = 0, y = 0;
    for (const [lng, lat] of ring) { x += lng; y += lat; }
    return { lat: y / ring.length, lng: x / ring.length };
  }
  if (geom.type === "MultiPolygon") {
    const ring = geom.coordinates[0][0];
    let x = 0, y = 0;
    for (const [lng, lat] of ring) { x += lng; y += lat; }
    return { lat: y / ring.length, lng: x / ring.length };
  }
  return { lat: undefined, lng: undefined };
}

async function fetchZip(url) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`HTTP ${res.status} for ${url}`);
  const buf = new Uint8Array(await res.arrayBuffer());
  // HDX zips are sometimes gzipped; fflate unzip handles zip, gunzip handles .gz
  try {
    return unzipSync(buf);
  } catch {
    const gz = gunzipSync(buf);
    return { "data.geojson": gz };
  }
}

async function importDataset(ds) {
  process.stdout.write(`→ ${ds.label} ... `);
  const files = await fetchZip(ds.url);
  // find the .geojson inside the zip
  const geoKey = Object.keys(files).find((k) => k.toLowerCase().endsWith(".geojson"));
  if (!geoKey) throw new Error(`no .geojson in ${ds.key}`);
  const fc = JSON.parse(new TextDecoder().decode(files[geoKey]));
  const features = fc.features || [];
  const entries = [];
  for (const f of features) {
    const tags = f.properties || {};
    const { titleAr, titleEn, fallback } = pickName(tags);
    if (!fallback) continue; // skip unnamed
    const { lat, lng } = centroid(f.geometry);
    const cat = categoryFromTags(tags, ds.category);
    const osmId = tags.osm_id || tags["@id"] || tags.id || fallback;
    const clientId = `${ds.key}:${osmId}`;
    const city = tags["addr:city"] || tags.province || tags.region || "";
    const type = tags.amenity || tags.healthcare || tags.building || "facility";
    entries.push({
      id: clientId, // server will reassign on first sync; deterministic here
      clientId,
      type: "offer",
      category: cat,
      titleAr,
      titleEn,
      bodyAr: `منشأة موثّقة من HOT OSM / HDX — ${type}`,
      bodyEn: `Facility from HOT OSM / HDX — ${type}`,
      city,
      lat,
      lng,
      authorRole: "ngo",
      verified: true,
      source: `hdx:${ds.key}`,
      region: ds.region,
      createdAt: new Date().toISOString(),
      syncedAt: null,
    });
  }
  console.log(`${entries.length} features`);
  return entries;
}

async function main() {
  const all = [];
  for (const ds of DATASETS) {
    try {
      const e = await importDataset(ds);
      all.push(...e);
    } catch (err) {
      console.error(`  ! ${ds.label} failed: ${err.message}`);
    }
  }
  // Merge with existing db.json (preserve user posts, overwrite HDX by clientId).
  let db = { entries: [] };
  try {
    db = JSON.parse(await fs.readFile(DB_PATH, "utf-8"));
  } catch {}
  const byClient = new Map();
  for (const e of db.entries) if (e.source && e.source.startsWith("hdx:")) byClient.set(e.clientId, e);
  for (const e of db.entries) if (!e.source || !e.source.startsWith("hdx:")) byClient.set(e.clientId, e);
  for (const e of all) byClient.set(e.clientId, e);
  db.entries = [...byClient.values()];
  await fs.mkdir(path.dirname(DB_PATH), { recursive: true });
  await fs.writeFile(DB_PATH, JSON.stringify(db, null, 2), "utf-8");
  const hdx = db.entries.filter((e) => e.source && e.source.startsWith("hdx:")).length;
  const user = db.entries.length - hdx;
  console.log(`\nDone. Total ${db.entries.length} entries (${hdx} HDX facilities, ${user} other).`);
}

main().catch((e) => {
  console.error("FATAL", e);
  process.exit(1);
});
