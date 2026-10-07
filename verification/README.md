# Quote check

In a study of texts, the thing that can be checked by machine is the quotes. Did the book really say this, in these words? This folder holds that check for every manuscript in the collection.

## Two checks

**The first check was part of the research.** Before a Hebrew quote was kept, it was searched for at its line in the source text (`find_he.py verify FILE "…" --line N`) and kept only if it came back FOUND. Quote and text were compared letters only, so vowel points and punctuation don't matter, but a changed or missing word does. The manuscripts record this in their opening notes, often with a count ("72 quote slots, all FOUND"). That check ran against the whole library the research used.

**The second check was made for this release** by [`check_quotes.py`](check_quotes.py), working on its own. It takes every run of four or more Hebrew words in every manuscript, reduces it to letters only, and looks for it anywhere in a set of source books. It had the <!-- n:books -->37<!-- /n --> books packed with the Only One guide: the core Chabad works (the Tanya, Torah Ohr, Likkutei Torah, the Mitteler Rebbe's main works, the Tzemach Tzedek, the Rebbe Rashab's series and tracts, the Rebbe Rayatz and the Rebbe) and a few others. It did not have the rest of the library.

## What it found

- **<!-- n:quotes -->24,745<!-- /n --> quotes in all, and <!-- n:found -->15,198<!-- /n --> of them (<!-- n:pct -->61.4%<!-- /n -->) were found word for word in those books.**
- **Where the book was there, the quotes were there.** The results that read one book line by line, where that book is in the set (the Tanya, the Gate of Unity, Imrei Binah, the Rashab's tracts and series, Sha'arei HaYichud), carry <!-- n:single_quotes -->2,180<!-- /n --> quotes; <!-- n:single_found -->2,179<!-- /n --> were found. The one left over is a saying of the Baal Shem Tov quoted inside a Tanya reading, and the full-library search below found it in Tzava'at HaRivash.
- **The rest are not found *here*.** Most of them quote a book that was not in the set: the Zohar, the Maharal, the Rambam, the Shelah, the Rayatz's and the Rebbe's letters, the wider Chassidic world. "Not found here" means *not checked a second time*, not *wrong*.

By manuscript: <!-- n:all_found -->124<!-- /n --> had every quote found, <!-- n:partly_found -->245<!-- /n --> had some found, <!-- n:none_found_here -->75<!-- /n --> had none found here (almost all of them read books outside the set), and <!-- n:no_Hebrew_quotes -->15<!-- /n --> quote no Hebrew. The [catalogue](catalogue.md) gives the numbers for every manuscript, and [`quotes.json`](quotes.json) gives every quote, with the book and line where it was found.

## A spot check against the full library

To see what "not found here" usually means, twelve quotes the second check did not find were sent to a search over the full library of 220 works (the ChassidusIntelligence `verify_quote` tool, which also compares letters only):

| Quote begins | Manuscript | Full library |
|---|---|---|
| הלא כל זה בהשגחה פרטיית | The Tanya, lines 1121-1400 | found: Tzava'at HaRivash 120 |
| אבל כשמדבר רק דברים בטלים | Darkei HaChassidus | found: Tzava'at HaRivash 30 |
| וזו היא תחבולת היצר בערמה | The animal soul | found: Keter Shem Tov 1:17 |
| וזהו תכלית עבודת איש ישראל | Subjects, K02 | found: Keter Shem Tov 1:40 |
| ונמצא שאינו שוכב ויושב בטל | Darkei HaChassidus | found: Noam Elimelech, Introduction |
| על פי דיני התורה אסור להתאבל | The medicine map | found: the Rayatz's letters, vol. 14 |
| ואיך כוללת ב' הפכים בנושא אחד | Subjects | found: the Alter Rebbe's letters, letter 19 |
| אבל בלי צמצום והלבשה | The Gate of Unity | found by this check once a letter-form bug was fixed: Tanya, line 832 |
| כי שלש עשרה מדות שהתורה נדרשת | Subjects, K03 | not found: open |
| כמו שכביכול פרוש | Works, group 04 | not found: open |
| ואפי' אם יגיע להתפעלו' אלקית | The animal soul | not found: open (Chanah Ariel) |
| ויותר טוב ונקל הוא לקבל | The medicine map, Chanah Ariel | not found: open (Chanah Ariel) |

Eight of twelve were confirmed. The four still open come from scanned books whose wording may differ between copies, or from books the search tool may not hold. They are listed so they can be looked up by hand.

## What the check does not show

- It shows that the words are in the book. It does not show that they are at the line the manuscript gives. The research's own check did test the line; this one searches the whole book.
- It says nothing about whether a *reading* of a quote is right. That is what the *stated* / *ours* marks are for, and what readers are for.
- A quote broken by an ellipsis is checked piece by piece, so each piece is checked but not the gap between them.

## Running it

The texts are not in this repository. The guide carries them as study copies, and the release only quotes them in short passages. With your own copy, one passage a line (`reference ⟶ text`, plain or gzipped):

    python3 verification/check_quotes.py --texts PATH/TO/TEXTS

It rewrites `catalogue.md`, `catalogue.yaml` and `quotes.json`, and the numbers on this page.
