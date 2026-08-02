# REFERENCE IMPLEMENTATION (Unit 6). Adapt per-unit content dicts, standard codes, and paths.
# See ../references/ for the method. Run from the scratchpad holding the working files/JSONs.
import copy
from docx import Document
from docx.oxml.ns import qn

doc = Document('Unit6_Student_Workbook_CourseStandard_EDITABLE.docx')
body = doc.element.body

def ptext(el): return ''.join(n.text or '' for n in el.iter(qn('w:t'))).strip()
def is_p(el): return el.tag==qn('w:p')
def is_tbl(el): return el.tag==qn('w:tbl')
def has_pbb(p):
    ppr=p.find(qn('w:pPr')); return ppr is not None and ppr.find(qn('w:pageBreakBefore')) is not None

def kids(): return list(body)

def region(code):
    ks=kids(); a=None
    for i,ch in enumerate(ks):
        if is_p(ch) and ptext(ch).startswith('Standard '+code): a=i; break
    b=len(ks)
    for i in range(a+1,len(ks)):
        if is_p(ks[i]) and ptext(ks[i]).startswith('Standard US.'): b=i; break
    return ks,a,b

def collect_block(ks,a,b,header):
    # find header paragraph in [a,b), collect until next PBB (exclusive)
    start=None
    for i in range(a,b):
        if is_p(ks[i]) and ptext(ks[i]).startswith(header): start=i; break
    assert start is not None, header
    block=[ks[start]]
    for i in range(start+1,b):
        ch=ks[i]
        if is_p(ch) and has_pbb(ch): break
        block.append(ch)
    return block

# ---- build US.45 templates (deepcopy) ----
ks,a45,b45 = region('US.45')
vocab_tpl  = [copy.deepcopy(e) for e in collect_block(ks,a45,b45,'VOCABULARY SUPPORTS')]
hippo_tpl  = [copy.deepcopy(e) for e in collect_block(ks,a45,b45,'HIPPO SUPPORTS')]
writing_blk= collect_block(ks,a45,b45,'WRITING SUPPORTS')
# drop trailing exit-ticket table from writing template
if is_tbl(writing_blk[-1]): writing_blk=writing_blk[:-1]
writing_tpl=[copy.deepcopy(e) for e in writing_blk]

# ---- helpers to edit cloned blocks ----
def find_para(block, startswith):
    for el in block:
        if is_p(el) and ptext(el).startswith(startswith): return el
    return None

def set_uniform_text(p, newtext):
    runs=p.findall(qn('w:r'))
    if not runs:
        r=p.makeelement(qn('w:r'),{}); p.append(r); runs=[r]
    first=runs[0]
    for t in first.findall(qn('w:t')): first.remove(t)
    t=first.makeelement(qn('w:t'),{}); t.set(qn('xml:space'),'preserve'); t.text=newtext; first.append(t)
    for r in runs[1:]:
        p.remove(r)

def rebuild_model(p, segments):
    runs=p.findall(qn('w:r'))
    base=runs[0].find(qn('w:rPr')) if runs else None
    for r in runs: p.remove(r)
    for label,bodytext in segments:
        r=p.makeelement(qn('w:r'),{}); rp=copy.deepcopy(base) if base is not None else p.makeelement(qn('w:rPr'),{})
        if rp.find(qn('w:b')) is None: rp.append(p.makeelement(qn('w:b'),{}))
        r.append(rp); t=p.makeelement(qn('w:t'),{}); t.set(qn('xml:space'),'preserve'); t.text=label; r.append(t); p.append(r)
        r2=p.makeelement(qn('w:r'),{}); rp2=copy.deepcopy(base) if base is not None else p.makeelement(qn('w:rPr'),{})
        bb=rp2.find(qn('w:b'));  rp2.remove(bb) if bb is not None else None
        r2.append(rp2); t2=p.makeelement(qn('w:t'),{}); t2.set(qn('xml:space'),'preserve'); t2.text=bodytext; r2.append(t2); p.append(r2)

def rebuild_wordattack(p, eng, esp):
    runs=p.findall(qn('w:r'))
    label_rpr=copy.deepcopy(runs[0].find(qn('w:rPr')))
    body_rpr=copy.deepcopy(label_rpr)
    for tg in ('w:b','w:color'):
        e=body_rpr.find(qn(tg));  body_rpr.remove(e) if e is not None else None
    for r in runs: p.remove(r)
    def add(rpr,text):
        r=p.makeelement(qn('w:r'),{}); r.append(copy.deepcopy(rpr))
        t=p.makeelement(qn('w:t'),{}); t.set(qn('xml:space'),'preserve'); t.text=text; r.append(t); p.append(r)
    add(label_rpr,"Word-attack strategy: ")
    add(body_rpr,"break long terms into smaller parts you recognize. Several terms are Spanish cognates (%s / %s), so use the Spanish column to unlock meaning." % (eng,esp))

# ---- per-standard content ----
C = {
 'US.47': dict(cog=('Holocaust','Holocausto'),
   hippo=[("H: ","Taken April 16, 1945, as U.S. troops liberated the Buchenwald concentration camp near the end of the war in Europe, when the full scale of the Holocaust was being revealed. "),
          ("I: ","The American public and the world, released through the U.S. Army Signal Corps and the press. "),
          ("P: ","To create an official record of Nazi atrocities and confront denial that the camps existed. "),
          ("POV: ","It shows the liberators' and survivors' view; the perpetrators are outside the frame. "),
          ("O: ","Connects to earlier U.S. refusal to raise immigration quotas (the SS St. Louis, 1939) and to the postwar admission of survivors.")],
   cer=[("Claim: ","The U.S. response to the Holocaust shifted from limited action before the war, to direct liberation during it, to gradual acceptance of survivors afterward. "),
        ("Evidence: ","Before the war strict immigration quotas kept many Jewish refugees out (the SS St. Louis was turned away in 1939); during the war U.S. troops liberated camps such as Buchenwald in 1945. "),
        ("Reasoning: ","This shows the U.S. did little to rescue Jews early but confronted the Holocaust once its armies reached the camps, and later loosened policy to admit survivors.")]),
 'US.48': dict(cog=('declaration','declaración'),
   hippo=[("H: ","Photographed December 7, 1941, during Japan's surprise attack on the U.S. naval base at Pearl Harbor, Hawaii. "),
          ("I: ","The American public, published to show the devastation of the attack. "),
          ("P: ","To document the damage; once released, the image helped rally Americans for war. "),
          ("POV: ","The U.S. Navy's perspective as the victim of a surprise attack. "),
          ("O: ","Connects to FDR's “date which will live in infamy” speech and the U.S. declaration of war the next day.")],
   cer=[("Claim: ","The Japanese attack on Pearl Harbor was the immediate cause that brought the United States into World War II. "),
        ("Evidence: ","On December 7, 1941, Japan bombed the U.S. fleet at Pearl Harbor, and the next day Congress declared war on Japan. "),
        ("Reasoning: ","The attack ended American isolationism overnight by making neutrality impossible and uniting public opinion behind entering the war.")]),
 'US.49': dict(cog=('invasion','invasión'),
   hippo=[("H: ","Delivered June 4, 1940, to the British House of Commons after the evacuation of Dunkirk, as France was falling and Britain faced Nazi Germany largely alone. "),
          ("I: ","The British Parliament and public — and, indirectly, the still-neutral United States. "),
          ("P: ","To rally Britain to keep fighting and to signal determination to potential allies. "),
          ("POV: ","Churchill's defiant wartime-leadership perspective. "),
          ("O: ","Connects to U.S. Lend-Lease aid to Britain and to Churchill's later cooperation with Roosevelt and Stalin.")],
   cer=[("Claim: ","Individual leaders shaped the course of World War II through the decisions they made. "),
        ("Evidence: ","Churchill rallied Britain to resist Nazi Germany after Dunkirk in 1940, while Eisenhower planned and commanded the D-Day invasion in 1944. "),
        ("Reasoning: ","These leaders' choices — resistance and strategic command — show how key individuals directed the Allied war effort toward victory.")]),
 'US.50': dict(cog=('strategy','estrategia'),
   hippo=[("H: ","Photographed February 23, 1945, during the Battle of Iwo Jima in the Pacific, as U.S. Marines captured the island. "),
          ("I: ","The American public; the image was soon used to promote war bonds. "),
          ("P: ","To capture the moment of victory on Mount Suribachi; later used for morale and fundraising. "),
          ("POV: ","The U.S. Marines' and American view of a hard-won Pacific victory. "),
          ("O: ","Connects to the island-hopping strategy and to the heavy casualties that shaped the decision to use the atomic bomb.")],
   cer=[("Claim: ","Geography and military strategy strongly shaped the outcomes of key World War II battles. "),
        ("Evidence: ","At Midway (1942) U.S. code-breaking and carrier positioning let a smaller fleet defeat Japan, and Iwo Jima (1945) was taken for its strategic airfields despite heavy losses. "),
        ("Reasoning: ","These show that terrain, location, and strategy — not just numbers — decided battles and moved the Allies closer to Japan.")]),
 'US.51': dict(cog=('combat','combate'),
   hippo=[("H: ","Photographed March 1945 at Ramitelli, Italy, showing the Tuskegee Airmen (332nd Fighter Group), African American pilots who served in a still-segregated military. "),
          ("I: ","The American public and press, documenting the airmen's service. "),
          ("P: ","To record and publicize the contributions of Black pilots. "),
          ("POV: ","It highlights the airmen's excellence, taken within a segregated system that limited them. "),
          ("O: ","Connects to the Double V campaign and to the later integration of the armed forces in 1948.")],
   cer=[("Claim: ","Special fighting forces made vital contributions to World War II while facing discrimination at home. "),
        ("Evidence: ","The Tuskegee Airmen escorted bombers over Europe with a strong record, and the Japanese American 442nd Regimental Combat Team became one of the most decorated units in U.S. history. "),
        ("Reasoning: ","Their service proved the skill and loyalty of soldiers from groups facing prejudice, strengthening later arguments for civil rights and integration.")]),
 'US.52': dict(cog=('industry','industria'),
   hippo=[("H: ","Photographed February 1943 at the Vultee aircraft plant in Nashville, Tennessee, as women filled defense jobs while men served overseas. "),
          ("I: ","The American public, produced by the Office of War Information to encourage women to join the workforce. "),
          ("P: ","Recruitment — to present women's war work as normal and patriotic. "),
          ("POV: ","The government's promotional view of women's labor; it downplays the barriers women faced. "),
          ("O: ","Connects to “Rosie the Riveter” and to postwar debates over whether women would keep their jobs.")],
   cer=[("Claim: ","World War II brought large numbers of women into the workforce and military, changing American society. "),
        ("Evidence: ","Women took defense-industry jobs such as building aircraft (as at the Vultee plant in Nashville), and hundreds of thousands served in units like the WACs and WAVES. "),
        ("Reasoning: ","This showed women could do jobs once reserved for men and, though many left work after the war, it laid groundwork for later expansion of women's roles.")]),
 'US.53': dict(cog=('discrimination','discriminación'),
   hippo=[("H: ","Photographed around 1942 at a North American Aviation plant, as wartime labor demand opened defense jobs to more workers. "),
          ("I: ","The public, documenting integrated war production. "),
          ("P: ","To show wartime industry and, implicitly, changing labor patterns. "),
          ("POV: ","An optimistic view of workplace integration; wartime segregation and discrimination still persisted. "),
          ("O: ","Connects to Executive Order 8802, the Fair Employment Practices Committee, and the Double V campaign.")],
   cer=[("Claim: ","World War II improved some economic opportunities for African Americans and set the stage for civil rights gains. "),
        ("Evidence: ","Executive Order 8802 (1941) banned discrimination in defense industries and created the FEPC, and wartime pressure led toward integration of the armed forces in 1948. "),
        ("Reasoning: ","Wartime labor needs and Black activism (the Double V campaign) forced changes that became a foundation for the postwar civil rights movement.")]),
 'US.54': dict(cog=('internment','internamiento'),
   hippo=[("H: ","Photographed May 8, 1942, in Hayward, California, as the Mochida family awaited forced removal to an internment camp after Executive Order 9066. "),
          ("I: ","Taken for a U.S. government agency to document the removal; many of Lange's images were withheld at the time. "),
          ("P: ","To officially record the “evacuation”; Lange used it to quietly show the human cost. "),
          ("POV: ","Sympathetic to the interned families; the government framed removal as military necessity. "),
          ("O: ","Connects to Executive Order 9066 and to the Korematsu v. United States decision.")],
   cer=[("Claim: ","The internment of Japanese Americans violated constitutional rights in the name of wartime security. "),
        ("Evidence: ","Executive Order 9066 (1942) forced about 120,000 Japanese Americans — most of them U.S. citizens — into camps, and in Korematsu v. United States (1944) the Supreme Court upheld the removal. "),
        ("Reasoning: ","This shows how fear and prejudice led the government to suspend citizens' rights, a decision later condemned and formally apologized for in 1988.")]),
 'US.55': dict(cog=('rationing','racionamiento'),
   hippo=[("H: ","Issued in 1943 by the Office of Price Administration, when the U.S. rationed scarce goods to support the war effort. "),
          ("I: ","American consumers and households, explaining how to use ration books. "),
          ("P: ","To share scarce resources fairly and to prevent inflation and hoarding. "),
          ("POV: ","The federal government's view that shared sacrifice was a patriotic duty. "),
          ("O: ","Connects to bond drives, factory conversion, and other home-front mobilization.")],
   cer=[("Claim: ","World War II transformed the American home front through shared sacrifice and government mobilization. "),
        ("Evidence: ","The government rationed goods such as gasoline and sugar with ration books (1942–43), and factories converted to war production of tanks, planes, and ships. "),
        ("Reasoning: ","These changes show how total war reached everyday life, requiring civilians to sacrifice and the economy to reorganize around military needs.")]),
 'US.56': dict(cog=('atomic','atómica'),
   hippo=[("H: ","Photographed August 9, 1945, when the U.S. dropped the second atomic bomb on Nagasaki, days after Hiroshima, forcing Japan toward surrender. "),
          ("I: ","The military and, later, the public — documenting the new weapon's power. "),
          ("P: ","To record the bombing; the image became a symbol of the atomic age. "),
          ("POV: ","The U.S. Army Air Forces' perspective; the victims on the ground are unseen. "),
          ("O: ","Connects to the Manhattan Project and to the debate over ending the war versus its human cost.")],
   cer=[("Claim: ","The U.S. used the atomic bomb to end the war quickly, though the decision remains debated. "),
        ("Evidence: ","The secret Manhattan Project built the bomb, and in August 1945 the U.S. dropped bombs on Hiroshima and Nagasaki, after which Japan surrendered. "),
        ("Reasoning: ","Leaders argued the bombs avoided a costly invasion of Japan, but the massive civilian deaths raised lasting moral questions.")]),
 'US.57': dict(cog=('conference','conferencia'),
   hippo=[("H: ","Photographed February 1945 at the Yalta Conference, where Churchill, Roosevelt, and Stalin met as Allied victory neared. "),
          ("I: ","The public, showing unity among the “Big Three.” "),
          ("P: ","To project cooperation and to plan the postwar world. "),
          ("POV: ","The Allied leaders' official view of unity; tensions, especially over Eastern Europe, are hidden. "),
          ("O: ","Connects to the later Potsdam Conference and to the origins of the Cold War.")],
   cer=[("Claim: ","The Yalta and Potsdam Conferences shaped the postwar world and set the stage for the Cold War. "),
        ("Evidence: ","At Yalta (February 1945) the Allies agreed to divide Germany and create the United Nations, and at Potsdam (July–August 1945) they finalized occupation and demanded Japan's surrender. "),
        ("Reasoning: ","These decisions redrew borders and spheres of influence, but disputes — especially over Eastern Europe — soon divided the former allies.")]),
 'US.58': dict(cog=('nations','naciones'),
   hippo=[("H: ","Photographed January 1, 1942, when 26 Allied nations signed the Declaration by United Nations, pledging to fight the Axis together. "),
          ("I: ","The world public, showing Allied commitment early in the U.S. war effort. "),
          ("P: ","To formalize the wartime alliance and lay groundwork for a postwar organization. "),
          ("POV: ","The Allied nations' perspective of unity against the Axis. "),
          ("O: ","Connects to Cordell Hull's diplomacy and to the 1945 founding of the United Nations.")],
   cer=[("Claim: ","The United Nations was founded to prevent future world wars through international cooperation. "),
        ("Evidence: ","The 1942 Declaration by United Nations united the Allies, and Secretary of State Cordell Hull worked to design a permanent organization, leading to the UN's founding in 1945. "),
        ("Reasoning: ","Having seen the League of Nations fail and two world wars occur, leaders built the UN so nations could resolve disputes and keep the peace together.")]),
}

def clone(tpl): return [copy.deepcopy(e) for e in tpl]

for code, c in C.items():
    ks,a,b = region(code)
    # anchors
    act2 = next(ks[i] for i in range(a,b) if is_p(ks[i]) and ptext(ks[i]).startswith('Activity 2'))
    act6 = next(ks[i] for i in range(a,b) if is_p(ks[i]) and ptext(ks[i]).startswith('Activity 6'))
    exit_tbl = next(ks[i] for i in range(a,b) if is_tbl(ks[i]) and 'EXIT TICKET' in ptext(ks[i]))

    vb=clone(vocab_tpl)
    rebuild_wordattack(find_para(vb,'Word-attack strategy'), c['cog'][0], c['cog'][1])

    hb=clone(hippo_tpl)
    set_uniform_text(find_para(hb,'HIPPO SUPPORTS'), 'HIPPO SUPPORTS — analyzing the source · '+code)
    rebuild_model(find_para(hb,'H: Taken in 1935'), c['hippo'])

    wb=clone(writing_tpl)
    set_uniform_text(find_para(wb,'WRITING SUPPORTS'), 'WRITING SUPPORTS — Constructed Response (CER) · '+code)
    rebuild_model(find_para(wb,'Claim: Economic crisis'), c['cer'])

    for el in vb: act2.addprevious(el)
    for el in hb: act6.addprevious(el)
    for el in wb: exit_tbl.addprevious(el)
    print('built', code)

doc.save('Unit6_Student_Workbook_CourseStandard_EDITABLE.docx')
print('SAVED')
