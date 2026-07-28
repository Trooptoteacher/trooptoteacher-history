# -*- coding: utf-8 -*-
"""Unit 10 labeled best-fit organizer -- Main Idea & Details.
US.85: Nixon's achievements -- foreign-policy breakthroughs, domestic reforms, the
"silent majority" strategy, and Vietnamization -- hold up one main idea: that his
presidency accomplished a great deal despite Watergate. Seeded as faint hints.
HAS a Tennessee Connection. Content approved for US.85.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .mi-box{ display:flex; flex-direction:column; min-height:0; }
  .mi-box .band{ flex:0 0 auto; }
  .mi-box .well{ flex:1 1 0; }
  .fade{ position:absolute; top:7px; left:10px; right:10px; font-size:8.3pt; font-style:italic;
         color:#9aa4b4; line-height:1.3; }
  .fade.sm{ font-size:7.4pt; line-height:1.24; }
  .mi-supports{ font-size:8pt; font-weight:800; color:var(--navy); text-transform:uppercase;
                letter-spacing:.05em; text-align:center; flex:0 0 auto; margin:3px 0 1px; }
  .mi-arrows{ display:grid; grid-template-columns:repeat(4,1fr); flex:0 0 auto; }
  .arr-u{ width:0; height:0; border-left:12px solid transparent; border-right:12px solid transparent;
          border-bottom:15px solid var(--navy); margin:0 auto; }
  .mi-details{ display:grid; grid-template-columns:repeat(4,1fr); gap:8px; flex:2.5 1 0; min-height:0; }
  .mi-details .band{ font-size:8pt; padding:5px 5px; line-height:1.12; }
  .tnbox{ flex:0 0 auto; margin-top:8px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.7pt; line-height:1.32; color:#3a2f12; }
  .tnbox .t b{ color:#7a5c15; }
"""

BODY = r"""
    <div class="prompt">Fill each <b>detail</b> box first, using the faint hints as anchors. Then infer the <b>main idea</b> all four support and write it up top &mdash; the arrows show every detail holding it up. Finish with one summary sentence.</div>
    <div class="canvas">
      <div class="mi-box" style="flex:1.15 1 0; min-height:0;">
        <div class="band navy sm">MAIN&nbsp;IDEA</div>
        <div class="well lines"><span class="fade">Though Watergate ended his presidency, Nixon achieved a great deal at home and abroad.</span></div>
      </div>
      <div class="mi-supports">&uarr;&nbsp; these four achievements support the main idea &nbsp;&uarr;</div>
      <div class="mi-arrows">
        <div class="arr-u"></div><div class="arr-u"></div><div class="arr-u"></div><div class="arr-u"></div>
      </div>
      <div class="mi-details">
        <div class="mi-box"><div class="band gold sm">Foreign&#8209;Policy Breakthroughs</div><div class="well tint-gold lines"><span class="fade sm">Opened relations with <b>China</b> (1972); <b>d&eacute;tente</b> &amp; the SALT I arms treaty with the USSR.</span></div></div>
        <div class="mi-box"><div class="band navy sm">Domestic Reforms</div><div class="well tint-navy lines"><span class="fade sm">Created the <b>EPA</b>; <b>Title IX</b> for gender equality; the <b>26th Amendment</b> &mdash; voting age 18.</span></div></div>
        <div class="mi-box"><div class="band navy sm">The &ldquo;Silent Majority&rdquo;</div><div class="well tint-navy lines"><span class="fade sm">Appealed to Americans who didn&rsquo;t protest &mdash; reshaping the Republican coalition for decades.</span></div></div>
        <div class="mi-box"><div class="band navy sm">Vietnamization</div><div class="well tint-navy lines"><span class="fade sm">Gradually withdrew U.S. troops while backing South Vietnam &mdash; which ultimately fell.</span></div></div>
      </div>
      <div class="mi-box" style="flex:0.82 1 0; min-height:0; margin-top:8px;">
        <div class="band gold sm">In one sentence, how should we remember the Nixon presidency?</div>
        <div class="well cream lines"></div>
      </div>
      <div class="tnbox">
        <span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection &mdash;</b> Tennessee Senator <b>Howard Baker</b> served as Senate Minority
        Leader during these years &mdash; a leading Republican voice who would soon become a national figure in the
        Watergate hearings.</span>
      </div>
    </div>
"""

_UDL = dict(
    scaffold="Fill the four detail boxes first using the faint hints, then infer the main idea together. Frame: &ldquo;All four show that ___.&rdquo;",
    extend="Historians debate Nixon&rsquo;s legacy. Use the boxes to argue: do his achievements or Watergate define him?",
    show="Students may <b>write</b> the boxes, <b>say</b> the main idea aloud, or <b>rank</b> the four achievements.")

ORGANIZERS = [
    dict(
        slug="22_us85_mainidea",
        title="Nixon: Achievements in a Shadowed Presidency",
        kicker="Unit 10 &middot; US.85 &middot; Best&#8209;Fit Organizer",
        chips=[("Main Idea &amp; Details", "navy"), ("&#9733; Tennessee Connection", "gold"), ("DOK 2&#8211;3 &middot; Summarize", "skill")],
        why=("A main&#8209;idea organizer separates the <b>big idea</b> from the details, so students can hold Nixon&rsquo;s "
             "real achievements and his fall in view at the same time. "
             "<span class='cite'>Summarizing &mdash; keep the main idea, cut the rest &mdash; is a high&#8209;yield "
             "comprehension strategy (Marzano).</span>"),
        body=BODY, extra_css=CSS, udl=_UDL,
        role="Teacher Graphic Organizer Toolkit &middot; Unit 10 &middot; US.85 (labeled)",
    ),
]
