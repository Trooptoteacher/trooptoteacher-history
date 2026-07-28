# -*- coding: utf-8 -*-
"""Unit 10 labeled -- US.88 The Carter Administration (problem -> solution).
Three columns, one per challenge Carter faced (stagflation, the energy crisis,
diplomacy & crisis). Each column stacks PROBLEM -> CARTER'S RESPONSE -> RESULT,
with faded hints. Balanced framing -- notes both Camp David's success and the Iran
hostage crisis. HAS a Tennessee Connection. Content approved for US.88.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .ps3{ flex:1 1 auto; display:grid; grid-template-columns:repeat(3,1fr); gap:11px; min-height:0; }
  .ps-col{ display:flex; flex-direction:column; min-height:0; }
  .ps-col .chead{ flex:0 0 auto; text-align:center; font-family:Georgia,serif; font-weight:700;
       font-size:9.6pt; color:var(--navy); padding:2px 0 5px; line-height:1.05; }
  .cell{ position:relative; display:flex; flex-direction:column; min-height:0; }
  .cell .band{ flex:0 0 auto; font-size:7.7pt; padding:4px 7px; letter-spacing:.02em; }
  .cell .well{ flex:1 1 0; min-height:0; }
  .cell .fh{ position:absolute; left:8px; right:8px; font-size:7.2pt; font-style:italic;
       color:#9aa6bd; line-height:1.24; }
  .ps-prob{ flex:1.15 1 0; } .ps-resp{ flex:1.25 1 0; } .ps-res{ flex:1.1 1 0; }
  .arr-mid{ flex:0 0 15px; display:flex; align-items:center; justify-content:center; }
  .arr-mid .arr-d{ margin:1px 0; }
  .tnbox{ flex:0 0 auto; margin-top:8px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.5pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""

# (title, problem hint, response hint, result hint)
_cols = [
    ("Stagflation",
     "high inflation (13.5%) <b>and</b> unemployment at once; interest rates near 20%",
     "voluntary wage&#8209;price guidelines; the Federal Reserve tightens money",
     "the measures fell short &mdash; the economy stayed weak"),
    ("The Energy Crisis",
     "oil shortages, long gas lines &amp; soaring heating costs",
     "created the <b>Department of Energy</b>; urged conservation &amp; less foreign oil",
     "gas lines frustrated the public and damaged him politically"),
    ("Diplomacy &amp; Crisis",
     "Cold&#8209;War tensions, the Panama Canal question &amp; a hostile Iran",
     "the <b>Camp David Accords</b> (Egypt&ndash;Israel peace); Panama Canal treaties",
     "Camp David was a triumph &mdash; but the <b>Iran hostage crisis</b> (444 days) doomed his term"),
]

def _col(title, prob, resp, res):
    return f"""
        <div class="ps-col">
          <div class="chead">{title}</div>
          <div class="cell ps-prob"><div class="band red sm">PROBLEM</div>
            <div class="well tint-red lines"><span class="fh" style="top:5px;">{prob}</span></div></div>
          <div class="arr-mid"><div class="arr-d"></div></div>
          <div class="cell ps-resp"><div class="band navy sm">CARTER&rsquo;S RESPONSE</div>
            <div class="well tint-navy lines"><span class="fh" style="top:5px;">{resp}</span></div></div>
          <div class="arr-mid"><div class="arr-d"></div></div>
          <div class="cell ps-res"><div class="band gold sm">RESULT</div>
            <div class="well tint-gold lines"><span class="fh" style="top:5px;">{res}</span></div></div>
        </div>"""

BODY = f"""
    <div class="prompt">Carter met three big challenges. In each column, read the faint hints and write the <b>problem</b>, his <b>response</b>, and the <b>result</b>. Follow the arrows down: <b>problem &rarr; response &rarr; result</b>.</div>
    <div class="canvas">
      <div class="ps3">
        {_col(*_cols[0])}
        {_col(*_cols[1])}
        {_col(*_cols[2])}
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Tennessee Senator <b>Howard Baker</b> was a key Republican voice as
        Senate Minority Leader during these years. And Tennessee banker <b>Jake Butcher</b> helped bring the
        <b>1982 World&rsquo;s Fair to Knoxville</b> &mdash; one of the last major World&rsquo;s Fairs held in the United States.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="25_us88_problemsolution",
    title="President Carter&rsquo;s Toughest Tests",
    kicker="Unit 10 &middot; US.88 &middot; Best&#8209;Fit Organizer",
    chips=[("Problem &rarr; Solution", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 3 &middot; Evaluate", "skill")],
    why=("Laying each challenge out as <b>problem &rarr; response &rarr; result</b> lets students judge Carter fairly &mdash; "
         "crediting Camp David while weighing the crises that sank his presidency. "
         "<span class='cite'>Weighing responses against outcomes builds SSP.04 (evaluate).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Fill the &ldquo;problem&rdquo; row across all three columns first, then work down one column at a time.",
        extend="Which problem was most out of Carter&rsquo;s control? Use the results row to defend your answer.",
        show="Students may <b>write</b> the cells, <b>say</b> a column aloud, or <b>rank</b> the three challenges by difficulty."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 10 &middot; US.88 (labeled)",
)]
