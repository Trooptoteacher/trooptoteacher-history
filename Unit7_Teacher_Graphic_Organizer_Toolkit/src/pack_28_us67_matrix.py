# -*- coding: utf-8 -*-
"""Unit 7 labeled matrix -- US.67 Presidential Vietnam Policies.
Compare three presidents (Kennedy | Johnson | Nixon) across the same three criteria
(policy | what they did | result). Faded italic hints in LIGHT cells. Neutral
framing. HAS a Tennessee Connection (Albert Gore Sr.). Content approved for US.67.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .mx{ flex:1 1 auto; display:grid; gap:5px; min-height:0;
       grid-template-columns:0.72fr 1fr 1fr 1fr;
       grid-template-rows:auto 1fr 1.15fr 1.15fr; }
  .mx .corner{ background:transparent; display:flex; flex-direction:column;
       justify-content:flex-end; align-items:flex-start; padding:2px 4px;
       font-size:7.3pt; font-weight:800; letter-spacing:.03em; color:var(--muted);
       text-transform:uppercase; line-height:1.25; }
  .mx .chead{ color:#fff; font-weight:800; font-size:10pt; text-align:center;
       padding:7px 6px; border-radius:6px; display:flex; flex-direction:column;
       justify-content:center; background:var(--navy); line-height:1.05; }
  .mx .chead small{ font-weight:600; font-size:7.1pt; opacity:.92; margin-top:2px; }
  .mx .rhead{ background:var(--navy); color:#fff; font-weight:800; font-size:9pt;
       padding:6px 9px; border-radius:6px; display:flex; flex-direction:column;
       justify-content:center; line-height:1.1; }
  .mx .cell{ position:relative; background:var(--paper); border:1.5px solid var(--rule);
       border-radius:6px; overflow:hidden;
       background-image:repeating-linear-gradient(to bottom, transparent 0 25px, var(--wl) 25px 26px);
       background-position:0 28px; background-clip:content-box; }
  .mx .fh{ position:absolute; top:6px; left:9px; right:9px; font-size:7.6pt;
       font-style:italic; color:#9aa6bd; line-height:1.24; }
  .tnbox{ flex:0 0 auto; margin-top:7px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.6pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""

COLS = [
    ("Kennedy", "1961&ndash;63"),
    ("Johnson", "1963&ndash;69"),
    ("Nixon", "1969&ndash;74"),
]

ROWS = [
    ("Policy", [
        "&ldquo;Flexible Response&rdquo;",
        "Escalation",
        "&ldquo;Vietnamization&rdquo;",
    ]),
    ("What they did", [
        "advisors 700 &rarr; 16,000; counterinsurgency; avoided large combat",
        "Gulf of Tonkin &rarr; 543,000 troops by 1969; heavy bombing",
        "gradual withdrawal + bombing of Cambodia &amp; Laos; Paris Accords (1973)",
    ]),
    ("Result", [
        "set the stage for later escalation",
        "victory proved elusive; he chose not to run again",
        "U.S. exit &mdash; &ldquo;peace with honor&rdquo;; the South fell in 1975",
    ]),
]


def _grid():
    cells = ['<div class="corner">President&nbsp;&rarr;<br>Compare&nbsp;&darr;</div>']
    for nm, sub in COLS:
        cells.append(f'<div class="chead">{nm}<small>{sub}</small></div>')
    for crit, hints in ROWS:
        cells.append(f'<div class="rhead">{crit}</div>')
        for h in hints:
            cells.append(f'<div class="cell"><span class="fh">{h}</span></div>')
    return '<div class="mx">' + "".join(cells) + '</div>'


BODY = f"""
    <div class="prompt">Compare the three presidents across the same three questions. The faint notes are starters &mdash; <b>write over them</b>, then trace how the war grew, then wound down, across three administrations.</div>
    {_grid()}
    <div class="tnbox">
      <span class="star">&#9733;</span>
      <span class="t"><b>Tennessee Connection &mdash;</b> Tennessee&rsquo;s <b>Senator Albert Gore Sr.</b> was an early, vocal
      critic of the war, breaking with Johnson&rsquo;s escalation. His anti&#8209;war stance <b>cost him his Senate seat in
      1970</b> &mdash; a defeat that foreshadowed the South&rsquo;s political realignment.</span>
    </div>
"""

_UDL = dict(
    scaffold="Fill the <b>Policy</b> row together first, then let students complete each president by column.",
    extend="Which president had the hardest choices in Vietnam? Defend your answer using the &ldquo;result&rdquo; row.",
    show="Students may <b>write</b> in cells, <b>say</b> a column aloud, or build a <b>timeline</b> of the three presidencies.")

ORGANIZERS = [
    dict(
        slug="28_us67_matrix",
        title="Three Presidents, One War",
        kicker="Unit 7 &middot; US.67 &middot; Best&#8209;Fit Organizer",
        chips=[("Comparison Matrix", "navy"), ("&#9733; Tennessee Connection", "gold"),
               ("DOK 2&#8211;3 &middot; Compare", "skill")],
        why=("A matrix holds Kennedy, Johnson, and Nixon against one yardstick, so students see how each shaped the "
             "war &mdash; escalating it, then trying to end it. "
             "<span class='cite'>Comparing on structured criteria is Marzano&rsquo;s highest&#8209;yield strategy; SSP.03 synthesize.</span>"),
        body=BODY, extra_css=CSS, udl=_UDL,
        role="Teacher Graphic Organizer Toolkit &middot; Unit 7 &middot; US.67 (labeled)",
    ),
]
