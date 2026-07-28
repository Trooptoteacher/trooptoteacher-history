# -*- coding: utf-8 -*-
"""Unit 3 labeled best-fit organizer -- T-chart (weigh two sides of a debate).
US.27: Wilson's Fourteen Points & the League of Nations ratification debate.
       JOIN / Ratify (Wilson & internationalists) vs. REJECT (Lodge &
       reservationists). Arguments seeded as faint hints; students add more,
       then take a reasoned stance.
TN tie: Cordell Hull of Pickett County (gold callout).
Neutral framing: both sides presented as legitimate; the verdict is the
student's own reasoned stance.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .tc{ flex:1 1 auto; display:flex; flex-direction:column; gap:8px; min-height:0; }
  .ctx{ flex:0 0 auto; display:flex; flex-direction:column; }
  .ctx .band{ flex:0 0 auto; }
  .ctx .well{ flex:0 0 auto; padding:6px 12px; font-size:8.6pt; line-height:1.32; color:#2c3446; }
  .ctx .well b{ color:var(--navy); }
  .tc-cols{ flex:1 1 auto; display:flex; gap:12px; min-height:0; }
  .tc-col{ flex:1 1 0; display:flex; flex-direction:column; min-height:0; }
  .tc-col .band{ flex:0 0 auto; position:relative; }
  .tc-col .band small{ display:block; font-weight:600; font-size:8pt; opacity:.92; letter-spacing:0; text-transform:none; margin-top:1px; }
  .tc-col .well{ flex:1 1 0; min-height:0; }
  .fade{ position:absolute; top:8px; left:11px; right:11px; font-size:8.4pt; font-style:italic;
         color:#9aa4b4; line-height:1.5; }
  .tnbox{ flex:0 0 auto; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.7pt; line-height:1.32; color:#3a2f12; }
  .tnbox .t b{ color:#7a5c15; }
"""

BODY = r"""
    <div class="prompt">Weigh <b>both sides</b> of the debate over joining the League of Nations. Add reasons and evidence to each column &mdash; then take a reasoned stance of your own.</div>
    <div class="tc">
      <div class="ctx">
        <div class="band navy sm">Context &mdash; Wilson&rsquo;s Fourteen Points (1918)</div>
        <div class="well top" style="border-radius:0 0 6px 6px;">A peace plan built on <b>self&#8209;determination</b>, <b>free trade</b>, and <b>open diplomacy</b> &mdash; and <b>Point 14</b>, a <b>League of Nations</b> to keep peace through collective security.</div>
      </div>
      <div class="tc-cols">
        <div class="tc-col">
          <div class="band navy">JOIN &middot; RATIFY<small>Wilson &amp; the internationalists</small></div>
          <div class="well navy lines"><span class="fade">&bull;&nbsp; Collective security to help prevent future wars<br>&bull;&nbsp; U.S. moral leadership in the postwar world<br>&bull;&nbsp; Honor the peace settlement Wilson negotiated</span></div>
        </div>
        <div class="tc-col">
          <div class="band red">REJECT<small>Sen. Henry Cabot Lodge &amp; the reservationists</small></div>
          <div class="well red lines"><span class="fade">&bull;&nbsp; Article X could pull the U.S. into foreign wars<br>&bull;&nbsp; Protect Congress&rsquo;s power to declare war &amp; national sovereignty<br>&bull;&nbsp; Keep the tradition of avoiding &ldquo;entangling alliances&rdquo;</span></div>
        </div>
      </div>
      <div class="tc-col" style="flex:0.72 1 0; min-height:0;">
        <div class="band gold sm">What actually happened &middot; your stance</div>
        <div class="well cream lines"><span class="fade">The U.S. Senate rejected the Treaty of Versailles, and the United States never joined the League. Should it have? &mdash; My stance: __________ <b>because</b> __________</span></div>
      </div>
      <div class="tnbox">
        <span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection &mdash;</b> <b>Cordell Hull</b> of Pickett County, Tennessee &mdash; serving in Congress during the League debate &mdash;
        later championed international cooperation as Secretary of State and helped found the United Nations.</span>
      </div>
    </div>
"""

_UDL = dict(
    scaffold="Give a starter for each column: &ldquo;The U.S. should join because ___&rdquo; / &ldquo;The U.S. should stay out because ___.&rdquo; Fill one reason on each side together.",
    extend="Was rejecting the League a missed chance to prevent future war, or a wise choice to protect sovereignty? Defend either side with evidence.",
    show="Students may <b>write</b> reasons, <b>say</b> a stance aloud, <b>draw</b> a two&#8209;pan balance, or <b>debate</b> it in teams.")

ORGANIZERS = [
    dict(
        slug="28_us27_tchart",
        title="Should the U.S. Join the League of Nations?",
        kicker="Unit 3 &middot; US.27 &middot; Best&#8209;Fit Organizer",
        chips=[("T&#8209;Chart &middot; Weigh Two Sides", "navy"), ("&#9733; Tennessee Connection", "gold"), ("DOK 3 &middot; Argument", "skill")],
        why=("A T&#8209;chart forces a decision that rests on evidence from <b>both</b> sides of the ratification debate "
             "before students commit to a stance. "
             "<span class='cite'>Building an argument from competing claims and evidence is SSP.04; comparing "
             "similarities and differences is Marzano&rsquo;s highest&#8209;yield move.</span>"),
        body=BODY, extra_css=CSS, udl=_UDL,
        role="Teacher Graphic Organizer Toolkit &middot; Unit 3 &middot; US.27 (labeled)",
    ),
]
