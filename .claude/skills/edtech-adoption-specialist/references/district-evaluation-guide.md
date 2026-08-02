# District Technology Evaluation Guide

This reference covers how to prepare vendor responses for district-level application evaluation forms in Tennessee. The primary reference model is the Williamson County Schools (WCS) Application Evaluation form, which is among the most comprehensive in the state. Other districts (MNPS, SCS, etc.) follow similar patterns.

## Overview of District Vetting Process

Most Tennessee districts follow a multi-stage process:

1. **Vendor submits application** — Complete an evaluation form and provide supporting documentation
2. **Technology department review** — IT reviews security, SSO, data privacy, and infrastructure compatibility
3. **Instructional review** — Curriculum team evaluates pedagogical value and standards alignment
4. **Privacy/legal review** — Legal counsel reviews terms, DPA, and privacy policy
5. **Approval or denial** — Decision communicated with any conditions
6. **Ongoing monitoring** — Annual review and DPA renewal

## WCS Application Evaluation Form — Section-by-Section Guide

### Section 1: General Application Information

Prepare the following for every submission:

| Field | Guidance |
|-------|----------|
| Application Name | Official product name as it appears in app stores and marketing |
| Vendor/Company Name | Legal entity name (e.g., "TroopToTeacher Technologies LLC") |
| Vendor Contact | Name, email, phone of primary point of contact |
| Application URL | Production URL of the application |
| Application Description | 2-3 sentence description emphasizing educational purpose and target grade levels |
| Target Audience | Specific grade levels and subject areas (e.g., "Grades 9-12, U.S. History") |
| Cost/Pricing Model | Free, freemium, per-student, per-school, per-district — be specific |
| Platform Availability | Web, iOS, Android, Chromebook — list all supported platforms |

### Section 2: Account Management & Authentication

Districts prioritize SSO and centralized account management. Prepare responses for:

| Question Area | How to Respond |
|--------------|----------------|
| **Does the app require student accounts?** | Yes/No. If yes, describe what data is collected at account creation. |
| **SSO support** | List all supported protocols: SAML 2.0, OAuth 2.0, OpenID Connect. Name specific providers: ClassLink, Microsoft Entra ID, Google. |
| **ClassLink integration** | Critical for WCS and many TN districts. If not yet integrated, state timeline. ClassLink uses SAML or OIDC. |
| **Schoology LTI integration** | WCS uses Schoology as its LMS. Support for LTI 1.3 and LTI Advantage (Deep Linking, Assignment and Grade Services) is strongly preferred. |
| **Automated provisioning** | Describe support for OneRoster CSV, OneRoster REST API, SCIM, or Clever. |
| **Can accounts be created without student email?** | Important for younger students. Describe class code, teacher-created, or rostering-based options. |
| **Account deletion process** | Describe how accounts are deleted upon request or contract termination. Include timeline. |

#### SSO Implementation Details to Document

```
Supported SSO protocols:
- SAML 2.0: [Yes/No] — [Implementation details]
- OAuth 2.0: [Yes/No] — [Implementation details]
- OpenID Connect: [Yes/No] — [Implementation details]

Supported identity providers:
- ClassLink: [Yes/No/Planned] — [Timeline if planned]
- Microsoft Entra ID (Azure AD): [Yes/No]
- Google Workspace: [Yes/No]
- Schoology (via LTI): [Yes/No] — [LTI version supported]

Rostering/Provisioning:
- OneRoster v1.1 CSV: [Yes/No]
- OneRoster v1.1 REST API: [Yes/No]
- Clever: [Yes/No]
- SCIM: [Yes/No]
- Manual CSV import: [Yes/No]
```

### Section 3: Data Privacy & FERPA

| Question Area | How to Respond |
|--------------|----------------|
| **What student data is collected?** | Provide an exhaustive list: name, email, school, grade, usage data, assessment scores, etc. Categorize as PII vs. non-PII. |
| **Is data shared with third parties?** | List all subprocessors with their purpose. If none, state explicitly. |
| **Is data used for advertising or marketing?** | Must be "No" for school products. |
| **Is data sold to third parties?** | Must be "No" — required by Tennessee law. |
| **Where is data stored?** | US-based data centers required. Name the cloud provider and region (e.g., "Microsoft Azure, East US 2 region"). |
| **Data retention policy** | Specify how long data is retained and what happens after contract termination. |
| **Data deletion upon request** | Describe the process and timeline for data deletion requests. |
| **FERPA compliance statement** | Provide or reference your FERPA compliance statement. |
| **Will you sign a DPA?** | Should be "Yes." Reference your DPA template or willingness to sign the district's DPA. |
| **SDPC NDPA** | State whether you have signed or are willing to sign the Student Data Privacy Consortium National Data Privacy Agreement. |

### Section 4: Data Security

| Question Area | How to Respond |
|--------------|----------------|
| **Encryption in transit** | "All data transmitted using TLS 1.2 or higher." Specify if HSTS is enforced. |
| **Encryption at rest** | "All data encrypted at rest using AES-256." Name the mechanism (e.g., Azure Storage Service Encryption). |
| **Access controls** | Describe role-based access controls (RBAC), least-privilege principles, and MFA requirements for staff. |
| **Penetration testing** | Describe frequency (annual recommended) and whether results are available. |
| **Data breach notification** | "District will be notified within [72 hours / 30 days] of discovering a breach." Tennessee law requires notification within a reasonable time; districts often require 72 hours. |
| **Employee background checks** | "All employees with access to student data undergo background checks." |
| **SOC 2 / ISO 27001** | State certification status or timeline. |
| **Vulnerability management** | Describe patching cadence and vulnerability scanning practices. |

### Section 5: Content & Age-Appropriateness

| Question Area | How to Respond |
|--------------|----------------|
| **Content review process** | Describe how content is reviewed for age-appropriateness before publication. |
| **User-generated content** | If users can create/share content, describe moderation processes. |
| **Content aligned to standards** | Reference specific Tennessee Academic Standards (e.g., US.01–US.95 for U.S. History). |
| **TN Age-Appropriate Materials Act compliance** | Affirm compliance and describe content review procedures. |
| **Advertising** | "No advertising is displayed to students." Required for school products. |
| **External links** | Describe whether the app links to external sites and how those are vetted. |

### Section 6: AI Disclosure

This section is increasingly required by TN districts (2024+):

| Question Area | How to Respond |
|--------------|----------------|
| **Does the application use AI?** | Yes/No. If yes, describe specifically which features use AI. |
| **Is AI generative (creates content)?** | Distinguish between generative AI and classification/recommendation AI. |
| **Third-party or proprietary AI?** | Name the provider (e.g., "OpenAI GPT-4", "Anthropic Claude", "Proprietary model"). |
| **Is student data sent to AI models?** | Critical question. If yes, describe what data, whether it's anonymized, and retention. |
| **Is student data used for model training?** | Must be "No" for school products. |
| **Can AI features be disabled?** | Describe opt-out capabilities at district, school, teacher, or student level. |
| **Human review of AI outputs** | Describe oversight mechanisms. |
| **Training data sources** | Describe what data the AI was trained on. |

### Section 7: Accessibility

| Question Area | How to Respond |
|--------------|----------------|
| **WCAG conformance level** | Target WCAG 2.2 Level AA. State current conformance level honestly. |
| **VPAT available?** | Provide the VPAT document or link. Use the ITI VPAT 2.5 template. |
| **Keyboard navigation** | "All features are accessible via keyboard navigation." |
| **Screen reader support** | "Application is compatible with JAWS, NVDA, VoiceOver, and TalkBack." |
| **Captions/transcripts** | "All video and audio content includes captions and transcripts." |
| **Text resizing** | "Content supports text resizing up to 200% without loss of functionality." |
| **Color contrast** | "All text meets WCAG 2.2 AA contrast ratios (4.5:1 for normal text, 3:1 for large text)." |

### Section 8: Interoperability

| Question Area | How to Respond |
|--------------|----------------|
| **LTI support** | Specify version: LTI 1.1, LTI 1.3, LTI Advantage. |
| **LTI Advantage services** | Deep Linking, Assignment and Grade Services, Names and Role Provisioning Services. |
| **Grade passback** | Describe how grades are returned to the LMS (e.g., Schoology). |
| **OneRoster support** | CSV import/export, REST API. Specify version (1.0, 1.1). |
| **1EdTech certification** | State TrustEd Apps, LTI, or OneRoster certification status. |

### Section 9: Terms of Use & Legal

| Question Area | How to Respond |
|--------------|----------------|
| **Terms of Use URL** | Provide the public URL. |
| **Privacy Policy URL** | Provide the public URL. |
| **Intellectual property** | Clarify who owns content created by teachers and students in the platform. |
| **User content gallery** | If student/teacher work can be displayed publicly, describe the opt-in process and privacy controls. |
| **Indemnification** | Describe vendor indemnification obligations. |
| **Governing law** | Specify (Tennessee preferred for TN districts). |

---

## Common Compliance Gaps & How to Resolve Them

| Gap | Severity | Resolution |
|-----|----------|-----------|
| No ClassLink integration | High | Contact ClassLink for integration partnership. Minimum viable: SAML IdP integration. |
| No VPAT document | High | Complete ITI VPAT 2.5 template. Can be self-assessed initially but third-party audit recommended. |
| No DPA template | Blocker | Draft a DPA or adopt the SDPC NDPA template. |
| AI features with no opt-out | High | Implement feature flags at the district/school/teacher/student level. |
| Student data stored outside US | Blocker | Migrate to US-based data center region. |
| No data breach notification plan | High | Draft incident response plan with 72-hour notification commitment. |
| No iKeepSafe certification | Medium | Begin the application process at ikeepsafe.org. |
| Privacy policy missing COPPA language | High | Add required COPPA disclosures covering data types, use, sharing, parental rights, and deletion. |
| No LTI integration | Medium | Implement LTI 1.3 to integrate with Schoology and other LMS platforms. |
| Terms of Use silent on student IP | Medium | Add clear clause that students and teachers retain IP rights to their content. |

---

## District-Specific Notes

### Williamson County Schools (WCS)
- **LMS:** Schoology
- **SSO:** ClassLink, Microsoft Entra ID
- **Form:** WCS Application Evaluation (submitted via technology department)
- **Key concerns:** AI disclosure, data privacy, ClassLink compatibility, LTI with Schoology

### Metro Nashville Public Schools (MNPS)
- **LMS:** Schoology
- **SSO:** ClassLink
- **Form:** MNPS Technology Request Form
- **Key concerns:** Equity and accessibility, FERPA compliance, data minimization

### Shelby County Schools (SCS)
- **LMS:** Canvas
- **SSO:** Clever, Google Workspace
- **Form:** SCS Instructional Technology Evaluation
- **Key concerns:** Cost-effectiveness, standards alignment, student data privacy
