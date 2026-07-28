# -*- coding: utf-8 -*-
"""Unit 8 labeled matrix -- US.77 Kennedy's New Frontier.
Compare four New Frontier initiatives (Education | Civil Rights | Peace Corps |
Space) across the same three criteria (goal | what Kennedy did | result). Faded
italic hints in LIGHT cells. Neutral framing -- includes that many programs stalled
in Congress. HAS a Tennessee Connection. Content approved for US.77.
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
    ("Education", "schools &amp; college"),
    ("Civil Rights", "end discrimination"),
    ("Peace Corps", "service abroad"),
    ("Space", "reach the Moon"),
]

ROWS = [
    ("Goal", [
        "improve schools &amp; expand college access",
        "enforce desegregation &amp; voting rights",
        "promote U.S. values through service, not force",
        "beat the USSR to the Moon",
    ]),
    ("What Kennedy did", [
        "proposed federal aid to education",
        "used federal power to enforce civil rights",
        "created the Peace Corps (1961) &mdash; volunteers abroad",
        "made a Moon landing a national priority (after Sputnik &amp; Gagarin)",
    ]),
    ("Result", [
        "much of it stalled in Congress",
        "limited progress; strong resistance",
        "thousands served; lasting goodwill &mdash; still runs today",
        "set the stage for Apollo 11 (1969)",
    ]),
]


def _grid():
    cells = ['<div class="corner">Program&nbsp;&rarr;<br>Compare&nbsp;&darr;</div>']
    for nm, sub in COLS:
        cells.append(f'<div class="chead">{nm}<small>{sub}</small></div>')
    for crit, hints in ROWS:
        cells.append(f'<div class="rhead">{crit}</div>')
        for h in hints:
            cells.append(f'<div class="cell"><span class="fh">{h}</span></div>')
    return '<div class="mx">' + "".join(cells) + '</div>'


BODY = f"""
    <div class="prompt">Compare the four New Frontier programs across the same three questions. The faint notes are starters &mdash; <b>write over them</b>, then notice which succeeded and which stalled.</div>
    {_grid()}
    <div class="tnbox">
      <span class="star">&#9733;</span>
      <span class="t"><b>Tennessee Connection &mdash;</b> The New Frontier reached Tennessee directly: the <b>Area
      Redevelopment Act</b> targeted <b>Appalachian Tennessee</b>, one of the nation&rsquo;s poorest regions, and the
      administration&rsquo;s push for <b>education spending</b> benefited Tennessee schools.</span>
    </div>
"""

_UDL = dict(
    scaffold="Fill the <b>Goal</b> row together first, then let students complete each program by column.",
    extend="Which New Frontier program succeeded most, and which fell short? Use the &ldquo;result&rdquo; row as evidence.",
    show="Students may <b>write</b> in cells, <b>say</b> a column aloud, or <b>rank</b> the four programs by impact.")

ORGANIZERS = [
    dict(
        slug="26_us77_matrix",
        title="Kennedy&rsquo;s New Frontier: Big Goals, Mixed Results",
        kicker="Unit 8 &middot; US.77 &middot; Best&#8209;Fit Organizer",
        chips=[("Comparison Matrix", "navy"), ("&#9733; Tennessee Connection", "gold"),
               ("DOK 2&#8211;3 &middot; Compare", "skill")],
        why=("A matrix holds the four New Frontier programs against one yardstick, so students see each one&rsquo;s goal, "
             "action, and result &mdash; and why some passed while others stalled. "
             "<span class='cite'>Comparing on structured criteria is Marzano&rsquo;s highest&#8209;yield strategy; SSP.03 synthesize.</span>"),
        body=BODY, extra_css=CSS, udl=_UDL,
        role="Teacher Graphic Organizer Toolkit &middot; Unit 8 &middot; US.77 (labeled)",
    ),
]
