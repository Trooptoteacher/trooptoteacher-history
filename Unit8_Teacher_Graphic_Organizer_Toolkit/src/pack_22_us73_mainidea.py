# -*- coding: utf-8 -*-
"""Unit 8 labeled best-fit organizer -- Main Idea & Details.
US.73: Eisenhower-era domestic developments -- the polio vaccine and the Interstate
Highway System (its jobs/goods, its suburbs/mobility, and its costs) -- hold up one
main idea about breakthroughs that reshaped daily life, with benefits and costs.
Seeded as faint hints. HAS a Tennessee Connection. Content approved for US.73.
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
    <div class="prompt">Fill each <b>detail</b> box first, using the faint hints as anchors. Then infer the <b>main idea</b> all four support and write it up top &mdash; the arrows show every detail holding it up. Finish with one summary sentence.</div>
    <div class="canvas">
      <div class="mi-box" style="flex:1.15 1 0; min-height:0;">
        <div class="band navy sm">MAIN&nbsp;IDEA</div>
        <div class="well lines"><span class="fade">Eisenhower-era breakthroughs in medicine and highways reshaped everyday American life &mdash; bringing big benefits, and some costs.</span></div>
      </div>
      <div class="mi-supports">&uarr;&nbsp; these four developments support the main idea &nbsp;&uarr;</div>
      <div class="mi-arrows">
        <div class="arr-u"></div><div class="arr-u"></div><div class="arr-u"></div><div class="arr-u"></div>
      </div>
      <div class="mi-details">
        <div class="mi-box"><div class="band gold sm">The Polio Vaccine</div><div class="well tint-gold lines"><span class="fade sm">The 1955 Salk vaccine ended parents&rsquo; fear of polio &mdash; restoring confidence in science and public health.</span></div></div>
        <div class="mi-box"><div class="band navy sm">Highways: Jobs &amp; Goods</div><div class="well tint-navy lines"><span class="fade sm">The largest public works project in U.S. history: millions of jobs; goods moved coast to coast; cars, gas, motels &amp; fast food grew.</span></div></div>
        <div class="mi-box"><div class="band navy sm">Highways: Suburbs &amp; Mobility</div><div class="well tint-navy lines"><span class="fade sm">Longer commutes made suburbs possible; family life &amp; leisure grew more mobile.</span></div></div>
        <div class="mi-box"><div class="band red sm">Highways: The Costs</div><div class="well tint-red lines"><span class="fade sm">Bypassed small towns declined; new roads divided urban neighborhoods &mdash; often minority communities.</span></div></div>
      </div>
      <div class="mi-box" style="flex:0.82 1 0; min-height:0; margin-top:8px;">
        <div class="band gold sm">In one sentence, how did these developments change daily life?</div>
        <div class="well cream lines"></div>
      </div>
      <div class="tnbox">
        <span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection &mdash;</b> Eisenhower&rsquo;s highway act reshaped Tennessee: <b>I&#8209;40, I&#8209;65,
        I&#8209;24, and I&#8209;75</b> connected <b>Nashville, Memphis, Chattanooga, and Knoxville</b> to the national network &mdash;
        accelerating suburban growth and the trucking industry.</span>
      </div>
    </div>
"""

_UDL = dict(
    scaffold="Fill the four detail boxes first using the faint hints, then infer the main idea together. Frame: &ldquo;All four of these show that ___.&rdquo;",
    extend="The highways brought benefits <b>and</b> costs. Using the last two boxes, argue whether they helped or hurt more.",
    show="Students may <b>write</b> the boxes, <b>say</b> the main idea aloud, or <b>map</b> the interstate routes.")

ORGANIZERS = [
    dict(
        slug="22_us73_mainidea",
        title="Vaccines &amp; Highways: The 1950s Remade Daily Life",
        kicker="Unit 8 &middot; US.73 &middot; Best&#8209;Fit Organizer",
        chips=[("Main Idea &amp; Details", "navy"), ("&#9733; Tennessee Connection", "gold"), ("DOK 2&#8211;3 &middot; Summarize", "skill")],
        why=("A main&#8209;idea organizer separates the <b>big idea</b> from the details, so students weigh the benefits and "
             "costs of two era&#8209;defining developments instead of just listing them. "
             "<span class='cite'>Summarizing &mdash; keep the main idea, cut the rest &mdash; is a high&#8209;yield "
             "comprehension strategy (Marzano).</span>"),
        body=BODY, extra_css=CSS, udl=_UDL,
        role="Teacher Graphic Organizer Toolkit &middot; Unit 8 &middot; US.73 (labeled)",
    ),
]
