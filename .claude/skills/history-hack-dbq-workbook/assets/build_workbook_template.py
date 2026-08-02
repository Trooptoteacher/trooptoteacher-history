# =============================================================================
# History Hack Platinum Workbook — ReportLab engine TEMPLATE
# -----------------------------------------------------------------------------
# This is the canonical build engine, generalized from the validated Unit 1
# U.S. History DBQ Workbook. To template a new unit/subject:
#   1) Update the SET / metadata block (unit title, DBQ title, standards, name).
#   2) Swap the document sources, charts, maps, and Tennessee Connection source.
#   3) Keep the two-pass marker mechanism (TOCMarker/XWMarker + make_pdf loop)
#      and the page furniture UNCHANGED — never hardcode page numbers.
#   4) Glue any artifact-specific XWMarker INSIDE the KeepTogether with its image
#      (see references/engine-conventions.md — the KeepTogether marker bug).
# The living source of truth is the History-Hack-US-History-Workbooks GitHub repo;
# this bundled copy is a starting point when that repo is unavailable.
# =============================================================================
#!/usr/bin/env python3
"""
History Hack — Unit 1 DBQ Workbook (Print Master, Pilot)
TroopToTeacher Technologies LLC

Print-first, off-screen companion to the online History Hack unit.
100% original / public-domain source content, expanded from the app's
already-vetted Unit 1 primary sources. No third-party (Pearson) content.

AI & ML Expert's least-cost call: pure programmatic assembly (ReportLab),
no premium model — highest fidelity to vetted data, ~zero model cost.
"""
import json, os, urllib.request
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, FrameBreak, NextPageTemplate, HRFlowable, Image as RLImage
)
from PIL import Image as PILImage
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "fonts")
os.makedirs(FONT_DIR, exist_ok=True)

# ---------- brand palette (History Hack: navy / red / gold) ----------
NAVY   = colors.HexColor("#1F3A5F")
NAVY2  = colors.HexColor("#2C3E63")
RED    = colors.HexColor("#B22234")
GOLD   = colors.HexColor("#C9A227")
INK    = colors.HexColor("#1A1A1A")
MUTED  = colors.HexColor("#555555")
BORDER = colors.HexColor("#C9C2B4")
CARD   = colors.HexColor("#F8F5EF")
LIGHT  = colors.HexColor("#EEF2F8")
WHITE  = colors.white
RULE   = colors.HexColor("#9AA3B2")

# ---------- fonts (embed DM Sans + Source Serif) ----------
FONTS = {
    "DMSans-Regular": "https://github.com/googlefonts/dm-fonts/raw/main/Sans/exports/DMSans-Regular.ttf",
    "DMSans-Bold":    "https://github.com/googlefonts/dm-fonts/raw/main/Sans/exports/DMSans-Bold.ttf",
    "DMSans-Medium":  "https://github.com/googlefonts/dm-fonts/raw/main/Sans/exports/DMSans-Medium.ttf",
    "SourceSerif-Regular": "https://github.com/adobe-fonts/source-serif/raw/release/TTF/SourceSerif4-Regular.ttf",
    "SourceSerif-Bold":    "https://github.com/adobe-fonts/source-serif/raw/release/TTF/SourceSerif4-Bold.ttf",
    "SourceSerif-It":      "https://github.com/adobe-fonts/source-serif/raw/release/TTF/SourceSerif4-It.ttf",
}
def ensure_fonts():
    reg = {}
    for name, url in FONTS.items():
        path = os.path.join(FONT_DIR, name + ".ttf")
        if not os.path.exists(path):
            try:
                urllib.request.urlretrieve(url, path)
            except Exception as e:
                print("WARN font dl", name, e)
        if os.path.exists(path):
            pdfmetrics.registerFont(TTFont(name, path))
            reg[name] = True
    return reg

REG = ensure_fonts()
# fallbacks if a download failed
HEAD  = "DMSans-Bold" if "DMSans-Bold" in REG else "Helvetica-Bold"
HEADM = "DMSans-Medium" if "DMSans-Medium" in REG else "Helvetica-Bold"
BODYF = "DMSans-Regular" if "DMSans-Regular" in REG else "Helvetica"
SERIF = "SourceSerif-Regular" if "SourceSerif-Regular" in REG else "Times-Roman"
SERIFB= "SourceSerif-Bold" if "SourceSerif-Bold" in REG else "Times-Bold"
SERIFI= "SourceSerif-It" if "SourceSerif-It" in REG else "Times-Italic"

STORE = "U.S. History Hack"
APP_URL = "https://apps.apple.com/app/history-hack"
COPYRIGHT = "\u00A9 2026 TroopToTeacher Technologies LLC \u2014 U.S. History Hack. All rights reserved. Licensed for single-classroom use. Do not redistribute."
LOGO_PATH = os.path.join(HERE, "images", "ushh_logo_circle.png")

# ---------- load data ----------
sources = json.load(open(os.path.join(HERE, "unit-1-sources.json")))
by_title = {s["documentTitle"]: s for s in sources}

# ---------------------------------------------------------------------------
# Unit 1 covers SEVEN TN standards (US.01-US.07). This workbook contains ONE
# focused DBQ built on US.01-US.06, PLUS a short US.07 document set so the
# workbook as a whole covers all seven standards of Unit 1 honestly.
# ---------------------------------------------------------------------------
SET = {
    "unit": "Unit 1",
    "unit_title": "The Rise of Industrialization (1877\u20131900)",
    "unit_overview": ("Students will analyze the transformation of the American economy and the "
                      "changing social and political conditions in the United States in response to the rise of "
                      "industrialization, large-scale rural-to-urban migration, and mass immigration from "
                      "Southern and Eastern Europe and Asia."),
    "dbq_number": "DBQ 1",
    "title": "Growth and Its Costs: Was Gilded Age America \u201cProgress\u201d for All?",
    # HONEST LABEL: this DBQ is a focused subset of the unit's standards.
    "standards": "Focused DBQ \u2014 TN Standards US.01\u2013US.06",
    "unit_standards": "Full Unit 1 spans TN Standards US.01\u2013US.07",
    "time": "Suggested time: 55\u201360 minutes",
    "prompt": ("Between 1862 and 1900, the United States expanded across the continent, "
               "industrialized rapidly, and grew enormously in wealth and population. "
               "Using the documents below and your knowledge of U.S. History, evaluate the "
               "extent to which this growth represented genuine \u201cprogress\u201d \u2014 and for whom. "
               "Support your argument with evidence from at least four of the six documents."),
    "docs": [
        "Homestead Act", "Pacific Railway Act", "Dawes General Allotment Act",
        "Plessy v. Ferguson Decision", "The Gospel of Wealth", "How the Other Half Lives",
    ],
    # US.07 companion set (completes Unit 1's seven standards)
    "us07_docs": ["Chinese Exclusion Act", "Twenty Years at Hull-House"],
    "us07_title": "Old and New Immigration: Who Was Welcome in Industrial America?",
    "us07_prompt": ("As industrial cities grew, the United States debated who belonged. "
                    "Using the two documents below and your knowledge of U.S. History, explain how "
                    "Americans responded to the 'new' immigration of the late 1800s \u2014 in law and in "
                    "the settlement-house movement."),
}

# ---------- image pairings (all public-domain, from Drive image library) ----------
IMG_DIR = os.path.join(HERE, "images", "print")
# maps documentTitle -> (filename, caption, short source credit)
DOC_IMAGES = {
    "Homestead Act": (
        "US.01_rawding-sod-house.jpg",
        "The Rawding family in front of their Nebraska sod house, 1886 \u2014 Homestead Act "
        "settlement on the Great Plains.",
        "Solomon D. Butcher, 1886. Library of Congress, Prints & Photographs Division. Public domain."),
    "Pacific Railway Act": (
        "US.01_chinese-central-pacific-workers.jpg",
        "Chinese laborers grade and lay track for the Central Pacific Railroad through the Sierra "
        "Nevada \u2014 the majority of the Central Pacific workforce.",
        "Alfred A. Hart (attrib.), c. 1865\u20131869. National Park Service, Golden Spike NHP. Public domain."),
    "Dawes General Allotment Act": (
        "US.02_tom-torlino-carlisle.jpg",
        "Navajo student Tom Torlino, before (1882) and after (1885) enrollment at the Carlisle "
        "Indian Industrial School \u2014 the most reproduced image of federal assimilation policy.",
        "John N. Choate, 1882 & 1885. Beinecke Library, Yale (via Wikimedia Commons). Public domain."),
    "Plessy v. Ferguson Decision": (
        "US.03_nast-worse-than-slavery.jpg",
        "Thomas Nast, 'The Union as It Was \u2014 Worse Than Slavery,' Harper's Weekly, Oct. 24, 1874, "
        "indicting the terror campaign that ended Reconstruction.",
        "Thomas Nast, 1874. Library of Congress, Prints & Photographs Division. Public domain."),
    "The Gospel of Wealth": (
        "US.04_standard-oil-octopus.jpg",
        "Udo Keppler, 'Next!' Puck, Sept. 7, 1904 \u2014 Standard Oil as an octopus whose tentacles wrap the "
        "statehouse and U.S. Capitol and reach for the White House; the era's most famous image of concentrated wealth.",
        "Udo J. Keppler, 'Next!', Puck, Sept. 7, 1904. Library of Congress, Prints & Photographs Division "
        "(digital ID ppmsca.25884); no known restrictions on publication. Reproduced from the flattened "
        "single-plate scan; magazine gutter and margins removed, image content unaltered."),
    "How the Other Half Lives": (
        "US.05_tenement_housing_riis_1890.jpg",
        "Jacob Riis's photograph of New York City tenement conditions, c. 1890 \u2014 the images that "
        "forced middle-class America to see tenement poverty.",
        "Jacob A. Riis, c. 1890. Museum of the City of New York. Public domain."),
    "Chinese Exclusion Act": (
        "US.07_five-cents-a-spot-riis.jpg",
        "Jacob Riis, 'Five Cents a Spot,' 1889 \u2014 crowded immigrant lodgings in a Bayard Street "
        "tenement, from How the Other Half Lives (1890).",
        "Jacob A. Riis, 1889. Library of Congress, Prints & Photographs Division. Public domain."),
    "Twenty Years at Hull-House": (
        "US.06_ellis-island-immigrants.jpg",
        "The inspection room at Ellis Island, c. 1910\u20131920, where more than twelve million "
        "immigrants were processed between 1892 and 1954.",
        "Detroit Publishing Co., c. 1910\u20131920. Library of Congress, Prints & Photographs Division. Public domain."),
}

MAPS_DIR = os.path.join(HERE, "images", "maps")
CHARTS_DIR = os.path.join(HERE, "images", "charts")

def full_image_flowable(path, max_w, max_h=None, caption=None, credit=None, alt=None):
    """Place a full-width image (chart or map) with a source-caption box beneath it.
    `alt` is a short plain-language description folded into the caption for accessibility."""
    if not os.path.exists(path):
        return []
    iw, ih = PILImage.open(path).size
    ratio = iw/ih
    w = max_w
    h = w/ratio
    if max_h and h > max_h:
        h = max_h
        w = h*ratio
    img = RLImage(path, width=w, height=h)
    img.hAlign = "CENTER"
    flow = [Spacer(1,6), img]
    if caption or credit or alt:
        parts = []
        if caption:
            parts.append(f"<b>{caption}</b>")
        if alt:
            parts.append(f"<i>What it shows:</i> {alt}")
        if credit:
            parts.append(f"<font size=7 color='#777777'>{credit}</font>")
        cap = Paragraph(" &mdash; ".join(parts) if len(parts) > 1 else parts[0],
                        S("fullcap", fontName=BODYF, fontSize=8.5, leading=12, textColor=MUTED, alignment=TA_LEFT))
        capbox = Table([[cap]], colWidths=[max_w])
        capbox.setStyle(TableStyle([
            ("BACKGROUND",(0,0),(-1,-1),colors.HexColor("#F2EFE8")),
            ("LINEABOVE",(0,0),(-1,-1),0.5,BORDER),
            ("LEFTPADDING",(0,0),(-1,-1),8),("RIGHTPADDING",(0,0),(-1,-1),8),
            ("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5),
        ]))
        flow += [Spacer(1,2), capbox]
    return flow

def sentence_starter(text, width=None):
    """Accessibility scaffold: a bordered sentence-frame box with a blank write line."""
    w = width if width else (PAGE_W-2*MARGIN)
    p = Paragraph(f"<b>Sentence starter:</b> <i>{text}</i>", S("ss", fontName=SERIFI, fontSize=10, leading=14, textColor=NAVY))
    box = Table([[p]], colWidths=[w])
    box.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),LIGHT),
        ("BOX",(0,0),(-1,-1),0.8,NAVY),
        ("LEFTPADDING",(0,0),(-1,-1),9),("RIGHTPADDING",(0,0),(-1,-1),9),
        ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6),
        ("LINEBEFORE",(0,0),(0,-1),3,GOLD),
    ]))
    return [KeepTogether([box, Spacer(1,4), WriteLines(2, width=w)])]

def numbered_tasks(items, width=None):
    """A numbered list of guided-question tasks with write lines after each.
    Each question+writelines pair is kept together so WriteLines never has to
    split across a page break (its Table subclass can't be re-instantiated by
    ReportLab's auto-split machinery)."""
    w = width if width else (PAGE_W-2*MARGIN)
    flow = []
    for i, q in enumerate(items, 1):
        flow.append(KeepTogether([Paragraph(f"<b>{i}.</b> {q}", st_q), WriteLines(2, width=w, gap=16)]))
        flow.append(Spacer(1,2))
    return flow

def tn_banner(width=None):
    """BOLD branded Tennessee Connection banner — signature series element.
    Navy field, gold border + left rule, red accent tab, gold small-caps title,
    grayscale-legible (relies on value contrast, not hue)."""
    w = width if width else (PAGE_W-2*MARGIN)
    title = Paragraph("TENNESSEE CONNECTION", S("tnbanner_title", fontName=HEAD, fontSize=16,
                       leading=19, textColor=GOLD, alignment=TA_LEFT))
    subtitle = Paragraph("A U.S. History Hack&trade; signature feature &mdash; local primary sources, "
                          "state-specific standards alignment, and Tennessee history no national "
                          "publisher builds for your classroom.",
                          S("tnbanner_sub", fontName=BODYF, fontSize=9.5, leading=13,
                            textColor=colors.HexColor("#E7EAF2"), alignment=TA_LEFT))
    inner = Table([[title],[subtitle]], colWidths=[w-0.34*inch-18])
    inner.setStyle(TableStyle([
        ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
        ("TOPPADDING",(0,0),(0,0),0),("BOTTOMPADDING",(0,0),(0,0),3),
        ("TOPPADDING",(0,1),(0,1),0),("BOTTOMPADDING",(0,1),(0,1),0),
    ]))
    banner = Table([[inner]], colWidths=[w])
    banner.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),NAVY),
        ("BOX",(0,0),(-1,-1),1.6,GOLD),
        ("LINEBEFORE",(0,0),(0,-1),7,RED),
        ("LEFTPADDING",(0,0),(-1,-1),16),("RIGHTPADDING",(0,0),(-1,-1),12),
        ("TOPPADDING",(0,0),(-1,-1),10),("BOTTOMPADDING",(0,0),(-1,-1),10),
    ]))
    return banner

def doc_image_flowable(title, max_w, max_h=2.35*inch):
    """Return [Image, caption-table] flowables for a document, or [] if none."""
    info = DOC_IMAGES.get(title)
    if not info:
        return []
    fn, caption, credit = info
    path = os.path.join(IMG_DIR, fn)
    if not os.path.exists(path):
        return []
    iw, ih = PILImage.open(path).size
    ratio = iw/ih
    w = max_w
    h = w/ratio
    if h > max_h:
        h = max_h
        w = h*ratio
    img = RLImage(path, width=w, height=h)
    img.hAlign = "CENTER"
    cap = Paragraph(f"<b>Image \u2014</b> {caption} <i><font size=7 color='#777777'>{credit}</font></i>",
                    S("imcap", fontName=BODYF, fontSize=8, leading=11, textColor=MUTED, alignment=TA_LEFT))
    capbox = Table([[cap]], colWidths=[max_w])
    capbox.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),colors.HexColor("#F2EFE8")),
        ("LINEABOVE",(0,0),(-1,-1),0.5,BORDER),
        ("LEFTPADDING",(0,0),(-1,-1),6),("RIGHTPADDING",(0,0),(-1,-1),6),
        ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4),
    ]))
    return [Spacer(1,6), img, Spacer(1,2), capbox]

# ---- which documents ARE the visual source (analyzed as its own document, OPTIC) ----
# For these, the image is a primary source in its own right and gets a full standalone
# OPTIC analysis box (Overview, Parts, Title/Text, Interrelationships, Conclusion) —
# the College Board scores political cartoons and photographs as full documents.
VISUAL_IS_PRIMARY = {
    "Plessy v. Ferguson Decision",   # Nast, "Worse Than Slavery" (1874) political cartoon
    "The Gospel of Wealth",          # Keppler, "Next!" Standard Oil octopus (1904) cartoon
    "How the Other Half Lives",      # Riis tenement photograph (c.1890)
}

def optic_box(title, letter_id, W):
    """Standalone OPTIC visual-source analysis for the paired image, treated as its own document."""
    info = DOC_IMAGES.get(title)
    if not info or title not in VISUAL_IS_PRIMARY:
        return []
    fn, caption, credit = info
    rows = []
    for lab, hint in [
        ("O \u2014 Overview", "In one sentence, what does this image show at first glance?"),
        ("P \u2014 Parts", "List the specific people, objects, symbols, and details you notice."),
        ("T \u2014 Title / Text", "What do the title, caption, or any words tell you about the message?"),
        ("I \u2014 Interrelationships", "How do the parts connect? What is the artist/photographer arguing?"),
        ("C \u2014 Conclusion", "What is the creator's point of view and purpose? Who is the audience?"),
    ]:
        rows.append([Paragraph(f"<b>{lab}</b><br/><font size=7 color='#777777'>{hint}</font>", st_small), ""])
    ot = Table(rows, colWidths=[1.9*inch, W-1.9*inch], rowHeights=[0.62*inch]*5)
    ot.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("GRID",(0,0),(-1,-1),0.5,BORDER),
        ("BACKGROUND",(0,0),(0,-1),colors.HexColor("#F3EEDF")),
        ("LEFTPADDING",(0,0),(-1,-1),6),("TOPPADDING",(0,0),(-1,-1),5),
    ]))
    intro = Paragraph(
        "<b>This image is a document too.</b> Analyze it on its own with OPTIC \u2014 just as the AP exam "
        "treats political cartoons and photographs as full sources requiring point-of-view and purpose analysis.",
        st_tnote)
    return [Spacer(1,8),
            Paragraph("Visual Source \u2014 Analyze With OPTIC", st_h2),
            intro, ot]

# fuller verbatim public-domain excerpts (expanded from the same vetted sources)
FULLER = {
    "Homestead Act": (
        "Any person who is the head of a family, or who has arrived at the age of "
        "twenty-one years, and is a citizen of the United States, or who shall have filed "
        "his declaration of intention to become such, as required by the naturalization laws "
        "\u2026 shall \u2026 be entitled to enter one quarter section [160 acres] or a less quantity "
        "of unappropriated public lands \u2026 That the person applying for the benefit of this act "
        "shall \u2026 make affidavit \u2026 that such application is made for his or her exclusive use "
        "and benefit, and that said entry is made for the purpose of actual settlement and "
        "cultivation, and not \u2026 for the use or benefit of any other person."
    ),
    "Pacific Railway Act": (
        "That the right of way through the public lands be, and the same is hereby, granted "
        "to said company for the construction of said railroad and telegraph line \u2026 and the "
        "right \u2026 is hereby given to said company to take from the public lands adjacent \u2026 "
        "earth, stone, timber, and other materials for the construction thereof; said right of way "
        "is granted to said railroad to the extent of two hundred feet in width on each side "
        "\u2026 That there be, and is hereby, granted to the said company \u2026 every alternate "
        "section of public land \u2026 to the amount of five alternate sections per mile on each side."
    ),
    "Dawes General Allotment Act": (
        "That in all cases where any tribe or band of Indians has been \u2026 located upon any "
        "reservation \u2026 the President \u2026 is hereby authorized \u2026 to allot the lands in said "
        "reservation in severalty to any Indian located thereon in quantities as follows: To each "
        "head of a family, one-quarter of a section \u2026 And every Indian born within the territorial "
        "limits of the United States to whom allotments shall have been made \u2026 is hereby declared "
        "to be a citizen of the United States \u2026 Provided, That the Secretary of the Interior may "
        "\u2026 sell \u2026 such portions of the lands of said reservation \u2026 as \u2026 not needed."
    ),
    "Plessy v. Ferguson Decision": (
        "The object of the [Fourteenth] amendment was undoubtedly to enforce the absolute "
        "equality of the two races before the law, but in the nature of things it could not have "
        "been intended to abolish distinctions based upon color, or to enforce social, as "
        "distinguished from political, equality \u2026 Laws permitting, and even requiring, their "
        "separation in places where they are liable to be brought into contact do not necessarily "
        "imply the inferiority of either race \u2026 We consider the underlying fallacy of the "
        "plaintiff's argument to consist in the assumption that the enforced separation of the two "
        "races stamps the colored race with a badge of inferiority."
    ),
    "The Gospel of Wealth": (
        "This, then, is held to be the duty of the man of wealth \u2026 to consider all surplus "
        "revenues which come to him simply as trust funds, which he is called upon to administer "
        "\u2026 in the manner which, in his judgment, is best calculated to produce the most beneficial "
        "results for the community \u2026 The man who dies thus rich dies disgraced. Such, in my "
        "opinion, is the true Gospel concerning Wealth, obedience to which is destined some day to "
        "solve the problem of the rich and the poor."
    ),
    "How the Other Half Lives": (
        "The tenements grew into a smoldering heap of contradictions \u2026 In the tenements all "
        "the influences make for evil \u2026 that we know. \u2026 Suppose we look into one [tenement] \u2026 "
        "Be a little careful, please! The hall is dark and you might stumble \u2026 Here is a door. "
        "Listen! That short, hacking cough, that tiny, helpless wail\u2014what do they mean? \u2026 The "
        "child is dying with measles. With half a chance it might have lived; but it had none."
    ),
}

# ---------------- styles ----------------
def S(name, **kw):
    return ParagraphStyle(name, **kw)

st_cover_kicker = S("ck", fontName=HEADM, fontSize=13, textColor=GOLD, alignment=TA_CENTER, spaceAfter=6, tracking=2)
st_cover_title  = S("ct", fontName=HEAD, fontSize=30, leading=36, textColor=WHITE, alignment=TA_CENTER, spaceAfter=10)
st_cover_sub    = S("cs", fontName=BODYF, fontSize=13, leading=18, textColor=colors.HexColor("#D8DEEA"), alignment=TA_CENTER)
st_cover_foot   = S("cf", fontName=BODYF, fontSize=9, leading=13, textColor=colors.HexColor("#AEB7C7"), alignment=TA_CENTER)

st_h1     = S("h1", fontName=HEAD, fontSize=17, leading=21, textColor=NAVY, spaceBefore=4, spaceAfter=6)
st_h2     = S("h2", fontName=HEAD, fontSize=12.5, leading=16, textColor=RED, spaceBefore=8, spaceAfter=4)
st_label  = S("lb", fontName=HEADM, fontSize=9, leading=12, textColor=NAVY, spaceAfter=2)
st_body   = S("bd", fontName=BODYF, fontSize=10.5, leading=15, textColor=INK, alignment=TA_LEFT, spaceAfter=6)
st_bodyj  = S("bj", fontName=BODYF, fontSize=10.5, leading=15, textColor=INK, alignment=TA_JUSTIFY, spaceAfter=6)
st_source = S("src", fontName=SERIF, fontSize=11, leading=16.5, textColor=INK, alignment=TA_JUSTIFY, spaceAfter=4, leftIndent=6, rightIndent=6)
st_cite   = S("cit", fontName=SERIFI, fontSize=8.5, leading=12, textColor=MUTED, spaceBefore=3)
st_gloss  = S("gl", fontName=BODYF, fontSize=8.8, leading=12.5, textColor=INK)
st_q      = S("q", fontName=HEADM, fontSize=10, leading=14, textColor=INK, spaceBefore=4, spaceAfter=2, leftIndent=2)
st_small  = S("sm", fontName=BODYF, fontSize=8.5, leading=12, textColor=MUTED)
st_tnote  = S("tn", fontName=BODYF, fontSize=9.5, leading=14, textColor=INK, spaceAfter=5)

PAGE_W, PAGE_H = letter
MARGIN = 0.72*inch

# ---------------- writing lines ----------------
class WriteLines(Table):
    def __init__(self, n=4, width=PAGE_W-2*MARGIN, gap=22, **kw):
        # Tolerate ReportLab's internal re-instantiation during table splitting,
        # which calls self.__class__(data, colWidths=..., rowHeights=..., ...).
        if "colWidths" in kw and kw["colWidths"]:
            width = kw["colWidths"][0]
        if isinstance(n, list):
            n = len(n)
        rows = [[""] for _ in range(n)]
        super().__init__(rows, colWidths=[width], rowHeights=[gap]*n)
        self.setStyle(TableStyle([
            ("LINEBELOW",(0,0),(-1,-1),0.6,RULE),
            ("TOPPADDING",(0,0),(-1,-1),0),
            ("BOTTOMPADDING",(0,0),(-1,-1),0),
            ("LEFTPADDING",(0,0),(-1,-1),0),
        ]))

def hbox(flowables, pad=8, bg=CARD, border=BORDER, width=PAGE_W-2*MARGIN):
    t = Table([[flowables]], colWidths=[width])
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),bg),
        ("BOX",(0,0),(-1,-1),0.8,border),
        ("LEFTPADDING",(0,0),(-1,-1),pad),("RIGHTPADDING",(0,0),(-1,-1),pad),
        ("TOPPADDING",(0,0),(-1,-1),pad),("BOTTOMPADDING",(0,0),(-1,-1),pad),
    ]))
    return t

def accent_bar(text, color=NAVY, tc=WHITE, size=12, width=PAGE_W-2*MARGIN):
    p = Paragraph(text, S("bar", fontName=HEAD, fontSize=size, leading=size+3, textColor=tc))
    t = Table([[p]], colWidths=[width])
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),color),
        ("LEFTPADDING",(0,0),(-1,-1),9),("RIGHTPADDING",(0,0),(-1,-1),9),
        ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6),
        ("LINEBEFORE",(0,0),(0,-1),3,GOLD),
    ]))
    return t

# ---------------- page decoration (header/footer) ----------------
# NOTE: diagonal watermark removed per author request (keep copyright footer only).
US07_START_PAGE = 10**9  # set after first build pass; page where US.07 set begins
GEO_START_PAGE = 10**9   # set after first build pass; page where the geography/charts/a11y sections begin

# ---- Table of Contents page-capture dict (two-pass mechanism, mirrors US07Marker/GeoSectionMarker) ----
# Keyed by a short section id -> page number recorded on the PRIOR build pass.
# TOCMarker() flowables record into this dict as they are drawn; section_toc() reads the dict
# to render the TOC's page-number column. Because the TOC page appears BEFORE the sections it
# lists, the numbers it prints on a given pass reflect the PRIOR pass's layout -- so we run one
# extra warm-up pass (3 total) to guarantee the dict is fully populated and stable before the
# final render.
TOC_PAGES = {}

# ---- TN Standards Crosswalk marker dict (same mechanism, separate namespace for clarity) ----
# Keys: US01a, US01b, US02, US03, US05, US06, US07, US07b, US07syn, CHART, MAPNAT, MAPTN, ORG
# Populated by XWMarker() flowables placed at the TOP of each anchor section/document.
XW = {}

def content_page(c, doc):
    c.saveState()
    # top rule
    c.setStrokeColor(GOLD); c.setLineWidth(2)
    c.line(MARGIN, PAGE_H-0.55*inch, PAGE_W-MARGIN, PAGE_H-0.55*inch)
    c.setFont(HEADM, 8.5); c.setFillColor(NAVY)
    c.drawString(MARGIN, PAGE_H-0.5*inch, "U.S. HISTORY HACK  \u2022  DBQ WORKBOOK")
    if doc.page >= GEO_START_PAGE:
        section = "Geography, Data & Skills"
    elif doc.page >= US07_START_PAGE:
        section = "US.07 Document Set"
    else:
        section = SET["dbq_number"]
    c.drawRightString(PAGE_W-MARGIN, PAGE_H-0.5*inch, SET["unit"] + "  \u2022  " + section)
    # footer
    c.setStrokeColor(BORDER); c.setLineWidth(0.6)
    c.line(MARGIN, 0.6*inch, PAGE_W-MARGIN, 0.6*inch)
    c.setFont(BODYF, 7); c.setFillColor(MUTED)
    c.drawString(MARGIN, 0.44*inch, COPYRIGHT)
    c.setFont(HEADM, 8.5); c.setFillColor(NAVY)
    c.drawRightString(PAGE_W-MARGIN, 0.44*inch, str(doc.page))
    c.restoreState()

def cover_page(c, doc):
    c.saveState()
    c.setFillColor(NAVY); c.rect(0,0,PAGE_W,PAGE_H, fill=1, stroke=0)
    c.setFillColor(NAVY2); c.rect(0, PAGE_H-3.5*inch, PAGE_W, 3.5*inch, fill=1, stroke=0)
    c.setStrokeColor(GOLD); c.setLineWidth(3)
    c.line(MARGIN, PAGE_H-1.05*inch, PAGE_W-MARGIN, PAGE_H-1.05*inch)
    c.line(MARGIN, 1.15*inch, PAGE_W-MARGIN, 1.15*inch)
    c.setFillColor(RED); c.rect(0,0,0.28*inch,PAGE_H, fill=1, stroke=0)
    c.restoreState()

# ---------------- build story ----------------
def build():
    story = []
    W = PAGE_W-2*MARGIN

    # ---- COVER ----
    logo_flow = []
    if os.path.exists(LOGO_PATH):
        lg = RLImage(LOGO_PATH, width=1.55*inch, height=1.55*inch)
        lg.hAlign = "CENTER"
        logo_flow = [lg, Spacer(1, 0.18*inch)]
    story += [Spacer(1, 0.95*inch),
              *logo_flow,
              Paragraph("DOCUMENT-BASED QUESTION WORKBOOK", st_cover_kicker),
              Spacer(1, 0.12*inch),
              Paragraph(SET["unit_title"], st_cover_title),
              Spacer(1, 0.15*inch),
              Paragraph("Print Edition &nbsp;\u2022&nbsp; Off-Screen Companion to the U.S. History Hack Online Unit", st_cover_sub),
              Spacer(1, 0.14*inch),
              Paragraph(SET["unit_overview"], S("covov", fontName=SERIFI, fontSize=10.5, leading=15, textColor=colors.HexColor("#C7CEDC"), alignment=TA_CENTER)),
              Spacer(1, 0.12*inch),
              Paragraph(SET["unit_standards"], st_cover_sub),
              Spacer(1, 0.04*inch),
              Paragraph("Featured DBQ: US.01\u2013US.06 &nbsp;\u2022&nbsp; US.07 Document Set included", st_cover_foot),
              Spacer(1, 2.05*inch),
              Paragraph("TroopToTeacher Technologies LLC", S("cb", fontName=HEAD, fontSize=13, textColor=GOLD, alignment=TA_CENTER, spaceAfter=10)),
              Paragraph("A no-device, paper-first way to do rigorous source analysis.", st_cover_foot),
              Spacer(1, 3),
              Paragraph("Master copy \u2014 licensed for single-classroom printing.", st_cover_foot)]
    story += [NextPageTemplate("content"), PageBreak()]

    # ---- COPYRIGHT / EDITION PAGE (front matter, before How to Use) ----
    story += section_copyright(W)

    # ---- TABLE OF CONTENTS (front matter, before How to Use) ----
    story += section_toc(W)

    # ---- TENNESSEE STANDARDS ALIGNMENT (new; after TOC, before How to Use) ----
    story += section_crosswalk(W)

    # ---- ACCESSIBILITY & ACCOMMODATIONS (new; after crosswalk, before How to Use) ----
    story += section_accommodations(W)

    # ---- HOW TO USE ----
    story += [TOCMarker("how_to_use")]
    story += [Paragraph("How to Use This Workbook", st_h1),
              HRFlowable(width=W, thickness=1, color=GOLD, spaceAfter=8),
              Paragraph("This workbook lets students do the same document-based analysis found in the online "
                        "U.S. History Hack unit \u2014 entirely on paper. It is built for classrooms reducing screen time: "
                        "print one master copy, photocopy for your class, and students write directly in the workbook.", st_tnote)]
    steps = [
        ("1. Read the prompt", "Every DBQ opens with a central question. Read it first so you know what you are arguing."),
        ("2. Analyze each document with HIPPO", "For each source, complete the HIPPO box \u2014 Historical context, Intended audience, Purpose, Point of view, and the main idea. HIPPO is how you interrogate a single source."),
        ("3. Answer the guided questions", "Short questions check your understanding and pull out usable evidence."),
        ("4. Write your argument with C-E-R", "At the end, use the Claim\u2013Evidence\u2013Reasoning organizer to build a full response that uses at least four documents. CER is how you turn source analysis into an argument."),
    ]
    rows = [[Paragraph(f"<b>{t}</b>", st_label), Paragraph(d, st_body)] for t,d in steps]
    tbl = Table(rows, colWidths=[1.9*inch, W-1.9*inch])
    tbl.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("LINEBELOW",(0,0),(-1,-2),0.5,BORDER),
        ("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7),
        ("BACKGROUND",(0,0),(0,-1),LIGHT),
        ("LEFTPADDING",(0,0),(-1,-1),8),
    ]))
    story += [Spacer(1,4), tbl, Spacer(1,12)]
    story += [hbox([Paragraph("<b>HIPPO vs. CER \u2014 two different jobs.</b> HIPPO is a <i>reading</i> tool you use "
                              "on each document. CER is a <i>writing</i> tool you use once at the end, across all the "
                              "documents, to make your argument. You analyze first, then you argue.", st_tnote)],
                   bg=colors.HexColor("#FBF3E4"), border=GOLD)]
    story += [PageBreak()]

    # ---- DBQ TITLE + PROMPT ----
    story += [TOCMarker("central_q")]
    story += [accent_bar(f"{SET['dbq_number']} &nbsp;&mdash;&nbsp; {SET['title']}", color=NAVY, size=13),
              Spacer(1,8),
              Paragraph(f"<b>{SET['standards']}</b> &nbsp;|&nbsp; {SET['time']}", st_small),
              Paragraph("<i>This DBQ is a focused subset of Unit 1. A US.07 immigration document set follows so the full workbook covers all seven Unit 1 standards.</i>", st_small),
              Spacer(1,8),
              Paragraph("The Central Question", st_h2),
              hbox([Paragraph(SET["prompt"], st_bodyj)], bg=LIGHT, border=NAVY),
              Spacer(1,8),
              TOCMarker("roster"),
              Paragraph("Document Roster", st_h2)]
    st_thead = S("th", fontName=HEADM, fontSize=9, leading=12, textColor=WHITE)
    st_rdoc  = S("rd", fontName=HEADM, fontSize=9.5, leading=13, textColor=NAVY)
    roster = [[Paragraph(f"Doc {chr(65+i)}", st_rdoc),
               Paragraph(by_title[t]["documentTitle"], st_body),
               Paragraph(by_title[t]["author"], st_small),
               Paragraph(by_title[t]["date"], st_small)] for i,t in enumerate(SET["docs"])]
    rtbl = Table([[Paragraph("#",st_thead),Paragraph("Document",st_thead),
                   Paragraph("Author / Source",st_thead),Paragraph("Date",st_thead)]]+roster,
                  colWidths=[0.6*inch, 2.7*inch, W-0.6*inch-2.7*inch-1.3*inch, 1.3*inch])
    rtbl.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("BACKGROUND",(0,0),(-1,0),NAVY),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[WHITE, CARD]),
        ("GRID",(0,0),(-1,-1),0.5,BORDER),
        ("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5),
        ("LEFTPADDING",(0,0),(-1,-1),6),
    ]))
    story += [rtbl, Spacer(1,12)]

    # ---- PERSPECTIVES REPRESENTED MAP ----
    story += [Paragraph("Perspectives Represented in This Document Set", st_h2),
              Paragraph("A strong DBQ set is built to hold competing points of view. As you read, notice "
                        "whose voice each document carries \u2014 and whose it leaves out.", st_tnote)]
    persp = [
        ["Document", "Whose perspective"],
        ["Homestead Act (Doc A)", "The federal government and white settlers \u2014 expansion framed as opportunity."],
        ["Pacific Railway Act (Doc B)", "Government and railroad corporations \u2014 with Chinese labor visible in the paired image."],
        ["Dawes Act (Doc C)", "Federal assimilation policy imposed on Native nations \u2014 the Native experience of forced 'allotment.'"],
        ["Plessy v. Ferguson (Doc D)", "The Supreme Court majority upholding segregation \u2014 counterposed by the Nast cartoon's Black perspective."],
        ["The Gospel of Wealth (Doc E)", "The industrialist elite \u2014 wealth as stewardship (Carnegie), critiqued by the 'Next!' cartoon."],
        ["How the Other Half Lives (Doc F)", "The urban immigrant and working poor \u2014 seen through a reformer's lens (Riis)."],
    ]
    st_ph = S("ph", fontName=HEADM, fontSize=9, leading=12, textColor=WHITE)
    prows = []
    for idx,(a,b) in enumerate(persp):
        if idx==0:
            prows.append([Paragraph(a,st_ph),Paragraph(b,st_ph)])
        else:
            prows.append([Paragraph(f"<b>{a}</b>",st_small),Paragraph(b,st_small)])
    ptbl = Table(prows, colWidths=[2.3*inch, W-2.3*inch])
    ptbl.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("BACKGROUND",(0,0),(-1,0),NAVY),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[WHITE,CARD]),
        ("GRID",(0,0),(-1,-1),0.5,BORDER),
        ("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5),("LEFTPADDING",(0,0),(-1,-1),6),
    ]))
    story += [ptbl, Spacer(1,8),
              hbox([Paragraph("<b>Missing voices \u2014 a question for you.</b> Which perspectives are <i>not</i> "
                              "directly represented here (for example, Native voices in their own words, or women "
                              "workers)? Naming a 'missing voice' is exactly the kind of outside-evidence move the "
                              "AP DBQ rewards.", st_tnote)], bg=colors.HexColor("#FBF3E4"), border=GOLD)]
    story += [PageBreak()]

    # ---- DOCUMENT PAGES (DBQ US.01-US.06) ----
    story += [TOCMarker("doc_set")]
    DOC_XW_KEYS = ["US01a", "US01b", "US02", "US03", "US05", "US06"]
    for i, t in enumerate(SET["docs"]):
        story += build_doc_page(t, chr(65+i), W, xw_key=DOC_XW_KEYS[i])

    # ---- CER ESSAY ORGANIZER ----
    story += [accent_bar("Build Your Argument \u2014 Claim \u2022 Evidence \u2022 Reasoning", color=NAVY, size=13),
              Spacer(1,8),
              Paragraph("Now use the documents you analyzed to answer the Central Question. Your response must "
                        "use evidence from <b>at least four</b> of the six documents.", st_tnote),
              Spacer(1,4),
              Paragraph("Restate the Central Question in your own words:", st_label), WriteLines(2), Spacer(1,6),
              Paragraph("CLAIM \u2014 your overall answer/argument", st_h2), WriteLines(3), Spacer(1,4),
              Paragraph("EVIDENCE \u2014 specific details from the documents (cite Doc A\u2013F)", st_h2), WriteLines(6)]
    story += [PageBreak(),
              Paragraph("REASONING \u2014 explain how each piece of evidence supports your claim", st_h2), WriteLines(8),
              Spacer(1,6),
              Paragraph("COUNTERPOINT \u2014 what is the strongest argument against your claim, and why is your claim still stronger?", st_h2),
              WriteLines(5)]
    story += [PageBreak(),
              accent_bar("Full Response", color=RED, size=12), Spacer(1,6),
              Paragraph("Write your complete essay below. Use the organizer on the previous pages.", st_tnote),
              WriteLines(20)]
    story += [PageBreak(),
              accent_bar("Teacher Notes & Scoring", color=NAVY, size=12), Spacer(1,8),
              Paragraph("Beginner On-Ramp Rubric \u2014 C-E-R (4 points)", st_h2),
              Paragraph("<i>This simplified 4-point rubric is a classroom on-ramp for students new to DBQs. The "
                        "industry-standard instrument \u2014 the College Board AP 7-point DBQ rubric \u2014 is provided in "
                        "the accompanying Teacher's Guide and should be used for graded/AP-aligned work.</i>", st_small)]
    rub = [["Score","Descriptor"],
           ["4 \u2014 Exceeds","Clear claim; accurate evidence from 4+ documents; reasoning explicitly links evidence to claim; addresses counterpoint."],
           ["3 \u2014 Meets","Clear claim; evidence from at least 4 documents; reasoning present for most evidence."],
           ["2 \u2014 Approaching","Claim present; evidence from 2\u20133 documents; limited reasoning."],
           ["1 \u2014 Beginning","Vague/absent claim; minimal or inaccurate document use."]]
    st_rubh = S("rh", fontName=HEADM, fontSize=9, leading=12, textColor=WHITE)
    rub_rows = []
    for idx,(a,b) in enumerate(rub):
        if idx==0:
            rub_rows.append([Paragraph(a,st_rubh),Paragraph(b,st_rubh)])
        else:
            rub_rows.append([Paragraph(f"<b>{a}</b>",st_small),Paragraph(b,st_small)])
    rt = Table(rub_rows, colWidths=[1.5*inch, W-1.5*inch])
    rt.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("BACKGROUND",(0,0),(-1,0),NAVY),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[WHITE,CARD]),
        ("GRID",(0,0),(-1,-1),0.5,BORDER),
        ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6),("LEFTPADDING",(0,0),(-1,-1),6),
    ]))
    story += [rt, Spacer(1,10),
              Paragraph("Online correlation: this DBQ mirrors the Unit 1 primary-source set in the U.S. History Hack app "
                        "(standards US.01\u2013US.06). The US.07 immigration set that follows completes the unit's "
                        "seven standards. Assign digitally or print \u2014 the documents match.", st_small)]

    # ============ US.07 COMPANION DOCUMENT SET ============
    story += [PageBreak(),
              US07Marker(),
              TOCMarker("us07_set"),
              accent_bar(f"US.07 Document Set &nbsp;&mdash;&nbsp; {SET['us07_title']}", color=NAVY, size=13),
              Spacer(1,8),
              Paragraph("<b>TN Standard US.07</b> &nbsp;|&nbsp; Completes Unit 1's seven standards", st_small),
              Spacer(1,8),
              Paragraph("The Central Question", st_h2),
              hbox([Paragraph(SET["us07_prompt"], st_bodyj)], bg=LIGHT, border=NAVY),
              Spacer(1,6),
              Paragraph("Read both documents, complete each HIPPO box, then answer the synthesis question at the end of this set.", st_tnote),
              PageBreak()]
    US07_XW_KEYS = ["US07", "US07b"]
    for j, t in enumerate(SET["us07_docs"]):
        story += build_doc_page(t, chr(65+j), W, xw_key=US07_XW_KEYS[j])
    # US.07 short synthesis
    story += [XWMarker("US07syn"),
              accent_bar("US.07 \u2014 Synthesis", color=RED, size=12), Spacer(1,6),
              Paragraph(SET["us07_prompt"], st_tnote),
              Paragraph("Write a short response (one paragraph) using BOTH documents:", st_label),
              WriteLines(9)]

    # ============ NEW: GEOGRAPHY, CHARTS & ACCESSIBILITY SECTIONS ============
    # Placed after the full document set (DBQ + US.07), before any back matter.
    story += [GeoSectionMarker()]
    story += section_charts(W)
    story += section_national_map(W)
    story += section_tn_connection(W)
    story += section_organizer(W)

    return story

from reportlab.platypus import Flowable
class US07Marker(Flowable):
    """Zero-height flowable that records the page where the US.07 set begins."""
    def __init__(self):
        super().__init__(); self.width = 0; self.height = 0
    def draw(self):
        global US07_START_PAGE
        pg = self.canv.getPageNumber()
        if pg < US07_START_PAGE:
            US07_START_PAGE = pg

class GeoSectionMarker(Flowable):
    """Zero-height flowable that records the page where the geography/charts/a11y sections begin."""
    def __init__(self):
        super().__init__(); self.width = 0; self.height = 0
    def draw(self):
        global GEO_START_PAGE
        pg = self.canv.getPageNumber()
        if pg < GEO_START_PAGE:
            GEO_START_PAGE = pg

class TOCMarker(Flowable):
    """Zero-height flowable that records the page where a named TOC-listed section begins.
    Mirrors US07Marker/GeoSectionMarker exactly, but is keyed (many sections, one shared dict)
    instead of a single global int."""
    def __init__(self, key):
        super().__init__(); self.width = 0; self.height = 0; self.key = key
    def draw(self):
        pg = self.canv.getPageNumber()
        # always take the FIRST page a section's marker is seen on, per pass
        TOC_PAGES[self.key] = pg

class XWMarker(Flowable):
    """Zero-height flowable for the TN Standards Crosswalk. Mirrors TOCMarker exactly,
    but writes into the XW dict so the crosswalk table can look up real page numbers
    for documents / sections that are not already 1:1 with a TOC_PAGES entry (e.g.
    individual Documents A-F, individual US.07 sub-documents, the synthesis prompt)."""
    def __init__(self, key):
        super().__init__(); self.width = 0; self.height = 0; self.key = key
    def draw(self):
        pg = self.canv.getPageNumber()
        if self.key not in XW or pg < XW[self.key]:
            XW[self.key] = pg

# ---- shared document-page builder (used by DBQ docs and US.07 docs) ----
def build_doc_page(t, letter_id, W, xw_key=None):
    s = by_title[t]
    excerpt = FULLER.get(t, s["excerpt"])
    block = []
    if xw_key:
        block += [XWMarker(xw_key)]
    block += [accent_bar(f"Document {letter_id}", color=RED, size=12)]
    block += [Spacer(1,6),
              Paragraph(s["documentTitle"], st_h1),
              Paragraph(f"<b>{s['author']}</b> &nbsp;\u2022&nbsp; {s['date']}", st_small),
              Spacer(1,4)]
    block += [hbox([Paragraph(excerpt, st_source)], bg=colors.HexColor("#FCFBF7"), border=NAVY)]
    block += [Paragraph(f"Source: {s['author']}, <i>{s['documentTitle']}</i>, {s['date']}. Public domain.", st_cite)]
    # paired public-domain image
    block += doc_image_flowable(t, W)
    story2 = [KeepTogether(block)]
    # glossary
    terms = s.get("bracketedTerms", [])
    if terms:
        gl = " &nbsp;&nbsp;|&nbsp;&nbsp; ".join(
            f"<b>{x['term']}</b>: {x['definition']} <font color='#888888'>(ES: {x.get('termEs','')} \u2014 {x.get('definitionEs','')})</font>"
            for x in terms)
        story2 += [Spacer(1,4), Paragraph("Key Terms", st_label),
                   hbox([Paragraph(gl, st_gloss)], bg=LIGHT, border=BORDER, pad=6)]
    # standalone OPTIC visual-source analysis (only when the image is a primary source in its own right)
    story2 += optic_box(t, letter_id, W)
    story2 += [Spacer(1,8), Paragraph("HIPPO \u2014 Analyze This Source", st_h2)]
    hippo_rows = []
    for lab, hint in [("H \u2014 Historical Context","What was happening at the time?"),
                      ("I \u2014 Intended Audience","Who was meant to read/hear this?"),
                      ("P \u2014 Purpose","Why was it created?"),
                      ("P \u2014 Point of View","Whose perspective? What bias?"),
                      ("O \u2014 Outside/Main Idea","In one sentence, what does it say?")]:
        hippo_rows.append([Paragraph(f"<b>{lab}</b><br/><font size=7 color='#777777'>{hint}</font>", st_small), ""])
    ht = Table(hippo_rows, colWidths=[1.9*inch, W-1.9*inch], rowHeights=[0.46*inch]*5)
    ht.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("GRID",(0,0),(-1,-1),0.5,BORDER),
        ("BACKGROUND",(0,0),(0,-1),colors.HexColor("#EDEFF4")),
        ("LEFTPADDING",(0,0),(-1,-1),6),("TOPPADDING",(0,0),(-1,-1),5),
    ]))
    story2 += [ht]
    story2 += [Spacer(1,8), Paragraph("Guided Question", st_h2),
               Paragraph(s["question"], st_q), WriteLines(2)]
    story2 += [PageBreak()]
    return story2

# ============================================================================
# NEW SECTIONS — geography, charts, accessibility (inserted after US.07 set,
# before any back matter). Reuses existing helpers/palette/fonts only.
# ============================================================================

def section_charts(W):
    """SECTION 1 — Reading the Data: Charts & Graphs (US.06/US.07 evidence)."""
    story = [TOCMarker("reading_data"), XWMarker("CHART")]
    story += [accent_bar("Reading the Data &nbsp;&mdash;&nbsp; Charts &amp; Graphs", color=NAVY, size=13),
             Spacer(1,8),
             Paragraph("Extends US.06&ndash;US.07 &nbsp;|&nbsp; Secondary-source data analysis", st_small),
             Paragraph("<i>These two charts are secondary-source data visualizations built from U.S. Census "
                       "Bureau and U.S. Immigration and Naturalization Service (INS) public-domain statistics. "
                       "Treat them as documents: read the axes and labels the way you would read a written source.</i>",
                       st_tnote),
             Spacer(1,4)]
    story += full_image_flowable(
        os.path.join(CHARTS_DIR, "chart_immigration_by_decade.png"), W, max_h=2.6*inch,
        caption="Immigrants Admitted to the United States, by Decade, 1861\u20131900",
        alt="A bar chart showing the number of immigrants admitted each decade from 1861 to 1900, "
            "with the bars rising sharply toward the end of the century.",
        credit="U.S. Census Bureau / INS. Public domain.")
    story += [Spacer(1,10)]
    _urban = full_image_flowable(
        os.path.join(CHARTS_DIR, "chart_urbanization.png"), W, max_h=2.6*inch,
        caption="Urban Share of the U.S. Population, 1860\u20131900",
        alt="A line chart showing the percentage of Americans living in cities climbing steadily "
            "from 1860 to 1900.",
        credit="U.S. Census Bureau / INS. Public domain.")
    # Keep the CHART_URBAN marker glued to the urbanization image so it records the
    # image's REAL page (the block may break to the next page as a unit).
    story += [KeepTogether([XWMarker("CHART_URBAN")] + _urban)]
    story += [Spacer(1,10),
              Paragraph("Analyze the Data", st_h2)]
    story += numbered_tasks([
        "Which decade saw the largest jump in immigration? By roughly how many people did it grow?",
        "Describe the trend in urban population from 1860 to 1900. What in the documents you read helps explain it?",
        "How do these two data sets connect to each other? Write one sentence linking immigration and urban growth.",
    ], width=W)
    story += sentence_starter("The data shows ______ because ______.", width=W)
    return story


def section_national_map(W):
    """SECTION 2 — Mapping the Nation: Geographic Reasoning (SSP.06, national map)."""
    story = [PageBreak(),
             TOCMarker("mapping"), XWMarker("MAPNAT"),
             accent_bar("Mapping the Nation &nbsp;&mdash;&nbsp; Geographic Reasoning", color=NAVY, size=13),
             Spacer(1,6),
             Paragraph("SSP.06 &nbsp;|&nbsp; Spatial &amp; geographic reasoning with primary-source maps", st_small),
             Paragraph("<i>This 1892 map shows the land-grant and bond-aided railroads authorized by Congress "
                       "under laws like the Pacific Railway Act (Document B). The land grants in that document "
                       "are the dark bands and lines you see below &mdash; the policy made visible on a map.</i>",
                       st_tnote),
             Spacer(1,1)]
    story += full_image_flowable(
        os.path.join(MAPS_DIR, "US_railroads_landgrant_1892_loc.jpg"), W, max_h=3.55*inch,
        caption="Map of Land-Grant and Bond-Aided Railroads of the United States, 1892",
        alt="A national map of the United States with railroad lines drawn across the country, "
            "concentrated most heavily west of the Mississippi River and across the northern and "
            "southern transcontinental corridors.",
        credit="Library of Congress, Geography and Map Division, 1892. Public domain.")
    story += [Spacer(1,5),
              Paragraph("Geographic-Reasoning Task", st_h2)]
    story += numbered_tasks([
        "Where are the land-grant railroads most concentrated? What regions of the country?",
        "How might a railroad running through a territory change who settles there? (Connect to the "
        "Homestead Act and Dawes Act documents.)",
        "What does this map suggest about how the federal government used land to shape westward expansion?",
    ], width=W)
    story += sentence_starter("The map shows ______, which suggests that the government ______.", width=W)
    return story


def section_tn_connection(W):
    """SECTION 3 — Tennessee Connection: 1888 TN railroad map. Flagship differentiator."""
    story = [PageBreak(),
             TOCMarker("tn_connect"), XWMarker("MAPTN"),
             tn_banner(width=W),
             Spacer(1,10),
             Paragraph("The 1888 Tennessee Railroad &amp; County Map", st_h1),
             Paragraph("SSP.06 &nbsp;|&nbsp; Local geographic reasoning \u2014 Tennessee", st_small),
             Paragraph("By the 1880s, Tennessee's rail network tied East Tennessee's coal and iron fields \u2014 "
                       "around Chattanooga and the Cumberland Plateau \u2014 into the same national industrial "
                       "economy shown on the national map. This is the same industrialization the unit studies, "
                       "happening in your home state.", st_tnote),
             Spacer(1,4)]
    story += full_image_flowable(
        os.path.join(MAPS_DIR, "TN_railroad_county_1888_loc.jpg"), W, max_h=3.3*inch,
        caption="New Enlarged Scale Railroad and County Map of Tennessee, Rand McNally, 1888",
        alt="A wide map of Tennessee showing county lines and railroad lines crossing the state, with a "
            "denser network of rail lines in East and Middle Tennessee than in West Tennessee.",
        credit="Library of Congress, Geography and Map Division, 1888. Public domain.")
    story += [Spacer(1,10),
              Paragraph("Geographic-Reasoning Task \u2014 Tennessee", st_h2)]
    story += numbered_tasks([
        "Find Chattanooga and the East Tennessee counties on the map. How does the rail network there "
        "compare to West Tennessee?",
        "Why would railroads matter for moving coal and iron out of Tennessee to the rest of the country?",
    ], width=W)
    story += sentence_starter("In Tennessee, the railroad map shows ______, which mattered because ______.", width=W)
    return story


def section_organizer(W):
    """SECTION 4 (a11y) — reusable source-analysis graphic organizer."""
    story = [PageBreak(),
             TOCMarker("organizer"), XWMarker("ORG"),
             accent_bar("Graphic Organizer &nbsp;&mdash;&nbsp; Analyze Any Source", color=RED, size=13),
             Spacer(1,8),
             Paragraph("Reusable tool &nbsp;|&nbsp; Use with any document, image, map, or chart in this workbook", st_small),
             Paragraph("Use this grid whenever you need a quick way to break down a source \u2014 in this "
                       "workbook or any other. Fill in one row per source.", st_tnote),
             Spacer(1,6)]
    st_orgh = S("orgh", fontName=HEADM, fontSize=9, leading=12, textColor=WHITE)
    headers = ["Source", "What it shows", "Whose perspective", "Evidence I can use"]
    head_row = [Paragraph(h, st_orgh) for h in headers]
    col_w = [W*0.19, W*0.29, W*0.24, W*0.28]
    rows = [head_row] + [["", "", "", ""] for _ in range(6)]
    org = Table(rows, colWidths=col_w, rowHeights=[0.34*inch] + [0.62*inch]*6)
    org.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("BACKGROUND",(0,0),(-1,0),NAVY),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[WHITE, CARD]),
        ("GRID",(0,0),(-1,-1),0.6,BORDER),
        ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6),
        ("LEFTPADDING",(0,0),(-1,-1),6),("RIGHTPADDING",(0,0),(-1,-1),6),
    ]))
    story += [org, Spacer(1,10)]
    story += [hbox([Paragraph("<b>How to use it.</b> Write the document letter or title in the first column. "
                               "In the next three columns, note what the source shows, whose point of view it "
                               "carries, and one piece of evidence you could quote or cite from it. This is the "
                               "same thinking HIPPO and OPTIC ask for, organized as a quick-reference grid you "
                               "can use on any new source \u2014 including the maps and charts in this section.",
                               st_tnote)], bg=colors.HexColor("#FBF3E4"), border=GOLD)]
    return story

# ============================================================================
# FRONT MATTER — copyright/edition page + Table of Contents
# Inserted after the cover's PageBreak, before "How to Use This Workbook".
# Reuses existing helpers/palette/fonts only (NAVY / RED / GOLD, hbox, accent_bar, S()).
# ============================================================================

# Ordered TOC entries: (key, label). Keys match the TOCMarker() keys registered at each
# section's start in build(). Page numbers are captured via the two-pass marker mechanism
# and read back here — never hardcoded.
TOC_ENTRIES = [
    ("tn_standards", "Tennessee Standards Alignment"),
    ("accommodations", "Accessibility &amp; Accommodations"),
    ("how_to_use",   "How to Use This Workbook"),
    ("central_q",    "The Central Question \u2014 \u201c" + SET["title"].split(":")[0] + "\u201d"),
    ("roster",       "Document Roster"),
    ("doc_set",      "Documents A\u2013F: Primary Sources"),
    ("us07_set",     "US.07 Document Set \u2014 \u201c" + SET["us07_title"].split(":")[0] + "\u201d"),
    ("reading_data", "Reading the Data \u2014 Charts &amp; Graphs"),
    ("mapping",      "Mapping the Nation \u2014 Geographic Reasoning"),
    ("tn_connect",   "Tennessee Connection"),
    ("organizer",    "Graphic Organizer \u2014 Analyze Any Source"),
]

st_copy_h      = S("cph", fontName=HEAD, fontSize=15, leading=19, textColor=NAVY, alignment=TA_CENTER, spaceAfter=4)
st_copy_body   = S("cpb", fontName=BODYF, fontSize=9.5, leading=14, textColor=INK, alignment=TA_CENTER, spaceAfter=7)
st_copy_small  = S("cps", fontName=BODYF, fontSize=9, leading=13, textColor=MUTED, alignment=TA_CENTER, spaceAfter=6)
st_copy_label  = S("cpl", fontName=HEADM, fontSize=8.5, leading=11, textColor=NAVY, alignment=TA_CENTER)

def _isbn_barcode_placeholder(width):
    """An outlined barcode-placeholder rectangle. NO fabricated ISBN number is used anywhere."""
    w = 1.9*inch
    p = Paragraph("ISBN barcode\n(to be assigned)", S("bcp", fontName=BODYF, fontSize=7.5, leading=10,
                   textColor=MUTED, alignment=TA_CENTER))
    # Table cell with just an outline box, sized like a barcode zone
    t = Table([[p]], colWidths=[w], rowHeights=[0.62*inch])
    t.setStyle(TableStyle([
        ("BOX",(0,0),(-1,-1),0.8,MUTED),
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("ALIGN",(0,0),(-1,-1),"CENTER"),
    ]))
    outer = Table([[t]], colWidths=[width])
    outer.setStyle(TableStyle([("ALIGN",(0,0),(-1,-1),"CENTER")]))
    return outer

def section_copyright(W):
    """TASK 1 — copyright / edition page. Honest, no fabricated ISBN."""
    story = [Spacer(1, 0.55*inch)]
    story += [Paragraph("U.S. History Hack&trade;", st_copy_h),
              Paragraph(SET["unit_title"] + " \u2014 Print Edition", st_copy_body),
              Spacer(1, 14),
              HRFlowable(width=2.4*inch, thickness=1, color=GOLD, hAlign="CENTER", spaceAfter=14)]
    story += [Paragraph("\u00A9 2026 TroopToTeacher Technologies LLC. All rights reserved.", st_copy_body),
              Paragraph("Licensed for single-classroom printing. Not for redistribution or resale.", st_copy_small),
              Spacer(1, 10)]
    story += [Paragraph("ISBN: [to be assigned]", st_copy_label),
              Spacer(1, 6),
              _isbn_barcode_placeholder(W),
              Spacer(1, 14)]
    story += [Paragraph("TroopToTeacher Technologies LLC &middot; Franklin, Tennessee", st_copy_small),
              Spacer(1, 10)]
    story += [Paragraph(
        "All primary sources and maps are public-domain works; data charts are built from U.S. Census "
        "Bureau and U.S. Immigration and Naturalization Service public-domain statistics. See in-text "
        "captions for full provenance.",
        S("cpsrc", fontName=BODYF, fontSize=9, leading=13, textColor=MUTED, alignment=TA_CENTER, spaceAfter=6))]
    story += [Paragraph(
        "Supplemental instructional material. Tennessee-standards aligned; not marketed as Common "
        "Core-aligned per T.C.A. \u00A7 49-6-2202.",
        S("cpdisc", fontName=BODYF, fontSize=9, leading=13, textColor=MUTED, alignment=TA_CENTER, spaceAfter=10))]
    story += [Spacer(1, 8),
              Paragraph(
        "U.S. History Hack and TroopToTeacher are trademarks of TroopToTeacher Technologies LLC.",
        S("cptm", fontName=BODYF, fontSize=8.5, leading=12, textColor=MUTED, alignment=TA_CENTER))]
    story += [PageBreak()]
    return story

def _dot_leader_row(label, page_key, W):
    """One TOC row: title (left) ... dot leader ... page number (right), matching brand type.
    A three-column table gives a true dot-leader effect: title | dots (HRFlowable, dotted) | page#.
    Page number is a live reference into TOC_PAGES, resolved at draw time (section_toc() re-runs
    on every build pass since it's called fresh inside build())."""
    pg = TOC_PAGES.get(page_key)
    pg_text = str(pg) if pg else "\u2013"
    title_p = Paragraph(label, S("tocL", fontName=BODYF, fontSize=11.5, leading=15, textColor=INK))
    dots = HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#B7AF9C"),
                       dash=(1, 2), lineCap="round", vAlign="BOTTOM")
    page_p  = Paragraph(f"<b>{pg_text}</b>", S("tocP", fontName=HEADM, fontSize=11.5, leading=15,
                         textColor=NAVY, alignment=TA_LEFT))
    dot_w = 0.5*inch
    title_w = W*0.72
    page_w = W - title_w - dot_w
    row = Table([[title_p, dots, page_p]], colWidths=[title_w, dot_w, page_w])
    row.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"BOTTOM"),
        ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),4),
        ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),4),
    ]))
    return row

def section_toc(W):
    """TASK 2 — Table of Contents with dot-leader rows and real captured page numbers."""
    story = [Paragraph("Table of Contents", st_h1),
             HRFlowable(width=W, thickness=1, color=GOLD, spaceAfter=10)]
    rows = [_dot_leader_row(label, key, W) for key, label in TOC_ENTRIES]
    story += rows
    story += [Spacer(1, 12),
              Paragraph("<i>Page numbers reflect this print master's current layout and are captured "
                        "automatically from the workbook's running footer.</i>", st_small)]
    story += [PageBreak()]
    return story

def _xw_page(key):
    """Look up a captured crosswalk page number; '\u2013' placeholder until stable."""
    pg = XW.get(key)
    return str(pg) if pg else "\u2013"

def section_crosswalk(W):
    """NEW SECTION \u2014 Tennessee Standards Alignment Crosswalk.
    Placed AFTER the Table of Contents and BEFORE 'How to Use This Workbook'.
    Both tables use captured page numbers from the XW dict (two-pass marker mechanism) \u2014
    never hardcoded. Zebra shading (CARD), gold rules, navy headers; grayscale-legible."""
    story = [TOCMarker("tn_standards")]
    story += [Paragraph("Tennessee Standards Alignment", st_h1),
              HRFlowable(width=W, thickness=1, color=GOLD, spaceAfter=8)]
    story += [Paragraph(
        "This workbook is a <b>supplemental, standards-based</b> resource. The table below shows "
        "where each Tennessee U.S. History content standard for Unit 1 (US.01\u2013US.07) and each "
        "Social Studies Practice (SSP.01\u2013SSP.06) is addressed. Standard text is quoted from the "
        "Tennessee Academic Standards for Social Studies (2017). Where a standard is supported by "
        "background/context rather than a dedicated primary-source document, it is marked "
        "<b>Context</b> with a teacher note, so adopters can see coverage honestly.", st_tnote)]
    story += [Paragraph(
        "Literacy skills reinforced here align to Common Core reading/writing-in-history (RH/WHST) "
        "practices, AP U.S. History historical thinking skills, the C3 Framework inquiry arc, and the "
        "Inquiry Design Model \u2014 provided as cross-walk reference only; this product is "
        "Tennessee-standards aligned and is not marketed as Common Core-aligned (T.C.A. \u00A7 49-6-2202).",
        st_tnote), Spacer(1, 6)]

    # ---------------- TABLE 1 — Content Standards US.01–US.07 ----------------
    st_xwh = S("xwh", fontName=HEADM, fontSize=9, leading=12, textColor=WHITE)
    st_xwstd = S("xwstd", fontName=HEADM, fontSize=9.5, leading=13, textColor=NAVY)
    st_xwbody = S("xwbody", fontName=BODYF, fontSize=9.5, leading=13, textColor=INK)
    st_xwcov_full = S("xwcovF", fontName=HEADM, fontSize=9.5, leading=13, textColor=colors.HexColor("#1E5E3A"))
    st_xwcov_ctx  = S("xwcovC", fontName=HEADM, fontSize=9.5, leading=13, textColor=colors.HexColor("#8A5A00"))

    def cov_cell(label):
        style = st_xwcov_full if label == "Full" else st_xwcov_ctx
        mark = "FULL" if label == "Full" else "CONTEXT"
        return Paragraph(f"<b>{mark}</b>", style)

    t1_rows = [
        [Paragraph("Standard", st_xwh), Paragraph("Content Standard (abbreviated, verbatim)", st_xwh),
         Paragraph("Where in this workbook", st_xwh), Paragraph("Coverage", st_xwh)],
        ["US.01",
         "Explain how the Homestead Act and the Transcontinental Railroad impacted the settlement "
         "of the West. (C,E,G,H,P)",
         f"Doc A Homestead Act (p.{_xw_page('US01a')}); Doc B Pacific Railway Act (p.{_xw_page('US01b')}); "
         f"National map (p.{_xw_page('MAPNAT')})",
         "Full"],
        ["US.02",
         "Examine federal policies toward American Indians: reservations, assimilation, boarding "
         "schools, Dawes Act. (C,G,H,P,T)",
         f"Doc C Dawes General Allotment Act (p.{_xw_page('US02')})",
         "Full"],
        ["US.03",
         "Explain the impact of the Compromise of 1877: Jim Crow, lynching, disenfranchisement, "
         "\u201cPap\u201d Singleton &amp; the Exodusters, Plessy v. Ferguson. (T.C.A. \u00A749-6-1006) "
         "(C,G,H,P,T,TCA)",
         f"Doc D Plessy v. Ferguson (p.{_xw_page('US03')})",
         "Full"],
        ["US.04",
         "Analyze causes/consequences of Gilded Age politics &amp; economics: political machines, "
         "scandals, civil service reform, farmers vs. wage earners vs. capitalists (Boss Tweed, Nast, "
         "Pendleton Act, Credit Mobilier, Interstate Commerce Act). (C,E,G,H,P)",
         f"Central Question framing &amp; Doc E \u201cGospel of Wealth\u201d (p.{_xw_page('US05')}) provide "
         "the economic-inequality lens; political-machine specifics are teacher-supplied context.",
         "Context"],
        ["US.05",
         "Describe changes in American life from inventions/innovations of business leaders &amp; "
         "entrepreneurs (Bell, Rockefeller, Bessemer, Tesla, Carnegie, Vanderbilt, Edison, Madam C.J. "
         "Walker, J.P. Morgan). (C,E,H)",
         f"Doc E Andrew Carnegie, \u201cThe Gospel of Wealth\u201d (p.{_xw_page('US05')})",
         "Full (Carnegie); other figures = teacher context"],
        ["US.06",
         "Locate major industrial centers (Boston, Pittsburgh, Chicago, San Francisco, New York City) "
         "and describe how industrialization moved people rural&rarr;urban. (C,E,G,H)",
         f"Doc F Jacob Riis on urban tenements (p.{_xw_page('US06')}); Urbanization chart 1860\u20131900 "
         f"(p.{_xw_page('CHART_URBAN')}); National railroad map (p.{_xw_page('MAPNAT')})",
         "Full"],
        ["US.07",
         "Describe differences between \u201cold\u201d/\u201cnew\u201d immigrants, analyze assimilation, "
         "determine impacts of migration (Angel/Ellis Island, nativism, push/pull, Chinese Exclusion "
         "Act, Gentleman's Agreement, Jane Addams, Jacob Riis). (C,E,G,H,P)",
         f"US.07 Document Set: Chinese Exclusion Act + settlement-house source (pp.{_xw_page('US07')}"
         f"\u2013{_xw_page('US07b')}); Synthesis prompt (p.{_xw_page('US07syn')})",
         "Full"],
    ]
    t1_data = [t1_rows[0]] + [
        [Paragraph(f"<b>{r[0]}</b>", st_xwstd), Paragraph(r[1], st_xwbody),
         Paragraph(r[2], st_xwbody), cov_cell(r[3])]
        for r in t1_rows[1:]
    ]
    std_w = 0.85*inch
    cov_w = 0.92*inch
    remain = W - std_w - cov_w
    col1 = [std_w, remain*0.56, remain*0.44, cov_w]
    t1 = Table(t1_data, colWidths=col1, repeatRows=1)
    zebra = [WHITE, CARD]
    t1_style = [
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("BACKGROUND", (0,0), (-1,0), NAVY),
        ("GRID", (0,0), (-1,-1), 0.5, BORDER),
        ("LINEBELOW", (0,0), (-1,0), 1.4, GOLD),
        ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING", (0,0), (-1,-1), 6), ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ]
    for i in range(1, len(t1_data)):
        t1_style.append(("BACKGROUND", (0,i), (-1,i), zebra[i % 2]))
    t1.setStyle(TableStyle(t1_style))
    story += [t1, Spacer(1, 4)]
    story += [Paragraph(
        "<b>Full</b> = addressed by a primary-source document and student task. <b>Context</b> = the "
        "standard's theme is present as framing/background; the teacher supplies the named specifics "
        "using the companion lecture deck. This honesty is intentional \u2014 a single focused DBQ cannot "
        "carry every named person in US.04/US.05, and we will not overclaim.",
        S("xwfoot1", fontName=BODYF, fontSize=8, leading=11, textColor=MUTED, spaceAfter=6))]
    story += [PageBreak()]

    # ---------------- TABLE 2 — Social Studies Practices SSP.01–SSP.06 ----------------
    story += [XWMarker("tn_standards_p2"),
              Paragraph("Tennessee Standards Alignment", S("xwcont", fontName=HEAD, fontSize=12.5,
                        leading=16, textColor=NAVY, spaceAfter=2)),
              Paragraph("Social Studies Practices SSP.01\u2013SSP.06 (continued)", st_small),
              HRFlowable(width=W, thickness=1, color=GOLD, spaceBefore=4, spaceAfter=8)]

    t2_rows = [
        [Paragraph("Practice", st_xwh), Paragraph("What it requires (abbreviated, verbatim)", st_xwh),
         Paragraph("Where in this workbook", st_xwh)],
        ["SSP.01",
         "Collect data from primary &amp; secondary sources (printed materials, maps, charts, "
         "political cartoons, photographs, artifacts).",
         f"Six primary-source documents A\u2013F (pp.{_xw_page('US01a')}\u2013{_xw_page('US06')}); "
         f"immigration document set (p.{_xw_page('US07')}); charts &amp; maps (pp.{_xw_page('CHART')}, "
         f"{_xw_page('MAPNAT')}, {_xw_page('MAPTN')})"],
        ["SSP.02",
         "Critically examine a source: extract/paraphrase, evidence vs. assertion, inferences, author "
         "purpose/POV/bias, strengths &amp; limitations.",
         f"OPTIC / sourcing analysis frames on every document page (pp.{_xw_page('US01a')}\u2013"
         f"{_xw_page('US06')})"],
        ["SSP.03",
         "Synthesize data across sources: compare for accuracy/validity, recognize disparities, frame "
         "questions.",
         f"US.07 Synthesis prompt using BOTH documents (p.{_xw_page('US07syn')}); DBQ requires weighing "
         "Documents A\u2013F together"],
        ["SSP.04",
         "Construct &amp; communicate evidence-based arguments: defend ideas, compare viewpoints, "
         "cause/effect, predict/devise outcomes.",
         f"DBQ essay planner &amp; thesis/evidence tasks; graphic organizer (p.{_xw_page('ORG')})"],
        ["SSP.05",
         "Develop historical awareness: accounts change over time, historical empathy vs. "
         "present-mindedness, context, continuity &amp; change.",
         "Central Question \u201cWas Gilded Age America \u2018Progress\u2019 for All?\u201d and per-document "
         "context lines require weighing perspectives of the period"],
        ["SSP.06",
         "Develop geographic awareness: map types by origin/authority/validity, geographic perspective "
         "across scales, spatial associations, regions, human-environment interaction.",
         f"\u201cMapping the Nation\u201d 1892 land-grant railroad map (p.{_xw_page('MAPNAT')}); "
         f"\u201cTennessee Connection\u201d 1888 TN railroad &amp; county map (p.{_xw_page('MAPTN')})"],
    ]
    t2_data = [t2_rows[0]] + [
        [Paragraph(f"<b>{r[0]}</b>", st_xwstd), Paragraph(r[1], st_xwbody), Paragraph(r[2], st_xwbody)]
        for r in t2_rows[1:]
    ]
    col2 = [0.72*inch, W*0.42, 0]
    col2[2] = W - col2[0] - col2[1]
    t2 = Table(t2_data, colWidths=col2, repeatRows=1)
    t2_style = [
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("BACKGROUND", (0,0), (-1,0), NAVY),
        ("GRID", (0,0), (-1,-1), 0.5, BORDER),
        ("LINEBELOW", (0,0), (-1,0), 1.4, GOLD),
        ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING", (0,0), (-1,-1), 6), ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ]
    for i in range(1, len(t2_data)):
        t2_style.append(("BACKGROUND", (0,i), (-1,i), zebra[i % 2]))
    t2.setStyle(TableStyle(t2_style))
    story += [t2, Spacer(1, 4)]
    story += [Paragraph(
        "Practices are demonstrated through the workbook's recurring analysis routines (HIPPO, OPTIC, "
        "CER) rather than a single stand-alone task, since Social Studies Practices are, by design, "
        "applied across every source rather than taught once.",
        S("xwfoot2", fontName=BODYF, fontSize=8, leading=11, textColor=MUTED, spaceAfter=8))]

    story += [HRFlowable(width=W, thickness=1, color=GOLD, spaceBefore=4, spaceAfter=6),
              Paragraph(
        "Standards text: Tennessee Academic Standards for Social Studies, Tennessee Department of "
        "Education (2017 revision, in effect through 2026\u201327). Full standards: tn.gov/education "
        "\u2192 Academic Standards \u2192 Social Studies.",
        S("xwsrc", fontName=BODYF, fontSize=8.5, leading=12, textColor=MUTED))]
    story += [PageBreak()]
    return story

def _acc_callout(header_text, body_text, W):
    """A short callout box: navy header strip + CARD-background body, matching hbox/accent_bar language."""
    head = Table([[Paragraph(header_text, S("acch", fontName=HEAD, fontSize=11, leading=14, textColor=WHITE))]],
                 colWidths=[W])
    head.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), NAVY),
        ("LEFTPADDING", (0,0), (-1,-1), 10), ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LINEBEFORE", (0,0), (0,-1), 3, GOLD),
    ]))
    body = Table([[Paragraph(body_text, S("accb", fontName=BODYF, fontSize=9.7, leading=13.5, textColor=INK))]],
                 colWidths=[W])
    body.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), CARD),
        ("BOX", (0,0), (-1,-1), 0.8, BORDER),
        ("LEFTPADDING", (0,0), (-1,-1), 10), ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 8), ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ]))
    return KeepTogether([head, body])


def section_accommodations(W):
    """NEW SECTION -- Accessibility & Accommodations matrix.
    Placed AFTER the Tennessee Standards Alignment crosswalk and BEFORE 'How to Use This
    Workbook'. Integrity-first: only documents supports genuinely built into this workbook.
    Any page reference inside a cell is pulled from the existing captured markers (ORG, CHART,
    MAPNAT, MAPTN) via _xw_page() -- never hardcoded. Plain ASCII only; no Unicode
    checkmarks/arrows/bullets (prior build hit tofu on those)."""
    story = [TOCMarker("accommodations")]
    story += [Paragraph("Accessibility &amp; Accommodations", st_h1),
              HRFlowable(width=W, thickness=1, color=GOLD, spaceAfter=8)]
    story += [Paragraph(
        "This workbook is built with accessibility in mind and includes supports that help "
        "students with disabilities, students on 504/IEP plans, and English learners access the "
        "same rigorous primary-source work as their peers. The matrix below itemizes the supports "
        "<b>already present in this book</b> and the teacher action that activates each. "
        "<b>Important:</b> this workbook supports and complements a student's accommodations "
        "&mdash; it does not replace, and is not a substitute for, the individualized "
        "accommodations required by a student's IEP or 504 plan. Teachers should always apply "
        "each student's legally required accommodations.", st_tnote), Spacer(1, 6)]

    st_amh = S("amh", fontName=HEADM, fontSize=9, leading=12, textColor=WHITE)
    st_amneed = S("amneed", fontName=HEADM, fontSize=9.3, leading=12.5, textColor=NAVY)
    st_ambody = S("ambody", fontName=BODYF, fontSize=9.3, leading=12.5, textColor=INK)

    rows_data = [
        ("Reading load / processing (SWD, IEP)",
         "Primary sources are chunked into short, excerpted passages with inline glosses rather "
         "than full-length dense text",
         "Every document A&ndash;F and the US.07 set",
         "Allow extended time; let students annotate directly on the excerpt; pair with the "
         "graphic organizer."),
        ("Written-expression support (SWD, IEP)",
         "Reusable source-analysis graphic organizer + sentence-starter frames scaffold the "
         "analysis and the CER argument",
         f"Graphic Organizer (p.{_xw_page('ORG')}); sentence frames on analysis tasks",
         "Permit organizer-first drafting; accept bullet/organizer responses where the IEP allows "
         "reduced written output."),
        ("Structured analysis routine (SWD, 504)",
         "Consistent OPTIC (visual) and HIPPO/sourcing (text) frames give a predictable, "
         "step-by-step routine on every source",
         "Every document page",
         "Teach the routine once; students reuse it, reducing task-initiation and working-memory "
         "load."),
        ("English learners (EL / WIDA)",
         "Spanish-language glosses for key terms and plain-language phrasing throughout",
         "Throughout document analysis",
         "Encourage bilingual glossing; pair EL students; allow first-language brainstorming "
         "before English writing."),
        ("Low-vision / print access",
         "High-contrast navy/black-on-cream layout, &ge;10.5pt body type, and clean "
         "single-column reading order; scales cleanly on a copier or PDF zoom",
         "Whole workbook",
         "Enlarge to 129%/legal on the copier for large-print, or have students zoom the PDF; "
         "all text remains reflow-legible."),
        ("Screen-reader / read-aloud (SWD, IEP)",
         "Every image, map, and chart carries a plain-language text description that doubles as "
         "alt-text / a read-aloud transcript",
         f"Charts (p.{_xw_page('CHART')}), maps (pp.{_xw_page('MAPNAT')}, {_xw_page('MAPTN')}), "
         "document images",
         "Read the description aloud or let assistive tech read it; no student misses the "
         "visual-source content."),
        ("Output flexibility (504, IEP)",
         "Tasks accept multiple response modes &mdash; written, oral, or organizer-based &mdash; "
         "because the rubric scores the reasoning, not the format",
         "DBQ tasks + rubric",
         "Offer oral defense or scribed responses per plan; score the argument, not "
         "handwriting/spelling."),
    ]

    head_row = [Paragraph("Learner need / plan area", st_amh),
                Paragraph("Built-in support in this workbook", st_amh),
                Paragraph("Where / how", st_amh),
                Paragraph("Teacher action", st_amh)]
    body_rows = [[Paragraph(f"<b>{need}</b>", st_amneed), Paragraph(support, st_ambody),
                  Paragraph(where, st_ambody), Paragraph(action, st_ambody)]
                 for need, support, where, action in rows_data]
    am_data = [head_row] + body_rows

    need_w = W * 0.19
    where_w = W * 0.23
    remain = W - need_w - where_w
    col_w = [need_w, remain * 0.52, where_w, remain * 0.48]
    amt = Table(am_data, colWidths=col_w, repeatRows=1)
    zebra = [WHITE, CARD]
    am_style = [
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("BACKGROUND", (0,0), (-1,0), NAVY),
        ("GRID", (0,0), (-1,-1), 0.5, BORDER),
        ("LINEBELOW", (0,0), (-1,0), 1.4, GOLD),
        ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING", (0,0), (-1,-1), 6), ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ]
    for i in range(1, len(am_data)):
        am_style.append(("BACKGROUND", (0,i), (-1,i), zebra[i % 2]))
    amt.setStyle(TableStyle(am_style))
    amfoot = Paragraph(
        "These supports are embedded in the material itself. They are designed to work alongside "
        "&mdash; never in place of &mdash; the individualized accommodations in a student's IEP "
        "or 504 plan.",
        S("amfoot", fontName=BODYF, fontSize=8, leading=11, textColor=MUTED, spaceAfter=8))
    story += [amt, Spacer(1, 5), amfoot]

    story += [Spacer(1, 10),
              HRFlowable(width=W, thickness=0.75, color=GOLD, spaceAfter=10)]

    story += [_acc_callout(
        "Digital &amp; Printable Use",
        "<b>Digital and printable.</b> This unit is a print-ready PDF and an inherently digital "
        "resource. Teachers can print it for in-class use OR upload and assign it in any "
        "learning-management system (Google Classroom, Canvas, Schoology) for digital completion "
        "and submission. No separate digital edition is required &mdash; the same file serves "
        "both modes.", W)]
    story += [Spacer(1, 12)]
    story += [_acc_callout(
        "Review &amp; Reinforcement",
        "<b>Where review happens.</b> This workbook is one focused document-based investigation, "
        "not a full review cycle. Spaced review and reinforcement are handled at the curriculum "
        "level &mdash; by sequencing this DBQ alongside the companion U.S. History Hack&trade; "
        "lecture decks, the TCAP review hub, and other Unit 1 materials. Teachers control the "
        "review cadence across the unit; this book supplies the primary-source analysis core.", W)]

    story += [PageBreak()]
    return story


def _build_once(path):
    doc = BaseDocTemplate(path, pagesize=letter,
                          leftMargin=MARGIN, rightMargin=MARGIN,
                          topMargin=0.85*inch, bottomMargin=0.8*inch,
                          title="U.S. History Hack \u2014 Unit 1 DBQ Workbook (Print Master)",
                          author="Perplexity Computer")
    frame = Frame(MARGIN, 0.8*inch, PAGE_W-2*MARGIN, PAGE_H-1.65*inch, id="body")
    cover_frame = Frame(0,0,PAGE_W,PAGE_H, id="cover", leftPadding=MARGIN, rightPadding=MARGIN, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([
        PageTemplate(id="cover", frames=[cover_frame], onPage=cover_page),
        PageTemplate(id="content", frames=[frame], onPage=content_page),
    ])
    doc.build(build())

def make_pdf(path):
    # Multi-pass build. Markers (US07Marker / GeoSectionMarker / TOCMarker) are recorded at
    # DRAW time (inside doc.build()), but consumed at STORY-CONSTRUCTION time (inside build(),
    # which runs before doc.build() draws anything). So each pass's story reflects the PRIOR
    # pass's marker values -- values only stabilize once a pass produces the same page numbers
    # as the pass before it. Adding the new copyright+TOC pages shifts every later page number,
    # so we run enough passes to reach a fixed point rather than a fixed pass count.
    prev_toc = None
    for i in range(8):
        _build_once(path)
        cur_toc = (dict(TOC_PAGES), dict(XW))
        if cur_toc == prev_toc and i >= 1:
            print(f"Converged after {i+1} passes.")
            break
        prev_toc = cur_toc
    print("WROTE", path, "| US.07 starts on page", US07_START_PAGE, "| GEO starts on page", GEO_START_PAGE)
    print("TOC_PAGES:", TOC_PAGES)
    print("XW:", XW)

if __name__ == "__main__":
    make_pdf(os.path.join(HERE, "HistoryHack_Unit1_DBQ_Workbook_MASTER.pdf"))
