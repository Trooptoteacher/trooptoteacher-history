# -*- coding: utf-8 -*-
"""Unit 1 labeled — US.07 'Old' vs. 'New' immigrants (Venn).
Region labels + hints live INSIDE the SVG (viewBox coords) so they always track
the circles regardless of how the SVG scales. Topic sourced from standards
inventory (US.07: Immigration - Old vs. New, Assimilation, Nativism).
"""

CSS = r"""
  .v7head{ flex:0 0 auto; display:flex; justify-content:space-between; align-items:flex-end; padding:0 3%; margin-bottom:2px; }
  .v7head .oh{ display:flex; flex-direction:column; }
  .v7head .oh.b{ align-items:flex-end; }
  .v7head .nm{ font-weight:800; font-size:12.5pt; }
  .v7head .yr{ font-size:8pt; font-weight:700; color:var(--muted); }
  .v7head .a .nm{ color:var(--navy); } .v7head .b .nm{ color:var(--red); }
  .venn-wrap{ flex:1 1 auto; position:relative; min-height:0; }
  .venn-wrap svg{ width:100%; height:100%; display:block; }
"""

BODY = r"""
    <div class="prompt">Two waves, one country. Write what set each wave apart &mdash; and what every newcomer <b>shared</b>.</div>
    <div class="v7head">
      <span class="oh a"><span class="nm">&ldquo;OLD&rdquo; Immigrants</span><span class="yr">before the 1880s</span></span>
      <span class="oh b"><span class="nm">&ldquo;NEW&rdquo; Immigrants</span><span class="yr">1880s&ndash;1920s</span></span>
    </div>
    <div class="canvas">
      <div class="venn-wrap">
        <svg viewBox="0 0 900 560" preserveAspectRatio="xMidYMid meet" font-family="Helvetica Neue, Arial, sans-serif">
          <circle cx="330" cy="285" r="245" fill="#EEF1F7" stroke="#1F3A5F" stroke-width="3.5"/>
          <circle cx="570" cy="285" r="245" fill="#FBEEEF" stroke="#B22234" stroke-width="3.5"/>
          <path d="M 450,71.4 A 245,245 0 0,1 450,498.6 A 245,245 0 0,1 450,71.4 Z" fill="#FAF3E2" stroke="#C9A227" stroke-width="2.5"/>
          <!-- writing guides -->
          <g stroke="#B9C2D0" stroke-width="1.2" stroke-dasharray="2 5">
            <line x1="150" y1="335" x2="300" y2="335"/><line x1="140" y1="373" x2="300" y2="373"/><line x1="150" y1="411" x2="300" y2="411"/></g>
          <g stroke="#D8B3B7" stroke-width="1.2" stroke-dasharray="2 5">
            <line x1="600" y1="335" x2="750" y2="335"/><line x1="600" y1="373" x2="760" y2="373"/><line x1="600" y1="411" x2="750" y2="411"/></g>
          <g stroke="#E0CB94" stroke-width="1.2" stroke-dasharray="2 5">
            <line x1="408" y1="360" x2="492" y2="360"/><line x1="404" y1="398" x2="496" y2="398"/></g>
          <!-- region labels (in-SVG => always inside the circles) -->
          <g text-anchor="middle" font-weight="800">
            <text x="212" y="250" font-size="19" fill="#1F3A5F">ONLY &ldquo;OLD&rdquo;</text>
            <text x="688" y="250" font-size="19" fill="#B22234">ONLY &ldquo;NEW&rdquo;</text>
            <text x="450" y="205" font-size="19" fill="#8a6a1e">BOTH</text>
          </g>
          <!-- faded hint prompts, safely inside each lobe -->
          <g text-anchor="middle" font-style="italic" font-weight="600" font-size="12.5" fill="#9aa2b2">
            <text x="212" y="284">region? religion?</text>
            <text x="212" y="303">where they settled?</text>
          </g>
          <g text-anchor="middle" font-style="italic" font-weight="600" font-size="12.5" fill="#caa8ad">
            <text x="688" y="284">S &amp; E Europe? cities?</text>
            <text x="688" y="303">nativism they faced?</text>
          </g>
          <g text-anchor="middle" font-style="italic" font-weight="600" font-size="11.5" fill="#c1a860">
            <text x="450" y="300">why leave?</text>
            <text x="450" y="318">shared hopes?</text>
          </g>
        </svg>
      </div>
    </div>
"""

ORGANIZERS = [dict(
    slug="26_us07_venn",
    title="&ldquo;Old&rdquo; vs. &ldquo;New&rdquo; Immigrants",
    kicker="Unit 1 &middot; US.07 &middot; Best-Fit Organizer",
    chips=[("Venn &middot; Compare Two", "navy"), ("DOK 2&ndash;3 &middot; Comparison", "skill")],
    why=("The &ldquo;old&rdquo; (pre-1880s, mostly N/W Europe) and &ldquo;new&rdquo; (1880s&ndash;1920s, mostly S/E Europe) waves differed in origin, "
         "religion, and reception &mdash; but shared the immigrant experience. The overlap is where nativism&rsquo;s logic breaks down. "
         "<span class='cite'>Similarities/differences analysis is Marzano&rsquo;s highest-yield strategy.</span>"),
    body=BODY, extra_css=CSS,
    udl=dict(
        scaffold="Give a labeled word bank (Ireland, Germany, Italy, Poland, Russia, Catholic, Jewish, tenement, farm) to sort into the regions.",
        extend="Use the BOTH region to challenge nativist arguments: if both waves shared so much, what really drove the backlash?",
        show="Students may <b>write</b>, <b>say</b> the contrast, <b>draw</b> a map of origins, or <b>build</b> the Venn with sortable cards."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 1 &middot; US.07 (labeled)",
)]
