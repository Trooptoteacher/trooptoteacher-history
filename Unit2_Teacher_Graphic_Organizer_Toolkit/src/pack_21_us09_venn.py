# -*- coding: utf-8 -*-
"""Unit 2 labeled -- US.09 Booker T. Washington vs. W.E.B. Du Bois (Venn).
Topic identities live in a LEGEND ROW ABOVE the circles (HTML, clearly outside).
Region labels + in-lobe hints are <text> INSIDE the SVG (viewBox coords) so they
always track the circles and read as faded watermarks students write over.
Content approved for US.09 (competing strategies for African American advancement).
"""

CSS = r"""
  .vlegend{ flex:0 0 auto; display:flex; justify-content:space-between; align-items:flex-end; gap:16px; padding:0 2%; margin-bottom:3px; }
  .vlegend .oh{ display:flex; align-items:center; gap:8px; flex:1 1 0; min-width:0; }
  .vlegend .oh.b{ justify-content:flex-end; }
  .vlegend .dot{ width:14px; height:14px; border-radius:50%; flex:0 0 auto; }
  .vlegend .a .dot{ background:var(--navy); }
  .vlegend .b .dot{ background:var(--red); }
  .vlegend .nm{ font-weight:800; font-size:12.5pt; white-space:nowrap; }
  .vlegend .a .nm{ color:var(--navy); } .vlegend .b .nm{ color:var(--red); }
  .vlegend .wl{ flex:1 1 auto; min-width:70px; height:0; border-bottom:1.6px dotted #B9C2D0; margin-bottom:4px; }
  .venn-wrap{ flex:1 1 auto; position:relative; min-height:0; }
  .venn-wrap svg{ width:100%; height:100%; display:block; }
  .tnbox{ flex:0 0 auto; margin-top:6px; background:var(--gold-tint); border:1.6px solid var(--gold); border-left:6px solid var(--gold);
          border-radius:0 6px 6px 0; padding:7px 12px; display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.8pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""

BODY = r"""
    <div class="prompt">Compare their strategies for African American advancement &mdash; <b>background, education,</b> and <b>rights</b>. Write what set each apart in its circle, and the goal they <b>shared</b> in the center.</div>
    <div class="vlegend">
      <span class="oh a"><span class="dot"></span><span class="nm">Booker&nbsp;T.&nbsp;Washington</span><span class="wl"></span></span>
      <span class="oh b"><span class="wl"></span><span class="nm">W.E.B.&nbsp;Du&nbsp;Bois</span><span class="dot"></span></span>
    </div>
    <div class="canvas">
      <div class="venn-wrap">
        <svg viewBox="0 0 900 560" preserveAspectRatio="xMidYMid meet" font-family="Helvetica Neue, Arial, sans-serif">
          <circle cx="330" cy="285" r="245" fill="#EEF1F7" stroke="#1B2A4A" stroke-width="3.5"/>
          <circle cx="570" cy="285" r="245" fill="#FBEEEF" stroke="#B22234" stroke-width="3.5"/>
          <path d="M 450,72.5 A 245,245 0 0,1 450,497.5 A 245,245 0 0,1 450,72.5 Z" fill="#FAF3E2" stroke="#C89B3C" stroke-width="2.5"/>
          <!-- region captions: faded, minimized watermarks (inside the svg) -->
          <g text-anchor="middle" font-weight="800" font-size="12.5" fill="#9aa2b2" letter-spacing="0.5">
            <text x="250" y="135">ONLY WASHINGTON</text>
            <text x="650" y="135" fill="#caa8ad">ONLY DU BOIS</text>
            <text x="450" y="150" fill="#c1a860">BOTH</text>
          </g>
          <!-- faded hint prompts, safely inside each lobe -->
          <g text-anchor="middle" font-style="italic" font-weight="600" font-size="12.5" fill="#9aa2b2">
            <text x="250" y="228">Tuskegee</text>
            <text x="250" y="248">vocational skills</text>
            <text x="250" y="268">Atlanta Compromise</text>
          </g>
          <g text-anchor="middle" font-style="italic" font-weight="600" font-size="12.5" fill="#caa8ad">
            <text x="650" y="228">Talented Tenth</text>
            <text x="650" y="248">NAACP</text>
            <text x="650" y="268">immediate rights</text>
          </g>
          <g text-anchor="middle" font-style="italic" font-weight="600" font-size="11.5" fill="#c1a860">
            <text x="450" y="238">goal: advance</text>
            <text x="450" y="256">African Americans</text>
          </g>
          <!-- writing guides -->
          <g stroke="#B9C2D0" stroke-width="1.2" stroke-dasharray="2 5">
            <line x1="170" y1="315" x2="320" y2="315"/><line x1="160" y1="353" x2="320" y2="353"/><line x1="165" y1="391" x2="320" y2="391"/><line x1="185" y1="429" x2="320" y2="429"/></g>
          <g stroke="#D8B3B7" stroke-width="1.2" stroke-dasharray="2 5">
            <line x1="580" y1="315" x2="730" y2="315"/><line x1="580" y1="353" x2="740" y2="353"/><line x1="580" y1="391" x2="735" y2="391"/><line x1="580" y1="429" x2="715" y2="429"/></g>
          <g stroke="#E0CB94" stroke-width="1.2" stroke-dasharray="2 5">
            <line x1="405" y1="300" x2="495" y2="300"/><line x1="402" y1="338" x2="498" y2="338"/><line x1="405" y1="376" x2="495" y2="376"/></g>
        </svg>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> <b>Fisk University</b> in Nashville was central to this debate &mdash;
        <b>W.E.B. Du Bois</b> attended Fisk before he became a national voice for immediate rights.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="21_us09_venn",
    title="Washington vs. Du Bois",
    kicker="Unit 2 &middot; US.09 &middot; Best-Fit Organizer",
    chips=[("Venn &middot; Compare Two", "navy"), ("DOK 2&ndash;3 &middot; Comparison", "skill")],
    tn=True,
    why=("The era&rsquo;s defining debate over how to advance African Americans. The overlap shows a "
         "<b>shared goal</b>, which sharpens the real difference in <b>strategy</b> &mdash; present both figures "
         "evenly and let students weigh the approaches. "
         "<span class='cite'>Identifying similarities &amp; differences is Marzano&rsquo;s highest-yield strategy.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Give a labeled word bank (Tuskegee, vocational, Atlanta Compromise, Talented Tenth, NAACP, Fisk, immediate rights) to sort into the regions.",
        extend="Use the BOTH region to argue: if they shared the same goal, which strategy fit the moment &mdash; and what did each risk?",
        show="Students may <b>write</b>, <b>say</b> the contrast, <b>draw</b> a portrait pair, or <b>build</b> the Venn with sortable cards."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 2 &middot; US.09 (labeled)",
)]
