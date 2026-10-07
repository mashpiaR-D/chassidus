# Mishneh Torah at index level: what each book is and where the inner teaching appears

**Only One research** · October 5, 2026 · early draft 0.1 · Result [016](../../CONTENTS.md#016) · manuscript 3 of 9 · [Cite](CITATION.bib) · [Quote check](../../verification/catalogue.md#mishneh-torah-at-index-level-what-each-book-is-and-where-the-inner-teaching-october-5-2026)

---
*Sources: `rambam/_text/mt-00-introduction.txt` to `mt-14-sefer-shoftim.txt` (Torat Emet Hebrew, one halachah per line). Book 1, Madda, is read in full in `mishneh-torah-madda.md`. The other thirteen books (about 750,000 words) were read here at index level: the structure of each book, and a search of its closing halachot and of the known places where the Rambam steps out of law into teaching. Every Hebrew line below came back "FOUND near line N" from `find_he.py verify <file> "<phrase>" --line N`.*

## How the Rambam built it

The Mishneh Torah has fourteen books (the numerical value of *yad*, "hand"). The Guide explains the plan (Guide III:35, lines 1223-1238 of guide.txt): each book is a class of commandments with one purpose. Madda holds the beliefs; the rest hold deeds. A pattern runs through the whole work: **the Rambam ends many sections of law with a paragraph of inner teaching.** Those closing paragraphs are where the guide should look.

## The books

| # | Book | What it is | Where the inner teaching appears |
| --- | --- | --- | --- |
| 0 | Introduction | The chain of the Oral Torah from Moses to Rav Ashi; the 613 commandments; the plan of the work | The chain of transmission as one living line of teachers |
| 1 | Madda (Knowledge) | Unity, love and fear, traits, study, idolatry, return | The whole book; see `mishneh-torah-madda.md` |
| 2 | Ahavah (Love) | Shema, prayer, tefillin, mezuzah, tzitzit, blessings, circumcision | Kavanah in Shema and prayer; the mezuzah as a waking bell (read in `mishneh-torah-madda.md`) |
| 3 | Zemanim (Times) | Shabbat, eruv, festivals, fasts, the calendar, Purim and Chanukah | Joy in the mitzvah (Lulav 8:15); seeing yourself leaving Egypt; crying out in trouble; peace; Shabbat as the sign |
| 4 | Nashim (Women) | Marriage, divorce, levirate marriage | The inner will to do good (Gerushin 2:20) |
| 5 | Kedushah (Holiness) | Forbidden relations, forbidden foods, slaughter | Turning the mind to Torah against desire (Issurei Biah 22:20-21) |
| 6 | Haflaah (Utterances) | Oaths, vows, the nazirite, valuations | Vows as training of character; the nazirite "holy to G-d" |
| 7 | Zeraim (Seeds) | Mixed kinds, gifts to the poor, tithes, the sabbatical year | Tzedakah (Matnot Aniyim 10); "every person whose spirit moves him" (Shemittah 13:13) |
| 8 | Avodah (Temple Service) | The Temple, its vessels, the daily and Yom Kippur service, misuse of holy things | The chukim, laws without a known reason (Meilah 8:8) |
| 9 | Korbanot (Offerings) | Passover, festival, firstborn, substitute offerings | "Most laws of the Torah are counsels from afar" (Temurah 4:13) |
| 10 | Taharah (Purity) | Impurity of the dead, leprosy, vessels, foods, immersion pools | Immersing the soul "in the waters of pure knowledge" (Mikvaot 11:12) |
| 11 | Nezikin (Damages) | Property damage, theft, robbery, injury, murder and saving life | Law of the person; little direct inner teaching |
| 12 | Kinyan (Acquisition) | Sales, gifts, neighbors, agents, slaves | Compassion even where the law allows harshness (Avadim 9:8) |
| 13 | Mishpatim (Judgments) | Hiring, loans, claims, inheritance | Law of the person; little direct inner teaching |
| 14 | Shoftim (Judges) | Courts, witnesses, rebels, mourning, kings and wars | Kindness to mourners and the sick as "love your fellow" (Evel 14:1); the righteous of the nations (Melachim 8:11); the Messiah (Melachim 11-12, read in `mishneh-torah-madda.md`) |

## The inner halachot, with verified lines

**Joy is service (Zemanim: Lulav 8:15, line 1272).** "The joy a person has in doing the commandment and in the love of G-d who commanded them is a great service"; the one who lowers himself in joy "is the great one, honored, who serves from love". *Ties to:* S53, S50.

**You yourself left Egypt (Chametz uMatzah 7:6, line 1121).** "In every generation a person must show himself as if he himself has now come out of the slavery of Egypt." *Ties to:* S78 (The higher return), technique `picturing`. A rare place where the Rambam commands a work of imagination.

**Trouble is not chance (Taaniyot 1:1-3, lines 1555-1557).** Cry out in every trouble; this is "one of the ways of return". To say "this is the way of the world, it happened by chance" is "the way of cruelty" (line 1557). *Ties to:* S51 (The sudden cry), S85. Note: the Rambam's providence here is broader than in Guide III:17.

**The greatest joy (Megillah 2:17, line 1669).** "There is no greater joy than to gladden the heart of the poor, orphans, widows and converts; one who gladdens these unfortunate ones is like the Shechinah." *Ties to:* S54, S86, technique `act`.

**Peace (Chanukah 4:14, line 1698).** "The whole Torah was given to make peace in the world."

**Shabbat is the sign (Shabbat 30:15, line 659).** "Shabbat is the sign between G-d and us forever." *Ties to:* S76.

**The inner will (Gerushin 2:20, nashim line 583).** A Jew "wants to be of Israel and wants to do all the commandments"; it is only his inclination that overpowered him. *Ties to:* S41. Used by the Rebbe (see `mishneh-torah-madda.md`).

**A mind full of wisdom (Issurei Biah 22:21, kedushah line 504).** "Greatest of all: he should turn himself and his thought to words of Torah and widen his mind in wisdom, for the thought of forbidden relations grows strong only in a heart empty of wisdom." *Ties to:* technique `hold`, `choose_line`. The same advice is in Guide III:49 (line 1403).

> שאין מחשבת עריות מתגברת אלא בלב פנוי מן החכמה (kedushah line 504)

**Vows for character (Nedarim 13:23-25, haflaah lines 453-455).** Vowing "to set right his traits and fix his deeds" is praiseworthy, but one should not make a habit of vows; better to keep away from what should be kept away from without a vow. *Ties to:* Deot 3:1 guard.

**Tzedakah (Matnot Aniyim 10:1-3, zeraim lines 364-366).** "We must be more careful with tzedakah than with any positive commandment"; Israel are brothers, "and if a brother will not have mercy on a brother, who will?" *Ties to:* S54, technique `act`. The Tanya's Iggeret HaKodesh returns to tzedakah many times (for example lines 1292-1295 of the Tanya file).

**Anyone can be Levi (Shemittah 13:13, zeraim line 1594).** "Not only the tribe of Levi, but every single person from all who come into the world, whose spirit moves him and whose understanding teaches him to set himself apart to stand before G-d, to serve Him and to know G-d... is made holy of holies, and G-d will be his portion." *Ties to:* S83 (Accepting the yoke), S60. The Rebbe quotes it (Likkutei Sichos vol. 31, line 5348 of that file). The most universal line in the Mishneh Torah, and a good fit for D28 (ours).

> ולא שבט לוי בלבד אלא כל איש ואיש מכל באי העולם אשר נדבה רוחו אותו (zeraim line 1594)

**The chukim (Meilah 8:8, avodah line 1532).** One should look for the reasons of the laws, but a law with no known reason should not be taken lightly. David, when mocked for them, "added cleaving to the Torah". *Ties to:* S36 (Faith above knowing). Here the Rambam comes closest to the Chassidic "kabbalas ol".

**Laws as counsels (Temurah 4:13, korbanot line 510).** "Most laws of the Torah are only counsels from afar, from the One great in counsel, to fix the traits and straighten all deeds." This is the Guide's reasons of the commandments (III:26-49) in one sentence.

**Immersion of the soul (Mikvaot 11:12, taharah line 1808).** Purity is a decree, "yet there is a hint": as one who intends to purify is pure once he immerses, so one who intends to purify his soul from bad thoughts and traits, "once he has resolved in his heart to leave those counsels and brought his soul into the waters of knowledge, is pure". The last halachah of the book of Purity. *Ties to:* S77, technique `depth`. *Proposed new technique* **R-T4 "Immersion in knowing"**: when stained by a thought or a trait, resolve once to leave it, then bring the mind down into one clear thought of G-d as into water.

> והביא נפשו במי הדעת טהור (taharah line 1808)

**Compassion toward the one in your power (Avadim 9:8, kinyan line 985).** Though the law allows hard work, "the way of piety and wisdom is to be merciful"; Israel, "whom G-d gave the good of the Torah... are merciful to all", as His mercy is "on all His works". *Ties to:* S54.

**Kindness as love of the fellow (Evel 14:1, shoftim line 654).** Visiting the sick, comforting mourners, escorting the dead, gladdening bride and groom: "all the things you want others to do for you, do for your brother". *Ties to:* S86, technique `act`.

**The righteous of the nations (Melachim 8:11, shoftim line 770).** One who keeps the seven Noahide laws "because G-d commanded them" has a share in the World to Come; but if he keeps them "by the decision of reason" only, he is not among the pious of the nations. *Ties to:* D28. Chassidus (the Rebbe's Noahide campaign) builds on this halachah (ours: the exact Chabad sources were not checked in this pass).

## What the index shows (ours)

- The Mishneh Torah is not only law. Its inner line is steady: know G-d (Madda), love Him (Ahavah), keep His times with joy (Zemanim), be holy with a full mind (Kedushah), train traits (Haflaah), give (Zeraim), take the laws without reasons on trust (Avodah), purify the soul (Taharah), be merciful (Kinyan), do kindness (Shoftim), and wait for a world "busy only with knowing G-d". - Where the guide needs law as the frame of practice (the hour before prayer, joy, tzedakah, immersion), the Mishneh Torah gives a sure anchor.

## Where the thread is thin

- Books 8-13 (Temple, offerings, purity, damages, acquisition, judgments) were read only at index level. Their inner content was sought in their closing halachot and in the places listed above; long stretches of detailed law were not read line by line. - Kiddush HaChodesh (the calendar and astronomy, in Zemanim) and the laws of the Temple are the thinnest for the guide's purpose.
