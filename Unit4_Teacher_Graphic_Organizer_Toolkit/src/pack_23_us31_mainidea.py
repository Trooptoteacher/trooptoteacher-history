# -*- coding: utf-8 -*-
"""Unit 4 labeled best-fit organizer -- Main Idea & Details.
US.31: New technologies -- air travel & electricity. Four supporting developments
       hold up one main idea about how new technology reshaped 1920s life. Seeded
       as faint hints. TN tie: the rural-urban electrification gap (later TVA).
Neutral framing: developments described factually; the summary is the student's.
Content approved for US.31.
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
    <div class="prompt">Fill each <b>detail</b> box first, using the faint hints as anchors. Then infer the <b>main idea</b> all four developments support and write it up top &mdash; the arrows show every detail holding it up. Finish with one summary sentence.</div>
    <div class="canvas">
      <div class="mi-box" style="flex:1.15 1 0; min-height:0;">
        <div class="band navy sm">MAIN&nbsp;IDEA</div>
        <div class="well lines"><span class="fade">New technologies &mdash; air travel and electricity &mdash; reshaped how Americans traveled, worked, and lived in the 1920s.</span></div>
      </div>
      <div class="mi-supports">&uarr;&nbsp; these four developments support the main idea &nbsp;&uarr;</div>
      <div class="mi-arrows">
        <div class="arr-u"></div><div class="arr-u"></div><div class="arr-u"></div><div class="arr-u"></div>
      </div>
      <div class="mi-details">
        <div class="mi-box"><div class="band red sm">Aviation Takes Off</div><div class="well tint-red lines"><span class="fade sm">Wright Brothers, 1903; WWI advanced aircraft; airmail, 1918; Lindbergh&rsquo;s solo transatlantic flight, 1927.</span></div></div>
        <div class="mi-box"><div class="band navy sm">Air Travel&rsquo;s Impact</div><div class="well tint-navy lines"><span class="fade sm">Cross&#8209;country trips: days &rarr; hours. Passenger&#8209;miles: 6,000 (1926) &rarr; 173,000 (1929); new airports.</span></div></div>
        <div class="mi-box"><div class="band gold sm">Electricity Spreads</div><div class="well tint-gold lines"><span class="fade sm">By 1930, 85% of urban homes had power; generation 6B kWh (1902) &rarr; 117B (1929).</span></div></div>
        <div class="mi-box"><div class="band navy sm">Electricity Changes Life</div><div class="well tint-navy lines"><span class="fade sm">Streetlights, trolleys, elevators (skyscrapers); appliances &mdash; vacuum, washer, iron, refrigerator.</span></div></div>
      </div>
      <div class="mi-box" style="flex:0.82 1 0; min-height:0; margin-top:8px;">
        <div class="band gold sm">In one sentence, how did new technology change everyday American life?</div>
        <div class="well cream lines"></div>
      </div>
      <div class="tnbox">
        <span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection &mdash;</b> Not everyone shared these gains at once. The <b>rural&#8209;urban
        electrification gap</b> left much of rural Tennessee without power until New Deal programs like the
        <b>Tennessee Valley Authority (TVA)</b> brought electricity to underserved areas in the 1930s.</span>
      </div>
    </div>
"""

_UDL = dict(
    scaffold="Fill the four detail boxes first using the faint hints, then infer the main idea together. Frame: &ldquo;All four of these show that ___.&rdquo;",
    extend="Did these technologies improve life for <b>all</b> Americans at once, or some first? Use the TVA note as evidence.",
    show="Students may <b>write</b> the boxes, <b>say</b> the main idea aloud, or <b>draw</b> an icon for each development.")

ORGANIZERS = [
    dict(
        slug="23_us31_mainidea",
        title="New Technology Reshapes Everyday Life",
        kicker="Unit 4 &middot; US.31 &middot; Best&#8209;Fit Organizer",
        chips=[("Main Idea &amp; Details", "navy"), ("&#9733; Tennessee Connection", "gold"), ("DOK 2 &middot; Summarize", "skill")],
        why=("A main&#8209;idea organizer separates the <b>big idea</b> from the developments that support it, so students "
             "summarize instead of listing facts. "
             "<span class='cite'>Summarizing &mdash; keep the main idea, cut the rest &mdash; is a high&#8209;yield "
             "comprehension strategy (Marzano).</span>"),
        body=BODY, extra_css=CSS, udl=_UDL,
        role="Teacher Graphic Organizer Toolkit &middot; Unit 4 &middot; US.31 (labeled)",
    ),
]
