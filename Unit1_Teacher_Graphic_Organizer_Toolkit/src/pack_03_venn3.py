# -*- coding: utf-8 -*-
"""Blank reproducible: 3-circle Venn (compare three)."""

CSS = r"""
  .venn3-wrap{ flex:1 1 auto; position:relative; min-height:0; }
  .venn3-wrap svg{ width:100%; height:100%; display:block; }
"""

BODY = r"""
    <div class="prompt">Write what is <b>unique</b> to each topic in its outer lobe. Where circles overlap, write what those topics <b>share</b>.</div>
    <div class="canvas">
      <div class="venn3-wrap">
        <svg viewBox="0 0 900 700" preserveAspectRatio="xMidYMid meet"
             font-family="Helvetica Neue, Arial, sans-serif">
          <!-- three mutually overlapping circles (equilateral centers) -->
          <circle cx="332" cy="250" r="215" fill="#EEF1F7" fill-opacity="0.55" stroke="#1B2A4A" stroke-width="3.5"/>
          <circle cx="568" cy="250" r="215" fill="#FBEEEF" fill-opacity="0.55" stroke="#B22234" stroke-width="3.5"/>
          <circle cx="450" cy="454" r="215" fill="#FAF3E2" fill-opacity="0.55" stroke="#C89B3C" stroke-width="3.5"/>

          <!-- faint dashed writing guides in each single lobe -->
          <g stroke="#B9C2D0" stroke-width="1.3" stroke-dasharray="2 5">
            <line x1="150" y1="300" x2="300" y2="300"/><line x1="140" y1="332" x2="300" y2="332"/><line x1="155" y1="364" x2="300" y2="364"/></g>
          <g stroke="#D8B3B7" stroke-width="1.3" stroke-dasharray="2 5">
            <line x1="600" y1="300" x2="750" y2="300"/><line x1="600" y1="332" x2="760" y2="332"/><line x1="600" y1="364" x2="745" y2="364"/></g>
          <g stroke="#E0CB94" stroke-width="1.3" stroke-dasharray="2 5">
            <line x1="375" y1="540" x2="525" y2="540"/><line x1="365" y1="572" x2="535" y2="572"/><line x1="380" y1="604" x2="520" y2="604"/></g>

          <!-- topic identity labels + write lines -->
          <g font-weight="800" font-size="23">
            <text x="96" y="152" fill="#1B2A4A">Topic A:</text>
            <line x1="200" y1="146" x2="322" y2="146" stroke="#1B2A4A" stroke-width="2.2"/>
            <text x="604" y="152" fill="#B22234">Topic B:</text>
            <line x1="708" y1="146" x2="828" y2="146" stroke="#B22234" stroke-width="2.2"/>
            <text x="330" y="662" fill="#8a6a1e">Topic C:</text>
            <line x1="437" y1="656" x2="560" y2="656" stroke="#C89B3C" stroke-width="2.2"/>
          </g>

          <!-- region captions -->
          <g font-weight="800" letter-spacing="0.5" text-anchor="middle">
            <text x="222" y="248" font-size="20" fill="#1B2A4A">ONLY A</text>
            <text x="678" y="248" font-size="20" fill="#B22234">ONLY B</text>
            <text x="450" y="596" font-size="20" fill="#8a6a1e">ONLY C</text>
            <text x="450" y="212" font-size="17" fill="#5A6579">A &amp; B</text>
            <text x="318" y="404" font-size="17" fill="#5A6579">A &amp; C</text>
            <text x="582" y="404" font-size="17" fill="#5A6579">B &amp; C</text>
            <text x="450" y="330" font-size="20" fill="#1B2A4A">ALL&nbsp;3</text>
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
