# -*- coding: utf-8 -*-
"""Blank reproducible: Problem -> Solution (define, weigh options, decide)."""

CSS = r"""
  .ps-box{ display:flex; flex-direction:column; min-height:0; }
  .ps-box>.band{ flex:0 0 auto; }
  .ps-box>.well{ flex:1 1 0; }
  .ps-sols{ display:grid; grid-template-columns:repeat(3,1fr); gap:9px; flex:1.9 1 0; min-height:0; }
  .ps-sol{ display:flex; flex-direction:column; min-height:0; }
  .ps-sol .band.navy{ flex:0 0 auto; }
  .ps-sol .sol-well{ flex:1.3 1 0; min-height:0; border-radius:0; }
  .ps-sol .band.tradelbl{ flex:0 0 auto; font-size:8pt; background:var(--gold); color:var(--navy);
                          border-radius:0; letter-spacing:.02em; }
  .ps-sol .trade-well{ flex:1 1 0; min-height:0; }
  .arr-lbl{ margin:1px 0 3px; }
"""

BODY = r"""
    <div class="prompt">State the <b>problem</b>, map <b>2&#8211;3 possible solutions</b> with their likely results, then choose the best one and justify it. Follow the arrows: <b>problem &rarr; options &rarr; decision</b>.</div>
    <div class="canvas">
      <div class="ps-box" style="flex:1 1 0; min-height:0;">
        <div class="band red sm">PROBLEM &mdash; what is wrong, and for whom?</div>
        <div class="well tint-red lines"></div>
      </div>
      <div class="arr-d"></div>
      <div class="arr-lbl">Weigh the options</div>
      <div class="ps-sols">
        <div class="ps-sol">
          <div class="band navy sm">Possible Solution&nbsp;1</div>
          <div class="well sol-well lines"></div>
          <div class="band sm tradelbl">Likely result &middot; trade&#8209;off</div>
          <div class="well trade-well tint-gold lines"></div>
        </div>
        <div class="ps-sol">
          <div class="band navy sm">Possible Solution&nbsp;2</div>
          <div class="well sol-well lines"></div>
          <div class="band sm tradelbl">Likely result &middot; trade&#8209;off</div>
          <div class="well trade-well tint-gold lines"></div>
        </div>
        <div class="ps-sol">
          <div class="band navy sm">Possible Solution&nbsp;3</div>
          <div class="well sol-well lines"></div>
          <div class="band sm tradelbl">Likely result &middot; trade&#8209;off</div>
          <div class="well trade-well tint-gold lines"></div>
        </div>
      </div>
      <div class="arr-d"></div>
      <div class="arr-lbl">Decide</div>
      <div class="ps-box" style="flex:1 1 0; min-height:0;">
        <div class="band gold sm">Best solution &plus; justification &mdash; I chose ___ because&hellip;</div>
        <div class="well cream lines"></div>
      </div>
    </div>
"""

ORGANIZERS = [dict(
    slug="12_problemsolution_blank",
    title="Problem &rarr; Solution",
    kicker="Reusable Organizer &middot; Any Unit &middot; Any Subject",
    chips=[("Weigh options", "navy"), ("DOK 3 &middot; Decision", "skill")],
    why=("Use to define a <b>problem</b>, weigh two or three possible solutions against their likely "
         "results, and justify the best choice with evidence. "
         "<span class='cite'>Generating &amp; testing possible solutions is a high&#8209;yield reasoning "
         "strategy (Marzano); it builds cause&#8209;effect thinking (TN SSP.05).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Provide the problem and one solution; students supply the rest. Offer a starter: &ldquo;If we ___, then ___ because ___.&rdquo;",
        extend="Add a second criterion (cost <i>and</i> fairness) and explain a trade&#8209;off you are willing to accept.",
        show="Students may <b>write</b>, <b>say</b> (record), <b>draw</b> the flow, or <b>build</b> the options with cards and vote."),
    role="Teacher Graphic Organizer Toolkit &middot; Blank Reproducible",
)]
