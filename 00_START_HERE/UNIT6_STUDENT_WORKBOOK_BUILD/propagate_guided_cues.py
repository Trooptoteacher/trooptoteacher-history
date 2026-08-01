import importlib.util, copy
spec=importlib.util.spec_from_file_location("bgn","/home/user/trooptoteacher-history/.claude/skills/history-hack-unit-content-build/scripts/build_guided_notes.py")
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
from docx import Document
from docx.oxml.ns import qn

def txt(el): return ''.join(n.text or '' for n in el.iter(qn('w:t')))

def ensure_cue_rows(tbl, n):
    """Expand the Cornell table so there are exactly n cue-content rows before the 'Key terms' row."""
    rows=tbl.findall(qn('w:tr'))
    kt=None
    for r in rows:
        if 'Key terms' in txt(r): kt=r; break
    cue_rows=[r for r in rows if txt(r).strip()!='' and 'Cues (tied' not in txt(r) and 'Key terms' not in txt(r)]
    empty_cue_rows=[r for r in rows if txt(r).strip()=='' ]
    # count current cue-content rows = rows between header and key-terms (excluding header + kt)
    idx_rows=tbl.findall(qn('w:tr'))
    header=idx_rows[0]
    content=[r for r in idx_rows if r is not header and r is not kt]
    cur=len(content)
    if cur>=n: return cur
    template=content[-1] if content else None
    while cur<n and template is not None and kt is not None:
        newrow=copy.deepcopy(template)
        # clear any text in the copied cue cell (col0) paragraphs
        cells=newrow.findall(qn('w:tc'))
        if cells:
            for p in cells[0].findall(qn('w:p')):
                for r in p.findall(qn('w:r')): p.remove(r)
        kt.addprevious(newrow); cur+=1
    return cur

CUES={
"US.45":[("①  Key Characteristics of Fascism","▶ Deck · DI 1 of 4","What traits make a government fascist?"),
("②  Fundamental Tenets of Communism","▶ Deck · DI 2 of 4","What drives history — and who owns property?"),
("③  Totalitarianism — Italy, Germany, USSR","▶ Deck · DI 3 of 4","How did each regime take total control?"),
("④  Factors in Its International Spread","▶ Deck · DI 4 of 4","Why did these ideas spread after WWI?")],
"US.46":[("①  Quarantine Speech (Oct 5, 1937)","▶ Deck · DI 1 of 4","How did FDR warn Americans about aggression?"),
("②  Four Freedoms Speech (Jan 6, 1941)","▶ Deck · DI 2 of 4","What four freedoms were worth defending?"),
("③  Atlantic Charter (Aug 14, 1941)","▶ Deck · DI 3 of 4","What postwar goals did the U.S. & Britain set?"),
("④  Lend-Lease Act (Mar 11, 1941)","▶ Deck · DI 4 of 4","How did the U.S. aid the Allies without joining the war?")],
"US.47":[("①  U.S. Response Before the War","▶ Deck · DI 1 of 4","How did the U.S. respond to Jewish refugees before the war?"),
("②  Liberation of the Concentration Camps","▶ Deck · DI 2 of 4","What did U.S. forces find as they liberated the camps?"),
("③  Post-War Immigration of Survivors","▶ Deck · DI 3 of 4","How did the U.S. respond to survivors after the war?"),
("④  Moral & Ethical Implications","▶ Deck · DI 4 of 4","What lasting moral questions does the Holocaust raise?")],
"US.48":[("①  Factors in the European Theater","▶ Deck · DI 1 of 4","What pulled the U.S. toward war in Europe?"),
("②  Factors in the Pacific Theater","▶ Deck · DI 2 of 4","What pulled the U.S. toward war in the Pacific?"),
("③  Attack on Pearl Harbor (Dec 7, 1941)","▶ Deck · DI 3 of 4","What happened at Pearl Harbor, and why did it matter?"),
("④  Consequences of American Entry","▶ Deck · DI 4 of 4","How did U.S. entry change the war?")],
"US.49":[("①  Allied Political Leaders","▶ Deck · DI 1 of 4","Who led the Allied nations, and how?"),
("②  Allied Military Leaders","▶ Deck · DI 2 of 4","Which commanders shaped Allied strategy?"),
("③  Axis Leaders","▶ Deck · DI 3 of 4","Who led the Axis powers?"),
("④  Comparing Leadership Approaches","▶ Deck · DI 4 of 4","How did Allied and Axis leadership differ?")],
"US.50":[("①  Battle of Midway (June 1942)","▶ Deck · DI 1 of 4","Why was Midway the Pacific turning point?"),
("②  Battle of Iwo Jima (Feb–Mar 1945)","▶ Deck · DI 2 of 4","Why was Iwo Jima so costly and important?"),
("③  Battle of Okinawa (Apr–Jun 1945)","▶ Deck · DI 3 of 4","How did Okinawa shape what came next?"),
("④  D-Day: Normandy Invasion (Jun 6, 1944)","▶ Deck · DI 4 of 4","How did D-Day open the Western Front?")],
"US.51":[("①  Tuskegee Airmen","▶ Deck · DI 1 of 5","Who were the Tuskegee Airmen, and what did they achieve?"),
("②  442nd Regimental Combat Team","▶ Deck · DI 2 of 5","What made the 442nd so distinguished?"),
("③  101st Airborne Division","▶ Deck · DI 3 of 5","What was the 101st's role in the war?"),
("④  Navajo Code Talkers","▶ Deck · DI 4 of 5","How did the Code Talkers protect U.S. communications?"),
("⑤  Individual Sacrifice & Legacy","▶ Deck · DI 5 of 5","What legacy did these units leave?")],
"US.52":[("①  Factors Leading to Participation","▶ Deck · DI 1 of 4","Why did so many women enter the workforce?"),
("②  Challenges & Opportunities","▶ Deck · DI 2 of 4","What challenges and openings did women face?"),
("③  Impact on Production & Economy","▶ Deck · DI 3 of 4","How did women's work affect wartime production?"),
("④  Long-term Effects on Society","▶ Deck · DI 4 of 4","How did WWII change women's role long-term?")],
"US.53":[("①  Second Great Migration & Opportunity","▶ Deck · DI 1 of 4","Why and where did Black Americans move?"),
("②  Double V Campaign","▶ Deck · DI 2 of 4","What were the two victories of the Double V?"),
("③  Fair Employment Practices Committee","▶ Deck · DI 3 of 4","What did the FEPC change?"),
("④  Integration of the Armed Forces","▶ Deck · DI 4 of 4","How did the war push toward integration?")],
"US.54":[("①  Executive Order 9066 & Internment","▶ Deck · DI 1 of 4","What did EO 9066 authorize?"),
("②  Constitutional Issues","▶ Deck · DI 2 of 4","Which constitutional rights were at stake?"),
("③  Korematsu v. United States (1944)","▶ Deck · DI 3 of 4","How did the Court rule, and why does it matter?"),
("④  Impact & Historical Lessons","▶ Deck · DI 4 of 4","What lasting lessons came from internment?")],
"US.55":[("①  Rationing & Conservation","▶ Deck · DI 1 of 4","How did rationing reshape daily life?"),
("②  War Bonds & Propaganda","▶ Deck · DI 2 of 4","How did the government fund and sell the war?"),
("③  Migration, Factory Conversion, Bracero","▶ Deck · DI 3 of 4","How did the economy retool for war?"),
("④  Tennessee's Wartime Role","▶ Deck · DI 4 of 4","How did Tennessee contribute to the war effort?")],
"US.56":[("①  Oak Ridge, Tennessee Selection","▶ Deck · DI 1 of 4","Why was Oak Ridge, TN chosen?"),
("②  Manhattan Project Overview","▶ Deck · DI 2 of 4","What was the Manhattan Project?"),
("③  Rationale for Using Atomic Weapons","▶ Deck · DI 3 of 4","Why did the U.S. use the atomic bomb?"),
("④  The Ethical Debate","▶ Deck · DI 4 of 4","What ethical questions does the bomb raise?")],
"US.57":[("①  Yalta Conference (Feb 1945)","▶ Deck · DI 1 of 4","What did the Big Three decide at Yalta?"),
("②  Potsdam Conference (Jul–Aug 1945)","▶ Deck · DI 2 of 4","What changed by Potsdam?"),
("③  Cold War Origins","▶ Deck · DI 3 of 4","How did wartime diplomacy seed the Cold War?"),
("④  Assessing Allied Diplomacy","▶ Deck · DI 4 of 4","How well did Allied diplomacy work?")],
"US.58":[("①  Lessons from the League's Failure","▶ Deck · DI 1 of 4","Why did the League fail, and what was learned?"),
("②  Cordell Hull's Role","▶ Deck · DI 2 of 4","Why is Tennessean Cordell Hull the 'Father of the UN'?"),
("③  UN Goals & Structure","▶ Deck · DI 3 of 4","What are the UN's goals and structure?"),
("④  UN Legacy & Limitations","▶ Deck · DI 4 of 4","What has the UN achieved, and where is it limited?")],
}

doc=Document('_committed_base.docx')
for code,cues in CUES.items():
    tbl=m.find_cornell_table(doc,code)
    ensure_cue_rows(tbl,len(cues))
    m.seed_guided_cornell(tbl,cues)
    print(f"seeded {code}: {len(cues)} cue segments")
doc.save('Unit6_Workbook_guidedcues.docx')
print("saved Unit6_Workbook_guidedcues.docx")
