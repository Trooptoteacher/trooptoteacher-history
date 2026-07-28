# -*- coding: utf-8 -*-
"""Unit 6 labeled -- US.57 Yalta vs. Potsdam (2-circle Venn).
Compare the two Allied conferences: what was unique to each and what they shared.
Per the house Venn rule, ALL region labels and faded content hints live as <text>
INSIDE the SVG (they scale with the diagram and never drift into the letterbox
margins); the topic labels + write-lines sit in a legend row ABOVE the diagram.
A bottom note ties both to the Cold War's origins. No TN tie. Approved US.57.
"""

CSS = r"""
  .legend{ flex:0 0 auto; display:flex; gap:10px; margin-bottom:4px; }
  .legend .lg{ flex:1 1 0; border-radius:6px; padding:6px 11px; color:#fff; font-size:8.6pt; line-height:1.2; }
  .legend .lg.a{ background:var(--navy); } .legend .lg.b{ background:var(--red); }
  .legend .lg b{ font-size:9.6pt; letter-spacing:.02em; } .legend .lg small{ opacity:.9; }
  .venn-wrap{ flex:1 1 auto; position:relative; min-height:0; }
  .venn-wrap svg{ width:100%; height:100%; display:block; }
  .note{ flex:0 0 auto; margin-top:4px; background:var(--cream); border:1.6px solid var(--gold);
         border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 11px;
         font-size:8.8pt; color:var(--navy); line-height:1.3; } .note b{ color:var(--navy); }
"""

BODY = r"""
    <div class="prompt">Both were <b>Allied conferences</b> near the war&rsquo;s end. Write what was <b>unique</b> to each on its side, and what they <b>shared</b> in the middle &mdash; the faint notes are starters.</div>
    <div class="canvas">
      <div class="legend">
        <div class="lg a"><b>YALTA</b> &nbsp;&middot;&nbsp; Feb. 1945 <small>&mdash; FDR &middot; Churchill &middot; Stalin</small></div>
        <div class="lg b"><b>POTSDAM</b> &nbsp;&middot;&nbsp; July&ndash;Aug. 1945 <small>&mdash; Truman &middot; Attlee &middot; Stalin</small></div>
      </div>
      <div class="venn-wrap">
        <svg viewBox="0 0 900 560" preserveAspectRatio="xMidYMid meet">
          <circle cx="330" cy="285" r="245" fill="#EEF1F7" stroke="#1B2A4A" stroke-width="3.5"/>
          <circle cx="570" cy="285" r="245" fill="#FBEEEF" stroke="#B22234" stroke-width="3.5"/>
          <path d="M 450,72.5 A 245,245 0 0,1 450,497.5 A 245,245 0 0,1 450,72.5 Z"
                fill="#FAF3E2" stroke="#C89B3C" stroke-width="2.5"/>
          <!-- region captions (inside SVG) -->
          <text x="205" y="120" text-anchor="middle" font-family="Georgia,serif" font-size="18" font-weight="700" fill="#1B2A4A">Only Yalta</text>
          <text x="450" y="92" text-anchor="middle" font-family="Georgia,serif" font-size="17" font-weight="700" fill="#8a6a1e">Both</text>
          <text x="695" y="120" text-anchor="middle" font-family="Georgia,serif" font-size="18" font-weight="700" fill="#B22234">Only Potsdam</text>
          <!-- faded starters (inside SVG) -->
          <g font-family="Helvetica,Arial,sans-serif" font-size="14.5" font-style="italic" fill="#9aa6bd" text-anchor="middle">
            <text x="203" y="235">plan the United Nations</text>
            <text x="203" y="285">Stalin: &#8220;free elections&#8221;</text>
            <text x="203" y="335">USSR to fight Japan</text>
            <text x="450" y="215">the Big Three met</text>
            <text x="450" y="265">split Germany into zones</text>
            <text x="450" y="315">reparations &amp; tension</text>
            <text x="697" y="235">Germany had surrendered</text>
            <text x="697" y="285">ultimatum to Japan</text>
            <text x="697" y="335">Truman &amp; Attlee now lead</text>
          </g>
        </svg>
      </div>
      <div class="note"><b>Why it matters &rarr;</b> Both conferences exposed a growing split: Stalin&rsquo;s &ldquo;free elections&rdquo; meant
      communist&#8209;controlled governments, while the West expected real democracy &mdash; the <b>origins of the Cold War</b>.</div>
    </div>
"""

ORGANIZERS = [dict(
    slug="32_us57_venn2",
    title="Yalta &amp; Potsdam: Two Meetings, One Widening Split",
    kicker="Unit 6 &middot; US.57 &middot; Best&#8209;Fit Organizer",
    chips=[("Venn &middot; Compare Two", "navy"), ("DOK 2&#8211;3 &middot; Compare", "skill")],
    why=("Two conferences, months apart, decided the shape of the post&#8209;war world. A Venn makes the <b>overlap</b> "
         "visible &mdash; and sharpens what changed between February and July 1945. "
         "<span class='cite'>Identifying similarities &amp; differences is Marzano&rsquo;s highest&#8209;yield strategy; SSP.03.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Fill the <b>Both</b> region first (they were both Allied conferences), then find what made each one different.",
        extend="What changed between Yalta and Potsdam &mdash; in leaders, and in trust? Explain what the shift reveals.",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>sort</b> outcome cards into the three regions."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 6 &middot; US.57 (labeled)",
)]
