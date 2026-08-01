# -*- coding: utf-8 -*-
"""Rebuild every Teacher Deck (re-embeds any images present in its asset folder)
and re-render its PDF, then refresh the deliverable copies. Run after
sync_images.py drops new primary sources in.

Usage: python3 BUILD/rebuild_decks.py
"""
import os, subprocess, glob, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

for deck in sorted(glob.glob(os.path.join(HERE, "decks", "Unit*_Teacher_Deck"))):
    name = os.path.basename(deck)
    unit = name.split("_")[0].replace("Unit", "")
    html = glob.glob(os.path.join(deck, "pages", "*.html"))
    subprocess.run(["python3", os.path.join(deck, "build_deck.py")],
                   cwd=deck, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    html = glob.glob(os.path.join(deck, "pages", "*.html"))
    if not html:
        print(f"{name}: no page built — skipped"); continue
    pdf = os.path.join(deck, "exports", f"{name}.pdf")
    subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf}", "file://" + html[0]],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # refresh deliverable copies
    deliv = os.path.join(ROOT, "BUILD", f"unit{unit}", "deliverables")
    os.makedirs(deliv, exist_ok=True)
    if os.path.exists(pdf):
        shutil.copy2(pdf, os.path.join(deliv, f"{name}.pdf"))
    # count embedded images (base64) in the html
    n_img = open(html[0]).read().count("data:image/")
    print(f"{name}: rebuilt · {n_img} image(s) embedded · PDF refreshed")
print("\nAll decks rebuilt. Drop more images in ASSETS/primary_sources/ and re-run sync + this script.")
