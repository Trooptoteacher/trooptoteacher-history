# -*- coding: utf-8 -*-
"""Distribute dropped primary-source images from the ONE canonical bank
(ASSETS/primary_sources/) into every consumer so a single drop propagates:
  * each unit's Teacher Deck        -> BUILD/decks/UnitN_Teacher_Deck/assets/primary_sources/
  * each unit's workbook/cover       -> BUILD/unitN/assets/primary_sources/
  * the web edition                  -> WEB_EDITION/.../primary-sources/assets/primary_sources/
SVGs are rasterized to a .png sibling (for Word/docx, which can't embed SVG);
decks and web keep the original too. Reports what is present vs. still missing.

Usage:  python3 BUILD/sync_images.py            # sync everything present in the bank
        python3 BUILD/sync_images.py --report   # just list present/missing, no copy
"""
import os, sys, json, shutil, subprocess, glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)  # course root
CANON = os.path.join(ROOT, "ASSETS", "primary_sources")
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
REPORT = "--report" in sys.argv

sourcing = json.load(open(os.path.join(ROOT, "05_STANDARDS_ALIGNMENT", "primary_source_sourcing.json")))["sources"]
by_unit = {}
for s in sourcing:
    by_unit.setdefault(s["unit"], []).append(s)

def rasterize_svg(svg_path):
    """Render an SVG to a PNG sibling via headless Chromium (for docx)."""
    png = os.path.splitext(svg_path)[0] + ".png"
    if os.path.exists(png):
        return png
    try:
        subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu",
                        "--force-device-scale-factor=2", "--default-background-color=00000000",
                        "--window-size=800,800", f"--screenshot={png}", "file://" + os.path.abspath(svg_path)],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60)
        return png if os.path.exists(png) else None
    except Exception:
        return None

def copy_into(dest_dir, fname):
    src = os.path.join(CANON, fname)
    if not os.path.exists(src):
        return False
    os.makedirs(dest_dir, exist_ok=True)
    shutil.copy2(src, os.path.join(dest_dir, fname))
    if fname.lower().endswith(".svg"):
        png = rasterize_svg(src)
        if png:
            shutil.copy2(png, os.path.join(dest_dir, os.path.basename(png)))
    return True

WEB_ASSETS = os.path.join(ROOT, "WEB_EDITION", "public", "data", "government", "primary-sources", "assets", "primary_sources")
present_total, missing = 0, []
for unit, items in sorted(by_unit.items()):
    deck = os.path.join(ROOT, "BUILD", "decks", f"Unit{unit}_Teacher_Deck", "assets", "primary_sources")
    unitassets = os.path.join(ROOT, "BUILD", f"unit{unit}", "assets", "primary_sources")
    up, um = [], []
    for s in items:
        f = s["filename"]
        if os.path.exists(os.path.join(CANON, f)):
            present_total += 1; up.append(f)
            if not REPORT:
                copy_into(deck, f); copy_into(unitassets, f); copy_into(WEB_ASSETS, f)
        else:
            um.append(f); missing.append(f)
    print(f"Unit {unit}: {len(up)}/{len(items)} present" + (f"  · missing: {', '.join(x.split('_',1)[0] for x in um)}" if um else "  ✓ complete"))

print(f"\nTOTAL: {present_total}/{len(sourcing)} images in the bank." + (" All present — ready to rebuild." if not missing else f" {len(missing)} still to drop."))
if not REPORT and present_total:
    print("Synced into all deck / unit / web asset folders. Next: rebuild decks & docx to embed them.")
