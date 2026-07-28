# -*- coding: utf-8 -*-
"""Blank reproducible: Compare / Contrast Matrix (options x criteria)."""

CSS = r"""
  .mx{ display:grid; grid-template-columns:1.15fr 1fr 1fr 1fr;
       grid-template-rows:auto 1fr 1fr 1fr 0.9fr; gap:8px;
       flex:1 1 auto; min-height:0; }
  .mxband{ border-radius:6px; display:flex; flex-direction:column; align-items:center;
           justify-content:center; text-align:center; line-height:1.15; }
  .mx .well{ min-height:0; }
  .mx-corner{ font-size:8.5pt; }
  .mx-crit{ background:var(--navy-tint); }
  .mx-span{ grid-column:1 / -1; display:flex; flex-direction:column; min-height:0; }
  .mx-span .band{ flex:0 0 auto; }
  .mx-span .well{ flex:1 1 0; }
  .cap{ position:absolute; top:5px; left:8px; font-size:7.6pt; font-weight:800;
        letter-spacing:.03em; text-transform:uppercase; color:var(--muted); }
"""

BODY = r"""
    <div class="prompt">Name each <b>option</b> across the top and each <b>criterion</b> down the side. Fill every box with what that option shows for that criterion. Then name the <b>pattern</b> you see.</div>
    <div class="canvas">
      <div class="mx">
        <div class="band navy mxband mx-corner">CRITERIA&nbsp;&darr;<br>OPTIONS&nbsp;&rarr;</div>
        <div class="band red mxband">Option&nbsp;A</div>
        <div class="band navy mxband">Option&nbsp;B</div>
        <div class="band gold mxband">Option&nbsp;C</div>

        <div class="well top mx-crit"><span class="cap">Criterion&nbsp;1</span></div>
        <div class="well top lines"></div>
        <div class="well top lines"></div>
        <div class="well top lines"></div>

        <div class="well top mx-crit"><span class="cap">Criterion&nbsp;2</span></div>
        <div class="well top lines"></div>
        <div class="well top lines"></div>
        <div class="well top lines"></div>

        <div class="well top mx-crit"><span class="cap">Criterion&nbsp;3</span></div>
        <div class="well top lines"></div>
        <div class="well top lines"></div>
        <div class="well top lines"></div>

        <div class="mx-span">
          <div class="band gold sm">Pattern &middot; conclusion &mdash; what the whole matrix tells you</div>
          <div class="well cream lines"></div>
        </div>
      </div>
    </div>
"""

ORGANIZERS = [dict(
    slug="05_matrix_blank",
    title="Compare &middot; Contrast Matrix",
    kicker="Reusable Organizer &middot; Any Unit &middot; Any Subject",
    chips=[("Compare 3+ on criteria", "navy"), ("DOK 2&#8211;3 &middot; Analysis", "skill")],
    why=("Use to compare <b>three or more</b> things across several named criteria at once, so patterns "
         "across the whole set become visible. "
         "<span class='cite'>Comparing on structured criteria &mdash; identifying similarities &amp; "
         "differences &mdash; is the highest&#8209;yield strategy for learning gains (Marzano).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Pre&#8209;name one or two criteria and a starter: &ldquo;On ___, Option A ___ while Option C ___.&rdquo; Complete one row as a class.",
        extend="In the conclusion, explain <i>why</i> the pattern holds &mdash; what causes options to line up or split the way they do?",
        show="Students may <b>write</b>, <b>say</b> (record), <b>draw</b> symbols in cells, or <b>build</b> the grid with cards."),
    role="Teacher Graphic Organizer Toolkit &middot; Blank Reproducible",
)]
