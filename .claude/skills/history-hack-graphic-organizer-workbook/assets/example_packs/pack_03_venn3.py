# -*- coding: utf-8 -*-
"""Blank reproducible: 3-circle Venn (compare three)."""

CSS = r"""
  .v3legend{ flex:0 0 auto; display:flex; justify-content:center; gap:15px; flex-wrap:nowrap; margin-bottom:4px; }
  .v3legend .lg{ display:flex; align-items:center; gap:6px; font-weight:800; font-size:11pt; white-space:nowrap; }
  .v3legend .sw{ width:14px; height:14px; border-radius:50%; border:2.5px solid; flex:0 0 auto; }
  .v3legend .wf{ display:inline-block; border-bottom:2px solid; width:112px; height:19px; }
  .v3legend .a{ color:var(--navy); } .v3legend .a .sw{ background:var(--navy-tint); border-color:var(--navy); } .v3legend .a .wf{ border-color:var(--navy); }
  .v3legend .b{ color:var(--red); } .v3legend .b .sw{ background:var(--red-tint); border-color:var(--red); } .v3legend .b .wf{ border-color:var(--red); }
  .v3legend .c{ color:#8a6a1e; } .v3legend .c .sw{ background:var(--gold-tint); border-color:var(--gold); } .v3legend .c .wf{ border-color:var(--gold); }
  .venn3-wrap{ flex:1 1 auto; position:relative; min-height:0; }
  .venn3-wrap svg{ width:100%; height:100%; display:block; }
"""

BODY = r"""
    <div class="prompt">Name each topic in the key, then fill the circles: <b>unique</b> traits in the single lobes, <b>shared</b> traits where they overlap.</div>
    <div class="v3legend">
      <span class="lg a"><span class="sw"></span>Topic&nbsp;A:&nbsp;<span class="wf"></span></span>
      <span class="lg b"><span class="sw"></span>Topic&nbsp;B:&nbsp;<span class="wf"></span></span>
      <span class="lg c"><span class="sw"></span>Topic&nbsp;C:&nbsp;<span class="wf"></span></span>
    </div>
    <div class="canvas">
      <div class="venn3-wrap">
        <svg viewBox="0 0 900 660" preserveAspectRatio="xMidYMid meet"
             font-family="Helvetica Neue, Arial, sans-serif">
          <!-- three mutually overlapping circles (equilateral centers) -->
          <circle cx="332" cy="228" r="212" fill="#EEF1F7" fill-opacity="0.5" stroke="#1F3A5F" stroke-width="3.5"/>
          <circle cx="568" cy="228" r="212" fill="#FBEEEF" fill-opacity="0.5" stroke="#B22234" stroke-width="3.5"/>
          <circle cx="450" cy="428" r="212" fill="#FAF3E2" fill-opacity="0.5" stroke="#C9A227" stroke-width="3.5"/>

          <!-- faint dashed writing guides in each single lobe -->
          <g stroke="#B9C2D0" stroke-width="1.3" stroke-dasharray="2 5">
            <line x1="150" y1="248" x2="300" y2="248"/><line x1="140" y1="280" x2="300" y2="280"/><line x1="155" y1="312" x2="300" y2="312"/></g>
          <g stroke="#D8B3B7" stroke-width="1.3" stroke-dasharray="2 5">
            <line x1="600" y1="248" x2="750" y2="248"/><line x1="600" y1="280" x2="760" y2="280"/><line x1="600" y1="312" x2="745" y2="312"/></g>
          <g stroke="#E0CB94" stroke-width="1.3" stroke-dasharray="2 5">
            <line x1="375" y1="512" x2="525" y2="512"/><line x1="365" y1="544" x2="535" y2="544"/><line x1="380" y1="576" x2="520" y2="576"/></g>

          <!-- region captions: minimized + faded so students have room to write -->
          <g font-weight="700" letter-spacing="0.5" text-anchor="middle">
            <text x="216" y="222" font-size="13" fill="#9aa2b2">ONLY A</text>
            <text x="684" y="222" font-size="13" fill="#c2a3a8">ONLY B</text>
            <text x="450" y="560" font-size="13" fill="#cbb583">ONLY C</text>
            <text x="450" y="188" font-size="11" fill="#b6bcc8">A &amp; B</text>
            <text x="322" y="378" font-size="11" fill="#b6bcc8">A &amp; C</text>
            <text x="578" y="378" font-size="11" fill="#b6bcc8">B &amp; C</text>
            <text x="450" y="306" font-size="12" fill="#aab0be">ALL&nbsp;3</text>
          </g>
        </svg>
      </div>
    </div>
"""

ORGANIZERS = [dict(
    slug="03_venn3_blank",
    title="Venn Diagram &mdash; Compare Three",
    kicker="Reusable Organizer &middot; Any Unit &middot; Any Subject",
    chips=[("Compare 3", "navy"), ("DOK 2&ndash;3 &middot; Comparison", "skill")],
    why=("Use when a task asks students to <b>compare three</b> things at once &mdash; the overlaps expose what is "
         "shared by two, what is shared by all three, and what stays unique. "
         "<span class='cite'>Identifying similarities &amp; differences is the highest-yield strategy for "
         "learning gains (Marzano).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Give a word bank and start with the ALL&nbsp;3 center: &ldquo;All three share ___.&rdquo; Let pairs fill one lobe at a time.",
        extend="Argue which topic is the &ldquo;odd one out&rdquo; and defend it with one trait from its unique lobe.",
        show="Students may <b>write</b>, <b>say</b> (record), <b>draw</b> icons, or <b>build</b> the circles with sticky notes."),
    role="Teacher Graphic Organizer Toolkit &middot; Blank Reproducible",
)]
