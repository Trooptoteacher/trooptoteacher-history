# -*- coding: utf-8 -*-
"""Unit cover pages for the U.S. History Hack Teacher Graphic Organizer Workbook.
Two full-bleed covers (Unit 2, Unit 3) -> one combined US-Letter PDF + PNGs.
Content sourced from the student textbook cover pages (03_TEXTBOOK_UNITS/unit-N.html);
standards range from the canonical 07_DEPLOY/unit_standard_map.json.
Era-relevant artwork is original SVG in the brand palette (copyright-clean).
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
  .frame{ position:absolute; inset:0.34in; border:1.5px solid rgba(200,155,60,.55); border-radius:6px; pointer-events:none; }
  .frame::after{ content:""; position:absolute; inset:6px; border:1px solid rgba(200,155,60,.28); border-radius:4px; }
  .inner{ position:relative; z-index:2; flex:1 1 auto; display:flex; flex-direction:column;
          padding:0.7in 0.72in 0.5in; }
  /* top wordmark row */
  .top{ display:flex; justify-content:space-between; align-items:center; flex:0 0 auto; }
  .wm{ font-size:11pt; font-weight:800; letter-spacing:.18em; color:var(--gold); text-transform:uppercase; }
  .series{ font-size:8pt; font-weight:700; letter-spacing:.16em; color:var(--muted); text-transform:uppercase; }
  .rule{ height:2px; background:linear-gradient(90deg,var(--gold),rgba(200,155,60,0)); margin:12px 0 0; flex:0 0 auto; }
  /* title block */
  .unitno{ margin-top:30px; font-size:12pt; font-weight:800; letter-spacing:.34em; color:var(--red);
           text-transform:uppercase; flex:0 0 auto; }
  .unitno b{ color:var(--gold); }
  h1{ font-family:Georgia,"Times New Roman",serif; font-size:41pt; line-height:1.0; color:#fff;
      margin-top:8px; font-weight:700; flex:0 0 auto; }
  .subtitle{ font-family:Georgia,serif; font-style:italic; font-size:15pt; color:var(--gold);
             margin-top:12px; line-height:1.25; flex:0 0 auto; }
  .era{ margin-top:12px; font-size:11pt; font-weight:800; letter-spacing:.14em; color:var(--cream); text-transform:uppercase; flex:0 0 auto; }
  .era::before{ content:""; display:inline-block; width:26px; height:2px; background:var(--gold); vertical-align:middle; margin-right:10px; }
  /* art */
  .art{ flex:1 1 auto; display:flex; align-items:center; justify-content:center; min-height:0; margin:6px 0; }
  .art svg{ width:86%; height:100%; max-height:3.5in; display:block; }
  /* essential question */
  .eq{ flex:0 0 auto; background:rgba(247,245,239,.06); border-left:4px solid var(--gold);
       border-radius:0 6px 6px 0; padding:12px 16px; }
  .eq .lbl{ font-size:8.5pt; font-weight:800; letter-spacing:.12em; color:var(--gold); text-transform:uppercase; }
  .eq .q{ font-family:Georgia,serif; font-size:13.5pt; line-height:1.34; color:#fff; margin-top:5px; }
  /* meta band */
  .meta{ flex:0 0 auto; display:flex; gap:0; margin-top:16px; border-top:1px solid rgba(200,155,60,.3); padding-top:12px; }
  .meta .m{ flex:1 1 0; padding:0 12px; border-right:1px solid rgba(255,255,255,.12); }
  .meta .m:first-child{ padding-left:0; } .meta .m:last-child{ border-right:none; padding-right:0; }
  .meta .k{ font-size:7.5pt; font-weight:800; letter-spacing:.1em; color:var(--muted); text-transform:uppercase; }
  .meta .v{ font-size:10pt; font-weight:700; color:var(--cream); margin-top:3px; line-height:1.2; }
  .meta .v .star{ color:var(--gold); }
  /* footer */
  .foot{ flex:0 0 auto; margin-top:16px; display:flex; justify-content:space-between; align-items:center;
         font-size:8pt; color:var(--muted); }
  .foot .b{ font-weight:800; color:var(--gold); letter-spacing:.02em; }
  .repro{ border:1px solid rgba(200,155,60,.5); color:var(--gold); font-size:7pt; font-weight:800;
          letter-spacing:.09em; text-transform:uppercase; padding:3px 8px; border-radius:3px; }
"""

# ---------------- Era artwork (original SVG, brand palette) ----------------
ART_U2 = r"""
<svg viewBox="0 0 900 470" preserveAspectRatio="xMidYMid meet" aria-label="Illustration: Gilded Age industrial skyline with factories, smokestacks, gears, and a rail line">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#26385c"/><stop offset="1" stop-color="#1B2A4A"/>
    </linearGradient>
  </defs>
  <!-- sun: clean gold ring with soft glow -->
  <circle cx="655" cy="140" r="58" fill="#C89B3C" opacity="0.10"/>
  <circle cx="655" cy="140" r="58" fill="none" stroke="#C89B3C" stroke-width="2.5" opacity="0.7"/>
  <!-- smoke plumes -->
  <g fill="#C89B3C" opacity="0.16">
    <path d="M250 190 C230 150 300 150 275 110 C255 80 320 78 300 45 L330 45 C350 82 292 92 318 122 C340 158 268 158 292 195 Z"/>
    <path d="M470 205 C452 172 512 172 490 140 C472 114 528 112 512 84 L540 84 C556 116 505 124 528 152 C548 184 486 184 508 212 Z"/>
  </g>
  <!-- gear emblem -->
  <g transform="translate(150,120)" fill="none" stroke="#C89B3C" stroke-width="6" opacity="0.55">
    <circle r="46"/><circle r="18"/>
    <g stroke-width="12">
      <line x1="0" y1="-46" x2="0" y2="-64"/><line x1="0" y1="46" x2="0" y2="64"/>
      <line x1="-46" y1="0" x2="-64" y2="0"/><line x1="46" y1="0" x2="64" y2="0"/>
      <line x1="-33" y1="-33" x2="-46" y2="-46"/><line x1="33" y1="33" x2="46" y2="46"/>
      <line x1="33" y1="-33" x2="46" y2="-46"/><line x1="-33" y1="33" x2="-46" y2="46"/>
    </g>
  </g>
  <!-- skyline silhouette -->
  <g fill="#C89B3C">
    <rect x="120" y="300" width="90" height="150"/>
    <rect x="150" y="250" width="26" height="50"/>            <!-- smokestack -->
    <rect x="230" y="270" width="120" height="180"/>
    <rect x="255" y="205" width="24" height="65"/>
    <rect x="300" y="230" width="24" height="40"/>
    <rect x="370" y="320" width="80" height="130"/>
    <rect x="470" y="255" width="120" height="195"/>
    <rect x="500" y="195" width="26" height="60"/>
    <rect x="548" y="215" width="22" height="40"/>
    <rect x="610" y="335" width="70" height="115"/>
    <rect x="700" y="290" width="95" height="160"/>
    <rect x="732" y="245" width="24" height="45"/>
  </g>
  <!-- lit windows (cream) -->
  <g fill="#F7F5EF" opacity="0.85">
    <rect x="245" y="290" width="10" height="14"/><rect x="270" y="290" width="10" height="14"/><rect x="295" y="290" width="10" height="14"/>
    <rect x="245" y="330" width="10" height="14"/><rect x="295" y="330" width="10" height="14"/>
    <rect x="490" y="285" width="10" height="14"/><rect x="520" y="285" width="10" height="14"/><rect x="550" y="285" width="10" height="14"/>
    <rect x="490" y="330" width="10" height="14"/><rect x="550" y="330" width="10" height="14"/>
    <rect x="720" y="320" width="10" height="14"/><rect x="750" y="320" width="10" height="14"/>
  </g>
  <!-- ground + rail line -->
  <rect x="60" y="450" width="800" height="4" fill="#C89B3C"/>
  <g stroke="#C89B3C" stroke-width="3" opacity="0.8">
    <line x1="90" y1="464" x2="830" y2="464"/><line x1="90" y1="472" x2="830" y2="472"/>
  </g>
  <g stroke="#C89B3C" stroke-width="2" opacity="0.55">
    <line x1="130" y1="462" x2="130" y2="474"/><line x1="210" y1="462" x2="210" y2="474"/><line x1="290" y1="462" x2="290" y2="474"/>
    <line x1="370" y1="462" x2="370" y2="474"/><line x1="450" y1="462" x2="450" y2="474"/><line x1="530" y1="462" x2="530" y2="474"/>
    <line x1="610" y1="462" x2="610" y2="474"/><line x1="690" y1="462" x2="690" y2="474"/><line x1="770" y1="462" x2="770" y2="474"/>
  </g>
</svg>
"""

ART_U3 = r"""
<svg viewBox="0 0 900 470" preserveAspectRatio="xMidYMid meet" aria-label="Illustration: a globe crossed by an eagle, framed by rays, symbolizing Progressive reform and American empire">
  <!-- rays -->
  <g stroke="#C89B3C" stroke-width="2" opacity="0.28">
    <line x1="450" y1="235" x2="450" y2="40"/><line x1="450" y1="235" x2="640" y2="70"/><line x1="450" y1="235" x2="260" y2="70"/>
    <line x1="450" y1="235" x2="720" y2="150"/><line x1="450" y1="235" x2="180" y2="150"/>
    <line x1="450" y1="235" x2="760" y2="235"/><line x1="450" y1="235" x2="140" y2="235"/>
  </g>
  <!-- globe -->
  <g transform="translate(450,235)">
    <circle r="150" fill="#26385c" stroke="#C89B3C" stroke-width="3"/>
    <ellipse rx="150" ry="52" fill="none" stroke="#C89B3C" stroke-width="1.6" opacity="0.55"/>
    <ellipse rx="150" ry="105" fill="none" stroke="#C89B3C" stroke-width="1.6" opacity="0.45"/>
    <line x1="-150" y1="0" x2="150" y2="0" stroke="#C89B3C" stroke-width="1.6" opacity="0.55"/>
    <ellipse rx="80" ry="150" fill="none" stroke="#C89B3C" stroke-width="1.6" opacity="0.4"/>
    <line x1="0" y1="-150" x2="0" y2="150" stroke="#C89B3C" stroke-width="1.4" opacity="0.4"/>
    <!-- suggested landmasses -->
    <g fill="#C89B3C" opacity="0.5">
      <path d="M-92 -40 q20 -22 44 -12 q10 20 -6 34 q-20 18 -40 6 q-14 -14 2 -28 Z"/>
      <path d="M-70 30 q16 -6 26 10 q6 26 -12 40 q-18 8 -24 -14 q-6 -24 10 -36 Z"/>
      <path d="M40 -46 q30 -10 52 8 q8 22 -14 30 q-34 10 -46 -12 q-6 -18 8 -26 Z"/>
      <path d="M34 26 q26 -4 34 18 q2 22 -20 26 q-24 2 -28 -20 q-2 -18 14 -24 Z"/>
    </g>
  </g>
  <!-- eagle, wings spread across the globe -->
  <g fill="#F7F5EF">
    <!-- left wing -->
    <path d="M450 190 C388 150 322 150 250 176 C300 172 330 186 356 206 C312 200 286 210 262 230 C312 220 344 232 372 250 C428 214 448 206 450 200 Z"/>
    <!-- right wing (mirror) -->
    <path d="M450 190 C512 150 578 150 650 176 C600 172 570 186 544 206 C588 200 614 210 638 230 C588 220 556 232 528 250 C472 214 452 206 450 200 Z"/>
    <!-- body + tail -->
    <path d="M450 196 C458 196 462 206 461 220 C460 240 456 260 450 276 C444 260 440 240 439 220 C438 206 442 196 450 196 Z"/>
    <!-- head -->
    <circle cx="450" cy="182" r="12"/>
    <path d="M450 176 l16 4 l-16 6 Z" fill="#C89B3C"/>  <!-- beak -->
  </g>
  <!-- banner ribbon -->
  <g>
    <path d="M300 372 L600 372 L582 400 L600 428 L300 428 L318 400 Z" fill="#B22234"/>
    <path d="M300 372 L318 400 L300 428 L276 428 L294 400 L276 372 Z" fill="#8a1a26"/>
    <path d="M600 372 L582 400 L600 428 L624 428 L606 400 L624 372 Z" fill="#8a1a26"/>
    <text x="450" y="406" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-size="20" fill="#F7F5EF">Reform &amp; Empire</text>
  </g>
</svg>
"""

UNITS = [
    dict(
        slug="unit2_cover", no="Two",
        title="The Gilded Age",
        subtitle="Progress, Poverty, and the Price of Growth",
        era="1870 &ndash; 1900",
        eq="Who benefited from America&rsquo;s industrial revolution, and at whose expense did that prosperity come?",
        standards="US.08 &ndash; US.18", ssp="SSP.06 &middot; Geographic Awareness", days="18 days",
        tn="Coal Creek War, Anderson County (1891&ndash;92)",
        art=ART_U2,
    ),
    dict(
        slug="unit3_cover", no="Three",
        title="Progressive Era &amp; Imperialism",
        subtitle="Reform and Empire: Can America Be Both a Democracy and a World Power?",
        era="1890 &ndash; 1920",
        eq="Can government fix the problems created by industrial capitalism &mdash; and what does the reach for empire reveal about America&rsquo;s values?",
        standards="US.19 &ndash; US.27", ssp="SSP.04 &middot; Argue with Evidence", days="18 days",
        tn="Ida B. Wells, Memphis, TN",
        art=ART_U3,
    ),
]

TEMPLATE = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>{title}</title>
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
    <div class="art">{art}</div>
    <div class="eq"><div class="lbl">Essential Question</div><div class="q">{eq}</div></div>
    <div class="meta">
      <div class="m"><div class="k">Standards</div><div class="v">{standards}</div></div>
      <div class="m"><div class="k">Primary Practice</div><div class="v">{ssp}</div></div>
      <div class="m"><div class="k">Pacing</div><div class="v">{days}</div></div>
      <div class="m"><div class="k">&#9733; Tennessee</div><div class="v"><span class="star">&#9733;</span> {tn}</div></div>
    </div>
    <div class="foot">
      <span class="b">U.S. History Hack&trade; &nbsp;&middot;&nbsp; &copy; 2026 TroopToTeacher Technologies LLC</span>
      <span class="repro">Reproducible</span>
    </div>
  </div>
</div></body></html>"""

os.makedirs(PAGES, exist_ok=True)
for u in UNITS:
    html = TEMPLATE.format(css=CSS, **u)
    with open(os.path.join(PAGES, f"{u['slug']}.html"), "w") as f:
        f.write(html)
    print("wrote", u["slug"])
