# -*- coding: utf-8 -*-
"""Unit cover pages (all 10 units) — U.S. History Hack Teacher Graphic Organizer Workbook.
One combined US-Letter PDF, one cover per unit.

APPROVED SOURCE OF TRUTH: the Course Standard (Platinum) manifest in Drive
("_LIVE — History Hack — Platinum UDL Master (2026-27)" / "Course Standard (Platinum)
Print Sets"). Unit titles, years, and standard ranges are taken verbatim from that
manifest — NOT from the repo's 03_TEXTBOOK_UNITS/*.html or unit_standard_map.json,
which are superseded drafts.

Only fields I can source from the approved manifest are printed (title, years,
standards). Essential questions / SSP / pacing are omitted until pulled from the
approved per-unit standards source. Art is a placeholder medallion to swap for a
final AI-generated image.
"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = os.path.join(HERE, "pages")

CSS = r"""
  :root{ --navy:#1B2A4A; --red:#B22234; --gold:#C89B3C; --cream:#F7F5EF; --paper:#fff; --muted:#9aa6bd; }
  *{box-sizing:border-box;margin:0;padding:0;}
  @page{ size:8.5in 11in; margin:0; }
  html,body{ background:#8a8f99; }
  body{ font-family:"Helvetica Neue",Arial,sans-serif; }
  .page{ position:relative; width:8.5in; height:11in; background:var(--navy); overflow:hidden; display:flex; flex-direction:column; color:var(--cream); }
  .frame{ position:absolute; inset:0.34in; border:1.5px solid rgba(200,155,60,.55); border-radius:6px; }
  .frame::after{ content:""; position:absolute; inset:6px; border:1px solid rgba(200,155,60,.28); border-radius:4px; }
  .inner{ position:relative; z-index:2; flex:1 1 auto; display:flex; flex-direction:column; padding:0.78in 0.72in 0.56in; }
  .top{ display:flex; justify-content:space-between; align-items:center; flex:0 0 auto; }
  .wm{ font-size:11pt; font-weight:800; letter-spacing:.18em; color:var(--gold); text-transform:uppercase; }
  .series{ font-size:8pt; font-weight:700; letter-spacing:.16em; color:var(--muted); text-transform:uppercase; }
  .rule{ height:2px; background:linear-gradient(90deg,var(--gold),rgba(200,155,60,0)); margin:12px 0 0; flex:0 0 auto; }
  .unitno{ margin-top:34px; font-size:12pt; font-weight:800; letter-spacing:.34em; color:var(--red); text-transform:uppercase; flex:0 0 auto; }
  .unitno b{ color:var(--gold); }
  h1{ font-family:Georgia,"Times New Roman",serif; font-size:39pt; line-height:1.03; color:#fff; margin-top:10px; font-weight:700; flex:0 0 auto; }
  .era{ margin-top:14px; font-size:12pt; font-weight:800; letter-spacing:.16em; color:var(--cream); text-transform:uppercase; flex:0 0 auto; }
  .era::before{ content:""; display:inline-block; width:28px; height:2px; background:var(--gold); vertical-align:middle; margin-right:12px; }
  .art{ flex:1 1 auto; display:flex; align-items:center; justify-content:center; min-height:0; margin:6px 0; position:relative; }
  .art svg{ height:100%; max-height:3.7in; display:block; }
  .art .ph{ position:absolute; bottom:2px; font-size:7pt; letter-spacing:.14em; text-transform:uppercase; color:rgba(154,166,189,.55); }
  .stdband{ flex:0 0 auto; display:flex; align-items:center; justify-content:center; gap:16px;
            background:rgba(247,245,239,.06); border:1px solid rgba(200,155,60,.4); border-radius:6px; padding:14px 18px; }
  .stdband .k{ font-size:8.5pt; font-weight:800; letter-spacing:.14em; color:var(--gold); text-transform:uppercase; }
  .stdband .v{ font-family:Georgia,serif; font-size:17pt; font-weight:700; color:#fff; }
  .stdband .c{ font-size:9pt; font-weight:700; color:var(--muted); letter-spacing:.04em; }
  .foot{ flex:0 0 auto; margin-top:18px; display:flex; justify-content:space-between; align-items:center; font-size:8pt; color:var(--muted); }
  .foot .b{ font-weight:800; color:var(--gold); }
  .repro{ border:1px solid rgba(200,155,60,.5); color:var(--gold); font-size:7pt; font-weight:800; letter-spacing:.09em; text-transform:uppercase; padding:3px 8px; border-radius:3px; }
"""

def medallion(numeral, era_short):
    return f"""
<svg viewBox="0 0 300 300" preserveAspectRatio="xMidYMid meet" aria-label="Unit {numeral} medallion (placeholder for final unit illustration)">
  <circle cx="150" cy="150" r="122" fill="#26385c" stroke="#C89B3C" stroke-width="2.5"/>
  <circle cx="150" cy="150" r="110" fill="none" stroke="#C89B3C" stroke-width="1" opacity="0.6"/>
  <g fill="#C89B3C"><path d="M150 46 l6 13 l14 1 l-11 9 l4 14 l-13 -8 l-13 8 l4 -14 l-11 -9 l14 -1 Z"/></g>
  <text x="150" y="152" text-anchor="middle" dominant-baseline="central" font-family="Georgia, serif" font-weight="700" font-size="88" fill="#F7F5EF">{numeral}</text>
  <text x="150" y="214" text-anchor="middle" font-family="Helvetica Neue, Arial, sans-serif" font-weight="800" font-size="15" letter-spacing="3" fill="#C89B3C">{era_short}</text>
  <text x="150" y="238" text-anchor="middle" font-family="Helvetica Neue, Arial, sans-serif" font-weight="700" font-size="8" letter-spacing="3" fill="#9aa6bd">U.S. HISTORY HACK</text>
</svg>"""

# (num, title, years, std_range, std_count) — VERBATIM from the approved Course Standard (Platinum) manifest.
UNITS = [
    ("1",  "The Rise of Industrialization",      "1877&ndash;1900", "US.01&ndash;US.07", "7 standards"),
    ("2",  "The Progressive Era",                 "1890&ndash;1920", "US.08&ndash;US.18", "11 standards"),
    ("3",  "Imperialism &amp; World War&nbsp;I",  "1890&ndash;1920", "US.19&ndash;US.27", "9 standards"),
    ("4",  "The Roaring Twenties",                "1920&ndash;1929", "US.28&ndash;US.38", "11 standards"),
    ("5",  "The Great Depression &amp; New Deal", "1929&ndash;1941", "US.39&ndash;US.44", "6 standards"),
    ("6",  "World War&nbsp;II",                   "1939&ndash;1945", "US.45&ndash;US.58", "14 standards"),
    ("7",  "The Cold War",                        "1945&ndash;1991", "US.59&ndash;US.70", "12 standards"),
    ("8",  "Postwar America",                     "1945&ndash;1963", "US.71&ndash;US.77", "7 standards"),
    ("9",  "The Civil Rights Movement",           "1954&ndash;1975", "US.78&ndash;US.82", "5 standards"),
    ("10", "Modern America",                      "1965&ndash;2016", "US.83&ndash;US.95", "13 standards"),
]

TEMPLATE = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Unit {num} — {title}</title>
<style>{css}</style></head><body>
<div class="page">
  <div class="frame"></div>
  <div class="inner">
    <div class="top"><span class="wm">U.S. History Hack&trade;</span><span class="series">Teacher Graphic Organizer Workbook</span></div>
    <div class="rule"></div>
    <div class="unitno">Unit <b>{num}</b></div>
    <h1>{title}</h1>
    <div class="era">{years}</div>
    <div class="art">{art}<span class="ph">Placeholder &middot; replace with unit illustration</span></div>
    <div class="stdband">
      <span class="k">Standards&nbsp;Addressed</span>
      <span class="v">{std_range}</span>
      <span class="c">{std_count}</span>
    </div>
    <div class="foot">
      <span class="b">U.S. History Hack&trade; &nbsp;&middot;&nbsp; &copy; 2026 TroopToTeacher Technologies LLC</span>
      <span class="repro">Reproducible</span>
    </div>
  </div>
</div></body></html>"""

os.makedirs(PAGES, exist_ok=True)
for num, title, years, std_range, std_count in UNITS:
    era_short = years.replace("&ndash;", "–")
    html = TEMPLATE.format(css=CSS, num=num, title=title, years=years, std_range=std_range,
                           std_count=std_count, art=medallion(num, era_short))
    slug = f"unit{int(num):02d}_cover"
    with open(os.path.join(PAGES, f"{slug}.html"), "w") as f:
        f.write(html)
    print("wrote", slug, "-", title.replace('&amp;','&').replace('&nbsp;',' '))
