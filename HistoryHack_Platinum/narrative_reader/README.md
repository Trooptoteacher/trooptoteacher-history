# Narrative Textbook (Reader) — drop folder

Drag the **narrative textbook PDFs** into THIS folder, one per unit, named exactly:

```
HH_Unit01_Reader.pdf
HH_Unit02_Reader.pdf
HH_Unit03_Reader.pdf
HH_Unit04_Reader.pdf
HH_Unit05_Reader.pdf
HH_Unit06_Reader.pdf
HH_Unit07_Reader.pdf
HH_Unit08_Reader.pdf
HH_Unit09_Reader.pdf
HH_Unit10_Reader.pdf
```

The exact filename matters — the upload script maps each one to its blob path:

| This file | → Azure Blob path | Shows in Library as |
|---|---|---|
| `HH_Unit01_Reader.pdf` | `books/unit01/HH_Unit01_Reader.pdf` | Unit 1 **Reader** |
| … | … | … |
| `HH_Unit10_Reader.pdf` | `books/unit10/HH_Unit10_Reader.pdf` | Unit 10 **Reader** |

## Notes
- **Per-unit, not one big file.** The Library serves the Reader per unit, so each unit's
  card opens that unit's reading. (There is no whole-course Reader slot.)
- If your downloaded files are named differently, either rename them to the pattern above
  before dropping, or drop them as-is and tell me the names — I'll adjust the mapping.
- After the files land here, `HistoryHack_Platinum/upload_library_blobs.sh` pushes them to
  Azure (same run as the workbooks/decks). No separate step.
- These are **not** committed as the products of record — this folder is a staging area so
  the files ride the existing upload pipeline, exactly like the deck/workbook deliverables.
