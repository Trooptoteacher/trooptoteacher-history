# -*- coding: utf-8 -*-
"""Unit 2 labeled best-fit organizers, one per standard GC.31-GC.34.
Topics drawn verbatim from the TN GC standards + instructional-guide targets.
Nothing invented; writable areas light; seeded prompts are questions.
Best-fit: GC.31 T-chart (legal vs. expected duties), GC.32 sequence (nomination
process), GC.33 cause & effect (media -> public opinion), GC.34 concept web
(ways to participate).
"""
from common import tchart, cause_effect_chain, cause_effect_split, concept_web

def _o(slug, title, kicker, chips, why, bc, udl, role, **kw):
    body, css = bc
    d = dict(slug=slug, title=title, kicker=kicker, chips=chips, why=why,
             body=body, extra_css=css, udl=udl, role=role)
    d.update(kw)
    return d

_SHOW = "Students may <b>write</b>, <b>say</b> (record), <b>draw</b>, or <b>build</b> their response."
def ROLE(std): return f"Teacher Graphic Organizer Toolkit &middot; Unit 2 &middot; {std} (labeled)"
def KICK(std): return f"Unit 2 &middot; {std} &middot; Best-Fit Organizer"

ORGANIZERS = [

  # GC.31 — Responsibilities of citizens -> T-chart (legal duty vs. expected)
  _o("20_gc31_tchart",
     "Responsibilities of Citizens",
     KICK("GC.31"),
     [("T&#8209;Chart &middot; Two Kinds of Duty", "navy"), ("DOK 2 &middot; Classify", "skill")],
     "Some civic duties are required by law; others are expected of a good citizen but not enforced. Sorting them "
     "shows students what a republic <em>demands</em> versus what it <em>depends on</em>. "
     "<span class='cite'>Collecting and organizing civic information builds TN Practice SSP.01.</span>",
     tchart("Sort each responsibility: is it a <b>legal duty</b> (required) or <b>expected</b> of a good citizen?",
            "LEGAL DUTIES", "required &mdash; enforced by law", "EXPECTED OF GOOD CITIZENS", "not required, but the republic needs it",
            [("Obey the law", "what happens if you don't?"),
             ("Pay taxes", "who is required, and why?"),
             ("Jury duty", "when are you legally summoned?")],
            [("Stay informed", "why did Jefferson say this matters?"),
             ("Vote", "a right and a responsibility &mdash; why?"),
             ("Volunteer / serve", "how does service strengthen the nation?")],
            "<b>Weigh it:</b> Which single responsibility matters most for the well-being of the nation &mdash; and why? ______________________"),
     dict(scaffold="Give the eight responsibilities on cards; students place each under Legal or Expected first.",
          extend="Pick one 'expected' responsibility and argue whether it should become a legal duty.",
          show=_SHOW),
     ROLE("GC.31")),

  # GC.32 — Nomination process -> sequence
  _o("21_gc32_sequence",
     "How a Candidate Is Nominated",
     KICK("GC.32"),
     [("Sequence &middot; Process Flow", "red"), ("SSP.05 &middot; DOK 2", "skill")],
     "A candidate can't reach the general election without first winning the party's nomination. Mapping the flow "
     "shows students how primaries, caucuses, and conventions fit together. "
     "<span class='cite'>Sequencing a process builds chronological reasoning (SSP.05).</span>",
     cause_effect_chain(
       "Work down the process. In each box, record how the step chooses or narrows the candidates.",
       [("PRIMARIES &amp; CAUCUSES",
         "&mdash; how do party members pick a favorite? (open vs. closed primary; caucus meeting)"),
        ("NATIONAL CONVENTION",
         "&mdash; how is the nominee made official, and what does the running mate add?"),
        ("GENERAL ELECTION",
         "&mdash; how do all voters &mdash; not just one party &mdash; now choose among the nominees?")],
       tail=('<div class="midbar" style="margin-top:8px"><b>Weigh it:</b> Washington warned against the &ldquo;spirit of party.&rdquo; '
             'Do parties help or hurt this process? ____________________________________</div>')),
     dict(scaffold="Provide the three stages on cards; students order them, then add how each narrows the field.",
          extend="Explain the difference between an open and a closed primary and why a party might prefer each.",
          show=_SHOW),
     ROLE("GC.32")),

  # GC.33 — Media & public opinion -> cause & effect
  _o("22_gc33_causeeffect",
     "How Media Shapes Public Opinion",
     KICK("GC.33"),
     [("Cause &amp; Effect", "red"), ("SSP.02 &middot; DOK 3", "skill")],
     "The media doesn't just report &mdash; by choosing what to cover and how to word it, it influences which issues seem "
     "important. Tracing that chain builds a citizen's guard against spin. "
     "<span class='cite'>Critically examining sources for purpose and bias is TN Practice SSP.02.</span>",
     cause_effect_split(
       "List what the media <b>does</b> on the left; list the <b>effect</b> on public opinion on the right.",
       "PUBLIC OPINION", "what people believe matters",
       "Story selection? Framing? Poll wording? Which voices are quoted?",
       "Which issues seem important? What do people come to believe?",
       "<b>Spot the bias:</b> Give one example of wording or framing that could push an audience toward a view. ______________________"),
     dict(scaffold="Model one cause&rarr;effect pair together (e.g., a loaded poll question &rarr; a skewed result).",
          extend="Compare two headlines about the same event and explain how each frames the story differently.",
          show=_SHOW),
     ROLE("GC.33")),

  # GC.34 — Means of participation -> concept web
  _o("23_gc34_conceptweb",
     "Ways Citizens Participate",
     KICK("GC.34"),
     [("Concept Web &middot; Connect Ideas", "navy"), ("SSP.04 &middot; DOK 2", "skill")],
     "Voting is only the beginning. A concept web gathers the many channels &mdash; protest, petition, lobbying, running "
     "for office, direct democracy &mdash; around one hub, so students see participation as a whole toolkit. "
     "<span class='cite'>Constructing and communicating civic action builds TN Practice SSP.04.</span>",
     concept_web("In each bubble, name a way citizens participate and give one real example.",
                 "WAYS CITIZENS / PARTICIPATE",
                 ["Vote", "Campaign", "Demonstrate", "Lobby", "Petition", "Run for office", "Initiative / Referendum / Recall"]),
     dict(scaffold="Fill two bubbles together (e.g., vote, petition) and model naming a real example for each.",
          extend="Rank the methods by how much power each gives an ordinary citizen, and defend your top choice.",
          show=_SHOW),
     ROLE("GC.34")),
]
