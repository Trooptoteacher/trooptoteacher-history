# -*- coding: utf-8 -*-
"""Blank reproducible: T-Chart (compare two things head-to-head)."""

CSS = r"""
  .tc-box{ display:flex; flex-direction:column; min-height:0; }
  .tc-box .band{ flex:0 0 auto; }
  .tc-box .well{ flex:1 1 0; }
"""

BODY = r"""
    <div class="prompt">Write your two topics in the label bands below. In each column, list what is true of <b>that topic</b> on points <b>you</b> choose &mdash; keep the lines across from each other about the <b>same point</b>. Then name the single biggest difference.</div>
    <div class="canvas">
      <div class="row" style="flex:3 1 0; min-height:0;">
        <div class="tc-box fill">
          <div class="band navy sm">Topic&nbsp;A</div>
          <div class="well lines"></div>
        </div>
        <div class="tc-box fill">
          <div class="band red sm">Topic&nbsp;B</div>
          <div class="well lines"></div>
        </div>
      </div>
      <div class="tc-box" style="flex:1.05 1 0; min-height:0; margin-top:10px;">
        <div class="band navy sm">Synthesis &mdash; the most important difference, and why it matters</div>
        <div class="well cream lines"></div>
      </div>
    </div>
"""

ORGANIZERS = [dict(
    slug="04_tchart_blank",
    title="T&#8209;Chart &mdash; Compare Two",
    kicker="Reusable Organizer &middot; Any Unit &middot; Any Subject",
    chips=[("Compare 2", "navy"), ("DOK 2 &middot; Comparison", "skill")],
    why=("Use to compare <b>two</b> things head&#8209;to&#8209;head on points you choose, lining up each "
         "trait side&#8209;by&#8209;side so real differences stand out. "
         "<span class='cite'>Identifying similarities &amp; differences is the highest&#8209;yield "
         "strategy for learning gains (Marzano).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Offer a point list (&ldquo;cost, speed, who it helps&hellip;&rdquo;) and a starter: &ldquo;On ___, Topic A ___, but Topic B ___.&rdquo; Fill one row together first.",
        extend="In the synthesis, rank the differences and defend which one matters most with one piece of evidence.",
        show="Students may <b>write</b>, <b>say</b> (record), <b>draw</b> icons, or <b>build</b> the two columns with sticky notes."),
    role="Teacher Graphic Organizer Toolkit &middot; Blank Reproducible",
)]
