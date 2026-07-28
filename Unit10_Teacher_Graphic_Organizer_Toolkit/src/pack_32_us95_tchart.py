# -*- coding: utf-8 -*-
"""Unit 10 labeled -- US.95 The Obama Administration (T-chart).
Two columns hold the presidency's major achievements and its setbacks, each a
labeled item with a FADED hint and write-lines. A synthesis band asks what the
era revealed about the powers and limits of the presidency. HAS a Tennessee
Connection. Content approved for US.95.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .tc2{ flex:1 1 auto; display:flex; gap:12px; min-height:0; }
  .tc2 .col{ flex:1 1 0; display:flex; flex-direction:column; min-height:0; }
  .tc2 .colhead{ color:#fff; font-weight:800; font-size:9.5pt; text-align:center; padding:6px 6px;
       border-radius:6px 6px 0 0; letter-spacing:.02em; flex:0 0 auto; }
  .tc2 .colhead.win{ background:var(--navy); } .tc2 .colhead.set{ background:var(--red); }
  .tc2 .colhead small{ display:block; font-weight:600; font-size:6.9pt; opacity:.9; margin-top:1px; }
  .tc2 .stack{ flex:1 1 auto; display:flex; flex-direction:column; gap:7px; padding-top:6px; min-height:0; }
  .card{ flex:1 1 0; position:relative; border:1.5px solid var(--rule); border-radius:6px; overflow:hidden;
       background-image:repeating-linear-gradient(to bottom, transparent 0 22px, var(--wl) 22px 23px);
       background-position:0 33px; padding:4px 9px 0; }
  .card.win{ background-color:var(--navy-tint); } .card.set{ background-color:#fbeeee; }
  .card .nm{ font-family:Georgia,serif; font-weight:700; font-size:8.9pt; color:var(--navy); line-height:1.05; }
  .card.set .nm{ color:#7c2a24; }
  .card .rl{ font-size:7.4pt; font-style:italic; color:#9aa4b4; line-height:1.22; margin-top:1px; }
  .synthbox{ flex:0 0 auto; margin-top:8px; display:flex; flex-direction:column; }
  .synthbox .well{ min-height:50px; position:relative; }
  .synthbox .fh{ position:absolute; top:6px; left:11px; right:11px; font-size:7.9pt; font-style:italic;
             color:#9aa6bd; line-height:1.34; }
  .tnbox{ flex:0 0 auto; margin-top:7px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.5pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""

def _card(kind, nm, rl):
    return (f'<div class="card {kind}"><div class="nm">{nm}</div>'
            f'<div class="rl">{rl}</div></div>')

_wins = [
    ("Affordable Care Act", "&ldquo;Obamacare&rdquo; extended health insurance to millions of uninsured Americans"),
    ("Economic Recovery", "the Recovery Act helped end the Great Recession; unemployment fell 10% &rarr; 4.7%"),
    ("Foreign Policy Wins", "the Paris Climate accord, the Iran nuclear deal, a Cuba opening, bin Laden killed"),
    ("Social Progress", "advanced marriage equality; created DACA for young immigrants"),
]
_sets = [
    ("Congressional Gridlock", "after 2010, GOP opposition brought shutdowns, debt&#8209;ceiling fights &amp; a blocked Court seat"),
    ("Foreign Challenges", "Syria&rsquo;s civil war, the rise of ISIS, Russian moves in Ukraine, Benghazi"),
    ("Deepening Division", "persistent racial tensions and a sharply polarized political climate"),
]

_wins_html = "\n          ".join(_card("win", n, r) for n, r in _wins)
_sets_html = "\n          ".join(_card("set", n, r) for n, r in _sets)

BODY = f"""
    <div class="prompt">On each card, write the details of that achievement or setback &mdash; the faint notes are starters. Then answer the band below: what did the Obama years reveal about the <b>power</b> and the <b>limits</b> of the presidency?</div>
    <div class="canvas">
      <div class="tc2">
        <div class="col">
          <div class="colhead win">ACHIEVEMENTS<small>what the administration accomplished</small></div>
          <div class="stack">
            {_wins_html}
          </div>
        </div>
        <div class="col">
          <div class="colhead set">SETBACKS<small>what limited or challenged it</small></div>
          <div class="stack">
            {_sets_html}
          </div>
        </div>
      </div>
      <div class="synthbox">
        <div class="band navy sm">What did these years show about the <b>power</b> and the <b>limits</b> of the presidency?</div>
        <div class="well cream lines">
          <span class="fh">A president can drive big change (healthcare, recovery) &mdash; but a divided Congress and a polarized nation can stall even a determined agenda</span>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Tennessee sat at the center of these debates: Senators <b>Lamar Alexander</b>
        and <b>Bob Corker</b> played significant roles in Senate battles over healthcare, trade, and foreign policy during
        the Obama years.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="32_us95_tchart",
    title="The Obama Years: Achievements &amp; Setbacks",
    kicker="Unit 10 &middot; US.95 &middot; Best&#8209;Fit Organizer",
    chips=[("T&#8209;Chart &middot; Two Sides", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2&#8211;3 &middot; Evaluate", "skill")],
    why=("A two&#8209;column chart weighs accomplishments against setbacks, so students judge the presidency on the full "
         "record &mdash; not one headline. "
         "<span class='cite'>Weighing evidence on both sides builds SSP.04 (evaluate).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Fill one achievement and one setback together first, using the faint notes.",
        extend="Choose the achievement and the setback you think mattered most, and defend both picks.",
        show="Students may <b>write</b> the cards, <b>say</b> a side aloud, or <b>debate</b> the record in pairs."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 10 &middot; US.95 (labeled)",
)]
