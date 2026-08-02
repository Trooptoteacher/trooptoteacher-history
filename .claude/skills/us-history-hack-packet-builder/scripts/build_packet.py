"""
US History Hack — For-Sale Packet Assembler (repeatable workflow)

Bundles every for-sale product into one branded, secured PDF in this order:
    1. Meet the Author        (About pp.1-3: bio, credentials, TN standards, ELL, ecosystem + app QR)
    2. Copyright & Terms       (Terms of Use, full)
    3. Content                 (the workbook: Student / Teacher / Diff Pack / etc.)
    4. How to Download & Print (About p.4)

Then stamps a slim brand strip (store name + app link) on EVERY page, and runs the
result through secure_pdfs.secure() for the copyright watermark + AES-256 encryption.

Usage:
    python3 build_packet.py <content.pdf> <output_basename>
    # e.g. python3 build_packet.py source/HH_Unit01_Student.pdf US_History_Hack_Unit1_Student_Workbook

Front/back matter are rebuilt fresh each run from build_about.py + build_terms.py outputs,
so any edit to those scripts automatically flows into every future packet.
"""
import sys, os, io, subprocess
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader, PdfWriter

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "fonts")
ABOUT = os.path.join(HERE, "US_History_Hack_About_The_Author.pdf")   # 4 pages
TERMS = os.path.join(HERE, "US_History_Hack_Terms_of_Use.pdf")
ASSEMBLED_DIR = os.path.join(HERE, "assembled")
SECURED_DIR = os.path.join(HERE, "secured")
APP_URL = "https://apps.apple.com/us/app/u-s-history-hack-1877-present/id6757368709"

os.makedirs(ASSEMBLED_DIR, exist_ok=True)
os.makedirs(SECURED_DIR, exist_ok=True)

pdfmetrics.registerFont(TTFont("DMSans-Med", os.path.join(FONT_DIR, "DMSans-Medium.ttf")))
pdfmetrics.registerFont(TTFont("Inter", os.path.join(FONT_DIR, "Inter-Regular.ttf")))

from reportlab.lib import colors
NAVY = colors.HexColor("#1F3A5F")
GOLD = colors.HexColor("#C8A04B")


def rebuild_frontback():
    """Rebuild About + Terms so any edits flow through automatically."""
    subprocess.run([sys.executable, os.path.join(HERE, "build_about.py")], check=True, cwd=HERE)
    subprocess.run([sys.executable, os.path.join(HERE, "build_terms.py")], check=True, cwd=HERE)


def brand_strip_overlay(w, h):
    """Slim brand strip just above the security footer: store name (left) + app link (right)."""
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(w, h))
    yb = 0.40 * inch  # sits above the 0.22in security watermark line
    c.setFont("DMSans-Med", 6.8)
    c.setFillColor(colors.Color(0.04, 0.12, 0.24, alpha=0.70))
    c.drawString(0.6 * inch, yb, "U.S. History Hack 1877\u2013Present")
    c.setFont("Inter", 6.8)
    c.setFillColor(colors.Color(0.04, 0.12, 0.24, alpha=0.62))
    label = "Get the app: apps.apple.com  \u2022  trooptoteacher.com"
    c.drawRightString(w - 0.6 * inch, yb, label)
    # clickable app-link hotspot over the strip
    c.linkURL(APP_URL, (w - 2.6 * inch, yb - 2, w - 0.6 * inch, yb + 8), relative=0)
    c.save()
    buf.seek(0)
    return PdfReader(buf).pages[0]


def add_pages(writer, reader, brand=True):
    for page in reader.pages:
        if brand:
            w = float(page.mediabox.width); h = float(page.mediabox.height)
            page.merge_page(brand_strip_overlay(w, h))
        writer.add_page(page)


def assemble(content_pdf, out_basename):
    rebuild_frontback()
    about = PdfReader(ABOUT)            # p0-2 front, p3 download/print
    terms = PdfReader(TERMS)
    content = PdfReader(content_pdf)

    writer = PdfWriter()
    # 1. Meet the Author (About pages 1-3)
    front = PdfWriter(); [front.add_page(about.pages[i]) for i in range(3)]
    buf = io.BytesIO(); front.write(buf); buf.seek(0)
    add_pages(writer, PdfReader(buf))
    # 2. Copyright & Terms
    add_pages(writer, terms)
    # 3. Content
    add_pages(writer, content)
    # 4. How to Download & Print (About page 4)
    back = PdfWriter(); back.add_page(about.pages[3])
    buf2 = io.BytesIO(); back.write(buf2); buf2.seek(0)
    add_pages(writer, PdfReader(buf2))

    assembled_path = os.path.join(ASSEMBLED_DIR, out_basename + ".pdf")
    with open(assembled_path, "wb") as f:
        writer.write(f)
    print(f"ASSEMBLED: {assembled_path}  ({os.path.getsize(assembled_path)//1024} KB, {len(writer.pages)} pages)")
    return assembled_path


def main():
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(1)
    content_pdf = sys.argv[1]
    out_basename = sys.argv[2].replace(".pdf", "")
    assembled = assemble(content_pdf, out_basename)
    # secure (watermark + encryption) into secured/
    import secure_pdfs
    secured_path = os.path.join(SECURED_DIR, out_basename + ".pdf")
    secure_pdfs.secure(assembled, secured_path)
    print(f"DONE -> {secured_path}")


if __name__ == "__main__":
    main()
