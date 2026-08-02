"""Build the Copyright & Terms of Use packet PDF for US History Hack."""
import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from brand import (register_fonts, NAVY, NAVY2, GOLD, GOLD_L, INK, SLATE,
                   PAPER, LINE, WHITE, REDFLAG, GREENOK, LOGO, PAGE_W, PAGE_H, MARGIN)

register_fonts()
OUT = "/home/user/workspace/tpt_launch/US_History_Hack_Terms_of_Use.pdf"
LW = PAGE_W - 2*MARGIN

c = canvas.Canvas(OUT, pagesize=(PAGE_W, PAGE_H))
c.setTitle("US History Hack — Copyright & Terms of Use")
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

def footer(pg):
    c.setFillColor(NAVY); c.rect(0, 0, PAGE_W, 0.5*inch, fill=1, stroke=0)
    c.setFillColor(GOLD); c.rect(0, 0.5*inch, PAGE_W, 2, fill=1, stroke=0)
    c.setFont("DMSans-Med", 8.5); c.setFillColor(WHITE)
    c.drawString(MARGIN, 0.20*inch, "© TroopToTeacher Technologies LLC  •  US History Hack  •  All Rights Reserved")
    c.setFont("Inter", 8.5); c.setFillColor(GOLD_L)
    c.drawRightString(PAGE_W - MARGIN, 0.20*inch, f"Page {pg}")

def newpage_header():
    c.setFillColor(PAPER); c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    c.setFillColor(NAVY); c.rect(0, PAGE_H - 0.9*inch, PAGE_W, 0.9*inch, fill=1, stroke=0)
    c.setFillColor(GOLD); c.rect(0, PAGE_H - 0.9*inch - 3, PAGE_W, 3, fill=1, stroke=0)
    c.drawImage(ImageReader(LOGO), MARGIN, PAGE_H - 0.80*inch, width=0.6*inch, height=0.6*inch, mask='auto')
    c.setFont("DMSans-Bold", 14); c.setFillColor(WHITE)
    c.drawString(MARGIN + 0.78*inch, PAGE_H - 0.50*inch, "US History Hack — Terms of Use & Copyright")
    return PAGE_H - 1.35*inch

def heading(y, num, text):
    if y < 1.4*inch:  # not enough room; caller handles paging
        return y
    c.setFillColor(GOLD); c.rect(MARGIN, y, 0.28*inch, 0.28*inch, fill=1, stroke=0)
    c.setFont("DMSans-Bold", 9.5); c.setFillColor(NAVY)
    c.drawCentredString(MARGIN + 0.14*inch, y+0.075*inch, str(num))
    c.setFont("DMSans-Bold", 14); c.setFillColor(NAVY)
    c.drawString(MARGIN + 0.42*inch, y+0.05*inch, text)
    y -= 0.22*inch
    c.setFillColor(LINE); c.rect(MARGIN, y, LW, 0.8, fill=1, stroke=0)
    return y - 0.26*inch

def draw_check(x, y, sz=11):
    # green checkmark, vector
    c.setStrokeColor(GREENOK); c.setLineWidth(1.8); c.setLineCap(1)
    c.line(x, y+sz*0.30, x+sz*0.32, y)
    c.line(x+sz*0.32, y, x+sz*0.9, y+sz*0.75)

def draw_x(x, y, sz=10):
    c.setStrokeColor(REDFLAG); c.setLineWidth(1.8); c.setLineCap(1)
    c.line(x, y, x+sz*0.8, y+sz*0.8)
    c.line(x, y+sz*0.8, x+sz*0.8, y)

def draw_warning(x, y, sz=16):
    # filled white triangle with ! on red bg (used in red box -> draw white)
    c.setFillColor(WHITE)
    c.setLineJoin(1)
    p = c.beginPath(); p.moveTo(x, y); p.lineTo(x+sz, y); p.lineTo(x+sz/2, y+sz*0.9); p.close()
    c.drawPath(p, fill=1, stroke=0)
    c.setFillColor(REDFLAG)
    c.setFont("DMSans-Bold", sz*0.62)
    c.drawCentredString(x+sz/2, y+sz*0.18, "!")

def body(y, text, size=10.5, lead=14.5, indent=0):
    c.setFont("Inter", size); c.setFillColor(INK)
    for ln in wrap(text, "Inter", size, LW - indent):
        c.drawString(MARGIN + indent, y, ln); y -= lead
    return y

# ============ PAGE 1: COVER ============
c.setFillColor(NAVY); c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
# gold frame
c.setStrokeColor(GOLD); c.setLineWidth(2)
c.rect(0.5*inch, 0.5*inch, PAGE_W-1.0*inch, PAGE_H-1.0*inch, fill=0, stroke=1)
logo_sz = 1.7*inch
c.drawImage(ImageReader(LOGO), (PAGE_W-logo_sz)/2, PAGE_H - 3.0*inch, width=logo_sz, height=logo_sz, mask='auto')
c.setFont("DMSans-Bold", 30); c.setFillColor(WHITE)
c.drawCentredString(PAGE_W/2, PAGE_H - 3.7*inch, "Copyright & Terms of Use")
c.setFont("DMSans-Med", 15); c.setFillColor(GOLD_L)
c.drawCentredString(PAGE_W/2, PAGE_H - 4.15*inch, "US History Hack Curriculum Products")
c.setFillColor(GOLD); c.rect(PAGE_W/2 - 1.3*inch, PAGE_H - 4.45*inch, 2.6*inch, 2, fill=1, stroke=0)
c.setFont("Inter", 11); c.setFillColor(WHITE)
c.drawCentredString(PAGE_W/2, PAGE_H - 4.9*inch, "TroopToTeacher Technologies LLC  •  Franklin, Tennessee")

# notice box
bx, bw, bh = MARGIN, LW, 1.7*inch
by = 2.4*inch
c.setFillColor(NAVY2); c.roundRect(bx, by, bw, bh, 9, fill=1, stroke=0)
c.setStrokeColor(GOLD); c.setLineWidth(1.2); c.roundRect(bx, by, bw, bh, 9, fill=0, stroke=1)
c.setFont("DMSans-Bold", 12); c.setFillColor(GOLD_L)
c.drawString(bx+0.3*inch, by+bh-0.4*inch, "PLEASE READ BEFORE USE")
c.setFont("Inter", 10); c.setFillColor(WHITE)
notice = ("By downloading or using any US History Hack product, you agree to the terms in this "
          "document. These materials are protected by U.S. copyright law (17 U.S.C. §§ 101 et seq.). "
          "Your purchase grants a license to USE the materials — it does NOT transfer ownership. "
          "These terms are strictly enforced.")
ny = by+bh-0.7*inch
for ln in wrap(notice, "Inter", 10, bw-0.6*inch):
    c.drawString(bx+0.3*inch, ny, ln); ny -= 13.5
c.setFont("Inter", 9); c.setFillColor(GOLD_L)
c.drawCentredString(PAGE_W/2, 0.95*inch, "Effective June 2026  •  © TroopToTeacher Technologies LLC  •  All Rights Reserved")
c.showPage()

# ============ PAGE 2: LICENSE + ALLOWED/NOT ALLOWED ============
y = newpage_header()
y = heading(y, 1, "Your License")
y = body(y, "When you purchase a US History Hack product, you receive a non-transferable, "
            "non-exclusive license for use by a SINGLE teacher in a single classroom. You may "
            "use the materials with your own students for as long as you teach, on as many of "
            "your own devices as you need.")
y -= 0.12*inch
y = heading(y, 2, "What You ARE Allowed To Do")

allowed = [
    "Use the materials with your own students in your own classroom.",
    "Print copies for your own students as needed for instruction.",
    "Save the files on your personal and school devices for your own use.",
    "Post pages inside a PASSWORD-PROTECTED platform (Google Classroom, Canvas, Schoology) limited to your own students.",
    "Reference the materials in your lesson planning and grading.",
    "Leave a review and tell colleagues where they can purchase their own license.",
]
c.setFont("Inter", 10.5)
for a in allowed:
    draw_check(MARGIN, y)
    c.setFillColor(INK)
    lines = wrap(a, "Inter", 10.5, LW - 0.32*inch)
    for k, ln in enumerate(lines):
        c.setFont("Inter", 10.5); c.drawString(MARGIN + 0.30*inch, y, ln); y -= 14
    y -= 4

y -= 0.10*inch
y = heading(y, 3, "What You Are NOT Allowed To Do")
prohibited = [
    "Share, email, sell, sublicense, trade, or give away the files to ANY other person — including colleagues, teammates, or other schools.",
    "Upload the files to any public website, shared drive, or file-sharing service where others can download them.",
    "Post the materials on the open internet, a public-facing page, or any unsecured site.",
    "Claim authorship, remove the copyright notice, or alter the branding.",
    "Reproduce, adapt, or create derivative products to sell or distribute.",
    "Use the materials for whole-school, district, or commercial purposes under a single-teacher license.",
    "Use AI tools to copy, regenerate, or repackage the content for redistribution.",
]
for p in prohibited:
    draw_x(MARGIN, y)
    c.setFillColor(INK)
    lines = wrap(p, "Inter", 10.5, LW - 0.32*inch)
    for k, ln in enumerate(lines):
        c.setFont("Inter", 10.5); c.drawString(MARGIN + 0.30*inch, y, ln); y -= 14
    y -= 4
footer(2)
c.showPage()

# ============ PAGE 3: MULTI-USE + ENFORCEMENT + CONTACT ============
y = newpage_header()
y = heading(y, 4, "Need More Than One Classroom?")
y = body(y, "If multiple teachers, a grade team, a whole school, or a district will use these "
            "materials, you must purchase the appropriate number of licenses or a site license. "
            "Multi-license and school/district pricing is available — buying additional licenses "
            "is affordable and supports the continued creation of these resources.")
y -= 0.05*inch
y = body(y, "Multi-classroom and district licensing: contact TroopToTeacher Technologies LLC "
            "through the US History Hack store, or add additional licenses at the discounted "
            "rate on the product page at checkout.", size=10.5)
y -= 0.15*inch

y = heading(y, 5, "Copyright Notice")
y = body(y, "All US History Hack materials — including text, layout, graphics, questions, answer "
            "keys, and design — are the original work of and are owned by TroopToTeacher "
            "Technologies LLC. Primary-source documents reproduced within these materials are "
            "drawn from public-domain U.S. government sources (U.S. Statutes at Large, the "
            "Library of Congress, and the National Archives) and are cited accordingly; the "
            "original curriculum, arrangement, questions, and presentation remain fully "
            "copyrighted by TroopToTeacher Technologies LLC.")
y -= 0.15*inch

# Enforcement box
ebh = 1.65*inch
c.setFillColor(REDFLAG); c.roundRect(MARGIN, y-ebh, LW, ebh, 9, fill=1, stroke=0)
draw_warning(MARGIN+0.3*inch, y-0.48*inch, 16)
c.setFont("DMSans-Bold", 13); c.setFillColor(WHITE)
c.drawString(MARGIN+0.62*inch, y-0.40*inch, "Strictly Enforced")
c.setFont("Inter", 10); c.setFillColor(WHITE)
enf = ("Unauthorized sharing or distribution is copyright infringement and a violation of these "
       "terms. TroopToTeacher Technologies LLC actively monitors for misuse and will pursue all "
       "available remedies — including DMCA takedown notices, account reporting to Teachers Pay "
       "Teachers, and legal action under U.S. copyright law. Statutory damages for willful "
       "infringement can reach $150,000 per work (17 U.S.C. § 504). Please respect the work "
       "and buy a license for everyone who uses it.")
ey = y - 0.66*inch
for ln in wrap(enf, "Inter", 10, LW - 0.6*inch):
    c.drawString(MARGIN+0.3*inch, ey, ln); ey -= 13
y = y - ebh - 0.3*inch

y = heading(y, 6, "Questions & Permissions")
y = body(y, "For licensing questions, permission requests, or to report a violation, contact "
            "TroopToTeacher Technologies LLC through the US History Hack store on Teachers Pay "
            "Teachers. Thank you for supporting an independent veteran-owned education business.")
footer(3)
c.showPage()
c.save()
print("WROTE", OUT, os.path.getsize(OUT), "bytes")
