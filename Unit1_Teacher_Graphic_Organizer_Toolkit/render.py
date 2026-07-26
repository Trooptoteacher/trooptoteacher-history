#!/usr/bin/env python3
"""Render toolkit HTML pages -> cropped 2x PNGs (letter, 1632x2112) and a combined PDF.
Usage:
  python3 render.py png [page1.html page2.html ...]   # default: all pages/*.html
  python3 render.py pdf                               # combined PDF of all pages in order
"""
import os, sys, subprocess, glob, struct

ROOT = os.path.dirname(os.path.abspath(__file__))
PAGES = os.path.join(ROOT, "pages")
EXPORTS = os.path.join(ROOT, "exports")
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
SCALE = 2
PAGE_W, PAGE_H = 816 * SCALE, 1056 * SCALE  # letter @96dpi, 2x
os.makedirs(EXPORTS, exist_ok=True)

def chrome(args):
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu",
                    "--hide-scrollbars", "--disable-dev-shm-usage"] + args,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def render_png(html):
    from PIL import Image
    base = os.path.splitext(os.path.basename(html))[0]
    raw = os.path.join(EXPORTS, f"_{base}_raw.png")
    out = os.path.join(EXPORTS, f"{base}.png")
    # --window-size is in CSS px; DSF scales the output. Width == page width (no
    # centering gap); height a bit taller than the page so nothing clips, then crop.
    win_w, win_h = 816, 1180
    chrome([f"--force-device-scale-factor={SCALE}", f"--window-size={win_w},{win_h}",
            f"--screenshot={raw}", f"file://{html}"])
    img = Image.open(raw).convert("RGB")
    img = img.crop((0, 0, min(PAGE_W, img.width), min(PAGE_H, img.height)))
    img.save(out)
    os.remove(raw)
    print(f"  png {out}  {img.size}")
    return out

def render_pdf_combined():
    # Build a combined PDF by rendering each page HTML to PDF then concatenating.
    htmls = sorted(glob.glob(os.path.join(PAGES, "*.html")))
    parts = []
    for h in htmls:
        base = os.path.splitext(os.path.basename(h))[0]
        p = os.path.join(EXPORTS, f"_{base}.pdf")
        chrome(["--no-pdf-header-footer", f"--print-to-pdf={p}", f"file://{h}"])
        parts.append(p)
    out = os.path.join(EXPORTS, "Unit1_Teacher_Graphic_Organizer_Toolkit.pdf")
    concat_pdfs(parts, out)
    for p in parts:
        os.remove(p)
    print(f"  pdf {out}")

def concat_pdfs(parts, out):
    # Minimal PDF merge (pypdf if present, else naive via ghostscript/pdfunite if available).
    try:
        from pypdf import PdfWriter
        w = PdfWriter()
        for p in parts:
            w.append(p)
        with open(out, "wb") as f:
            w.write(f)
        return
    except Exception:
        pass
    for tool in (["pdfunite"], ["gs", "-dBATCH", "-dNOPAUSE", "-q", "-sDEVICE=pdfwrite"]):
        from shutil import which
        if which(tool[0]):
            if tool[0] == "pdfunite":
                subprocess.run(tool + parts + [out], check=True)
            else:
                subprocess.run(tool + [f"-sOutputFile={out}"] + parts, check=True)
            return
    raise SystemExit("No PDF merge tool (install pypdf).")

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "png"
    if mode == "png":
        files = sys.argv[2:] or sorted(glob.glob(os.path.join(PAGES, "*.html")))
        for f in files:
            f = f if os.path.isabs(f) else os.path.join(PAGES, os.path.basename(f))
            print(f"render {os.path.basename(f)}")
            render_png(f)
    elif mode == "pdf":
        render_pdf_combined()
