# The Chabad Library as Medicine

**Only One research** · October 5, 2026 · early draft 0.1 · Result [040](../../CONTENTS.md#040) · manuscript 2 of 47 · [Cite](CITATION.bib) · [Quote check](../../verification/catalogue.md#the-chabad-library-as-medicine-october-5-2026)

---
*A map of the Chabad library by what it heals: for each work, the problems of the human condition it addresses, the therapeutic program it lays out, and the psychological reframe its philosophy gives. It feeds the library of truths behind the guide in `Tanya Guided Meditation/universal/engine/`.*

## Tiers

| Tier | What | Status |
| --- | --- | --- |
| **A · The core medicine** | 22 works, 31 readers: Tanya; Torah Ohr; Likkutei Torah; the Mitteler Rebbe's Kuntres HaHispaalus, Sha'arei Teshuvah, Imrei Binah, Sha'arei Orah, Sha'ar HaYichud, Toras Chaim; the Tzemach Tzedek's Derech Mitzvosecha; the Rebbe Rashab's Kuntres HaAvodah, HaTefillah, Umaayan; the Rebbe Rayatz's Sefer HaSichos; the Rebbe's Hayom Yom, Inyanah Shel Toras HaChassidus, Likkutei Sichos (vols. 30–39 as held here); Biurei Tanya; R. Aharon of Strashelye, R. Hillel of Paritch, R. Yitzchak Eizik of Homel, R. Yehudah Leib of Yanovitch | **done** |
| **B · Maamarim and letters** | the maamarim collections and every Rebbe's Igros Kodesh, searched by condition | next |
| **C · Law, customs, histories** | one light pass each; lived cases pulled from the histories and memoirs | after B |

The Rebbe Rashab's *Toras Shalom* as held here is his halachic responsa, so it moved to Tier C.

## Tier A · what came back

- **322 problems, 210 programs and 314 reframes** from 31 readers, backed by **975 quoted passages**. Every quotation was re-checked against its source file by `build_map.py`: all 975 found, each at the line the reader gave.
- **43 conditions** a person could walk in with, in 11 families, from "I understand it, but my heart feels nothing" to "Constant worry about money, health and family" and "Grief for someone I lost".
- **118 candidate truths** for the guide, each in the engine's shape (a fixed meaning, doors by state, clothings by the person's world, where the picture breaks, who it is not for). A separate critic checked each against its passages: **97 supported, 21 partly, 0 not.**
- **A completeness critic** named what Tier A leaves missing, the commonest being marriage and home, a child in trouble, waiting for a partner or a child, illness, anxiety and sleeplessness as a condition in itself, real questions of faith, anger at God, decisions, shame, procrastination, repairing harm, aging, caregivers, survivors, and addiction. It also wrote the search plan for Tier B, with Hebrew probes and hit counts from the Rebbe's letters.

How much of each work is medicine, in the readers' words: **core** for the Tanya and Kuntres HaHispaalus; **substantial** for Sha'arei Teshuvah, Kuntres HaAvodah, HaTefillah and Umaayan, Hayom Yom and Sha'arei Avodah; **some** for the maamarim collections (Torah Ohr, Likkutei Torah, Toras Chaim, Sha'arei Orah, Pelach HaRimon, Chanah Ariel), the Rebbe's Likkutei Sichos and essay on Chassidus, the Rayatz's Sefer HaSichos and Biurei Tanya; **little** for Sheeris Yehudah, which is mostly halacha.

## Files

| File | What |
| --- | --- |
| MAP.md | **Start here.** The 43 conditions, by family, each linking to its entry |
| map/ | One file per family: each condition in full, with its programs, reframes, cautions, key passages and candidate truths. Every source id links to the passage |
| WORKS.md · works/ | The same material by work: what each is, how much is medicine, its model of the person and philosophy, what it treats, and every passage it quoted |
| CHECKS.md | The quotation check, the verdict on every candidate truth, what is missing, and the Tier B and C plan |
| truth-candidates.json | The 118 candidate truths in the engine's shape, with sources and verdicts. Candidates, not yet approved for the guide |
| `data/tier-a.json` | The study's full output. `python3 build_map.py` rebuilds everything above from it |

## How it's read

Nobody reads 311 MB of Hebrew word by word in one pass. Each reader does a structural read of its work (outline, openings), searches it with a keyword kit for where it treats a human condition, and reads those passages closely. Every quotation is copied from the file and checked by `tools/find_he.py verify` before it is recorded; readers say in `coverage` what they read closely, skimmed, and did not reach.

- `tier-a-readers.json` · the 31 assignments: work, file, line range, focus
- `tools/find_he.py` · outline, skim, read, grep, count and verify Hebrew in the library's text files (letters-only matching; prints without nikud)
