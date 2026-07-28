# -*- coding: utf-8 -*-
"""Unit 10 labeled matrix -- US.91 The Clinton Administration.
Compare four defining events (NAFTA | Welfare Reform | Balanced Budget |
Impeachment) across the same two questions (what it was | outcome). Faded italic
hints in LIGHT cells. Balanced framing. HAS a Tennessee Connection.
Content approved for US.91.
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
  .mx .chead{ color:#fff; font-weight:800; font-size:8.6pt; text-align:center;
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
    ("NAFTA", "1994 &middot; free trade"),
    ("Welfare Reform", "1996 &middot; work rules"),
    ("Balanced Budget", "first since 1969"),
    ("Impeachment", "1998&ndash;99"),
]

ROWS = [
    ("What it was", [
        "ended trade barriers among the U.S., Canada &amp; Mexico",
        "work requirements &amp; time limits replaced older welfare (TANF)",
        "growth &amp; tax increases erased the federal deficit",
        "the Lewinsky affair &rarr; charges of perjury &amp; obstruction",
    ]),
    ("Outcome", [
        "trade rose &mdash; but many manufacturing jobs moved to Mexico",
        "welfare rolls fell sharply; poverty reduction was limited",
        "budget surpluses &mdash; a strong late&#8209;1990s economy",
        "the House impeached; the Senate <b>acquitted</b> &mdash; a party&#8209;line split",
    ]),
]


def _grid():
    cells = ['<div class="corner">Event&nbsp;&rarr;<br>Compare&nbsp;&darr;</div>']
    for nm, sub in COLS:
        cells.append(f'<div class="chead">{nm}<small>{sub}</small></div>')
    for crit, hints in ROWS:
        cells.append(f'<div class="rhead">{crit}</div>')
        for h in hints:
            cells.append(f'<div class="cell"><span class="fh">{h}</span></div>')
    return '<div class="mx">' + "".join(cells) + '</div>'


BODY = f"""
    <div class="prompt">Compare the four events across the same two questions. The faint notes are starters &mdash; <b>write over them</b>, then notice how prosperity and scandal ran side by side.</div>
    {_grid()}
    <div class="tnbox">
      <span class="star">&#9733;</span>
      <span class="t"><b>Tennessee Connection &mdash;</b> Vice President <b>Al Gore of Carthage, Tennessee</b>, shaped the
      administration&rsquo;s technology policy and the &ldquo;information superhighway.&rdquo; He later won the <b>Nobel Peace
      Prize</b> for his environmental advocacy.</span>
    </div>
"""

_UDL = dict(
    scaffold="Fill the <b>&ldquo;What it was&rdquo;</b> row together first, then let students complete each outcome by column.",
    extend="Clinton left office popular despite impeachment. Use the outcomes row to explain how that could be.",
    show="Students may <b>write</b> in cells, <b>say</b> a column aloud, or <b>rank</b> the four events by lasting impact.")

ORGANIZERS = [
    dict(
        slug="28_us91_matrix",
        title="The Clinton Years: Prosperity and Scandal",
        kicker="Unit 10 &middot; US.91 &middot; Best&#8209;Fit Organizer",
        chips=[("Comparison Matrix", "navy"), ("&#9733; Tennessee Connection", "gold"),
               ("DOK 2&#8211;3 &middot; Analyze", "skill")],
        why=("A matrix holds four very different events against the same two questions, so students see the era&rsquo;s "
             "booming economy and its political turmoil at once. "
             "<span class='cite'>Comparing on structured criteria is Marzano&rsquo;s highest&#8209;yield strategy; SSP.03.</span>"),
        body=BODY, extra_css=CSS, udl=_UDL,
        role="Teacher Graphic Organizer Toolkit &middot; Unit 10 &middot; US.91 (labeled)",
    ),
]
