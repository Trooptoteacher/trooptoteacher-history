# -*- coding: utf-8 -*-
"""Blank reproducible: Claim -> Evidence -> Reasoning, linked by arrows."""

CSS = r"""
  .cer{ flex:1 1 auto; display:flex; flex-direction:column; min-height:0; }
  .cer-claim{ flex:0 0 auto; display:flex; flex-direction:column; }
  .cer-claim .well{ flex:0 0 92px; }
  .cer-ev{ flex:1 1 auto; display:flex; flex-direction:column; min-height:0; }
  .cer-ev-h{ display:flex; align-items:center; }
  .cer-ev-row{ flex:1 1 auto; display:flex; gap:12px; min-height:0; }
  .cer-ev-row .col{ flex:1 1 0; gap:0; }
  .cer-ev-row .well{ flex:1 1 auto; }
  .cer-num{ position:absolute; top:6px; left:10px; width:20px; height:20px; border-radius:50%;
    background:var(--red); color:#fff; font-size:9pt; font-weight:800; display:flex; align-items:center; justify-content:center; }
  .cer-reason{ flex:0 0 auto; display:flex; flex-direction:column; }
  .cer-reason .well{ flex:0 0 130px; }
  .cer-arr{ display:flex; flex-direction:column; align-items:center; flex:0 0 auto; margin:4px 0 2px; }
  .cer-arr .arr-lbl{ margin-bottom:2px; }
  .band.wfull{ border-radius:6px 6px 0 0; }
"""

BODY = r"""
    <div class="prompt">State your <b>claim</b>, back it with <b>evidence</b>, then explain your <b>reasoning</b> &mdash; how the evidence proves the claim.</div>
    <div class="canvas">
      <div class="cer">

        <div class="cer-claim">
          <div class="band navy wfull">CLAIM &mdash; my answer to the question</div>
          <div class="well lines" style="border-radius:0 0 6px 6px;"></div>
        </div>

        <div class="cer-arr"><div class="arr-lbl">Backed by</div><div class="arr-d"></div></div>

        <div class="cer-ev">
          <div class="band red wfull">EVIDENCE &mdash; facts, quotes &amp; details that prove it</div>
          <div class="cer-ev-row" style="border:1.6px solid var(--red); border-top:none; border-radius:0 0 6px 6px; padding:10px; background:var(--red-tint);">
            <div class="col"><div class="well lines top"><span class="cer-num">1</span></div></div>
            <div class="col"><div class="well lines top"><span class="cer-num">2</span></div></div>
            <div class="col"><div class="well lines top"><span class="cer-num">3</span></div></div>
          </div>
        </div>

        <div class="cer-arr"><div class="arr-lbl">Which proves</div><div class="arr-d"></div></div>

        <div class="cer-reason">
          <div class="band gold wfull">REASONING &mdash; this evidence supports my claim because&hellip;</div>
          <div class="well lines cream" style="border-radius:0 0 6px 6px;"></div>
        </div>

      </div>
    </div>
"""

ORGANIZERS = [dict(
    slug="14_cer_blank",
    title="Claim &middot; Evidence &middot; Reasoning",
    kicker="Reusable Organizer &middot; Any Unit &middot; Any Subject",
    chips=[("Make a claim", "navy"), ("DOK 3 &middot; Argument", "skill")],
    why=("Use to build an <b>evidence&#8209;based argument</b> &mdash; a defensible claim, the evidence that "
         "supports it, and the reasoning that ties them together. "
         "<span class='cite'>Constructing arguments from evidence is a core disciplinary practice "
         "(TN Social Studies Practices).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Give a claim frame: &ldquo;___ because ___.&rdquo; and a reasoning starter: &ldquo;This shows ___ because ___.&rdquo; Fill just one evidence box first.",
        extend="Add a <b>counterclaim</b> and one sentence explaining why your evidence still wins.",
        show="Students may <b>write</b>, <b>say</b> (record) the argument, or <b>build</b> it from evidence cards before writing."),
    role="Teacher Graphic Organizer Toolkit &middot; Blank Reproducible",
)]
