# -*- coding: utf-8 -*-
"""Unit cover pages (all 10 units) for the U.S. History Hack Teacher Graphic
Organizer Workbook. One combined US-Letter PDF, one cover per unit.

TEMPORARY placeholder art: a gold medallion sits in the image zone — swap it for
a final AI-generated image per unit. Text (title/era/essential question/SSP/
pacing) is sourced from the student textbook cover pages
(03_TEXTBOOK_UNITS/unit-N.html); standards ranges from 07_DEPLOY/unit_standard_map.json
(FLAGGED: the map is internally inconsistent — confirm ranges before final print).
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
  .page{ position:relative; width:8.5in; height:11in; background:var(--navy); overflow:hidden;
         display:flex; flex-direction:column; color:var(--cream); }
  .frame{ position:absolute; inset:0.34in; border:1.5px solid rgba(200,155,60,.55); border-radius:6px; }
  .frame::after{ content:""; position:absolute; inset:6px; border:1px solid rgba(200,155,60,.28); border-radius:4px; }
  .inner{ position:relative; z-index:2; flex:1 1 auto; display:flex; flex-direction:column; padding:0.7in 0.72in 0.5in; }
  .top{ display:flex; justify-content:space-between; align-items:center; flex:0 0 auto; }
  .wm{ font-size:11pt; font-weight:800; letter-spacing:.18em; color:var(--gold); text-transform:uppercase; }
  .series{ font-size:8pt; font-weight:700; letter-spacing:.16em; color:var(--muted); text-transform:uppercase; }
  .rule{ height:2px; background:linear-gradient(90deg,var(--gold),rgba(200,155,60,0)); margin:12px 0 0; flex:0 0 auto; }
  .unitno{ margin-top:26px; font-size:12pt; font-weight:800; letter-spacing:.34em; color:var(--red); text-transform:uppercase; flex:0 0 auto; }
  .unitno b{ color:var(--gold); }
  h1{ font-family:Georgia,"Times New Roman",serif; font-size:36pt; line-height:1.02; color:#fff; margin-top:8px; font-weight:700; flex:0 0 auto; }
  .subtitle{ font-family:Georgia,serif; font-style:italic; font-size:14pt; color:var(--gold); margin-top:11px; line-height:1.25; flex:0 0 auto; }
  .era{ margin-top:11px; font-size:11pt; font-weight:800; letter-spacing:.14em; color:var(--cream); text-transform:uppercase; flex:0 0 auto; }
  .era::before{ content:""; display:inline-block; width:26px; height:2px; background:var(--gold); vertical-align:middle; margin-right:10px; }
  .art{ flex:1 1 auto; display:flex; align-items:center; justify-content:center; min-height:0; margin:6px 0; }
  .art svg{ height:100%; max-height:3.2in; display:block; }
  .art .ph{ position:absolute; bottom:6px; font-size:7pt; letter-spacing:.14em; text-transform:uppercase; color:rgba(154,166,189,.6); }
  .eq{ flex:0 0 auto; background:rgba(247,245,239,.06); border-left:4px solid var(--gold); border-radius:0 6px 6px 0; padding:12px 16px; }
  .eq .lbl{ font-size:8.5pt; font-weight:800; letter-spacing:.12em; color:var(--gold); text-transform:uppercase; }
  .eq .q{ font-family:Georgia,serif; font-size:12.5pt; line-height:1.34; color:#fff; margin-top:5px; }
  .meta{ flex:0 0 auto; display:flex; margin-top:15px; border-top:1px solid rgba(200,155,60,.3); padding-top:12px; }
  .meta .m{ flex:1 1 0; padding:0 14px; border-right:1px solid rgba(255,255,255,.12); }
  .meta .m:first-child{ padding-left:0; } .meta .m:last-child{ border-right:none; padding-right:0; }
  .meta .k{ font-size:7.5pt; font-weight:800; letter-spacing:.1em; color:var(--muted); text-transform:uppercase; }
  .meta .v{ font-size:10pt; font-weight:700; color:var(--cream); margin-top:3px; line-height:1.2; }
  .foot{ flex:0 0 auto; margin-top:15px; display:flex; justify-content:space-between; align-items:center; font-size:8pt; color:var(--muted); }
  .foot .b{ font-weight:800; color:var(--gold); }
  .repro{ border:1px solid rgba(200,155,60,.5); color:var(--gold); font-size:7pt; font-weight:800; letter-spacing:.09em; text-transform:uppercase; padding:3px 8px; border-radius:3px; }
"""

def medallion(numeral, era_short):
    # Temporary placeholder: gold double-ring medallion with the unit numeral + era.
    return f"""
<svg viewBox="0 0 300 300" preserveAspectRatio="xMidYMid meet" aria-label="Unit {numeral} medallion (placeholder for final unit illustration)">
  <circle cx="150" cy="150" r="120" fill="#26385c" stroke="#C89B3C" stroke-width="2.5"/>
  <circle cx="150" cy="150" r="108" fill="none" stroke="#C89B3C" stroke-width="1" opacity="0.6"/>
  <g fill="#C89B3C"><path d="M150 48 l6 13 l14 1 l-11 9 l4 14 l-13 -8 l-13 8 l4 -14 l-11 -9 l14 -1 Z"/></g>
  <text x="150" y="150" text-anchor="middle" dominant-baseline="central" font-family="Georgia, serif" font-weight="700" font-size="86" fill="#F7F5EF">{numeral}</text>
  <text x="150" y="212" text-anchor="middle" font-family="Helvetica Neue, Arial, sans-serif" font-weight="800" font-size="15" letter-spacing="3" fill="#C89B3C">{era_short}</text>
  <text x="150" y="236" text-anchor="middle" font-family="Helvetica Neue, Arial, sans-serif" font-weight="700" font-size="8" letter-spacing="3" fill="#9aa6bd">U.S. HISTORY HACK</text>
</svg>"""

# unit: (no_word, numeral, title, subtitle, era, eq, standards, ssp, days)
UNITS = [
    ("One", "1", "Reconstruction", "The Promise and Peril of Rebuilding a Nation", "1865&ndash;1877",
     "How should a nation rebuild after civil war &mdash; and who is included in, or excluded from, the new order it creates?",
     "US.REC &middot; US.01&ndash;US.07", "SSP.05 &middot; Historical Awareness", "&mdash;"),
    ("Two", "2", "The Gilded Age", "Progress, Poverty, and the Price of Growth", "1870&ndash;1900",
     "Who benefited from America&rsquo;s industrial revolution, and at whose expense did that prosperity come?",
     "US.08&ndash;US.18", "SSP.06 &middot; Geographic Awareness", "18 days"),
    ("Three", "3", "Progressive Era &amp; Imperialism", "Reform and Empire", "1890&ndash;1920",
     "Can government fix the problems created by industrial capitalism &mdash; and what does the reach for empire reveal about America&rsquo;s values?",
     "US.19&ndash;US.27", "SSP.04 &middot; Argue with Evidence", "18 days"),
    ("Four", "4", "WWI &amp; the Roaring Twenties", "War, Prosperity, and the Search for American Identity", "1914&ndash;1929",
     "How do war and cultural upheaval reshape national identity, and who gets to define what it means to be American?",
     "US.28&ndash;US.38", "SSP.03 &middot; Synthesize Data", "18 days"),
    ("Five", "5", "The Great Depression &amp; New Deal", "Crisis and Response", "1929&ndash;1941",
     "When the free market catastrophically fails, what obligations does the government have to its citizens?",
     "US.39&ndash;US.44", "SSP.04 &middot; Argue with Evidence", "16 days"),
    ("Six", "6", "World War II", "Democracy at War", "1939&ndash;1945",
     "What sacrifices are citizens of a democracy obligated to make in defense of their freedoms &mdash; and where is the limit?",
     "US.45&ndash;US.58", "SSP.02 &middot; Examine Sources", "18 days"),
    ("Seven", "7", "The Cold War", "Containment, Conformity, and the Fight for Freedom", "1945&ndash;1968",
     "How do nations and individuals respond when the values they publicly claim to uphold conflict with their actions?",
     "US.71&ndash;US.77", "SSP.05 &middot; Historical Awareness", "22 days"),
    ("Eight", "8", "Vietnam, Watergate &amp; the 1970s", "Fractures in American Democracy", "1965&ndash;1980",
     "What happens to a democracy when its citizens lose faith in their government, and what does it take to rebuild trust?",
     "US.59&ndash;US.70", "SSP.03 &middot; Synthesize Data", "16 days"),
    ("Nine", "9", "The Conservative Revolution", "Morning in America: Reagan and the End of the Cold War", "1980&ndash;2001",
     "What are the virtues and the limits of limited government, free markets, and individual responsibility?",
     "US.78&ndash;US.82", "SSP.04 &middot; Argue with Evidence", "16 days"),
    ("Ten", "10", "America in the 21st Century", "Unfinished Business", "2001&ndash;Present",
     "What does it mean to be a citizen of a democracy in an age of terror, digital information, and global interdependence?",
     "US.83&ndash;US.95", "SSP.04 &middot; Argue with Evidence", "14 days"),
]

TEMPLATE = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Unit {no} — {title}</title>
<style>{css}</style></head><body>
<div class="page">
  <div class="frame"></div>
  <div class="inner">
    <div class="top"><span class="wm">U.S. History Hack&trade;</span><span class="series">Teacher Graphic Organizer Workbook</span></div>
    <div class="rule"></div>
    <div class="unitno">Unit <b>{no}</b></div>
    <h1>{title}</h1>
    <div class="subtitle">{subtitle}</div>
    <div class="era">{era}</div>
    <div class="art">{art}<span class="ph">Placeholder &middot; replace with unit illustration</span></div>
    <div class="eq"><div class="lbl">Essential Question</div><div class="q">{eq}</div></div>
    <div class="meta">
      <div class="m"><div class="k">Standards</div><div class="v">{standards}</div></div>
      <div class="m"><div class="k">Primary Practice</div><div class="v">{ssp}</div></div>
      <div class="m"><div class="k">Pacing</div><div class="v">{days}</div></div>
    </div>
    <div class="foot">
      <span class="b">U.S. History Hack&trade; &nbsp;&middot;&nbsp; &copy; 2026 TroopToTeacher Technologies LLC</span>
      <span class="repro">Reproducible</span>
    </div>
  </div>
</div></body></html>"""

os.makedirs(PAGES, exist_ok=True)
for no, num, title, subtitle, era, eq, standards, ssp, days in UNITS:
    era_short = era.replace("&ndash;", "–")
    html = TEMPLATE.format(css=CSS, no=no, title=title, subtitle=subtitle, era=era, eq=eq,
                           standards=standards, ssp=ssp, days=days, art=medallion(num, era_short))
    slug = f"unit{num:0>2}_cover" if num.isdigit() else f"unit_{num}"
    slug = f"unit{int(num):02d}_cover"
    with open(os.path.join(PAGES, f"{slug}.html"), "w") as f:
        f.write(html)
    print("wrote", slug)
