# -*- coding: utf-8 -*-
"""Unit 6 labeled best-fit organizer -- Main Idea & Details.
US.53: African Americans in WWII -- Second Great Migration & jobs, the Double V
campaign, military service, and the FEPC (EO 8802) -- hold up one main idea about
wartime gains that fed the coming civil rights movement. Seeded as faint hints.
HAS a Tennessee Connection. Content approved for US.53.
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
        <div class="well lines"><span class="fade">WWII opened new jobs and raised civil-rights consciousness for African Americans &mdash; laying groundwork for the postwar movement.</span></div>
      </div>
      <div class="mi-supports">&uarr;&nbsp; these four developments support the main idea &nbsp;&uarr;</div>
      <div class="mi-arrows">
        <div class="arr-u"></div><div class="arr-u"></div><div class="arr-u"></div><div class="arr-u"></div>
      </div>
      <div class="mi-details">
        <div class="mi-box"><div class="band navy sm">Migration &amp; Jobs</div><div class="well tint-navy lines"><span class="fade sm">1.5M moved North &amp; West (Detroit, Chicago, LA) for defense jobs; Black family income doubled &mdash; but discrimination persisted.</span></div></div>
        <div class="mi-box"><div class="band red sm">Double V Campaign</div><div class="well tint-red lines"><span class="fade sm">The <i>Pittsburgh Courier</i> called for victory over fascism <b>abroad</b> and racism <b>at home</b>; NAACP grew from 50,000 to 450,000.</span></div></div>
        <div class="mi-box"><div class="band gold sm">Military Service</div><div class="well tint-gold lines"><span class="fade sm">1 million served in segregated forces &mdash; fighting for democracy while facing prejudice, sharpening the contradiction.</span></div></div>
        <div class="mi-box"><div class="band navy sm">FEPC (EO 8802)</div><div class="well tint-navy lines"><span class="fade sm">A. Philip Randolph&rsquo;s threatened march pressured FDR to issue Executive Order 8802 (1941), creating the FEPC against job discrimination.</span></div></div>
      </div>
      <div class="mi-box" style="flex:0.82 1 0; min-height:0; margin-top:8px;">
        <div class="band gold sm">In one sentence, how did WWII move civil rights forward?</div>
        <div class="well cream lines"></div>
      </div>
      <div class="tnbox">
        <span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection &mdash;</b> African Americans in Tennessee contributed greatly despite
        segregation; the <b>FEPC</b> reached Tennessee war industries, and after the war <b>returning Black veterans</b>
        became leaders in Tennessee&rsquo;s civil rights movement.</span>
      </div>
    </div>
"""

_UDL = dict(
    scaffold="Fill the four detail boxes first using the faint hints, then infer the main idea together. Frame: &ldquo;All four of these show that ___.&rdquo;",
    extend="How did the <b>Double V</b> idea connect the war abroad to the fight at home? Defend your answer with evidence.",
    show="Students may <b>write</b> the boxes, <b>say</b> the main idea aloud, or <b>design</b> a Double V poster.")

ORGANIZERS = [
    dict(
        slug="28_us53_mainidea",
        title="Victory Abroad, the Fight at Home",
        kicker="Unit 6 &middot; US.53 &middot; Best&#8209;Fit Organizer",
        chips=[("Main Idea &amp; Details", "navy"), ("&#9733; Tennessee Connection", "gold"), ("DOK 2&#8211;3 &middot; Summarize", "skill")],
        why=("A main&#8209;idea organizer separates the <b>big idea</b> from the developments that support it, so students "
             "see how wartime change fed the coming civil rights movement. "
             "<span class='cite'>Summarizing &mdash; keep the main idea, cut the rest &mdash; is a high&#8209;yield "
             "comprehension strategy (Marzano).</span>"),
        body=BODY, extra_css=CSS, udl=_UDL,
        role="Teacher Graphic Organizer Toolkit &middot; Unit 6 &middot; US.53 (labeled)",
    ),
]
