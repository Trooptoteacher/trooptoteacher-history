# -*- coding: utf-8 -*-
"""Unit 10 labeled -- US.84 Social Activism & Counterculture (T-chart).
Two columns hold the two sides of the 1960s "generation gap": the older
establishment and the younger counterculture. Each side gets FADED viewpoint hints
and write-lines. A synthesis band asks why the two generations clashed. HAS a
Tennessee Connection. Content approved for US.84.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .tc2{ flex:1 1 auto; display:flex; gap:12px; min-height:0; }
  .tc2 .col{ flex:1 1 0; display:flex; flex-direction:column; min-height:0; }
  .tc2 .colhead{ color:#fff; font-weight:800; font-size:9.4pt; text-align:center; padding:6px 6px;
       border-radius:6px 6px 0 0; letter-spacing:.02em; flex:0 0 auto; }
  .tc2 .colhead.est{ background:var(--navy); } .tc2 .colhead.cnt{ background:var(--red); }
  .tc2 .colhead small{ display:block; font-weight:600; font-size:6.9pt; opacity:.9; margin-top:1px; }
  .tc2 .stack{ flex:1 1 auto; display:flex; flex-direction:column; gap:7px; padding-top:6px; min-height:0; }
  .card{ flex:1 1 0; position:relative; border:1.5px solid var(--rule); border-radius:6px; overflow:hidden;
       background-image:repeating-linear-gradient(to bottom, transparent 0 22px, var(--wl) 22px 23px);
       background-position:0 34px; padding:4px 9px 0; }
  .card.est{ background-color:var(--navy-tint); } .card.cnt{ background-color:#fbeeee; }
  .card .nm{ font-family:Georgia,serif; font-weight:700; font-size:8.9pt; color:var(--navy); line-height:1.05; }
  .card.cnt .nm{ color:#7c2a24; }
  .card .rl{ font-size:7.4pt; font-style:italic; color:#9aa4b4; line-height:1.22; margin-top:1px; }
  .synthbox{ flex:0 0 auto; margin-top:8px; display:flex; flex-direction:column; }
  .synthbox .well{ min-height:50px; position:relative; }
  .synthbox .fh{ position:absolute; top:6px; left:11px; right:11px; font-size:7.9pt; font-style:italic;
             color:#9aa6bd; line-height:1.34; }
  .tnbox{ flex:0 0 auto; margin-top:7px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.5pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""

def _card(kind, nm, rl):
    return (f'<div class="card {kind}"><div class="nm">{nm}</div>'
            f'<div class="rl">{rl}</div></div>')

_est = [
    ("Shaped by hard times", "grew up through the Depression &amp; World War II &mdash; valued sacrifice &amp; duty"),
    ("Trust in authority", "respected institutions, tradition &amp; the government they had built and defended"),
    ("Critics of protest", "saw many protesters as unpatriotic radicals hurting the country &amp; the troops"),
]
_cnt = [
    ("Raised in prosperity", "grew up in postwar comfort &mdash; freer to question the world their parents made"),
    ("Question authority", "challenged traditional values, the Vietnam War &amp; &ldquo;the establishment&rdquo;"),
    ("Hippies &amp; Woodstock", "rejected materialism; embraced peace, music &amp; community (Woodstock, 1969)"),
]

_est_html = "\n          ".join(_card("est", n, r) for n, r in _est)
_cnt_html = "\n          ".join(_card("cnt", n, r) for n, r in _cnt)

BODY = f"""
    <div class="prompt">Each side of the 1960s &ldquo;generation gap&rdquo; had its own view of activism and authority. On each card, write what that side <b>believed</b> &mdash; the faint notes are starters. Then answer the band below.</div>
    <div class="canvas">
      <div class="tc2">
        <div class="col">
          <div class="colhead est">THE ESTABLISHMENT<small>the older generation</small></div>
          <div class="stack">
            {_est_html}
          </div>
        </div>
        <div class="col">
          <div class="colhead cnt">THE COUNTERCULTURE<small>the younger generation</small></div>
          <div class="stack">
            {_cnt_html}
          </div>
        </div>
      </div>
      <div class="synthbox">
        <div class="band navy sm">Why did the two generations <b>clash</b> so sharply in the 1960s?</div>
        <div class="well cream lines">
          <span class="fh">Different life experiences (Depression &amp; war vs. postwar plenty) led to opposite views of patriotism, authority, and how much America needed to change</span>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Tennessee felt these currents its own way: <b>Nashville&rsquo;s</b> music scene
        absorbed countercultural influences, <b>Vanderbilt University</b> became a center of student activism, and the
        <b>Highlander</b> center kept training social&#8209;justice organizers.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="21_us84_tchart",
    title="The Generation Gap",
    kicker="Unit 10 &middot; US.84 &middot; Best&#8209;Fit Organizer",
    chips=[("T&#8209;Chart &middot; Two Sides", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2&#8211;3 &middot; Compare", "skill")],
    why=("A two&#8209;column chart sets the generations side by side, so students see the &ldquo;gap&rdquo; as two worldviews "
         "shaped by two very different histories &mdash; not just old vs. young. "
         "<span class='cite'>Identifying similarities &amp; differences is Marzano&rsquo;s #1 strategy.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Fill one card on each side together, using the faint notes. Ask: what did each side fear losing?",
        extend="Was the counterculture a healthy challenge or a threat to American values? Argue with evidence from both columns.",
        show="Students may <b>write</b> the cards, <b>say</b> a side&rsquo;s view aloud, or <b>design</b> a 1960s protest or pro&#8209;tradition poster."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 10 &middot; US.84 (labeled)",
)]
