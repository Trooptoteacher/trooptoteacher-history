// Unit 6 Course Standard STUDENT WORKBOOK — docx-js, EXACT Unit 5 template (no deviation).
// Design tokens extracted from Unit5_Student_Workbook_CourseStandard.docx.
const fs=require('fs'); const D=require('docx');
const {Document,Packer,Paragraph,TextRun,HeadingLevel,AlignmentType,Table,TableRow,TableCell,
  WidthType,BorderStyle,ShadingType,PageBreak,TableOfContents,Header,Footer,PageNumber,HeightRule,ImageRun}=D;
const C=JSON.parse(fs.readFileSync('analysis/unit6_content.json','utf8'));
const IMG=fs.existsSync('analysis/unit6_images.json')?JSON.parse(fs.readFileSync('analysis/unit6_images.json','utf8')):{};
const EXIT=fs.existsSync('analysis/unit6_exit_tickets.json')?JSON.parse(fs.readFileSync('analysis/unit6_exit_tickets.json','utf8')):{};
// Deck map: exact TEACHER-deck slide numbers per activity (skill: history-hack-
// workbook-print-bundle — workbook points to the teacher deck for follow-along).
const MAP=fs.existsSync('analysis/unit6_deck_map.json')?JSON.parse(fs.readFileSync('analysis/unit6_deck_map.json','utf8')):{activity_slides:{}};
const ASSESS=fs.existsSync('analysis/unit6_assessment.json')?JSON.parse(fs.readFileSync('analysis/unit6_assessment.json','utf8')):{formative:{}};
function fmtSlides(arr){ if(!arr||!arr.length) return '';
  const a=[...arr].sort((x,y)=>x-y);
  const contig=a.every((v,i)=>i===0||v===a[i-1]+1);
  if(a.length===1) return 'slide '+a[0];
  return (contig?('slides '+a[0]+'–'+a[a.length-1]):('slides '+a.join(', ')));
}
// "Role . slide(s) N" for an activity — the exact place a student finds it on the deck.
function deckRef(code,act,role){
  const sl=((MAP.activity_slides||{})[code]||{})['Activity '+act]||[];
  const s=fmtSlides(sl);
  return role+(s?(' · '+s):'');
}
const SAMPLE=process.env.SAMPLE?Number(process.env.SAMPLE):0; const ORDER=SAMPLE?C.order.slice(0,SAMPLE):C.order;
// docx ImageRun needs an explicit media type, else the library writes the part
// as "*.undefined" with no [Content_Types] entry -> invalid OOXML. Derive it.
const imgType=(f)=>{const e=(f||'').toLowerCase().split('.').pop();
  return e==='jpg'?'jpeg':(['jpeg','png','gif','bmp','svg'].includes(e)?e:'jpeg');};

// Cover hero image — the unit's curated public-domain photograph (app hero art).
const HERO={file:'analysis/assets/hero.jpg', w:1280, h:1030,
  cap:'“Into the Jaws of Death” — U.S. troops wade ashore under fire at Omaha Beach, Normandy, on D-Day, June 6, 1944.',
  cred:'Chief Photographer’s Mate Robert F. Sargent, U.S. Coast Guard / National Archives. Public domain.'};
function coverHero(rec,{maxW=380,maxH=290}={}){
  let w=Math.min(rec.w,maxW), h=Math.round(rec.h*(w/rec.w));
  if(h>maxH){ h=maxH; w=Math.round(rec.w*(h/rec.h)); }
  const out=[new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:40,after:30},
    border:{top:{style:BorderStyle.SINGLE,size:14,color:GOLD,space:8},bottom:{style:BorderStyle.SINGLE,size:14,color:GOLD,space:8}},
    children:[new ImageRun({data:fs.readFileSync(rec.file),type:imgType(rec.file),transformation:{width:w,height:h},
      altText:{title:'Unit cover image',description:rec.cap,name:'cover-hero'}})]})];
  out.push(P(R(rec.cap,{s:18,i:true,c:GREY}),{align:AlignmentType.CENTER,spacing:{after:8}}));
  out.push(P(R('Source: '+rec.cred,{s:18,c:GREY}),{align:AlignmentType.CENTER,spacing:{after:110}}));
  return out;
}
const STUDENT_SUPPORTS=process.env.STUDENT_SUPPORTS==='1'; // legacy Cornell-only support backs; superseded by per-activity supportsBack() below
// ── Per-activity UDL 3.0 / MTSS supports on the VERSO. Default INCLUDED (skill:
// history-hack-workbook-print-bundle §1 Duplex Law); SUPPORTS=0 → single-sided
// (activity only). Four-rung ladder: frames → cloze+word bank → how-to+model →
// try-it + self-check. Supports add ways IN; never lower the bar or replace IEP/504.
const SUPPORTS=process.env.SUPPORTS!=='0';
const ACT_NAMES={1:'Vocabulary Word Bank',2:'Vocabulary Studio',3:'Cornell Notes',4:'Close Read',5:'Primary Source (HIPPO)',6:'Practice Quiz',7:'Constructed Response (CER)'};
function supportsBack(n,code,s,a){
  if(!SUPPORTS) return [];
  const V=s.vocab||[]; const t0=V[0]||{term:s.title,def:''}; const t1=V[1]||t0;
  const topic=(s.title||code).split(':')[0];
  const RUNG=(k,label,lines)=>callout(`RUNG ${k} · ${label}`,lines);
  const out=[H(`Supports · Activity ${n} — ${ACT_NAMES[n]} — ${code}`,3,{brk:true})];
  out.push(P(R('Optional — supports the activity on the front (UDL 3.0 · MTSS). Print duplex to include. More ways in; the bar stays the same. Not a replacement for an IEP/504.',{s:19,i:true,c:GREY}),{spacing:{after:70}}));
  if(n===1){
    out.push(RUNG(1,'Frame',['This term, ______, means ______ in my own words. I know because ______.']));
    out.push(RUNG(2,'Cloze + word bank',['Word bank: '+V.map(v=>v.term).join(' · '),`Fill in: ${t0.term} is ${'_'.repeat(22)}.   ${t1.term} is ${'_'.repeat(22)}.`]));
    out.push(RUNG(3,'How-to + worked model',['Learn a term in 4 moves — SAY it · DEFINE it in your own words · USE it in a sentence · PICTURE it.',`Model — ${t0.term}: “${t0.def}”  →  In my words: ______.`]));
    out.push(RUNG(4,'Try it + self-check',['Use 2 terms in your own sentences about this standard:']));
    out.push(...ruled(4));
    out.push(callout('Self-check',['☐ I can say each term   ☐ I can define it   ☐ I can use it in a sentence']));
  } else if(n===2){
    out.push(RUNG(1,'Frame',['Definition: ______.   One characteristic: ______.   Example: ______.   Non-example: ______.']));
    out.push(RUNG(2,'Cloze model (build on this)',[`${t0.term} means ${t0.def}`,'One example is ______.   One non-example is ______ because ______.']));
    out.push(RUNG(3,'How-to + worked model',['Build a Frayer: (1) define in your words, (2) list traits, (3) give a real example, (4) give a non-example and say why.',`Worked — ${t0.term}: example → ______ ; non-example → ______.`]));
    out.push(RUNG(4,'Try it + self-check',[`Quick Frayer for “${t1.term}”:`]));
    out.push(writeTable(['Definition (your words)','One example','One non-example'],[['','','']],[3216,3216,3216],{lines:2}));
    out.push(callout('Self-check',['☐ My example fits   ☐ My non-example shows the boundary   ☐ I can use the term']));
  } else if(n===3){
    out.push(RUNG(1,'Frame',['Cue: ______  →  Note: The key idea is ______, shown by ______.']));
    out.push(RUNG(2,'Cloze note',[`A key idea of ${topic.toLowerCase()} is ${t0.term}: ${t0.def} This matters because ______.`]));
    out.push(RUNG(3,'How-to + worked model',['Cornell notes: write the CUE (question) on the left, the NOTE (answer + evidence) on the right, then a 2–3 sentence summary.','Worked cue → note:  “Who benefited?” → ______ benefited because ______.']));
    out.push(RUNG(4,'Rehearse + transfer',['Rehearse one cue→note here, then copy your best line onto the front notes:']));
    out.push(writeTable(['Cue','Rehearse the note here'],[['',''],['','']],[2600,7048],{lines:2}));
    out.push(callout('Self-check',['☐ My note answers the cue   ☐ I gave evidence   ☐ I can summarize in 2–3 sentences']));
  } else if(n===4){
    const chunk=((s.close_sections&&s.close_sections[0])||['',''])[0]||topic;
    out.push(RUNG(1,'Frame',['The text says “______” (evidence).   This shows ______ (my answer).']));
    out.push(RUNG(2,'Cloze + word gloss',[`Gist of “${chunk}”: it is mainly about ______.`,'Glossary help: '+V.slice(0,2).map(v=>`${v.term} = ${v.def}`).join('   ')]));
    out.push(RUNG(3,'How-to + worked model',['Find evidence: (1) read the question, (2) find the sentence that answers it, (3) quote it, (4) say what it shows.','Worked — Q: main idea? → Evidence: “______.” → Shows: ______.']));
    out.push(RUNG(4,'Try it + self-check',[(a.tdq&&a.tdq[0])?('Answer on the lines: '+a.tdq[0]):'Answer one text-dependent question on the lines:']));
    out.push(...ruled(4));
    out.push(callout('Self-check',['☐ I quoted real evidence   ☐ I said what it shows   ☐ I answered the question asked']));
  } else if(n===5){
    out.push(RUNG(1,'Frame (HIPPO)',['H: When it was made, ______ was happening.   I: It was meant for ______.   P: It was made to ______.   P: It reflects the view of ______.   O: It connects to this standard by ______.']));
    out.push(RUNG(2,'Cloze',['This source was created during ______, meant for ______, in order to ______.']));
    out.push(RUNG(3,'How-to + worked model',['Analyze a source: ask who made it, when, for whom, and why — then what it reveals.','Worked — Purpose: the creator wanted ______, which tells us ______.']));
    out.push(RUNG(4,'Try it + self-check',['Complete two HIPPO parts on the lines (your choice):']));
    out.push(...ruled(4));
    out.push(callout('Self-check',['☐ I named context   ☐ I named purpose or point of view   ☐ I connected it to the standard']));
  } else if(n===6){
    out.push(RUNG(1,'Frame',['I can rule out ______ because ______.   My best answer is ______ because ______.']));
    out.push(RUNG(2,'Strategy checklist',['☐ Read the whole question   ☐ Predict before you look   ☐ Cross out two wrong choices   ☐ Pick the best answer, not just a true one']));
    out.push(RUNG(3,'How-to + worked model',['Attack an item: cover the choices, predict, then eliminate — two choices are usually clearly wrong.','Worked — rule out the off-topic choice and the too-extreme choice, then decide between the last two using the stem.']));
    out.push(RUNG(4,'Reteach + self-check',['Missed one? Reread your Cornell notes for: '+V.map(v=>v.term).slice(0,3).join(' · '),'Confidence now (1–4): ____   One thing to revisit: ____________________']));
  } else if(n===7){
    out.push(RUNG(1,'Frame (CER)',['Claim: I believe ______.   Evidence: For example, ______.   Reasoning: This proves my claim because ______.']));
    out.push(RUNG(2,'Cloze paragraph',['______ (claim). One piece of evidence is ______. This matters because ______, which shows ______.']));
    out.push(RUNG(3,'How-to + model',['Write a CER: state a claim, give two pieces of evidence, explain how each proves the claim.','Model — Claim: ______. Evidence 1: ______. Reasoning: because ______.']));
    out.push(RUNG(4,'Draft it + self-check',['Draft your CER on the lines, then check it:']));
    out.push(...ruled(5));
    out.push(callout('Self-check',['☐ Clear claim   ☐ Two pieces of evidence   ☐ Reasoning links evidence to claim']));
  }
  return out;
}

// ---- exact tokens ----
const NAVY='1B2A4A', RED='B22234', GOLD='C89B3C', INK='1A1A1A', CREAM='F7F5EF', WHITE='FFFFFF', GREY='4B5563', BORD='D9D5C8';
const FONT='Calibri';
const CW=9648;                         // 6.7in content width (DXA)
const bd=(c=BORD,sz=4)=>({style:BorderStyle.SINGLE,size:sz,color:c});
const CELLB=(c=BORD)=>({top:bd(c),bottom:bd(c),left:bd(c),right:bd(c)});
function R(text,{s=22,b=false,i=false,c=INK,caps=false}={}){return new TextRun({text,size:s,bold:b,italics:i,color:c,font:FONT,allCaps:caps});}
function P(runs,{align,spacing,indent,border}={}){return new Paragraph({alignment:align,spacing:spacing||{after:100},indent,border,children:Array.isArray(runs)?runs:[runs]});}
function H(text,lvl,{brk=false,mins=null,deck=null}={}){const map={1:HeadingLevel.HEADING_1,2:HeadingLevel.HEADING_2,3:HeadingLevel.HEADING_3};
  const kids=[R(text,{s:lvl===1?36:lvl===2?28:24,b:true,c:lvl===3?RED:NAVY})];
  if(mins) kids.push(R(`    ⏱ ~${mins} min`,{s:18,b:true,c:GOLD}));
  // Deck key: ties this activity to its slide role so a student always knows which
  // slide the activity comes from (lesson-flow gate: role-based ▶ Deck reference).
  if(deck) kids.push(R(`    ▶ Deck · ${deck}`,{s:18,b:true,c:NAVY}));
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
// Records come from the verified History Hack primary-source bank (see references).
function sourceImage(rec,{max,maxH}={}){
  let w=max?Math.min(rec.w,max):rec.w, h=Math.round(rec.h*(w/rec.w));
  // Cap by HEIGHT too so tall portraits don't fill the page and push the HIPPO
  // analysis onto the next page (no-bleed rule for Activity 5).
  if(maxH && h>maxH){ h=maxH; w=Math.round(rec.w*(h/rec.h)); }
  const out=[new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:60},children:[
    new ImageRun({data:fs.readFileSync(rec.file),type:imgType(rec.file),transformation:{width:w,height:h},
      altText:{title:rec.title||'Primary source',description:rec.alt||rec.caption||rec.title||'Primary source image',name:rec.title||'source'}})]})];
  const cap=[rec.title, rec.creator?('· '+rec.creator):'', rec.year?('· '+rec.year):''].filter(Boolean).join(' ');
  out.push(P(R(cap,{s:19,b:true}),{spacing:{after:20}}));
  out.push(P(R(`Source: ${rec.citation||''} ${rec.rights||''}${rec.rightsUrl?(' '+rec.rightsUrl):''}`.trim(),{s:18,c:GREY}),{spacing:{after:rec.colorKey?12:40}}));
  if(rec.colorKey) out.push(P([R('▶ ',{s:18,b:true,c:GOLD}),R('Fine detail and color read best on screen. A large full-color version is on the projection-map slides at the end of the slide deck.',{s:18,i:true,c:GREY})],{spacing:{after:40}}));
  return out;
}
// compact image only (no caption/citation) — for the launch-page hook (source is cited in Activity 5)
function imgOnly(rec,max){const w=Math.min(rec.w,max), h=Math.round(rec.h*(w/rec.w));
  return new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:60},children:[
    new ImageRun({data:fs.readFileSync(rec.file),type:imgType(rec.file),transformation:{width:w,height:h},
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
  out.push(new Paragraph({spacing:{before:0,after:0,line:255,lineRule:'auto'},
    border:{bottom:{style:BorderStyle.SINGLE,size:4,color:'C9C4B5',space:3}},children:[R(' ',{s:18})]}));
  if(i<n-1) out.push(new Paragraph({spacing:{before:0,after:0,line:70,lineRule:'exact'},children:[R(' ',{s:2})]}));
}return out;}
function linesFor(h){return Math.max(2,Math.round(h/380));}
// writing table: label cells keep text; blank writing cells get ruled lines
function writeTable(headers,rows,widths,{rowH=560,lines,noSplit}={}){
  const trs=[];
  if(headers)trs.push(new TableRow({tableHeader:true,children:headers.map((h,i)=>cell(P(R(h,{s:18,b:true,c:i===0?NAVY:WHITE}),{spacing:{after:0}}),{w:widths[i],fill:i===0?CREAM:NAVY}))}));
  const nl=lines||linesFor(rowH);
  rows.forEach(r=>trs.push(new TableRow({cantSplit:noSplit,children:r.map((cx,i)=>cell(cx?[P(R(cx,{s:20,b:i===0}),{spacing:{after:0}})]:ruled(nl),{w:widths[i]}))})));
  return table(trs,widths);}
// cream label bar + ruled writing lines
function writeBox(label,nLines=3){return table([
  new TableRow({children:[cell(P(R(label,{s:21,b:true,c:NAVY}),{spacing:{after:0}}),{w:CW,fill:CREAM})]}),
  new TableRow({children:[cell(ruled(nLines),{w:CW})]})],[CW]);}
const PB=()=>new Paragraph({children:[new PageBreak()]});
// ---- white-space FILL rule: right-sized activities so no page is left blank ----
const FILL_LIB={
  quickwrite:(topic)=>[P(R('QUICK WRITE',{s:21,b:true,c:NAVY})),P(R(topic,{s:20})),writeTable(null,[[''],['']],[CW],{rowH:480})],
  sketch:(topic)=>[P(R('SKETCH IT (RESPONSE CHOICE — draw instead of write)',{s:21,b:true,c:NAVY})),P(R(topic,{s:20})),writeTable(null,[['']],[CW],{rowH:1600})],
  retrieval:()=>[P(R('RETRIEVAL — without looking back, list what you remember',{s:21,b:true,c:NAVY})),writeTable(null,[['1.'],['2.'],['3.']],[CW],{rowH:460})],
  stretch:(topic)=>[P(R('STRETCH (EXTENSION — open to all)',{s:21,b:true,c:RED})),P(R(topic,{s:20})),writeTable(null,[[''],['']],[CW],{rowH:560})],
  connect:(topic)=>[P(R('MAKE A CONNECTION',{s:21,b:true,c:NAVY})),P(R(topic,{s:20})),writeTable(null,[[''],['']],[CW],{rowH:520})],
};
// pick fillers to consume a gap: 'lg'≈3/4 page, 'md'≈1/2, 'sm'≈1/4
function fillGap(size,code,topic){
  const s=C.standards[code], t=topic||`this standard (${code})`;
  if(size==='lg')return [...FILL_LIB.retrieval(),...FILL_LIB.quickwrite(`In 3–4 sentences, explain the most important idea of ${t}. Use one key term.`),...FILL_LIB.stretch(`Argue a “who benefited / who bore the costs” claim about ${t} with two pieces of evidence.`)];
  if(size==='md')return [...FILL_LIB.quickwrite(`Summarize ${t} in your own words, then underline your key term.`),...FILL_LIB.sketch(`Draw and label a quick diagram that captures ${t}.`)];
  return FILL_LIB.connect(`How does ${t} connect to another standard in this unit, or to today?`);
}
function gap(h=140){return new Paragraph({spacing:{after:h},children:[R('',{s:12})]});}
// DOODLE / SKETCH zone — labeled cream bar + a tall open box for drawing (UDL: draw your thinking)
function doodle(label,note,h=1500){return [callout(label,[note]),
  table([new TableRow({height:{value:h,rule:HeightRule.ATLEAST},children:[cell(P(R(' ',{s:12}),{spacing:{after:0}}),{w:CW})]})],[CW])];}
function priorityBar(n,term,es){return table([new TableRow({children:[cell([
  P([R(`PRIORITY TERM ${n}`,{s:18,b:true,c:GOLD}),R(`     ${term}`,{s:24,b:true,c:WHITE}),R(`      ·   ES: ${es}`,{s:18,c:'D9D5C8'})],{spacing:{after:0}})],{w:CW,fill:NAVY})]})],[CW]);}
// GEOGRAPHY PRIORITY banner — geography is one of the most-missed EOC skills, so
// the Geographer's Lens is flagged like a priority term so it isn't skipped.
function geoPriorityBar(){return table([new TableRow({children:[cell([
  P([R('PRIORITY SKILL',{s:18,b:true,c:GOLD}),R('     Geography',{s:24,b:true,c:WHITE}),R('      ·   one of the most-missed skills on the EOC — do not skip it',{s:18,c:'D9D5C8'})],{spacing:{after:0}})],{w:CW,fill:NAVY})]})],[CW]);}
function retrievalBox(code){return [gap(120),
  callout('SPACED RETRIEVAL — quick recall (no notes)',['Pull it up cold to strengthen memory, then check your notes.']),
  writeTable(['Recall prompt','Your answer (from memory)'],[
    ['One key term or fact from THIS standard',''],
    ['One thing you learned EARLIER in this unit or course',''],
    ['How the two connect',''],
  ],[3800,5848],{rowH:600})];}
function vocabSelfCheck(code,fillLines=2){const s=C.standards[code]; const W=[3048,1650,1650,1650,1650];
  const head=new TableRow({tableHeader:true,children:['Term','1 · never seen it','2 · heard it','3 · can use it','4 · can teach it'].map((h,i)=>cell(P(R(h,{s:18,b:true,c:i===0?NAVY:WHITE}),{align:i?AlignmentType.CENTER:AlignmentType.LEFT,spacing:{after:0}}),{w:W[i],fill:i===0?CREAM:NAVY}))});
  const rows=s.vocab.map(v=>new TableRow({children:[cell(P(R(v.term,{s:18,b:true}),{spacing:{after:0}}),{w:W[0]}),...[1,2,3,4].map(k=>cell(ruled(1),{w:W[k]}))]}));
  return [
    callout('VOCABULARY SELF-CHECK · Knowledge Rating',['Rate each term NOW in pencil, then again at the END — growth is the goal; no penalty for “never seen it.”']),
    table([head,...rows],W),
    P([R('MAKE IT YOURS (RESPONSE CHOICE): ',{s:20,b:true,c:NAVY}),R('choose ONE term above and show you own it — write a sentence, sketch it, or give a real-world example.',{s:20})],{spacing:{before:60,after:40}}),
    ...ruled(fillLines)];}
function sourceExtension(code){return [gap(120),
  callout('EXTEND & RE-ENGAGE (open to all)',['Push past the document — corroborate, contextualize, and judge its meaning.']),
  writeTable(['Historian move','Your response'],[
    ['Corroborate — what other source would confirm or complicate this one?',''],
    ['Contextualize — what was happening at the time that explains it?',''],
    ['So what? — why does this source still matter?',''],
  ],[4600,5048],{rowH:600}),
  callout('CONFIDENCE CHECK-IN',['Rate your understanding of this standard (1–4): ______    One thing to revisit: ____________________'])];}

// ================= COVER =================
const cover=[
  P(R("1776 - 2026   •   AMERICA'S 250TH ANNIVERSARY   •   SEMIQUINCENTENNIAL EDITION",{s:20,b:true,c:GOLD}),{align:AlignmentType.CENTER,spacing:{before:200,after:220}}),
  P(R('U.S. HISTORY HACK™',{s:44,b:true,c:NAVY}),{align:AlignmentType.CENTER,spacing:{after:40}}),
  P(R('TROOPTOTEACHER TECHNOLOGIES',{s:20,b:true,c:NAVY}),{align:AlignmentType.CENTER,spacing:{after:320}}),
  P(R('UNIT 6',{s:52,b:true,c:RED}),{align:AlignmentType.CENTER,spacing:{after:60}}),
  P(R('World War II, 1939–1945',{s:32,b:true,c:NAVY}),{align:AlignmentType.CENTER,spacing:{after:120}}),
  P(R('COURSE STANDARD EDITION',{s:26,b:true,c:NAVY}),{align:AlignmentType.CENTER,spacing:{after:60}}),
  P(R('US.45 – US.58   •   14 Tennessee U.S. History Standards   •   Grades 9–12',{s:22,c:INK}),{align:AlignmentType.CENTER,spacing:{after:140}}),
  ...coverHero(HERO),
  callout('TENNESSEE CONNECTION · OAK RIDGE, THE “SECRET CITY”',['Tennessee helped build the atomic bomb. Oak Ridge — the “Secret City” — was a central site of the Manhattan Project (US.56), enriching the uranium used in the first atomic weapons. At its peak it held about 75,000 workers, many of whom never knew what they were making. Cordell Hull of Pickett County (US.58) helped found the United Nations, and Fort Campbell became home to the 101st Airborne (US.51).']),
  P(R('One common workbook designed for learner variability. Every student works toward the same Tennessee standards; supports vary the means, not the goal or the ceiling.',{s:22,i:true,c:NAVY}),{align:AlignmentType.CENTER,spacing:{before:150,after:110}}),
  P(R('Release-Ready · Pilot Edition',{s:22,b:true,c:NAVY}),{align:AlignmentType.CENTER,spacing:{after:40}}),
  P(R('© 2026 TroopToTeacher Technologies LLC. All rights reserved.   ISBN: [to be assigned]',{s:18,c:GREY}),{align:AlignmentType.CENTER}),
  PB()];

// ================= FRONT MATTER =================
const front=[
  H('Copyright, Ownership & Framework',1),
  P(R('U.S. History Hack™ — Unit 6: World War II (1939–1945), Course Standard Edition.',{s:22,b:true})),
  P(R('© 2026 TroopToTeacher Technologies LLC. All rights reserved. This workbook is proprietary; reproduction or redistribution outside a licensed classroom is prohibited.',{s:22})),
  P(R('Source integrity. Every primary source in this unit is public-domain and cited to its holding repository (National Archives, Library of Congress, HathiTrust). See the Source Library.',{s:22})),
  P(R('Reading provenance (district-clear). Close-Read passages are labeled “History Hack-authored instructional synthesis” — they build on the standard record and are not presented as primary sources.',{s:22})),
  P(R('Framework stack. This workbook anchors to Tennessee U.S. History standards US.45–US.58 and the Social Studies Practices (SSP.01–SSP.06), and is designed on CAST UDL 3.0 and an MTSS support model.',{s:22})),
  P([R('Pacing. ',{s:22,b:true}),R('Each standard is built for ',{s:22}),R('one 45-minute class period.',{s:22,b:true}),R(' Each activity shows a ',{s:22}),R('⏱ ~ minutes',{s:22,b:true,c:GOLD}),R(' estimate at its heading. There is more here than one period holds — your teacher chooses which activities you do in class; the rest may become warm-ups, stations, or homework.',{s:22})]),
  PB(),
  H('Table of Contents',1), new TableOfContents('Contents',{hyperlink:true,headingStyleRange:'1-2'}), PB(),
  H('Tennessee Standards & SSP Crosswalk',1),
  P(R('Each standard below is taught to the full Course Standard expectation; the Social Studies Practices are embedded in every activity cycle.',{s:22})),
  dataTable(['Standard','Focus','Lenses'],
    C.order.map(c=>[c,C.standards[c].title,`${(C.standards[c].lenses||'').replace(/ \([A-Z]+\)/g,'')}`]),[1400,5148,3100]),
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
  ],[2400,4448,2800]),
  H('How CAST UDL 3.0 is visible in this workbook',2),
  P(R('Multiple means of Engagement (response choice, relevance via Tennessee Connection), Representation (Word Bank, pronunciation, Spanish, Close-Read supports), and Action & Expression (write/say/diagram, Frayer, CER). No fixed-track labels appear.',{s:21})),
  H('My Support Plan (optional — you choose)',2),
  P(R('Supports are available by design. Check the ones you might try; you can change your mind any time.',{s:22})),
  writeTable(['Support I might use','When it would help me'],[
    ['Word Bank + Spanish column',''],
    ['Guided or Light Support Back',''],
    ['Response choice (say/record or diagram)',''],
    ['Sentence frames / Rehearsal Lab',''],
  ],[3400,6248],{rowH:640}),
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
  ],[2600,7048]),
  H('Before You Begin — Set Your Goal',2),
  P(R('This unit asks one big question: as the United States industrialized, who benefited and who bore the costs? Set a goal, then note what you already know.',{s:22})),
  writeTable(['Prompt','Your response'],[
    ['My goal for this unit is…',''],
    ['One thing I already know about this era…',''],
    ['One question I want answered…',''],
  ],[3000,6648],{rowH:760}),
  PB()];

// ================= PER-STANDARD =================
function block(code){
  const s=C.standards[code], a=s.auth, r=s.ref, out=[];
  const L=code.replace('.','')+'-L0'+code.slice(-1);
  out.push(H(`Standard ${code} — ${s.title}`,1,{brk:true}));
  out.push(P([R(`TN Academic Standard ${code}: `,{s:22,b:true}),R(s.tn.replace(/^US\.\d+\s*[–-]\s*/,''),{s:22})],{spacing:{after:60}}));
  out.push(callout('LEARNING TARGETS — I can…',(s.targets||[s.target||s.ican.replace(/^I can /,'')]).map(t=>R('•  I can '+t+'.',{s:21}))));
  if(s.lenses) out.push(P([R('Lenses for this standard: ',{s:19,b:true,c:NAVY}),R(s.lenses,{s:19,c:GREY})],{spacing:{after:80}}));
  out.push(coreCallout('CORE PATH — the same for every student',[
    'Same rigor for everyone: analyze the sources and vocabulary, then show what you learned on the Practice Quiz and the CER.',
    'UDL and MTSS give you flexible ways in — they never lower the bar.',
    'Check yourself against the learning targets on the Cornell Notes page.']));
  if(s.tn_connection) out.push(callout('★ Tennessee Connection',[s.tn_connection]));
  out.push(callout('SET YOUR GOAL (self-direction)',['My goal for this standard — what will I be able to do, and how will I show it?']));
  out.push(...ruled(2));
  // Text HOOK — a provocative, standard-specific question (images live in the analysis activities, framed + cited).
  out.push(callout('HOOK — think before you dig in',[s.hook||'What is the big question behind this standard?']));
  out.push(...ruled(2));
  out.push(callout('ACTIVATE — what do you already know or wonder?',['Jot what you already know or want to find out about this standard. You’ll come back to it.']));
  out.push(...ruled(3));
  // PREVIEW & PREDICT fills the rest of the launch page (front/back print — no
  // dead space). Fewer ruled lines when a TN-connection callout is also present
  // so the page stays full without bleeding.
  out.push(callout('PREVIEW & PREDICT',['Which learning target will be hardest, and why? Connect it to the unit’s big question: how did the war change America at home and abroad, and who sacrificed even while excluded?']));
  
  // Activity 1 — Word Bank
  out.push(H(`Activity 1 — Vocabulary (Part A: Reference / Word Bank) — ${code}`,2,{brk:true,mins:10,deck:deckRef(code,1,'Key Vocabulary')}));
  out.push(P(R('Use this word bank throughout the standard. The Spanish column supports access, not translation of assessment.',{s:21}),{spacing:{after:60}}));
  out.push(dataTable(['Term','Student-friendly meaning','Spanish'],s.vocab.map(v=>[
    new TextRun({text:v.term,bold:true,size:18,font:FONT,color:INK}),
    new TextRun({text:v.def,size:18,font:FONT,color:INK}),
    new TextRun({text:v.es,size:18,font:FONT,color:INK})]),[2683,4282,2683]));
  {const _pron=s.vocab.filter(v=>v.say);
   out.push(callout('LANGUAGE SUPPORT',[_pron.length
     ? 'Pronunciations: '+_pron.map(v=>`${v.term} (${v.say})`).join('; ')+'.'
     : 'Use the Spanish column in the Word Bank above to access these terms — cognates and translations support understanding, not translation of assessment.']));}
  {const _wl=s.vocab.reduce((a,v)=>a+Math.max(1,Math.ceil((v.def||'').length/52)),0);
   out.push(...vocabSelfCheck(code,Math.max(0,Math.min(4,23-_wl))));}
  if(SUPPORTS) out.push(...supportsBack(1,code,s,a));
  // Activity 2 — Frayer
  out.push(H(`Activity 2 — Vocabulary Studio (Frayer-inspired) — ${code}`,2,{brk:true,mins:7,deck:deckRef(code,2,'Key Vocabulary')}));
  out.push(callout('RESPONSE CHOICE',['Complete each studio by writing, speaking, or diagramming.']));
  a.frayer.forEach((term,fi)=>{const v=s.vocab.find(x=>x.term===term)||s.vocab[0];
    out.push(gap(fi===0?40:200));
    out.push(priorityBar(fi+1,term,v.es));
    out.push(P(R('Word-bank meaning to build on: '+v.def,{s:20})));
    out.push(writeTable(['Definition (in your own words)','Characteristics'],[['',''],['Examples','Non-examples'],['','']],[4824,4824],{rowH:760}));
    out.push(callout('Use it to explain',['Write one sentence that uses “'+term+'” to explain this standard.']));
    out.push(...ruled(2));});
  out.push(gap(140));
  out.push(callout('CONNECT THE TERMS (UDL · build understanding)',['How do these priority terms fit together? Write or sketch how one leads to or affects another.']));
  out.push(...ruled(2));
  if(SUPPORTS) out.push(...supportsBack(2,code,s,a));
  // Activity 3 — Cornell Notes — FRONT (note-taking; the whole page is writing space)
  out.push(H(`Activity 3 — Direct Teaching Cornell Notes — ${code}`,2,{brk:true,mins:20,deck:deckRef(code,3,'Direct Instruction')}));
  out.push(P(R('Name: ______________________    Class / Period: __________    Date: __________',{s:21})));
  out.push(P(R(`${code} — ${s.title}  •  These notes capture the direct-teaching content and the Close Read for this standard.`,{s:20,c:GREY})));
  out.push(P(R('Your learning targets are on this standard’s opening page — take notes that help you meet them.',{s:19,i:true,c:GREY}),{spacing:{after:60}}));
  out.push(writeTable(['Cues (tied to your learning targets)','My notes'],
    (s.cues||['Who benefited?','Who bore the costs?','Who decided?','Key terms →']).map(q=>[q,'']),[3050,6598],{lines:5}));
  out.push(...doodle('DOODLE ZONE — draw your thinking (UDL · another way in)','Need another way in? Sketch the key idea, a quick timeline, or how the pieces connect. Words optional.',1400));
  // Cornell Notes — BACK (keep going, then process & check)
  out.push(H(`Cornell Notes — keep going, then process & check — ${code}`,2,{brk:true}));
  out.push(callout('MORE NOTES / DIAGRAMS',['Continue your notes here, add a quick sketch, or map how the ideas connect.']));
  out.push(...ruled(8));
  out.push(callout('Key terms to list',[s.vocab.map(v=>v.term).join(' · ')]));
  out.push(writeBox('Summary — In your own words (2–3 sentences)',3));
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
  // Guided + Light Support Cornell backs. Default OFF in the student workbook —
  // they live in the Teacher Graphic Organizer Toolkit as reproducibles (truer
  // to MTSS: copy as needed). Set STUDENT_SUPPORTS=1 to keep them in the book.
  if(STUDENT_SUPPORTS){
  // Guided Support Back
  out.push(H(`Guided Support for the Cornell Notes — ${code}`,3,{brk:true}));
  out.push(P(R('These scaffolds support ONLY the Cornell notes — use them to take and process those notes. Optional and easy to set aside; not a separate assignment or a label.',{s:20,i:true})));
  out.push(dataTable(['Key vocabulary','What it means'],s.vocab.map(v=>[
    new TextRun({text:v.term,bold:true,size:20,font:FONT,color:INK}),v.def]),[3200,6448]));
  out.push(P(R('Break it into steps:',{s:21,b:true})));
  out.push(P(R('1) Name one cause or effect.    2) Give one piece of evidence.    3) Write one sentence explaining the link.',{s:20})));
  out.push(callout('Sentence frame',['One key cause/effect of '+s.title.split(':')[0].toLowerCase()+' was ______, shown by ______, which mattered because ______.']));
  out.push(callout('Modeled example (one worked note — yours will differ)',['A key idea of '+s.title.split(':')[0].toLowerCase()+' was '+s.vocab[0].term+': '+s.vocab[0].def]));
  out.push(callout('GUIDED NOTE REHEARSAL LAB',['Rehearse the cause→effect chain below, then transfer it to your Cornell notes.']));
  out.push(writeTable(['Step','Rehearse it here'],[['Name it',''],['Evidence',''],['Explain',''],['Headline','']],[2600,7048],{rowH:760}));
  out.push(writeBox('TRANSFER CHECK — move one rehearsed idea onto the front notes',3));
  // Light Support Back
  out.push(H(`Light Support for the Cornell Notes — ${code}`,3,{brk:true}));
  out.push(P(R('A lighter scaffold for the SAME Cornell notes. Try the notes first; reach for this only if you need it.',{s:20,i:true})));
  out.push(writeTable(['Key vocabulary','Finish the idea — “This term means …”'],
    s.vocab.map(v=>[v.term,'']),[3200,6448],{lines:2}));
  out.push(P(R('Guiding questions — answer on the lines below (or in your front notes):',{s:21,b:true})));
  a.tdq.forEach(q=>out.push(P(R('• '+q,{s:20}))));
  out.push(...ruled(6));
  out.push(gap(80));
  out.push(callout('WHICH CUE STILL NEEDS WORK?',['Circle the Cornell cue from the front page you still need help with, and tell your teacher so we can go over it.']));
  out.push(callout('LIGHT PROCESSING LAB',['Answer one guiding question from above in a full sentence, in your own words.']));
  out.push(...ruled(8));
  } // end STUDENT_SUPPORTS
  if(SUPPORTS) out.push(...supportsBack(3,code,s,a));
  // Activity 4 — Close Read
  out.push(H(`Activity 4 — Close Read — ${code}`,2,{brk:true,mins:18,deck:deckRef(code,4,'Direct Instruction')}));
  out.push(P(R('Reading type: History Hack-authored instructional synthesis. This is not a primary source. Builds SSP.03 (synthesize) and SSP.05 (historical awareness).',{s:20,i:true,c:GREY})));
  // Passage in titled CHUNKS (single column). The text-dependent questions are
  // MERGED into the Evidence Lab — each question is a row you find evidence for —
  // so the whole Close Read fits ONE page (no front-to-back split, no flipping),
  // and the activity is more coherent. Font + language support adapt to length.
  const _secs=(a.close_sections&&a.close_sections.length)?a.close_sections:[['',a.close]];
  const _cl=(a.close||'').length;
  const _long=_cl>1350;
  const _pf=24; // ACCESSIBILITY FLOOR: primary reading passage = 12pt, never shrunk (flow to more pages; skill: history-hack-workbook-print-bundle §type-floor)
  const _rows=_cl>1900?2:3;
  const _wl=_cl>1900?1:2;
  const _chunks=[];
  _secs.forEach(([h,c])=>{ if(h) _chunks.push(R(h,{s:_pf,b:true,c:NAVY})); _chunks.push(R(c,{s:_pf})); });
  // KEY TERMS FIRST — pre-teach the terms BEFORE the reading (print-bundle standard).
  out.push(callout('KEY TERMS FIRST',['Know these before you read: '+s.vocab.slice(0,2).map(v=>v.term).join(', ')+'. Read once for the gist, then again for evidence.']));
  out.push(callout('CORE PATH — read one chunk at a time',_chunks));
  out.push(P([R('CLOSE-READ EVIDENCE LAB — ',{s:21,b:true,c:NAVY}),R('for each question: quote the EVIDENCE from the passage above, then write YOUR ANSWER on the lines.',{s:20})],{spacing:{before:100,after:20}}));
  const _tdq=a.tdq.slice(0,_rows);
  // Generous ruled answer space (all writing on lines — closes the white-space gap).
  out.push(writeTable(['Text-dependent question','Evidence from the passage','Your answer (what it shows)'],_tdq.map(q=>[q,'','']),[3248,2900,3500],{lines:Math.max(_wl+1,3),noSplit:true}));
  out.push(P(R('',{s:12}),{spacing:{after:180}})); // breathing room after the Close Read before the next section
  // NO-BLEED RULE: the Close Read (passage + TDQs + Evidence Lab) fills its own
  // page. Do NOT append a trailing retrieval/connect box here — it overflows a
  // few lines onto a near-empty next page. Geographic work and spaced retrieval
  // each get their own full page below instead.
  if(SUPPORTS) out.push(...supportsBack(4,code,s,a));
  const gmap=(IMG[code]||{}).map;
  // Geographer's Lens — its own page (map image where one exists, else a
  // grounded map-sketch task). Fills a full page AND adds the geographic lens.
  if(s.geo && !gmap){
    out.push(H(`Geographer’s Lens — ${code}`,2,{brk:true,mins:12}));
    out.push(geoPriorityBar());
    out.push(P(R('Geographers don’t just find places — they explain how WHERE shapes WHAT happens. Work these like a geographer. Built on the Five Themes of Geography · C3 Dimension 2 · SSP.06 (spatial reasoning).',{s:20,i:true,c:GREY})));
    const places=s.geo_places||[];
    if(places.length){
      // ONE table, double duty: reference (given) + analysis (student). Covers
      // the Location / Place / Human-Environment themes with NO redundancy and
      // NO blank from-scratch map box.
      out.push(callout('THE PLACES — then explain why geography put them there',[s.geo]));
      out.push(writeTable(['Place','Where','What happened (given)','Why HERE? (your analysis)'],
        places.map(p=>[p[0],p[1],p[2],'']),[1900,1350,3100,3298],{lines:1}));
    }
    out.push(callout('MOVEMENT & REGION — what’s the spatial pattern?',['In 1–2 sentences: is this a movement, a cluster, or a whole region? Name the direction or shape it takes on a map.']));
    out.push(...ruled(2));
    out.push(callout('GEOGRAPHY AS A FORCE — how did location shape the outcome?',['How did geography change WHAT happened — who was affected, how far or fast it spread, or who was left out? Use one place above as your evidence.']));
    out.push(...ruled(3));
    out.push(callout('READ IT LIKE A SOURCE — RESPONSE CHOICE',['A map is a source with a point of view. Show your thinking your way — write it, OR sketch a quick arrows-and-labels diagram: what would a map of this make CLEAR, and what would it HIDE or leave out?']));
    out.push(...ruled(3));
  }
  // Geographer's Lens map page — standards with a verified period map
  if(gmap){
    out.push(H(`Geographer’s Lens — ${code}`,2,{brk:true,mins:10}));
    out.push(geoPriorityBar());
    out.push(P(R('Analyze this period map as a primary source. Geographer’s lens (G) · builds SSP.06.',{s:20,i:true,c:GREY})));
    out.push(...sourceImage(gmap,{max:540}));
    if(s.geo) out.push(callout('MAP TASK',[s.geo]));
    out.push(writeTable(['Map question','Your answer'],[
      ['What does the map show, and where?',''],
      ['What pattern or movement do you see?',''],
      ['How does the geography connect to this standard?',''],
      ['What does this map leave out or make hard to see?',''],
    ],[3800,5848],{lines:2}));
    out.push(...doodle('MARK UP THE MAP (draw your thinking)','On the map above, circle or label what you notice — routes, regions, clusters — then sketch the pattern here in your own quick map.',1150));
  }
  // Activity 5 — Primary Source / Data (HIPPO)
  out.push(H(`Activity 5 — Primary Source / Data Analysis — ${code}`,2,{brk:true,mins:18,deck:deckRef(code,5,'Primary Source')}));
  const im=(IMG[code]||{});
  if(im.anchor){
    out.push(P(R(`Primary source (${im.anchor.medium}) — analyze it with HIPPO. Builds SSP.01–SSP.02.`,{s:20,i:true,c:GREY})));
    out.push(...sourceImage(im.anchor,{max:470,maxH:330}));
  } else {
    const src=s.sources[0];
    out.push(P(R('Document (text primary source — analyze with HIPPO). Builds SSP.01–SSP.02.',{s:20,i:true,c:GREY})));
    out.push(callout(src.title.toUpperCase(),['“'+src.quote+'”']));
    out.push(P(R(`Source: ${src.who}, ${src.date}. ${src.repo}. Public domain. ${src.url}`,{s:18,c:GREY})));
  }
  out.push(writeTable(['HIPPO — analyze the source (prompt)','Your analysis'],[
    ['H — Historical context: what was happening when this was created?',''],
    ['I — Intended audience: who was meant to see or obey it?',''],
    ['P — Purpose: why was it created?',''],
    ['P — Point of view: whose perspective does it reflect?',''],
    ['O — Outside connection: how does it connect to this standard?',''],
  ],[4200,5448],{lines:2}));
  out.push(callout('SUPPORT OPTION',['Sentence frame: This source shows ______ because it ______, which reveals ______.']));
  if(im.anchor) out.push(callout('CONFIDENCE CHECK-IN',['Rate your understanding of this standard (1–4): ______    One thing to revisit: ____________________']));
  else out.push(...sourceExtension(code));
  if(SUPPORTS) out.push(...supportsBack(5,code,s,a));
  // Activity 6 — Practice Quiz
  out.push(H(`Activity 6 — Core Application: Practice Quiz — ${code}`,2,{brk:true,mins:8,deck:deckRef(code,6,'Progress Check')}));
  out.push(callout('SELF-GRADING — answer first, then check yourself',['Commit to each answer (mark it, say it, or explain it aloud) BEFORE you look. The answer key is at the bottom of this page — grade yourself, then reread the Cornell notes for anything you missed.']));
  // One more item than before: add a distinct, bank-sourced formative item (not
  // the exit ticket, which is rendered separately). All items carry their key so
  // the bottom-of-page answer key can be printed (self-grading).
  const _qids=new Set(a.quiz.map(q=>q.id));
  const items=[...a.quiz, {id:`u6-${code.toLowerCase().replace('.','')}-dok${s.cfu.dok}-tc`,dok:s.cfu.dok,stem:s.cfu.stem,opts:s.cfu.options,key:s.cfu.key}];
  const _extra=((ASSESS.formative||{})[code]||[]).find(f=>f&&f.stem&&!_qids.has(f.id));
  if(_extra) items.push({id:_extra.id,dok:_extra.dok||2,stem:_extra.stem,opts:Object.fromEntries((_extra.choices||[]).map(c=>[c.id,c.text])),key:_extra.key});
  const _ans=[];
  items.forEach((q,qi)=>{
    out.push(P(R(`${qi+1}.  [DOK ${q.dok} · ${q.id} · pre-field-test]`,{s:18,b:true,c:GREY})));
    out.push(P(R(q.stem,{s:21,b:true})));
    ['A','B','C','D'].forEach(x=>{ if(q.opts&&q.opts[x]!==undefined) out.push(P(R(`${x}. ${q.opts[x]}`,{s:20}),{indent:{left:260},spacing:{after:20}})); });
    if(q.key) _ans.push(`${qi+1}-${q.key}`);
  });
  // Self-grading answer key at the BOTTOM of the activity (print-bundle standard).
  out.push(P(R('— — — — —  cover this until you have answered every question  — — — — —',{s:18,c:GREY}),{align:AlignmentType.CENTER,spacing:{before:140,after:20}}));
  out.push(callout('ANSWER KEY — grade yourself',['Answers: '+_ans.join('    ')+'.']));
  if(SUPPORTS) out.push(...supportsBack(6,code,s,a));
  // Activity 7 — CER
  out.push(H(`Activity 7 — Constructed Response (CER) — ${code}`,2,{brk:true,mins:18,deck:deckRef(code,7,'Constructed Response')}));
  // Compact big-question organizer (single combined callout — keeps the CER +
  // Exit Ticket on ONE page per the no-bleed rule; the exit ticket must never
  // spill to a near-empty next page).
  out.push(callout('BIG-QUESTION ORGANIZER — in World War II, how did the war reshape America at home and its role in the world — and who sacrificed, even while being excluded?',['Jot quick notes from THIS standard: Who benefited? · Who bore the costs? · Who decided?']));
  out.push(...ruled(2));
  out.push(callout('CONSTRUCTED RESPONSE (CER) — builds SSP.04 Argumentation',[a.cer]));
  out.push(new Table({width:{size:CW,type:WidthType.DXA},columnWidths:[2200,7448],rows:[
    new TableRow({tableHeader:true,children:[cell(P(R('Part',{s:18,b:true,c:WHITE}),{spacing:{after:0}}),{w:2200,fill:NAVY}),cell(P(R('Write here',{s:18,b:true,c:WHITE}),{spacing:{after:0}}),{w:7448,fill:NAVY})]}),
    ...[['Claim',2],['Evidence (two specifics)',4],['Reasoning',3]].map(([lab,n])=>new TableRow({children:[cell(P(R(lab,{s:20,b:true}),{spacing:{after:0}}),{w:2200}),cell(ruled(n),{w:7448})]}))
  ]}));
  out.push(callout('SELF-CHECK (CER rubric — see Toolkit)',['Is my claim defensible? · TWO specific pieces of evidence? · Does my reasoning explain HOW the evidence proves the claim?']));
  // Exit Ticket — end-of-standard formative (vetted item from the question bank; key + next steps teacher-side)
  const xt=EXIT[code];
  if(xt) out.push(table([new TableRow({children:[cell([
    P([R('EXIT TICKET — before you leave  ',{s:21,b:true,c:NAVY}),R(`[item ${xt.id} · DOK ${xt.dok} · pre-field-test]`,{s:18,c:GREY})],{spacing:{after:60}}),
    P(R(xt.stem,{s:22,b:true}),{spacing:{after:50}}),
    ...xt.choices.map(c=>P(R(`${c.id}.   ${c.text}`,{s:21}),{indent:{left:360},spacing:{after:24}})),
    P([R('Show what you know (your choice): ',{s:20,b:true,c:NAVY}),R('mark the best answer, say it, or explain it — then rate how sure you are:  ☐ Not yet   ☐ Getting there   ☐ Got it',{s:20})],{spacing:{before:40,after:0}}),
    P(R('Answer key and next steps are in the Teacher Guide.',{s:18,i:true,c:GREY}),{spacing:{before:20,after:0}})
  ],{w:CW,fill:CREAM})]})],[CW]));
  if(SUPPORTS) out.push(...supportsBack(7,code,s,a));
  return out;
}
const standards=[]; ORDER.forEach(c=>block(c).forEach(x=>standards.push(x)));

// ================= BACK MATTER =================
const back=[
  H('Your Tennessee Connection',1),
  callout('TENNESSEE CONNECTION · OAK RIDGE, THE “SECRET CITY”',['Tennessee was central to winning — and ending — World War II. In 1942 the federal government built Oak Ridge in the hills of East Tennessee as a secret site of the Manhattan Project (US.56). Its plants enriched the uranium used in the bomb dropped on Hiroshima. The town grew to about 75,000 people almost overnight, yet most workers — including thousands of women (US.52) — had no idea what they were building. Tennessee also sent its people to the war: Fort Campbell trained the 101st Airborne (US.51), Alcoa produced aluminum for warplanes (US.55), and Cordell Hull of Pickett County, Secretary of State, helped found the United Nations and won the Nobel Peace Prize (US.58).']),
  P(R('Reflect (RESPONSE CHOICE): How does a local story change the way you understand a national event? Answer by writing, recording, or diagramming.',{s:21})),
  H('Local History Investigation',2),
  P(R('Industrialization touched Tennessee too — railroads, mines, mills, and the people who worked them. Investigate one local connection and record what you find.',{s:22})),
  writeTable(['Prompt','Your findings'],[
    ['A person, place, or industry from this era near me',''],
    ['One source I could check (library, TSLA, family, museum)',''],
    ['Who benefited / who bore the costs, locally',''],
    ['One question I still have',''],
  ],[3400,6248],{rowH:760}),
  H('Progress Tracker & Cumulative Review',1),
  P(R('Track your Progress Check result for each standard and note one thing to revisit.',{s:22})),
  writeTable(['Standard','Progress Check (✓ / reteach)','One thing to revisit'],
    C.order.map(c=>[c,'','']),[1600,4024,4024],{rowH:620}),
  H('Optional Extension Bank (higher-DOK, open to all)',1),
  P(R('Any student may choose an extension. These are EXTENSION, not a track.',{s:22})),
  ...C.order.map(c=>P([R(`${c}: `,{s:21,b:true,c:NAVY}),R(C.standards[c].auth.cer.replace('Claim + Evidence + Reasoning: ',''),{s:21})])),
  H('Think Like a Test-Writer (unit review — open to all)',1),
  P(R('You met a quick “think like a test-writer” prompt in every standard. Here is the full how-to, once, plus room to write your best questions for the whole unit.',{s:22})),
  callout('HOW TO WRITE A DOK-3 QUESTION',[
    'DOK-3 = strategic thinking: the reader must analyze, compare, evaluate, or justify using evidence — and there should be more than one defensible answer (not a fact you can just look up).',
    'Sentence starters: “Why did ______ lead to ______?”  ·  “Which mattered more — ______ or ______ — and why?”  ·  “What is the BEST evidence that ______?”  ·  “Evaluate whether ______.”  ·  “Defend or challenge: ______.”',
    'Frame:  [Analyze / Evaluate / Justify]  +  [something from this unit]  +  “using evidence.”',
    'Quick check: does my question make the reader THINK and use evidence? If yes, it’s DOK-3.']),
  writeTable(['Standard','Your DOK-3 question','Your answer key (one sentence)'],
    [['',''],['',''],['',''],['','']].map((_,i)=>['','','']),[1500,4574,3574],{rowH:820}),
  H('Reusable Toolkit & Source Library',1),
  H('Written Response Rubric (CER)',2),
  dataTable(['Level','Claim','Evidence','Reasoning'],[
    ['4 — Strong','Precise, defensible','2+ accurate, specific','Explains how evidence proves the claim'],
    ['3 — Proficient','Clear','2 accurate','Explains the link'],
    ['2 — Developing','General','1 accurate','Partial link'],
    ['1 — Beginning','Unclear/missing','Missing/inaccurate','No reasoning'],
  ],[1800,2616,2616,2616]),
  H('Source Library — full citations & clickable links',2),
  ...C.order.flatMap(c=>[P(R(`${c} — ${C.standards[c].title}`,{s:21,b:true,c:NAVY})),
    ...C.standards[c].sources.map(x=>P([R(`${x.title}. `,{s:19,b:true}),R(`${x.who}, ${x.date}. ${x.repo}. Public domain. `,{s:19}),R(x.url,{s:18,c:'2A5DB0'})]))]),
  H('The Good War? — Who Fought, Who Sacrificed, Who Was Excluded',1),
  P(R('This section complicates the “Good War” narrative: the U.S. fought fascism abroad while denying rights to many of its own people at home. It is History Hack-authored instructional synthesis grounded in this unit’s sourced record — not a primary source.',{s:22})),
  ...[['Serving While Excluded','Black Americans fought under segregation and demanded a “Double V” — victory over fascism abroad and racism at home (US.53); the Tuskegee Airmen, Navajo Code Talkers, and the Japanese-American 442nd (US.51) served with distinction even as their communities faced discrimination.'],
    ['A Freedom Denied at Home','While fighting for freedom, the U.S. forced about 120,000 Japanese Americans — most of them citizens — into internment camps under Executive Order 9066; the Supreme Court upheld it in Korematsu (US.54).'],
    ['The Home Front & Women','Rationing, war bonds, and war production remade daily life (US.55); millions of women entered defense work — “Rosie the Riveter” (US.52) — including at Oak Ridge, though many lost those jobs when the war ended.'],
    ['A New World Order — and the Bomb','The Manhattan Project ended the war with atomic weapons (US.56); Yalta and Potsdam (US.57) divided the postwar world; and the United Nations (US.58) was founded to prevent the next global war — even as the Holocaust (US.47) revealed how far totalitarianism had gone.']
  ].flatMap(([h,b])=>[H(h,2),P(R(b,{s:21}))]),
  P(R('Residual note (known follow-up): sourced visuals and named Key-Figure entries for these histories remain pending.',{s:18,i:true,c:GREY})),
  H('Unit Reflection',2),
  P(R('Return to the unit’s big question: how did World War II reshape America at home and its role in the world — and who sacrificed for a freedom they were still denied? Write a final claim with two pieces of evidence from different standards.',{s:22})),
  writeTable(['Part','Write here'],[['My claim',''],['Evidence 1 (standard: ___)',''],['Evidence 2 (standard: ___)',''],['Why it matters today','']],[2600,7048],{rowH:820})];

// ================= ASSEMBLE =================
const header=new Header({children:[P(R('U.S. History Hack™ · Unit 6 · Course Standard Edition',{s:18,b:true,c:GOLD}),{align:AlignmentType.RIGHT,spacing:{after:0}})]});
const footer=new Footer({children:[new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:0},children:[
  R('U.S. History Hack™ · Unit 6 (Course Standard)   © 2026 TroopToTeacher Technologies LLC   |   Page ',{s:18,c:GREY}),
  new TextRun({children:[PageNumber.CURRENT],size:15,color:GREY,bold:true,font:FONT})]})]});
const doc=new Document({creator:'TroopToTeacher Technologies LLC',title:'U.S. History Hack — Unit 6 Course Standard Student Workbook (Pilot)',
  features:{updateFields:true},
  styles:{default:{document:{run:{font:FONT,size:22,color:INK}}},paragraphStyles:[
    {id:'Heading1',name:'Heading 1',basedOn:'Normal',next:'Normal',quickFormat:true,run:{font:FONT,size:36,bold:true,color:NAVY},paragraph:{spacing:{before:220,after:90},outlineLevel:0,keepNext:true}},
    {id:'Heading2',name:'Heading 2',basedOn:'Normal',next:'Normal',quickFormat:true,run:{font:FONT,size:28,bold:true,color:NAVY},paragraph:{spacing:{before:150,after:80},outlineLevel:1,keepNext:true}},
    {id:'Heading3',name:'Heading 3',basedOn:'Normal',next:'Normal',quickFormat:true,run:{font:FONT,size:24,bold:true,color:RED},paragraph:{spacing:{before:120,after:70},outlineLevel:2,keepNext:true}},
  ]},
  sections:[{properties:{page:{size:{width:12240,height:15840},margin:{top:1152,bottom:1152,left:1296,right:1296,header:720,footer:720}}},
    headers:{default:header},footers:{default:footer},children: SAMPLE ? [P(R(`SAMPLE — Unit 6 · first ${SAMPLE} standards (activities only, ruled-line writing) — for review`,{s:24,b:true,c:NAVY}),{align:AlignmentType.CENTER,spacing:{after:120}}), ...standards] : [...cover,...front,...standards,...back]}]});
const OUTFILE=SAMPLE?`deliverables/Unit6_SAMPLE_${SAMPLE}standards.docx`:'deliverables/Unit6_Student_Workbook_CourseStandard.docx';
Packer.toBuffer(doc).then(b=>{fs.writeFileSync(OUTFILE,b);console.log('WROTE',OUTFILE,b.length,'bytes');});
