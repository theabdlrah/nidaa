# scripts/shp_to_geojson.py
# Minimal dependency-free SHP (polygon) -> GeoJSON converter.
# Only used ONCE, locally, to produce data/gaza-boundary.geojson from the
# HDX Gaza Strip Municipal Boundaries .shp. Not part of the app runtime.
import struct, json, sys, zipfile, os

SRC_ZIP = "data/_tmp_gzb/g.zip"
SHP_NAME = "GazaStrip_MunicipalBoundaries.shp"
OUT = "data/gaza-boundary.geojson"

def read_shp_polygons(path):
    with open(path, "rb") as f:
        data = f.read()
    # header: 100 bytes (we skip). file code already checked by caller.
    records = []
    pos = 100
    n = len(data)
    while pos + 8 <= n:
        rec_num = struct.unpack_from(">i", data, pos)[0]
        rec_len = struct.unpack_from(">i", data, pos + 4)[0] * 2
        start = pos + 8
        end = start + rec_len  # rec_len excludes the 8-byte record header
        if end > n:
            break
        shape_type = struct.unpack_from("<i", data, start)[0]
        if shape_type == 5:  # Polygon
            # layout (content-relative bytes):
            #   0  : shapeType (int32)
            #   4  : bbox = 4 x double (32 bytes)
            #   36 : numParts (int32)
            #   40 : numPoints (int32)
            #   44 : parts[numParts] (int32)
            #   44+4*numParts : points[numPoints] (2 x double)
            num_parts = struct.unpack_from("<i", data, start + 36)[0]
            num_points = struct.unpack_from("<i", data, start + 40)[0]
            if num_parts <= 0 or num_points <= 0 or num_parts > 100000 or num_points > 10000000:
                pos = end
                continue
            parts = []
            for i in range(num_parts):
                off = start + 44 + 4 * i
                if off + 4 <= end:
                    parts.append(struct.unpack_from("<i", data, off)[0])
                else:
                    parts.append(len(flat))
            pts_start = start + 44 + 4 * num_parts
            flat = []
            i = 0
            while i < num_points and len(flat) < num_points:
                if pts_start + 16 * i + 16 > end:
                    break
                x = struct.unpack_from("<d", data, pts_start + 16 * i)[0]
                y = struct.unpack_from("<d", data, pts_start + 16 * i + 8)[0]
                flat.append([x, y])
                i += 1
            rings = []
            for pi in range(len(parts)):
                s = parts[pi]
                e2 = parts[pi + 1] if pi + 1 < len(parts) else len(flat)
                rings.append(flat[s:e2])
            records.append(rings)
        pos = end
    return records

def main():
    with zipfile.ZipFile(SRC_ZIP) as z:
        with z.open(SHP_NAME) as shp:
            raw = shp.read()
    # shp is in memory now; write to temp file for the reader
    tmp = "data/_tmp_gzb/bound.shp"
    with open(tmp, "wb") as f:
        f.write(raw)
    rings_all = read_shp_polygons(tmp)
    features = []
    for rings in rings_all:
        features.append({
            "type": "Feature",
            "properties": {},
            "geometry": {"type": "Polygon", "coordinates": rings},
        })
    fc = {"type": "FeatureCollection", "features": features}
    os.makedirs("data", exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(fc, f, ensure_ascii=False)
    print(f"wrote {OUT}: {len(features)} polygons, {sum(len(r) for f in features for r in f['geometry']['coordinates'])} rings")

if __name__ == "__main__":
    main()
