// Unit 1 Teacher How-to-Use & MTSS Guide — docx-js, EXACT Unit 5 template tokens/structure.
const fs=require('fs'); const D=require('docx');
const {Document,Packer,Paragraph,TextRun,HeadingLevel,AlignmentType,Table,TableRow,TableCell,
  WidthType,BorderStyle,ShadingType,PageBreak,Header,Footer,PageNumber,HeightRule,ImageRun,TableLayoutType}=D;
// Invisible fixed-width spacer: iOS/Apple/Google previewers ignore <w:tblLayout type="fixed"> and
// autofit columns to their widest glyph content, collapsing blank cells. A fixed-width transparent
// PNG is measured by every renderer, holding each column at its intended width on all viewers.
const SPACER_PNG=Buffer.from('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR4nGP4//8/AwAI/AL+p5qgoAAAAABJRU5ErkJggg==','base64');
function widthAnchor(w){return new ImageRun({type:'png',data:SPACER_PNG,transformation:{width:Math.max(8,Math.round((w-300)/15)),height:1},altText:{title:'',description:'spacer',name:'spacer'}});}
const C=JSON.parse(fs.readFileSync('analysis/unit1_content.json','utf8'));
const EXIT=fs.existsSync('analysis/unit1_exit_tickets.json')?JSON.parse(fs.readFileSync('analysis/unit1_exit_tickets.json','utf8')):{};
const DIMNAME={C:'Culture',E:'Economics',G:'Geography',H:'History',P:'Politics/Government',T:'Tennessee',TCA:'TN Code Annotated'};
const NAVY='1B2A4A',RED='B22234',GOLD='C89B3C',INK='1A1A1A',CREAM='F7F5EF',WHITE='FFFFFF',GREY='6B7280',BORD='D9D5C8';
const FONT='Calibri',CW=9792;
const bd=(c=BORD,sz=4)=>({style:BorderStyle.SINGLE,size:sz,color:c});const CELLB=(c=BORD)=>({top:bd(c),bottom:bd(c),left:bd(c),right:bd(c)});
function Rr(t,{s=22,b=false,i=false,c=INK}={}){return new TextRun({text:t,size:s,bold:b,italics:i,color:c,font:FONT});}
function P(runs,{align,spacing}={}){return new Paragraph({alignment:align,spacing:spacing||{after:100},children:Array.isArray(runs)?runs:[runs]});}
function H(t,l){const m={1:HeadingLevel.HEADING_1,2:HeadingLevel.HEADING_2,3:HeadingLevel.HEADING_3};
  return new Paragraph({heading:m[l],spacing:{before:l===1?220:150,after:90},keepNext:true,children:[Rr(t,{s:l===1?36:l===2?28:24,b:true,c:l===3?RED:NAVY})]});}
function cell(ch,{w,fill}={}){return new TableCell({width:{size:w,type:WidthType.DXA},shading:fill?{type:ShadingType.CLEAR,fill,color:'auto'}:undefined,margins:{top:60,bottom:60,left:110,right:110},borders:CELLB(),children:Array.isArray(ch)?ch:[ch]});}
function table(rows,w){return new Table({width:{size:CW,type:WidthType.DXA},columnWidths:w,layout:TableLayoutType.FIXED,rows});}
function dataTable(hd,rows,w){const hr=new TableRow({tableHeader:true,children:hd.map((h,i)=>cell(P(Rr(h,{s:19,b:true,c:WHITE}),{spacing:{after:0}}),{w:w[i],fill:NAVY}))});
  const br=rows.map(r=>new TableRow({children:r.map((cx,i)=>cell(P(typeof cx==='string'?Rr(cx,{s:20}):cx,{spacing:{after:0}}),{w:w[i]}))}));return table([hr,...br],w);}
function callout(label,lines){const k=[P(Rr(label,{s:21,b:true,c:NAVY}),{spacing:{after:60}})];(lines||[]).forEach(l=>k.push(P(Rr(l,{s:22}),{spacing:{after:40}})));
  return table([new TableRow({children:[cell(k,{w:CW,fill:CREAM})]})],[CW]);}
const PB=()=>new Paragraph({children:[new PageBreak()]});
function writeTable(headers,rows,w,{rowH=560}={}){const trs=[];
  if(headers)trs.push(new TableRow({tableHeader:true,children:headers.map((h,i)=>cell(P(Rr(h,{s:18,b:true,c:i===0?NAVY:WHITE}),{spacing:{after:0}}),{w:w[i],fill:i===0?CREAM:NAVY}))}));
  rows.forEach(r=>trs.push(new TableRow({height:{value:rowH,rule:HeightRule.ATLEAST},children:r.map((cx,i)=>cell(P(cx?Rr(cx,{s:20,b:i===0}):[widthAnchor(w[i]),Rr('',{s:20})],{spacing:{after:0}}),{w:w[i]}))})));
  return table(trs,w);}
function writeBox(label,lines=2,h=520){const rows=[new TableRow({children:[cell(P(Rr(label,{s:21,b:true,c:NAVY}),{spacing:{after:0}}),{w:CW,fill:CREAM})]})];
  for(let i=0;i<lines;i++)rows.push(new TableRow({height:{value:h,rule:HeightRule.ATLEAST},children:[cell(P([widthAnchor(CW),Rr('',{s:20})],{spacing:{after:0}}),{w:CW})]}));
  return table(rows,[CW]);}
function priorityBar(txt){return table([new TableRow({children:[cell(P([Rr('PRIORITY TERM',{s:16,b:true,c:GOLD}),Rr('     '+txt,{s:24,b:true,c:WHITE})],{spacing:{after:0}}),{w:CW,fill:NAVY})]})],[CW]);}
function blankCornell(){return [
  H('Blank Cornell Notes — Universal Front (printable)',2),
  P(Rr('Name: ______________________    Class / Period: __________    Date: __________    Topic: ______________________',{s:21})),
  callout('LEARNING TARGET',['I can __________________________________________________________________________________']),
  writeTable(['Guiding cues (about 25%)','My notes (about 75%)'],[['',''],['',''],['',''],['','']],[2639,7153],{rowH:900}),
  P(Rr('The 25/75 split describes the approximate width of each writing column (label, not a fixed track).',{s:18,i:true,c:GREY})),
  writeBox('Key terms to list',1,420),
  writeBox('Summary — In your own words (2–3 sentences)',2,560),
  writeBox('My 12–15 word headline',1,460),
  P(Rr('Print duplex: the Guided or Light Support for these notes goes on the reverse of this page.',{s:18,i:true,c:GREY})),
  PB()];}
function blankVocabStudio(){return [
  H('Blank Vocabulary Studio — Frayer (printable)',2),
  callout('RESPONSE CHOICE',['Complete the studio by writing, speaking, or diagramming.']),
  priorityBar('__________________________     ES: __________________'),
  P(Rr('Word-bank meaning to build on: ______________________________________________________________',{s:20})),
  writeTable(['Definition (in your own words)','Characteristics'],[['',''],['Examples','Non-examples'],['','']],[4896,4896],{rowH:900}),
  writeBox('Use it to explain — write one sentence that uses the term',1,520),
  PB()];}
const AKEY_CFU={}; C.order.forEach(c=>AKEY_CFU[c]=C.standards[c].cfu.key);

const body=[
  H('Unit 1 — Teacher How-to-Use & MTSS Guide',1),
  P(Rr(`${C.unit.title} · Course Standard · ${C.unit.standards_range} · Grades 9–12`,{s:22,b:true,c:NAVY})),
  P(Rr('Release-Ready · Pilot Edition. This guide holds the answer key for teacher use only — keep it separate from student materials.',{s:20,i:true,c:GREY})),

  H('1. Firm Goals, Flexible Means',1),
  P(Rr('One firm learning goal per standard; flexible, universal means. Supports are available by design and never lower the goal. They work alongside — never in place of — required IEP or 504 accommodations.',{s:22})),
  H('The same six labels students see',2),
  dataTable(['Label','Meaning'],[
    ['CORE PATH','Essential instruction every student completes.'],
    ['SUPPORT OPTION','Optional scaffold that keeps the goal, not lowers it.'],
    ['LANGUAGE SUPPORT','Vocabulary, pronunciation, and Spanish cognates.'],
    ['RESPONSE CHOICE','Write, say/record, or diagram.'],
    ['PROGRESS CHECK','Quick DOK-2/3 check to guide reteach or extend.'],
    ['EXTENSION','Deeper challenge once the goal is met.'],
  ],[2639,7153]),

  H('2. Label-to-Action Table',1),
  dataTable(['When you see…','Do this'],[
    ['CORE PATH','Teach to all; this is the standard expectation.'],
    ['SUPPORT OPTION / Guided Back','Offer to any student; never assign by track.'],
    ['LANGUAGE SUPPORT','Pre-teach Word Bank terms; use Spanish column for access.'],
    ['PROGRESS CHECK','Collect a quick response; route with the Decision Cycle.'],
    ['EXTENSION','Offer the higher-DOK CER/Extension Bank to anyone ready.'],
  ],[3045,6747]),

  H('3. MTSS — Tiers of Support Intensity',1),
  dataTable(['Tier','Who / when','In this unit'],[
    ['Tier 1 (Core)','All students','Full deck + workbook CORE PATH, Word Bank, Cornell Notes.'],
    ['Tier 2 (Targeted)','Students missing a Progress Check','Guided Support Back, sentence frames, Rehearsal Lab.'],
    ['Tier 3 (Intensive)','Persistent barrier','Pair Guided Back with IEP/504 supports; reteach a step.'],
  ],[1827,3248,4717]),

  H('4. The MTSS Decision Cycle',1),
  P(Rr('PROGRESS CHECK → identify barrier → select support → reteach → recheck → extend',{s:24,b:true,c:NAVY})),
  callout('Scaffold fading',['Fade Guided → Light → independent as evidence grows; reintroduce support for a new barrier. Required IEP/504 accommodations do not fade unless the authorized team changes them.']),

  H('5. District Review Evidence Snapshot',1),
  dataTable(['Criterion','Where it shows'],[
    [`Standards alignment (${C.unit.standards_range})`,'Standards & SSP Crosswalk; per-standard blocks.'],
    ['Public-domain sources, cited','Source Library; Activity 5 each standard.'],
    ['UDL 3.0 visible','Accessibility matrix; callouts throughout.'],
    ['MTSS','This guide §3–4; wrap-up decision band in the Teacher Deck.'],
    ['Assessment integrity','Answer key here (separate); de-biased positions.'],
  ],[3451,6341]),

  H('6. Direct Teaching + Cornell Notes + Slide Deck Workflow',1),
  P(Rr('Project the Student (Lean) Deck; students take Cornell Notes on the Universal Front. The Teacher (Full) Deck carries Quick Reviews, Guided Practice, Checks for Understanding, and Answer Reveals.',{s:22})),
  H('Verified Lean Student Deck ranges (from the final 64-slide deck)',2),
  dataTable(['Standard','Lean Deck range','Direct-teaching','Vocab','Primary source','Progress Check'],
    C.order.map(c=>{const r=C.standards[c].ref;return [c,r.range,r.dt,String(r.vocab),String(r.source),String(r.progress)];}),[1421,1928,1928,1471,1522,1522]),

  H('7. What to Print and When',1),
  dataTable(['Print','When'],[
    ['Cornell Universal Front (per standard)','Day 1 of each standard.'],
    ['Guided / Light Support Backs','On request only; reverse of the front.'],
    ['Practice Quiz + CER','After direct teaching, before the standard assessment.'],
    ['Source Library','Once per unit for reference.'],
  ],[3248,6544]),

  H('8. Per-Standard Lesson Sequence & Pacing (one standard = one 45-minute period)',1),
  P(Rr('Each standard is taught in a single 45-minute period, but the workbook intentionally holds more activity than one period can fit — run them all and it is roughly 90–105 minutes. That is by design: you choose which activities fill your period, and the rest become bell-ringers, stations, homework, reteach, or extension. The estimates below are honest time-on-task for an average class; adjust for yours. Every workbook activity header shows the same ⏱ estimate so students can self-pace.',{s:22})),
  H('Honest activity time estimates (pick what fills your 45 minutes)',2),
  dataTable(['Activity','~Time','Note'],[
    ['Standard launch (hook · goal · activate · predict)','5 min','Frames the learning target and the day.'],
    ['Activity 1 — Vocabulary Word Bank','10 min','Reference + self-check + quick-write.'],
    ['Activity 2 — Vocabulary Studio (Frayer)','7 min','One priority term, four quadrants.'],
    ['Activity 3 — Cornell Notes (with slide deck)','20 min','Direct-teaching capture — front + processing back.'],
    ['Activity 4 — Close Read','15 min','Passage, annotation, text-dependent questions.'],
    ['Geographer’s Lens map (standards with a map, as applicable)','10 min','Analyze the period map + mark-up.'],
    ['Activity 5 — Primary Source / Data (HIPPO)','15 min','Source + five HIPPO prompts + response.'],
    ['Activity 6 — Practice Quiz','8 min','A few items + one short DOK-3 write.'],
    ['Activity 7 — CER + Exit Ticket','15 min','CER organizer + paragraph (~12) and Exit Ticket (~3).'],
  ],[3349,913,5530]),
  P(Rr('Run every activity and a standard totals ≈ 105 minutes (≈ 95 without a map) — about two periods of work compressed into a one-period design. So it is a menu, not a checklist.',{s:22})),
  callout('How to fill the period — your call',[
    'You decide which activities run in class. A common choice is Launch → Cornell Notes with the deck → one analysis activity (Close Read or Primary Source) → the Exit Ticket, but nothing forces that set — pick what your class needs that day.',
    'The Exit Ticket is the daily formative check; try to close every period with it (see §16 for the keys and reteach routing).',
    'Whatever you do not run in class becomes a bell-ringer, station, early-finisher task, homework, reteach, or extension. Rigor stays the same for every learner; UDL/MTSS supports layer on without lowering the bar.']),
  PB(),

  H('9. Assessment Source & Item Metadata',1),
  P(Rr('Each standard’s Progress Check / Transfer Check is a Teacher-Deck Check for Understanding (DOK 2–3). The additional Practice-Quiz DOK-1 items are '+C.unit.brand+'-authored recall items. All items are pre-field-test (classroom-formative), not a secure TCAP form. Correct-answer positions are de-biased and identical across Student Progress Check, Teacher CFU/Reveal, and the workbook Transfer Check.',{s:22})),
  callout(`De-biased key distribution (Transfer Checks, ${C.unit.standards_range})`,[C.order.map(c=>C.standards[c].cfu.key).join(' · ')]),

  H('10. Practice Quiz — Answer Key & Rationales',1),
  P(Rr('For teacher use only — keep separate from student copies.',{s:20,i:true,c:GREY})),
  ...C.order.flatMap(c=>{const s=C.standards[c],a=s.auth,q1=a.quiz[0];return [
    H(`${c} — ${s.title}`,3),
    dataTable(['Item','DOK','Key','Rationale'],[
      [`${q1.id}`,String(q1.dok),q1.key,'Recall of the standard’s core term/fact.'],
      [`u1-${c.toLowerCase().replace('.','')}-dok${s.cfu.dok}-tc`,String(s.cfu.dok),s.cfu.key,s.cfu.why],
    ],[2639,913,913,5327]),
  ];}),
  PB(),

  H('11. How CAST UDL 3.0 Is Visible in Unit 1',1),
  dataTable(['UDL principle','In this unit'],[
    ['Engagement','Response choice; Tennessee Connection relevance; optional extensions.'],
    ['Representation','Word Bank + pronunciation + Spanish; Close-Read supports; HIPPO scaffold.'],
    ['Action & Expression','Write / say / diagram; Frayer studio; CER with rubric.'],
  ],[2639,7153]),
  P(Rr('No fixed-track labels appear anywhere in the student materials; supports are universal and optional.',{s:20,i:true,c:GREY})),
  new Paragraph({children:[new PageBreak()]}),
  H('12. Printable Blank Templates',1),
  P(Rr('Reusable blank versions of the two most-printed student pages — print as many as you need for any lesson. Each is designed to fill one page; the Cornell notes are meant to print duplex with a support scaffold on the reverse.',{s:22})),
  ...blankCornell(),
  ...blankVocabStudio(),

  H('13. Social Studies Practices (SSP) Crosswalk',1),
  P(Rr('Each activity in the seven-activity cycle builds specific Tennessee Social Studies Practices. Every SSP.01–SSP.06 is covered within each standard’s cycle.',{s:22})),
  dataTable(['Activity','Builds','Practice'],[
    ['Cornell Notes (Activity 3)','SSP.05','Develop historical awareness — sequence events, recognize cause & effect.'],
    ['Close Read (Activity 4)','SSP.03 · SSP.05','Synthesize data from multiple sources; historical awareness.'],
    ['Primary Source / HIPPO (Activity 5)','SSP.01 · SSP.02','Gather, analyze, and evaluate sources; critically examine a source for point of view, bias, context.'],
    ['Geographer’s Lens (G-tagged standards)','SSP.06','Analyze relationships among geography, economics, and society across time and place.'],
    ['Practice Quiz (Activity 6)','SSP.01–06 (assessed)','Applied across items.'],
    ['CER (Activity 7)','SSP.04','Construct and communicate arguments citing supporting evidence.'],
  ],[3248,1928,4616]),
  callout('Coverage',['All six practices (SSP.01–SSP.06) are built within every standard’s cycle.']),
  PB(),

  H('14. Standard Dimension Coverage (C · E · G · H · P · T · TCA)',1),
  P(Rr('Each TN standard carries dimension tags. This crosswalk shows where each dimension is taught within the standard — evidence of full coverage for adoption review. Students see these as plain-language “lenses” on each standard’s opening page.',{s:22})),
  ...C.order.flatMap(code=>{const s=C.standards[code];return [
    H(`${code} — ${s.title}`,3),
    dataTable(['Dimension','Where it is taught in this standard'],
      (s.dim_map?Object.entries(s.dim_map).map(([k,v])=>[`${DIMNAME[k]||k} (${k})`,v])
        :(s.lenses||'').split('·').map(x=>x.trim()).filter(Boolean).map(seg=>{
          const j=seg.indexOf(':'); return j>0?[seg.slice(0,j).trim(),seg.slice(j+1).trim()]:['Lens',seg];})),
      [2842,6950]),
  ];}),
  PB(),

  H('15. Constructed Response (CER) — 6-Point Rubric',1),
  P(Rr('The course’s canonical constructed-response scale. Student materials use the simple Full / Developing / Beginning per part; teachers score with the 6-point guide below (aligns with the DBQ/CER rubric bank).',{s:22})),
  dataTable(['Score','Level','What it looks like'],[
    ['6','Exemplary','Defensible, insightful claim; TWO or more precise, accurate pieces of evidence; reasoning fully explains HOW the evidence proves the claim; cohesive and sophisticated.'],
    ['5','Advanced','Clear claim; strong, accurate evidence; reasoning explains the link with only minor gaps.'],
    ['4','Proficient','Adequate claim; some specific evidence; reasoning present but general.'],
    ['3','Adequate','Basic claim; limited or partly accurate evidence; reasoning thin.'],
    ['2','Developing','Vague claim; little evidence; evidence largely unexplained.'],
    ['1','Beginning','No clear claim; little or no evidence; no reasoning.'],
  ],[812,1725,7255]),
  P(Rr('Swap in your bank’s exact CER rubric text if it differs; the 6-point scale (6 Exemplary → 1 Beginning) is the course convention.',{s:18,i:true,c:GREY})),
  PB(),

  H('16. Exit Ticket Answer Keys + What’s Next (reteach)',1),
  P(Rr('For teacher use only — keep separate from student copies. Each standard’s Exit Ticket (end of the standard, on the CER page) with its key and reteach routing. Items are pre-field-test.',{s:20,i:true,c:GREY})),
  dataTable(['Std','Item','DOK','Key','What’s Next if a student misses it'],
    C.order.filter(c=>EXIT[c]).map(c=>{const x=EXIT[c];return [c,x.id,String(x.dok),x.correct,
      `Revisit ${C.standards[c].title} — reteach with the Cornell cues + Guided Support; re-check with the Progress Check.`];}),
    [913,1928,710,710,5531]),
];

const header=new Header({children:[P(Rr(`${C.unit.course_name} · ${C.unit.code} Teacher Guide`,{s:16,b:true,c:GOLD}),{align:AlignmentType.RIGHT,spacing:{after:0}})]});
const footer=new Footer({children:[new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:0},children:[
  Rr(`${C.unit.course_name} · ${C.unit.code} Teacher Guide   © 2026 TroopToTeacher Technologies LLC   |   Page `,{s:15,c:GREY}),
  new TextRun({children:[PageNumber.CURRENT],size:15,color:GREY,bold:true,font:FONT})]})]});
const doc=new Document({creator:'TroopToTeacher Technologies LLC',title:`${C.unit.course_name} — ${C.unit.code} Teacher How-to-Use & MTSS Guide (Pilot)`,
  styles:{default:{document:{run:{font:FONT,size:22,color:INK}}},paragraphStyles:[
    {id:'Heading1',name:'Heading 1',basedOn:'Normal',next:'Normal',run:{font:FONT,size:36,bold:true,color:NAVY},paragraph:{spacing:{before:220,after:90},outlineLevel:0,keepNext:true}},
    {id:'Heading2',name:'Heading 2',basedOn:'Normal',next:'Normal',run:{font:FONT,size:28,bold:true,color:NAVY},paragraph:{spacing:{before:150,after:80},outlineLevel:1,keepNext:true}},
    {id:'Heading3',name:'Heading 3',basedOn:'Normal',next:'Normal',run:{font:FONT,size:24,bold:true,color:RED},paragraph:{spacing:{before:120,after:70},outlineLevel:2,keepNext:true}},
  ]},
  sections:[{properties:{page:{size:{width:12240,height:15840},margin:{top:1152,bottom:1152,left:1224,right:1224,header:720,footer:720}}},
    headers:{default:header},footers:{default:footer},children:body}]});
Packer.toBuffer(doc).then(b=>{fs.writeFileSync('deliverables/Unit1_Teacher_HowToUse_and_MTSS_Guide.docx',b);console.log('WROTE teacher guide',b.length,'bytes');});
