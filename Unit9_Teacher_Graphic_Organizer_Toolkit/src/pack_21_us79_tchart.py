# -*- coding: utf-8 -*-
"""Unit 9 labeled -- US.79 Civil Rights Advocates & Opponents (T-chart).
Two columns hold the era's advocates and its opponents, each a named figure with a
FADED role hint and write-lines. A synthesis band asks how the two sides coincided,
confronted, and challenged each other. Factual framing of both. HAS a Tennessee
Connection. Content approved for US.79.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .tc2{ flex:1 1 auto; display:flex; gap:12px; min-height:0; }
  .tc2 .col{ flex:1 1 0; display:flex; flex-direction:column; min-height:0; }
  .tc2 .colhead{ color:#fff; font-weight:800; font-size:9.5pt; text-align:center; padding:6px 6px;
       border-radius:6px 6px 0 0; letter-spacing:.02em; flex:0 0 auto; }
  .tc2 .colhead.adv{ background:var(--navy); } .tc2 .colhead.opp{ background:var(--red); }
  .tc2 .colhead small{ display:block; font-weight:600; font-size:6.9pt; opacity:.9; margin-top:1px; }
  .tc2 .stack{ flex:1 1 auto; display:flex; flex-direction:column; gap:6px; padding-top:6px; min-height:0; }
  .card{ flex:1 1 0; position:relative; border:1.5px solid var(--rule); border-radius:6px; overflow:hidden;
       background-image:repeating-linear-gradient(to bottom, transparent 0 22px, var(--wl) 22px 23px);
       background-position:0 40px; padding:4px 8px 0; }
  .card.adv{ background-color:var(--navy-tint); } .card.opp{ background-color:#fbeeee; }
  .card .nm{ font-family:Georgia,serif; font-weight:700; font-size:9.4pt; color:var(--navy); line-height:1.05; }
  .card.opp .nm{ color:#7c2a24; }
  .card .rl{ font-size:7.3pt; font-style:italic; color:#9aa4b4; line-height:1.16; margin-top:1px; }
  .synthbox{ flex:0 0 auto; margin-top:8px; display:flex; flex-direction:column; }
  .synthbox .well{ min-height:52px; position:relative; }
  .synthbox .fh{ position:absolute; top:6px; left:11px; right:11px; font-size:7.9pt; font-style:italic;
             color:#9aa6bd; line-height:1.34; }
  .tnbox{ flex:0 0 auto; margin-top:7px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.6pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""

def _card(kind, nm, rl):
    return (f'<div class="card {kind}"><div class="nm">{nm}</div>'
            f'<div class="rl">{rl}</div></div>')

_adv = [
    ("Dr. Martin Luther King Jr.", "nonviolence; the Montgomery Bus Boycott; the SCLC; &ldquo;I Have a Dream&rdquo;"),
    ("Rosa Parks", "sparked the Montgomery Bus Boycott &mdash; a symbol of quiet dignity"),
    ("Thurgood Marshall", "NAACP counsel; argued <i>Brown</i>; first Black Supreme Court Justice"),
    ("Malcolm X", "Black nationalism, then a broader human&#8209;rights view after Mecca"),
]
_opp = [
    ("Bull Connor", "Birmingham official; turned fire hoses &amp; dogs on peaceful protesters &mdash; it backfired"),
    ("Orval Faubus", "Arkansas governor; used the National Guard to block the Little Rock Nine"),
    ("Strom Thurmond", "led the 1948 &ldquo;Dixiecrat&rdquo; revolt; filibustered the 1957 Civil Rights Act 24+ hours"),
]

_adv_html = "\n          ".join(_card("adv", n, r) for n, r in _adv)
_opp_html = "\n          ".join(_card("opp", n, r) for n, r in _opp)

BODY = f"""
    <div class="prompt">On each card, write what that person <b>did</b> and the <b>approach</b> they used &mdash; the faint role notes are starters. Then answer the band below: how did the two sides confront and change each other?</div>
    <div class="canvas">
      <div class="tc2">
        <div class="col">
          <div class="colhead adv">ADVOCATES<small>working to advance civil rights</small></div>
          <div class="stack">
            {_adv_html}
          </div>
        </div>
        <div class="col">
          <div class="colhead opp">OPPONENTS<small>working to resist or delay them</small></div>
          <div class="stack">
            {_opp_html}
          </div>
        </div>
      </div>
      <div class="synthbox">
        <div class="band navy sm">How did advocates and opponents <b>coincide, confront, and challenge</b> each other?</div>
        <div class="well cream lines">
          <span class="fh">Advocates paired courtroom wins (Marshall) with mass protest (King) &nbsp;&middot;&nbsp; and violent resistance, shown on TV, often won the movement more public sympathy</span>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> The <b>Highlander Folk School</b> in Monteagle, Tennessee, trained
        civil rights leaders &mdash; including <b>Rosa Parks</b> and <b>Dr. King</b> &mdash; in the strategies of nonviolent resistance.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="21_us79_tchart",
    title="Two Sides of a Struggle",
    kicker="Unit 9 &middot; US.79 &middot; Best&#8209;Fit Organizer",
    chips=[("T&#8209;Chart &middot; Two Sides", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2&#8211;3 &middot; Compare", "skill")],
    why=("A two&#8209;column chart sets advocates and opponents side by side, so students see not just who each was but "
         "how their actions collided and moved history. "
         "<span class='cite'>Identifying similarities &amp; differences is Marzano&rsquo;s #1 strategy; SSP.06 examine.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Fill one advocate and one opponent together first, using the faint role notes.",
        extend="Advocates disagreed on <b>approach</b> (King&rsquo;s nonviolence vs. Malcolm X&rsquo;s self&#8209;defense). Explain how both moved the movement.",
        show="Students may <b>write</b> the cards, <b>say</b> a figure&rsquo;s story aloud, or <b>match</b> names to actions."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 9 &middot; US.79 (labeled)",
)]
