# -*- coding: utf-8 -*-
"""Unit 6 labeled best-fit organizer -- Main Idea & Details.
US.47: U.S. response to the Holocaust across three phases -- before the war, the
liberation of camps, and post-war immigration -- plus why the early response was
limited. Four detail boxes hold up one main idea. Seeded as faint hints. Handled
with dignity and factual restraint. No TN tie in source. Approved US.47.
"""

CSS = r"""
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
"""

BODY = r"""
    <div class="prompt">Fill each <b>detail</b> box first, using the faint hints as anchors. Then infer the <b>main idea</b> all four support and write it up top &mdash; the arrows show every detail holding it up. Finish with one summary sentence.</div>
    <div class="canvas">
      <div class="mi-box" style="flex:1.15 1 0; min-height:0;">
        <div class="band navy sm">MAIN&nbsp;IDEA</div>
        <div class="well lines"><span class="fade">The U.S. response to the Holocaust was limited before the war, direct in liberating the camps, and opened afterward to survivors.</span></div>
      </div>
      <div class="mi-supports">&uarr;&nbsp; these four points support the main idea &nbsp;&uarr;</div>
      <div class="mi-arrows">
        <div class="arr-u"></div><div class="arr-u"></div><div class="arr-u"></div><div class="arr-u"></div>
      </div>
      <div class="mi-details">
        <div class="mi-box"><div class="band navy sm">Before the War</div><div class="well tint-navy lines"><span class="fade sm">1924 quota law limited Jewish immigration; the <i>St.&nbsp;Louis</i> turned away (937 refugees, 1939); Evian Conference (1938) failed.</span></div></div>
        <div class="mi-box"><div class="band gold sm">Why Doors Stayed Closed</div><div class="well tint-gold lines"><span class="fade sm">Anti&#8209;Semitism, isolationism, Depression&#8209;era economic fears, and security concerns; the War Refugee Board came only in 1944.</span></div></div>
        <div class="mi-box"><div class="band red sm">Liberating the Camps</div><div class="well tint-red lines"><span class="fade sm">U.S. forces freed Buchenwald, Dachau &amp; Mauthausen; soldiers documented the atrocities; footage shocked the public and aided the Nuremberg trials.</span></div></div>
        <div class="mi-box"><div class="band navy sm">After the War</div><div class="well tint-navy lines"><span class="fade sm">The Displaced Persons Act (1948) admitted about 205,000 people; survivors resettled in the U.S.</span></div></div>
      </div>
      <div class="mi-box" style="flex:0.82 1 0; min-height:0; margin-top:8px;">
        <div class="band gold sm">In one sentence, how would you describe the U.S. response to the Holocaust?</div>
        <div class="well cream lines"></div>
      </div>
    </div>
"""

_UDL = dict(
    scaffold="Fill the four boxes first using the faint hints, then infer the main idea together. Frame: &ldquo;Across all three phases, the U.S. response was ___.&rdquo;",
    extend="Historians debate whether the U.S. could have done more before 1944. Use the first two boxes to weigh that question with evidence.",
    show="Students may <b>write</b> the boxes, <b>say</b> the main idea aloud, or present it as a short <b>timeline</b>.")

ORGANIZERS = [
    dict(
        slug="22_us47_mainidea",
        title="The U.S. Response to the Holocaust",
        kicker="Unit 6 &middot; US.47 &middot; Best&#8209;Fit Organizer",
        chips=[("Main Idea &amp; Details", "navy"), ("DOK 2&#8211;3 &middot; Analyze", "skill")],
        why=("A main&#8209;idea organizer separates the <b>big idea</b> from the details that support it, so students can "
             "analyze a difficult history with care across its three phases. "
             "<span class='cite'>Summarizing and analyzing evidence are high&#8209;yield practices (SSP.01, SSP.02).</span>"),
        body=BODY, extra_css=CSS, udl=_UDL,
        role="Teacher Graphic Organizer Toolkit &middot; Unit 6 &middot; US.47 (labeled)",
    ),
]
