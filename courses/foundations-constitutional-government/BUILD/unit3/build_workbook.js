// Unit 1 Course Standard STUDENT WORKBOOK — docx-js, EXACT Unit 5 template (no deviation).
// Design tokens extracted from Unit5_Student_Workbook_CourseStandard.docx.
const fs=require('fs'); const D=require('docx');
const {Document,Packer,Paragraph,TextRun,HeadingLevel,AlignmentType,Table,TableRow,TableCell,
  WidthType,BorderStyle,ShadingType,PageBreak,TableOfContents,Header,Footer,PageNumber,HeightRule,ImageRun}=D;
const C=JSON.parse(fs.readFileSync('analysis/unit3_content.json','utf8'));
const IMG=fs.existsSync('analysis/unit3_images.json')?JSON.parse(fs.readFileSync('analysis/unit3_images.json','utf8')):{};
const EXIT=fs.existsSync('analysis/unit3_exit_tickets.json')?JSON.parse(fs.readFileSync('analysis/unit3_exit_tickets.json','utf8')):{};
const SAMPLE=process.env.SAMPLE?Number(process.env.SAMPLE):0; const ONLYSTD=process.env.ONLYSTD||''; const PREVIEW=SAMPLE||ONLYSTD; const ORDER=ONLYSTD?[ONLYSTD]:(SAMPLE?C.order.slice(0,SAMPLE):C.order);
// ---- course/unit chrome (parameterized — no hardcoded US-History / district content) ----
const U=C.unit; const BRAND=(U.brand||'Government Hack'); const BRANDTM=BRAND+'™';
const UNIT_NO=(U.code||'Unit 1').replace(/Unit\s*/i,'');
const COURSE=U.course_name||'Foundations of Constitutional Government';
const RANGE=U.standards_range||'';
const EQ=U.essential_question||'';
const TNLABEL=U.tn_connection_label||'TENNESSEE CONNECTION';

// ---- exact tokens ----
const NAVY='1B2A4A', RED='B22234', GOLD='C89B3C', INK='1A1A1A', CREAM='F7F5EF', WHITE='FFFFFF', GREY='6B7280', BORD='D9D5C8';
const FONT='Calibri';
const CW=9792;                         // 6.8in printable width = 12240 − 1224 − 1224 (U.S. History Hack brand)
const bd=(c=BORD,sz=4)=>({style:BorderStyle.SINGLE,size:sz,color:c});
const CELLB=(c=BORD)=>({top:bd(c),bottom:bd(c),left:bd(c),right:bd(c)});
const LP=process.env.LARGEPRINT?Number(process.env.LARGEPRINT):1;
const SZ=(n)=>Math.round(n*LP);
function R(text,{s=22,b=false,i=false,c=INK,caps=false}={}){return new TextRun({text,size:SZ(s),bold:b,italics:i,color:c,font:FONT,allCaps:caps});}
function P(runs,{align,spacing,indent,border}={}){return new Paragraph({alignment:align,spacing:spacing||{after:100},indent,border,children:Array.isArray(runs)?runs:[runs]});}
function H(text,lvl,{brk=false,mins=null}={}){const map={1:HeadingLevel.HEADING_1,2:HeadingLevel.HEADING_2,3:HeadingLevel.HEADING_3};
  const kids=[R(text,{s:lvl===1?36:lvl===2?28:24,b:true,c:lvl===3?RED:NAVY})];
  if(mins) kids.push(R(`    ⏱ ~${mins} min`,{s:18,b:true,c:GOLD}));
  return new Paragraph({heading:map[lvl],pageBreakBefore:brk,spacing:{before:lvl===1?220:150,after:90},keepNext:true,children:kids});}
function cell(children,{w,fill,borders}={}){return new TableCell({width:{size:w,type:WidthType.DXA},
  shading:fill?{type:ShadingType.CLEAR,fill,color:'auto'}:undefined,margins:{top:55,bottom:55,left:110,right:110},
  borders:borders||CELLB(),children:Array.isArray(children)?children:[children]});}
function table(rows,widths){return new Table({width:{size:CW,type:WidthType.DXA},columnWidths:widths,rows});}
// single-cell cream callout: LABEL then content lines
function callout(label,lines=[]){const kids=[P(R(label,{s:21,b:true,c:NAVY,caps:false}),{spacing:{after:lines.length?60:0}})];
  (Array.isArray(lines)?lines:[lines]).forEach(l=>kids.push(P(typeof l==='string'?R(l,{s:22}):l,{spacing:{after:40}})));
  return table([new TableRow({children:[cell(kids,{w:CW,fill:CREAM})]})],[CW]);}
// PROMINENT callout — navy fill, gold label, white text. Used for CORE PATH (the firm, universal bar).
function coreCallout(label,lines=[]){const kids=[P(R(label,{s:23,b:true,c:GOLD}),{spacing:{after:lines.length?70:0}})];
  (Array.isArray(lines)?lines:[lines]).forEach(l=>kids.push(P(typeof l==='string'?R(l,{s:22,c:WHITE}):l,{spacing:{after:40}})));
  return table([new TableRow({children:[cell(kids,{w:CW,fill:NAVY,borders:CELLB(NAVY)})]})],[CW]);}
// Primary-source image: picture (with alt text) + caption + full public-domain citation.
// Records come from the verified public-domain primary-source bank (see references).
function sourceImage(rec,{max}={}){
  const w=max?Math.min(rec.w,max):rec.w, h=max?Math.round(rec.h*(w/rec.w)):rec.h;
  const out=[new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:60},children:[
    new ImageRun({data:fs.readFileSync(rec.file),transformation:{width:w,height:h},
      altText:{title:rec.title||'Primary source',description:rec.alt||rec.caption||rec.title||'Primary source image',name:rec.title||'source'}})]})];
  const cap=[rec.title, rec.creator?('· '+rec.creator):'', rec.year?('· '+rec.year):''].filter(Boolean).join(' ');
  out.push(P(R(cap,{s:19,b:true}),{spacing:{after:20}}));
  out.push(P(R(`Source: ${rec.citation||''} ${rec.rights||''}${rec.rightsUrl?(' '+rec.rightsUrl):''}`.trim(),{s:16,c:GREY}),{spacing:{after:rec.colorKey?12:40}}));
  if(rec.colorKey) out.push(P([R('▶ ',{s:17,b:true,c:GOLD}),R('Fine detail and color read best on screen. A large full-color version is on the projection-map slides at the end of the slide deck.',{s:17,i:true,c:GREY})],{spacing:{after:40}}));
  return out;
}
// compact image only (no caption/citation) — for the launch-page hook (source is cited in Activity 5)
function imgOnly(rec,max){const w=Math.min(rec.w,max), h=Math.round(rec.h*(w/rec.w));
  return new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:60},children:[
    new ImageRun({data:fs.readFileSync(rec.file),transformation:{width:w,height:h},
      altText:{title:rec.title||'Primary source',description:rec.alt||rec.title||'Primary source image',name:'hook'}})]});}
// data table with navy header row
function dataTable(headers,rows,widths){
  const hr=new TableRow({tableHeader:true,children:headers.map((h,i)=>cell(P(R(h,{s:19,b:true,c:WHITE}),{spacing:{after:0}}),{w:widths[i],fill:NAVY}))});
  const body=rows.map(r=>new TableRow({children:r.map((cx,i)=>cell(P(typeof cx==='string'?R(cx,{s:20}):cx,{spacing:{after:0}}),{w:widths[i]}))}));
  return table([hr,...body],widths);}
// evidence-based ruled writing lines (baselines) — research favors lined writing space
// Writing baselines. NOTE: LibreOffice/Word merge adjacent paragraphs that share an
// identical bottom border and suppress the INTERNAL borders — so N stacked bordered
// paragraphs collapse to one visible line. We break that merge with a tiny border-less
// spacer between each line, so every baseline renders.
function ruled(n=3){const out=[];for(let i=0;i<n;i++){
  // Visible notebook line (C9C2B4 was invisible on-screen). Medium-gray rule + anti-merge spacer
  // between lines so EVERY line renders in the flow, not just in table cells.
  out.push(new Paragraph({widowControl:false,spacing:{before:SZ(28),after:SZ(28)},
    border:{bottom:{style:BorderStyle.SINGLE,size:8,color:'8892A0',space:1}},
    children:[new TextRun({text:' ',size:SZ(16),font:FONT})]}));
  if(i<n-1) out.push(new Paragraph({spacing:{before:0,after:0,line:SZ(50),lineRule:'exact'},children:[new TextRun({text:' ',size:SZ(2),font:FONT})]}));
}return out;}
function linesFor(h){return Math.max(2,Math.round(h/380));}
// writing table: label cells keep text; blank writing cells get ruled lines
function writeTable(headers,rows,widths,{rowH=560,lines}={}){
  const trs=[];
  if(headers)trs.push(new TableRow({tableHeader:true,children:headers.map((h,i)=>cell(P(R(h,{s:18,b:true,c:i===0?NAVY:WHITE}),{spacing:{after:0}}),{w:widths[i],fill:i===0?CREAM:NAVY}))}));
  const nl=lines||linesFor(rowH);
  rows.forEach(r=>trs.push(new TableRow({children:r.map((cx,i)=>cell(cx?[P(R(cx,{s:20,b:i===0}),{spacing:{after:0}})]:ruled(nl),{w:widths[i]}))})));
  return table(trs,widths);}
// cream label bar + ruled writing lines
function writeBox(label,nLines=3){return table([
  new TableRow({children:[cell(P(R(label,{s:21,b:true,c:NAVY}),{spacing:{after:0}}),{w:CW,fill:CREAM})]}),
  new TableRow({children:[cell(ruled(nLines),{w:CW})]})],[CW]);}
// Cornell note-taking — EXACT brand layout (U.S. History Hack workbook): navy header row,
// narrow cue column (2448) + wide notes column (7344), grid 4896|4896, zebra rows, cantSplit,
// atLeast row height; ruled writing lines fill the wide notes column so notes run across the page.
function cornellCell(children,{w,fill}={}){return new TableCell({width:{size:w,type:WidthType.DXA},
  shading:fill?{type:ShadingType.CLEAR,fill,color:'auto'}:undefined,margins:{top:50,bottom:50,left:80,right:80},
  borders:CELLB('C9C2B4'),children:Array.isArray(children)?children:[children]});}
function cornell(cues,rightLabel,nLines=3){
  const head=new TableRow({tableHeader:true,cantSplit:true,children:[
    cornellCell(P(R('Guiding cues',{s:20,b:true,c:WHITE}),{spacing:{after:0}}),{w:2448,fill:NAVY}),
    cornellCell(P(R(rightLabel,{s:20,b:true,c:WHITE}),{spacing:{after:0}}),{w:7344,fill:NAVY})]});
  const rows=cues.map((q,i)=>new TableRow({cantSplit:true,height:{value:520,rule:HeightRule.ATLEAST},children:[
    cornellCell(P(R(q,{s:21,c:NAVY}),{spacing:{after:40}}),{w:2448,fill:i%2?WHITE:CREAM}),
    cornellCell(ruled(nLines),{w:7344,fill:i%2?WHITE:CREAM})]}));
  return new Table({width:{size:CW,type:WidthType.DXA},columnWidths:[4896,4896],rows:[head,...rows]});}
// Split panel: left = open DRAW/DIAGRAM box, right = WRITE on notebook lines (UDL: draw or write).
function splitDrawWrite(drawLabel,writeLabel,h=3400,nLines=8){return table([new TableRow({height:{value:h,rule:HeightRule.ATLEAST},cantSplit:true,children:[
  cell([P(R(drawLabel,{s:15,b:true,c:NAVY}),{spacing:{after:20}})],{w:4896}),
  cell([P(R(writeLabel,{s:15,b:true,c:NAVY}),{spacing:{after:20}}),...ruled(nLines)],{w:4896})]})],[4896,4896]);}
const PB=()=>new Paragraph({children:[new PageBreak()]});
// ---- white-space FILL rule: right-sized activities so no page is left blank ----
const FILL_LIB={
  quickwrite:(topic)=>[P(R('QUICK WRITE',{s:21,b:true,c:NAVY})),P(R(topic,{s:20})),writeTable(null,[[''],[''],['']],[CW],{rowH:520})],
  sketch:(topic)=>[P(R('SKETCH IT (RESPONSE CHOICE — draw instead of write)',{s:21,b:true,c:NAVY})),P(R(topic,{s:20})),writeTable(null,[['']],[CW],{rowH:1600})],
  retrieval:()=>[P(R('RETRIEVAL — without looking back, list what you remember',{s:21,b:true,c:NAVY})),writeTable(null,[['1.'],['2.'],['3.']],[CW],{rowH:460})],
  stretch:(topic)=>[P(R('STRETCH (EXTENSION — open to all)',{s:21,b:true,c:RED})),P(R(topic,{s:20})),writeTable(null,[[''],['']],[CW],{rowH:560})],
  connect:(topic)=>[P(R('MAKE A CONNECTION',{s:21,b:true,c:NAVY})),P(R(topic,{s:20})),writeTable(null,[[''],['']],[CW],{rowH:520})],
};
// pick fillers to consume a gap: 'lg'≈3/4 page, 'md'≈1/2, 'sm'≈1/4
function fillGap(size,code,topic){
  const s=C.standards[code], t=topic||`this standard (${code})`;
  if(size==='lg')return [...FILL_LIB.retrieval(),...FILL_LIB.quickwrite(`In 3–4 sentences, explain the most important idea of ${t}. Use one key term.`),...FILL_LIB.stretch(`Make an evidence-based claim about ${t} — support it with two specifics and explain your reasoning.`)];
  if(size==='md')return [...FILL_LIB.quickwrite(`Summarize ${t} in your own words, then underline your key term.`),...FILL_LIB.sketch(`Draw and label a quick diagram that captures ${t}.`)];
  return FILL_LIB.connect(`How does ${t} connect to another standard in this unit, or to today?`);
}
function gap(h=140){return new Paragraph({spacing:{after:h},children:[R('',{s:12})]});}
// DOODLE / SKETCH zone — labeled cream bar + a tall open box for drawing (UDL: draw your thinking)
function doodle(label,note,h=1500){return [callout(label,[note]),
  table([new TableRow({height:{value:h,rule:HeightRule.ATLEAST},children:[cell(P(R(' ',{s:12}),{spacing:{after:0}}),{w:CW})]})],[CW])];}
function priorityBar(n,term,es){return table([new TableRow({children:[cell([
  P([R(`PRIORITY TERM ${n}`,{s:16,b:true,c:GOLD}),R(`     ${term}`,{s:24,b:true,c:WHITE}),R(`      ·   ES: ${es}`,{s:18,c:'D9D5C8'})],{spacing:{after:0}})],{w:CW,fill:NAVY})]})],[CW]);}
function retrievalBox(code){return [gap(120),
  callout('SPACED RETRIEVAL — quick recall (no notes)',['Pull it up cold to strengthen memory, then check your notes.']),
  writeTable(['Recall prompt','Your answer (from memory)'],[
    ['One key term or fact from THIS standard',''],
    ['One thing you learned EARLIER — how does it connect?',''],
  ],[3857,5935],{rowH:500,lines:1})];}
function vocabSelfCheck(code){const s=C.standards[code]; const W=[3092,1675,1675,1675,1675];
  const head=new TableRow({tableHeader:true,children:['Term','1 · never seen it','2 · heard it','3 · can use it','4 · can teach it'].map((h,i)=>cell(P(R(h,{s:15,b:true,c:i===0?NAVY:WHITE}),{align:i?AlignmentType.CENTER:AlignmentType.LEFT,spacing:{after:0}}),{w:W[i],fill:i===0?CREAM:NAVY}))});
  const rows=s.vocab.map(v=>new TableRow({children:[cell(P(R(v.term,{s:18,b:true}),{spacing:{after:0}}),{w:W[0]}),...[1,2,3,4].map(k=>cell(ruled(1),{w:W[k]}))]}));
  return [gap(40),
    callout('VOCABULARY SELF-CHECK · Knowledge Rating',['Rate each term NOW in pencil, then again at the END — growth is the goal; no penalty for “never seen it.”']),
    table([head,...rows],W),
    P([R('MAKE IT YOURS (RESPONSE CHOICE): ',{s:20,b:true,c:NAVY}),R('choose ONE term above and show you own it — write a sentence, sketch it, or give a real-world example.',{s:20})],{spacing:{before:60,after:40}}),
    ...ruled(2)];}
function sourceExtension(code){return [gap(120),
  callout('EXTEND & RE-ENGAGE (open to all)',['Push past the document — corroborate, contextualize, and judge its meaning.']),
  writeTable(['Historian move','Your response'],[
    ['Corroborate — what other source would confirm or complicate this one?',''],
    ['Contextualize — what was happening at the time that explains it?',''],
    ['So what? — why does this source still matter?',''],
  ],[4669,5123],{rowH:600}),
  callout('CONFIDENCE CHECK-IN',['Rate your understanding of this standard (1–4): ______    One thing to revisit: ____________________'])];}

// ================= COVER =================
const cover=[
  P(R((U.cover_era?U.cover_era+'   •   ':'')+'UNITED STATES GOVERNMENT & CIVICS (GC)   •   COURSE STANDARD EDITION',{s:20,b:true,c:GOLD}),{align:AlignmentType.CENTER,spacing:{before:200,after:220}}),
  P(R(BRANDTM.toUpperCase(),{s:44,b:true,c:NAVY}),{align:AlignmentType.CENTER,spacing:{after:40}}),
  P(R('TROOPTOTEACHER TECHNOLOGIES',{s:20,b:true,c:NAVY}),{align:AlignmentType.CENTER,spacing:{after:320}}),
  P(R('UNIT '+UNIT_NO,{s:52,b:true,c:RED}),{align:AlignmentType.CENTER,spacing:{after:60}}),
  P(R((U.title||COURSE),{s:32,b:true,c:NAVY}),{align:AlignmentType.CENTER,spacing:{after:120}}),
  P(R('COURSE STANDARD EDITION',{s:26,b:true,c:NAVY}),{align:AlignmentType.CENTER,spacing:{after:60}}),
  P(R(RANGE+'   •   Tennessee U.S. Government & Civics Standards   •   Grades 9–12',{s:22,c:INK}),{align:AlignmentType.CENTER,spacing:{after:300}}),
  callout('★ '+TNLABEL,[U.tn_connection||'']),
  P(R('One common workbook designed for learner variability. Every student works toward the same Tennessee standards; supports vary the means, not the goal or the ceiling.',{s:22,i:true,c:NAVY}),{align:AlignmentType.CENTER,spacing:{before:280,after:180}}),
  P(R('Release-Ready · Pilot Edition',{s:22,b:true,c:NAVY}),{align:AlignmentType.CENTER,spacing:{after:40}}),
  P(R('© 2026 TroopToTeacher Technologies LLC. All rights reserved.   ISBN: [to be assigned]',{s:18,c:GREY}),{align:AlignmentType.CENTER}),
  PB()];

// ================= FRONT MATTER =================
const front=[
  H('Copyright, Ownership & Framework',1),
  P(R(BRANDTM+' — '+(U.code||'Unit 1')+': '+(U.title||COURSE)+', Course Standard Edition.',{s:22,b:true})),
  P(R('© 2026 TroopToTeacher Technologies LLC. All rights reserved. This workbook is proprietary; reproduction or redistribution outside a licensed classroom is prohibited.',{s:22})),
  P(R('Source integrity. Every primary source in this unit is public-domain and cited to its holding repository (National Archives, Library of Congress). See the Source Library.',{s:22})),
  P(R('Reading provenance (district-clear). Close-Read passages are labeled “'+BRAND+'-authored instructional synthesis” — they build on the standard record and are not presented as primary sources.',{s:22})),
  P(R('Framework stack. This workbook anchors to Tennessee U.S. Government & Civics standards '+RANGE+' and the Social Studies Practices (SSP.01–SSP.06), and is designed on CAST UDL 3.0 and an MTSS support model.',{s:22})),
  P([R('Pacing. ',{s:22,b:true}),R('Each standard is built for ',{s:22}),R('one 45-minute class period.',{s:22,b:true}),R(' Each activity shows a ',{s:22}),R('⏱ ~ minutes',{s:22,b:true,c:GOLD}),R(' estimate at its heading. There is more here than one period holds — your teacher chooses which activities you do in class; the rest may become warm-ups, stations, or homework.',{s:22})]),
  PB(),
  H('Table of Contents',1), new TableOfContents('Contents',{hyperlink:true,headingStyleRange:'1-2'}), PB(),
  H('Tennessee Standards & SSP Crosswalk',1),
  P(R('Each standard below is taught to the full Course Standard expectation; the Social Studies Practices are embedded in every activity cycle.',{s:22})),
  dataTable(['Standard','Focus','Student Deck slides'],
    C.order.map(c=>[c,C.standards[c].title,`${C.standards[c].ref.range}`]),[1522,6240,2030]),
  H('Social Studies Practices (SSP.01–SSP.06)',2),
  P(R('SSP.01 Gather/evaluate sources · SSP.02 Critically examine a primary source · SSP.03 Synthesize evidence · SSP.04 Construct/communicate argument · SSP.05 Develop historical awareness · SSP.06 Chronological/spatial reasoning. Each Close Read, Primary Source/Data, and CER activity names the practices it builds.',{s:21})),
  PB(),
  H('Accessibility, UDL & Accommodations Matrix',1),
  P(R('One firm learning goal per standard; flexible, universal means. Supports are available by design and never lower the goal. They work alongside — never in place of — required IEP or 504 accommodations.',{s:22})),
  dataTable(['Universal support','What it is','Where it appears'],[
    ['CORE PATH','Essential instruction every student completes','Every activity'],
    ['LANGUAGE SUPPORT','Vocabulary, pronunciation, Spanish cognates','Word Bank, Guided/Light Backs'],
    ['RESPONSE CHOICE','Write, say/record, or diagram','Every activity'],
    ['SUPPORT OPTION','Optional scaffold that keeps the goal','Guided Support Back, Primary Source'],
    ['PROGRESS CHECK','Quick DOK-2/3 check to guide reteach/extend','Cornell Notes, Practice Quiz'],
    ['EXTENSION','Deeper challenge once the goal is met','Extension Bank, CER'],
  ],[2436,4514,2842]),
  H('How CAST UDL 3.0 is visible in this workbook',2),
  P(R('Multiple means of Engagement (response choice, relevance via Tennessee Connection), Representation (Word Bank, pronunciation, Spanish, Close-Read supports), and Action & Expression (write/say/diagram, Frayer, CER). No fixed-track labels appear.',{s:21})),
  H('My Support Plan (optional — you choose)',2),
  P(R('Supports are available by design. Check the ones you might try; you can change your mind any time.',{s:22})),
  writeTable(['Support I might use','When it would help me'],[
    ['Word Bank + Spanish column',''],
    ['Guided or Light Support Back',''],
    ['Response choice (say/record or diagram)',''],
    ['Sentence frames / Rehearsal Lab',''],
  ],[3451,6341],{rowH:640}),
  PB(),
  H('How to Use This Workbook',1),
  P(R('Each standard runs the same seven-activity cycle: (1) Vocabulary Word Bank, (2) Vocabulary Studio, (3) Direct-Teaching Cornell Notes with optional Guided and Light Support Backs, (4) Close Read, (5) Primary Source / Data Analysis, (6) Core Application Practice Quiz, (7) Constructed Response (CER). Work the CORE PATH; reach for SUPPORT OPTIONS as needed.',{s:22})),
  H('Label legend — these appear throughout every standard cycle',2),
  dataTable(['Label','Meaning'],[
    ['CORE PATH','The essential instruction every student completes.'],
    ['SUPPORT OPTION','An optional scaffold that keeps the goal, not lowers it.'],
    ['LANGUAGE SUPPORT','Vocabulary, pronunciation, and Spanish cognates for access.'],
    ['RESPONSE CHOICE','Show learning by writing, saying/recording, or diagramming.'],
    ['PROGRESS CHECK','A quick DOK-2/3 check that guides reteach or extend.'],
    ['EXTENSION','A deeper challenge once the goal is met.'],
  ],[2639,7153]),
  H('Before You Begin — Set a S.M.A.R.T. Goal',2,{brk:true}),
  P(R('Strong learners set goals — but a goal only helps if it is built well. First learn how, then write yours.',{s:22})),
  callout('WHAT MAKES A GOAL STRONG? Build it S.M.A.R.T.',[
    R('S — Specific: say exactly what you will be able to do (“explain how a bill becomes law,” not “do well”).',{s:20}),
    R('M — Measurable: how will you PROVE it? — a score, a diagram, or teaching a partner.',{s:20}),
    R('A — Achievable: a real stretch you can reach with effort — not too easy, not impossible.',{s:20}),
    R('R — Relevant: it connects to this unit’s big question.',{s:20}),
    R('T — Time-bound: name WHEN — “by the end of this unit.”',{s:20})]),
  callout('SEE THE DIFFERENCE',[
    R('Weak:  “I want to do good in government.”  (vague — nothing to measure)',{s:20}),
    R('S.M.A.R.T.:  “By the end of this unit I can explain how the three branches check each other, and prove it by teaching a partner and scoring 80%+ on the check.”',{s:20,b:true})]),
  P(R('This unit’s big question: '+EQ,{s:20,i:true,c:GREY})),
  callout('BUILD YOURS — write each piece on the lines, then combine them at the bottom',['Fill in each part of your goal. Use the lines.']),
  writeTable(['Part of my goal','Write your piece on the lines'],[
    ['S — Specific: what exactly will I be able to do?',''],
    ['M — Measurable: how will I prove it? (a score, a diagram, teaching a partner)',''],
    ['A — Achievable: what effort will it take to reach it?',''],
    ['R — Relevant: how does it connect to the big question above?',''],
    ['T — Time-bound: by when?',''],
  ],[3900,5892],{rowH:560,lines:2}),
  writeBox('PUT IT TOGETHER — my S.M.A.R.T. goal in one or two sentences:',3),
  PB()];

// ================= PER-STANDARD =================
function block(code){
  const s=C.standards[code], a=s.auth, r=s.ref, out=[];
  const L=code.replace('.','')+'-L0'+code.slice(-1);
  out.push(H(`Standard ${code} — ${s.title}`,1,{brk:true}));
  out.push(P([R(`TN Academic Standard ${code}: `,{s:22,b:true}),R(s.tn.replace(/^US\.\d+\s*[–-]\s*/,''),{s:22})],{spacing:{after:60}}));
  out.push(callout('LEARNING TARGETS — I can…',(s.targets||[s.target||s.ican.replace(/^I can /i,'')]).map(t=>R('•  I can '+t.replace(/^I can /i,'')+'.',{s:21}))));
  if(s.lenses) out.push(P([R('Lenses for this standard: ',{s:19,b:true,c:NAVY}),R(s.lenses,{s:19,c:GREY})],{spacing:{after:80}}));
  out.push(coreCallout('CORE PATH — the same for every student',['Every student works this standard at the same rigor: analyze the sources and vocabulary, then demonstrate learning on the Practice Quiz and CER. UDL and MTSS give you flexible ways in — they never lower the bar. Check yourself against the learning targets on the Cornell Notes page.']));
  if(s.tn_connection) out.push(callout('★ Tennessee Connection',[s.tn_connection]));
  out.push(callout('SET YOUR GOAL (self-direction)',['My goal for this standard — what will I be able to do, and how will I show it?']));
  out.push(...ruled(2));
  // Text HOOK — a provocative, standard-specific question (images live in the analysis activities, framed + cited).
  out.push(callout('HOOK — think before you dig in',[s.hook||'What is the big question behind this standard?']));
  out.push(...ruled(2));
  out.push(callout('ACTIVATE — what do you already know or wonder?',['Jot what you already know or want to find out about this standard. You’ll come back to it.']));
  out.push(...ruled(3));
  out.push(callout('FIRST IMPRESSIONS — before you dig in (you’ll revisit this at the end)',['In your own words: what do you think this standard is about, and why might it matter to you or your community? Write 2–3 sentences.']));
  out.push(...ruled(3));
  // Activity 1 — Word Bank
  out.push(H(`Activity 1 — Vocabulary (Part A: Reference / Word Bank) — ${code}`,2,{brk:true,mins:10}));
  out.push(P(R('Use this word bank throughout the standard. The Spanish column supports access, not translation of assessment.',{s:21}),{spacing:{after:60}}));
  out.push(dataTable(['Term','Student-friendly meaning','Spanish'],s.vocab.map(v=>[
    new TextRun({text:v.term,bold:true,size:SZ(20),font:FONT,color:INK}), v.def, v.es]),[2723,4347,2722]));
  out.push(callout('LANGUAGE SUPPORT',['Pronunciations: '+s.vocab.filter(v=>v.say).map(v=>`${v.term} (${v.say})`).join('; ')+'.']));
  out.push(...vocabSelfCheck(code));
  out.push(...FILL_LIB.quickwrite('Which of these terms do you think will matter MOST for this standard, and why? You’ll revisit this at the end.'));
  // Activity 2 — Frayer
  out.push(H(`Activity 2 — Vocabulary Studio (Frayer-inspired) — ${code}`,2,{brk:true,mins:7}));
  out.push(callout('RESPONSE CHOICE',['Complete each studio by writing, speaking, or diagramming.']));
  a.frayer.forEach((term,fi)=>{const v=s.vocab.find(x=>x.term===term)||s.vocab[0];
    out.push(gap(fi===0?30:100));
    out.push(priorityBar(fi+1,term,v.es));
    out.push(P([R('Word-bank meaning to build on: ',{s:20,b:true}),R(v.def,{s:20})]));
    out.push(writeTable(['Definition (in your own words)','Characteristics'],[['',''],['Examples','Non-examples'],['','']],[4896,4896],{rowH:600}));
    out.push(callout('Use it to explain',['Write one sentence that uses “'+term+'” to explain this standard.']));
    out.push(...ruled(1));});
  out.push(gap(50));
  out.push(callout('CONNECT THE TERMS (UDL · build understanding)',['How do these priority terms fit together? Write or sketch how one leads to or affects another.']));
  out.push(...ruled(2));
  // Activity 3 — Cornell Notes — FRONT (note-taking; the whole page is writing space)
  out.push(H(`Activity 3 — Direct Teaching Cornell Notes — ${code}`,2,{brk:true,mins:20}));
  out.push(P(R(`${code} — ${s.title}  •  Lean Student Deck slides ${r.range}  •  direct-teaching slides ${r.dt}`,{s:20,c:GREY})));
  out.push(P(R('Your learning targets are on this standard’s opening page — take notes that help you meet them.',{s:19,i:true,c:GREY}),{spacing:{after:60}}));
  // Cornell note-taking — brand layout: navy header, narrow cue col + wide notes col, ruled lines
  out.push(cornell(s.cues||['Main idea?','Key term →','Why does it matter?','Connect it →'],
    'My notes — write your notes here',3));
  out.push(...ruled(4));
  out.push(...doodle('DOODLE ZONE — draw your thinking (UDL · another way in)','Need another way in? Sketch the key idea, a quick timeline, or how the pieces connect. Words optional.',2050));
  // Cornell Notes — BACK (keep going, then process & check)
  out.push(H(`Cornell Notes — keep going, then process & check — ${code}`,2,{brk:true}));
  out.push(callout('UDL · CHOOSE HOW YOU CAPTURE IDEAS (same target for everyone)',['Keep going with your notes: WRITE on the lines, DRAW or diagram in the box, or do both — your choice. You may also record your notes aloud.']));
  out.push(splitDrawWrite('DRAW / DIAGRAM — sketch the idea, a timeline, or how the pieces connect','WRITE — keep taking notes on the lines',2700,6));
  out.push(callout('Key terms to list',[s.vocab.map(v=>v.term).join(' · ')]));
  out.push(writeBox('Summary — In your own words (2–3 sentences)',4));
  out.push(table([new TableRow({children:[cell([
    P(R('PROGRESS CHECK · one question',{s:21,b:true,c:NAVY}),{spacing:{after:60}}),
    P(R(s.cfu.stem,{s:22,b:true}),{spacing:{after:60}}),
    ...['A','B','C','D'].map(x=>P(R(`${x}.   ${s.cfu.options[x]}`,{s:21}),{indent:{left:360},spacing:{after:30}})),
    P(R('Commit before you move on — mark it, say it, or explain it aloud.',{s:19,i:true,c:GREY}),{spacing:{after:0}})
  ],{w:CW,fill:CREAM})]})],[CW]));
  out.push(callout('CHECK YOURSELF — how am I doing?',[
    R('Which learning targets (on this standard’s opening page) can you now meet? Tick the number; circle any you still need help with.',{s:20,i:true,c:GREY}),
    R((s.targets||['1']).map((t,i)=>`☐ ${i+1}`).join('        '),{s:24,b:true})]));
  out.push(writeBox('My 12–15 word headline for this standard',2));
  // Guided Support Back
  out.push(H(`Guided Support for the Cornell Notes — ${code}`,3,{brk:true}));
  out.push(P(R('These scaffolds support ONLY the Cornell notes — use them to take and process those notes. Optional and easy to set aside; not a separate assignment or a label.',{s:20,i:true})));
  out.push(dataTable(['Key vocabulary','What it means'],s.vocab.map(v=>[
    new TextRun({text:v.term,bold:true,size:SZ(20),font:FONT,color:INK}),v.def]),[3248,6544]));
  out.push(P(R('Break it into steps:',{s:21,b:true})));
  out.push(P(R('1) Name one cause or effect.    2) Give one piece of evidence.    3) Write one sentence explaining the link.',{s:20})));
  out.push(callout('Sentence frame',['One key cause/effect of '+s.title.split(':')[0].toLowerCase()+' was ______, shown by ______, which mattered because ______.']));
  out.push(callout('Modeled example (one worked note — yours will differ)',['A key idea of '+s.title.split(':')[0].toLowerCase()+' was '+s.vocab[0].term+': '+s.vocab[0].def]));
  out.push(callout('GUIDED NOTE REHEARSAL LAB — practice ONE note, step by step',['Build one good note here first, then copy it onto your Cornell page. Name the idea → give one piece of evidence → explain the link → write a short headline.']));
  out.push(writeTable(['Step','Rehearse it here'],[['Name it',''],['Evidence',''],['Explain',''],['Headline','']],[2639,7153],{rowH:760}));
  out.push(writeBox('TRANSFER CHECK — move one rehearsed idea onto the front notes',3));
  // Light Support Back
  out.push(H(`Light Support for the Cornell Notes — ${code}`,3,{brk:true}));
  out.push(P(R('A lighter scaffold for the SAME Cornell notes. Try the notes first; reach for this only if you need it.',{s:20,i:true})));
  out.push(writeTable(['Key vocabulary','Finish the idea — “This term means …”'],
    s.vocab.map(v=>[v.term,'']),[3248,6544],{lines:2}));
  out.push(P(R('Guiding questions — answer on the lines below (or in your front notes):',{s:21,b:true})));
  a.tdq.forEach(q=>out.push(P(R('• '+q,{s:20}))));
  out.push(...ruled(6));
  out.push(gap(80));
  out.push(callout('WHICH CUE STILL NEEDS WORK?',['Circle the Cornell cue from the front page you still need help with, and tell your teacher so we can go over it.']));
  out.push(callout('LIGHT PROCESSING LAB',['Answer one guiding question from above in a full sentence, in your own words.']));
  out.push(...ruled(6));
  // Activity 4 — Close Read
  out.push(H(`Activity 4 — Close Read — ${code}`,2,{brk:true,mins:15}));
  out.push(P(R('Reading type: '+BRAND+'-authored instructional synthesis. This is not a primary source. Builds SSP.03 (synthesize) and SSP.05 (historical awareness).',{s:20,i:true,c:GREY})));
  out.push(callout('CORE PATH',[a.close]));
  out.push(callout('LANGUAGE SUPPORT',['Key terms to know first: '+s.vocab.slice(0,2).map(v=>v.term).join(', ')+'. Read once for the gist, then again for evidence.']));
  out.push(P(R('Text-dependent questions (answer in the Evidence Lab below or aloud):',{s:21,b:true})));
  a.tdq.forEach((q,i)=>out.push(P(R(`${i+1}. ${q}`,{s:20}))));
  out.push(P(R('RESPONSE CHOICE: answer any question by writing in the Evidence Lab, saying/recording it, or diagramming it.',{s:20,i:true})));
  out.push(callout('CLOSE-READ EVIDENCE LAB',['Log evidence from the passage below.']));
  out.push(writeTable(['Question / claim','Exact passage evidence','What the evidence shows'],[['','',''],['','','']],[3264,3264,3264],{rowH:600,lines:2}));
  const gmap=(IMG[code]||{}).map;
  if(s.geo && !gmap){out.push(gap(100));
    out.push(...doodle('GEOGRAPHER’S LENS (G · SSP.06) — sketch & label the geography',s.geo+' Then draw a quick map below and label at least two places.',1050));}
  else out.push(...retrievalBox(code));
  // Geographer's Lens map page — standards with a verified period map
  if(gmap){
    out.push(H(`Geographer’s Lens — ${code}`,2,{brk:true,mins:10}));
    out.push(P(R('Analyze this period map as a primary source. Geographer’s lens (G) · builds SSP.06.',{s:20,i:true,c:GREY})));
    out.push(...sourceImage(gmap,{max:540}));
    if(s.geo) out.push(callout('MAP TASK',[s.geo]));
    out.push(writeTable(['Map question','Your answer'],[
      ['What does the map show, and where?',''],
      ['What pattern or movement do you see?',''],
      ['How does the geography connect to this standard?',''],
      ['What does this map leave out or make hard to see?',''],
    ],[3857,5935],{lines:2}));
    out.push(...doodle('MARK UP THE MAP (draw your thinking)','On the map above, circle or label what you notice — routes, regions, clusters — then sketch the pattern here in your own quick map.',1150));
  }
  // Activity 5 — Primary Source / Data (HIPPO)
  out.push(H(`Activity 5 — Primary Source / Data Analysis — ${code}`,2,{brk:true,mins:15}));
  const im=(IMG[code]||{});
  if(im.anchor){
    out.push(P(R(`Primary source (${im.anchor.medium}) — analyze it with HIPPO. Builds SSP.01–SSP.02.`,{s:20,i:true,c:GREY})));
    out.push(...sourceImage(im.anchor,{max:470}));
  } else {
    const src=s.sources[0];
    out.push(P(R('Document (text primary source — analyze with HIPPO). Builds SSP.01–SSP.02.',{s:20,i:true,c:GREY})));
    out.push(callout(src.title.toUpperCase(),['“'+src.quote+'”']));
    out.push(P(R(`Source: ${src.who}, ${src.date}. ${src.repo}. Public domain. ${src.url}`,{s:18,c:GREY})));
  }
  out.push(callout('FIRST LOOK — before you analyze',['Jot 3–4 things you notice in the source (details, words, people, dates). No wrong answers.']));
  out.push(...ruled(4));
  out.push(writeTable(['HIPPO — analyze the source (prompt)','Your analysis'],[
    ['H — Historical context: what was happening when this was created?',''],
    ['I — Intended audience: who was meant to see or obey it?',''],
    ['P — Purpose: why was it created?',''],
    ['P — Point of view: whose perspective does it reflect?',''],
    ['O — Outside connection: how does it connect to this standard?',''],
  ],[4263,5529],{lines:4}));
  // Activity 5 BACK PAGE — support + synthesis + historian extension (fills the second page)
  out.push(H(`Primary Source Analysis — go deeper — ${code}`,2,{brk:true}));
  out.push(callout('SUPPORT OPTION (use if you need it)',['Sentence frame: This source shows ______ because it ______, which reveals ______.']));
  out.push(callout('SOURCE SYNTHESIS — put it together (SSP.03)',['In 2–3 sentences: what does this source reveal about this standard, and how do you know? Cite one specific detail from it.']));
  out.push(...ruled(5));
  out.push(callout('THINK LIKE A HISTORIAN — corroborate or challenge (SSP.03)',['Name ONE other source that could CONFIRM this one, and ONE way it could COMPLICATE or CHALLENGE it — or, whose voice is missing here?']));
  out.push(...ruled(5));
  out.push(callout('SO WHAT? — why this source still matters today',['In 1–2 sentences: why does this source still matter for understanding government today?']));
  out.push(...ruled(4));
  out.push(callout('CONFIDENCE CHECK-IN',['Rate your understanding of this standard (1–4): ______    One thing to revisit: ____________________']));
  // Activity 6 — Practice Quiz
  out.push(H(`Activity 6 — Core Application: Practice Quiz — ${code}`,2,{brk:true,mins:8}));
  out.push(callout('RESPONSE CHOICE',['Commit to an answer by marking it, saying it, or explaining it aloud before checking. Answer key is in the Teacher Guide (kept separate).']));
  const items=[...a.quiz, {id:`u1-${code.toLowerCase().replace('.','')}-dok${s.cfu.dok}-tc`,dok:s.cfu.dok,stem:s.cfu.stem,opts:s.cfu.options}];
  items.forEach(q=>{
    out.push(P(R(`[DOK ${q.dok} · item ${q.id} · pre-field-test]`,{s:18,b:true,c:GREY})));
    out.push(P(R(q.stem,{s:21,b:true})));
    ['A','B','C','D'].forEach(x=>out.push(P(R(`${x}. ${q.opts[x]}`,{s:20}),{indent:{left:260},spacing:{after:20}})));
  });
  out.push(gap(100));
  out.push(callout('STRETCH — think like a test-writer (open to all)',['Write your OWN DOK-3 question for this standard, then a one-sentence answer key. Use the supports below — everyone can do this.']));
  out.push(callout('HOW TO WRITE A DOK-3 QUESTION (supports)',[
    'DOK-3 = strategic thinking: the reader must analyze, compare, evaluate, or justify using evidence — and there should be more than one defensible answer (not a fact you can just look up).',
    'Sentence starters: “Why did ______ lead to ______?”  ·  “Which mattered more — ______ or ______ — and why?”  ·  “What is the BEST evidence that ______?”  ·  “Evaluate whether ______.”  ·  “Defend or challenge: ______.”',
    'Frame:  [Analyze / Evaluate / Justify]  +  [something from THIS standard]  +  “using evidence.”',
    'Quick check: does my question make the reader THINK and use evidence? If yes, it’s DOK-3.']));
  out.push(gap(120));
  out.push(writeBox('NOW WRITE YOUR DOK-3 QUESTION HERE',5));
  out.push(writeBox('YOUR ANSWER KEY — one clear, defensible sentence',4));
  // Activity 7 — CER
  out.push(H(`Activity 7 — Constructed Response (CER) — ${code}`,2,{brk:true,mins:15}));
  out.push(callout('BIG-QUESTION ORGANIZER (before you write) — '+EQ,['Plan your argument here, then use it to write your claim, evidence, and reasoning below.']));
  out.push(writeTable(['Plan your argument','Your quick notes (from this standard)'],
    [['My claim (answer the prompt)',''],['Evidence 1 (a source or fact)',''],['Reasoning (why it proves the claim)','']],[3096,6696],{lines:1}));
  out.push(callout('CONSTRUCTED RESPONSE (CER) — builds SSP.04 Argumentation',[a.cer]));
  out.push(new Table({width:{size:CW,type:WidthType.DXA},columnWidths:[2233,7559],rows:[
    new TableRow({tableHeader:true,children:[cell(P(R('Part',{s:18,b:true,c:WHITE}),{spacing:{after:0}}),{w:2233,fill:NAVY}),cell(P(R('Write here',{s:18,b:true,c:WHITE}),{spacing:{after:0}}),{w:7559,fill:NAVY})]}),
    ...[['Claim',4],['Evidence (two specifics)',6],['Reasoning',5]].map(([lab,n])=>new TableRow({children:[cell(P(R(lab,{s:20,b:true}),{spacing:{after:0}}),{w:2233}),cell(ruled(n),{w:7559})]}))
  ]}));
  // Activity 7 BACK PAGE — self-grade against the rubric + supports (self-grading spread)
  out.push(H(`Constructed Response — self-grade & supports — ${code}`,2,{brk:true}));
  out.push(callout('SELF-GRADE — score your own CER against the rubric below',['Reread your response, then circle the level that best fits each part. Being honest here is how you level up.']));
  out.push(dataTable(['Level','Claim','Evidence','Reasoning'],[
    ['4 — Strong','Precise, defensible','2+ accurate, specific','Explains HOW evidence proves the claim'],
    ['3 — Proficient','Clear','2 accurate','Explains the link'],
    ['2 — Developing','General','1 accurate','Partial link'],
    ['1 — Beginning','Unclear / missing','Missing / inaccurate','No reasoning'],
  ],[1800,2664,2664,2664]));
  out.push(callout('MY SCORE',['Claim: ____ / 4        Evidence: ____ / 4        Reasoning: ____ / 4        TOTAL: ____ / 12']));
  out.push(callout('SUPPORTS — sentence frames (use if you need them)',['Claim: \u201c______ because ______.\u201d','Evidence: \u201cOne example is ______ (from ______).  Another is ______.\u201d','Reasoning: \u201cThis proves my claim because ______, which shows ______.\u201d']));
  out.push(callout('REVISE — make your lowest-scoring part stronger',['Pick the part you scored lowest and rewrite it here — better:']));
  out.push(...ruled(6));
  // Exit Ticket — end-of-standard formative (vetted item from the question bank; key + next steps teacher-side)
  const xt=EXIT[code];
  if(xt) out.push(table([new TableRow({children:[cell([
    P([R('EXIT TICKET — before you leave  ',{s:21,b:true,c:NAVY}),R(`[item ${xt.id} · DOK ${xt.dok} · pre-field-test]`,{s:16,c:GREY})],{spacing:{after:60}}),
    P(R(xt.stem,{s:22,b:true}),{spacing:{after:50}}),
    ...xt.choices.map(c=>P(R(`${c.id}.   ${c.text}`,{s:21}),{indent:{left:360},spacing:{after:24}})),
    P([R('Show what you know (your choice): ',{s:20,b:true,c:NAVY}),R('mark the best answer, say it, or explain it — then rate how sure you are:  ☐ Not yet   ☐ Getting there   ☐ Got it',{s:20})],{spacing:{before:40,after:0}}),
    P(R('Answer key and next steps are in the Teacher Guide.',{s:18,i:true,c:GREY}),{spacing:{before:20,after:0}})
  ],{w:CW,fill:CREAM})]})],[CW]));
  // ---- Standard support page (kept OUT of the activity flow; Activities 1-7 stay byte-identical to the brand) ----
  out.push(H(`UDL Access, Choice & Reflection — ${code}`,2,{brk:true}));
  out.push(callout('UDL ACCESS & MTSS SUPPORT (this standard)',['UDL 3.0 (CAST, 2024): read-aloud on request · key terms glossed (EN/ES) · respond in writing, speech, or a labeled diagram · large-print & screen-reader friendly. Same learning target for everyone; supports vary the means, not the ceiling.','MTSS: Tier 1 — this core lesson for all · Tier 2 — small-group reteach of this standard using its Cornell cues + graphic organizer, then re-check · Tier 3 — intensive 1:1 with concrete→representational→abstract scaffolding, progress-monitored to the same standard.']));
  out.push(callout('SHOW WHAT YOU KNOW — YOUR WAY (same CER rubric, same standard)',['Build your Claim–Evidence–Reasoning in whichever mode lets you think best — the standard and the CER rubric are identical for every mode; the mode changes how you SHOW it, never what you are held to:','WRITE it  ·  SAY it aloud and record it (audio or video)  ·  DRAW and label a diagram that makes the argument  ·  BUILD a model or artifact and caption its claim, evidence, and reasoning.','You may ask for a word processor, speech-to-text, a scribe, or a sentence/argument frame — these change how you produce, not the standard you meet.']));
  out.push(callout('CHOICE & VOICE — you decide how to go deeper (pick ONE)',['You choose your path to show this standard — every option meets the same target:','DEFEND a term: pick the vocabulary word that matters most and argue why in 2–3 sentences.  ·  CONNECT it: pick a current event, your community, or your own life and explain how this standard shows up there.  ·  TAKE A SIDE: pick one debatable question and argue your position with evidence.','Your pick is yours — bring what matters to you into the work.']));
  out.push(callout('REFLECT & CONNECT — how your thinking grew, and whose view you weighed',['Reflect (self-awareness): What did you believe about this topic BEFORE, and what changed AFTER? Name one thing to revisit.','Consider another view (empathy): Name one person or group who might see this standard differently than you; state their view fairly in one sentence — even if you disagree.','Norm (restorative): we critique ideas, not people; we assume good faith; we make room for every voice.']));
  return out;
}
const standards=[]; ORDER.forEach(c=>block(c).forEach(x=>standards.push(x)));

// ================= BACK MATTER =================
const back=[
  H('Your Tennessee Connection',1),
  callout('★ '+TNLABEL,[U.tn_connection||'']),
  P(R('Reflect (RESPONSE CHOICE): How does a Tennessee connection change the way you understand a national idea? Answer by writing, recording, or diagramming.',{s:21})),
  H('Tennessee Civics Investigation',2),
  P(R(U.tn_connection_task||'Investigate one way Tennessee government reflects an idea from this unit, and record what you find.',{s:22})),
  writeTable(['Prompt','Your findings'],[
    ['A Tennessee example connected to this unit',''],
    ['One source I could check (library, TN Secretary of State, TSLA, a representative’s office)',''],
    ['How it connects to a standard in this unit',''],
    ['One question I still have',''],
  ],[3451,6341],{rowH:760}),
  H('Progress Tracker & Cumulative Review',1),
  P(R('Track your Progress Check result for each standard and note one thing to revisit.',{s:22})),
  writeTable(['Standard','Progress Check (✓ / reteach)','One thing to revisit'],
    C.order.map(c=>[c,'','']),[1624,4084,4084],{rowH:620}),
  H('Optional Extension Bank (higher-DOK, open to all)',1),
  P(R('Any student may choose an extension. These are EXTENSION, not a track.',{s:22})),
  ...C.order.map(c=>P([R(`${c}: `,{s:21,b:true,c:NAVY}),R(C.standards[c].auth.cer.replace('Claim + Evidence + Reasoning: ',''),{s:21})])),
  H('Reusable Toolkit & Source Library',1),
  H('Written Response Rubric (CER)',2),
  dataTable(['Level','Claim','Evidence','Reasoning'],[
    ['4 — Strong','Precise, defensible','2+ accurate, specific','Explains how evidence proves the claim'],
    ['3 — Proficient','Clear','2 accurate','Explains the link'],
    ['2 — Developing','General','1 accurate','Partial link'],
    ['1 — Beginning','Unclear/missing','Missing/inaccurate','No reasoning'],
  ],[1827,2655,2655,2655]),
  H('Source Library — full citations & clickable links',2),
  ...C.order.flatMap(c=>[P(R(`${c} — ${C.standards[c].title}`,{s:21,b:true,c:NAVY})),
    ...C.standards[c].sources.map(x=>P([R(`${x.title}. `,{s:19,b:true}),R(`${x.who}, ${x.date}. ${x.repo}. Public domain. `,{s:19}),R(x.url,{s:17,c:'2A5DB0'})]))]),
  H(U.perspectives_title||'Multiple Perspectives',1),
  P(R((U.perspectives_intro||'This section presents multiple perspectives grounded in this unit’s sourced record.'),{s:22})),
  ...(U.perspectives||[]).flatMap(([h,b])=>[H(h,2),P(R(b,{s:21}))]),
  H('Unit Reflection',2),
  P(R('Return to the unit’s big question: '+EQ+' Write a final claim with two pieces of evidence from different standards.',{s:22})),
  writeTable(['Part','Write here'],[['My claim',''],['Evidence 1 (standard: ___)',''],['Evidence 2 (standard: ___)',''],['Why it matters today','']],[2639,7153],{rowH:820})];

// ================= ASSEMBLE =================
const header=new Header({children:[P(R(BRANDTM+' · '+(U.code||'Unit 1')+' · Course Standard Edition',{s:16,b:true,c:GOLD}),{align:AlignmentType.RIGHT,spacing:{after:0}})]});
const footer=new Footer({children:[new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:0},children:[
  R(BRANDTM+' · '+(U.code||'Unit 1')+' (Course Standard)   © 2026 TroopToTeacher Technologies LLC   |   Page ',{s:15,c:GREY}),
  new TextRun({children:[PageNumber.CURRENT],size:15,color:GREY,bold:true,font:FONT})]})]});
const doc=new Document({creator:'TroopToTeacher Technologies LLC',title:BRAND+' — '+(U.code||'Unit 1')+' Course Standard Student Workbook',
  features:{updateFields:true},
  styles:{default:{document:{run:{font:FONT,size:SZ(22),color:INK}}},paragraphStyles:[
    {id:'Heading1',name:'Heading 1',basedOn:'Normal',next:'Normal',quickFormat:true,run:{font:FONT,size:36,bold:true,color:NAVY},paragraph:{spacing:{before:220,after:90},outlineLevel:0,keepNext:true}},
    {id:'Heading2',name:'Heading 2',basedOn:'Normal',next:'Normal',quickFormat:true,run:{font:FONT,size:28,bold:true,color:NAVY},paragraph:{spacing:{before:150,after:80},outlineLevel:1,keepNext:true}},
    {id:'Heading3',name:'Heading 3',basedOn:'Normal',next:'Normal',quickFormat:true,run:{font:FONT,size:24,bold:true,color:RED},paragraph:{spacing:{before:120,after:70},outlineLevel:2,keepNext:true}},
  ]},
  sections:[{properties:{page:{size:{width:12240,height:15840},margin:{top:1152,bottom:1152,left:1224,right:1224,header:720,footer:720}}},
    headers:{default:header},footers:{default:footer},children: PREVIEW ? [P(R(`PREVIEW — Unit 1 · first ${SAMPLE} standards (activities only, ruled-line writing) — for review`,{s:24,b:true,c:NAVY}),{align:AlignmentType.CENTER,spacing:{after:120}}), ...standards] : [...cover,...front,...standards,...back]}]});
const OUTFILE=PREVIEW?`deliverables/Unit3_PREVIEW_${ONLYSTD||SAMPLE+'std'}.docx`:'deliverables/Unit3_Student_Workbook_CourseStandard'+(LP>1?'_LargePrint':'')+'.docx';
Packer.toBuffer(doc).then(b=>{fs.writeFileSync(OUTFILE,b);console.log('WROTE',OUTFILE,b.length,'bytes');});
