# Privacy, Security & AI Disclosure Guide

This reference provides specific guidance for drafting and reviewing privacy policies, security documentation, AI disclosure statements, and related compliance documents for EdTech vendors operating in Tennessee schools.

## Privacy Policy Requirements

An EdTech privacy policy for Tennessee schools must address all of the following. Each section includes recommended language patterns.

### 1. Scope & Applicability

State clearly who the policy applies to and in what context.

**Recommended language pattern:**
> This Privacy Policy describes how [Vendor Name] ("we," "us," or "our") collects, uses, and discloses information from and about users of [Product Name] ("the Service"), including students, teachers, school administrators, and parents who access the Service through their school or district ("School Users"). This policy applies specifically to our use of student data in the educational context and supplements our general privacy policy.

### 2. Data Collection

Enumerate every category of data collected. Be exhaustive.

**Categories to address:**

| Data Category | Examples | Required Disclosure |
|--------------|----------|-------------------|
| **Account information** | Name, email, school, grade, role | What is collected, why, and from whom |
| **Authentication data** | SSO tokens, session IDs | How obtained, retention period |
| **Usage/activity data** | Pages visited, time on task, features used | Whether collected, how used |
| **Assessment data** | Scores, responses, progress metrics | Storage, access controls, retention |
| **User-generated content** | Essays, projects, uploaded files | Ownership, storage, deletion |
| **Device/technical data** | IP address, browser type, OS, device ID | Whether collected, how used |
| **Location data** | General (IP-based) or precise (GPS) | Must disclose if collected; avoid precise location for students |
| **Cookies/tracking** | Session cookies, analytics cookies | List all cookies and their purposes |
| **Communication data** | In-app messages, support tickets | Storage and access policies |

### 3. COPPA Compliance Section

Required if any users may be under 13.

**Key provisions to include:**
- We do not knowingly collect personal information from children under 13 without verifiable parental consent or school consent under the COPPA school consent exception
- Description of what data is collected from children
- How parental consent is obtained (or how school consent operates)
- Parent's right to review, delete, and refuse further collection
- Contact information for privacy inquiries

**School Consent Exception (COPPA):**
> When [Product Name] is used in a school setting, the school or district may consent on behalf of parents for the collection of student information solely for educational purposes. We rely on the school to obtain any necessary parental consent before providing student information to us.

### 4. FERPA Compliance Section

**Key provisions to include:**
- Vendor acts as a "school official" with a "legitimate educational interest" as defined under FERPA
- Student education records are used solely for the purpose of providing the contracted service
- No re-disclosure of student PII except as authorized by FERPA
- Compliance with parent/eligible student rights to access and amend records
- Data destruction upon contract termination

**Recommended language pattern:**
> We may receive student education records from schools and districts as a "school official" under FERPA (34 CFR § 99.31(a)(1)). We use this information solely to provide the educational services described in our agreement with the school or district. We do not use student education records for any purpose other than providing, improving, or maintaining the Service as contracted. We do not disclose student education records to any third party except as directed by the school or district, or as required by law.

### 5. Tennessee-Specific Provisions

#### Tennessee Student Data Accessibility, Transparency, and Accountability Act

**Required provisions:**
- Student data is not sold or used for non-educational commercial purposes
- Data is accessible to authorized school/district personnel
- Transparent disclosure of data practices
- Data breach notification within a reasonable time (recommend 72 hours for district contracts)
- Data is deleted or returned upon contract termination

#### Tennessee Age-Appropriate Materials Act (Public Chapter 744)

**Recommended statement:**
> All content within [Product Name] has been reviewed for age-appropriateness in compliance with Tennessee Public Chapter 744. We maintain content review procedures to ensure no materials that are sexually explicit as defined under TCA § 49-6-2201 are included in the Service. Our content review process is documented and available upon request.

### 6. Data Sharing & Third Parties

**Must address:**
- Complete list of categories of third parties with whom data is shared
- Purpose of each sharing relationship
- Whether subprocessors have access to student data
- Subprocessor list (or commitment to maintain and disclose one)
- That data is never sold, rented, or traded
- That data is never used for targeted advertising

**Subprocessor disclosure format:**

| Subprocessor | Purpose | Data Access | Location |
|-------------|---------|-------------|----------|
| [Cloud Provider] | Infrastructure hosting | Encrypted data at rest | US |
| [Analytics Tool] | Anonymized usage analytics | Anonymized/aggregated only | US |
| [AI Provider, if applicable] | [Specific AI feature] | [Specify what data is sent] | US |

### 7. Data Retention & Deletion

**Specify:**
- How long each category of data is retained
- What triggers deletion (contract end, account deletion request, retention period expiration)
- Timeline for deletion after contract termination (recommend 30-60 days)
- Whether data can be exported before deletion
- Format of exported data

**Recommended language pattern:**
> Upon termination of our agreement with a school or district, we will delete all student education records within [30/60] days unless the school or district requests the data be returned to them. Schools and districts may request data export in a standard machine-readable format at any time during the contract period.

### 8. Security Measures

**Include in the privacy policy or link to a separate security page:**
- Encryption in transit (TLS 1.2+)
- Encryption at rest (AES-256)
- Access controls (RBAC, least privilege)
- Employee security training
- Background checks for employees with data access
- Penetration testing cadence
- Incident response procedures
- US-based data storage

---

## Terms of Service — Key Sections for EdTech

### Intellectual Property

**Critical provisions:**
- Vendor retains IP in the platform and content
- Teachers retain IP in content they create
- Students retain IP in content they create
- Vendor receives a limited license to display/process user content as needed for the Service
- Vendor does NOT acquire ownership of teacher- or student-created content
- Content galleries require explicit opt-in consent

**Recommended language pattern:**
> Teachers and students retain all intellectual property rights in content they create using [Product Name]. By submitting content to the Service, users grant [Vendor Name] a limited, non-exclusive license to store, display, and process the content solely as necessary to provide the Service. [Vendor Name] does not claim ownership of any user-created content.

### User Content Gallery Provisions (if applicable)

If the product features a gallery or showcase of user work:
- Participation must be opt-in, never default
- For students under 18, parental/guardian consent is required
- Users must be able to remove their content at any time
- Content in the gallery must not include student PII unless explicitly consented
- Describe moderation practices

### Acceptable Use

Address:
- Prohibited uses (commercial exploitation, harassment, illegal activity)
- Teacher vs. student account distinctions
- Content standards for user-generated materials
- Account sharing and credential policies

### Limitation of Liability & Indemnification

- Vendor indemnifies school/district for data breaches caused by vendor negligence
- Typical limitation of liability caps (varies by contract)
- Governing law: Tennessee (for TN district contracts)

---

## AI Disclosure Statement Template

For vendors that use AI features, prepare a standalone AI disclosure document:

```markdown
# AI Disclosure Statement — [Product Name]

**Vendor:** [Legal Entity Name]
**Date:** [Date]
**Version:** [Version number]

## AI Features Overview

[Product Name] uses artificial intelligence in the following features:

| Feature | AI Type | Provider | Purpose |
|---------|---------|----------|---------|
| [Feature Name] | [Generative / Classification / Recommendation / etc.] | [3rd Party Name or "Proprietary"] | [Brief description] |

## Data Handling

### Data Sent to AI Models
[Describe exactly what data is sent to AI models, if any]

### Student Data Protection
- Student personally identifiable information (PII) is [never sent to / anonymized before being sent to] AI models
- Student data is NOT used to train or improve AI models
- [Describe any data anonymization or de-identification techniques]

### Third-Party AI Providers
| Provider | Data Sent | Data Retention by Provider | Training Exclusion |
|----------|-----------|---------------------------|-------------------|
| [Provider Name] | [What data] | [Retention period] | [Yes — data excluded from training / Contractual guarantee] |

## Opt-Out Capabilities

AI features can be disabled at the following levels:
- [ ] District level
- [ ] School level
- [ ] Teacher level
- [ ] Individual student level

To disable AI features, [describe the process — admin settings, contact support, etc.].

## Human Oversight

[Describe how AI outputs are supervised, reviewed, or moderated]

## Bias Mitigation

[Describe measures taken to identify and reduce bias in AI features]

## Model Improvement

- AI models are [not improved / improved] using data from the Service
- If improved: [Describe what data is used and how it is anonymized]
- Users [can / cannot] opt out of contributing to model improvement

## Contact

For questions about AI practices: [Contact information]
```

---

## Data Breach Response Plan Template

Districts expect vendors to have a documented breach response plan:

```markdown
# Data Breach Response Plan — [Vendor Name]

## 1. Identification & Classification
- How breaches are detected (monitoring, alerts, user reports)
- Classification criteria (severity levels)
- Initial assessment procedures

## 2. Containment
- Immediate containment steps
- Evidence preservation
- Affected system isolation

## 3. Notification
- **Internal notification:** [Team/role] notified within [X hours]
- **District notification:** Affected districts notified within 72 hours of confirmed breach
- **Parent notification:** Coordinated with the district per FERPA requirements
- **Regulatory notification:** Tennessee Attorney General if required by state law
- **Notification content:** Nature of breach, data affected, remediation steps, contact info

## 4. Investigation & Remediation
- Root cause analysis
- Affected data/user identification
- System remediation and patching
- Third-party forensics engagement criteria

## 5. Post-Incident
- Lessons learned review
- Policy/procedure updates
- District communication follow-up
- Documentation retention (minimum 3 years)
```

---

## iKeepSafe Certification Guidance

### COPPA+ Certification
- Apply at [ikeepsafe.org](https://ikeepsafe.org)
- Requires review of privacy policy, data practices, and consent mechanisms
- Annual renewal required
- Typical timeline: 4-8 weeks for initial certification
- Cost: Varies by company size (contact iKeepSafe)

### FERPA Certification
- Companion to COPPA+ certification
- Reviews school official designation, data use limitations, and security practices
- Can be pursued simultaneously with COPPA+

### Preparation Steps
1. Ensure privacy policy addresses all COPPA and FERPA requirements (use this guide)
2. Document all data collection, storage, and sharing practices
3. Prepare a data flow diagram showing how student data moves through systems
4. Document parental consent mechanisms
5. Prepare data deletion and retention procedures documentation
6. Submit application with all supporting documentation

---

## Common Sense Privacy Evaluation

Common Sense Media evaluates EdTech products on a detailed rubric:

### Key Evaluation Areas
- **Data Collection:** Minimization, purpose limitation, transparency
- **Data Sharing:** Third-party access, advertising, tracking
- **Data Security:** Encryption, breach notification, access controls
- **Data Rights:** Access, deletion, portability, correction
- **Data Sold:** Whether data is sold or used for non-educational purposes
- **Ads & Tracking:** Presence of advertising or behavioral tracking
- **Parental Consent:** How consent is obtained for minors
- **School Purpose:** Whether the product is designed for and limited to educational use

### Preparation Steps
1. Complete a self-assessment using Common Sense's evaluation questions
2. Ensure privacy policy is detailed and transparent
3. Minimize data collection to what is educationally necessary
4. Eliminate all advertising and behavioral tracking in the school version
5. Provide clear data deletion and export capabilities

---

## 1EdTech TrustEd Apps Certification

### Overview
1EdTech (formerly IMS Global) TrustEd Apps certification demonstrates interoperability and privacy compliance:

- **LTI Certification:** Validates LTI 1.3 / LTI Advantage implementation
- **OneRoster Certification:** Validates roster data exchange compliance
- **TrustEd Apps:** Comprehensive certification covering privacy, security, and interoperability

### Preparation Steps
1. Implement LTI 1.3 and LTI Advantage (Deep Linking, AGS, NRPS)
2. Implement OneRoster v1.1 (CSV and/or REST API)
3. Complete the 1EdTech application conformance testing
4. Submit for certification review
5. Maintain certification through annual renewal

---

## VPAT (Voluntary Product Accessibility Template)

### Template Selection
Use the **ITI VPAT 2.5** template, which covers:
- WCAG 2.2 Level A and AA (required)
- Section 508 (required for federally-funded programs)
- EN 301 549 (optional, for international)

### Conformance Levels
For each success criterion, report one of:
- **Supports:** Fully meets the criterion
- **Partially Supports:** Some functionality meets the criterion
- **Does Not Support:** Does not meet the criterion
- **Not Applicable:** Criterion is not relevant to the product

### Key Sections to Complete
1. Product description and evaluation methods
2. WCAG 2.2 Level A criteria (all must be addressed)
3. WCAG 2.2 Level AA criteria (all must be addressed)
4. Remarks and explanations for each criterion
5. Remediation plans for any "Partially Supports" or "Does Not Support" items

### Tips
- Be honest about conformance levels — districts and accessibility consultants will verify
- Include specific remarks for each criterion, not just the conformance level
- Provide a remediation timeline for any gaps
- Update the VPAT with each major product release
