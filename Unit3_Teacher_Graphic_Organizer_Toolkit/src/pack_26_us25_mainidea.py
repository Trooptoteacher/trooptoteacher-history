# -*- coding: utf-8 -*-
"""Unit 3 labeled best-fit organizer -- Main Idea & Details.
US.25: Key figures & developments in WWI. Four supporting developments hold up
       one main idea about how America helped turn the tide on the Western Front.
       Required items grouped into four detail boxes, seeded as faint hints.
TN tie: Sgt. Alvin C. York of Fentress County (gold callout).
Neutral framing: developments described factually; the summary is the student's.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .mi-box{ display:flex; flex-direction:column; min-height:0; }
  .mi-box .band{ flex:0 0 auto; }
  .mi-box .well{ flex:1 1 0; }
  .fade{ position:absolute; top:7px; left:10px; right:10px; font-size:8.4pt; font-style:italic;
         color:#9aa4b4; line-height:1.32; }
  .fade.sm{ font-size:7.5pt; line-height:1.26; }
  .mi-supports{ font-size:8pt; font-weight:800; color:var(--navy); text-transform:uppercase;
                letter-spacing:.05em; text-align:center; flex:0 0 auto; margin:3px 0 1px; }
  .mi-arrows{ display:grid; grid-template-columns:repeat(4,1fr); flex:0 0 auto; }
  .arr-u{ width:0; height:0; border-left:12px solid transparent; border-right:12px solid transparent;
          border-bottom:15px solid var(--navy); margin:0 auto; }
  .mi-details{ display:grid; grid-template-columns:repeat(4,1fr); gap:8px; flex:2.5 1 0; min-height:0; }
  .mi-details .band{ font-size:8.4pt; padding:5px 5px; line-height:1.12; }
  .tnbox{ flex:0 0 auto; margin-top:8px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.7pt; line-height:1.32; color:#3a2f12; }
  .tnbox .t b{ color:#7a5c15; }
"""

BODY = r"""
    <div class="prompt">Fill each <b>detail</b> box first, using the faint hints as anchors. Then infer the <b>main idea</b> all four developments support and write it up top &mdash; the arrows show every detail holding it up. Finish with one summary sentence.</div>
    <div class="canvas">
      <div class="mi-box" style="flex:1.15 1 0; min-height:0;">
        <div class="band navy sm">MAIN&nbsp;IDEA</div>
        <div class="well lines"><span class="fade">American troops, new tactics, and standout soldiers helped the Allies gain the advantage on the Western Front.</span></div>
      </div>
      <div class="mi-supports">&uarr;&nbsp; these four developments support the main idea &nbsp;&uarr;</div>
      <div class="mi-arrows">
        <div class="arr-u"></div><div class="arr-u"></div><div class="arr-u"></div><div class="arr-u"></div>
      </div>
      <div class="mi-details">
        <div class="mi-box"><div class="band red sm">Trench Warfare &amp; New Technology</div><div class="well tint-red lines"><span class="fade sm">Trench warfare &amp; No Man&rsquo;s Land; new weapons &mdash; machine guns, poison gas, tanks, and aircraft.</span></div></div>
        <div class="mi-box"><div class="band navy sm">Harlem Hellfighters</div><div class="well tint-navy lines"><span class="fade sm">The 369th Infantry Regiment &mdash; an African American unit that fought on the Western Front.</span></div></div>
        <div class="mi-box"><div class="band gold sm">Military Leaders</div><div class="well tint-gold lines"><span class="fade sm">Gen. John J. Pershing led the AEF; Herbert Hoover ran the Food Administration on the supply side.</span></div></div>
        <div class="mi-box"><div class="band navy sm">Sgt. Alvin C. York</div><div class="well tint-navy lines"><span class="fade sm">Meuse&ndash;Argonne Offensive, October 1918.</span></div></div>
      </div>
      <div class="mi-box" style="flex:0.82 1 0; min-height:0; margin-top:8px;">
        <div class="band gold sm">In one sentence, how did America&rsquo;s entry change the war?</div>
        <div class="well cream lines"></div>
      </div>
      <div class="tnbox">
        <span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection &mdash;</b> Alvin C. York of <b>Fentress County, Tennessee</b> became one of the most decorated American soldiers of WWI &mdash; in the Meuse&ndash;Argonne Offensive of October 1918 he helped capture 132 German soldiers.</span>
      </div>
    </div>
"""

_UDL = dict(
    scaffold="Fill the four detail boxes first using the faint hints, then infer the main idea together. Frame: &ldquo;All four of these show that ___.&rdquo;",
    extend="Which development mattered most to the Allied advantage? Defend your pick with evidence from the boxes.",
    show="Students may <b>write</b> the boxes, <b>say</b> the main idea aloud, or <b>draw</b> an icon for each development.")

ORGANIZERS = [
    dict(
        slug="26_us25_mainidea",
        title="How America Helped Turn the Tide",
        kicker="Unit 3 &middot; US.25 &middot; Best&#8209;Fit Organizer",
        chips=[("Main Idea &amp; Details", "navy"), ("&#9733; Tennessee Connection", "gold"), ("DOK 2 &middot; Summarize", "skill")],
        why=("A main&#8209;idea organizer separates the <b>big idea</b> from the details and evidence that support it, "
             "so students summarize instead of listing facts. "
             "<span class='cite'>Summarizing &mdash; keep the main idea, cut the rest &mdash; is a high&#8209;yield "
             "comprehension strategy (Marzano).</span>"),
        body=BODY, extra_css=CSS, udl=_UDL,
        role="Teacher Graphic Organizer Toolkit &middot; Unit 3 &middot; US.25 (labeled)",
    ),
]
