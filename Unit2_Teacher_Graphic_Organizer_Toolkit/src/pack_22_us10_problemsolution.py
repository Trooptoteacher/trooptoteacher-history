# -*- coding: utf-8 -*-
"""Unit 2 labeled -- US.10 Farmers vs. the Railroads: Populism's Answer
(problem -> solution). Top red band states the problem over a LIGHT well seeded
with faint hints; a down-arrow leads to three LIGHT "Farmers' response" cards,
each with a small "result?" area; a final cream well asks students to judge the
outcome. Content approved for US.10 (Populism, the farmers' movement).
"""

CSS = r"""
  .ps-box{ display:flex; flex-direction:column; min-height:0; }
  .ps-box>.band{ flex:0 0 auto; }
  .ps-box>.well{ flex:1 1 0; }
  .seed{ padding:6px 11px; font-size:8.4pt; font-style:italic; color:#9aa2b2; line-height:1.25; }
  .seed b{ font-style:normal; font-weight:800; color:#8792a4; letter-spacing:.03em; text-transform:uppercase; font-size:7.4pt; }
  .ps-sols{ display:grid; grid-template-columns:repeat(3,1fr); gap:9px; flex:2 1 0; min-height:0; }
  .ps-sol{ display:flex; flex-direction:column; min-height:0; }
  .ps-sol .band.navy{ flex:0 0 auto; }
  .ps-sol .subcap{ flex:0 0 auto; background:var(--navy-tint); font-size:7.5pt; font-style:italic; color:#8792a4;
                   text-align:center; padding:3px 6px; line-height:1.12; }
  .ps-sol .sol-well{ flex:1.3 1 0; min-height:0; border-radius:0; }
  .ps-sol .band.tradelbl{ flex:0 0 auto; font-size:8pt; background:var(--gold); color:var(--navy);
                          border-radius:0; letter-spacing:.02em; }
  .ps-sol .trade-well{ flex:0.8 1 0; min-height:0; }
  .arr-lbl{ margin:1px 0 3px; }
  .tnbox{ flex:0 0 auto; margin-top:6px; background:var(--gold-tint); border:1.6px solid var(--gold); border-left:6px solid var(--gold);
          border-radius:0 6px 6px 0; padding:7px 12px; display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.8pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""

BODY = r"""
    <div class="prompt">Name the <b>problem</b> that squeezed farmers, map how they <b>organized in response</b> and what each move produced, then judge: did Populism <b>solve</b> it? Follow the arrows.</div>
    <div class="canvas">
      <div class="ps-box" style="flex:1.1 1 0; min-height:0;">
        <div class="band red sm">THE PROBLEM &mdash; what squeezed farmers?</div>
        <div class="well tint-red lines">
          <div class="seed"><b>Consider&nbsp;&middot;</b> railroad discrimination &amp; high freight rates &middot; mounting debt &middot; falling crop prices / deflation</div>
        </div>
      </div>
      <div class="arr-d"></div>
      <div class="arr-lbl">The farmers&rsquo; response</div>
      <div class="ps-sols">
        <div class="ps-sol">
          <div class="band navy sm">Organize</div>
          <div class="subcap">the Granger movement &middot; Farmers&rsquo; Alliance</div>
          <div class="well sol-well lines"></div>
          <div class="band sm tradelbl">Result?</div>
          <div class="well trade-well tint-gold lines"></div>
        </div>
        <div class="ps-sol">
          <div class="band navy sm">Populist demands</div>
          <div class="subcap">free silver &middot; regulate the railroads</div>
          <div class="well sol-well lines"></div>
          <div class="band sm tradelbl">Result?</div>
          <div class="well trade-well tint-gold lines"></div>
        </div>
        <div class="ps-sol">
          <div class="band navy sm">Politics</div>
          <div class="subcap">William Jennings Bryan &middot; &ldquo;Cross of Gold,&rdquo; 1896</div>
          <div class="well sol-well lines"></div>
          <div class="band sm tradelbl">Result?</div>
          <div class="well trade-well tint-gold lines"></div>
        </div>
      </div>
      <div class="arr-d"></div>
      <div class="arr-lbl">Judge the outcome</div>
      <div class="ps-box" style="flex:1 1 0; min-height:0;">
        <div class="band gold sm">Did Populism solve the farmers&rsquo; problems?</div>
        <div class="well cream lines">
          <div class="seed">___________ &nbsp;<b>because</b>&nbsp; _________________________________________________</div>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> The <b>Farmers&rsquo; Alliance</b> had strong chapters across rural
        Tennessee, organizing farmers here into the national movement.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="22_us10_problemsolution",
    title="Farmers vs. the Railroads: Populism&rsquo;s Answer",
    kicker="Unit 2 &middot; US.10 &middot; Best-Fit Organizer",
    chips=[("Problem &rarr; Solution", "navy"), ("DOK 3 &middot; Decision", "skill")],
    tn=True,
    why=("Use to <b>define the farmers&rsquo; problem</b>, weigh their organized solutions against what each "
         "produced, and <b>judge the outcome</b> with evidence. "
         "<span class='cite'>Construct &amp; communicate an argument with evidence (TN SSP.04).</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Fill the problem well together and give a starter: &ldquo;Farmers organized so that ___, which led to ___.&rdquo;",
        extend="Rank the three responses: which did the most to address the problem, and what did it leave unsolved?",
        show="Students may <b>write</b>, <b>say</b> (record), <b>draw</b> the flow, or <b>build</b> the responses with cards and vote."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 2 &middot; US.10 (labeled)",
)]
