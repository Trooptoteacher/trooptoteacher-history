# -*- coding: utf-8 -*-
"""Unit 5 labeled best-fit organizer -- Main Idea & Details.
US.41: Impact of the Depression on the American people. Four supporting details --
mass unemployment, families under stress, internal migration, Hoovervilles --
hold up one main idea about how the Depression reshaped everyday life. Seeded as
faint hints. TN tie: Memphis 30% unemployment; Highlander Folk School. Neutral
framing; the summary is the student's. Content approved for US.41.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .mi-box{ display:flex; flex-direction:column; min-height:0; }
  .mi-box .band{ flex:0 0 auto; }
  .mi-box .well{ flex:1 1 0; }
  .fade{ position:absolute; top:7px; left:10px; right:10px; font-size:8.3pt; font-style:italic;
         color:#9aa4b4; line-height:1.3; }
  .fade.sm{ font-size:7.5pt; line-height:1.25; }
  .mi-supports{ font-size:8pt; font-weight:800; color:var(--navy); text-transform:uppercase;
                letter-spacing:.05em; text-align:center; flex:0 0 auto; margin:3px 0 1px; }
  .mi-arrows{ display:grid; grid-template-columns:repeat(4,1fr); flex:0 0 auto; }
  .arr-u{ width:0; height:0; border-left:12px solid transparent; border-right:12px solid transparent;
          border-bottom:15px solid var(--navy); margin:0 auto; }
  .mi-details{ display:grid; grid-template-columns:repeat(4,1fr); gap:8px; flex:2.5 1 0; min-height:0; }
  .mi-details .band{ font-size:8.2pt; padding:5px 5px; line-height:1.12; }
  .tnbox{ flex:0 0 auto; margin-top:8px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.7pt; line-height:1.32; color:#3a2f12; }
  .tnbox .t b{ color:#7a5c15; }
"""

BODY = r"""
    <div class="prompt">Fill each <b>detail</b> box first, using the faint hints as anchors. Then infer the <b>main idea</b> all four hardships support and write it up top &mdash; the arrows show every detail holding it up. Finish with one summary sentence.</div>
    <div class="canvas">
      <div class="mi-box" style="flex:1.15 1 0; min-height:0;">
        <div class="band navy sm">MAIN&nbsp;IDEA</div>
        <div class="well lines"><span class="fade">The Great Depression reshaped everyday life for ordinary Americans &mdash; how they worked, where they lived, and how families survived.</span></div>
      </div>
      <div class="mi-supports">&uarr;&nbsp; these four hardships support the main idea &nbsp;&uarr;</div>
      <div class="mi-arrows">
        <div class="arr-u"></div><div class="arr-u"></div><div class="arr-u"></div><div class="arr-u"></div>
      </div>
      <div class="mi-details">
        <div class="mi-box"><div class="band red sm">Mass Unemployment</div><div class="well tint-red lines"><span class="fade sm">Peaked at 25% in 1933 (12&ndash;15M jobless); youth unemployment near 50%; many idle for years.</span></div></div>
        <div class="mi-box"><div class="band navy sm">Families Under Stress</div><div class="well tint-navy lines"><span class="fade sm">Role reversal; households double up; gardens, bartering &amp; church aid; shame &amp; withdrawal.</span></div></div>
        <div class="mi-box"><div class="band gold sm">Internal Migration</div><div class="well tint-gold lines"><span class="fade sm">Rural&rarr;urban, South&rarr;North, Plains&rarr;California; following family &amp; work; facing discrimination.</span></div></div>
        <div class="mi-box"><div class="band navy sm">Hoovervilles</div><div class="well tint-navy lines"><span class="fade sm">Shanty towns of cardboard, tin &amp; scrap on city edges; named for Hoover; no water or power.</span></div></div>
      </div>
      <div class="mi-box" style="flex:0.82 1 0; min-height:0; margin-top:8px;">
        <div class="band gold sm">In one sentence, how did the Depression change life for ordinary Americans?</div>
        <div class="well cream lines"></div>
      </div>
      <div class="tnbox">
        <span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection &mdash;</b> The Depression devastated Tennessee: by 1933 unemployment in
        <b>Memphis</b> topped <b>30%</b>, and West Tennessee <b>sharecroppers</b> were among the hardest hit. The
        <b>Highlander Folk School</b> in Monteagle trained labor organizers to help Tennessee workers through the crisis.</span>
      </div>
    </div>
"""

_UDL = dict(
    scaffold="Fill the four detail boxes first using the faint hints, then infer the main idea together. Frame: &ldquo;All four of these show that ___.&rdquo;",
    extend="Which hardship do you think was hardest to endure &mdash; and why? Defend your pick with evidence from the boxes.",
    show="Students may <b>write</b> the boxes, <b>say</b> the main idea aloud, or <b>draw</b> a scene for each hardship.")

ORGANIZERS = [
    dict(
        slug="22_us41_mainidea",
        title="How the Depression Changed Everyday Life",
        kicker="Unit 5 &middot; US.41 &middot; Best&#8209;Fit Organizer",
        chips=[("Main Idea &amp; Details", "navy"), ("&#9733; Tennessee Connection", "gold"), ("DOK 2 &middot; Summarize", "skill")],
        why=("A main&#8209;idea organizer separates the <b>big idea</b> from the hardships that support it, so students "
             "summarize the human cost instead of listing facts. "
             "<span class='cite'>Summarizing &mdash; keep the main idea, cut the rest &mdash; is a high&#8209;yield "
             "comprehension strategy (Marzano).</span>"),
        body=BODY, extra_css=CSS, udl=_UDL,
        role="Teacher Graphic Organizer Toolkit &middot; Unit 5 &middot; US.41 (labeled)",
    ),
]
