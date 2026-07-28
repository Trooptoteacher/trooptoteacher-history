# -*- coding: utf-8 -*-
"""Unit 10 labeled -- US.94 Communication Methods Evolution (2-circle Venn).
Compare 1970s communication with present-day communication: what is unique to each
and what they share -- plus each era's characteristic strengths and limits. Per the
house Venn rule, ALL region labels and faded hints live as <text> INSIDE the SVG;
topic labels sit in a legend row ABOVE. HAS a Tennessee Connection. Approved for US.94.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .legend{ flex:0 0 auto; display:flex; gap:10px; margin-bottom:4px; }
  .legend .lg{ flex:1 1 0; border-radius:6px; padding:6px 11px; color:#fff; font-size:8.6pt; line-height:1.2; }
  .legend .lg.a{ background:var(--navy); } .legend .lg.b{ background:var(--red); }
  .legend .lg b{ font-size:9.6pt; letter-spacing:.02em; } .legend .lg small{ opacity:.9; }
  .venn-wrap{ flex:1 1 auto; position:relative; min-height:0; }
  .venn-wrap svg{ width:100%; height:100%; display:block; }
  .tnbox{ flex:0 0 auto; margin-top:4px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:6px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:13pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.4pt; line-height:1.28; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""

BODY = r"""
    <div class="prompt">Compare how Americans communicated in the <b>1970s</b> with how we communicate <b>today</b>. Write what was <b>unique</b> to each on its side, and what they <b>share</b> in the middle &mdash; the faint notes are starters. Note each era&rsquo;s strengths <i>and</i> limits.</div>
    <div class="canvas">
      <div class="legend">
        <div class="lg a"><b>THE 1970s</b> <small>&mdash; slower &middot; local &middot; deliberate</small></div>
        <div class="lg b"><b>TODAY</b> <small>&mdash; instant &middot; global &middot; digital</small></div>
      </div>
      <div class="venn-wrap">
        <svg viewBox="0 0 900 560" preserveAspectRatio="xMidYMid meet">
          <circle cx="330" cy="285" r="245" fill="#EEF1F7" stroke="#1B2A4A" stroke-width="3.5"/>
          <circle cx="570" cy="285" r="245" fill="#FBEEEF" stroke="#B22234" stroke-width="3.5"/>
          <path d="M 450,72.5 A 245,245 0 0,1 450,497.5 A 245,245 0 0,1 450,72.5 Z"
                fill="#FAF3E2" stroke="#C89B3C" stroke-width="2.5"/>
          <text x="205" y="118" text-anchor="middle" font-family="Georgia,serif" font-size="18" font-weight="700" fill="#1B2A4A">Only the 1970s</text>
          <text x="450" y="92" text-anchor="middle" font-family="Georgia,serif" font-size="17" font-weight="700" fill="#8a6a1e">Both</text>
          <text x="695" y="118" text-anchor="middle" font-family="Georgia,serif" font-size="18" font-weight="700" fill="#B22234">Only Today</text>
          <g font-family="Helvetica,Arial,sans-serif" font-size="14" font-style="italic" fill="#9aa6bd" text-anchor="middle">
            <text x="200" y="205">landline phones, 3 TV</text>
            <text x="200" y="235">networks, radio, mail</text>
            <text x="200" y="300">deeper focus &mdash;</text>
            <text x="200" y="330">but slow &amp; local</text>
            <text x="450" y="225">sharing news</text>
            <text x="450" y="270">&amp; connecting</text>
            <text x="450" y="315">people</text>
            <text x="700" y="205">smartphones, social</text>
            <text x="700" y="235">media, email, streaming</text>
            <text x="700" y="300">instant &amp; global &mdash; but</text>
            <text x="700" y="330">overload &amp; privacy risks</text>
          </g>
        </svg>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Tennessee helped lead the next leap: in 2010 the <b>Chattanooga</b>
        Electric Power Board launched the first citywide <b>1&#8209;gigabit&#8209;per&#8209;second internet</b> in the U.S. &mdash;
        making &ldquo;Gig City&rdquo; a national model, while Nashville grew into a major tech hub.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="31_us94_venn2",
    title="From Landlines to Live Streams",
    kicker="Unit 10 &middot; US.94 &middot; Best&#8209;Fit Organizer",
    chips=[("Venn &middot; Compare Two", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2&#8211;3 &middot; Compare", "skill")],
    why=("A Venn makes the <b>overlap</b> visible &mdash; both eras connect people and share news &mdash; while sorting what "
         "changed and weighing each era&rsquo;s strengths and limits. "
         "<span class='cite'>Identifying similarities &amp; differences is Marzano&rsquo;s highest&#8209;yield strategy; SSP.03.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Fill the <b>Both</b> region first (what has <i>not</i> changed), then sort each method to its era.",
        extend="Which era&rsquo;s communication was &ldquo;better&rdquo;? Use the strengths and limits to defend a position.",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>interview</b> an older relative about 1970s communication."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 10 &middot; US.94 (labeled)",
)]
