#!/usr/bin/env python3
"""
Source & Asset Standards Crosswalk (course-agnostic).

Rolls every primary source and visual asset up against the standard it supports,
so a course has one auditable list of "what sources/images/maps/charts we use and
which standard each serves." Captures geographic positions where the standard
calls for geography.

Inputs (per course, same layout as U.S. History Hack):
  build_*/<unit>_content.json  — text primary sources (sources[]) + geo/geo_places
  build_*/<unit>_images.json   — image assets per standard (anchor, map, …)

Outputs (written next to the course tree, under guardrails/crosswalk/):
  asset_crosswalk.csv   — one row per (standard, asset)
  asset_crosswalk.md    — human-readable crosswalk + coverage summary

Coverage gates (exit non-zero with --strict):
  - every standard has >=1 primary-source anchor
  - every image asset has a citation AND rights/license
  - every geography standard (geo set) has geo_places (positions captured)
  - WARN: a geography standard with no map asset

Usage:
  python3 asset_standards_crosswalk.py [/path/to/CourseTree] [--strict]
"""
import json, os, sys, glob, csv

argv = sys.argv[1:]
strict = "--strict" in argv
roots = [a for a in argv if not a.startswith("--")]
ROOT = roots[0] if roots else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "crosswalk")
os.makedirs(OUT, exist_ok=True)

MAP_MEDIA = {"map"}
CHART_MEDIA = {"chart", "graph", "data", "diagram", "infographic"}

def load(path):
    try: return json.load(open(path, encoding="utf8"))
    except Exception: return {}

# pair content + images by unit directory
units = {}
for f in glob.glob(os.path.join(ROOT, "build_*", "*_content.json")):
    units.setdefault(os.path.dirname(f), {})["content"] = f
for f in glob.glob(os.path.join(ROOT, "build_*", "*_images.json")):
    units.setdefault(os.path.dirname(f), {})["images"] = f

rows = []            # (unit, std, kind, slot, medium, title, creator, year, cited, rights, geo_positions)
gaps = {"no_anchor": [], "asset_no_citation": [], "asset_no_rights": [],
        "geo_no_positions": [], "geo_no_map": []}

def asset_medium(rec, slot):
    m = (rec.get("medium") or "").lower()
    if slot == "map" or m in MAP_MEDIA: return "map"
    if m in CHART_MEDIA: return m
    return m or "image"

for udir in sorted(units):
    content = load(units[udir].get("content", "")) if units[udir].get("content") else {}
    images = load(units[udir].get("images", "")) if units[udir].get("images") else {}
    std = content.get("standards", {})
    unit = os.path.basename(udir)
    for code in content.get("order", list(std.keys())):
        s = std.get(code, {})
        has_geo = bool(s.get("geo") and str(s.get("geo")).strip())
        places = len(s.get("geo_places") or [])
        geo_positions = str(places) if has_geo else "n/a"

        # 1) text primary sources from content
        for i, src in enumerate(s.get("sources") or []):
            rows.append((unit, code, "text-source", f"source{i+1}", "document",
                         src.get("title", ""), src.get("who", ""), src.get("date", ""),
                         "Y" if src.get("quote") or src.get("title") else "N", "quoted-in-text",
                         geo_positions))

        # 2) image assets from images JSON (anchor, map, and any other dict slots with a file/title)
        img = images.get(code, {})
        img_slots = [(k, v) for k, v in img.items() if isinstance(v, dict) and (v.get("file") or v.get("title"))]
        anchor_present = any(k == "anchor" for k, _ in img_slots)
        has_map = False
        for slot, rec in img_slots:
            med = asset_medium(rec, slot)
            if med == "map": has_map = True
            cited = "Y" if rec.get("citation") else "N"
            rights = rec.get("rights", "") or ""
            rows.append((unit, code, "image", slot, med, rec.get("title", ""),
                         rec.get("creator", ""), str(rec.get("year", "")), cited,
                         rights or "MISSING", geo_positions))
            if not rec.get("citation"): gaps["asset_no_citation"].append(f"{code}/{slot}")
            if not rights: gaps["asset_no_rights"].append(f"{code}/{slot}")

        if not anchor_present and not (s.get("sources")):
            gaps["no_anchor"].append(code)
        if has_geo and places == 0: gaps["geo_no_positions"].append(code)
        if has_geo and not has_map: gaps["geo_no_map"].append(code)

# write CSV
csv_path = os.path.join(OUT, "asset_crosswalk.csv")
with open(csv_path, "w", newline="", encoding="utf8") as fh:
    w = csv.writer(fh)
    w.writerow(["unit", "standard", "kind", "slot", "medium", "title", "creator/who",
                "year/date", "cited", "rights/license", "geo_positions"])
    w.writerows(rows)

# coverage summary
n_std = len({(u, c) for (u, c, *_r) in rows}) or 0
n_img = sum(1 for r in rows if r[2] == "image")
n_map = sum(1 for r in rows if r[4] == "map")
n_chart = sum(1 for r in rows if r[4] in CHART_MEDIA)
n_text = sum(1 for r in rows if r[2] == "text-source")

md = [f"# Source & Asset Standards Crosswalk — {os.path.basename(ROOT)}", "",
      f"- Standards with assets: **{n_std}**",
      f"- Text primary sources: **{n_text}**  ·  Images: **{n_img}**  ·  Maps: **{n_map}**  ·  Charts/graphs: **{n_chart}**",
      "", "## Coverage gaps", ""]
labels = {"no_anchor": "Standards with NO primary source (text or image)",
          "asset_no_citation": "Image assets missing a citation",
          "asset_no_rights": "Image assets missing rights/license",
          "geo_no_positions": "Geography standards with NO geo_places (positions not captured)",
          "geo_no_map": "Geography standards with no map asset (WARN)"}
any_hard = False
for k in ["no_anchor", "asset_no_citation", "asset_no_rights", "geo_no_positions", "geo_no_map"]:
    v = sorted(set(gaps[k]))
    mark = "✅" if not v else ("⚠️" if k == "geo_no_map" else "⛔")
    if v and k != "geo_no_map": any_hard = True
    md.append(f"- {mark} **{labels[k]}:** {', '.join(v) if v else 'none'}")
md += ["", "## Full crosswalk", "",
       "| Unit | Std | Kind | Slot | Medium | Title | Creator/Who | Year | Cited | Rights | Geo pos |",
       "|---|---|---|---|---|---|---|---|---|---|---|"]
for r in rows:
    md.append("| " + " | ".join(str(x).replace("|", "/") for x in r) + " |")
open(os.path.join(OUT, "asset_crosswalk.md"), "w", encoding="utf8").write("\n".join(md))

print(f"WROTE {csv_path}")
print(f"WROTE {os.path.join(OUT, 'asset_crosswalk.md')}")
print(f"standards={n_std} text_sources={n_text} images={n_img} maps={n_map} charts={n_chart}")
for k in gaps:
    if gaps[k]:
        print(f"  {labels[k]}: {len(set(gaps[k]))} -> {', '.join(sorted(set(gaps[k]))[:12])}")
if strict and any_hard:
    print("\nFAIL (--strict): hard coverage gaps present.")
    sys.exit(1)
