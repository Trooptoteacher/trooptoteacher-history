# -*- coding: utf-8 -*-
"""Blank reproducible: 2-circle Venn (the approved house-style reference)."""

CSS = r"""
  .venn-wrap{ flex:1 1 auto; position:relative; min-height:0; }
  .venn-wrap svg{ width:100%; height:100%; display:block; }
  .topicbar{ position:absolute; top:-2px; display:flex; align-items:center; gap:6px; font-weight:800; font-size:12pt; }
  .writefield{ background:var(--paper); border-bottom:2px solid; min-width:150px; height:20px; display:inline-block; }
  .vlbl{ position:absolute; text-align:center; font-size:11.5pt; font-weight:800; letter-spacing:.03em; }
"""

BODY = r"""
    <div class="prompt">In each circle, write what is <b>unique</b> to that topic. In the middle, write what they <b>share</b>.</div>
    <div class="canvas">
      <div class="venn-wrap">
        <svg viewBox="0 0 900 560" preserveAspectRatio="xMidYMid meet">
          <circle cx="330" cy="285" r="245" fill="#EEF1F7" stroke="#1B2A4A" stroke-width="3.5"/>
          <circle cx="570" cy="285" r="245" fill="#FBEEEF" stroke="#B22234" stroke-width="3.5"/>
          <path d="M 450,72.5 A 245,245 0 0,1 450,497.5 A 245,245 0 0,1 450,72.5 Z"
                fill="#FAF3E2" stroke="#C89B3C" stroke-width="2.5"/>
          <g stroke="#B9C2D0" stroke-width="1.2" stroke-dasharray="2 5">
            <line x1="150" y1="235" x2="330" y2="235"/><line x1="140" y1="285" x2="330" y2="285"/><line x1="150" y1="335" x2="330" y2="335"/></g>
          <g stroke="#D8B3B7" stroke-width="1.2" stroke-dasharray="2 5">
            <line x1="570" y1="235" x2="750" y2="235"/><line x1="570" y1="285" x2="760" y2="285"/><line x1="570" y1="335" x2="750" y2="335"/></g>
          <g stroke="#E0CB94" stroke-width="1.2" stroke-dasharray="2 5">
            <line x1="410" y1="255" x2="490" y2="255"/><line x1="405" y1="285" x2="495" y2="285"/><line x1="410" y1="315" x2="490" y2="315"/></g>
        </svg>
        <div class="topicbar" style="left:5%; color:var(--navy);">Topic&nbsp;A: <span class="writefield" style="border-color:var(--navy);"></span></div>
        <div class="topicbar" style="right:5%; color:var(--red);">Topic&nbsp;B: <span class="writefield" style="border-color:var(--red);"></span></div>
        <div class="vlbl" style="top:33%; left:17%; color:var(--navy);">ONLY&nbsp;A</div>
        <div class="vlbl" style="top:33%; right:17%; color:var(--red);">ONLY&nbsp;B</div>
        <div class="vlbl" style="top:30%; left:44.5%; color:#8a6a1e;">BOTH</div>
      </div>
    </div>
"""

ORGANIZERS = [dict(
    slug="02_venn2_blank",
    title="Venn Diagram &mdash; Compare Two",
    kicker="Reusable Organizer &middot; Any Unit &middot; Any Subject",
    chips=[("Compare 2 Things", "navy"), ("DOK 2 &middot; Comparison", "skill")],
    why=("Use when a task asks students to <b>compare two</b> things &mdash; the overlap makes shared "
         "traits visible and forces precise differences. "
         "<span class='cite'>Identifying similarities &amp; differences is the highest-yield strategy "
         "for learning gains (Marzano).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Give a word bank and a sentence starter: &ldquo;Both ___ and ___ are ___.&rdquo; Let pairs fill the BOTH region first.",
        extend="Rank the differences: which one matters most, and why? Defend it in one sentence of evidence.",
        show="Students may <b>write</b>, <b>say</b> (record), <b>draw</b> icons, or <b>build</b> the circles with sticky notes."),
    role="Teacher Graphic Organizer Toolkit &middot; Blank Reproducible",
)]
