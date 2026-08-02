---
name: us-history-hack-packet-builder
description: "Assemble, brand, and secure a for-sale U.S. History Hack product packet for Teachers Pay Teachers (TpT) or any download sale. Wraps any workbook content PDF with required front/back matter in a fixed order — Meet the Author -> Copyright & Terms of Use -> Content -> How to Download & Print — stamps a brand strip (store name + App Store link) on every page, then applies a copyright watermark and AES-256 encryption (printing allowed, copy/edit blocked). Use when the user says: build the packet for Unit N, wrap this workbook for sale, assemble a TpT packet, add the About/Terms front matter, make this sellable, prepare a product for download, or re-run the packet workflow. For History Hack / TroopToTeacher Technologies LLC."
license: MIT
metadata:
  author: TroopToTeacher Technologies LLC
  version: '1.0'
---

# U.S. History Hack — For-Sale Packet Builder

## When to Use This Skill

Use whenever a finished workbook (Student, Teacher, Differentiation Pack, bundle, or any content PDF) needs to become a **sellable, branded, copyright-protected packet** — for Teachers Pay Teachers or any direct download sale.

Trigger phrases: "build the packet for Unit N", "wrap this for sale", "assemble a TpT packet", "add the About and Terms", "make this sellable", "prepare for download", "re-run the packet workflow".

## What the Packet Always Contains (fixed order)

Every for-sale packet is bundled in this exact order, decided with the founder (Sean Reynolds):

1. **Meet the Author** — bio, credentials, "Built to Tennessee Standards" (US.01–US.95, EOC blueprint), five-band differentiation, bilingual ELL supports, designed-with-TDOE-rubric, the ecosystem cards, and the **App Store QR + link**. (About pages 1–3)
2. **Copyright & Terms of Use** — full license, allowed/not-allowed, strictly-enforced notice (17 U.S.C.).
3. **Content** — the actual workbook PDF being sold.
4. **How to Download & Print** — step-by-step buyer instructions. (About page 4)

A **brand strip** ("U.S. History Hack 1877–Present" + "Get the app: apps.apple.com • trooptoteacher.com", clickable) is stamped on **every page**. Then a copyright watermark footer + faint diagonal mark go on every page, and the file is encrypted (empty user password so it opens freely; owner password locks copy/edit/annotate; **printing allowed** per TpT rules).

## Hard Facts — Keep These Accurate (do NOT drift)

- App name: **"U.S. History Hack 1877–Present"** (exact App Store title).
- App is **NOT free** — say "Free trial, then subscription." Never label it "Free." No specific trial-day count unless the founder confirms one.
- App URL: `https://apps.apple.com/us/app/u-s-history-hack-1877-present/id6757368709`
- Website: `https://www.trooptoteacher.com`  •  YouTube: `@TroopToTeacherTechnologies`
- YouTube videos are **English only** — do NOT claim Spanish videos. Bilingual strength = **Spanish ELL documents** for the standards/content.
- Do **NOT** use the word "scenario-based."
- Approval claim: **"Under district review in Tennessee"** as a supplemental resource. NEVER claim state/statewide approval. **Never name the county/district** (the founder's employer stays private).
- **No Franklin High School and no county name anywhere.** "Franklin, Tennessee" as the LLC location is the only allowed Franklin reference.
- Keep the **red / America 250 / Air Force One** color scheme (NAVY #1F3A5F, RED #B22234, GOLD #C8A04B). The founder loves it.
- TDOE rating wording: "TN Level 5 Educator (sustained highest rating)" + "4.96 / 5.00 five-year average."

## Instructions

1. **Set up the working directory.** The scripts assume they run from a folder that also contains `fonts/` and (regenerated) `app_qr.png`. Copy `scripts/*` into your working dir (e.g. `/home/user/workspace/tpt_launch/`) and ensure `fonts/` (DMSans + Inter TTFs) and `assets/app_qr.png` exist. If the QR is missing, run `python3 gen_qr.py` first.

2. **Edit copy in one place if needed.** All About-page copy lives in `build_about.py`; all Terms copy in `build_terms.py`. Edit there — changes flow automatically into every future packet because `build_packet.py` rebuilds front/back matter each run.

3. **Run the pipeline** for each content PDF:
   ```bash
   python3 build_packet.py <content.pdf> <output_basename>
   # e.g.
   python3 build_packet.py source/HH_Unit01_Student.pdf US_History_Hack_Unit1_Student_Workbook
   ```
   This writes the assembled file to `assembled/` and the final secured file to `secured/<output_basename>.pdf`.

4. **QC before sharing (mandatory).** Render the assembled (pre-secure) PDF and visually verify:
   - Order is Author → Terms → Content → Download/Print.
   - Brand strip sits cleanly at the bottom of every page (no collision with content footers).
   - No text overflow/wrapping on the About feature cards.
   - The App Store QR is crisp and the "Open in the App Store" link is present.
   ```bash
   python3 -c "import pypdfium2 as pdfium; d=pdfium.PdfDocument('assembled/<basename>.pdf'); [d[i].render(scale=1.1).to_pil().save(f'assets/qc_{i+1}.png') for i in [0,3,6,len(d)-1]]"
   ```
   Read the rendered PNGs and fix any issue before sharing.

5. **Share** the secured file with `share_file`. Use a stable `name` per product so versions stack (e.g. `tpt_unit1_student_packet`).

6. **Per-buyer watermark note.** TpT does not pass buyer identity, so the watermark is a generic single-classroom-license mark, not per-buyer. If the founder wants per-buyer stamping, that must be done manually per sale — flag this, don't fake it.

## Files in this skill

- `scripts/build_packet.py` — master assembler (front matter + Terms + content + back matter, brand strip, then secure).
- `scripts/build_about.py` — builds the 4-page About PDF (Author / TN standards & differentiation / ecosystem+QR / Download&Print).
- `scripts/build_terms.py` — builds the Copyright & Terms of Use PDF.
- `scripts/secure_pdfs.py` — watermark + AES-256 encryption (print allowed, copy/edit blocked). Owner pw: `HistoryHack-TTT-Owner-2026`.
- `scripts/brand.py` — shared brand kit (America 250 palette, fonts).
- `scripts/gen_qr.py` — regenerates the App Store QR (`assets/app_qr.png`).
- `scripts/app_qr.png` — prebuilt App Store QR (copy to your working `assets/` if needed).
- `fonts/` — DM Sans + Inter TTFs required by the build scripts.

## Examples

**"Build the packet for Unit 4 Teacher Edition"**
→ Confirm the content PDF path, run `python3 build_packet.py source/HH_Unit04_Teacher.pdf US_History_Hack_Unit4_Teacher_Edition`, QC-render, fix any layout issue, then `share_file` as `tpt_unit4_teacher_packet`.

**"I changed the trial to 7 days — update everything"**
→ Edit the trial wording in `build_about.py`, then re-run `build_packet.py` for each product. Front matter rebuilds automatically.
