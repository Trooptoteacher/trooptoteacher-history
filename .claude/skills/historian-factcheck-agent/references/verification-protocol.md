# Verification Protocol — Step-by-Step

This document expands the 6-step protocol in SKILL.md. Use it when a claim does not fall cleanly into a common pattern or when the operator asks for deep verification.

---

## Step 1 — Isolate the Claim (Atomic Splitting)

A sentence often contains multiple claims. Split into atomic claims before verifying.

### Example
Sentence under review:
> "The Dawes Severalty Act of 1887, signed by President Grover Cleveland on February 8, allotted 160-acre plots to individual Native families and resulted in the loss of approximately 90 million acres of tribal land between 1887 and 1934."

Atomic claims:
- A: A federal statute named "Dawes Severalty Act" was enacted in 1887.
- B: The Dawes Severalty Act was signed by Grover Cleveland.
- C: Cleveland signed the Dawes Act on February 8, 1887.
- D: The Act allotted 160-acre plots to individual Native families (basic allotment size).
- E: Approximately 90 million acres of tribal land were lost between 1887 and 1934 as a consequence of the Act.

Verify each independently. A may be VERIFIED (easy), B may be VERIFIED, C may be VERIFIED with a specific NARA record, D may be VERIFIED with the statute text, E will likely require a specific federal or institutional source for the acreage total and the date range.

### Edge cases in splitting
- **Causal claims** ("X caused Y") split into (a) X happened, (b) Y happened, (c) the causal link is attested in primary sources
- **Comparative claims** ("X was larger than Y") split into (a) X's size, (b) Y's size, (c) comparison
- **Quotes** are a single claim — either the quote is exact or it isn't; don't split words of a quote
- **Attributions** ("Lincoln said X") split into (a) Lincoln made a statement at [event/date], (b) the statement's exact text

---

## Step 2 — Classify the Claim Type

Refer to the table in SKILL.md. When in doubt:
- If it's a citation (statute or case), classify as citation
- If it includes a specific number, classify as numerical (trigger extra scrutiny rules)
- If it's prose about what a document or actor did, classify as content or name

---

## Step 3 — Attempt Verification

### For statute citations
1. Go to GovInfo or National Archives
2. Confirm volume, page, and date
3. Quote the relevant statutory text if the claim is about what the statute DID (not just that it existed)
4. Cross-check the popular name against the official short title (e.g., the "Dawes Act" is officially the "General Allotment Act"; both names are acceptable)

### For case citations
1. Go to Justia, Oyez, or Cornell LII
2. Confirm reporter, volume, page, year
3. If the claim attributes the opinion to a specific justice, check the actual opinion's author line
4. If the claim is about the holding, verify against the opinion's text (not a summary)

### For numerical claims
1. Start with federal agency data if within scope (Census, BLS, BIA, Interior)
2. Move to institutional repositories if federal agencies don't cover the topic
3. If only a range of estimates exists, record all of them with sources, and recommend the content use the range — not a specific round number
4. Check whether the claim's number includes proper units (acres vs hectares, dollars vs 1862-dollars vs 2025-dollars, raw count vs per-capita)

### For attributions and names
1. Confirm the person existed and held the role at the time claimed
2. Confirm the specific act attributed to them (signed the bill, wrote the opinion, cast the vote, etc.) is documented
3. Watch for common attribution errors:
   - Majority opinion author vs. Chief Justice (*Plessy* majority = Brown, not Fuller)
   - Bill sponsor vs. signer vs. committee chair
   - Cabinet secretary vs. bureau head vs. commissioner

### For quotes
1. Find the original source (speech transcript, letter, published essay, press report)
2. Compare word-for-word; note any paraphrase, omission, or ellipsis
3. Record the date, occasion, and original publication
4. If a famous quote cannot be found in primary sources, flag CANNOT VERIFY — many "famous quotes" are misattributed

---

## Step 4 — Record the Verdict

Use this exact format for every claim:

```
CLAIM: [exact text from content]
TYPE: [statute citation | case citation | date | name | numerical | geographic | event | quote | content]
VERDICT: [VERIFIED | NEEDS CITATION | CANNOT VERIFY | INCORRECT | CONFLICTING EVIDENCE]
VERIFYING SOURCE(S):
  - [Source 1: URL or archive ID, specific location (page/volume/section)]
  - [Source 2: URL or archive ID, specific location]
NOTES: [max 2 sentences; if INCORRECT, the correct version with source; if CANNOT VERIFY, what was searched]
RECOMMENDED ACTION: [auto-apply fix | soften to range | remove specific figure | add citation | no change]
```

Every VERIFIED verdict must have at least one source entry. An empty VERIFYING SOURCE line is not allowed on a VERIFIED verdict.

---

## Step 5 — STATUS Block

See `guardrails-and-stop-rules.md` for format and cadence.

---

## Step 6 — Final Report

See `report-template.md` for full structure.

---

## Worked Example — The "60,000 Native Children in Boarding Schools by 1900" Claim

(This is the actual error caught during the Unit 1 perspective bubbles QC run on 2026-04-18. Walk through it as a training example.)

### Step 1 — Isolate
Atomic claim: "Approximately 60,000 Native children were in federal boarding schools by 1900."

### Step 2 — Classify
Type: numerical (specific round number — trigger extra scrutiny)

### Step 3 — Attempt verification
- Search National Native American Boarding School Healing Coalition: finds enrollment data showing ~20,000 by 1900 and ~60,000+ by the 1920s
- Search Bureau of Indian Affairs historical records: confirms NABSHC figures
- Search NARA catalog: confirms the boarding school enrollment growth trajectory

Conclusion: The figure 60,000 exists in authoritative sources BUT it applies to the 1920s, not 1900. For 1900, the figure is ~20,000.

### Step 4 — Record
```
CLAIM: "~60,000+ Native children by 1900 forcibly removed to boarding schools"
TYPE: numerical
VERDICT: INCORRECT
VERIFYING SOURCE(S):
  - National Native American Boarding School Healing Coalition: ~20,000 by 1900, rising to 60,000+ by the 1920s
  - U.S. Bureau of Indian Affairs historical enrollment data (via NARA): confirms trajectory
NOTES: The 60,000 figure is real but belongs to the 1920s. By 1900 the figure is ~20,000. The source claim conflates two different time periods.
RECOMMENDED ACTION: Revise to "~20,000 enrolled by 1900, rising to 60,000+ by the 1920s per the National Native American Boarding School Healing Coalition."
```

### Step 5 — STATUS
Produce STATUS block if this is the 5th, 10th, 15th, etc. claim of the session.

### Step 6 — Final report
This claim goes in the INCORRECT section of the final report with the recommended revision. Classify as SUBSTANTIVE (requires operator decision to apply the revision). Sean's standing policy applies: "unverified specifics → soften" — and here, we have a specific revision to recommend, not just a soften.

---

## Worked Example — The "175 Million Acres to UP+CP" Claim

### Step 1 — Isolate
Atomic claim: "Union Pacific and Central Pacific Railroad Companies received ~175 million acres in federal land grants."

### Step 2 — Classify
Type: numerical (specific round number — trigger extra scrutiny)

### Step 3 — Attempt verification
- Search Bureau of Land Management General Land Office records: finds that the 175 million acres figure is the total for ALL transcontinental railroad land grants across 1850–1871, not UP+CP specifically
- Pacific Railway Acts of 1862/1864 (GovInfo): specify the UP+CP land grant structure (alternate sections within 10 miles of the line, doubled to 20 miles in 1864)
- BLM historical summaries: UP received approximately 11.4 million acres (per Act); CP received approximately 11.6 million acres

Conclusion: The 175M figure is a real number but attributed to the wrong entity. UP+CP received roughly 23 million acres combined; the 175M is for all transcontinental railroads.

### Step 4 — Record
```
CLAIM: "Union Pacific and Central Pacific Railroad Companies (received ~175 million acres in federal land grants)"
TYPE: numerical
VERDICT: INCORRECT
VERIFYING SOURCE(S):
  - Bureau of Land Management, GLO historical records
  - Pacific Railway Act of 1862, 12 Stat. 489, § 3 (grant structure)
  - Pacific Railway Act of 1864, 13 Stat. 356 (doubled grant)
NOTES: The 175M figure represents total land grants to all federal transcontinental railroad projects 1850–1871, not UP+CP specifically. UP received ~11.4M acres and CP received ~11.6M acres per the 1862/1864 Acts.
RECOMMENDED ACTION: Replace with "Union Pacific received ~12 million acres and Central Pacific ~11.5 million acres in federal land grants, plus combined federal bond subsidies of ~$64 million under the 1862/1864 Acts."
```

---

## Common Failure Modes to Guard Against

1. **The "round number feels right" trap.** You see "~30 million buffalo killed" and think "sounds right." But verification shows 30M is the pre-slaughter population estimate, not the kill count. Always ask: what does this number count, exactly?

2. **The "cited source says something close" trap.** You find a source that says "60,000 by 1900" but a closer reading reveals "60,000 by the 1920s." Read the actual data, not the headline.

3. **The "attribution by association" trap.** Cleveland signed the Dawes Act, so the decision_makers list includes Cleveland. But if the claim is about who wrote the opinion or who chaired the committee, check that specific role — don't assume.

4. **The "popular name" vs "official citation" mismatch.** The "Dawes Act" is officially the "General Allotment Act." Both are fine, but the citation should use the name that matches Statutes at Large.

5. **The "date drift" trap.** A statute signed on Feb. 8 may have been passed on Feb. 7 and promulgated on Feb. 9. Match the claim to the specific date stated.

6. **The "modernization" trap.** Dollar figures from 1862 are not comparable to modern dollars without inflation adjustment. If the source cites $64 million in 1862 dollars, don't silently convert.

7. **The "fair quote" trap.** "Kill the Indian, save the man" is often attributed to Pratt as exact words. The original phrasing in Pratt's 1892 speech was slightly different ("kill the Indian in him, and save the man"). Quote precisely or mark as paraphrase.

---

© 2026 TroopToTeacher Technologies LLC. Proprietary. All rights reserved.
