# -*- coding: utf-8 -*-
"""Unit 6 labeled best-fit organizers (GC.23-GC.27).
Best-fit: GC.23 Matrix (First Amendment cases), GC.24 Cause & Effect (Heller ->
McDonald), GC.25 Concept web (rights of the accused), GC.26 Timeline (14th
Amendment over time), GC.27 Main Idea & Details (expanding rights). Verbatim
case/statute topics; writable areas light.
"""
from common import matrix, cause_effect_chain, concept_web, timeline, main_idea

def _o(slug, title, kicker, chips, why, bc, udl, role, **kw):
    body, css = bc
    d = dict(slug=slug, title=title, kicker=kicker, chips=chips, why=why,
             body=body, extra_css=css, udl=udl, role=role); d.update(kw); return d

_SHOW = "Students may <b>write</b>, <b>say</b> (record), <b>draw</b>, or <b>build</b> their response."
def ROLE(std): return f"Teacher Graphic Organizer Toolkit &middot; Unit 6 &middot; {std} (labeled)"
def KICK(std): return f"Unit 6 &middot; {std} &middot; Best-Fit Organizer"

ORGANIZERS = [

  # GC.23 — First Amendment cases -> Matrix
  _o("20_gc23_matrix", "First Amendment Cases",
     KICK("GC.23"),
     [("Matrix &middot; Case &times; Ruling", "navy"), ("SSP.02 &middot; DOK 3", "skill")],
     "The First Amendment&rsquo;s meaning is built case by case. A matrix holds each landmark case to the same two "
     "questions, so the pattern of speech, press, and religion rights comes into focus. "
     "<span class='cite'>Comparing sources against one yardstick builds TN Practice SSP.02.</span>",
     matrix("For each case, name the freedom at issue and how the Court ruled.",
            [("SPEECH", "Tinker · Schenck · Texas v. Johnson", "navy"),
             ("RELIGION", "Engel · Lemon", "red"),
             ("PRESS", "NYT v. U.S.", "gold")],
            [("The freedom at issue", ["", "", ""]),
             ("How the Court ruled", ["", "", ""])],
            "<b>Pattern:</b> When may the government limit a First Amendment freedom &mdash; and when may it not? ______________________"),
     dict(scaffold="Give a card set of case names to sort under Speech / Religion / Press before writing.",
          extend="Explain the 'clear and present danger' test (Schenck) and how Tinker limited school authority.", show=_SHOW),
     ROLE("GC.23")),

  # GC.24 — Second Amendment -> Cause & Effect
  _o("21_gc24_causeeffect", "The Second Amendment in Two Cases",
     KICK("GC.24"),
     [("Cause &amp; Effect &middot; Chain", "red"), ("SSP.04 &middot; DOK 2", "skill")],
     "Two cases, two years apart, settled how the Second Amendment applies. Tracing the chain shows students how a "
     "right moves from the federal government to the states. "
     "<span class='cite'>Illustrating cause and effect builds TN Practice SSP.04.</span>",
     cause_effect_chain(
       "Work down the chain from the amendment&rsquo;s text to its reach today.",
       [("The text (1791)", "&mdash; &lsquo;the right of the people to keep and bear Arms&rsquo; &mdash; individual right, or militia right?"),
        ("District of Columbia v. Heller (2008)", "&mdash; what did the Court decide the amendment protects?"),
        ("McDonald v. Chicago (2010)", "&mdash; how did incorporation extend that right to the states?"),
        ("Today", "&mdash; the right is not unlimited &mdash; what regulation may still be allowed?")],
       tail=('<div class="midbar" style="margin-top:8px"><b>So what?</b> How did two rulings change where the Second Amendment '
             'applies? ____________________________________</div>')),
     dict(scaffold="Provide the two case names on cards; students place Heller then McDonald and add each effect.",
          extend="Honors: compare two states&rsquo; firearm laws and explain how each fits within Heller&rsquo;s limits.", show=_SHOW),
     ROLE("GC.24")),

  # GC.25 — Rights of the accused -> Concept web
  _o("22_gc25_conceptweb", "Rights of the Accused",
     KICK("GC.25"),
     [("Concept Web &middot; Connect Rights", "navy"), ("SSP.02 &middot; DOK 2", "skill")],
     "The 4th&ndash;8th Amendments protect anyone accused of a crime, and three landmark cases put them into practice. "
     "A concept web gathers these rights &mdash; and the case behind each &mdash; around one hub. "
     "<span class='cite'>Organizing rights and cases builds schema (SSP.02).</span>",
     concept_web("In each bubble, name a right of the accused and the case that secured it.",
                 "RIGHTS OF / THE ACCUSED",
                 ["4th — no illegal search (Mapp v. Ohio)", "5th — right to remain silent (Miranda)",
                  "6th — right to a lawyer (Gideon)", "6th — speedy, public trial",
                  "8th — no cruel & unusual punishment", "The exclusionary rule"]),
     dict(scaffold="Match each amendment to its landmark case (Mapp, Gideon, Miranda) together first.",
          extend="Explain the exclusionary rule (Mapp) and why some argue it &lsquo;shields the guilty.&rsquo;", show=_SHOW),
     ROLE("GC.25")),

  # GC.26 — 14th Amendment over time -> Timeline
  _o("23_gc26_timeline", "The 14th Amendment Over Time",
     KICK("GC.26"),
     [("Timeline &middot; Change Over Time", "red"), ("SSP.05 &middot; DOK 3", "skill")],
     "The same Equal Protection Clause has been read in opposite ways across a century. A timeline makes the reversal &mdash; "
     "and the expansion &mdash; impossible to miss. "
     "<span class='cite'>Identifying continuity and change over time is TN Practice SSP.05.</span>",
     timeline("Write each year on the left, then explain how the Court read the 14th Amendment.",
              [("1896", "Plessy v. Ferguson", "&mdash; &lsquo;separate but equal&rsquo; is allowed", False),
               ("1925", "Gitlow v. New York", "&mdash; incorporation begins (Bill of Rights &rarr; states)", False),
               ("1954", "Brown v. Board of Education", "&mdash; &lsquo;separate&hellip; inherently unequal&rsquo;", False),
               ("2015", "Obergefell v. Hodges", "&mdash; due process &amp; equal protection extend marriage", True)]),
     dict(scaffold="Give the four cases on cards; students order them on the spine, then add each ruling.",
          extend="Explain how the same clause could justify Plessy (1896) and Brown (1954) &mdash; how does meaning change?", show=_SHOW),
     ROLE("GC.26")),

  # GC.27 — Rights for the underserved -> Main Idea & Details
  _o("24_gc27_mainidea", "Widening the Circle of Rights",
     KICK("GC.27"),
     [("Main Idea &amp; Details", "navy"), ("SSP.03 &middot; DOK 2", "skill")],
     "Laws and cases extended rights to groups long left out. Separating the big idea &mdash; the &lsquo;expanding circle&rsquo; &mdash; "
     "from its examples helps students see civil rights as an ongoing project. "
     "<span class='cite'>Synthesizing multiple sources builds TN Practice SSP.03.</span>",
     main_idea(
       "Main idea: rights expanded to the underserved. Fill each column with what it did.",
       "THE EXPANDING CIRCLE OF RIGHTS",
       [("Title IX (1972)", "what did it end, and where?"),
        ("Americans with Disabilities Act (1990)", "who did it protect, and how?"),
        ("A court lesson (Korematsu, 1944)", "why is it a warning, not a model?")],
       "<b>In one sentence:</b> Did laws or court rulings do more to widen the circle of rights? ______________________________________________"),
     dict(scaffold="Give the three items as cards; students match each to the right column first.",
          extend="Connect one law here to the 14th Amendment&rsquo;s Equal Protection Clause you studied in GC.26.", show=_SHOW),
     ROLE("GC.27")),
]
