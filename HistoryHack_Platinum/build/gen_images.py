#!/usr/bin/env python3
"""Populate <workspace>/analysis/unit<N>_images.json from the app's VERIFIED
public-domain primary-source image bank (primary-sources/images/unit-N.json).
Assigns one image per standard (greedy, no reuse), preferring cartoons/photos/
portraits as the HIPPO anchor; copies each used file into the workspace so the
build is self-contained. Every record is Public Domain (asserted + re-checked)."""
import json, os, sys, shutil, struct

WEB = "/workspace/history-hack-web-app/public"
BANK = WEB + "/data/us-history/primary-sources/images"

def jpeg_size(p):
    with open(p, "rb") as f:
        f.read(2)
        while True:
            b = f.read(1)
            while b and b[0] != 0xFF: b = f.read(1)
            if not b: return (0, 0)
            m = f.read(1)[0]
            if 0xC0 <= m <= 0xCF and m not in (0xC4, 0xC8, 0xCC):
                f.read(3); h = struct.unpack(">H", f.read(2))[0]; w = struct.unpack(">H", f.read(2))[0]
                return (w, h)
            l = struct.unpack(">H", f.read(2))[0]; f.read(l - 2)

MED_PRIORITY = {"political-cartoon": 0, "cartoon": 0, "photograph": 1, "portrait": 2,
                "poster": 3, "advertisement": 3, "map": 4}
MED_LABEL = {"political-cartoon": "political cartoon", "cartoon": "political cartoon"}

# Files whose PIXELS do not match their metadata title (verified by eye on the
# contact sheets) — the bank's rights are sound but a few records are mislabeled.
BLOCK = {
    "suffrage-awakening-1915.jpg",  # U3 US.22: actually a "Nature vs Corsets" health diagram
    "school-begins-1899.jpg",       # U3 US.27: actually a swamp/mosquito Puck cartoon, not the classroom cartoon
    "us-territorial-map-1900.jpg",  # U3 US.27: actually "View of Washington City," not a territorial map
    "dday-omaha-beach-1944.jpg",     # U6: used as the cover hero instead of the AP Iwo Jima; drop interior dup
    "migrant-mother-lange-1936.jpg", # U5: it is the cover hero; drop interior dup on US.41
    "freedmens_bureau_1868.jpg",     # U1 US.03: MISLABELED — actually a Pictorialist nude art photo, not the Freedmen's Bureau; inappropriate
    "nast_union_as_it_was_1874.jpg", # U1 US.03: MISLABELED — actually a "City of Washington" landscape print, not the Nast cartoon
}

def is_pd(r):
    return r.get("commercialUse") == "permitted" or "ublic" in (r.get("rightsLabel") or "")

def build(unit, order):
    bank = json.load(open(f"{BANK}/unit-{unit}.json"))
    ws = f"/home/user/Unit{unit}_Claude_Core"
    imgdir = f"{ws}/analysis/assets/img"
    os.makedirs(imgdir, exist_ok=True)
    # index images by standard (PD only)
    by_std = {}
    for r in bank:
        if not is_pd(r):
            print(f"  SKIP non-PD: {r.get('id')}"); continue
        if os.path.basename(r.get("src", "")) in BLOCK:
            print(f"  SKIP mislabeled: {os.path.basename(r['src'])}"); continue
        for s in (r.get("standardIds") or []):
            by_std.setdefault(s, []).append(r)
    used_ids = set()
    IMG = {}
    for code in order:
        cands = [r for r in by_std.get(code, []) if r["id"] not in used_ids]
        if not cands: continue
        cands.sort(key=lambda r: MED_PRIORITY.get(r.get("medium", ""), 5))
        r = cands[0]; used_ids.add(r["id"])
        srcfile = WEB + r["src"]
        if not os.path.exists(srcfile):
            print(f"  MISS file for {code}: {r['src']}"); continue
        base = os.path.basename(r["src"])
        shutil.copy(srcfile, f"{imgdir}/{base}")
        w, h = jpeg_size(srcfile)
        med = r.get("medium", "primary source")
        rec = {
            "file": f"analysis/assets/img/{base}", "w": w, "h": h,
            "medium": MED_LABEL.get(med, med),
            "title": r.get("title", ""), "creator": r.get("creator", ""),
            "year": str(r.get("year", "")),
            "citation": r.get("citationChicago", ""),
            "rights": r.get("rightsLabel", "Public domain"),
            "rightsUrl": r.get("rightsUrl", ""),
            "alt": r.get("alt") or r.get("caption") or r.get("title", ""),
            "caption": r.get("caption", ""),
        }
        if med == "map":
            rec["colorKey"] = True
        IMG[code] = {"anchor": rec}
    out = f"{ws}/analysis/unit{unit}_images.json"
    json.dump(IMG, open(out, "w"), ensure_ascii=False, indent=1)
    print(f"U{unit}: {len(IMG)}/{len(order)} standards get an image -> {out}")
    return IMG

if __name__ == "__main__":
    unit = int(sys.argv[1])
    content = json.load(open(f"/home/user/Unit{unit}_Claude_Core/analysis/unit{unit}_content.json"))
    build(unit, content["order"])
