"""Shared brand kit for US History Hack TpT documents."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FONT_DIR = os.path.join(os.path.dirname(__file__), "fonts")
LOGO = "/home/user/workspace/engine/channel_logo_circle.png"

# Brand palette — America 250 / new Air Force One livery (deep navy, white, federal red, gold)
NAVY   = colors.HexColor("#0A1F3C")   # deep Air Force One navy underside
NAVY2  = colors.HexColor("#14315A")
RED    = colors.HexColor("#B22234")   # Old Glory federal red
RED_D  = colors.HexColor("#8E1B29")   # deeper red for shadows
GOLD   = colors.HexColor("#C8A04B")   # muted military gold
GOLD_L = colors.HexColor("#E8C97A")
INK    = colors.HexColor("#1C1C1C")
SLATE  = colors.HexColor("#4A5568")
PAPER  = colors.HexColor("#F7F5EF")   # warm paper
LINE   = colors.HexColor("#D8D2C4")
WHITE  = colors.white
REDFLAG = colors.HexColor("#B22234")
GREENOK = colors.HexColor("#2F6B3A")

# ---- copyright / ownership (single source of truth) ----
COPYRIGHT_YEAR = "2026"
LLC            = "TroopToTeacher Technologies LLC"
COPYRIGHT      = "\u00a9 " + COPYRIGHT_YEAR + " " + LLC + ". All rights reserved."
COPYRIGHT_SHORT = "\u00a9 " + COPYRIGHT_YEAR + " " + LLC

def register_fonts():
    pdfmetrics.registerFont(TTFont("DMSans",       os.path.join(FONT_DIR, "DMSans-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("DMSans-Med",   os.path.join(FONT_DIR, "DMSans-Medium.ttf")))
    pdfmetrics.registerFont(TTFont("DMSans-Bold",  os.path.join(FONT_DIR, "DMSans-Bold.ttf")))
    pdfmetrics.registerFont(TTFont("Inter",        os.path.join(FONT_DIR, "Inter-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("Inter-Med",    os.path.join(FONT_DIR, "Inter-Medium.ttf")))
    # --- sketch-note / handwriting family (PROOF 4 anchor charts) ---
    _opt = {
        "Marker":       "PermanentMarkerAlt.ttf",   # Bangers - bold comic/marker display
        "HandBold":     "Kalam-Bold.ttf",           # bold handwriting (headings)
        "Hand":         "Kalam-Regular.ttf",        # handwriting (body)
        "HandPrint":    "PatrickHand-Regular.ttf",  # clean print handwriting
        "HandScript":   "Caveat-VF.ttf",            # casual script (accents/notes)
        "HandArch":     "ArchitectsDaughter-Regular.ttf",
    }
    for name, fn in _opt.items():
        p = os.path.join(FONT_DIR, fn)
        if os.path.exists(p):
            try:
                pdfmetrics.registerFont(TTFont(name, p))
            except Exception:
                pass

PAGE_W, PAGE_H = letter
MARGIN = 0.85 * inch
