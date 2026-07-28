# -*- coding: utf-8 -*-
"""Signature blank reproducible: Tennessee Connection (local <-> national + why it matters)."""

CSS = r"""
  .tnc{ flex:1 1 auto; display:flex; flex-direction:column; gap:9px; min-height:0; }
  .tnc .topic{ flex:0 0 auto; background:var(--cream); border:1.4px dashed var(--gold); border-radius:6px;
               padding:6px 11px; font-size:9.4pt; color:var(--navy); text-align:center; }
  .link{ flex:1 1 0; display:flex; gap:0; align-items:stretch; min-height:0; }
  .panel{ flex:1 1 0; display:flex; flex-direction:column; min-height:0; }
  .conn{ flex:0 0 78px; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:4px; }
  .conn .ring{ width:52px; height:52px; border-radius:50%; background:var(--gold-tint); border:2.5px solid var(--gold);
               display:flex; align-items:center; justify-content:center; color:#b8860b; font-size:20pt; line-height:1; }
  .conn .cap{ font-size:7.4pt; font-weight:800; letter-spacing:.05em; text-transform:uppercase; color:var(--muted); text-align:center; }
  .conn .ar{ font-size:15pt; color:var(--gold); line-height:.7; }
  .midband{ flex:0 0 auto; }
  .why2{ flex:0 0 auto; }
  .tnc .cue{ background:#fff; padding:1px 6px; border-radius:3px; }
"""

BODY = r"""
    <div class="prompt">Zoom in: link the <b>national</b> story to <b>Tennessee</b> &mdash; then say why the local story matters.</div>
    <div class="tnc">
      <div class="topic"><b>National topic / standard:</b> ____________________________________________________________________</div>
      <div class="link">
        <div class="panel">
          <div class="band navy sm">THE NATIONAL STORY</div>
          <div class="well navy lines" style="border-radius:0 0 6px 6px;"><div class="cue">what happened across the U.S.?</div></div>
        </div>
        <div class="conn">
          <div class="ar">&#9654;</div>
          <div class="ring">&#9733;</div>
          <div class="cap">connects&nbsp;to</div>
          <div class="ar" style="transform:rotate(180deg)">&#9654;</div>
        </div>
        <div class="panel">
          <div class="band gold sm">THE TENNESSEE STORY</div>
          <div class="well gold lines" style="border-radius:0 0 6px 6px;"><div class="cue">a TN person, place, or law</div></div>
        </div>
      </div>
      <div class="midband panel" style="flex:0 0 auto;">
        <div class="band red sm">THE LINK &mdash; how does the Tennessee story connect to the national one?</div>
        <div class="well red lines" style="border-radius:0 0 6px 6px; min-height:96px;"></div>
      </div>
      <div class="why2 panel" style="flex:0 0 auto;">
        <div class="band gold sm" style="background:var(--cream); color:var(--navy); border:1.5px solid var(--gold);">WHY THE LOCAL STORY MATTERS &mdash; why should Tennesseans know this?</div>
        <div class="well cream lines" style="border-radius:0 0 6px 6px; min-height:82px; border-color:var(--gold);"></div>
      </div>
    </div>
"""

ORGANIZERS = [dict(
    slug="16_tn_connection",
    title="Tennessee Connection",
    kicker="Reusable Organizer &middot; Our Signature Move",
    chips=[("Local &harr; National", "navy"), ("DOK 3 &middot; Connect", "skill")],
    why=("History sticks when it comes home. This organizer links a national event to a Tennessee person, place, or law &mdash; "
         "then asks students to argue why the local story matters. "
         "<span class='cite'>Relevance and personal connection drive engagement and retention (UDL 3.0).</span>"),
    body=BODY, extra_css=CSS, tn=True,
    udl=dict(
        scaffold="Provide the TN name/place and one national fact; students write only the <em>link</em> sentence: &ldquo;This connects because ___.&rdquo;",
        extend="Argue whether the Tennessee example is typical of the nation or an exception &mdash; and what that tells us.",
        show="Students may <b>write</b>, <b>say</b> the link aloud, <b>draw</b> a map line from TN to the nation, or <b>build</b> it as a matching pair."),
    role="Teacher Graphic Organizer Toolkit &middot; Blank Reproducible &middot; Signature",
)]
