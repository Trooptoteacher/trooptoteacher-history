# -*- coding: utf-8 -*-
"""Unit 2 labeled matrix.
US.14: The Muckrakers -- compare four investigative reformers across the same
       three criteria (what they exposed | the work / their method | the reform
       it drove). Signature works seeded as faint identity hints under each name.
TN tie: Edward Ward Carmack, Nashville newspaper editor.
Neutral framing: descriptive criteria; students judge the impact.
"""

CSS = r"""
  .mx{ flex:1 1 auto; display:grid; gap:5px; min-height:0; }
  .mx .corner{ background:transparent; }
  .mx .chead{ color:#fff; font-weight:800; font-size:10pt; text-align:center; padding:7px 6px; border-radius:6px; display:flex; flex-direction:column; justify-content:center; background:var(--navy); }
  .mx .chead small{ font-weight:600; font-size:7.4pt; opacity:.92; }
  .mx .rhead{ background:var(--navy); color:#fff; font-weight:800; font-size:9.6pt; padding:6px 9px; border-radius:6px; display:flex; flex-direction:column; justify-content:center; }
  .mx .rhead small{ font-weight:600; font-size:7.4pt; opacity:.9; font-style:italic; }
  .mx .cell{ background:var(--paper); border:1.5px solid var(--rule); border-radius:6px;
             background-image:repeating-linear-gradient(to bottom, transparent 0 26px, var(--wl) 26px 27px);
             background-position:0 9px; }
  .tnbox{ flex:0 0 auto; margin-top:7px; background:var(--gold-tint); border:1.6px solid var(--gold); border-left:6px solid var(--gold);
          border-radius:0 6px 6px 0; padding:7px 12px; display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.9pt; line-height:1.32; color:#3a2f12; }
  .tnbox .t b{ color:#7a5c15; }
  .cbar{ flex:0 0 auto; margin-top:7px; background:var(--cream); border:1.6px solid var(--gold); border-left:6px solid var(--gold);
         border-radius:0 6px 6px 0; padding:7px 11px; font-size:9pt; color:var(--navy); } .cbar b{ color:var(--navy); }
"""

COLS = [("What they exposed", ""),
        ("The work / their method", ""),
        ("The reform it drove", "")]
REFORMERS = [
    ("Ida Tarbell", "The History of Standard Oil (1904)"),
    ("Upton Sinclair", "The Jungle (1906) &middot; meatpacking"),
    ("Lincoln Steffens", "The Shame of the Cities (1904)"),
    ("Robert La Follette", "the &ldquo;Wisconsin Idea&rdquo;"),
]

def _grid():
    cells = ['<div class="corner"></div>']
    for nm, sub in COLS:
        cells.append(f'<div class="chead">{nm}</div>')
    for nm, sub in REFORMERS:
        cells.append(f'<div class="rhead">{nm}<small>{sub}</small></div>')
        for _ in COLS:
            cells.append('<div class="cell"></div>')
    return ('<div class="mx" style="grid-template-columns:0.95fr 1fr 1fr 1fr; '
            'grid-template-rows:auto 1fr 1fr 1fr 1fr;">' + "".join(cells) + '</div>')

BODY = f"""
    <div class="prompt">Compare the muckrakers across the same three questions. Look for how <b>investigation</b> turned into <b>reform</b>.</div>
    {_grid()}
    <div class="tnbox">
      <span class="star">&#9733;</span>
      <span class="t"><b>Tennessee Connection &mdash;</b> Edward Ward Carmack, a Nashville newspaper editor,
      used his platform to expose corruption.</span>
    </div>
    <div class="cbar"><b>Pattern:</b> What does muckraking reveal about the power of information in a democracy? ______________________________________</div>
"""

_UDL = dict(
    scaffold="Complete Tarbell&rsquo;s row together as the model; give a word bank (monopoly, meatpacking, corruption, exposure) for the rest.",
    extend="Rank the four by how much reform each investigation drove, and defend your order with matrix evidence.",
    show="Students may <b>write</b> in cells, <b>say</b> a row aloud, <b>draw</b> a headline for each, or <b>build</b> it as a matching sort.")

ORGANIZERS = [
    dict(
        slug="26_us14_matrix",
        title="The Muckrakers",
        kicker="Unit 2 &middot; US.14 &middot; Best-Fit Organizer",
        chips=[("Matrix &middot; Compare Reformers", "navy"), ("DOK 2&ndash;3 &middot; Analysis", "skill")],
        why=("Comparing reformers on the same criteria shows how investigative journalism turned exposure into reform &mdash; "
             "a defining engine of the Progressive Era. "
             "<span class='cite'>Structured comparison across criteria is Marzano&rsquo;s highest-yield strategy; SSP.03 synthesize.</span>"),
        body=BODY, extra_css=CSS, udl=_UDL, tn=True,
        role="Teacher Graphic Organizer Toolkit &middot; Unit 2 &middot; US.14 (labeled)",
    ),
]
