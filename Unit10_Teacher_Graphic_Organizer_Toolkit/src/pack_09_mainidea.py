# -*- coding: utf-8 -*-
"""Blank reproducible: Main Idea & Details (details support the main idea)."""

CSS = r"""
  .mi-box{ display:flex; flex-direction:column; min-height:0; }
  .mi-box .band{ flex:0 0 auto; }
  .mi-box .well{ flex:1 1 0; }
  .mi-arrows{ display:grid; grid-template-columns:repeat(4,1fr); flex:0 0 auto; margin:4px 0 2px; }
  .arr-u{ width:0; height:0; border-left:13px solid transparent; border-right:13px solid transparent;
          border-bottom:18px solid var(--navy); margin:0 auto; }
  .mi-details{ display:grid; grid-template-columns:repeat(4,1fr); gap:9px; flex:1.7 1 0; min-height:0; }
  .mi-supports{ font-size:8pt; font-weight:800; color:var(--navy); text-transform:uppercase;
                letter-spacing:.05em; text-align:center; flex:0 0 auto; margin-top:2px; }
"""

BODY = r"""
    <div class="prompt">Write the <b>main idea</b> at the top. In each box below, add a <b>detail or piece of evidence</b> that supports it &mdash; the arrows show every detail holding the main idea up. Then say it all in one sentence.</div>
    <div class="canvas">
      <div class="mi-box" style="flex:1.25 1 0; min-height:0;">
        <div class="band navy sm">MAIN&nbsp;IDEA</div>
        <div class="well lines"></div>
      </div>
      <div class="mi-supports">&uarr;&nbsp; these details support the main idea &nbsp;&uarr;</div>
      <div class="mi-arrows">
        <div class="arr-u"></div><div class="arr-u"></div><div class="arr-u"></div><div class="arr-u"></div>
      </div>
      <div class="mi-details">
        <div class="mi-box"><div class="band red sm">Detail&nbsp;1</div><div class="well tint-red lines"></div></div>
        <div class="mi-box"><div class="band navy sm">Detail&nbsp;2</div><div class="well tint-navy lines"></div></div>
        <div class="mi-box"><div class="band gold sm">Detail&nbsp;3</div><div class="well tint-gold lines"></div></div>
        <div class="mi-box"><div class="band navy sm">Detail&nbsp;4</div><div class="well tint-navy lines"></div></div>
      </div>
      <div class="mi-box" style="flex:0.8 1 0; min-height:0; margin-top:10px;">
        <div class="band gold sm">Summary &mdash; the whole thing in one sentence</div>
        <div class="well cream lines"></div>
      </div>
    </div>
"""

ORGANIZERS = [dict(
    slug="09_mainidea_blank",
    title="Main Idea &amp; Details",
    kicker="Reusable Organizer &middot; Any Unit &middot; Any Subject",
    chips=[("Summarize", "navy"), ("DOK 2 &middot; Main Idea", "skill")],
    why=("Use to pull the <b>central point</b> out of a text or lecture and anchor it to the details "
         "and evidence that support it. "
         "<span class='cite'>Summarizing &mdash; keeping the main idea and cutting the rest &mdash; is a "
         "high&#8209;yield comprehension strategy (Marzano).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Give a main&#8209;idea frame: &ldquo;This is mostly about ___ because ___.&rdquo; Fill one detail box together before students work.",
        extend="Rank the details from strongest to weakest support, or add a detail that would <i>weaken</i> the main idea.",
        show="Students may <b>write</b>, <b>say</b> (record), <b>draw</b> an icon per detail, or <b>build</b> it with labeled cards."),
    role="Teacher Graphic Organizer Toolkit &middot; Blank Reproducible",
)]
