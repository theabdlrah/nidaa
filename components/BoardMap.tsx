// components/BoardMap.tsx
// Client-only Leaflet map. Plots entries that carry lat/lng. Tile layer is
// cache-backed (lib/tileCache) so it keeps working offline.
"use client";

import { useEffect, useRef } from "react";
import type { QueuedEntry } from "@/lib/offlineQueue";
import { makeCachedTileLayer } from "@/lib/tileCache";
import type { Lang } from "@/lib/types";

export default function BoardMap({
  entries,
  lang,
}: {
  entries: QueuedEntry[];
  lang: Lang;
}) {
  const elRef = useRef<HTMLDivElement>(null);
  const mapRef = useRef<any>(null);
  const layerRef = useRef<any>(null); // tracked marker group (so we can clear)

  useEffect(() => {
    let cancelled = false;
    (async () => {
      const L = (await import("leaflet")).default;
      if (!elRef.current || cancelled) return;
      if (!mapRef.current) {
        const map = L.map(elRef.current, { preferCanvas: true }).setView(
          [33.5, 37.5],
          6
        );
        const tiles = await makeCachedTileLayer(
          "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
          {
            attribution: "© OpenStreetMap",
            maxZoom: 18,
          }
        );
        tiles.addTo(map);
        mapRef.current = map;
        layerRef.current = L.layerGroup().addTo(map);
      }
      const map = mapRef.current;

      // clear old markers (circleMarkers, not Markers — must use the group)
      layerRef.current.clearLayers();

      const pts = entries.filter(
        (e) => typeof e.lat === "number" && typeof e.lng === "number"
      );
      const bounds: any[] = [];
      for (const e of pts) {
        const color = e.type === "need" ? "#b91c1c" : "#15803d";
        const marker = L.circleMarker([e.lat!, e.lng!], {
          radius: 5,
          color,
          fillColor: color,
          fillOpacity: 0.8,
          weight: 1,
        });
        const title = lang === "ar" ? e.titleAr : e.titleEn;
        marker.bindPopup(
          `<strong>${title}</strong><br/>${e.category} · ${
            e.verified ? "✓ verified" : "unverified"
          }${e.city ? "<br/>" + e.city : ""}`
        );
        marker.addTo(layerRef.current);
        bounds.push([e.lat!, e.lng!]);
      }
      if (bounds.length > 0) {
        map.fitBounds(bounds, { padding: [30, 30], maxZoom: 12 });
      }
    })();
    return () => {
      cancelled = true;
    };
  }, [entries, lang]);

  return <div ref={elRef} className="map-canvas" style={{ height: 360 }} />;
}
