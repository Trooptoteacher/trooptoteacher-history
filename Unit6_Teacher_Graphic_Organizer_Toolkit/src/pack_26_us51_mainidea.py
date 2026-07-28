# -*- coding: utf-8 -*-
"""Unit 6 labeled best-fit organizer -- Main Idea & Details.
US.51: Special fighting forces -- Tuskegee Airmen, 442nd RCT, 101st Airborne,
Navajo Code Talkers -- hold up one main idea about diverse Americans making
decisive contributions, many while facing prejudice at home. Seeded as faint
hints. HAS a Tennessee Connection (Fort Campbell / 101st). Approved US.51.
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
  .mi-details .band{ font-size:8.1pt; padding:5px 5px; line-height:1.12; }
  .tnbox{ flex:0 0 auto; margin-top:8px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.7pt; line-height:1.32; color:#3a2f12; }
  .tnbox .t b{ color:#7a5c15; }
"""

BODY = r"""
    <div class="prompt">Fill each <b>detail</b> box first, using the faint hints as anchors. Then infer the <b>main idea</b> all four units support and write it up top &mdash; the arrows show every detail holding it up. Finish with one summary sentence.</div>
    <div class="canvas">
      <div class="mi-box" style="flex:1.15 1 0; min-height:0;">
        <div class="band navy sm">MAIN&nbsp;IDEA</div>
        <div class="well lines"><span class="fade">Special forces and individual soldiers &mdash; many facing prejudice at home &mdash; made decisive contributions and sacrifices to win the war.</span></div>
      </div>
      <div class="mi-supports">&uarr;&nbsp; these four forces support the main idea &nbsp;&uarr;</div>
      <div class="mi-arrows">
        <div class="arr-u"></div><div class="arr-u"></div><div class="arr-u"></div><div class="arr-u"></div>
      </div>
      <div class="mi-details">
        <div class="mi-box"><div class="band navy sm">Tuskegee Airmen</div><div class="well tint-navy lines"><span class="fade sm">First African American military pilots; 332nd Fighter Group; 15,000+ sorties; helped lead to 1948 desegregation of the military.</span></div></div>
        <div class="mi-box"><div class="band red sm">442nd Combat Team</div><div class="well tint-red lines"><span class="fade sm">Japanese American volunteers &mdash; many with families interned; most decorated unit of its size; 21 Medals of Honor; &ldquo;Go for Broke.&rdquo;</span></div></div>
        <div class="mi-box"><div class="band gold sm">101st Airborne</div><div class="well tint-gold lines"><span class="fade sm">&ldquo;Screaming Eagles&rdquo; parachuted into Normandy on D&#8209;Day; secured bridges; defended Bastogne in the Battle of the Bulge.</span></div></div>
        <div class="mi-box"><div class="band navy sm">Navajo Code Talkers</div><div class="well tint-navy lines"><span class="fade sm">Used the Navajo language as an unbreakable battlefield code in the Pacific &mdash; never cracked by the enemy.</span></div></div>
      </div>
      <div class="mi-box" style="flex:0.82 1 0; min-height:0; margin-top:8px;">
        <div class="band gold sm">In one sentence, what did these forces show about who won the war?</div>
        <div class="well cream lines"></div>
      </div>
      <div class="tnbox">
        <span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection &mdash;</b> <b>Fort Campbell</b>, straddling the Tennessee&ndash;Kentucky border,
        became home to the <b>101st Airborne Division</b> (&ldquo;Screaming Eagles&rdquo;) &mdash; whose paratroopers jumped into
        Normandy on D&#8209;Day and fought through the Battle of the Bulge.</span>
      </div>
    </div>
"""

_UDL = dict(
    scaffold="Fill the four detail boxes first using the faint hints, then infer the main idea together. Frame: &ldquo;All four of these show that ___.&rdquo;",
    extend="Several of these units served while facing prejudice at home. What does that add to their story? Defend your answer with evidence.",
    show="Students may <b>write</b> the boxes, <b>say</b> the main idea aloud, or <b>present</b> one unit&rsquo;s story.")

ORGANIZERS = [
    dict(
        slug="26_us51_mainidea",
        title="They Fought for a Country That Doubted Them",
        kicker="Unit 6 &middot; US.51 &middot; Best&#8209;Fit Organizer",
        chips=[("Main Idea &amp; Details", "navy"), ("&#9733; Tennessee Connection", "gold"), ("DOK 2 &middot; Summarize", "skill")],
        why=("A main&#8209;idea organizer separates the <b>big idea</b> from the units that support it, so students summarize "
             "the meaning of these forces&rsquo; service instead of just listing them. "
             "<span class='cite'>Summarizing &mdash; keep the main idea, cut the rest &mdash; is a high&#8209;yield "
             "comprehension strategy (Marzano).</span>"),
        body=BODY, extra_css=CSS, udl=_UDL,
        role="Teacher Graphic Organizer Toolkit &middot; Unit 6 &middot; US.51 (labeled)",
    ),
]
