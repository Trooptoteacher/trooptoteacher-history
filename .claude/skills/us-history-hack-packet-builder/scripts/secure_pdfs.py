"""
Secure US History Hack PDFs for TpT sale.
- Stamps a copyright/license watermark footer on EVERY page (travels with screenshots & reprints).
- Encrypts with an OWNER password + restrictive permissions:
    * NO content copying / extraction
    * NO modification / editing
    * NO annotation, NO form fill, NO assembly
    * Printing ALLOWED (TpT requires buyers can print)
    * NO user password (file opens normally — TpT requirement)
- Sets locked metadata (author/owner).

Usage: python3 secure_pdfs.py <input.pdf> <output.pdf>
"""
import sys, os, io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject

FONT_DIR = os.path.join(os.path.dirname(__file__), "fonts")
pdfmetrics.registerFont(TTFont("Inter", os.path.join(FONT_DIR, "Inter-Regular.ttf")))
pdfmetrics.registerFont(TTFont("Inter-Med", os.path.join(FONT_DIR, "Inter-Medium.ttf")))

# Owner password — controls permissions. NOT needed by buyers to open.
# Stored only here; the buyer never sees or needs it.
OWNER_PW = "HistoryHack-TTT-Owner-2026"

NAVY = colors.HexColor("#0F2A47")
GOLD = colors.HexColor("#C8A04B")

WATERMARK = "© TroopToTeacher Technologies LLC  •  Single-Classroom License  •  Not for resale or redistribution"

def make_overlay(w, h):
    """One footer-strip overlay sized to the page."""
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(w, h))
    # subtle footer band watermark
    c.setFont("Inter", 6.7)
    c.setFillColor(colors.Color(0.06, 0.16, 0.28, alpha=0.55))
    c.drawCentredString(w/2, 0.22*inch, WATERMARK)
    # faint diagonal ownership mark, very low opacity so it never blocks content
    c.saveState()
    c.translate(w/2, h/2)
    c.rotate(35)
    c.setFont("Inter-Med", 40)
    c.setFillColor(colors.Color(0.06, 0.16, 0.28, alpha=0.05))
    c.drawCentredString(0, 0, "US HISTORY HACK")
    c.restoreState()
    c.save()
    buf.seek(0)
    return PdfReader(buf).pages[0]

def secure(src, dst):
    reader = PdfReader(src)
    writer = PdfWriter()
    for page in reader.pages:
        w = float(page.mediabox.width); h = float(page.mediabox.height)
        overlay = make_overlay(w, h)
        page.merge_page(overlay)
        writer.add_page(page)

    writer.add_metadata({
        "/Title": os.path.basename(dst).replace("_", " ").replace(".pdf", ""),
        "/Author": "TroopToTeacher Technologies LLC",
        "/Creator": "US History Hack",
        "/Producer": "US History Hack — TroopToTeacher Technologies LLC",
        "/Copyright": "© TroopToTeacher Technologies LLC. All Rights Reserved.",
    })

    # Encrypt: empty USER pw (opens freely), strong OWNER pw, AES-256, locked perms.
    # permissions_flag controls what's allowed. We allow PRINT (high-res) only.
    from pypdf.constants import UserAccessPermissions as P
    perms = P.PRINT | P.PRINT_TO_REPRESENTATION  # printing allowed; everything else denied
    writer.encrypt(
        user_password="",
        owner_password=OWNER_PW,
        algorithm="AES-256",
        permissions_flag=perms,
    )
    with open(dst, "wb") as f:
        writer.write(f)
    print(f"SECURED: {os.path.basename(dst)}  ({os.path.getsize(dst)//1024} KB)")

if __name__ == "__main__":
    secure(sys.argv[1], sys.argv[2])
