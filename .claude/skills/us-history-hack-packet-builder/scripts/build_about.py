"""Build the About / Business page PDF for U.S. History Hack 1877-Present — America 250 edition.
Corrections applied (per author, June 2026):
  - App is NOT free: free trial, then subscription (no specific day count yet).
  - App name printed as "U.S. History Hack 1877-Present".
  - App link + QR code to the App Store listing.
  - No Spanish YOUTUBE videos claimed (videos are English-only); bilingual claim moved to
    Spanish ELL documents for all standards/content.
  - "Scenario-based" claim REMOVED entirely.
  - Tennessee standards + Tennessee connections emphasized.
  - Five-band differentiation, bilingual ELL supports, designed-with-TDOE-rubric, TN US.01-US.95.
  - Download & Print instructions included.
  - No Franklin High School / county references anywhere.
"""
import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from brand import (register_fonts, NAVY, NAVY2, RED, RED_D, GOLD, GOLD_L, INK, SLATE,
                   PAPER, LINE, WHITE, LOGO, PAGE_W, PAGE_H, MARGIN)

register_fonts()
OUT = "/home/user/workspace/tpt_launch/US_History_Hack_About_The_Author.pdf"
QR  = "/home/user/workspace/tpt_launch/assets/app_qr.png"
APP_URL = "https://apps.apple.com/us/app/u-s-history-hack-1877-present/id6757368709"
WEB_URL = "https://www.trooptoteacher.com"
LW = PAGE_W - 2*MARGIN
c = canvas.Canvas(OUT, pagesize=(PAGE_W, PAGE_H))
c.setTitle("About U.S. History Hack 1877-Present — The Author")
c.setAuthor("Perplexity Computer")

def wrap(text, font, size, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if c.stringWidth(t, font, size) <= max_w: cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def para(x, y, text, font, size, color, leading, max_w):
    c.setFont(font, size); c.setFillColor(color)
    for ln in wrap(text, font, size, max_w):
        c.drawString(x, y, ln); y -= leading
    return y

def section_head(y, label):
    c.setFillColor(RED); c.rect(MARGIN, y+3, 0.10*inch, 0.30*inch, fill=1, stroke=0)
    c.setFillColor(GOLD); c.rect(MARGIN+0.10*inch, y+3, 0.06*inch, 0.30*inch, fill=1, stroke=0)
    c.setFont("DMSans-Bold", 16.5); c.setFillColor(NAVY)
    c.drawString(MARGIN + 0.34*inch, y+9, label)
    y -= 0.26*inch
    c.setFillColor(LINE); c.rect(MARGIN, y, LW, 1, fill=1, stroke=0)
    return y - 0.28*inch

def top_band(title_only=False):
    """Slim navy header band used on pages 2-3."""
    bh = 0.95*inch
    c.setFillColor(NAVY); c.rect(0, PAGE_H - bh, PAGE_W, bh, fill=1, stroke=0)
    c.setFillColor(GOLD); c.rect(0, PAGE_H - bh - 3, PAGE_W, 3, fill=1, stroke=0)
    c.setFillColor(RED);  c.rect(0, PAGE_H - bh - 9, PAGE_W, 6, fill=1, stroke=0)
    c.drawImage(ImageReader(LOGO), MARGIN, PAGE_H - 0.86*inch, width=0.66*inch, height=0.66*inch, mask='auto')
    c.setFont("DMSans-Bold", 16); c.setFillColor(WHITE)
    c.drawString(MARGIN + 0.85*inch, PAGE_H - 0.62*inch, "U.S. History Hack")

def footer():
    c.setFillColor(NAVY); c.rect(0, 0, PAGE_W, 0.55*inch, fill=1, stroke=0)
    c.setFillColor(RED);  c.rect(0, 0.55*inch, PAGE_W, 4, fill=1, stroke=0)
    c.setFillColor(GOLD); c.rect(0, 0.59*inch, PAGE_W, 2, fill=1, stroke=0)
    c.setFont("DMSans-Med", 9.5); c.setFillColor(WHITE)
    c.drawString(MARGIN, 0.22*inch, "U.S. History Hack 1877\u2013Present")
    c.setFont("Inter", 9.5); c.setFillColor(GOLD_L)
    c.drawRightString(PAGE_W - MARGIN, 0.22*inch, "trooptoteacher.com  \u2022  @TroopToTeacherTechnologies")

# ===================== PAGE 1 — MEET THE AUTHOR =====================
c.setFillColor(PAPER); c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

band_h = 2.45 * inch
c.setFillColor(NAVY); c.rect(0, PAGE_H - band_h, PAGE_W, band_h, fill=1, stroke=0)
c.setFillColor(GOLD); c.rect(0, PAGE_H - band_h - 3, PAGE_W, 3, fill=1, stroke=0)
c.setFillColor(RED);  c.rect(0, PAGE_H - band_h - 9, PAGE_W, 6, fill=1, stroke=0)

logo_sz = 1.4 * inch
c.drawImage(ImageReader(LOGO), MARGIN, PAGE_H - band_h + (band_h - logo_sz)/2,
            width=logo_sz, height=logo_sz, mask='auto')
tx = MARGIN + logo_sz + 0.3*inch
c.setFont("DMSans-Bold", 28); c.setFillColor(WHITE)
c.drawString(tx, PAGE_H - 0.98*inch, "U.S. History Hack")
c.setFont("DMSans-Bold", 14); c.setFillColor(GOLD_L)
c.drawString(tx, PAGE_H - 1.28*inch, "1877 \u2013 Present")
c.setFont("DMSans-Med", 11); c.setFillColor(WHITE)
c.drawString(tx, PAGE_H - 1.56*inch, "Tennessee-Aligned U.S. History Curriculum")
c.setFont("Inter", 10); c.setFillColor(GOLD_L)
c.drawString(tx, PAGE_H - 1.82*inch, "by TroopToTeacher Technologies LLC  \u2022  Franklin, Tennessee")
# America 250 ribbon
ribbon_txt = "AMERICA 250  \u2022  1776 \u2013 2026  \u2022  SEMIQUINCENTENNIAL"
rib_w = c.stringWidth(ribbon_txt, "DMSans-Bold", 8.5) + 0.3*inch
c.setFillColor(RED); c.roundRect(tx, PAGE_H - 2.18*inch, rib_w, 0.26*inch, 4, fill=1, stroke=0)
c.setFont("DMSans-Bold", 8.5); c.setFillColor(WHITE)
c.drawString(tx+0.15*inch, PAGE_H - 2.115*inch, ribbon_txt)

# BODY
y = PAGE_H - band_h - 0.55*inch
y = section_head(y, "Meet the Author")
bio = ("I'm Sean Reynolds \u2014 a U.S. Air Force veteran, classroom history teacher, and the founder "
       "of TroopToTeacher Technologies LLC. After years of military service, I traded one mission "
       "for another: helping students understand the story of America. Every workbook in this store "
       "is built from that same sense of duty \u2014 accurate, rigorous, and made to help real teachers "
       "and real students succeed.")
y = para(MARGIN, y, bio, "Inter", 11.5, INK, 17, LW)
y -= 0.10*inch
bio2 = ("U.S. History Hack exists for one reason: to give educators primary-source-driven, "
        "differentiated U.S. History materials \u2014 built to Tennessee standards \u2014 that are ready to "
        "teach on Monday morning. No re-formatting, no guesswork, no fluff. What I build for my own "
        "classroom is what I offer here.")
y = para(MARGIN, y, bio2, "Inter", 11.5, INK, 17, LW)
y -= 0.30*inch

# CREDENTIALS — chips
y = section_head(y, "Credentials & Background")
creds = [
    ("TN Level 5 Educator", "Sustained highest TDOE effectiveness rating"),
    ("4.96 / 5.00 Effectiveness", "Five-year average TDOE educator rating"),
    ("U.S. History Specialist", "Aligned to TN Standards US.01\u2013US.95 & EOC blueprint"),
    ("USAF Veteran", "Built training & mentorship programs in service"),
    ("M.Ed. \u2022 Curriculum & EdTech", "Instructional design & education technology"),
    ("Founder & App Engineer", "TroopToTeacher Technologies LLC, Franklin TN"),
]
col_w = (LW - 0.3*inch) / 2
chip_h = 0.74*inch
row_y = y
for i, (title, sub) in enumerate(creds):
    col = i % 2
    if col == 0 and i > 0:
        row_y -= (chip_h + 0.16*inch)
    cx = MARGIN if col == 0 else MARGIN + col_w + 0.3*inch
    cy = row_y - chip_h
    c.setFillColor(WHITE); c.roundRect(cx, cy, col_w, chip_h, 7, fill=1, stroke=0)
    c.setStrokeColor(LINE); c.setLineWidth(1); c.roundRect(cx, cy, col_w, chip_h, 7, fill=0, stroke=1)
    c.setFillColor(RED); c.rect(cx, cy, 4, chip_h, fill=1, stroke=0)
    c.setFont("DMSans-Bold", 11.5); c.setFillColor(NAVY)
    c.drawString(cx + 0.20*inch, cy + chip_h - 0.27*inch, title)
    c.setFont("Inter", 9.2); c.setFillColor(SLATE)
    for j, ln in enumerate(wrap(sub, "Inter", 9.2, col_w - 0.35*inch)):
        c.drawString(cx + 0.20*inch, cy + chip_h - 0.47*inch - j*12, ln)
y = row_y - chip_h - 0.28*inch

# CLASSROOM-PROVEN banner
bh = 1.05*inch
c.setFillColor(NAVY); c.roundRect(MARGIN, y-bh, LW, bh, 9, fill=1, stroke=0)
c.setFillColor(RED); c.roundRect(MARGIN, y-bh, 0.14*inch, bh, 0, fill=1, stroke=0)
c.setFont("DMSans-Bold", 12.5); c.setFillColor(GOLD_L)
c.drawString(MARGIN+0.4*inch, y-0.32*inch, "Built by a Teacher \u2014 Proven in the Classroom")
c.setFont("Inter", 10); c.setFillColor(WHITE)
banner = ("Every resource is designed, taught, and refined in a real high-school U.S. History "
          "classroom before it reaches your students \u2014 aligned to Tennessee standards and ready to teach.")
fy = y-0.56*inch
for ln in wrap(banner, "Inter", 10, LW-0.7*inch):
    c.drawString(MARGIN+0.4*inch, fy, ln); fy -= 13

footer()
c.showPage()

# ===================== PAGE 2 — WHY THESE ARE DIFFERENT =====================
c.setFillColor(PAPER); c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
top_band()

y = PAGE_H - 1.55*inch
y = section_head(y, "Built to Tennessee Standards")
intro = ("Every unit is written to the Tennessee Academic Standards for U.S. History "
         "(US.01\u2013US.95) and the EOC blueprint \u2014 and designed against the TDOE Textbook "
         "and Instructional Materials Quality rubric. Tennessee connections are woven into "
         "the content so students see their own state in the national story.")
y = para(MARGIN, y, intro, "Inter", 11.5, INK, 17, LW)
y -= 0.22*inch

# Four feature cards (2x2): TN standards, 5-band diff, ELL bilingual, TDOE rubric
features = [
    ("Aligned to TN Standards",
     "Mapped to US.01\u2013US.95 and the EOC blueprint, with explicit Tennessee connections in every unit."),
    ("Five-Band Differentiation",
     "From below-grade to advanced \u2014 tiered readings, scaffolds, and questions so every learner has an entry point."),
    ("Bilingual ELL Supports",
     "Spanish ELL documents for the standards and content: simplified definitions, translated supports, and scaffolds for multilingual learners."),
    ("Designed with the TDOE Rubric",
     "Built against the TN Textbook Commission social studies scoring rubric and Policy 2.600 quality criteria."),
]
fcol_w = (LW - 0.3*inch) / 2
fcard_h = 1.58*inch
frow_y = y
for i, (title, sub) in enumerate(features):
    col = i % 2
    if col == 0 and i > 0:
        frow_y -= (fcard_h + 0.18*inch)
    cx = MARGIN if col == 0 else MARGIN + fcol_w + 0.3*inch
    cy = frow_y - fcard_h
    c.setFillColor(WHITE); c.roundRect(cx, cy, fcol_w, fcard_h, 8, fill=1, stroke=0)
    c.setStrokeColor(LINE); c.setLineWidth(1); c.roundRect(cx, cy, fcol_w, fcard_h, 8, fill=0, stroke=1)
    c.setFillColor(RED); c.rect(cx, cy, 5, fcard_h, fill=1, stroke=0)
    # gold tick header rule
    c.setFillColor(GOLD); c.rect(cx+0.18*inch, cy+fcard_h-0.30*inch, 0.55*inch, 3, fill=1, stroke=0)
    c.setFont("DMSans-Bold", 12.5); c.setFillColor(NAVY)
    c.drawString(cx + 0.18*inch, cy + fcard_h - 0.55*inch, title)
    c.setFont("Inter", 9.7); c.setFillColor(SLATE)
    sy = cy + fcard_h - 0.78*inch
    for ln in wrap(sub, "Inter", 9.7, fcol_w - 0.40*inch):
        c.drawString(cx + 0.18*inch, sy, ln); sy -= 12.5
y = frow_y - fcard_h - 0.45*inch

# WHAT'S IN EVERY UNIT
y = section_head(y, "What's in Every Unit")
bullets = [
    "Real primary sources \u2014 students read the actual documents, not summaries.",
    "Cornell Notes, Close Reads, HIPP analysis, and DOK-tagged questions.",
    "Tennessee-connected activities, including a 'Your County' local-history component.",
    "Answer keys and full teacher guidance included in the Teacher Edition.",
]
for b in bullets:
    c.setFillColor(RED); c.circle(MARGIN + 0.07*inch, y+4, 3.0, fill=1, stroke=0)
    c.setFillColor(INK)
    for ln in wrap(b, "Inter", 11.5, LW - 0.32*inch):
        c.setFont("Inter", 11.5); c.drawString(MARGIN + 0.28*inch, y, ln); y -= 16
    y -= 6

footer()
c.showPage()

# ===================== PAGE 3 — ECOSYSTEM + DOWNLOAD =====================
c.setFillColor(PAPER); c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
top_band()

y = PAGE_H - 1.55*inch
y = section_head(y, "The U.S. History Hack Ecosystem")
eco = [
    ("U.S. History Hack 1877\u2013Present \u2014 LIVE on the App Store",
     "1,000+ questions across 10 units and 95 Tennessee standards, with student & teacher modes, "
     "quizzes, flashcards, and audio learning. Start with a free trial, then continue by subscription."),
    ("Under District Review in Tennessee",
     "Currently in review for supplemental classroom use with a Tennessee school district — "
     "evaluated content-wise as a supplemental U.S. History resource."),
    ("YouTube \u2014 US History Hack",
     "Short, standards-aligned U.S. History videos for quick review and engagement "
     "(@TroopToTeacherTechnologies)."),
    ("Website \u2014 trooptoteacher.com",
     "App access, downloadable teacher content, and classroom resources, all in one place."),
]
for title, sub in eco:
    sub_lines = wrap(sub, "Inter", 10, LW - 0.55*inch)
    card_h = 0.34*inch + len(sub_lines)*12.5 + 0.12*inch
    c.setFillColor(WHITE); c.roundRect(MARGIN, y-card_h, LW, card_h, 7, fill=1, stroke=0)
    c.setStrokeColor(LINE); c.setLineWidth(1); c.roundRect(MARGIN, y-card_h, LW, card_h, 7, fill=0, stroke=1)
    c.setFillColor(RED); c.rect(MARGIN, y-card_h, 4, card_h, fill=1, stroke=0)
    c.setFont("DMSans-Bold", 11.5); c.setFillColor(NAVY)
    c.drawString(MARGIN+0.25*inch, y-0.26*inch, title)
    c.setFont("Inter", 10); c.setFillColor(SLATE)
    sy = y-0.46*inch
    for ln in sub_lines:
        c.drawString(MARGIN+0.25*inch, sy, ln); sy -= 12.5
    y -= (card_h + 0.16*inch)

y -= 0.05*inch

# GET THE APP — QR + link block
qb = 1.85*inch
c.setFillColor(NAVY); c.roundRect(MARGIN, y-qb, LW, qb, 9, fill=1, stroke=0)
c.setFillColor(RED); c.roundRect(MARGIN, y-qb, 0.14*inch, qb, 0, fill=1, stroke=0)
# QR on a white tile (right side)
qr_sz = 1.45*inch
qr_pad = 0.10*inch
qx = PAGE_W - MARGIN - qr_sz - 0.30*inch
qy = y - qb + (qb - (qr_sz + 2*qr_pad))/2
c.setFillColor(WHITE); c.roundRect(qx - qr_pad, qy - qr_pad, qr_sz + 2*qr_pad, qr_sz + 2*qr_pad, 8, fill=1, stroke=0)
c.drawImage(ImageReader(QR), qx, qy, width=qr_sz, height=qr_sz, mask='auto')
# text on left
c.setFont("DMSans-Bold", 14); c.setFillColor(GOLD_L)
c.drawString(MARGIN + 0.4*inch, y - 0.40*inch, "Get the App")
c.setFont("Inter", 10.5); c.setFillColor(WHITE)
txw = qx - (MARGIN + 0.4*inch) - 0.25*inch
appt = ("U.S. History Hack 1877\u2013Present on iPhone & iPad. Scan the code or tap the link below. "
        "Free trial, then subscription.")
ay = y - 0.66*inch
for ln in wrap(appt, "Inter", 10.5, txw):
    c.drawString(MARGIN + 0.4*inch, ay, ln); ay -= 14
ay -= 4
c.setFont("DMSans-Med", 9.5); c.setFillColor(GOLD_L)
link_label = "Open in the App Store \u2192"
c.drawString(MARGIN + 0.4*inch, ay, link_label)
lw_ = c.stringWidth(link_label, "DMSans-Med", 9.5)
c.linkURL(APP_URL, (MARGIN + 0.4*inch, ay-2, MARGIN + 0.4*inch + lw_, ay+11), relative=0)

footer()
c.showPage()

# ===================== PAGE 4 — DOWNLOAD & PRINT INSTRUCTIONS =====================
c.setFillColor(PAPER); c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
top_band()

y = PAGE_H - 1.55*inch
y = section_head(y, "How to Download & Print")
steps = [
    ("Download your file", "After purchase, download the PDF to your computer or device. Save a copy "
     "to a folder you'll remember \u2014 you can re-download from your account anytime."),
    ("Open in a PDF reader", "Open the file in Adobe Acrobat Reader (free), Preview (Mac), or your "
     "browser. The PDF opens freely \u2014 no password needed."),
    ("Print at full size", "In the print dialog choose 'Actual Size' (or 100% scale), not 'Fit'. "
     "Print on standard 8.5\u00d711 paper, single-sided for student handouts."),
    ("Black & white friendly", "Every page is designed to read clearly in grayscale, so you can print "
     "economically on a classroom copier."),
    ("Make classroom copies", "Your license permits printing and copying for the students in your own "
     "classroom. Please do not share the digital file outside your classroom (see Terms of Use)."),
]
n = 1
for title, sub in steps:
    # number badge
    c.setFillColor(RED); c.circle(MARGIN + 0.16*inch, y-0.02*inch, 0.16*inch, fill=1, stroke=0)
    c.setFont("DMSans-Bold", 12); c.setFillColor(WHITE)
    c.drawCentredString(MARGIN + 0.16*inch, y-0.07*inch, str(n))
    c.setFont("DMSans-Bold", 12.5); c.setFillColor(NAVY)
    c.drawString(MARGIN + 0.46*inch, y, title)
    yy = y - 0.22*inch
    c.setFont("Inter", 10.5); c.setFillColor(INK)
    for ln in wrap(sub, "Inter", 10.5, LW - 0.5*inch):
        c.drawString(MARGIN + 0.46*inch, yy, ln); yy -= 14
    y = yy - 0.16*inch
    n += 1

y -= 0.05*inch
# Need help box
nb = 0.95*inch
c.setFillColor(NAVY); c.roundRect(MARGIN, y-nb, LW, nb, 9, fill=1, stroke=0)
c.setFillColor(RED); c.roundRect(MARGIN, y-nb, 0.14*inch, nb, 0, fill=1, stroke=0)
c.setFont("DMSans-Bold", 12.5); c.setFillColor(GOLD_L)
c.drawString(MARGIN+0.4*inch, y-0.32*inch, "Need help with a file?")
c.setFont("Inter", 10.5); c.setFillColor(WHITE)
helpt = "Reach out through trooptoteacher.com \u2014 happy to help you get up and running."
hy = y-0.56*inch
for ln in wrap(helpt, "Inter", 10.5, LW-0.7*inch):
    c.drawString(MARGIN+0.4*inch, hy, ln); hy -= 13

footer()
c.showPage()
c.save()
print("WROTE", OUT, os.path.getsize(OUT), "bytes")
