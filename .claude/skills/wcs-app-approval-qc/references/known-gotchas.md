# Known Gotchas — WCS App Approval Packets

Extended failure-mode catalog. These are the specific errors observed in the April 2026 baseline QC of `WCS-Responses-for-App-Approval.docx`. Check for every one on every new packet.

---

## G1. Academic-year drift

**Symptom:** Header says "AY 2025–26" but current date is in AY 25-26's spring term and submission is really for 26-27.

**Why it happens:** Document template created in fall, never updated at year boundary.

**Fix:** Grep for every AY reference. Update header, section titles, and footer metadata in one pass.

**Detection script:**
```bash
grep -nE "AY 20[0-9]{2}" wcs_packet.md
```

---

## G2. Tech-stack template pollution

**Symptom:** Document claims "React Native/Expo + native mobile app" with App Store and Google Play URLs, but product is actually a web app.

**Why it happens:** Boilerplate WCS response templates often assume mobile apps. Vendor does not clean out non-applicable sections.

**Fix:**
- For History Hack baseline: web-only, Azure (Node.js, React, TypeScript, Azure SQL Central US)
- Remove all App Store / Google Play references
- Rewrite §2.6 "Installation" as web-only with LTI launch

**Detection pattern:** If App Store URLs and Azure SQL references coexist, one of them is wrong.

---

## G3. VPAT 2.4 and WCAG 2.1 AA

**Symptom:** "Draft a VPAT 2.4 document against WCAG 2.1 Level AA"

**Why it's wrong:**
- Current ITI VPAT = **2.5Rev (April 2025)**
- Current target under ADA Title II DOJ rule = **WCAG 2.2 AA**
- WCS is in the April 24, 2026 compliance cohort (50k+ population public entity)

**Fix:** Global replace "VPAT 2.4" → "VPAT 2.5Rev" and "WCAG 2.1 AA" → "WCAG 2.2 AA"

---

## G4. 72-hour breach window cited as TN law

**Symptom:** "Tennessee law requires notification within 72 hours"

**Why it's wrong:** 72 hours is GDPR. Tennessee's statute (**TCA § 47-18-2107**) requires notification within **45 days** of discovery.

**Fix:** "Provider commits to notifying the District within 72 hours of confirmed or reasonably suspected unauthorized access, which exceeds the 45-day statutory minimum under TCA § 47-18-2107."

---

## G5. Grade-7 COPPA contradiction

**Symptom:** "Designed for grades 7–11" AND "does not knowingly collect personal information from children under 13"

**Why it's wrong:** Grade 7 includes many 11- and 12-year-olds. If any user is under 13, COPPA applies and school-consent mechanism under 16 CFR § 312.5(c)(10) must be documented.

**Fix options:**
- Restrict stated scope to grades 8–12 or 9–12 if that matches product
- OR document school-consent mechanism, data minimization, and deletion rights for under-13 users

---

## G6. FERPA School Official prongs missing

**Symptom:** "Operates as a School Official under FERPA (20 U.S.C. § 1232g)"

**What's missing:** The three prongs from **34 CFR § 99.31(a)(1)(i)(B)**:
1. Performs institutional service the district would otherwise use employees for
2. Under the district's **direct control** regarding data use and maintenance
3. Subject to FERPA's use and redisclosure requirements

**Fix:** Quote all three verbatim in both the Privacy Policy and DPA Article 4.

---

## G7. Subprocessor list blank

**Symptom:** DPA Article 12 says "[INSERT LIST]"

**Required disclosures for History Hack:**
- Microsoft Azure (hosting, Azure SQL, identity)
- ElevenLabs (voice synthesis)
- HeyGen (video avatar generation)
- Any analytics SDK (Segment, Mixpanel, etc.) — if used
- Any email delivery (SendGrid, Postmark) — if used
- Any auth provider (Auth0, Clerk, Microsoft Entra) — if used

Format as table: Provider | Purpose | Data Categories | Data Location | DPA in Place

---

## G8. DPA survival clause incomplete

**Symptom:** "Articles 3, 7, 10 survive termination"

**What's missing:** Articles 9 (Breach Notification), 11 (Data Portability), and 14 (Governing Law) must also survive. A district that cannot export data or invoke governing law after termination is exposed.

**Fix:** "Articles 3, 7, 9, 10, 11, and 14 survive termination of this Agreement."

---

## G9. AI disclosure undersells AI footprint

**Symptom:** Only ElevenLabs and HeyGen listed, but vendor has broader AI usage.

**Expanded enumeration required:**
- Production student-facing AI (voice, avatars, chatbot, tutoring, question generation, adaptive difficulty)
- Authoring-time AI (content drafting, item writing, image generation) — disclose even though no student data touches it
- Explicit "No" categories (e.g., "No LLM-based student chat in production")

**WCS reviewers assume missing = hidden.** Full disclosure is safer.

---

## G10. "Active workstream" hedging reads as certification

**Symptom:** "Active 1EdTech LTI certification workstreams in project history"

**Problem:** District reviewer reads this as "probably certified." When it reaches legal counsel who finds no certification, trust is damaged.

**Fix:** Use concrete language:
- "Not 1EdTech LTI Certified. Implementation is compatible with the 1EdTech LTI 1.3 specification. Certification application planned for [date]."
- "Not Schoology Certified. Compatible via LTI 1.3 launch."

---

## G11. Whitelist URLs listed as action, not provided

**Symptom:** §2.6 says "compile full list" with no list attached.

**Problem:** WCS network admins cannot deploy the app. This is a submission blocker.

**Minimum list:**
- historyhack.app (primary)
- api.historyhack.app (API)
- auth.historyhack.app (or Entra endpoint)
- *.azurewebsites.net (Azure App Service, if applicable)
- *.database.windows.net (Azure SQL, if applicable)
- *.elevenlabs.io (voice)
- *.heygen.com (avatar)
- CDN FQDN (Cloudflare, Azure Front Door, etc.)
- Any font/asset CDNs

---

## G12. Common Sense Privacy not actually submitted

**Symptom:** "Submit History Hack for Common Sense evaluation" in action list but no reference number.

**Problem:** Common Sense review takes 6–12 weeks. If submission is now, rating will not be back before WCS decision.

**Fix:** Submit immediately. Record reference number. State: "Common Sense Privacy evaluation submitted [DATE], reference #[X], expected review completion [DATE]."

---

## G13. Tennessee Age-Appropriate Materials Act not addressed

**Symptom:** No mention of Public Chapter 744 of 2022.

**Why it matters:** TN Age-Appropriate Materials Act applies to instructional materials in TN public schools. US History content (slavery, civil rights, Indigenous removal, Vietnam, post-9/11) includes material that requires documented review.

**Fix:** Add subsection with:
- Content review process (who reviews, against what standard)
- Teacher override controls (can a teacher hide a lesson?)
- Parent visibility (can parents see what content their student accessed?)

---

## G14. Data Definitions in DPA Article 2 too thin

**Symptom:** Only "Student Data" defined.

**Minimum terms to define:**
- Student Data
- District
- Provider
- Personally Identifiable Information (PII)
- De-identified Data
- Authorized User
- Service
- Subprocessor
- Effective Date

One-term Definitions sections get redlined.

---

## G15. Internal PM language in external document

**Symptom:** "WEEK 1 priority" in the scorecard

**Problem:** External reviewers don't know the internal sprint cadence. Reads as unprofessional.

**Fix:** Replace with "Critical," "Immediate," or "Required before submission."

---

## G16. Contradictory WCS authorization status

**Symptom:** Packet describes WCS approval as pre-submission, but memory shows prior authorization (e.g., Aug 2026 supplemental-curriculum approval under TCA 49-6-2202(a)(3)).

**Fix:** At the top of the packet, state relationship to prior authorization:
- "Updating existing WCS authorization (effective [date]) to [new scope]"
- OR "Separate submission for [full district deployment / pilot expansion / new grade band]"

Do not submit a packet that appears to contradict WCS's own prior decision.

---

## G17. Placeholder-token contamination

**Symptom:** `[insert final domain]`, `[INSERT CLOUD PROVIDER]`, etc., left in final prose.

**Detection:** grep for: `\[insert`, `\[INSERT`, `TBD`, `TODO`, `XXX`, `FIXME`, `{{`, `}}`

**Any hit = Blocker.**

---

## G18. Multiple draft banners

**Symptom:** Header has "FLAG FOR HUMAN AND LEGAL REVIEW BEFORE SUBMISSION" AND footer has "DRAFT — LEGAL REVIEW REQUIRED"

**Fix:** One prominent banner (top of doc). One unobtrusive footer stamp with version + date.

---

## G19. Governing law venue too narrow

**Symptom:** DPA Article 14 pins disputes to "Williamson County, Tennessee" courts.

**Problem:** This is vendor-favorable (vendor is in Franklin/Williamson County). WCS's standard DPA may require a different venue. District may reject.

**Fix:** Use "Tennessee law; venue as mutually agreed" OR match WCS's template exactly.

---

## G20. Military / biographical credentials in submission footer

**Symptom:** Vendor bio includes "Retired USAF Master Sergeant" — true and impressive, but not relevant to WCS app approval.

**Fix:** Keep credentials directly relevant to this submission:
- "Tennessee Level 5 U.S. History Teacher"
- "M.Ed., [institution]"
- Vendor contact (phone, email)

Save military credentials for pitch decks and About pages.
