# -*- coding: utf-8 -*-
"""Unit 1 labeled — US.07 'Old' vs. 'New' immigrants (Venn).
Topic sourced from standards inventory (US.07: Immigration - Old vs. New,
Assimilation, Nativism).
"""

CSS = r"""
  .venn-wrap{ flex:1 1 auto; position:relative; min-height:0; }
  .venn-wrap svg{ width:100%; height:100%; display:block; }
  .vhead{ position:absolute; top:-2px; display:flex; flex-direction:column; gap:1px; }
  .vhead .nm{ font-weight:800; font-size:12pt; } .vhead .yr{ font-size:8pt; font-weight:700; color:var(--muted); }
  .vlbl{ position:absolute; text-align:center; font-size:11pt; font-weight:800; letter-spacing:.02em; }
  .vhint{ position:absolute; font-size:7.8pt; font-style:italic; color:#8792a4; text-align:center; width:150px; }
"""

BODY = r"""
    <div class="prompt">Two waves, one country. Write what set each wave apart &mdash; and what every newcomer shared.</div>
    <div class="canvas">
      <div class="venn-wrap">
        <svg viewBox="0 0 900 560" preserveAspectRatio="xMidYMid meet">
          <circle cx="330" cy="285" r="245" fill="#EEF1F7" stroke="#1B2A4A" stroke-width="3.5"/>
          <circle cx="570" cy="285" r="245" fill="#FBEEEF" stroke="#B22234" stroke-width="3.5"/>
          <path d="M 450,72.5 A 245,245 0 0,1 450,497.5 A 245,245 0 0,1 450,72.5 Z" fill="#FAF3E2" stroke="#C89B3C" stroke-width="2.5"/>
          <g stroke="#B9C2D0" stroke-width="1.2" stroke-dasharray="2 5">
            <line x1="150" y1="250" x2="330" y2="250"/><line x1="140" y1="300" x2="330" y2="300"/><line x1="150" y1="350" x2="330" y2="350"/></g>
          <g stroke="#D8B3B7" stroke-width="1.2" stroke-dasharray="2 5">
            <line x1="570" y1="250" x2="750" y2="250"/><line x1="570" y1="300" x2="760" y2="300"/><line x1="570" y1="350" x2="750" y2="350"/></g>
          <g stroke="#E0CB94" stroke-width="1.2" stroke-dasharray="2 5">
            <line x1="410" y1="265" x2="490" y2="265"/><line x1="405" y1="295" x2="495" y2="295"/><line x1="410" y1="325" x2="490" y2="325"/></g>
        </svg>
        <div class="vhead" style="left:3%; color:var(--navy);"><span class="nm">&ldquo;OLD&rdquo; Immigrants</span><span class="yr">before the 1880s</span></div>
        <div class="vhead" style="right:3%; text-align:right; color:var(--red);"><span class="nm">&ldquo;NEW&rdquo; Immigrants</span><span class="yr">1880s&ndash;1920s</span></div>
        <div class="vlbl" style="top:31%; left:12%; color:var(--navy);">ONLY&nbsp;&ldquo;OLD&rdquo;</div>
        <div class="vhint" style="top:41%; left:8%;">region? religion? where they settled?</div>
        <div class="vlbl" style="top:31%; right:12%; color:var(--red);">ONLY&nbsp;&ldquo;NEW&rdquo;</div>
        <div class="vhint" style="top:41%; right:8%;">S &amp; E Europe? cities? nativism faced?</div>
        <div class="vlbl" style="top:28%; left:44%; color:#8a6a1e;">BOTH</div>
        <div class="vhint" style="top:52%; left:calc(50% - 75px); color:#a98b3e;">why leave? what hopes &amp; hardships shared?</div>
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
