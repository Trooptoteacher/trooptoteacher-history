# -*- coding: utf-8 -*-
"""Unit 3 labeled matrix.
US.22: Big Stick (T. Roosevelt) vs Dollar (Taft) vs Moral (Wilson) diplomacy.
Compare three approaches across the same four criteria (core idea | main tool |
a real example | view of using force). Pre-loaded content is a FADED italic
watermark inside each LIGHT cell, so students can write over it.
TN tie: Cordell Hull of Pickett County, Tennessee.
Neutral framing: descriptive criteria only; students argue best fit on the line.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .mx{ flex:1 1 auto; display:grid; gap:5px; min-height:0;
       grid-template-columns:0.82fr 1fr 1fr 1fr;
       grid-template-rows:auto 1fr 1fr 1fr 1fr; }
  .mx .corner{ background:transparent; display:flex; flex-direction:column;
       justify-content:flex-end; align-items:flex-start; padding:2px 4px;
       font-size:7.4pt; font-weight:800; letter-spacing:.03em; color:var(--muted);
       text-transform:uppercase; line-height:1.25; }
  .mx .chead{ color:#fff; font-weight:800; font-size:10.5pt; text-align:center;
       padding:7px 6px; border-radius:6px; display:flex; flex-direction:column;
       justify-content:center; background:var(--navy); line-height:1.05; }
  .mx .chead small{ font-weight:600; font-size:7.3pt; opacity:.92; margin-top:2px; }
  .mx .rhead{ background:var(--navy); color:#fff; font-weight:800; font-size:9.6pt;
       padding:6px 9px; border-radius:6px; display:flex; flex-direction:column;
       justify-content:center; line-height:1.1; }
  .mx .cell{ position:relative; background:var(--paper); border:1.5px solid var(--rule);
       border-radius:6px; overflow:hidden;
       background-image:repeating-linear-gradient(to bottom, transparent 0 25px, var(--wl) 25px 26px);
       background-position:0 30px; background-clip:content-box; }
  .mx .fh{ position:absolute; top:6px; left:9px; right:9px; font-size:7.6pt;
       font-style:italic; color:#9aa6bd; line-height:1.22; }
  .tnbox{ flex:0 0 auto; margin-top:7px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.8pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
  .cbar{ flex:0 0 auto; margin-top:7px; background:var(--cream); border:1.6px solid var(--gold);
         border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 11px;
         font-size:9pt; color:var(--navy); } .cbar b{ color:var(--navy); }
"""

# three approaches (dark navy column labels)
COLS = [
    ("Big Stick", "T. Roosevelt &middot; 1901&ndash;1909"),
    ("Dollar", "Taft &middot; 1909&ndash;1913"),
    ("Moral", "Wilson &middot; 1913&ndash;1921"),
]

# criterion label + faded one-line hint for each of the three approaches
ROWS = [
    ("Core idea", [
        "&ldquo;speak softly and carry a big stick&rdquo;",
        "influence through American business &amp; investment",
        "reject imperialism; back democratic governments",
    ]),
    ("Main tool", [
        "military &amp; naval strength",
        "loans &amp; investment",
        "diplomacy &amp; moral pressure",
    ]),
    ("A real example", [
        "Panama Canal &middot; Roosevelt Corollary",
        "Latin America &amp; East Asia investments",
        "Mexico intervention debate",
    ]),
    ("View of using force", [
        "willing to use force",
        "force as a backup",
        "force only as a last resort",
    ]),
]


def _grid():
    cells = ['<div class="corner">Approach&nbsp;&rarr;<br>Criteria&nbsp;&darr;</div>']
    for nm, sub in COLS:
        cells.append(f'<div class="chead">{nm}<small>{sub}</small></div>')
    for crit, hints in ROWS:
        cells.append(f'<div class="rhead">{crit}</div>')
        for h in hints:
            cells.append(f'<div class="cell"><span class="fh">{h}</span></div>')
    return '<div class="mx">' + "".join(cells) + '</div>'


BODY = f"""
    <div class="prompt">Compare the three approaches across the same four questions. The faint notes are starters &mdash; <b>write over them</b> in your own words, then look for the <b>pattern</b>.</div>
    {_grid()}
    <div class="tnbox">
      <span class="star">&#9733;</span>
      <span class="t"><b>Tennessee Connection &mdash;</b> <b>Cordell Hull</b> of Pickett County, Tennessee served in
      Congress during this era; he favored international <b>trade agreements</b> over military intervention &mdash; later
      the longest-serving U.S. Secretary of State and a Nobel Peace Prize winner.</span>
    </div>
    <div class="cbar"><b>Your call:</b> Which approach best fit this era? ____________ <b>because</b> ______________________________________</div>
"""

_UDL = dict(
    scaffold="Fill the <b>Core idea</b> row together first as the model, then let students complete the rest by column.",
    extend="Argue which approach best fit the era &mdash; use evidence from the matrix to defend your &ldquo;___ because ___&rdquo; line.",
    show="Students may <b>write</b> in cells, <b>say</b> a column aloud, or <b>chart</b> the three side by side.")

ORGANIZERS = [
    dict(
        slug="23_us22_matrix",
        title="Three Ways to Lead in the World",
        kicker="Unit 3 &middot; US.22 &middot; Best&#8209;Fit Organizer",
        chips=[("Comparison Matrix", "navy"), ("&#9733; Tennessee Connection", "gold"),
               ("DOK 2&#8211;3 &middot; Compare", "skill")],
        why=("A matrix holds several cases against one yardstick, so patterns across the three diplomacies pop into view. "
             "<span class='cite'>Comparing on structured criteria &mdash; identifying similarities &amp; differences &mdash; "
             "is Marzano&rsquo;s highest-yield strategy; SSP.03 synthesize.</span>"),
        body=BODY, extra_css=CSS, udl=_UDL,
        role="Teacher Graphic Organizer Toolkit &middot; Unit 3 &middot; US.22 (labeled)",
    ),
]
