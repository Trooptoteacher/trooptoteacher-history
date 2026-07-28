# -*- coding: utf-8 -*-
"""Unit 6 labeled matrix -- US.50 Major WWII Battles.
Compare four battles (Midway | Iwo Jima | Okinawa | D-Day) across the same three
criteria (when & where | key geographic/military factor | outcome & why it
mattered). Faded italic hints in LIGHT cells. Neutral framing. HAS a Tennessee
Connection. Content approved for US.50.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .mx{ flex:1 1 auto; display:grid; gap:4px; min-height:0;
       grid-template-columns:0.62fr 1fr 1fr 1fr 1fr;
       grid-template-rows:auto 1fr 1.15fr 1.15fr; }
  .mx .corner{ background:transparent; display:flex; flex-direction:column;
       justify-content:flex-end; align-items:flex-start; padding:2px 3px;
       font-size:6.9pt; font-weight:800; letter-spacing:.02em; color:var(--muted);
       text-transform:uppercase; line-height:1.22; }
  .mx .chead{ color:#fff; font-weight:800; font-size:9pt; text-align:center;
       padding:6px 4px; border-radius:6px; display:flex; flex-direction:column;
       justify-content:center; background:var(--navy); line-height:1.03; }
  .mx .chead small{ font-weight:600; font-size:6.6pt; opacity:.92; margin-top:2px; }
  .mx .chead.eu{ background:#3a2f6a; }
  .mx .rhead{ background:var(--navy); color:#fff; font-weight:800; font-size:8.4pt;
       padding:5px 7px; border-radius:6px; display:flex; flex-direction:column;
       justify-content:center; line-height:1.1; }
  .mx .cell{ position:relative; background:var(--paper); border:1.5px solid var(--rule);
       border-radius:6px; overflow:hidden;
       background-image:repeating-linear-gradient(to bottom, transparent 0 24px, var(--wl) 24px 25px);
       background-position:0 28px; background-clip:content-box; }
  .mx .fh{ position:absolute; top:5px; left:7px; right:7px; font-size:7pt;
       font-style:italic; color:#9aa6bd; line-height:1.2; }
  .tnbox{ flex:0 0 auto; margin-top:7px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.6pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""

COLS = [
    ("Midway", "Pacific", False),
    ("Iwo Jima", "Pacific", False),
    ("Okinawa", "Pacific", False),
    ("D&#8209;Day", "Europe", True),
]

ROWS = [
    ("When &amp; where", [
        "June 1942 &middot; central Pacific atoll",
        "Feb.&ndash;Mar. 1945 &middot; volcanic island",
        "Apr.&ndash;June 1945 &middot; 340 mi. from Japan",
        "June 6, 1944 &middot; Normandy, France",
    ]),
    ("Key geographic / military factor", [
        "U.S. codebreakers revealed Japan&rsquo;s plan; carriers ambushed the fleet",
        "volcanic terrain &amp; tunnels; airfields needed for B&#8209;29 bombers",
        "close to Japan &mdash; a staging base for an invasion",
        "largest amphibious invasion ever; Eisenhower in command",
    ]),
    ("Outcome &amp; why it mattered", [
        "4 Japanese carriers sunk &mdash; the Pacific turning point",
        "costly Marine victory; iconic flag on Mt.&nbsp;Suribachi",
        "bloodiest Pacific battle &mdash; showed the cost of invading Japan",
        "opened the Western Front; freed France; squeezed Germany",
    ]),
]


def _grid():
    cells = ['<div class="corner">Battle&nbsp;&rarr;<br>Compare&nbsp;&darr;</div>']
    for nm, sub, eu in COLS:
        cells.append(f'<div class="chead{" eu" if eu else ""}">{nm}<small>{sub}</small></div>')
    for crit, hints in ROWS:
        cells.append(f'<div class="rhead">{crit}</div>')
        for h in hints:
            cells.append(f'<div class="cell"><span class="fh">{h}</span></div>')
    return '<div class="mx">' + "".join(cells) + '</div>'


BODY = f"""
    <div class="prompt">Compare the four battles across the same three questions. The faint notes are starters &mdash; <b>write over them</b>, then look for the pattern: how <b>geography</b> and <b>military factors</b> shaped each outcome.</div>
    {_grid()}
    <div class="tnbox">
      <span class="star">&#9733;</span>
      <span class="t"><b>Tennessee Connection &mdash;</b> Tennesseans served in every major battle of WWII. The
      <b>30th Infantry Division</b>, with Tennessee soldiers, fought from Normandy to the Elbe, and <b>Camp Forrest</b>
      near Tullahoma trained troops who fought at Normandy, Iwo Jima, and across the Pacific.</span>
    </div>
"""

_UDL = dict(
    scaffold="Fill the <b>When &amp; where</b> row together first, then let students complete each battle by column.",
    extend="Which mattered more to each outcome &mdash; <b>geography</b> or a <b>military decision</b>? Defend your answer for one battle.",
    show="Students may <b>write</b> in cells, <b>say</b> a column aloud, or <b>map</b> the four battle sites.")

ORGANIZERS = [
    dict(
        slug="25_us50_matrix",
        title="Four Battles That Turned the War",
        kicker="Unit 6 &middot; US.50 &middot; Best&#8209;Fit Organizer",
        chips=[("Comparison Matrix", "navy"), ("&#9733; Tennessee Connection", "gold"),
               ("DOK 2&#8211;3 &middot; Compare", "skill")],
        why=("A matrix holds four battles against one yardstick, so students see how <b>geography and military factors</b> "
             "shaped each outcome across the Pacific and European theaters. "
             "<span class='cite'>Comparing on structured criteria is Marzano&rsquo;s highest&#8209;yield strategy; SSP.03 synthesize.</span>"),
        body=BODY, extra_css=CSS, udl=_UDL,
        role="Teacher Graphic Organizer Toolkit &middot; Unit 6 &middot; US.50 (labeled)",
    ),
]
