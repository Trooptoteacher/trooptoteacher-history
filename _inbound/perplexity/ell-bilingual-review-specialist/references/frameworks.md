# ELL & Bilingual Instructional Design Frameworks — Full Reference

## 1. WIDA ELD Standards Framework (2020 Edition)

### Four Big Ideas

1. **Equity of Opportunity and Access**: Every multilingual learner deserves access to rigorous, grade-level content. Language proficiency should never be a gatekeeper to academic content. In History Hack, this means all TN U.S. History content (US.01-US.95) must be accessible regardless of English proficiency level.

2. **Integration of Content and Language**: Language development happens through meaningful content engagement, not in isolation. History Hack vocabulary, assessments, and narratives should teach language and history simultaneously — vocabulary terms should include historical context, not just dictionary definitions.

3. **Collaboration among Stakeholders**: ELL supports in edtech must bridge teachers, ELD specialists, families, and students. History Hack's teacher tools should surface ELL data (which students use Spanish mode, simplified definitions) so teachers can differentiate instruction.

4. **Functional Approach to Language Development**: Language is taught through its functions — narrating, explaining, arguing, informing. Assessment items should scaffold these functions: "Describe the causes..." scaffolds narration; "Evaluate the impact..." scaffolds argumentation.

### WIDA Proficiency Levels and History Hack Mapping

| WIDA Level | Label | History Hack Support |
|-----------|-------|---------------------|
| 1 | Entering | Full Spanish mode, simplified definitions, visual supports, ELL notes |
| 2 | Emerging | Spanish mode + English key terms highlighted, simplified definitions |
| 3 | Developing | Bilingual toggle (student chooses), simplified available, sentence stems |
| 4 | Expanding | English primary with Spanish glossary access, standard definitions |
| 5 | Bridging | English mode with academic vocabulary support |
| 6 | Reaching | Standard English mode |

### Key Language Uses (KLUs) in Social Studies

The four KLUs define how students use language in academic contexts:

1. **Narrate**: Tell stories of historical events, sequence cause and effect
2. **Inform**: Present factual information about people, places, events
3. **Explain**: Describe how or why historical events occurred
4. **Argue**: Take a position using historical evidence

Each KLU has genre-specific language demands. History Hack content should scaffold all four KLUs in both English and Spanish.

### Language Expectations for Grades 9-12 Social Studies

- Students interpret and analyze primary and secondary sources
- Students construct historical arguments using evidence
- Students compare perspectives across time periods and cultures
- Students use discipline-specific vocabulary (Tier 3 words)

## 2. CAST UDL Guidelines 3.0 (2024) — ELL Applications

### Principle 1: Engagement (The "Why" of Learning)

**For ELLs specifically:**
- 1.1 Promote expectations that optimize belonging — Validate home language and culture
- 1.2 Support coping skills, strategies, and constructive perspectives — Use growth-oriented language (not deficit framing)
- 1.3 Foster collaboration and interdependence — Enable peer support in home language
- 1.4 Empower community-building — Connect content to culturally relevant contexts

**History Hack implementation:**
- Growth-oriented language throughout ("growth opportunity" not "weak spot")
- Culturally responsive primary sources representing diverse perspectives
- Collaborative features that allow bilingual peer interaction

### Principle 2: Representation (The "What" of Learning)

**For ELLs specifically:**
- 2.1 Offer flexible ways of perceiving information — Bilingual text, audio, visual supports
- 2.2 Offer ways to customize display — Language toggle, font size, simplified text
- 2.3 Clarify language and symbols — Bilingual glossaries, cognate highlighting, simplified definitions
- 2.4 Offer alternatives for auditory and visual information — ReadAloud in both languages, captions
- 2.5 Illustrate connections and relationships — Visual organizers, timeline views, concept maps

**History Hack implementation:**
- `BilingualText` component for all translatable content
- `ReadAloudButton` for vocabulary, definitions, instructions
- `lexileLevel` toggle for simplified/standard definitions
- Unit color coding for visual organization
- Flashcard mode for vocabulary (reduces text density)

### Principle 3: Action & Expression (The "How" of Learning)

**For ELLs specifically:**
- 3.1 Optimize access to tools and assistive technologies — Keyboard nav, screen readers, language tools
- 3.2 Support planning and strategy development — Sentence stems, graphic organizers
- 3.3 Facilitate managing information and resources — Cornell Notes with bilingual support
- 3.4 Enhance capacity for monitoring progress — Progress tracking in active language

**History Hack implementation:**
- Cornell Notes tool with bilingual prompts
- Writing Lab with sentence stems in both languages
- Portfolio auto-save in active language
- Progress dashboard with bilingual labels

## 3. Mayer's Multimedia Learning Principles — ELL-Specific Applications

### Critical Principles for Bilingual Digital Content

| Principle | Standard Application | ELL-Specific Application |
|-----------|---------------------|--------------------------|
| **Coherence** | Remove extraneous material | Remove decorative text; every word must serve a purpose for ELLs who process each word more deliberately |
| **Signaling** | Highlight key info | Bold/color Tier 3 vocabulary; use unit color codes; tag standards |
| **Redundancy** | Don't duplicate narration as text | Exception for ELLs: bilingual text + audio CAN reinforce when user controls pacing |
| **Spatial Contiguity** | Text near related graphics | Spanish translations directly below/beside English, not in separate panels |
| **Temporal Contiguity** | Words and pictures together | Vocabulary images should appear alongside bilingual definitions |
| **Segmenting** | Break into learner-paced chunks | Bilingual content must be chunked more aggressively (5-7 items, not 10-15) |
| **Pre-training** | Teach key terms first | Pre-teach Tier 3 vocabulary before content lessons; vocab page serves this role |
| **Personalization** | Use "you" and "your" | Maintain conversational tone in Spanish translations (tú/usted consistency) |

### ELL-Specific Additions

- **Dual-coding for ELLs**: Pair text with images/icons more frequently than for monolingual learners
- **Cognate bridging**: When English-Spanish cognates exist, make them visible (constitution/constitución)
- **Controlled vocabulary in instructions**: UI instructions should use Tier 1 words; save Tier 3 for content

## 4. Krashen's Hypotheses Applied to EdTech

### Input Hypothesis (i+1)

Content should be slightly above the learner's current proficiency:
- **Simplified definitions** = i+1 for WIDA levels 1-3
- **Standard definitions** = i+1 for WIDA levels 4-5
- **Primary source quotes** = challenging input; needs scaffolding for all ELL levels

### Affective Filter Hypothesis

High anxiety blocks language acquisition:
- Never use deficit language about language ability
- Provide low-stakes practice modes (flashcards, games) before assessments
- Allow language choice — don't force English-only
- Growth-oriented feedback on all responses

### Monitor Hypothesis

Conscious grammar knowledge helps edit output:
- Sentence stems provide grammatical frameworks
- Writing Lab should offer both English and Spanish stems
- Constructed responses should accept code-switching (mixing languages) without penalty

## 5. Cognitive Load Theory for Multilingual Learners

### Intrinsic Load Management

Bilingual processing adds intrinsic load:
- Element interactivity is higher when processing two languages
- Reduce concurrent demands: show one language at a time by default
- `showBoth` mode (side-by-side) should be opt-in, not default

### Extraneous Load Reduction

- Clean, consistent UI layouts (History Hack design system)
- No split attention: translations inline, not in separate panels
- No redundancy overload: audio should match displayed language, not play both
- Icons and visual cues reduce text dependency

### Germane Load Optimization

- Schema building: connect new terms to known concepts via ELL support notes
- Cognate activation: highlight when English term has Spanish cognate
- Spaced repetition: flashcard mode with increasing intervals
- Retrieval practice: quiz modes test vocabulary in active language

## 6. ELPA21 Proficiency Descriptors

The English Language Proficiency Assessment for the 21st Century defines five performance levels aligned to content-area language use. History Hack content should be reviewed against these:

| Level | Receptive (Reading/Listening) | Productive (Writing/Speaking) |
|-------|-------------------------------|-------------------------------|
| 1 | Identifies isolated words and phrases | Produces single words or memorized phrases |
| 2 | Understands simple sentences about familiar topics | Produces simple sentences with support |
| 3 | Understands multi-sentence texts with some complexity | Produces connected sentences; emerging paragraphs |
| 4 | Understands complex texts with academic language | Produces organized paragraphs with academic language |
| 5 | Understands grade-level complex texts | Produces grade-level academic writing |

### Application to History Hack Content Tiers

- **Tier 1 (Simplified)**: Written for ELPA levels 2-3 receptive — short sentences, common words, concrete examples
- **Tier 2 (Standard)**: Written for ELPA levels 3-4 — complex sentences, academic vocabulary, abstract concepts
- **Tier 3 (Primary Sources)**: ELPA level 5+ — requires scaffolding (contextualization, vocabulary pre-teaching, guided reading questions) for levels 1-4

## 7. Tennessee-Specific ELL Context

### TN WIDA Adoption
Tennessee uses WIDA ACCESS for ELLs 2.0 as its annual English language proficiency assessment. History Hack content should align with WIDA proficiency level expectations used in TN schools.

### TN ELL Demographics (Relevant to Content Design)
- Spanish is the predominant home language for TN ELLs (~75%)
- History Hack's EN/ES bilingual support addresses the majority of TN ELL students
- Content should use Latin American standard Spanish (neutral register), consistent with TN ELL populations

### TN Social Studies Standards and ELL Access
- TN U.S. History EOC exam is in English only
- History Hack must prepare ELLs to demonstrate content knowledge in English while supporting comprehension in Spanish
- Bilingual vocabulary preparation is a critical bridge: students learn concepts in L1, demonstrate in L2
