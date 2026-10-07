# Only One research: Chassidus

> [!IMPORTANT]
> **This is early work.** It is about one month into the research, and there is a lot more to come. Studies here will be corrected, finished and added to, and some findings will change as the reading goes deeper. Read it as a first look at work in progress, not a finished book.

This repository contains research on Chassidus produced by Claude, Anthropic's AI model, working under the direction of the Only One project.

The question at the center of it is one the Rebbe answered in a single line in 1965: that all of Chassidus is one point. That point is the Essence of G-d, present in everything, so that "there is nothing besides Him" holds even in the lowest place. The research tests that claim against the library. It reads the Chabad works, and the books they stand on, line by line where it can. Of every line, subject and work it asks two things: how does this carry the one idea, and what does it do to a person who sits with it?

The collection includes results at different stages of checking. Every Hebrew quote was checked against its line in the source text when the research was done. A second, independent check, made for this release, covers every quote whose book we could check again here. Some readings could still have problems, such as a quote placed at the wrong line or a reading pushed further than the text goes. We will fix any such problems quickly. Throughout, the manuscripts mark which ties are the text's own (*stated*) and which are ours (*ours*, *reading*).

## Navigating the collection

The current catalogue contains <!-- n:manuscripts -->459<!-- /n --> manuscripts organized into <!-- n:families -->47<!-- /n --> results, about <!-- n:words -->4.0 million<!-- /n --> words in all. A result groups related manuscripts: a principal study, and the readings that carry it (one range of a book, one Rebbe's works, one source book). Each result is filed under one of six areas: the Unity Index, the Chabad works read line by line, the earlier books Chassidus stands on, contemplation, the person, and saying it plainly.

- Start with the [overview](OVERVIEW.md) for descriptions of the results.
- Use the [manuscript map](CONTENTS.md) to find individual manuscripts and their abstracts.
- The [`manuscripts/`](manuscripts/) directory holds each manuscript in its own folder, with a citation file.
- The [quote check](verification/README.md) explains how the Hebrew quotes were checked, and the [catalogue](verification/catalogue.md) gives the result for every manuscript. Most manuscripts, but not all, have been checked a second time.
- The [briefs](briefs/README.md) are the written questions that the studies started from.

### The reasoning, written out step by step

We are also releasing studies that write out *how* the sources reason, one step at a time, and not only what they conclude:

| Result | Subject |
|---|---|
| 035 | [The Gate of Unity as a step-by-step proof](manuscripts/SHY-the-Gate-of-Unity-as-a-step-by-step-proof-October-5-2026/manuscript.md) |
| 035 | [How the Mitteler Rebbe reasons about the unity: a procedure](manuscripts/MR-How-the-Mitteler-Rebbe-reasons-about-the-unity-a-procedure-October-5-2026/manuscript.md) |
| 035 | [How the later Rebbeim reason the unity at its deepest](manuscripts/DEEP-How-the-later-Rebbeim-reason-the-unity-at-its-deepest-October-5-2026/manuscript.md) |
| 035 | [One framework for thinking about the unity of G-d](manuscripts/One-framework-for-thinking-about-the-unity-of-God-October-5-2026/manuscript.md) |
| 032 | [The whole depth, station by station](manuscripts/FULL-DESCENT-the-whole-depth-station-by-station-October-1-2026/manuscript.md) |
| 033 | [The Depth Engine: how Chassidus takes any idea deeper](manuscripts/The-Depth-Engine-how-Chassidus-takes-any-idea-deeper-October-1-2026/manuscript.md) |
| 044 | [How the Rebbeim make a mashal, and how to make a new one](manuscripts/METHOD-how-the-Rebbeim-make-a-mashal-and-how-to-make-a-new-one-October-1-2026/manuscript.md) |
| 047 | [The ladder from zero: sixteen steps to the unity, for someone who does not yet believe](manuscripts/The-Ladder-From-Zero-October-1-2026/manuscript.md) |

## How the results were produced

The studies were done by Claude in Claude Code between September 28 and October 5, 2026. Each one started from a written brief, and <!-- n:briefs -->10<!-- /n --> of those briefs are kept in [`briefs/`](briefs/README.md). A brief says what to read, the one question to ask of every line, and what to bring back. Large books were split into ranges. Each range was read through, in order, by one research agent keeping running notes, and the reports were then merged into the principal study.

Three rules held everywhere:

1. **Quote only what is there.** Every Hebrew quote was copied from the text and checked, letter by letter, at its line with a small search tool (`find_he.py verify`) before it was kept. No Hebrew was written from memory; the few references given from memory are marked so. Text from scanned books is quoted exactly as the scan reads, errors included, and marked *OCR*.
2. **Say whose claim it is.** *Stated* means the text says it. *Ours* or *reading* means the tie, the order or the application is the research's own.
3. **Don't force it.** Where a tie is weak it is marked *thin* and left thin. Where the Rebbeim or the schools disagree, both sides are kept.

The library read is 220 works of Chabad and the wider Chassidic world, from the Baal Shem Tov to the Rebbe, together with earlier books Chassidus draws on: the Rambam, the Kuzari, the Zohar, R. Meir ibn Gabbai, the Ramak, the Maharal and the Shelah.

The direction came from the project's owner: which questions to ask and what mattered. Several manuscripts quote the owner's questions and decisions, and those notes are left as they were written. Much of the work was also written for the builders of the Only One guide, a chat that helps anyone, from any background, into the lived unity of G-d the Chabad way. The manuscripts say so where that is the case. Documents that were only build notes for the guide (voice drafts, simulated conversations, a product roadmap) are not part of this release.

## The texts themselves

The source books are not in this repository. The manuscripts quote them in short passages, each with its reference. To run the quote check yourself, you need your own copy of the texts; see [verification/README.md](verification/README.md).

## Versions and citations

We will keep the public release history of this collection. Corrections and revisions will be recorded as new versions, and earlier versions will stay available. See [VERSIONS.md](VERSIONS.md).

To cite an individual manuscript, use the `CITATION.bib` file in its folder.
