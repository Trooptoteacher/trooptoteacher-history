# -*- coding: utf-8 -*-
"""Unit 1 (US.01–US.07) — single source of truth for the Course Standard Platinum build.

Every value here is transcribed from the VERIFIED Drive source decks
(Teacher = full, Student/Lean = lean), read via the Drive connector's text
representation. No facts invented. Primary-source quotes/citations live in the
Student-deck source text (source_text/) and are pulled by the deck builder.

DOK / CFU answer keys are the ORIGINAL keys from the Teacher deck. `target_pos`
is the DE-BIASED position the correct answer is moved to, applied IN SYNC across
the Student PROGRESS CHECK, Teacher CFU, and ANSWER REVEAL (platinum requirement).
Original keys were A,A,A,C,A,C,B (heavily A-biased); de-biased spread is
B,D,C,A,D,B,A.
"""

UNIT = {
    "code": "Unit 1",
    "title": "The Rise of Industrialization (1877–1900)",
    "standards_range": "US.01–US.07",
    "publisher": "TroopToTeacher Technologies LLC",
    "footer": "U.S. History Hack · TroopToTeacher Technologies LLC · Aligned to TN Academic Standards & TCAP EOC",
}

# ---- Per-standard metadata (title + TN standard text + I CAN) ----
STANDARDS = {
    "US.01": {
        "title": "Homestead Act and Transcontinental Railroad",
        "tn": "Explain how the Homestead Act and the Transcontinental Railroad impacted the settlement of the West. (C, E, G, H, P)",
        "ican": "I can explain how the Homestead Act and the Transcontinental Railroad impacted the settlement of the West.",
    },
    "US.02": {
        "title": "Federal Policies Toward American Indians",
        "tn": "Examine federal policies toward American Indians, including the movement to reservations, assimilation, boarding schools, and the Dawes Act. (C, G, H, P, T)",
        "ican": "I can examine federal policies toward American Indians, including the movement to reservations, assimilation, boarding schools, and the Dawes Act.",
    },
    "US.03": {
        "title": "Compromise of 1877, Jim Crow & Plessy v. Ferguson",
        "tn": "Explain the impact of the Compromise of 1877, including Jim Crow laws, lynching, disenfranchisement methods, the efforts of Benjamin “Pap” Singleton and the Exodusters, and the Plessy v. Ferguson decision. (C, G, H, P, T, TCA) (T.C.A. § 49-6-1006)",
        "ican": "I can explain the impact of the Compromise of 1877, including Jim Crow laws, lynching, disenfranchisement methods, the efforts of Benjamin “Pap” Singleton and the Exodusters, and the Plessy v. Ferguson decision.",
    },
    "US.04": {
        "title": "Gilded Age Politics and Economics",
        "tn": "Analyze the causes and consequences of Gilded Age politics and economics as well as the significance of the rise of political machines, major scandals, civil service reform, and the economic difference between farmers, wage earners, and industrial capitalists, including the following: Boss Tweed, Thomas Nast, Credit Mobilier, Spoils system and President James A. Garfield’s assassination, Pendleton Act, Interstate Commerce Act. (C, E, G, H, P)",
        "ican": "I can analyze the causes and consequences of Gilded Age politics and economics as well as the significance of the rise of political machines, major scandals, civil service reform, and the economic difference between farmers, wage earners, and industrial capitalists, including the following: Boss Tweed, Thomas Nast, Credit Mobilier, Spoils system and President James A. Garfield’s assassination, Pendleton Act, Interstate Commerce Act.",
    },
    "US.05": {
        "title": "Inventions & Innovations of Business Leaders & Entrepreneurs",
        "tn": "Describe the changes in American life that resulted from the inventions and innovations of business leaders and entrepreneurs of the period, including the significance of: Alexander Graham Bell, Henry Bessemer, Andrew Carnegie, Thomas Edison, J.P. Morgan, John D. Rockefeller, Nikola Tesla, Cornelius Vanderbilt, Madam C.J. Walker, George Washington Carver. (C, E, H)",
        "ican": "I can describe the changes in American life that resulted from the inventions and innovations of business leaders and entrepreneurs of the period, including the significance of: Alexander Graham Bell, Henry Bessemer, Andrew Carnegie, Thomas Edison, J.P. Morgan, John D. Rockefeller, Nikola Tesla, Cornelius Vanderbilt, Madam C.J. Walker, George Washington Carver.",
    },
    "US.06": {
        "title": "Industrial Centers and Urbanization",
        "tn": "Locate the following major industrial centers, and describe how industrialization influenced the movement of people from rural to urban areas: Boston, Chicago, New York City, Pittsburgh, San Francisco. (C, E, G, H)",
        "ican": "I can locate the following major industrial centers, and describe how industrialization influenced the movement of people from rural to urban areas: Boston, Chicago, New York City, Pittsburgh, San Francisco.",
    },
    "US.07": {
        "title": "Immigration: Old vs. New Immigrants",
        "tn": "Describe the differences between “old” and “new” immigrants, analyze the assimilation process for “new” immigrants, and determine the impacts of increased migration on American society, including: Angel Island, Ellis Island, Push and pull factors, Ethnic clusters, Jane Addams, Competition for jobs, Rise of nativism, Jacob Riis, Chinese Exclusion Act and Gentleman’s Agreement. (C, E, G, H, P)",
        "ican": "I can describe the differences between “old” and “new” immigrants, analyze the assimilation process for “new” immigrants, and determine the impacts of increased migration on American society, including: Angel Island, Ellis Island, Push and pull factors, Ethnic clusters, Jane Addams, Competition for jobs, Rise of nativism, Jacob Riis, Chinese Exclusion Act and Gentleman’s Agreement.",
    },
}

# ---- Word Wall vocabulary (Teacher-deck verified: term / pronunciation / Spanish / definition) ----
VOCAB = {
    "US.01": [
        ("Homestead Act", "HOHM-sted", "Ley de Homestead",
         "An 1862 law that provided 160 acres of public land to settlers who agreed to live on and improve the land for five years, encouraging westward expansion."),
        ("Transcontinental Railroad", "tranz-kon-tih-NEN-tul RAYL-rohd", "Ferrocarril Transcontinental",
         "A continuous railroad line completed in 1869 that connected the eastern United States with the Pacific coast, revolutionizing transportation and commerce."),
        ("Westward Expansion", "WEST-werd ek-SPAN-shun", "Expansión hacia el Oeste",
         "The 19th-century movement of settlers, railroads, and U.S. authority across the continent toward the Pacific, encouraged by free land and new transportation."),
    ],
    "US.02": [
        ("Reservation System", "rez-er-VAY-shun SIS-tum", "Sistema de Reservaciones",
         "Federal policy that confined Native American tribes to designated areas of land, often far from their ancestral territories, to control indigenous populations and open land for white settlement."),
        ("Assimilation", "uh-sim-ih-LAY-shun", "Asimilación",
         "Federal policy aimed at forcing Native Americans to abandon their traditional cultures and adopt European-American ways of life, including language, religion, and customs."),
        ("Dawes Act", "DAWZ", "Ley Dawes",
         "An 1887 law that divided tribal lands into individual allotments, aiming to break up reservations and assimilate Native Americans; it resulted in massive Native land loss."),
    ],
    "US.03": [
        ("Compromise of 1877", "KOM-pruh-myz", "Compromiso de 1877",
         "An informal agreement resolving the disputed 1876 election: Rutherford B. Hayes became president in exchange for removing federal troops from the South, effectively ending Reconstruction."),
        ("Jim Crow Laws", "jim kroh", "Leyes de Jim Crow",
         "State and local laws enacted primarily in the South between 1877 and the 1960s that enforced racial segregation and denied African Americans their constitutional rights."),
        ("Disenfranchisement", "dis-en-FRAN-chyz-ment", "Privación del Derecho al Voto",
         "The systematic denial of voting rights through poll taxes, literacy tests, grandfather clauses, and violence, primarily targeting African American voters."),
    ],
    "US.04": [
        ("Gilded Age", "GIL-dud ayj", "Edad Dorada",
         "The period from roughly 1870 to 1900 of rapid growth, industrialization, and extreme wealth inequality — named by Mark Twain to suggest a thin gold layer over deep social problems."),
        ("Political Machines", "puh-LIT-ih-kul muh-SHEENZ", "Máquinas Políticas",
         "Corrupt organizations that controlled city politics through patronage, bribery, and vote manipulation, often trading services to immigrants for political support."),
        ("Spoils System", "spoylz SIS-tum", "Sistema de Botín",
         "The practice of rewarding political supporters with government jobs regardless of qualifications — 'to the victor belong the spoils.'"),
    ],
    "US.05": [
        ("Robber Barons / Captains of Industry", "ROB-er BAIR-unz", "Barones Ladrones / Capitanes de Industria",
         "Wealthy late-1800s industrialists who built massive business empires; critics called them 'robber barons,' supporters 'captains of industry.'"),
        ("Vertical Integration", "VUR-tih-kul in-teh-GRAY-shun", "Integración Vertical",
         "A business strategy where a company controls all stages of production, from raw materials to finished product — practiced by Andrew Carnegie in steel."),
        ("Horizontal Integration", "hor-ih-ZON-tul in-teh-GRAY-shun", "Integración Horizontal",
         "A business strategy where a company buys out competitors in the same industry to reduce competition and control prices — practiced by John D. Rockefeller in oil."),
    ],
    "US.06": [
        ("Urbanization", "ur-bun-ih-ZAY-shun", "Urbanización",
         "The rapid growth of cities due to industrialization and mass migration, transforming America from a predominantly rural to an urban society."),
        ("Granger Movement", "GRAYN-jer MOOV-ment", "Movimiento Granger",
         "A farmers' organization founded in 1867 that advocated railroad regulation and fought monopolistic practices that harmed farmers through high shipping rates."),
        ("Populism", "POP-yuh-liz-um", "Populismo",
         "An 1890s political movement of farmers and workers seeking railroad regulation, a graduated income tax, and free coinage of silver to combat economic inequality."),
    ],
    "US.07": [
        ("Old Immigrants", "ohld IM-ih-grunts", "Viejos Inmigrantes",
         "Immigrants who came primarily from Northern and Western Europe before 1880, often Protestant and more easily assimilated."),
        ("New Immigrants", "noo IM-ih-grunts", "Nuevos Inmigrantes",
         "Immigrants who came primarily from Southern and Eastern Europe and Asia after 1880, often Catholic, Jewish, or Orthodox, facing greater discrimination."),
        ("Ellis Island", "EL-is EYE-lund", "Isla Ellis",
         "The primary immigration processing station in New York Harbor from 1892 to 1954, where over 12 million immigrants — primarily Europeans — entered the United States."),
    ],
}

# ---- CFU / Progress-Check items (Teacher-deck verified). correct = ORIGINAL key letter.
#      target_pos = de-biased position (synced across student check + teacher CFU + reveal). ----
CFU = {
    "US.01": {
        "dok": 3, "correct": "A", "target_pos": "B",
        "stem": "A homesteading family and a Lakota family in 1875 would most likely have described the Homestead Act in very different ways. Which statement best explains why?",
        "options": {
            "A": "The same law that opened “free” land to settlers took that land away from American Indians who already lived on it.",
            "B": "The Homestead Act applied only to settlers and never affected American Indians in any way.",
            "C": "Both families received 160 acres each under the law, so their views would have matched.",
            "D": "The law was written to benefit American Indians first and settlers second.",
        },
        "why": "DOK 3: Students weigh competing perspectives. The Act’s “free” 160-acre grants to settlers came from land the federal government took from American Indian nations — opportunity for one group, dispossession for another.",
    },
    "US.02": {
        "dok": 2, "correct": "A", "target_pos": "D",
        "stem": "Based on the excerpt, what was the most likely long-term effect of dividing tribal land “in severalty” under the Dawes Act?",
        "options": {
            "A": "It broke up communal tribal ownership and led to large-scale Native land loss.",
            "B": "It strengthened tribal governments and expanded reservation territory.",
            "C": "It returned ancestral homelands to tribal control.",
            "D": "It had no measurable effect on Native landholding.",
        },
        "why": "DOK 2: The Act allotted land to individuals and declared the remainder “surplus” for sale, predictably dissolving collective tribal holdings and transferring tens of millions of acres out of Native hands.",
    },
    "US.03": {
        "dok": 3, "correct": "A", "target_pos": "C",
        "stem": "The Plessy majority reasoned that “separate” facilities did not make one race inferior. Which later argument most directly challenges that reasoning?",
        "options": {
            "A": "That state-enforced separation itself signals and enforces inequality, regardless of facility quality.",
            "B": "That segregation was acceptable as long as both facilities were physically identical.",
            "C": "That the Constitution explicitly required racial separation.",
            "D": "That African Americans had freely chosen separate facilities.",
        },
        "why": "DOK 3: Requires evaluating the Court’s logic. Harlan’s dissent — and later Brown v. Board (1954) — argued government-mandated separation is inherently unequal because the law itself brands a group as inferior.",
    },
    "US.04": {
        "dok": 2, "correct": "C", "target_pos": "A",
        "stem": "How does Bryce’s description of the political “Boss” help explain why the Pendleton Civil Service Reform Act was needed?",
        "options": {
            "A": "Both praise the political machines as honest and efficient.",
            "B": "Both argue that government jobs should be sold to the highest bidder.",
            "C": "Both reveal a spoils system in which offices and contracts were handed out for political loyalty, which reformers tried to end.",
            "D": "Both were written after the spoils system ended.",
        },
        "why": "DOK 2: Bryce describes the spoils system — bosses using offices and contracts to reward loyalty. The Pendleton Act attacked exactly this by requiring competitive exams; observer and reform law corroborate each other.",
    },
    "US.05": {
        "dok": 2, "correct": "A", "target_pos": "D",
        "stem": "A wealthy 1890s steel magnate funds free public libraries across the country instead of leaving his entire fortune to his heirs. Whose philosophy does this best reflect, and why?",
        "options": {
            "A": "Carnegie’s “Gospel of Wealth,” because surplus wealth is used as a trust to benefit society.",
            "B": "Carnegie’s philosophy, because it displays wealth publicly to impress others.",
            "C": "The opposite of Carnegie’s view, because he insisted fortunes pass to children.",
            "D": "The opposite of Carnegie’s view, because he opposed all charitable giving.",
        },
        "why": "DOK 2: Students apply the source to a new case. Carnegie argued the rich should live modestly and administer surplus wealth “as trust funds” for the public good — funding libraries is a textbook example of his Gospel of Wealth.",
    },
    "US.06": {
        "dok": 2, "correct": "C", "target_pos": "B",
        "stem": "A folk saying held that immigrants came expecting “streets paved with gold,” only to find the streets unpaved — and that they were expected to pave them. What does this reveal about the immigrant experience?",
        "options": {
            "A": "Immigrants found immediate wealth and success.",
            "B": "American cities were well-developed and welcoming.",
            "C": "Reality fell far short of expectations, and immigrants faced hard labor.",
            "D": "Immigrants were given skilled professional jobs.",
        },
        "why": "DOK 2: The saying contrasts the dream of “streets paved with gold” with the reality of unpaved streets immigrants themselves “were expected to pave,” highlighting difficult conditions.",
    },
    "US.07": {
        "dok": 2, "correct": "B", "target_pos": "A",
        "stem": "According to Jane Addams, what was the philosophy behind Hull-House?",
        "options": {
            "A": "That wealthy people should live separately from immigrants.",
            "B": "That different social classes depend on and can help each other.",
            "C": "That immigrants should return to their home countries.",
            "D": "That government should provide all social services.",
        },
        "why": "DOK 2: Addams states Hull-House operated on “the theory that the dependence of classes on each other is reciprocal,” emphasizing mutual benefit.",
    },
}


# ---- Anchor primary sources (public-domain; transcribed from the verified decks) ----
SOURCES = {
    "US.01": [
        ("Homestead Act", "U.S. Congress", "May 20, 1862 (12 Stat. 392)",
         "Any person who is the head of a family, or who has arrived at the age of twenty-one years, and is a citizen of the United States… shall be entitled to enter one quarter section [160 acres] of unappropriated public lands.",
         "National Archives", "https://www.archives.gov/milestone-documents/homestead-act"),
        ("Pacific Railway Act", "U.S. Congress", "July 1, 1862 (12 Stat. 489)",
         "The United States shall extinguish as rapidly as may be the Indian titles to all lands falling under the operation of this act… There is hereby granted to the said company… every alternate section of public land, designated by odd numbers.",
         "National Archives", "https://www.archives.gov/milestone-documents/pacific-railway-act"),
    ],
    "US.02": [
        ("Dawes General Allotment Act", "U.S. Congress", "Feb 8, 1887 (24 Stat. 388)",
         "…the President of the United States [is] authorized… to allot the lands in said reservation in severalty to any Indian located thereon in quantities as follows: To each head of a family, one-quarter of a section [160 acres].",
         "Library of Congress / Statutes at Large", "https://www.loc.gov/law/help/statutes-at-large/49th-congress/session-2/c49s2ch119.pdf"),
        ("Annual Report of the Commissioner of Indian Affairs", "Office of Indian Affairs", "1890",
         "The great object… is the disintegration of the tribes… and their absorption into the national life as American citizens.",
         "HathiTrust / U.S. Government", "https://www.doi.gov/ocl"),
    ],
    "US.03": [
        ("Plessy v. Ferguson (majority opinion)", "Supreme Court of the United States", "May 18, 1896 (163 U.S. 537)",
         "Laws permitting, and even requiring, [the] separation [of the races] in places where they are liable to be brought into contact do not necessarily imply the inferiority of either race…",
         "Library of Congress / U.S. Reports", "https://www.loc.gov/item/usrep163537/"),
        ("Harlan dissent, Plessy v. Ferguson", "Justice John Marshall Harlan", "May 18, 1896",
         "Our Constitution is color-blind, and neither knows nor tolerates classes among citizens.",
         "Library of Congress / U.S. Reports", "https://www.loc.gov/item/usrep163537/"),
    ],
    "US.04": [
        ("The American Commonwealth", "James Bryce", "1888",
         "The Boss… has a fine sense of political values… He dispenses places, rewards the loyal, punishes the mutinous… The machine works because it feeds those who serve it.",
         "HathiTrust / Public Domain", "https://catalog.hathitrust.org/Record/001260456"),
        ("Pendleton Civil Service Reform Act", "U.S. Congress", "January 16, 1883 (22 Stat. 403)",
         "…appointments to the [classified] service… shall be made… from among those graded highest as the results of such competitive examinations.",
         "Library of Congress / Statutes at Large", "https://www.loc.gov/law/help/statutes-at-large/47th-congress/session-2/c47s2ch27.pdf"),
    ],
    "US.05": [
        ("“Wealth” (The Gospel of Wealth)", "Andrew Carnegie", "June 1889",
         "The man who dies thus rich dies disgraced… This, then, is held to be the duty of the man of wealth: to consider all surplus revenues… as trust funds… to produce the most beneficial results for the community.",
         "Public Domain / North American Review", "https://www.carnegie.org/about/our-history/gospelofwealth/"),
        ("The Freeman (on Madam C.J. Walker)", "The Freeman (Indianapolis)", "c. 1911",
         "Mrs. Walker… has built up a business… giving employment to hundreds of colored women… a monument to Negro thrift and enterprise.",
         "Public Domain / Indianapolis Freeman", "https://www.loc.gov/item/mnwp000200/"),
    ],
    "US.06": [
        ("Proportion of Wage Earners in Manufactures, 1890", "Henry Gannett / U.S. Census Office", "1898",
         "[Statistical Atlas map] The darkest shading marks the industrial Northeast and Great Lakes — the manufacturing core drawing workers from farms and abroad.",
         "Library of Congress, Geography & Map Division", "https://www.loc.gov/resource/g3701gm.gct00010/?sp=86"),
        ("How the Other Half Lives", "Jacob Riis", "1890",
         "In the tenements all the influences make for evil… The gap between the classes… is widening day by day.",
         "Public Domain / Scribner’s", "https://www.loc.gov/item/12000787/"),
    ],
    "US.07": [
        ("Chinese Exclusion Act", "U.S. Congress", "May 6, 1882 (22 Stat. 58)",
         "…the coming of Chinese laborers to the United States be, and the same is hereby, suspended… it shall not be lawful for any Chinese laborer to come… to remain within the United States.",
         "National Archives", "https://www.archives.gov/milestone-documents/chinese-exclusion-act"),
        ("Twenty Years at Hull-House", "Jane Addams", "1910",
         "We early found ourselves spending many hours in efforts to secure… justice for immigrants… whom the state had left unprotected.",
         "Public Domain / Macmillan", "https://www.loc.gov/item/10025680/"),
    ],
}
# FINAL Student-deck slide references (from the built 64-slide deck)
REF = {
 'US.01':{'vocab':3,'dt':'4–7','source':8,'persp':9,'progress':12,'range':'2–12'},
 'US.02':{'vocab':14,'dt':'15–17','source':18,'persp':19,'progress':20,'range':'13–20'},
 'US.03':{'vocab':22,'dt':'23–26','source':27,'persp':28,'progress':29,'range':'21–29'},
 'US.04':{'vocab':31,'dt':'32–35','source':36,'persp':37,'progress':38,'range':'30–38'},
 'US.05':{'vocab':40,'dt':'41–43','source':44,'persp':45,'progress':46,'range':'39–46'},
 'US.06':{'vocab':48,'dt':'49–51','source':52,'persp':53,'progress':54,'range':'47–54'},
 'US.07':{'vocab':56,'dt':'57–60','source':61,'persp':62,'progress':63,'range':'55–63'},
}


def debiased_options(std):
    """Return (options_in_display_order, correct_letter) with the correct answer moved
    to its de-biased target position. Distractors keep relative order; used identically
    by the student PROGRESS CHECK, teacher CFU, and ANSWER REVEAL so all three stay in sync."""
    item = CFU[std]
    correct_text = item["options"][item["correct"]]
    distractors = [item["options"][l] for l in ["A", "B", "C", "D"] if l != item["correct"]]
    letters = ["A", "B", "C", "D"]
    tgt = item["target_pos"]
    ordered, di = {}, 0
    for L in letters:
        if L == tgt:
            ordered[L] = correct_text
        else:
            ordered[L] = distractors[di]; di += 1
    return ordered, tgt


if __name__ == "__main__":
    # self-check: print the de-biased key row
    row = []
    for s in ["US.01", "US.02", "US.03", "US.04", "US.05", "US.06", "US.07"]:
        _, k = debiased_options(s)
        row.append(f"{s}:{k}(DOK{CFU[s]['dok']})")
    print("De-biased progress-check keys →", "  ".join(row))
    for s in STANDARDS:
        assert len(VOCAB[s]) >= 3, s
        assert len(CFU[s]["options"]) == 4, s
    print("Vocab terms:", sum(len(v) for v in VOCAB.values()), "| standards:", len(STANDARDS))
