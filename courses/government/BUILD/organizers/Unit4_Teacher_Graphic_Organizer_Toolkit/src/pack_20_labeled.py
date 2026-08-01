# -*- coding: utf-8 -*-
"""Unit 4 labeled best-fit organizers (GC.16-GC.18).
Topics verbatim from the TN GC standards. Best-fit: GC.16 Concept web (the roles
of the President), GC.17 Matrix (department x duty), GC.18 T-chart (arguments
for vs. against the Electoral College). Writable areas light.
"""
from common import concept_web, matrix, tchart

def _o(slug, title, kicker, chips, why, bc, udl, role, **kw):
    body, css = bc
    d = dict(slug=slug, title=title, kicker=kicker, chips=chips, why=why,
             body=body, extra_css=css, udl=udl, role=role); d.update(kw); return d

_SHOW = "Students may <b>write</b>, <b>say</b> (record), <b>draw</b>, or <b>build</b> their response."
def ROLE(std): return f"Teacher Graphic Organizer Toolkit &middot; Unit 4 &middot; {std} (labeled)"
def KICK(std): return f"Unit 4 &middot; {std} &middot; Best-Fit Organizer"

ORGANIZERS = [

  # GC.16 — roles of the President -> Concept web
  _o("20_gc16_conceptweb", "The Many Hats of the President",
     KICK("GC.16"),
     [("Concept Web &middot; Connect Roles", "navy"), ("DOK 2 &middot; Organize", "skill")],
     "Article II packs many jobs into one office. A concept web gathers the President&rsquo;s roles around a single hub, so "
     "students see how much &mdash; and how many kinds of &mdash; power the office holds. "
     "<span class='cite'>Organizing ideas around a hub builds schema (SSP.01).</span>",
     concept_web("In each bubble, name what the President does in that role &mdash; and one check on it.",
                 "THE / PRESIDENT",
                 ["Commander-in-Chief", "Chief Executive", "Chief Diplomat", "Chief of State",
                  "Chief Administrator", "Chief Legislator", "Chief Citizen", "Chief of Party"]),
     dict(scaffold="Match three roles to real actions together (e.g., Commander-in-Chief &rarr; directs the military) before students finish.",
          extend="For two roles, name the constitutional check that limits the President&rsquo;s power in that role.", show=_SHOW),
     ROLE("GC.16")),

  # GC.17 — departments -> Matrix
  _o("21_gc17_matrix", "The Executive Departments",
     KICK("GC.17"),
     [("Matrix &middot; Department &times; Duty", "navy"), ("DOK 2 &middot; Classify", "skill")],
     "The President cannot execute the law alone. A matrix lines up the major departments against the same questions so "
     "students can see who does what. "
     "<span class='cite'>Holding cases to one yardstick is Marzano&rsquo;s highest-yield strategy.</span>",
     matrix("For each department, name what it does and a real problem it would handle.",
            [("STATE", "foreign policy", "navy"), ("TREASURY", "money", "red"), ("DEFENSE", "military", "gold")],
            [("What it does", ["", "", ""]), ("A problem it handles", ["", "", ""])],
            "<b>Add two more:</b> Justice and Education &mdash; what does each do? ______________________________________________"),
     dict(scaffold="Pre-fill the State column together; students complete Treasury and Defense, then add Justice &amp; Education.",
          extend="Explain the 'iron triangle' among a department, a congressional committee, and interest groups.", show=_SHOW),
     ROLE("GC.17")),

  # GC.18 — Electoral College for/against -> T-chart
  _o("22_gc18_tchart", "The Electoral College &mdash; For &amp; Against",
     KICK("GC.18"),
     [("T&#8209;Chart &middot; Weigh Two Sides", "navy"), ("SSP.04 &middot; DOK 3", "skill")],
     "The standard asks students to weigh the Electoral College, not just describe it. A T&#8209;chart forces evidence on "
     "both sides before a verdict &mdash; exactly the argument the country keeps having. "
     "<span class='cite'>Constructing arguments from both sides builds TN Practice SSP.04.</span>",
     tchart("Gather the strongest evidence for each side, then decide.",
            "ARGUMENTS FOR", "keep the Electoral College", "ARGUMENTS AGAINST", "reform or replace it",
            [("Protects smaller states", "how does it give small states a voice?"),
             ("Forces national campaigns", "why campaign in many states, not just big cities?"),
             ("Federalism", "how does it fit a system of states?")],
            [("Popular vote can lose", "why is a popular-vote/electoral split a problem?"),
             ("Swing states dominate", "why do a few states get most attention?"),
             ("One person, one vote?", "does every vote count equally?")],
            "<b>Your verdict:</b> Keep, reform, or replace the Electoral College &mdash; <b>because</b> ____________________________________"),
     dict(scaffold="Sort a set of claim cards into FOR and AGAINST before writing.",
          extend="Honors: research one reform (direct election, proportional allocation, the National Popular Vote compact) and evaluate it.",
          show=_SHOW),
     ROLE("GC.18")),
]
