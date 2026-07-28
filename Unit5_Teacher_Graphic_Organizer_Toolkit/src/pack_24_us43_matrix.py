# -*- coding: utf-8 -*-
"""Unit 5 labeled matrix -- US.43 FDR's New Deal: the three R's.
Compare the three families of New Deal action (Relief | Recovery | Reform) across
the same three criteria (which programs | what it did | still around today?).
Pre-loaded programs are a FADED italic watermark inside each LIGHT cell so students
write over it. TN tie: the TVA (Norris Dam). Neutral framing; students judge which
mattered most. Content approved for US.43.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .mx{ flex:1 1 auto; display:grid; gap:5px; min-height:0;
       grid-template-columns:0.82fr 1fr 1fr 1fr;
       grid-template-rows:auto 1.25fr 1fr 1fr; }
  .mx .corner{ background:transparent; display:flex; flex-direction:column;
       justify-content:flex-end; align-items:flex-start; padding:2px 4px;
       font-size:7.4pt; font-weight:800; letter-spacing:.03em; color:var(--muted);
       text-transform:uppercase; line-height:1.25; }
  .mx .chead{ color:#fff; font-weight:800; font-size:10.5pt; text-align:center;
       padding:7px 6px; border-radius:6px; display:flex; flex-direction:column;
       justify-content:center; background:var(--navy); line-height:1.05; }
  .mx .chead small{ font-weight:600; font-size:7.3pt; opacity:.92; margin-top:2px; }
  .mx .rhead{ background:var(--navy); color:#fff; font-weight:800; font-size:9.4pt;
       padding:6px 9px; border-radius:6px; display:flex; flex-direction:column;
       justify-content:center; line-height:1.1; }
  .mx .cell{ position:relative; background:var(--paper); border:1.5px solid var(--rule);
       border-radius:6px; overflow:hidden;
       background-image:repeating-linear-gradient(to bottom, transparent 0 25px, var(--wl) 25px 26px);
       background-position:0 30px; background-clip:content-box; }
  .mx .fh{ position:absolute; top:6px; left:9px; right:9px; font-size:7.6pt;
       font-style:italic; color:#9aa6bd; line-height:1.24; }
  .tnbox{ flex:0 0 auto; margin-top:7px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.8pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
  .cbar{ flex:0 0 auto; margin-top:7px; background:var(--cream); border:1.6px solid var(--gold);
         border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 11px;
         font-size:9pt; color:var(--navy); } .cbar b{ color:var(--navy); }
"""

COLS = [
    ("Relief", "help people <i>now</i>"),
    ("Recovery", "restart the economy"),
    ("Reform", "prevent the next crash"),
]

ROWS = [
    ("Which programs", [
        "CCC &mdash; jobs for young men (3B trees); WPA &mdash; 8.5M jobs (roads, schools, arts)",
        "AAA &mdash; pay farmers to cut output; NRA &mdash; industry codes; TVA &mdash; dams &amp; power",
        "FDIC &mdash; insures deposits; SEC &mdash; regulates markets; Social Security; FLSA (min. wage)",
    ]),
    ("What it did", [
        "immediate jobs &amp; aid for the jobless",
        "raise prices; restart farms &amp; industry",
        "fix the rules so a crash can&rsquo;t repeat",
    ]),
    ("Still around today?", [
        "CCC &amp; WPA ended, but modeled later job programs",
        "AAA &amp; NRA struck down by the Court; <b>TVA still runs</b>",
        "FDIC, SEC, Social Security &amp; FLSA all continue today",
    ]),
]


def _grid():
    cells = ['<div class="corner">The 3 R&rsquo;s&nbsp;&rarr;<br>Compare&nbsp;&darr;</div>']
    for nm, sub in COLS:
        cells.append(f'<div class="chead">{nm}<small>{sub}</small></div>')
    for crit, hints in ROWS:
        cells.append(f'<div class="rhead">{crit}</div>')
        for h in hints:
            cells.append(f'<div class="cell"><span class="fh">{h}</span></div>')
    return '<div class="mx">' + "".join(cells) + '</div>'


BODY = f"""
    <div class="prompt">Sort the New Deal into the <b>three R&rsquo;s</b> and compare them across the same three questions. The faint notes name key programs &mdash; <b>write over them</b>, then decide which R mattered most.</div>
    {_grid()}
    <div class="tnbox">
      <span class="star">&#9733;</span>
      <span class="t"><b>Tennessee Connection &mdash;</b> The <b>Tennessee Valley Authority (TVA)</b>, created in 1933, was
      one of the most impactful New Deal programs &mdash; bringing <b>electricity, flood control, and development</b> to
      one of the nation&rsquo;s poorest regions. <b>Norris Dam</b> was the first dam TVA completed, and TVA still operates today.</span>
    </div>
    <div class="cbar"><b>Your call:</b> Which New Deal program had the most <b>lasting</b> impact? ____________ <b>because</b> ________________________</div>
"""

_UDL = dict(
    scaffold="Teach the three R&rsquo;s first (Relief = help now, Recovery = restart, Reform = prevent). Sort a few programs together before students finish.",
    extend="Argue which R mattered most &mdash; and defend your &ldquo;___ because ___&rdquo; line with evidence from the &ldquo;still around today?&rdquo; row.",
    show="Students may <b>write</b> in cells, <b>say</b> a column aloud, or <b>sort</b> program cards into the three R&rsquo;s.")

ORGANIZERS = [
    dict(
        slug="24_us43_matrix",
        title="The New Deal&rsquo;s Three R&rsquo;s: Relief, Recovery, Reform",
        kicker="Unit 5 &middot; US.43 &middot; Best&#8209;Fit Organizer",
        chips=[("Comparison Matrix", "navy"), ("&#9733; Tennessee Connection", "gold"),
               ("DOK 2&#8211;3 &middot; Compare", "skill")],
        why=("The New Deal had many programs; a matrix sorts them into the <b>three R&rsquo;s</b> and holds each against one "
             "yardstick, so their purpose and legacy compare clearly. "
             "<span class='cite'>Comparing on structured criteria is Marzano&rsquo;s highest&#8209;yield strategy; SSP.03 synthesize.</span>"),
        body=BODY, extra_css=CSS, udl=_UDL,
        role="Teacher Graphic Organizer Toolkit &middot; Unit 5 &middot; US.43 (labeled)",
    ),
]
