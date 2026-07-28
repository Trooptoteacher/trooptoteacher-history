# -*- coding: utf-8 -*-
"""Unit 7 labeled -- US.61 Second Red Scare & McCarthyism (cause & effect).
Cold War events feed the center EVENT (the Second Red Scare); four EFFECTS --
McCarthyism, blacklisting, the Army-McCarthy hearings, the Rosenbergs -- flow out
to the right. LIGHT wells with faded hints. Neutral framing: fears and abuses both
named as facts. HAS a Tennessee Connection. Content approved for US.61.
"""

CSS = r"""
  .chip.gold{ background:var(--gold); color:var(--navy); }
  .ce-grid{ flex:1 1 auto; display:flex; align-items:stretch; gap:5px; min-height:0; }
  .ce-col{ flex:1 1 0; display:flex; flex-direction:column; min-height:0; }
  .ce-colhead{ font-size:8.6pt; font-weight:800; letter-spacing:.05em; text-transform:uppercase;
               text-align:center; margin-bottom:5px; flex:0 0 auto; }
  .ce-stack{ flex:1 1 auto; display:flex; flex-direction:column; gap:9px; min-height:0; }
  .cebox{ flex:1 1 0; display:flex; flex-direction:column; min-height:0; }
  .cebox .band{ border-radius:6px 6px 0 0; font-size:8.3pt; padding:5px 8px; line-height:1.15; }
  .cebox .band .yr{ color:var(--gold); font-weight:800; }
  .cebox.red .band .yr{ color:#f6d9a6; }
  .cebox .well{ flex:1 1 0; }
  .ce-arrs{ flex:0 0 24px; display:flex; flex-direction:column; justify-content:space-around;
            align-items:center; padding:22px 0; }
  .ce-arrs .arr-r{ border-left-width:16px; border-top-width:11px; border-bottom-width:11px; }
  .ce-arrs.out .arr-r{ border-left-color:var(--red); }
  .ce-center{ flex:1.24 1 0; display:flex; flex-direction:column; justify-content:center; min-height:0; }
  .ce-center .band{ font-size:10.4pt; padding:8px; border-radius:7px 7px 0 0; line-height:1.12; }
  .ce-center .band .yr{ color:var(--gold); font-weight:800; }
  .ce-center .well{ flex:1 1 0; }
  .ce-center .cue{ color:#aab3c4; font-style:italic; text-transform:none; letter-spacing:0;
                   font-weight:600; font-size:8pt; }
  .tnbox{ flex:0 0 auto; margin-top:8px; background:var(--gold-tint); border:1.6px solid var(--gold);
          border-left:6px solid var(--gold); border-radius:0 6px 6px 0; padding:7px 12px;
          display:flex; gap:10px; align-items:flex-start; }
  .tnbox .star{ color:#b8860b; font-size:14pt; line-height:1; flex:0 0 auto; }
  .tnbox .t{ font-size:8.7pt; line-height:1.3; color:#3a2f12; } .tnbox .t b{ color:#7a5c15; }
"""

def _cause_box(label):
    return (f'<div class="cebox"><div class="band navy sm">{label}</div>'
            f'<div class="well navy lines"></div></div>')

def _effect_box(label):
    return (f'<div class="cebox red"><div class="band red sm">{label}</div>'
            f'<div class="well red lines"></div></div>')

_causes = [
    "Soviet nuclear bomb <span class=\"yr\">(1949)</span> &amp; communist victory in China <span class=\"yr\">(1949)</span>",
    "The Korean War <span class=\"yr\">(1950&ndash;53)</span> &mdash; communism on the march",
    "Real spy cases &mdash; the Rosenbergs &amp; Alger Hiss",
]
_effects = [
    "<b>McCarthyism</b> &mdash; Sen. McCarthy&rsquo;s accusations spread paranoia",
    "<b>Blacklisting</b> &mdash; the Hollywood Ten; HUAC destroys careers",
    "Army&ndash;McCarthy hearings <span class=\"yr\">(1954)</span>: &ldquo;Have you no sense of decency?&rdquo;",
    "The Rosenbergs executed <span class=\"yr\">(1953)</span>; a climate of fear",
]

_causes_html = "\n            ".join(_cause_box(c) for c in _causes)
_effects_html = "\n            ".join(_effect_box(e) for e in _effects)

BODY = f"""
    <div class="prompt">Real Cold War fears sit on the <b>left</b>; four <b>effects</b> flow out on the <b>right</b>. Arrows show the chain: <b>fear &rarr; the Red Scare &rarr; effects</b>. Watch how genuine fear became overreach.</div>
    <div class="canvas">
      <div class="ce-grid">
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--navy);">Causes &middot; what fueled the fear</div>
          <div class="ce-stack">
            {_causes_html}
          </div>
        </div>
        <div class="ce-arrs"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-center">
          <div class="ce-colhead" style="color:var(--navy);">The event</div>
          <div class="cebox" style="flex:1 1 0;">
            <div class="band navy">THE SECOND RED SCARE, <span class="yr">1947&ndash;54</span></div>
            <div class="well lines cream"><span class="cue" style="position:absolute;top:7px;left:11px;right:11px;">Fear of communist infiltration at home &mdash; describe the mood of the era</span></div>
          </div>
        </div>
        <div class="ce-arrs out"><div class="arr-r"></div><div class="arr-r"></div><div class="arr-r"></div></div>
        <div class="ce-col">
          <div class="ce-colhead" style="color:var(--red);">Effects &middot; fear becomes overreach</div>
          <div class="ce-stack">
            {_effects_html}
          </div>
        </div>
      </div>
      <div class="tnbox"><span class="star">&#9733;</span>
        <span class="t"><b>Tennessee Connection.</b> Tennessee&rsquo;s <b>Senator Estes Kefauver</b> gained national fame
        through <b>televised hearings on organized crime (1950&ndash;51)</b> &mdash; showing, in the same era as McCarthy, how
        <b>television</b> could turn a Senate hearing into a national spectacle.</span></div>
    </div>
"""

ORGANIZERS = [dict(
    slug="22_us61_causeeffect",
    title="When Fear Became a Witch Hunt",
    kicker="Unit 7 &middot; US.61 &middot; Best&#8209;Fit Organizer",
    chips=[("Cause &amp; Effect", "navy"), ("&#9733; Tennessee Connection", "gold"),
           ("DOK 2&#8211;3 &middot; Causation", "skill")],
    why=("Reading it as <b>fear &rarr; Red Scare &rarr; effects</b> shows how <b>real</b> security concerns hardened into "
         "accusations, blacklists, and abuses of civil liberties. "
         "<span class='cite'>Analyzing cause &amp; effect is TN Social Studies Practice SSP.05.</span>"),
    body=BODY,
    extra_css=CSS,
    udl=dict(
        scaffold="Fill the center box first. Then sort the causes: which were <b>real</b> threats, and which fed <b>exaggerated</b> fear?",
        extend="Where is the line between security and overreach? Use the effects to argue when the Red Scare crossed it.",
        show="Students may <b>write</b>, <b>say</b> (record), or <b>diagram</b> how fear turned into a witch hunt."),
    role="Teacher Graphic Organizer Toolkit &middot; Unit 7 &middot; US.61 (labeled)",
)]
