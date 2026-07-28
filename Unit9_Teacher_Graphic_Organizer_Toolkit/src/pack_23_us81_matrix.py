# -*- coding: utf-8 -*-
"""Unit 9 labeled matrix -- US.81 Civil & Voting Rights Legislation.
Compare four landmark laws (Civil Rights Act 1964 | Voting Rights Act 1965 |
Civil Rights Act 1968 | 24th Amendment) across the same two questions (what it did |
impact). Faded italic hints in LIGHT cells. HAS a Tennessee Connection.
Content approved for US.81.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .mx{ flex:1 1 auto; display:grid; gap:4px; min-height:0;
       grid-template-columns:0.5fr 1fr 1fr 1fr 1fr;
       grid-template-rows:auto 1fr 1fr; }
  .mx .corner{ background:transparent; display:flex; flex-direction:column;
       justify-content:flex-end; align-items:flex-start; padding:2px 3px;
       font-size:6.9pt; font-weight:800; letter-spacing:.02em; color:var(--muted);
       text-transform:uppercase; line-height:1.22; }
  .mx .chead{ color:#fff; font-weight:800; font-size:8.7pt; text-align:center;
       padding:6px 4px; border-radius:6px; display:flex; flex-direction:column;
       justify-content:center; background:var(--navy); line-height:1.04; }
  .mx .chead small{ font-weight:600; font-size:6.7pt; opacity:.92; margin-top:2px; }
  .mx .rhead{ background:var(--navy); color:#fff; font-weight:800; font-size:8.6pt;
       padding:5px 7px; border-radius:6px; display:flex; flex-direction:column;
       justify-content:center; line-height:1.1; }
  .mx .cell{ position:relative; background:var(--paper); border:1.5px solid var(--rule);
       border-radius:6px; overflow:hidden;
       background-image:repeating-linear-gradient(to bottom, transparent 0 25px, var(--wl) 25px 26px);
       background-position:0 30px; background-clip:content-box; }
  .mx .fh{ position:absolute; top:5px; left:7px; right:7px; font-size:7.1pt;
       font-style:italic; color:#9aa6bd; line-height:1.24; }
  .tnbox{ flex:0 0 auto; margin-top:7px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.6pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""

COLS = [
    ("Civil Rights Act", "1964"),
    ("Voting Rights Act", "1965"),
    ("Civil Rights Act", "1968 &middot; Fair Housing"),
    ("24th Amendment", "1964"),
]

ROWS = [
    ("What it did", [
        "banned discrimination in public places, jobs &amp; federal programs; created the EEOC",
        "banned literacy tests; sent federal registrars to low&#8209;registration areas",
        "banned discrimination in housing sales, rentals &amp; financing",
        "eliminated <b>poll taxes</b> in federal elections",
    ]),
    ("Impact", [
        "ended legal segregation in public facilities; opened economic doors",
        "Black voter registration in the South rose <b>23% &rarr; 61%</b> by 1969",
        "addressed residential segregation &mdash; though enforcement stayed weak",
        "removed an economic barrier that kept poor Black &amp; white voters from the polls",
    ]),
]


def _grid():
    cells = ['<div class="corner">Law&nbsp;&rarr;<br>Compare&nbsp;&darr;</div>']
    for nm, sub in COLS:
        cells.append(f'<div class="chead">{nm}<small>{sub}</small></div>')
    for crit, hints in ROWS:
        cells.append(f'<div class="rhead">{crit}</div>')
        for h in hints:
            cells.append(f'<div class="cell"><span class="fh">{h}</span></div>')
    return '<div class="mx">' + "".join(cells) + '</div>'


BODY = f"""
    <div class="prompt">Compare the four laws across the same two questions. The faint notes are starters &mdash; <b>write over them</b>, then notice how together they dismantled legal segregation piece by piece.</div>
    {_grid()}
    <div class="tnbox">
      <span class="star">&#9733;</span>
      <span class="t"><b>Tennessee Connection &mdash;</b> Tennessee was a voting&#8209;rights battleground, with major
      <b>voter&#8209;registration drives in Memphis and Nashville</b>. The state&rsquo;s compliance with the <b>Voting Rights
      Act of 1965</b> transformed political participation for African Americans across Tennessee.</span>
    </div>
"""

_UDL = dict(
    scaffold="Fill the <b>&ldquo;What it did&rdquo;</b> row together first, then let students complete the impact of each law.",
    extend="Which law changed the most lives, and how do you know? Use the &ldquo;impact&rdquo; row as evidence.",
    show="Students may <b>write</b> in cells, <b>say</b> a column aloud, or <b>match</b> each law to the problem it solved.")

ORGANIZERS = [
    dict(
        slug="23_us81_matrix",
        title="Four Laws That Ended Legal Segregation",
        kicker="Unit 9 &middot; US.81 &middot; Best&#8209;Fit Organizer",
        chips=[("Comparison Matrix", "navy"), ("&#9733; Tennessee Connection", "gold"),
               ("DOK 2&#8211;3 &middot; Analyze", "skill")],
        why=("A matrix holds the four laws against the same two questions, so students see what each one changed &mdash; "
             "and how they fit together into one legal framework. "
             "<span class='cite'>Comparing on structured criteria is Marzano&rsquo;s highest&#8209;yield strategy; SSP.03 synthesize.</span>"),
        body=BODY, extra_css=CSS, udl=_UDL,
        role="Teacher Graphic Organizer Toolkit &middot; Unit 9 &middot; US.81 (labeled)",
    ),
]
