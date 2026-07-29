#!/usr/bin/env python3
"""Compile the complete Teacher Graphic Organizer Toolkit into one master PDF.

Order: front cover -> copyright/credits -> contents -> Units 1-10 (each unit's
combined PDF, in order) -> back cover. Renders the four brand pages in this
directory's pages/ with headless Chrome, then concatenates everything with pikepdf.

Run each unit's own `render.py pdf` first so the per-unit PDFs exist.
Usage:  python3 compile.py
"""
import os, subprocess, glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PAGES = os.path.join(HERE, "pages")
EXPORTS = os.path.join(HERE, "exports")
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
os.makedirs(EXPORTS, exist_ok=True)

BRAND = ["00_cover", "01_copyright", "02_contents"]  # front matter, in order
BACK = "99_backcover"


def render_pdf(name):
    src = os.path.join(PAGES, f"{name}.html")
    out = os.path.join(EXPORTS, f"_{name}.pdf")
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu",
                    "--hide-scrollbars", "--disable-dev-shm-usage",
                    "--no-pdf-header-footer", f"--print-to-pdf={out}", f"file://{src}"],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    return out


def unit_pdf(u):
    return os.path.join(ROOT, f"Unit{u}_Teacher_Graphic_Organizer_Toolkit",
                        "exports", f"Unit{u}_Teacher_Graphic_Organizer_Toolkit.pdf")


def main():
    order = [render_pdf(n) for n in BRAND]
    for u in range(1, 11):
        p = unit_pdf(u)
        if not os.path.exists(p):
            raise SystemExit(f"Missing {p} -- run that unit's `render.py pdf` first.")
        order.append(p)
    order.append(render_pdf(BACK))

    import pikepdf
    dst = pikepdf.Pdf.new()
    for f in order:
        with pikepdf.open(f) as src:
            dst.pages.extend(src.pages)
    with dst.open_metadata() as m:
        m["dc:title"] = ("U.S. History Hack — Teacher Graphic Organizer Toolkit "
                         "(Complete Series, Units 1–10)")
        m["dc:creator"] = ["Isabella Stuart"]
        m["dc:publisher"] = "TroopToTeacher Technologies LLC"
        m["dc:rights"] = "© 2026 TroopToTeacher Technologies LLC. All rights reserved."
    out = os.path.join(EXPORTS, "USHistoryHack_Teacher_Graphic_Organizer_Toolkit_Complete_Units1-10.pdf")
    dst.save(out)
    for n in BRAND + [BACK]:
        os.remove(os.path.join(EXPORTS, f"_{n}.pdf"))
    print(f"  wrote {out}  ({len(dst.pages)} pages)")


if __name__ == "__main__":
    main()
