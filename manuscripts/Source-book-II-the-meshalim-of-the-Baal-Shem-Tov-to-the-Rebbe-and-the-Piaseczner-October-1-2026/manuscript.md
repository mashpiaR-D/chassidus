# Source book II: the meshalim of the Baal Shem Tov to the Rebbe, and the Piaseczner

**Only One research** · October 1, 2026 · early draft 0.1 · Result [044](../../CONTENTS.md#044) · manuscript 5 of 5 · [Cite](CITATION.bib) · [Quote check](../../verification/catalogue.md#source-book-ii-the-meshalim-of-the-baal-shem-tov-to-the-rebbe-and-the-piaseczner-october-1-2026)

---
Strand SB2 of the meshalim project (see `BRIEF.md`). Companion data: `sb2.json`. Principles: `PRINCIPLES.md` / `principles.json` (ids PR-L01 to PR-L15).

**What is here.** 189 meshalim, one entry per mashal per author (a mashal that two authors use gets an entry under each only when each uses it differently; otherwise it is listed under 'recurs'). By author: Baal Shem Tov 30, Maggid of Mezritch 24, Tzemach Tzedek 28, Rebbe Maharash 16, Rebbe Rashab 38, Rebbe Rayatz 18, the Rebbe 17, Piaseczner Rebbe 18. Also 22 statements by these Rebbeim about how a mashal works (section 2).

**How to read an entry.** *Mashal* = the picture, told plainly. *Nimshal* = what it explains. *Parts* = which part of the picture stands for which part of the meaning. *Breaks* = where the picture stops fitting; **[stated]** means the text itself says so, **[ours]** means it is our reading. *Principles* = which of R. Aharon's laws of the mashal it shows (PR ids). *Source* = work, line in the file, and the Hebrew, checked with `find_he.py verify ... --line N` (all FOUND). **OCR** marks a scanned source. *Recurs* = where other Rebbeim use it. *Guide* = a plain-English rendering with no religious words, for the chat guide.

**Verification.** Every Hebrew line in this file and in `sb2.json` returned FOUND at the stated line. 18 entries come from OCR scans and are marked.

**Principle key (from PR).** PR-L01: A mashal exists to give the mind a handle on something it cannot hold. It is a handle, not the thing. PR-L02: Explaining by mashal is dangerous, so it has three main conditions, besides smaller ones. PR-L03: Condition one: only someone who first understands the teaching itself, from its root, as received from a teacher, may make a mashal for it. PR-L04: A mashal can be true because everything below is built like what is above, and because with G-d all is one. PR-L05: The deeper the maker's grasp, the more meshalim he can make: thousands, hundreds, or only a few. PR-L06: Condition two: a mashal may describe only how G-d is drawn into the worlds and is one with them. It may never describe what He is in Himself. PR-L07: Condition three: even an allowed mashal must not be matched to its subject on every side. Name the one point where it holds, and say where it fails. PR-L08: The model case: a person is one person in many powers. That is where the mashal of man holds. It fails at change. PR-L09: The best mashal comes from the soul's own life in the body. The person finds the truth in himself first. PR-L10: After the mashal does its work, take the physical picture off and keep only the point, as it is above. PR-L11: A mashal taken literally does more harm than no mashal: it makes G-d physical, splits Him into parts, and lets everyone think he understands. PR-L12: A good mashal ends in wonder. The more one knows, the more one sees that He is beyond knowing. PR-L13: Knowing counts only when it is grasped and felt in the soul as life. A mashal is for moving the heart, not for holding a fact. PR-L14: The further the listener is from the source, the more light and the more detail the mashal needs. PR-L15: A wise teacher hides his wisdom in a foreign garment so a student can receive it, and his whole self is inside the mashal. This is how G-d makes a world.

PR-L04 (below is built like above) is tagged on nearly every entry, since nearly every mashal is drawn from creation; the more telling tags are PR-L07 (the stated break), PR-L09 (from the self), PR-L03/L05 (root and levels) and PR-L06 (never the Essence).

## 1. What the source book shows (ours)

- **Two styles.** The Baal Shem Tov and the Maggid mostly tell *stories*: a king, a prince, a father, a merchant. They aim at the heart and at service (prayer, joy, teshuvah, stray thoughts). Their breaks are rarely stated; we supplied most of them. From the Tzemach Tzedek on, the meshalim become *structural* (sun and ray, water in colored glass, a person's name, flint and coal, letters in a word). These aim at the mind: how the One relates to the many.
- **The break becomes explicit.** The later texts mark the break themselves, again and again ('אין המשל דומה לנמשל'): the sun shines by necessity, G-d by will (TZ-06); a father's narrowing creates nothing (MAG-01); the soul is affected by the body, He is not; sea water and what it covers are two things, but nature is His own garment (RSB-35); the teacher's mind is for himself, every divine light is for the world (RBE-08). This is R. Aharon's third condition (PR-L07) practised as a habit.
- **Choosing between meshalim.** The Tzemach Tzedek rejects 'a flame bound in a coal' for the hidden sefiros and prefers 'a person's name' (TZ-04, TZ-05); the Rashab prefers the shining gem to the sun (RSB-03). The Rebbe states the rule: Chassidus brings two meshalim because no one mashal fits every detail (method note, MEL 2732; RBE-07). This extends PR-L07: each mashal is named for the one point where it holds.
- **The root of the mashal is higher.** The Tzemach Tzedek, the Maharash and the Rayatz each say that a mashal is lower than the idea in form but higher in root, so only a great mind can make one (MHS-04, RYZ-06, method notes). This is R. Aharon's first condition (PR-L03) and his levels of mashal (PR-L05: Solomon 3000, R. Meir 300).
- **'The mashal is the nimshal'.** The Rashab goes furthest: rightly seen, the physical thing *is* what it shows, and this is 'from my flesh I see G-d' (RSB-16; PR-L09). The Maharash says the whole world is a map of its source (MHS-01, MHS-02; PR-L04). The Piaseczner adds that 'from my flesh' is more than a comparison, because every good power in us must exist above.
- **The favorite domains.** King and kingdom, father and son, light and sun, water, fire, speech and letters. Almost every mashal is drawn either from the soul in the body or from nature, exactly the two sources R. Aharon allows (PR-L04, PR-L09).

## 2. What these Rebbeim say about the mashal itself

| Who | Point | Hebrew (verified) | Source | PR |
| --- | --- | --- | --- | --- |
| Maggid of Mezritch | The father himself does not need the parable; the child 'forces' him into it. The parable's letters are channels through which the wisdom flows; a wise son can then reach the wisdom itself. | ובשביל הבן מרכיב האב הדבר חכמה העליונה עם האותיות ושכל חדשים של משל והחכמה היא גנוזה בתוך המשל | Maggid Devarav LeYaakov, line 187 | PR-L01, PR-L03, PR-L15 |
| Maggid of Mezritch | Once the child has grasped the idea, the letters of the parable are superfluous. 'Wisdom excels folly as light excels darkness': the light of the idea shines out of the dark story. | והנה המשל הוא לעצמו סכלות וחשך אך בשביל דבר חכמה שבו דברו אותו | Maggid Devarav LeYaakov, line 181 | PR-L01, PR-L10 |
| Maggid of Mezritch | Torah's parables are not throwaway husks: the garment itself is holy, a contracted form of the higher light (compare the Rebbe Rashab: 'the Torah's mashal does not hide, it reveals'). | והנה דברי תורה אינם כשאר משלים ח"ו כי תורת ה' תמימה צריך להבין גם המשל והמליצה | Maggid Devarav LeYaakov, line 178 | PR-L01, PR-L04 |
| Baal Shem Tov (Keter Shem Tov) / Maggid | The mashal is a vessel (kli); to reach its light one must 'strip off' its physicality and enter its inside. | המשל הוא כלי להשכל וכן הדיבור הוא כלי למחשבה | Keter Shem Tov, line 348 | PR-L01 |
| Tzemach Tzedek | Only one wondrous in wisdom, who knows the idea in its truth, can find it in foreign matters in many ways; so 'though the mashal is lower than the nimshal, its root is higher'. (R. Aharon's first condition, stated independently.) | לפי שבאמת צריך חכמה רבה ויתירה לכוין את המשל | Derech Mitzvosecha (Tzemach Tzedek), line 12 | PR-L03, PR-L05 |
| Tzemach Tzedek | Yet the nimshal is understood from within it, because in its own terms it is like the nimshal; so too prophecy sees G-d 'in likeness', and the Torah is 'the parable of the Ancient One'. | והענין כי המשל הוא ענין אחר שאינו ממהות הנמשל ורחוק ממנו בערך | Derech Mitzvosecha (Tzemach Tzedek), line 143 | PR-L07, PR-L04 |
| Tzemach Tzedek | A very deep idea needs a chain of parables, each lowering the last; Solomon needed 3000, R. Meir 300. The parable is to the nimshal like hair to the brain: a coarse garment that still carries life. | אשר לזאת יצטרך המשל למשל ר"ל דוגמא לדוגמא | Derech Mitzvosecha (Tzemach Tzedek), line 189 | PR-L05, PR-L01, PR-L14 |
| Tzemach Tzedek | Many sages grasp an idea without a mashal yet cannot make one; making it shows the mashal's root is above the idea. | אבל לעשות משל לזה אין ביכולתם כי לעשות המשל צריך חכם גדול ביותר | Maamarei Admur HaTzemach Tzedek, line 615 | PR-L03, PR-L05 |
| Tzemach Tzedek | At first glance the parable covers the idea; then one must leave it and grasp the nimshal. The test of having grasped it is understanding every detail of the parable: then it no longer hides but glows with the idea in all its details. | הוא שיעזוב את המשל לגמרי, ויתפוס בהנמשל | Sefer HaChakirah (Tzemach Tzedek), line 1123 | PR-L01, PR-L07, PR-L10 |
| Maharash | 'Yet not everyone can say a parable, only a great mind' (Solomon, R. Meir). Lower in form, higher in root. | והוא כמו משל לשכל שהמשל למטה מהשכל | Toras Shmuel (Maharash), line 9401 | PR-L03, PR-L05 |
| Rebbe Rashab | Though the mashal conceals, through it one understands well; when the idea is very deep it can only come through a garment. Each of Solomon's 3000 levels is 'only a mashal' for the one above (line 3112). [OCR] | דבלתי המשל לא הי' מבין את השכל | Hemshech Samach Vav (Rashab), line 3104 (OCR) | PR-L01, PR-L05 |
| Rebbe Rashab | The Torah as 'parable of the Ancient One' reveals G-d's essence rather than hiding it. [OCR] | דהמשל דתורה אינו משל המעלים, כ"א המגלה | Hemshech Samach Vav (Rashab), line 6340 (OCR) | PR-L01, PR-L06 |
| Rebbe Rashab | A parable for a depth beyond one's mind teaches at least THAT the depth exists, even when it cannot teach WHAT it is; this is how the 'screen' (parsa) works between worlds. | הרי עכ"פ יודע מזה שיש דבר שלמעלה מהשכל | Hemshech Ayin Beis (Rashab), line 2617 | PR-L12, PR-L07 |
| Rebbe Rashab | The Rashab's strongest statement: the physical parable, rightly seen, IS what it shows. He ties it to 'from my flesh I see G-d' (R. Aharon's principle of the mashal from the self, PR-L09). | בכל השגה אלקית ממשל גשמי שבאמת המשל הוא הנמשל, וזהו מבשרי | Hemshech Ayin Beis (Rashab), line 1849 | PR-L09, PR-L04 |
| Rebbe Rashab | Yet among parables there are differences: some still let the idea be understood, some only hint (like a riddle). Beriah is 'like a parable', Asiyah 'like a riddle' (line 3414). | דכללות ענין המשל הוא דבר זר מעצם השכל ומעלים ומסתיר על השכל | Hemshech Ayin Beis (Rashab), line 3403 | PR-L07, PR-L05 |
| Rayatz | The mashal lets even the animal soul grasp G-dliness; this is how the two souls are joined: the G-dly soul's idea dressed in the animal soul's mind. | שהרי המשלים הם דברים גשמי', וע"י המשל בא אל הנמשל להשיג את הענין האלקי | Sefer HaMaamarim (Rayatz), line 559 | PR-L01, PR-L09 |
| the Rebbe | The Rebbe's rule of method: when Chassidus brings two or more meshalim for one thing, each explains different details; e.g. cause-and-effect shows that a new thing exists, light-and-source shows its closeness to the source. | כי אין המשל מכוון להנמשל בכל הפרטים , ולכן מביאים שני משלים | Sefer HaMaamarim Melukat (the Rebbe), line 2732 | PR-L07, PR-L05 |
| Piaseczner | Since all comes from G-d, every noble power found in us must exist above, though we don't know how; 'from my flesh' is more than comparison. | כלומר כל ענין מבשרי אחזה אלוה שאומרים אינו משל לבד כי איך נוכל אנו להמשיל משל מאתנו אליו | Derech HaMelech (Piaseczner), line 939 | PR-L09, PR-L07 |
| Piaseczner | The meshalim of holy matters are not like fox fables (where fox and man are far apart): their root is above, for man is the image of the higher form. | אבל אין זה משל זר לגמרי אל הנמשל כמו משלי שועלים ומשלי כובסים | Mevo HaShe'arim (Piaseczner), line 174 | PR-L04, PR-L09, PR-L05 |
| Piaseczner | Citing Song of Songs Rabbah ('do not take this mashal lightly; by it a person can stand in Torah'); tell it carefully and in order, as if it happened, since the child sees it in his imagination and is moved. | וכן את המשל לא יזנחו המלמדים ואבות הבנים | Chovat HaTalmidim (Piaseczner), line 48 | PR-L01, PR-L13 |
| Piaseczner | The soul is held and surrounded by the body, but He is not held by the worlds; only a ray of His light shines in them. (R. Aharon's third condition.) | שאין המשל מהתגלות נפש האדם דומה לגמרי לנמשל | Chovat HaTalmidim (Piaseczner), line 315 | PR-L07, PR-L09 |
| Piaseczner | Each sage, in his own prophetic-like arousal, 'saw a different image'; the differences are not of logic but of what each one's soul saw. | ובדרך זה המשלים הנזכרים במדרש, שיש שאיזה תנאים אמרו כ"א משל אחר על דבר אחד | Derech HaMelech (Piaseczner), line 1491 | PR-L05, PR-L03 |

## 3. Families (cross-references inside SB2)

- **The prince far from the king (captive, exiled, disguised):** SB2-BST-11 (The minister who dressed like the prince), SB2-BST-18 (The father counting money), SB2-BST-24 (The prince who gets a letter in the village), SB2-MAG-06 (The captive prince), SB2-MAG-07 (The prince bound to his father's joy), SB2-PIA-01 (The father who visits his imprisoned son), SB2-PIA-03 (The last moment before exile), SB2-PIA-14 (The prince who asks for shoes), SB2-PIA-17 (The captive prince who feels the king near), SB2-RBE-10 (The gem ground to save the prince)
- **The father who hides, steps back or walks on:** SB2-BST-20 (A small child learning to walk), SB2-MAG-03 (Father shows himself and walks on), SB2-RBE-03 (The father hides from his little son), SB2-RSB-06 (Dancers who step apart), SB2-MHS-06 (The child on his father's shoulders)
- **The father (teacher) who narrows himself for the child:** SB2-MAG-01 (Father lowers his mind for his child), SB2-MAG-02 (The child plays with the father's beard), SB2-MAG-10 (The funnel), SB2-RSB-18 (The interpreter in between), SB2-RBE-08 (The teacher-student parable does not fit), SB2-PIA-07 (The child learning the alphabet)
- **The father's love and delight in the son:** SB2-MAG-04 (The father's picture of his son), SB2-MAG-05 (The father whose son refutes him), SB2-MAG-22 (The lost traveler and the father's joy in the road), SB2-BST-13 (The guest who tests the son), SB2-BST-22 (The son who praises without measure), SB2-RSB-08 (The son who earns on his own), SB2-RYZ-10 (The father who guides his son)
- **Sun, ray, glass and colored vessels:** SB2-TZ-01 (Water takes the color of the glass), SB2-TZ-02 (The sun that melts and hardens), SB2-TZ-06 (The ray of the sun), SB2-TZ-20 (Light through a pane of glass), SB2-RSB-03 (A gem that shines), SB2-RSB-38 (Light through windows of many colors), SB2-RYZ-01 (A candle at noon), SB2-RYZ-15 (A house with no windows), SB2-RBE-17 (Light through a window and through a screen)
- **Name, flint and coal: what was hidden before:** SB2-TZ-04 (A person's name), SB2-TZ-05 (Flame bound in a coal, fire in a flint), SB2-MHS-03 (A name is only for others), SB2-RSB-14 (The king is not his kingship)
- **Speech, letters and the speaking soul:** SB2-MAG-15 (The king's will reaches us through speech), SB2-MAG-17 (The maker's power stays in the made), SB2-TZ-16 (One letter and the speaking soul), SB2-TZ-21 (One idea split into many words), SB2-RSB-04 (Letters joined in a word), SB2-RSB-10 (Thought passing through the finger)
- **Seed, drop and the 'nothing' in between:** SB2-MAG-11 (Egg and chicken: the moment between), SB2-MAG-12 (The seed must rot), SB2-TZ-09 (The seed-drop holds the whole child), SB2-RSB-05 (The seed has to rot first)
- **Water: springs, dams, rivers, fish:** SB2-TZ-15 (The barrel that overflows), SB2-TZ-17 (Water held back by a board), SB2-TZ-18 (Fish in the sea), SB2-TZ-19 (Groundwater purified through the earth), SB2-TZ-28 (The spring that never stops), SB2-MHS-10 (The dry river dug deeper), SB2-RSB-26 (The river overflowing its banks), SB2-RSB-37 (Water dripping on stone), SB2-RYZ-11 (A river fed by springs), SB2-PIA-05 (Clean water in a dirty flask)
- **Fire, lamp, wick and spark:** SB2-BST-04 (Keep a spark in the coals), SB2-BST-23 (The smith who never saw the spark), SB2-RSB-20 (A wick that won't hold the flame), SB2-RSB-21 (Ash: what remains after the fire), SB2-RYZ-03 (The lamp: oil, wick and flame), SB2-RYZ-13 (A spark rising into the torch), SB2-PIA-11 (A burning lamp: oil and wick become one flame), SB2-PIA-12 (Holding the candle versus straining to see), SB2-PIA-13 (The one who sees fire and the blind man who touches it)
- **Standing before the king (awe, bittul, speechlessness):** SB2-MAG-20 (A minister who stands always before the king), SB2-MAG-21 (The king's shining face), SB2-TZ-11 (Before a king, a small slip is a rebellion), SB2-TZ-13 (A great king lodging with a pauper), SB2-MHS-12 (Bowing very close to the king), SB2-RSB-07 (Too close to speak), SB2-RSB-24 (The commoner who sees the ministers bow), SB2-RYZ-17 (The condemned man who meets the king)
- **The king close at hand (road, field, palace):** SB2-BST-01 (Walls that are only an illusion), SB2-BST-27 (The king in disguise at war), SB2-MAG-08 (The king easier to reach on the road), SB2-RBE-02 (The king in the field), SB2-PIA-15 (The king who removes his garments)
- **A dwelling for the King:** SB2-MHS-05 (A home where the man himself lives), SB2-RBE-01 (Living in a friend's house), SB2-RYZ-04 (Cleaning the house for the king), SB2-PIA-09 (The enemy hiding in the palace)
- **Building and the plan in the first thought:** SB2-MAG-16 (The king building a house), SB2-MAG-09 (The tailor cutting the cloth), SB2-MAG-18 (Lifting the mountain in pieces), SB2-RSB-32 (Praising the axe instead of the builder), SB2-RSB-31 (The craftsman who loves the work)
- **Tools, levers, stones and ropes:** SB2-TZ-03 (The axe in the hewer's hand), SB2-TZ-12 (The weight on the scale), SB2-RSB-11 (The stone thrown upward), SB2-RSB-13 (The lever lifts from below), SB2-RSB-30 (The rope tied above), SB2-RSB-34 (A thick rope of 613 threads)
- **Hidden treasure and the praise that falls short:** SB2-TZ-10 (Pearls in a tied bundle), SB2-MHS-09 (Treasure locked in a chest), SB2-MHS-11 (Praising a millionaire for a silver coin), SB2-RSB-23 (Admitting your friend is right)
- **The world shows its Maker:** SB2-RSB-02 (The strong man and the stone), SB2-TZ-26 (The burning palace), SB2-RBE-13 (The child in the factory), SB2-RSB-16 (The world is the parable itself), SB2-MHS-01 (The map and the land), SB2-MHS-02 (Everything below is a mashal for above)
- **The mashal about the mashal:** SB2-BST-30 (The fox who forgot his 300 fables), SB2-MAG-24 (The mashal is a vessel for the idea), SB2-TZ-22 (A mashal versus a riddle), SB2-MHS-04 (The mashal is higher than the idea), SB2-RYZ-06 (The root of the mashal is higher), SB2-RBE-07 (Three parables: the torch, the barrel, the seed), SB2-RBE-08 (The teacher-student parable does not fit), SB2-RSB-35 (Sea water that covers is not like nature)

## Baal Shem Tov (30)

#### SB2-BST-01. Walls that are only an illusion *Domain:* king and kingdom; palace

- **Mashal.** A wise king built walls, towers and gates around himself, all by illusion, and scattered treasure at every gate. Some people stopped at the first gate, took the money and went home. His son pushed on, wanting only his father, and found that no wall stood between them: it was all illusion.
- **Nimshal.** G-d hides behind many garments and screens, yet He fills all the world; every barrier is made from Him, so nothing truly separates a person from Him.
- **Parts.** the king → G-d; illusory walls and gates → the screens, worlds and inner obstacles; treasure at each gate → the gifts and lesser goals along the way; the son → the soul that wants Him alone; seeing through the walls → knowing that every barrier is His own garment.
- **Breaks** [ours]. Ours: in the parable the walls are pure illusion; in the nimshal the screens are made 'from His very self' and really work as screens for us until we see through them. And a person still has to walk; knowing it is illusion does not let you skip the gates.
- **Principles.** PR-L04, PR-L01, PR-L09
- **Source.** Keter Shem Tov, `Chassidus-txt/Baal Shem Tov (R. Yisrael ben Eliezer) (1698-1760)/Keter Shem Tov (Medzhibozh, Ukraine, c. 1740-1760).txt` line 56: «שהיה מלך א' חכם גדול ועשה באחיזת ענים חומות ומגדלים ושערים» (there was a very wise king who made, by illusion, walls, towers and gates).
- **Recurs.** Maggid (tradition); Degel Machaneh Ephraim; Kedushas Levi (shofar); Piaseczner, Mevo HaShe'arim (line 200) cites it as the key to tzimtzum; Maharash, Toras Shmuel lists 'the Baal Shem Tov's parable for shofar' (Likkutei Sichos index line 19348).
- **See also in SB2.** SB2-BST-27, SB2-MAG-08, SB2-RBE-02, SB2-PIA-15.
- **Guide.** What feels like a wall between you and the deepest thing you love may be only a painted wall. Keep walking toward what you actually want, and the wall turns out to be nothing.

#### SB2-BST-02. Two who wanted to know the king *Domain:* king and kingdom; knowledge

- **Mashal.** Two men wanted to know the king. One went through every room of the palace, enjoyed its treasures, and in the end still could not know the king. The other said: since I can't know him anyway, I won't go in at all.
- **Nimshal.** There are two kinds of 'not knowing' G-d: the lazy kind that never searches, and the kind reached at the end of searching. Only the second is worth anything.
- **Parts.** the king → G-d's essence; the palace rooms and treasures → the levels of understanding one can reach; the one who entered → the person who studies and searches; the one who stayed outside → the person who refuses to look.
- **Breaks** [ours]. Ours: in the parable both end without knowing the king; it shows the value of the search, not that the search ever arrives.
- **Principles.** PR-L12, PR-L06, PR-L11
- **Source.** Keter Shem Tov, `Chassidus-txt/Baal Shem Tov (R. Yisrael ben Eliezer) (1698-1760)/Keter Shem Tov (Medzhibozh, Ukraine, c. 1740-1760).txt` line 1: «מלה"ד שנים שרוצים לידע את המלך וא' נכנס בכל חדרי המלך ונהנה מאוצרי והיכלי המלך ואח"כ לא יוכל לידע המלך» (it is like two who wanted to know the king; one entered all the king's rooms and enjoyed his treasuries and palaces, and afterward still could not know the king).
- **Recurs.** R. Aharon's preface: 'the whole end of knowing is that we do not know' (תכלית הידיעה אשר לא נדע); Bechinas Olam; the Rebbe Rashab (Samach Vav) on 'knowing by negation'.
- **Guide.** There is an 'I don't know' you say before you start, and an 'I don't know' you say after a long search. They are the same words, and they are not the same at all.

#### SB2-BST-03. The wise man's request *Domain:* king and kingdom; speech

- **Mashal.** On his day of joy, a king promised to grant anything anyone asked. Some asked for honor, some for wealth, and each got it. One wise man asked that the king himself speak with him three times a day. The king was very pleased, because the man valued his speech more than his riches.
- **Nimshal.** Prayer three times a day is the request to be spoken with by G-d Himself, and the one who asks for that receives the riches too.
- **Parts.** the king's day of joy → the open hour of prayer; those asking for honor and wealth → prayer only for needs; the wise man → the one who wants closeness itself; three conversations a day → the three daily prayers.
- **Breaks** [ours]. Ours: in the parable the king could refuse; the stated point is about what to want, not a promise of reward.
- **Principles.** PR-L04, PR-L01
- **Source.** Keter Shem Tov, `Chassidus-txt/Baal Shem Tov (R. Yisrael ben Eliezer) (1698-1760)/Keter Shem Tov (Medzhibozh, Ukraine, c. 1740-1760).txt` line 109: «שאמר ששאלתו ומבוקשו שידבר המלך בעצמו עמו ג"פ ביום» (who said that his request was that the king himself speak with him three times a day).
- **Recurs.** KST line 64 (same parable); Kedushas Levi; the Rebbe (sichos) on asking for the Giver, not the gift.
- **Guide.** You can ask for things, or you can ask for the one who gives them. People who ask for the second usually find they had asked for more.

#### SB2-BST-04. Keep a spark in the coals *Domain:* fire

- **Mashal.** A candle or coals that still have a spark can be blown back into flame. If not even a spark is left, you have to bring fire all over again.
- **Nimshal.** All day long a person should keep at least a little attachment to G-d, so that the next prayer can catch from it instead of starting cold.
- **Parts.** the coals → the person during the ordinary day; the spark → a small, steady awareness of G-d; blowing it into flame → the next prayer or study; bringing new fire → starting from nothing each time.
- **Breaks** [ours]. Ours: a spark keeps itself only by burning its fuel; a person must choose to keep the awareness.
- **Principles.** PR-L04, PR-L09
- **Source.** Keter Shem Tov, `Chassidus-txt/Baal Shem Tov (R. Yisrael ben Eliezer) (1698-1760)/Keter Shem Tov (Medzhibozh, Ukraine, c. 1740-1760).txt` line 87: «מלה"ד לנר או גחלים שאם יש בהם עדיין ניצוץ יוכל להבעיר» (it is like a candle or coals: if a spark is still in them, one can kindle it).
- **Recurs.** Tanya ch. 'the fire on the altar' (Alter Rebbe, Lev. 6:6 'fire always'); the Rebbe Rashab, Kuntres HaTefillah on keeping the after-glow of prayer.
- **See also in SB2.** SB2-BST-23, SB2-RSB-20, SB2-RSB-21, SB2-RYZ-03, SB2-RYZ-13, SB2-PIA-11, SB2-PIA-12, SB2-PIA-13.
- **Guide.** Keep one small warm thing going in you all day. When you come back to it later, you won't have to start a fire from scratch.

#### SB2-BST-05. The rebel who was promoted *Domain:* king and kingdom; repentance

- **Mashal.** A villager rebelled against the king, even struck his statue. The king made him a ruler and kept raising him until he became second to the king. The more good the king did and the more of the king's greatness he saw, the more it hurt him that he had rebelled.
- **Nimshal.** G-d's goodness to one who sinned is His 'revenge': kindness makes the regret deeper than any punishment could.
- **Parts.** the villager → the sinner; striking the statue → the sin; being raised step by step → G-d's continuing goodness; the growing pain → teshuvah from love.
- **Breaks** [ours]. Ours: in the parable the king acts by strategy; G-d's goodness is not a trick to shame us.
- **Principles.** PR-L04, PR-L07
- **Source.** Keter Shem Tov, `Chassidus-txt/Baal Shem Tov (R. Yisrael ben Eliezer) (1698-1760)/Keter Shem Tov (Medzhibozh, Ukraine, c. 1740-1760).txt` line 120: «ע"פ משל לאיש כפר א' שמרד במלך שהכה ורגם איקונין של מלך» (by a parable of a villager who rebelled against the king, who struck and stoned the king's statue).
- **Recurs.** Maharash and the Rebbe on teshuvah from love; the Rebbe Rashab, Ayin Beis on the baal teshuvah.
- **Guide.** Sometimes the hardest thing to bear after you have done wrong is that people keep being good to you. Let that sting. It is pulling you home.

#### SB2-BST-06. The woman fleeing her labor pains *Domain:* body; birth

- **Mashal.** A woman in labor went to another place to escape the pains, and the pains came with her.
- **Nimshal.** You cannot run from distress by changing place. The way out is to call to G-d from inside the narrow place.
- **Parts.** the woman → the person in trouble; the pains → the distress; moving away → trying to escape outwardly; birth → the 'wide place' that comes through prayer.
- **Breaks** [ours]. Ours: labor pains end in a birth by nature; the parable does not promise that every pain is a birth.
- **Principles.** PR-L04, PR-L09
- **Source.** Keter Shem Tov, `Chassidus-txt/Baal Shem Tov (R. Yisrael ben Eliezer) (1698-1760)/Keter Shem Tov (Medzhibozh, Ukraine, c. 1740-1760).txt` line 121: «משל לאשה יולדת שהלכה למקום אחר לפטור מחבלי לידה והצער הולך אחריה» (like a woman giving birth who went to another place to be free of the pangs, and the pain went after her).
- **Recurs.** the Piaseczner, Esh Kodesh, on prayer from within suffering.
- **Guide.** Wherever you go, you take the hurt with you. So stop running and talk from where you are; that is often where it starts to open.

#### SB2-BST-07. The servant sent to act as a rebel *Domain:* king and kingdom; war

- **Mashal.** A great king sent one of his servants to the provinces pretending to be a rebel, to test them. Some fought him and lost, some made peace with him. In one province the wise people sensed that this was the king's own will, and they did not take him seriously as an enemy.
- **Nimshal.** The evil inclination is a servant of G-d playing a rebel. The wise see that its pull is a test sent by the King and stand firm.
- **Parts.** the king → G-d; the servant playing rebel → the evil inclination; provinces that fight or surrender → people who struggle or give in; the wise province → the one who sees the test for what it is.
- **Breaks** [ours]. Ours: the servant only pretends; inner temptation feels fully real while it lasts.
- **Principles.** PR-L04, PR-L07
- **Source.** Keter Shem Tov, `Chassidus-txt/Baal Shem Tov (R. Yisrael ben Eliezer) (1698-1760)/Keter Shem Tov (Medzhibozh, Ukraine, c. 1740-1760).txt` line 131: «ושלח א' מעבדיו שינסה המדינות כאלו הוא עבד מורד באדונו» (and he sent one of his servants to test the provinces as if he were a servant rebelling against his master).
- **Recurs.** Zohar (the harlot sent by the king to test the prince), Tanya ch. 9 and 29; Keter Shem Tov line 151.
- **Guide.** The voice that pulls you off course is not as independent as it sounds. It was sent to see if you'd hold. Knowing that takes half its strength.

#### SB2-BST-08. Seeing your own face in a mirror *Domain:* nature; perception

- **Mashal.** A person looking into a mirror sees his own faults. In the same way, when you see a fault in someone else, it shows you that a trace of it is in you.
- **Nimshal.** Everything you are shown is shown for you. Another's fault is a mirror for your own repair.
- **Parts.** the mirror → the other person; the face seen → one's own trait; noticing → being shown it from above.
- **Breaks** [ours]. Ours: a mirror shows exactly what is there; what we see in others is only a hint, 'a trace', not proof.
- **Principles.** PR-L04, PR-L09
- **Source.** Keter Shem Tov, `Chassidus-txt/Baal Shem Tov (R. Yisrael ben Eliezer) (1698-1760)/Keter Shem Tov (Medzhibozh, Ukraine, c. 1740-1760).txt` line 132: «ע"פ משל המסתכל במראה יודע חסרונו» (by the parable: one who looks in a mirror knows his flaw).
- **Recurs.** Maggid, Maggid Devarav LeYaakov (line 226, 'like one who sees his own face in a mirror'); the Rebbe, Likkutei Sichos (line 17158).
- **Guide.** When something in another person bothers you a lot, ask quietly what it is showing you about yourself. You don't have to say it out loud.

#### SB2-BST-09. Four ministers who fled with the treasure *Domain:* king and kingdom; repentance

- **Mashal.** A king put four ministers over his treasury, and they took it and fled. One thought it over and came back on his own. The second came back after a wise man spoke to his heart. The third came back from fear after seeing a trial. The fourth never came back. The one who returned on his own was raised highest.
- **Nimshal.** Return to G-d has levels: from one's own understanding, from being taught, from fear of punishment; the highest is the return a person reaches by himself.
- **Parts.** the treasury → the soul and its powers entrusted to us; fleeing → sin; the four returns → kinds of teshuvah; greater honor → the higher level of self-made return.
- **Breaks** [ours]. Ours: in the parable the king ranks them by how they came back; in teshuvah any return is received.
- **Principles.** PR-L04, PR-L05
- **Source.** Keter Shem Tov, `Chassidus-txt/Baal Shem Tov (R. Yisrael ben Eliezer) (1698-1760)/Keter Shem Tov (Medzhibozh, Ukraine, c. 1740-1760).txt` line 133: «משל למלך שהיה ממנה על אוצרו ד' שרים ונטלו האוצר וברחו» (like a king who appointed four ministers over his treasury, and they took the treasury and fled).
- **Recurs.** Keter Shem Tov line 323 (same, 'from my teacher'); Toldos Yaakov Yosef.
- **Guide.** There are many ways to come back, and every one counts. The one you reach by thinking it through yourself goes deepest.

#### SB2-BST-10. Lost merchants and the guide *Domain:* commerce; travel

- **Mashal.** Merchants lost their way and lay down to sleep, until a man came to show them the road. One guide led them toward wild animals and robbers; another led them straight.
- **Nimshal.** The letters of the Torah, through which the world was made, came down into this world like lost travelers. One who studies for its own sake leads them back to their root; one who studies for himself leads them astray.
- **Parts.** the merchants → the letters of Torah; sleeping lost → letters spoken without heart; the guide → the one who learns; the straight road → learning for its own sake.
- **Breaks** [ours]. Ours: the parable makes the letters passive; the stated teaching gives them a root that pulls them home.
- **Principles.** PR-L04, PR-L03
- **Source.** Keter Shem Tov, `Chassidus-txt/Baal Shem Tov (R. Yisrael ben Eliezer) (1698-1760)/Keter Shem Tov (Medzhibozh, Ukraine, c. 1740-1760).txt` line 155: «משל שפעם א' תעו סוחרים מן הדרך ונחו שם לישן» (a parable: once merchants lost their way and lay down there to sleep).
- **Recurs.** Maggid on raising letters to their root; Tanya ch. 'Torah lishmah'.
- **Guide.** The words you read and say are travelers looking for their way home. How you say them decides where they go.

#### SB2-BST-11. The minister who dressed like the prince *Domain:* king and kingdom; teacher and student

- **Mashal.** A king sent his beloved son far away so that later he would have more joy. The son forgot all the king's pleasures and would not come home. The king sent great ministers, and none helped, until one wise minister changed his clothes and language to be like the son, came close to him at his own level, and brought him back.
- **Nimshal.** A teacher who wants to lift someone must come down to his level, dress as he is dressed and speak his language.
- **Parts.** the king → G-d; the far-off son → the soul that forgot its source; the ministers who failed → teaching from above; the wise minister in disguise → the tzaddik who comes down to the person's level.
- **Breaks** [ours]. Ours: the minister only seems to be like the son; a real teacher must actually feel the student's place.
- **Principles.** PR-L04, PR-L03, PR-L15
- **Source.** Keter Shem Tov, `Chassidus-txt/Baal Shem Tov (R. Yisrael ben Eliezer) (1698-1760)/Keter Shem Tov (Medzhibozh, Ukraine, c. 1740-1760).txt` line 162: «שהיה שם שר א' חכם שכסות לשון שינה כדמות הבן ההוא ונתקרב אליו במדריגתו» (a wise minister who changed his clothing and language to be like that son and came close to him at his level).
- **Recurs.** Maggid (line 61, prince dressed as a villager); Toldos Yaakov Yosef; the Rebbe (Lubavitch outreach).
- **See also in SB2.** SB2-BST-18, SB2-BST-24, SB2-MAG-06, SB2-MAG-07, SB2-PIA-01, SB2-PIA-03, SB2-PIA-14, SB2-PIA-17, SB2-RBE-10.
- **Guide.** To help someone, first go and stand where they are standing, in their words. Then walk back together.

#### SB2-BST-12. The drunk and the sober traveler *Domain:* travel; war

- **Mashal.** Two men passed through a forest of robbers, one drunk and one sober. Both were beaten and robbed. Later, asked about the road, the drunk said, 'All quiet, no danger' and could not explain his wounds. The sober one warned everyone to go armed.
- **Nimshal.** The tzaddik knows the battle with the evil inclination and can warn others; the one drunk on the world's pleasure feels nothing and tells everyone there is no danger.
- **Parts.** the forest → this world; the robbers → the evil inclination's attacks; the drunk → one who lives in pleasure; the sober man → the one who serves G-d awake.
- **Breaks** [ours]. Ours: both were hurt alike in the parable; in life the sober person is often hurt less because he is ready.
- **Principles.** PR-L04
- **Source.** Keter Shem Tov, `Chassidus-txt/Baal Shem Tov (R. Yisrael ben Eliezer) (1698-1760)/Keter Shem Tov (Medzhibozh, Ukraine, c. 1740-1760).txt` line 171: «ונזדמן שהלכו שנים א' היה שכור וא' היה בדעת מיושבת» (and it happened that two went, one drunk and one clear-minded).
- **Recurs.** Tanya ch. 'awake vs. asleep'; the Rayatz on the soul hearing the call.
- **Guide.** The person who feels the struggle is not worse off than the one who feels nothing. He is just awake, and he can tell you where the road is dangerous.

#### SB2-BST-13. The guest who tests the son *Domain:* father and son; teacher and student

- **Mashal.** A beloved son is tested by a guest with a hard question he cannot solve. The father cannot bear his son's struggle, so he quietly opens a door for him and shows him the way.
- **Nimshal.** When a person is stuck in serving G-d, G-d Himself opens a small opening so he can win.
- **Parts.** the father → G-d; the son → the soul; the guest's question → the test or difficulty; the opened door → help from above.
- **Breaks** [ours]. Ours: the father helps by a hint, not by answering for him; the work still belongs to the son.
- **Principles.** PR-L04, PR-L09
- **Source.** Tzava'at HaRivash, `Chassidus-txt/Baal Shem Tov (R. Yisrael ben Eliezer) (1698-1760)/Tzava'at HaRivash (Medzhibozh and Mezritch, c. 1740-1770).txt` line 290: «משל לבן חביב אצל אביו שבא אורח אחד לתהות את הבן בקנקנו» (like a son beloved to his father, when a guest came to test the son's worth).
- **Recurs.** Keter Shem Tov line 198 (the father's delight when the son is not defeated).
- **See also in SB2.** SB2-MAG-04, SB2-MAG-05, SB2-MAG-22, SB2-BST-22, SB2-RSB-08, SB2-RYZ-10.
- **Guide.** When you are stuck, watch for the small opening that shows up. Someone who loves you may have put it there.

#### SB2-BST-14. The cure for pride *Domain:* king and kingdom; body

- **Mashal.** A king wanted a cure to live forever and was told to keep far from pride. The humbler he acted, the prouder he felt of his humility, until his teacher taught him to act kingly outside and stay low inside, by showing him the toilet: what comes out of a person.
- **Nimshal.** Humility cannot be put on from outside; it must be inner. Remembering what one is made of keeps the heart low.
- **Parts.** the king → the person with gifts; humble acts → outward modesty; growing pride → pride in one's own humility; the teacher's lesson → inner lowliness, outer dignity.
- **Breaks** [ours]. Ours: the parable uses shame of the body; the stated aim is truth about oneself, not self-disgust.
- **Principles.** PR-L04, PR-L09
- **Source.** Keter Shem Tov, `Chassidus-txt/Baal Shem Tov (R. Yisrael ben Eliezer) (1698-1760)/Keter Shem Tov (Medzhibozh, Ukraine, c. 1740-1760).txt` line 209: «משל מלך ביקש רפואה שיחיה לעולם ונתנו לו רפואה להרחיק מגאוה» (a parable: a king sought a cure to live forever, and they gave him the cure of keeping far from pride).
- **Recurs.** Keter Shem Tov line 396 (false humility); Tanya ch. 'lowliness'.
- **Guide.** Don't try to look humble. Be honest about what you are made of, and humility will come by itself.

#### SB2-BST-15. The gem lost from the ring *Domain:* king and kingdom; father and son

- **Mashal.** A king lost a precious stone from his ring. Many servants and ministers stood around him, but he would not order them to search; he told only his only, beloved son to find it and return it to his father.
- **Nimshal.** G-d gives the work of finding what is lost (the scattered sparks, the hidden good) to Israel, His son, so that the son will have a share in it.
- **Parts.** the king → G-d; the lost stone → the holy sparks or hidden good in the world; the servants → angels and powers; the only son → the Jewish soul.
- **Breaks** [ours]. Ours: the king could have found it himself; the parable shows love, not need.
- **Principles.** PR-L04, PR-L06
- **Source.** Keter Shem Tov, `Chassidus-txt/Baal Shem Tov (R. Yisrael ben Eliezer) (1698-1760)/Keter Shem Tov (Medzhibozh, Ukraine, c. 1740-1760).txt` line 223: «והמשל למלך שנאבדה לו אבן יקרה מתוך טבעתו» (and the parable is of a king who lost a precious stone from his ring).
- **Recurs.** Maggid (raising sparks); the Rebbe Rashab on the work of birurim.
- **Guide.** The thing you were asked to find, maybe nobody else was asked. That is not a burden; it is trust.

#### SB2-BST-16. The angry messenger and the loving messenger *Domain:* king and kingdom; emotion

- **Mashal.** The king sends a soldier in a rage to summon a man. You shouldn't fear the messenger; go straight to the king and make peace. Sometimes the king sends a messenger with love; the fool plays with the messenger, and the wise man says: why play with the messenger? I'll go to the root.
- **Nimshal.** Every outer fear and outer love that comes to a person is sent to wake fear and love of G-d. Don't stay with the messenger; go to the One who sent it.
- **Parts.** the angry soldier → a frightening thing; the loving messenger → a pleasant attraction; going to the king → turning the feeling to G-d; playing with the messenger → staying with the object.
- **Breaks** [ours]. Ours: messengers in the parable are separate people; the stated teaching says the fear and love themselves are a fallen spark of His.
- **Principles.** PR-L04, PR-L01
- **Source.** Keter Shem Tov, `Chassidus-txt/Baal Shem Tov (R. Yisrael ben Eliezer) (1698-1760)/Keter Shem Tov (Medzhibozh, Ukraine, c. 1740-1760).txt` line 243: «מלה"ד לאיש חיל שלוח מהמלך לקרוא לאדם והוא בכעס גדול ובפחד» (it is like a soldier sent by the king to summon a man, in great anger and fear).
- **Recurs.** Maggid Devarav LeYaakov line 227 (same); Tzava'at HaRivash (fear from a fallen spark); Tanya ch. 'love and fear'.
- **Guide.** When something scares you or pulls at you, ask who sent it. Then skip the messenger and go to the sender.

#### SB2-BST-17. The prince's house of sticks *Domain:* father and son; play

- **Mashal.** A little prince built himself a small house of sticks. Someone knocked it down, and he ran crying to his father. The father laughed and did not rush to punish, because he was planning to build the boy a great palace.
- **Nimshal.** G-d does not hurry to avenge the small structures we lose, because He is preparing the great Temple of the future.
- **Parts.** the little prince → Israel; the stick house → what we build and lose now; the father's laugh → G-d's patience; the palace → the future redemption.
- **Breaks** [ours]. Ours: the child's pain is real and the father knows it; the parable does not say our losses do not matter.
- **Principles.** PR-L04, PR-L07
- **Source.** Keter Shem Tov, `Chassidus-txt/Baal Shem Tov (R. Yisrael ben Eliezer) (1698-1760)/Keter Shem Tov (Medzhibozh, Ukraine, c. 1740-1760).txt` line 253: «מלה"ד לבן המלך שהוא קטן ועשה לעצמו בית קטן מקיסמין» (it is like a little prince who made himself a small house of sticks).
- **Recurs.** the Rebbe on exile and the coming redemption.
- **Guide.** Sometimes something small breaks and it feels huge. It may be that something much bigger is being built.

#### SB2-BST-18. The father counting money *Domain:* father and son; captivity

- **Mashal.** A man was counting money while his son sat in captivity. The son came and said: you have money right there, redeem me!
- **Nimshal.** When a stray thought comes in prayer, it is a holy spark asking to be raised: 'You are attached to G-d right now; lift me up too.'
- **Parts.** the father counting → the person in prayer; the money → the power of prayer; the captive son → the spark inside the stray thought; redeeming → lifting the thought to its root.
- **Breaks** [ours]. Ours: the stray thought does not literally speak; the parable gives a voice to a hidden pull.
- **Principles.** PR-L04, PR-L09
- **Source.** Keter Shem Tov, `Chassidus-txt/Baal Shem Tov (R. Yisrael ben Eliezer) (1698-1760)/Keter Shem Tov (Medzhibozh, Ukraine, c. 1740-1760).txt` line 264: «והוא משל האדם שהיה מונה מעות והיה בנו בשבי'» (and it is a parable of a man counting money while his son was in captivity).
- **Recurs.** Tzava'at HaRivash on 'foreign thoughts'; the Alter Rebbe limits this practice (Tanya ch. 28).
- **See also in SB2.** SB2-BST-11, SB2-BST-24, SB2-MAG-06, SB2-MAG-07, SB2-PIA-01, SB2-PIA-03, SB2-PIA-14, SB2-PIA-17, SB2-RBE-10.
- **Guide.** A distracting thought in a quiet moment might not be an enemy. It may be a part of you asking to come along.

#### SB2-BST-19. The poor man and the minister *Domain:* king and kingdom; joy

- **Mashal.** A poor man begs the king with great weeping and gets only a little. A minister arranges a great celebration with praise of the king, and in the middle asks for his need, and the king gives him a large gift.
- **Nimshal.** Prayer in joy and praise is more accepted than prayer in sadness and tears.
- **Parts.** the poor man's weeping → sad prayer; the minister's celebration → joyful prayer; the large gift → what joy draws down.
- **Breaks** [ours]. Ours: the parable does not reject tears; it ranks joy above sadness as the main mood.
- **Principles.** PR-L04, PR-L01
- **Source.** Tzava'at HaRivash, `Chassidus-txt/Baal Shem Tov (R. Yisrael ben Eliezer) (1698-1760)/Tzava'at HaRivash (Medzhibozh and Mezritch, c. 1740-1770).txt` line 220: «כשעני שואל ומבקש ומתחנן לפני המלך בבכי' גדולה אעפ"כ אין נותנין לו אלא דבר מה» (when a poor man asks and begs before the king with great weeping, still they give him only a little).
- **Recurs.** Keter Shem Tov line 271 (same); the Piaseczner, Bnei Machshava Tova on prayer.
- **Guide.** You can ask from a heavy heart, and that's allowed. But try asking from a glad one: it opens more.

#### SB2-BST-20. A small child learning to walk *Domain:* father and son; body

- **Mashal.** A father teaching his little son to walk steps back from him, so the child will come closer.
- **Nimshal.** Sometimes G-d seems to move away from the righteous, so that they will draw closer.
- **Parts.** the father → G-d; stepping back → felt distance or dryness; the child's steps → effort in serving G-d.
- **Breaks** [ours]. Ours: the father's retreat is visible play; a person in dryness cannot see the father waiting.
- **Principles.** PR-L04, PR-L09
- **Source.** Keter Shem Tov, `Chassidus-txt/Baal Shem Tov (R. Yisrael ben Eliezer) (1698-1760)/Keter Shem Tov (Medzhibozh, Ukraine, c. 1740-1760).txt` line 279: «מלה"ד לבן קטן שאביו מלמדו לילך» (it is like a little son whose father teaches him to walk).
- **Recurs.** Maggid (line 183, father who shows himself and walks on); the Rebbe Rashab, Samach Vav (father who hides his face); the Rebbe, Melukat line 421.
- **See also in SB2.** SB2-MAG-03, SB2-RBE-03, SB2-RSB-06, SB2-MHS-06.
- **Guide.** When the closeness you used to feel seems to step back, it may be making room for you to take your own steps toward it.

#### SB2-BST-21. Every lock has a key *Domain:* craft; house

- **Mashal.** Every lock has a key cut to fit it. But there are thieves who open without a key: they break the lock.
- **Nimshal.** Every hidden matter has its 'key', its right intention. But the main key is to be like the thief who breaks everything: to break the heart in great humility, and then the screen above breaks too.
- **Parts.** the lock → the closed gate above; the fitted key → the right meditation (kavanah); breaking the lock → a broken, humble heart.
- **Breaks** [ours]. Ours: the parable praises a thief; the 'theft' here is honest surrender, not trickery.
- **Principles.** PR-L04, PR-L09
- **Source.** Keter Shem Tov, `Chassidus-txt/Baal Shem Tov (R. Yisrael ben Eliezer) (1698-1760)/Keter Shem Tov (Medzhibozh, Ukraine, c. 1740-1760).txt` line 290: «שיש לכל מסגר מפתח שפותח בכיוון ולפי המסגר כן מכוין המפתח» (every lock has a key that opens it exactly; the key is fitted to the lock).
- **Recurs.** the Baal Shem Tov's parable of the keys for shofar (Kedushas Levi; cited by the Rebbe, Likkutei Sichos); Rebbe Rashab on the 'broken heart'.
- **Guide.** You may not know the exact words that open the door. A heart that honestly breaks opens it anyway.

#### SB2-BST-22. The son who praises without measure *Domain:* king and kingdom; father and son

- **Mashal.** Ministers praise the king in measured times, each by his rank, and when the king is angry they are afraid to praise at all. The king's son praises his father without limit, because he is his father, and because he was given permission no minister has.
- **Nimshal.** Israel praise G-d as His children, without fear and without measure, and even thank Him for being allowed to.
- **Parts.** the ministers → the angels; measured praise → praise by rank; the king's anger → times of judgment; the son's endless praise → a Jew's praise as a child of G-d.
- **Breaks** [ours]. Ours: the parable needs an angry king; the stated nimshal uses it only to show the son is never afraid.
- **Principles.** PR-L04
- **Source.** Tzava'at HaRivash, `Chassidus-txt/Baal Shem Tov (R. Yisrael ben Eliezer) (1698-1760)/Tzava'at HaRivash (Medzhibozh and Mezritch, c. 1740-1770).txt` line 274: «שהבן קולס בלי שיעור כי הנה יש חיוב על הבן לקלס את אביו עד אין קץ» (that the son praises without measure, for the son is obliged to praise his father without end).
- **Recurs.** Keter Shem Tov line 293 (same); Rosh Hashanah liturgy.
- **See also in SB2.** SB2-MAG-04, SB2-MAG-05, SB2-MAG-22, SB2-BST-13, SB2-RSB-08, SB2-RYZ-10.
- **Guide.** You don't need the right title or the right words to say thank you. A child can say it anytime.

#### SB2-BST-23. The smith who never saw the spark *Domain:* craft; fire

- **Mashal.** A man learned the blacksmith's trade but never saw how you first put in a spark to light the fire. He went to work for the king, failed, was thrown out, and had to go back to his first teacher to learn the main thing.
- **Nimshal.** Torah and service are the gold; the spark that lights them is longing and fire for G-d. Without that spark the rest does not work.
- **Parts.** the trade → Torah study and mitzvos; the spark → warmth and longing in the heart; the king's house → real service of G-d; going back to the teacher → returning to the root of feeling.
- **Breaks** [ours]. Ours: a smith can buy fire elsewhere; the inner spark cannot be borrowed.
- **Principles.** PR-L04, PR-L09
- **Source.** Keter Shem Tov, `Chassidus-txt/Baal Shem Tov (R. Yisrael ben Eliezer) (1698-1760)/Keter Shem Tov (Medzhibozh, Ukraine, c. 1740-1760).txt` line 357: «א' שלמד מלאכה נפחין ולא ראה איך משימין תחלה ניצוץ אש להבעיר» (one who learned the smith's trade and did not see how one first puts in a spark of fire to kindle).
- **Recurs.** the Rebbe Rashab, Kuntres HaAvodah on dry service.
- **See also in SB2.** SB2-BST-04, SB2-RSB-20, SB2-RSB-21, SB2-RYZ-03, SB2-RYZ-13, SB2-PIA-11, SB2-PIA-12, SB2-PIA-13.
- **Guide.** You can know all the steps and still have no fire. Go back and find the first spark: what you actually long for.

#### SB2-BST-24. The prince who gets a letter in the village *Domain:* king and kingdom; joy

- **Mashal.** A prince living among villagers gets a letter of peace from his father and wants to celebrate, but he would be ashamed to dance alone, so he calls the villagers and gives them wine. They rejoice in their way, and he rejoices in his father.
- **Nimshal.** When the soul rejoices with G-d, it lets the body rejoice too, by food and drink, so the body joins the joy in its own way.
- **Parts.** the prince → the soul; the villagers → the body and its senses; the letter → closeness to G-d (Shabbos, festival); the wine → physical pleasures used for joy.
- **Breaks** [ours]. Ours: the villagers do not know why they rejoice; the body's joy can feel like the main thing if one forgets the letter.
- **Principles.** PR-L04, PR-L09
- **Source.** Keter Shem Tov, `Chassidus-txt/Baal Shem Tov (R. Yisrael ben Eliezer) (1698-1760)/Keter Shem Tov (Medzhibozh, Ukraine, c. 1740-1760).txt` line 481: «משל לבן מלך שהיה בין אנשי הכפרים ובא לו אגרת שלומים מאביו» (like a prince among villagers who received a letter of peace from his father).
- **Recurs.** Keter Shem Tov line 119 (same image); Tanya ch. 'joy of the soul'.
- **See also in SB2.** SB2-BST-11, SB2-BST-18, SB2-MAG-06, SB2-MAG-07, SB2-PIA-01, SB2-PIA-03, SB2-PIA-14, SB2-PIA-17, SB2-RBE-10.
- **Guide.** When something good happens inside, let your body celebrate too. A good meal can share in a joy it doesn't understand.

#### SB2-BST-25. The lion cubs and the picture of Samson *Domain:* nature; animals

- **Mashal.** A lion told his cubs they were the mightiest creatures. Exploring, they found a ruined palace with a painting of Samson tearing a lion apart, and ran home in fright. Their father said: on the contrary, this shows how strong you are; it happened once in history, so they paint it as a wonder.
- **Nimshal.** When Scripture praises something as remarkable, it shows that the opposite is the usual way. A rare thing is recorded because it is rare.
- **Parts.** the cubs → the reader of Torah; the painting → a story told as a wonder; the father's answer → the rule: the exception proves the rule.
- **Breaks** [ours]. Ours: this is a parable about reading, not about G-d; it teaches method, not the divine.
- **Principles.** PR-L04, PR-L03
- **Source.** Keter Shem Tov, `Chassidus-txt/Baal Shem Tov (R. Yisrael ben Eliezer) (1698-1760)/Keter Shem Tov (Medzhibozh, Ukraine, c. 1740-1760).txt` line 502: «ע"פ משל שהארי צוה ואמר לגוריו אריות קטנים בנים שלו» (by a parable: the lion commanded and said to his cubs, little lions, his sons).
- **Recurs.** (a reading method, not a metaphysical mashal).
- **Guide.** When something is held up as amazing, ask what that tells you about how things usually are.

#### SB2-BST-26. The poor woman and her one egg *Domain:* commerce; home

- **Mashal.** A poor woman had one egg and was overjoyed, planning: the egg becomes a chick, the chick lays eggs, then a cow, then wealth. In the middle of her joy the egg fell and broke, and she was left with nothing.
- **Nimshal.** One who does not know that he has fallen, and thinks there is nothing above him, loses even what he has; one who knows tries to rise.
- **Parts.** the egg → one's small spiritual level; the dreams → imagined greatness; the broken egg → the fall that comes from self-satisfaction.
- **Breaks** [ours]. Ours: planning is not bad; the stated fault is not knowing one's real place.
- **Principles.** PR-L04
- **Source.** Keter Shem Tov, `Chassidus-txt/Baal Shem Tov (R. Yisrael ben Eliezer) (1698-1760)/Keter Shem Tov (Medzhibozh, Ukraine, c. 1740-1760).txt` line 508: «לאשה עניה אחת שהיה לה ביצה אחת ושמחה בה שמחה גדולה» (of a poor woman who had one egg and rejoiced in it greatly).
- **Recurs.** a folk tale used morally.
- **Guide.** Enjoy what you have, but hold it carefully. Big dreams about a small thing can make you drop it.

#### SB2-BST-27. The king in disguise at war *Domain:* king and kingdom; war

- **Mashal.** When a king goes to war he changes his clothes. Those close to him know him by his movements. Those not close see where the guard is thickest and know the king must be there.
- **Nimshal.** When a person cannot pray with fire, and feels heavily blocked, the very weight of the block shows that the King is right there, hidden.
- **Parts.** the disguised king → G-d hidden in a hard moment; the heavy guard → the obstacles to prayer; those who know his movements → the deeply attached; those who reason from the guard → ordinary people.
- **Breaks** [ours]. Ours: guards in war are visible signs; inner resistance can also just be tiredness.
- **Principles.** PR-L04, PR-L09
- **Source.** Tzava'at HaRivash, `Chassidus-txt/Baal Shem Tov (R. Yisrael ben Eliezer) (1698-1760)/Tzava'at HaRivash (Medzhibozh and Mezritch, c. 1740-1770).txt` line 158: «במשל המלך כשבא למלחמה משנה את בגדיו» (as in the parable of the king who changes his clothes when he goes to war).
- **Recurs.** Tzava'at HaRivash line 129 (same); Maggid; the Rebbe Rashab on hiddenness.
- **See also in SB2.** SB2-BST-01, SB2-MAG-08, SB2-RBE-02, SB2-PIA-15.
- **Guide.** When it is hardest to feel anything, that heaviness may be guarding something important. Stay near it.

#### SB2-BST-28. Ice on the river *Domain:* nature; water

- **Mashal.** If ice was once thick, then even after it thins it can still hold a person crossing the river. If we see thin, weak ice, it shows it was never thick.
- **Nimshal.** A person who once had a strong inner state keeps its strength even when it weakens; true strength leaves its mark.
- **Parts.** the ice → one's inner firmness; thick ice → a deep past state; thin ice still holding → the trace that remains.
- **Breaks** [ours]. Ours: nature is a rough guide here; ice can crack anyway.
- **Principles.** PR-L04
- **Source.** Tzava'at HaRivash, `Chassidus-txt/Baal Shem Tov (R. Yisrael ben Eliezer) (1698-1760)/Tzava'at HaRivash (Medzhibozh and Mezritch, c. 1740-1770).txt` line 233: «משל לכפור אם יש לו גליד גדול ואח"כ הוא קטן אפ"ה יכול הנהר לעמוד בכפור» (like frost: if it had thick ice and afterward it is small, still the river can bear it).
- **Recurs.** (none found).
- **Guide.** What you built deeply in the past still holds you, even when it feels thin now.

#### SB2-BST-29. The broom *Domain:* home; tools

- **Mashal.** A broom is made to clean the house; it is good, though a low kind of good. When a child misbehaves and someone hits him with the broom, the broom becomes fully bad.
- **Nimshal.** Even the lowest things are good in their place; sin is what turns them into real evil.
- **Parts.** the broom → the low or physical things; cleaning → their proper use; hitting the child → misuse through sin.
- **Breaks** [ours]. Ours: a broom has no choice; a person's tools become bad only through a person.
- **Principles.** PR-L04
- **Source.** Tzava'at HaRivash, `Chassidus-txt/Baal Shem Tov (R. Yisrael ben Eliezer) (1698-1760)/Tzava'at HaRivash (Medzhibozh and Mezritch, c. 1740-1770).txt` line 265: «המכבד את הבית שעשוי לפנות את הבית והוא טוב קצת אבל הוא במדריגה תחתונה» (the broom that is made to clear the house; it is a little good, but at a low level).
- **Recurs.** Maggid Devarav LeYaakov (similar).
- **Guide.** Nothing low is bad in itself. What you do with it decides.

#### SB2-BST-30. The fox who forgot his 300 fables *Domain:* animals; mashal itself

- **Mashal.** The animals' king was angry, and the fox said, 'I'll appease him; I have three hundred fables.' On the way he forgot them all, and said: each of us will appease the king as he can.
- **Nimshal.** On the Days of Awe, don't lean on the great prayer leaders; each person must pray for himself.
- **Parts.** the lion-king → G-d on Rosh Hashanah; the fox's fables → the clever prayers of others; forgetting them → finding them useless; each appeasing by his own strength → personal prayer.
- **Breaks** [ours]. Ours: the midrash's fox is a trickster; the Baal Shem Tov uses only the moment he is left with himself.
- **Principles.** PR-L05, PR-L03
- **Source.** Keter Shem Tov, `Chassidus-txt/Baal Shem Tov (R. Yisrael ben Eliezer) (1698-1760)/Keter Shem Tov (Medzhibozh, Ukraine, c. 1740-1760).txt` line 37: «אמר השועל אני אלך שיש לי ג' מאות משלים» (the fox said, I will go, for I have three hundred fables).
- **Recurs.** R. Aharon's preface (R. Meir's 300 fox fables and R. Yochanan's three, as levels of mashal); Genesis Rabbah 78.
- **See also in SB2.** SB2-MAG-24, SB2-TZ-22, SB2-MHS-04, SB2-RYZ-06, SB2-RBE-07, SB2-RBE-08, SB2-RSB-35.
- **Guide.** Clever words you borrowed may leave you at the door. Bring what is yours, even if it is small.

## Maggid of Mezritch (24)

#### SB2-MAG-01. Father lowers his mind for his child *Domain:* father and son; teacher and student

- **Mashal.** A father who loves his small son does not talk to him with his great, wide mind, which the child could not take in. Out of love he narrows his mind and speaks and plays at the child's level, and he delights in it.
- **Nimshal.** G-d 'contracts' Himself so that the worlds and souls can bear Him; the contraction (tzimtzum) is done out of love and for the delight He has in us.
- **Parts.** the father's great mind → G-d's infinite light; narrowing it → tzimtzum; childish words and games → the worlds and the Torah's garments; the father's delight → His pleasure in our service.
- **Breaks** [stated + ours]. Stated elsewhere (Tzemach Tzedek, DM line 111): a father's narrowing creates nothing new, while G-d's contraction brings beings into existence. Ours: the child knows he is small; we usually don't feel the narrowing at all.
- **Principles.** PR-L04, PR-L07, PR-L09, PR-L15
- **Source.** Maggid Devarav LeYaakov, `Chassidus-txt/R. Dov Ber, Maggid of Mezritch (c.1704-1772)/Maggid Devarav leYaakov (Mezritch, Volhynia, 1760-1780).txt` line 264: «משל לאב שיש לו בן קטן ואהוב מאוד והנה כשרוצה האב להשתעשע עם בנו הקטן» (like a father who has a small, much-loved son; when the father wants to play with his little son).
- **Recurs.** MDL lines 170, 193, 216 (same); the Rebbe Rashab, Kuntres U'Maayan (line 499); the Rebbe, Melukat (line 2454); the Tzemach Tzedek, DM line 111 (with its break).
- **See also in SB2.** SB2-MAG-02, SB2-MAG-10, SB2-RSB-18, SB2-RBE-08, SB2-PIA-07.
- **Guide.** Love makes big people small on purpose. If the world feels like a smaller version of something vast, maybe it was made small so that you could hold it.

#### SB2-MAG-02. The child plays with the father's beard *Domain:* father and son; body

- **Mashal.** A father whose little son cannot climb onto his arm lifts him up, and once held, the child plays with his father's beard.
- **Nimshal.** G-d first lifts a person beyond his own strength, and then, held close, the person can 'play' with the higher, hidden flows (the 'beard', the Thirteen Attributes).
- **Parts.** the father lifting → help from above; the child too small to climb → a person who cannot reach by himself; playing with the beard → closeness to the higher attributes of mercy.
- **Breaks** [ours]. Ours: in the parable the child plays without understanding; the nimshal says the closeness comes first and understanding later.
- **Principles.** PR-L04, PR-L09
- **Source.** Maggid Devarav LeYaakov, `Chassidus-txt/R. Dov Ber, Maggid of Mezritch (c.1704-1772)/Maggid Devarav leYaakov (Mezritch, Volhynia, 1760-1780).txt` line 56: «ע"ד משל לאב שאין בנו קטן יכול לעלות על ידו מגביה אותו» (like a father whose small son cannot climb onto his arm; he lifts him).
- **Recurs.** the Rebbe, Melukat line 2980 (cites the Maggid's Or Torah, 'plays with his beard').
- **See also in SB2.** SB2-MAG-01, SB2-MAG-10, SB2-RSB-18, SB2-RBE-08, SB2-PIA-07.
- **Guide.** Sometimes you are lifted before you could climb. Don't analyze it; just enjoy being held.

#### SB2-MAG-03. Father shows himself and walks on *Domain:* father and son; play

- **Mashal.** A father sees his son playing with small children. He shows himself, and the son drops the games and runs after him, calling 'Father!' The father then deliberately walks on, and the son calls louder and runs faster.
- **Nimshal.** 'Draw me after You, we will run': G-d shows Himself and then hides, so that our longing and running grow.
- **Parts.** the father appearing → a moment of revelation; walking on → G-d's hiding afterwards; the son's louder cry → stronger longing.
- **Breaks** [ours]. Ours: the son can still see the father's back; a person in a time of hiding may see nothing.
- **Principles.** PR-L04, PR-L09
- **Source.** Maggid Devarav LeYaakov, `Chassidus-txt/R. Dov Ber, Maggid of Mezritch (c.1704-1772)/Maggid Devarav leYaakov (Mezritch, Volhynia, 1760-1780).txt` line 183: «משל אב כשרואה את בנו משתעשע עם ילדים קטנים בקטנות והולך האב ומראה א"ע לפי בנו» (a parable: when a father sees his son playing with little children, the father goes and shows himself to his son).
- **Recurs.** the Rebbe Rashab, Samach Vav (father who hides his face, line 7276); the Rebbe, Melukat line 421; Keter Shem Tov line 279.
- **See also in SB2.** SB2-BST-20, SB2-RBE-03, SB2-RSB-06, SB2-MHS-06.
- **Guide.** If you once felt something real and now it seems to have walked off, follow it. The walking away may be an invitation.

#### SB2-MAG-04. The father's picture of his son *Domain:* father and son; thought

- **Mashal.** A father who loves his son carries the son's image engraved in his mind; when the son is small he pictures him small, when grown, grown.
- **Nimshal.** 'Israel arose in G-d's thought': the souls are engraved in His mind, and He sees them as they are now.
- **Parts.** the father's mind → G-d's thought; the son's image → the Jewish soul; the picture growing → the soul's state now.
- **Breaks** [ours]. Ours: a father's picture can be out of date; the nimshal says G-d's is always current.
- **Principles.** PR-L04, PR-L09
- **Source.** Maggid Devarav LeYaakov, `Chassidus-txt/R. Dov Ber, Maggid of Mezritch (c.1704-1772)/Maggid Devarav leYaakov (Mezritch, Volhynia, 1760-1780).txt` line 233: «נחקקה להאב צורת הבן כמו שהיה עומד לפניו» (the son's form is engraved in the father as he stood before him).
- **Recurs.** the Rebbe Rashab, Samach Vav (line 7264); the Rebbe, Melukat lines 67, 299, 439, 986, 2297; Likkutei Sichos line 1112.
- **See also in SB2.** SB2-MAG-05, SB2-MAG-22, SB2-BST-13, SB2-BST-22, SB2-RSB-08, SB2-RYZ-10.
- **Guide.** Someone who loves you carries a picture of you, even when you are not in the room. You are held in a mind like that.

#### SB2-MAG-05. The father whose son refutes him *Domain:* father and son; learning

- **Mashal.** A father says a Torah thought in front of his son, and the son, being sharp, refutes it and says it another way. Though the son opposes him, the father is delighted.
- **Nimshal.** G-d's deepest will is the delight He gets when the righteous 'overrule' Him by their Torah and service.
- **Parts.** the father's teaching → G-d's decree or law; the son's refutation → the tzaddik's novel Torah or prayer; the father's joy → divine pleasure.
- **Breaks** [ours]. Ours: in the parable the son might be wrong; the stated point is the father's pleasure, not the son's correctness.
- **Principles.** PR-L04, PR-L07
- **Source.** Maggid Devarav LeYaakov, `Chassidus-txt/R. Dov Ber, Maggid of Mezritch (c.1704-1772)/Maggid Devarav leYaakov (Mezritch, Volhynia, 1760-1780).txt` line 252: «משל בזה אב שאומר בפני בנו איזה דבר הלכה או איזה חידוש בתורה» (a parable for this: a father who says a matter of halacha or a Torah insight before his son).
- **Recurs.** Talmud ('My children have defeated Me'); Keter Shem Tov line 198.
- **See also in SB2.** SB2-MAG-04, SB2-MAG-22, SB2-BST-13, SB2-BST-22, SB2-RSB-08, SB2-RYZ-10.
- **Guide.** Real love isn't threatened when you push back. Sometimes it is pleased most when you do.

#### SB2-MAG-06. The captive prince *Domain:* king and kingdom; captivity

- **Mashal.** A prince fell into captivity. When he is brought back before the king, the king delights in him more than in the son who was always at home.
- **Nimshal.** When a person raises what had fallen (when the 'sacks', the husks, drop away), G-d has more pleasure than from what was always holy.
- **Parts.** the captive prince → the fallen spark or the returning soul; captivity → exile in the material world or in sin; return → raising it; the king's greater joy → the higher pleasure from return.
- **Breaks** [ours]. Ours: the son at home did nothing wrong; the parable does not lower him, only shows the return's special joy.
- **Principles.** PR-L04
- **Source.** Maggid Devarav LeYaakov, `Chassidus-txt/R. Dov Ber, Maggid of Mezritch (c.1704-1772)/Maggid Devarav leYaakov (Mezritch, Volhynia, 1760-1780).txt` line 44: «כמשל הבן מלך שנפל לשביה כשמביאין אותו לפני המלך הוא נהנה מאוד» (like the prince who fell into captivity: when they bring him before the king, he greatly delights).
- **Recurs.** Keter Shem Tov line 358 (same); the Rebbe, Melukat lines 404, 2765; the Piaseczner, Esh Kodesh line 62.
- **See also in SB2.** SB2-BST-11, SB2-BST-18, SB2-BST-24, SB2-MAG-07, SB2-PIA-01, SB2-PIA-03, SB2-PIA-14, SB2-PIA-17, SB2-RBE-10.
- **Guide.** Coming back after being lost is not second best. For the one waiting, it can be the best day.

#### SB2-MAG-07. The prince bound to his father's joy *Domain:* king and kingdom; thought

- **Mashal.** A prince was captured by a reckless, drunken servant. To keep his mind bound to his father, so that he would stay in the king's heart, he constantly attached himself to the pleasure his father takes in ruling justly.
- **Nimshal.** In exile, a person can stay bound to G-d by attaching his thought to the delight G-d takes in His own way, even while surrounded by coarseness.
- **Parts.** the captor → the body and its desires; the prince's thought → the soul's attention; the king's pleasure in justice → G-d's delight in His ways; staying remembered → the bond kept alive.
- **Breaks** [ours]. Ours: the captor in the parable is outside the prince; the 'captor' in us is our own body.
- **Principles.** PR-L04, PR-L09
- **Source.** Maggid Devarav LeYaakov, `Chassidus-txt/R. Dov Ber, Maggid of Mezritch (c.1704-1772)/Maggid Devarav leYaakov (Mezritch, Volhynia, 1760-1780).txt` line 112: «משל לבן מלך שנשבה ליד א' מהעבדים פוחז א' ואוהב הוללת ושכרות» (like a prince captured by one of the servants, a reckless one who loved revelry and drunkenness).
- **Recurs.** the Piaseczner, Esh Kodesh line 62 (captive prince feels the king near).
- **See also in SB2.** SB2-BST-11, SB2-BST-18, SB2-BST-24, SB2-MAG-06, SB2-PIA-01, SB2-PIA-03, SB2-PIA-14, SB2-PIA-17, SB2-RBE-10.
- **Guide.** Even when you're stuck somewhere you don't want to be, you can keep your mind on what the one you love enjoys. That keeps you connected.

#### SB2-MAG-08. The king easier to reach on the road *Domain:* king and kingdom; travel

- **Mashal.** In his palace the king is hard to approach. On the road, at an inn, anyone may come before him, even a villager unworthy of the palace.
- **Nimshal.** In exile it is easier to reach holy spirit than in Temple times: whoever thinks of attachment to G-d, He dwells with him.
- **Parts.** the palace → the Temple era; the inn on the road → exile; the villager → the ordinary person today; speaking to the king → closeness in thought.
- **Breaks** [ours]. Ours: the king on the road is still the king; the parable does not lower Him, it lowers the barriers.
- **Principles.** PR-L04
- **Source.** Maggid Devarav LeYaakov, `Chassidus-txt/R. Dov Ber, Maggid of Mezritch (c.1704-1772)/Maggid Devarav leYaakov (Mezritch, Volhynia, 1760-1780).txt` line 69: «כמשל המלך כשהוא בבית מלכותו אי אפשר להתקרב אליו כל כך» (like the king: when he is in his royal house one cannot approach him so much).
- **Recurs.** Keter Shem Tov line 391 (same); the Alter Rebbe's 'king in the field' (Likkutei Torah, Elul), cited by the Rebbe (Melukat line 2970).
- **See also in SB2.** SB2-BST-01, SB2-BST-27, SB2-RBE-02, SB2-PIA-15.
- **Guide.** You may think closeness belongs to special places and times. Sometimes it's easier when everything is ordinary and on the move.

#### SB2-MAG-09. The tailor cutting the cloth *Domain:* craft

- **Mashal.** A tailor takes a whole piece of cloth and cuts it into small, thin pieces. Someone who is not a tailor says he ruined it; someone who understands sees this piece is for a sleeve, that one for something else, and it all has to be cut this way.
- **Nimshal.** G-d 'broke' the whole into the many (the breaking of the vessels) so that His light could be known in the details; what looks like damage is wise making.
- **Parts.** the whole cloth → the One before creation; cutting → the breaking and the many worlds; the onlooker who sees ruin → the unwise view of the world; the garment → the purpose that the pieces serve.
- **Breaks** [ours]. Ours: a tailor's cloth stays cloth; the nimshal speaks of light hidden in what looks like waste.
- **Principles.** PR-L04, PR-L03
- **Source.** Maggid Devarav LeYaakov, `Chassidus-txt/R. Dov Ber, Maggid of Mezritch (c.1704-1772)/Maggid Devarav leYaakov (Mezritch, Volhynia, 1760-1780).txt` line 29: «משל בר"מ לחייט שלקח חתיכה שלימה וחותך לחתיכות קטנות ודקות» (a parable in the Raaya Mehemna of a tailor who took a whole piece and cut it into small, thin pieces).
- **Recurs.** Zohar, Raaya Mehemna; the Rebbe Rashab on shevirah.
- **See also in SB2.** SB2-MAG-16, SB2-MAG-18, SB2-RSB-32, SB2-RSB-31.
- **Guide.** Something cut into pieces may not be ruined. It may be on its way to becoming something that fits.

#### SB2-MAG-10. The funnel *Domain:* craft; water

- **Mashal.** When you pour from one vessel into another and fear spilling, you use a funnel. The liquid narrows and goes in without loss.
- **Nimshal.** A teacher narrows his broad thought into words and letters so the student can receive it; so G-d narrows His light into letters and attributes.
- **Parts.** the liquid → the teacher's insight; the funnel → letters and words; the small vessel → the student's mind.
- **Breaks** [ours]. Ours: a funnel changes nothing in the liquid; words do shape the thought. (The text adds that the more limited the student, the narrower the teacher must make it.)
- **Principles.** PR-L04, PR-L07, PR-L15, PR-L14
- **Source.** Maggid Devarav LeYaakov, `Chassidus-txt/R. Dov Ber, Maggid of Mezritch (c.1704-1772)/Maggid Devarav leYaakov (Mezritch, Volhynia, 1760-1780).txt` line 144: «כשאדם רוצה להריק מכלי אל כלי ומתיירא שמא ישפוך לחוץ אזי נותן כלי הנק' משפך» (when a person wants to pour from vessel to vessel and fears he will spill outside, he uses a vessel called a funnel).
- **Recurs.** MDL 145 (teacher and student); the Piaseczner, Chovat HaTalmidim (funnel image, line 339, with a break).
- **See also in SB2.** SB2-MAG-01, SB2-MAG-02, SB2-RSB-18, SB2-RBE-08, SB2-PIA-07.
- **Guide.** Big things have to be narrowed to reach you. The narrowing is not loss; it is care.

#### SB2-MAG-11. Egg and chicken: the moment between *Domain:* nature; growth

- **Mashal.** A chicken comes from an egg, and there is a moment when it is neither egg nor chicken. No one can pin down that moment.
- **Nimshal.** Between one level and the next (thinker and thought, thought and speech) is a point of 'nothing' (ayin) that joins them and cannot be grasped.
- **Parts.** the egg → the earlier state; the chicken → the new state; the in-between moment → ayin, the hidden link.
- **Breaks** [ours]. Ours: the in-between moment is still physical; the ayin above is not a stage in time.
- **Principles.** PR-L04, PR-L07
- **Source.** Maggid Devarav LeYaakov, `Chassidus-txt/R. Dov Ber, Maggid of Mezritch (c.1704-1772)/Maggid Devarav leYaakov (Mezritch, Volhynia, 1760-1780).txt` line 82: «כמשל מביצה נתהווה תרנגול ויש שעה שאינו לא ביצה ולא תרנגל» (like a chicken coming from an egg: there is a time when it is neither egg nor chicken).
- **Recurs.** the Rebbe Rashab, Samach Vav ('ayin in the middle', the seed, line 2683).
- **See also in SB2.** SB2-MAG-12, SB2-TZ-09, SB2-RSB-05.
- **Guide.** Every real change passes through a moment when you are neither what you were nor what you will be. Don't rush that moment.

#### SB2-MAG-12. The seed must rot *Domain:* nature; plants

- **Mashal.** To make one grain of wheat into many, you bring it to its root, the soil's power of growth; it sprouts only after rain softens it and it loses its form and becomes 'nothing'.
- **Nimshal.** A thing changes only when it is brought back to its root and becomes nothing; the self that lets go becomes the root of much more.
- **Parts.** the grain → a person or trait; the soil → the root (wisdom, ayin); rotting → self-nullification; many grains → growth beyond oneself.
- **Breaks** [ours]. Ours: the grain has no choice; a person must agree to let go.
- **Principles.** PR-L04, PR-L09
- **Source.** Maggid Devarav LeYaakov, `Chassidus-txt/R. Dov Ber, Maggid of Mezritch (c.1704-1772)/Maggid Devarav leYaakov (Mezritch, Volhynia, 1760-1780).txt` line 115: «למשל החטה שרוצים לשנותה לעשות ממנה כמה חטים מביאים אותה לשרשה» (for example, wheat which one wishes to change, to make many grains of it, is brought to its root).
- **Recurs.** MDL line 173; the Rebbe Rashab, Samach Vav line 2683 and 7230; Rayatz, Sefer HaMaamarim line 1522.
- **See also in SB2.** SB2-MAG-11, SB2-TZ-09, SB2-RSB-05.
- **Guide.** To grow into more than you are, you may have to stop holding on to your shape for a while.

#### SB2-MAG-13. The bathtub and the hidden images *Domain:* water; craft

- **Mashal.** A bathtub is full of water, and two fine images are carved at the bottom. While it's full you can't see them; when the water is let out, the images appear.
- **Nimshal.** The divine 'faces' (partzufim) became visible only when the flood of light was drawn out and contained in vessels: 'And the heavens were finished.'
- **Parts.** the water → the unbounded light; the images → the ordered structures (partzufim); letting out the water → the containing that makes form visible.
- **Breaks** [ours]. Ours: in the parable the images were there all along; the nimshal speaks of form coming into being.
- **Principles.** PR-L04
- **Source.** Maggid Devarav LeYaakov, `Chassidus-txt/R. Dov Ber, Maggid of Mezritch (c.1704-1772)/Maggid Devarav leYaakov (Mezritch, Volhynia, 1760-1780).txt` line 178: «משל לאמבטי מלאה מים והיה בה ב' איסקרסי' נאים» (a parable of a bathtub full of water, and in it two fine images).
- **Recurs.** Midrash (Genesis Rabbah); MDL 181.
- **Guide.** Sometimes you can only see the shape of a thing after some of the flood has drained away.

#### SB2-MAG-14. The craftsman paid for labor *Domain:* commerce; craft

- **Mashal.** A householder pays a craftsman only for his effort, not for the full worth of the work. A king pays each minister by his rank.
- **Nimshal.** 'Kindness is Yours, for You pay each by his deeds': G-d's reward is pure kindness, beyond what the work is worth.
- **Parts.** the craftsman → the person serving G-d; payment for labor → reward; the real worth → what the deed does above.
- **Breaks** [ours]. Ours: a craftsman deserves his wage; the nimshal says G-d owes nothing, yet gives.
- **Principles.** PR-L04, PR-L07
- **Source.** Maggid Devarav LeYaakov, `Chassidus-txt/R. Dov Ber, Maggid of Mezritch (c.1704-1772)/Maggid Devarav leYaakov (Mezritch, Volhynia, 1760-1780).txt` line 254: «יובן ע"פ משל לאומן העושה מלאכה אצל בעה"ב» (it will be understood by a parable of a craftsman who works for a householder).
- **Recurs.** Keter Shem Tov line 217 (servant and master).
- **Guide.** What comes back to you for your efforts is a gift, not a paycheck. That makes it easier to be grateful.

#### SB2-MAG-15. The king's will reaches us through speech *Domain:* king and kingdom; speech

- **Mashal.** All the king's servants want to do his will, but while it is only in his will or thought, or even a sound coming out of his mouth, they cannot know what he wants. Only when he speaks in words is his command known.
- **Nimshal.** Speech is called 'kingship' (malchus): through it the hidden thought becomes known and can be done.
- **Parts.** the king's will → G-d's will; the servants → creations and souls; spoken words → divine speech, malchus.
- **Breaks** [ours]. Ours: a king's words are separate from him once spoken; divine speech remains united with Him.
- **Principles.** PR-L09, PR-L04, PR-L07
- **Source.** Maggid Devarav LeYaakov, `Chassidus-txt/R. Dov Ber, Maggid of Mezritch (c.1704-1772)/Maggid Devarav leYaakov (Mezritch, Volhynia, 1760-1780).txt` line 267: «משל למלך שהכל עבדיו ורוצים לקבל עול מלכותו ולעבוד עבודתו» (like a king whose servants all want to accept his rule and do his work).
- **Recurs.** Tanya, Shaar HaYichud (Alter Rebbe); the Rayatz on speech and kingship.
- **See also in SB2.** SB2-MAG-17, SB2-TZ-16, SB2-TZ-21, SB2-RSB-04, SB2-RSB-10.
- **Guide.** Even the people who love you can't help until you put what you want into words. Saying it is how it enters the world.

#### SB2-MAG-16. The king building a house *Domain:* king and kingdom; craft

- **Mashal.** A king wants to build a house. At first the will is completely closed, without detail. Then in thought it opens into the whole plan: length, width, rooms, doors, windows. Then he prepares wood and stones one by one until it is built.
- **Nimshal.** 'All was made in wisdom': creation goes from hidden will, to the overall plan in wisdom, to the many details, and the end was in the first thought.
- **Parts.** closed will → keser; the overall plan → chochmah; details and materials → the lower attributes and worlds; the finished house → the world, the 'dwelling'.
- **Breaks** [ours]. Ours: a builder needs materials that already exist; G-d makes them too.
- **Principles.** PR-L04, PR-L09, PR-L07
- **Source.** Maggid Devarav LeYaakov, `Chassidus-txt/R. Dov Ber, Maggid of Mezritch (c.1704-1772)/Maggid Devarav leYaakov (Mezritch, Volhynia, 1760-1780).txt` line 277: «נמשיל משל נאה למלך שעלה ברצונו לבנות לו בית» (we will give a fine parable: a king who wished to build himself a house).
- **Recurs.** MDL lines 77, 116, 263 ('the end of the deed was first in thought'); the Rebbe Rashab, Samach Vav line 7380, Ayin Beis line 472; Rayatz line 861.
- **See also in SB2.** SB2-MAG-09, SB2-MAG-18, SB2-RSB-32, SB2-RSB-31.
- **Guide.** Everything you build starts as a wish you can't yet describe. The finished thing was in that first wish.

#### SB2-MAG-17. The maker's power stays in the made *Domain:* craft; speech

- **Mashal.** When a wise man says or makes something wise, his power is in the thing he made or said; and he can still say and make much more.
- **Nimshal.** The Torah is G-d's wisdom; His power is in it, and that power is truly without end, so the Torah, though it seems bounded, is one with the Infinite.
- **Parts.** the wise maker → G-d; the made thing → the Torah; the maker's power in it → G-d's infinity in the Torah.
- **Breaks** [ours]. Ours: a craftsman's power leaves the thing when he leaves; G-d's power never leaves.
- **Principles.** PR-L04, PR-L09
- **Source.** Maggid Devarav LeYaakov, `Chassidus-txt/R. Dov Ber, Maggid of Mezritch (c.1704-1772)/Maggid Devarav leYaakov (Mezritch, Volhynia, 1760-1780).txt` line 81: «למשל אדם מדבר דבר חכמה או עושה דבר חכמה נמצא כח הפעל הוא בהכלי שעשה» (for example, a person says or does something wise; the maker's power is in the vessel he made).
- **Recurs.** Tanya ch. 20 (Alter Rebbe: 'the power of the maker in the made').
- **See also in SB2.** SB2-MAG-15, SB2-TZ-16, SB2-TZ-21, SB2-RSB-04, SB2-RSB-10.
- **Guide.** Something carefully made still carries its maker. Look at the thing in front of you and feel who is still in it.

#### SB2-MAG-18. Lifting the mountain in pieces *Domain:* king and kingdom; labor

- **Mashal.** A king ordered his servants to lift a huge mountain, which is impossible. They decided to dig it, break it and crumble it into small pieces; each lifted a little by his strength, and they did the king's word.
- **Nimshal.** G-d commands us to lift the holy sparks; the breaking of the vessels into small pieces was so that each person could lift his share.
- **Parts.** the mountain → the whole fallen world; breaking it → the shattering of the vessels; each lifting a little → each soul's portion of birurim.
- **Breaks** [ours]. Ours: the mountain is dead weight; sparks want to rise.
- **Principles.** PR-L04, PR-L03
- **Source.** Maggid Devarav LeYaakov, `Chassidus-txt/R. Dov Ber, Maggid of Mezritch (c.1704-1772)/Maggid Devarav leYaakov (Mezritch, Volhynia, 1760-1780).txt` line 242: «משל המלך צוה לעבדיו להגביה הר א' גדול מאוד» (a parable: the king commanded his servants to lift a very great mountain).
- **Recurs.** the Rebbe Rashab, Samach Vav on birurim; Zechariah 4:7.
- **See also in SB2.** SB2-MAG-16, SB2-MAG-09, SB2-RSB-32, SB2-RSB-31.
- **Guide.** The whole job is too big for anyone. It was broken into pieces so you could carry yours.

#### SB2-MAG-19. Before the shofar: the chosen nation praises *Domain:* king and kingdom; music

- **Mashal.** A great king settled seventy nations and chose one to praise him on his birthday. They praised all day, then sat sad, afraid their words hadn't reached him, and said, 'let's wake our elders, who know how to glorify him.'
- **Nimshal.** Rosh Hashanah is the King's birthday; Israel pray and then send the shofar-blower to wake the Patriarchs to carry the prayers up.
- **Parts.** the king's birthday → Rosh Hashanah; the chosen nation → Israel; the elders → the Patriarchs; waking them → the shofar.
- **Breaks** [ours]. Ours: the parable has the king far away; the stated teaching makes the shofar a call from the people to their own roots.
- **Principles.** PR-L04
- **Source.** Maggid Devarav LeYaakov, `Chassidus-txt/R. Dov Ber, Maggid of Mezritch (c.1704-1772)/Maggid Devarav leYaakov (Mezritch, Volhynia, 1760-1780).txt` line 59: «משל לפני תקיעות למלך גדול מפואר הושיב מדינה של ע' אומות» (a parable before the blowing: a great and glorious king settled a land of seventy nations).
- **Recurs.** Keter Shem Tov (shofar parables); the Rebbe, Likkutei Sichos index 19152-19348.
- **Guide.** When your words feel too small, call on what is older and deeper in you, and let it speak.

#### SB2-MAG-20. A minister who stands always before the king *Domain:* king and kingdom; pleasure

- **Mashal.** A minister always standing before the king is so overcome with awe that he doesn't feel himself or the great pleasure; one who is not always there, coming home, feels it more and thinks how close he is to royalty.
- **Nimshal.** The one closest to G-d, in deep humility, does not feel his own delight; feeling one's closeness is a sign of distance.
- **Parts.** the minister always near → the deeply bittul person; the occasional visitor → the one who feels his own spirituality; feeling pleasure → self-awareness in closeness.
- **Breaks** [ours]. Ours: the visitor's pleasure isn't bad; the parable ranks the two.
- **Principles.** PR-L04, PR-L09
- **Source.** Maggid Devarav LeYaakov, `Chassidus-txt/R. Dov Ber, Maggid of Mezritch (c.1704-1772)/Maggid Devarav leYaakov (Mezritch, Volhynia, 1760-1780).txt` line 238: «כמשל השר העומד לפני המלך תמיד מגודל הבושה אינו מרגיש א"ע» (like the minister who always stands before the king: from great shame he does not feel himself).
- **Recurs.** MDL line 28 (sitting before the king in shame); the Rebbe Rashab, Samach Vav line 4477.
- **See also in SB2.** SB2-MAG-21, SB2-TZ-11, SB2-TZ-13, SB2-MHS-12, SB2-RSB-07, SB2-RSB-24, SB2-RYZ-17.
- **Guide.** The closer you get to something great, the less you think about how close you are.

#### SB2-MAG-21. The king's shining face *Domain:* king and kingdom; joy

- **Mashal.** When the king's face is shining and he is glad and good-hearted, mercy rules; even one condemned to death who comes before him then is pardoned.
- **Nimshal.** When joy above is revealed, judgments are 'sweetened'; joy below draws the shining face.
- **Parts.** the king's joy → revealed delight above; the condemned man → the person with judgments; pardon → sweetening of judgment.
- **Breaks** [ours]. Ours: a king's mood changes; the nimshal is not that G-d changes, but that His light is revealed differently.
- **Principles.** PR-L04, PR-L08
- **Source.** Maggid Devarav LeYaakov, `Chassidus-txt/R. Dov Ber, Maggid of Mezritch (c.1704-1772)/Maggid Devarav leYaakov (Mezritch, Volhynia, 1760-1780).txt` line 204: «למשל כאשר המלך נהירין אנפהא ושמח וטוב לב» (for example, when the king's face shines and he is joyful and good-hearted).
- **Recurs.** MDL line 87; Rayatz line 692 (the condemned man who meets the king); Maharash line 1834.
- **See also in SB2.** SB2-MAG-20, SB2-TZ-11, SB2-TZ-13, SB2-MHS-12, SB2-RSB-07, SB2-RSB-24, SB2-RYZ-17.
- **Guide.** Joy changes the air in a room. When it is there, things that seemed unforgivable can soften.

#### SB2-MAG-22. The lost traveler and the father's joy in the road *Domain:* father and son; travel

- **Mashal.** A man lost his way and took another road thinking it was right; later he knew he was lost, searched, found the right road and reached his goal. The father, seeing his son on the right road, delights in the road itself, more than if the son had never strayed.
- **Nimshal.** Through real teshuvah a person reaches G-d's own delight 'in the road': sins are sweetened at their root.
- **Parts.** the lost road → sin; realizing and searching → teshuvah; the father's joy in the road → G-d's delight from return.
- **Breaks** [stated + ours]. Ours: while lost, the son felt no lack; only the father did. The nimshal turns on this: we can feel fine while far.
- **Principles.** PR-L04
- **Source.** Maggid Devarav LeYaakov, `Chassidus-txt/R. Dov Ber, Maggid of Mezritch (c.1704-1772)/Maggid Devarav leYaakov (Mezritch, Volhynia, 1760-1780).txt` line 166: «הנה נקדים משל: א' הלך לדרך ונאבד ממנו הדרך» (let us begin with a parable: one went on a road and lost his way).
- **Recurs.** MDL lines 167, 171; Talmud, 'a baal teshuvah stands where the righteous cannot'.
- **See also in SB2.** SB2-MAG-04, SB2-MAG-05, SB2-BST-13, SB2-BST-22, SB2-RSB-08, SB2-RYZ-10.
- **Guide.** Finding your way again after being lost can bring a joy that never getting lost would not.

#### SB2-MAG-23. A person's own joy makes his hand clap *Domain:* body; joy

- **Mashal.** A person full of joy claps his hand without meaning to, because the joy spreads into his limbs.
- **Nimshal.** When a person is joined to the Shechinah as a limb, the flow from above reaches him naturally, without his intending it.
- **Parts.** the joy → the divine flow; the hand → the person as a 'limb'; clapping by itself → receiving without effort.
- **Breaks** [ours]. Ours: a hand is part of the body; the nimshal needs a person to choose to be a limb.
- **Principles.** PR-L09, PR-L04
- **Source.** Maggid Devarav LeYaakov, `Chassidus-txt/R. Dov Ber, Maggid of Mezritch (c.1704-1772)/Maggid Devarav leYaakov (Mezritch, Volhynia, 1760-1780).txt` line 49: «כמשל אדם שיש לו שמחה מטפח ביד אפילו כשאינו מתכוין לכך» (like a person who has joy and claps with his hand even without meaning to).
- **Recurs.** Tanya ch. 23 (limbs as a chariot).
- **Guide.** When you are joined to something bigger, it moves through you on its own, the way gladness reaches your hands.

#### SB2-MAG-24. The mashal is a vessel for the idea *Domain:* the mashal itself; speech

- **Mashal.** A mashal is a vessel for understanding, just as speech is a vessel for thought. Speaking without intention is like 'broken vessels' with no life in them.
- **Nimshal.** To see the life inside words, a person must strip himself of physicality and dress himself in the words; then he is joined to G-d.
- **Parts.** the mashal → a vessel; the idea inside → its light; empty speech → broken vessels; stripping and entering the words → devekus.
- **Breaks** [stated]. Stated limit (the Maggid, MDL line 181): once the child grasps the idea himself, the mashal's letters are no longer needed.
- **Principles.** PR-L01, PR-L09, PR-L10
- **Source.** Maggid Devarav LeYaakov, `Chassidus-txt/R. Dov Ber, Maggid of Mezritch (c.1704-1772)/Maggid Devarav leYaakov (Mezritch, Volhynia, 1760-1780).txt` line 41: «המשל הוא כלי להשכל וכן הדיבור הוא כלי למחשבה» (the mashal is a vessel for the intellect, as speech is a vessel for thought).
- **Recurs.** Keter Shem Tov line 348 (same); R. Aharon's 'handles for the basket'; the Rebbe Rashab, Samach Vav line 3104.
- **See also in SB2.** SB2-BST-30, SB2-TZ-22, SB2-MHS-04, SB2-RYZ-06, SB2-RBE-07, SB2-RBE-08, SB2-RSB-35.
- **Guide.** A picture is a cup for an idea. Pay attention to what it holds, not just to the cup.

## Tzemach Tzedek (28)

#### SB2-TZ-01. Water takes the color of the glass *Domain:* water and light; vessels

- **Mashal.** Clear water poured into colored glass vessels looks red in one and green in another. The change is only to the eye: poured out, the water is clear again.
- **Nimshal.** G-d's light in the sefiros seems to become kindness here and strictness there, but it does not truly change; the difference comes from the vessels.
- **Parts.** the water → the divine light; the colored vessels → the sefiros' vessels; apparent color → kindness, judgment and so on; poured out, clear again → the light in itself, unchanged.
- **Breaks** [stated]. Stated (the Rebbe Rashab, Ayin Beis line 85): in some levels the lights really are kindness and might, not just colored; Samach Vav (line 5734) limits the parable to the light already inside the vessel. Stated (DM line 110): it fits the 'line' (kav) but His essence is above even that.
- **Principles.** PR-L04, PR-L07, PR-L08
- **Source.** Derech Mitzvosecha (Tzemach Tzedek), `Chassidus-txt/R. Menachem Mendel Schneersohn (Tzemach Tzedek) (1789-1866)/Derekh Mitzvotekha (Lubavitch, 1813-1827).txt` line 108: «וכמשל מים שמשתנים לפי גוון הכלי שאין השינוי בהם אמיתי רק למראה העין» (like water that changes with the color of the vessel; the change in it is not real, only to the eye).
- **Recurs.** R. Moshe Cordovero, Pardes (source); DM lines 110, 112; the Rebbe Rashab, Samach Vav lines 2539, 5582, 5673, 5964; Ayin Beis line 85; Rayatz line 183; the Rebbe, Likkutei Sichos line 36357.
- **See also in SB2.** SB2-TZ-02, SB2-TZ-06, SB2-TZ-20, SB2-RSB-03, SB2-RSB-38, SB2-RYZ-01, SB2-RYZ-15, SB2-RBE-17.
- **Guide.** The same light can look warm in one room and cold in another. It is the rooms that differ.

#### SB2-TZ-02. The sun that melts and hardens *Domain:* light and sun; fire

- **Mashal.** The sun (or fire) with one power, heat, melts wax, hardens wet clay, cooks, and burns: one force, many opposite effects, depending on what it acts on.
- **Nimshal.** G-d's power is one and simple; the many and opposite effects (kindness, judgment) come through the vessels it acts in.
- **Parts.** the sun's single heat → His one simple power; wax, clay, food → different receivers; opposite results → the varied workings of the sefiros.
- **Breaks** [stated]. Stated (DM line 108): the sun shines by necessity and cannot hold back its light, while G-d gives by will.
- **Principles.** PR-L04, PR-L07, PR-L08
- **Source.** Derech Mitzvosecha (Tzemach Tzedek), `Chassidus-txt/R. Menachem Mendel Schneersohn (Tzemach Tzedek) (1789-1866)/Derekh Mitzvotekha (Lubavitch, 1813-1827).txt` line 107: «כעין השמש והאש שבכח א' שבו והוא החום הוא מתיך השעוה ותקפיא דבר לח» (like the sun and fire: by one power in it, heat, it melts wax and hardens a wet thing).
- **Recurs.** Pardes (source); Kuzari; R. Aharon's 'one person with many powers'.
- **See also in SB2.** SB2-TZ-01, SB2-TZ-06, SB2-TZ-20, SB2-RSB-03, SB2-RSB-38, SB2-RYZ-01, SB2-RYZ-15, SB2-RBE-17.
- **Guide.** One warmth can soften one thing and harden another. What changes is what it touches.

#### SB2-TZ-03. The axe in the hewer's hand *Domain:* craft; tools

- **Mashal.** A woodcutter cuts with an axe. The cutting is done by him, through the axe; the axe is a different thing from the man.
- **Nimshal.** The sefiros are like tools through which G-d acts; the action is His, through a medium.
- **Parts.** the woodcutter → G-d; the axe → the vessel or sefirah; the cutting → the effect in the world.
- **Breaks** [stated]. Stated: this fits only the vessels, and only for 'action through a tool'; regarding essence, the axe is far from the hewer, but the sefiros' lights are not separate from Him.
- **Principles.** PR-L07, PR-L11
- **Source.** Derech Mitzvosecha (Tzemach Tzedek), `Chassidus-txt/R. Menachem Mendel Schneersohn (Tzemach Tzedek) (1789-1866)/Derekh Mitzvotekha (Lubavitch, 1813-1827).txt` line 107: «ולענין זה הוא כמשל החוצב בגרזן» (and in this respect it is like one who hews with an axe).
- **Recurs.** Isaiah 10:15; R. Aharon (the human-and-tools analogy he forbids for essence); the Rebbe, Melukat line 1548.
- **See also in SB2.** SB2-TZ-12, SB2-RSB-11, SB2-RSB-13, SB2-RSB-30, SB2-RSB-34.
- **Guide.** A tool does the work, but someone is holding it. Look past the tool to the hand.

#### SB2-TZ-04. A person's name *Domain:* the soul's faculties; speech

- **Mashal.** A person's name is not part of his soul, like his mind or feelings. It is only so others can call him and he will turn. When no one calls, he hardly needs it.
- **Nimshal.** The 'hidden sefiros' before creation, and G-d's relation to worlds, are like a name: not part of His essence, only how He 'turns' to others.
- **Parts.** the person → G-d's essence; his name → the source of the sefiros, the Name; being called → His turning toward creation.
- **Breaks** [stated]. Stated (DM line 287): a person's name is forced on him by society, while G-d chose to be called Merciful and Wise. Stated (DM line 276): unlike flint and coal, nothing of the name was hidden in the person beforehand, which is why this mashal fits best.
- **Principles.** PR-L06, PR-L07, PR-L09
- **Source.** Derech Mitzvosecha (Tzemach Tzedek), `Chassidus-txt/R. Menachem Mendel Schneersohn (Tzemach Tzedek) (1789-1866)/Derekh Mitzvotekha (Lubavitch, 1813-1827).txt` line 251: «כמשל שם האדם לגבי עצמות האדם שאינו בערך עצמותו כלל רק שעל ידו פונה לקוראו» (like a person's name relative to his essence: it is not in proportion to his essence at all, only by it he turns to the one who calls).
- **Recurs.** DM lines 230, 276, 287; the Maharash, Toras Shmuel line 710; the Rebbe Rashab, Samach Vav line 2479, Ayin Beis line 3705; the Rebbe, Melukat line 2299.
- **See also in SB2.** SB2-TZ-05, SB2-MHS-03, SB2-RSB-14.
- **Guide.** Your name is the part of you that is for others. You are much more than it, and you still turn when someone calls it.

#### SB2-TZ-05. Flame bound in a coal, fire in a flint *Domain:* fire

- **Mashal.** A flame is held inside a glowing coal; fire hides inside a flint until it is struck.
- **Nimshal.** Sefer Yetzirah says the sefiros are 'like a flame bound to a coal'. But the Tzemach Tzedek rejects it for the hidden sefiros in the Infinite: there the fire already exists in hiding, which is not true of Him.
- **Parts.** the coal or flint → the source; the hidden flame → sefiros in potential; striking → revelation.
- **Breaks** [stated]. Stated: this mashal does not fit the Essence, because the flame really exists in the coal and has a defined nature; the 'name' parable fits better.
- **Principles.** PR-L06, PR-L07
- **Source.** Derech Mitzvosecha (Tzemach Tzedek), `Chassidus-txt/R. Menachem Mendel Schneersohn (Tzemach Tzedek) (1789-1866)/Derekh Mitzvotekha (Lubavitch, 1813-1827).txt` line 276: «הנה אין הענין כמשל שלהבת הקשורה בגחלת» (the matter is not like the parable of a flame bound to a coal).
- **Recurs.** Sefer Yetzirah 1:7; the Rebbe Rashab, Samach Vav lines 1168, 2450, 7205; Ayin Beis lines 3705, 4497; Rayatz line 1395; the Rebbe, Melukat line 614.
- **See also in SB2.** SB2-TZ-04, SB2-MHS-03, SB2-RSB-14.
- **Guide.** Some things were waiting inside all along, like fire in a stone. Some are new, like a name. Know which you are dealing with.

#### SB2-TZ-06. The ray of the sun *Domain:* light and sun

- **Mashal.** The sun's light streaming out is nothing next to the sun itself; inside the sun, it counts for nothing.
- **Nimshal.** Creatures are like a ray: they are nothing next to their Source, and the light does not change Him.
- **Parts.** the sun → G-d; the ray → the light that gives life to worlds; the ray's nothingness in the sun → creation's bittul.
- **Breaks** [stated]. Stated: the sun shines by its nature, without choice, while He gives by will (DM line 252, 295); Samach Vav (line 1871) says the ray fits for 'nullification' but not for creation from nothing.
- **Principles.** PR-L04, PR-L07, PR-L08
- **Source.** Derech Mitzvosecha (Tzemach Tzedek), `Chassidus-txt/R. Menachem Mendel Schneersohn (Tzemach Tzedek) (1789-1866)/Derekh Mitzvotekha (Lubavitch, 1813-1827).txt` line 252: «אך מ"מ אין המשל דזיו השמש דומה לנמשל כלל» (but even so, the parable of the sun's light is not like the nimshal at all).
- **Recurs.** Tanya, Shaar HaYichud ch. 3 (source); Samach Vav lines 634, 1871, 2389, 2420; Ayin Beis lines 144, 542, 1003; Rayatz lines 222, 383; the Rebbe, Melukat lines 1163, 1295, 2732.
- **See also in SB2.** SB2-TZ-01, SB2-TZ-02, SB2-TZ-20, SB2-RSB-03, SB2-RSB-38, SB2-RYZ-01, SB2-RYZ-15, SB2-RBE-17.
- **Guide.** A beam of sunlight is real, but next to the sun it disappears. Maybe you can feel like that beam: real, and resting in something much bigger.

#### SB2-TZ-07. The child who calls 'Abba' *Domain:* father and son; speech

- **Mashal.** A small child calls his father 'Abba'. The word reaches the father himself, though the child cannot know who his father is the way a grown-up would.
- **Nimshal.** Our knowing of G-d does not reach Him as He is, yet like the child's call it is aimed at His very self.
- **Parts.** the child → the person; the word 'Abba' → our idea of G-d; the father himself → His essence; the adult's understanding → the true knowledge we lack.
- **Breaks** [ours]. Ours: the father can explain himself later; our knowledge of Him will never reach Him.
- **Principles.** PR-L12, PR-L09
- **Source.** Derech Mitzvosecha (Tzemach Tzedek), `Chassidus-txt/R. Menachem Mendel Schneersohn (Tzemach Tzedek) (1789-1866)/Derekh Mitzvotekha (Lubavitch, 1813-1827).txt` line 53: «וה"ז כמשל קריאת אבא שהתינוק קורא לגבי עצמיות ביאור הענין» (and this is like the call 'Abba' that the infant calls, relative to the real explanation of the matter).
- **Recurs.** the Rebbe (sichos on 'simple faith').
- **Guide.** You don't need to understand someone to call them. A child calling 'Dad' reaches him completely.

#### SB2-TZ-08. The messenger who says only what he was told *Domain:* commerce; speech

- **Mashal.** A messenger says nothing on his own; he only says what was put in his mouth. He is just a vessel that carries the message from sender to receiver.
- **Nimshal.** The channels through which G-d's light flows to the worlds are like messengers: carriers with nothing of their own.
- **Parts.** the sender → G-d; the messenger → the intermediate channels (angels, sefiros' garments); the message → the flow of life.
- **Breaks** [ours]. Ours: a messenger may still distort; the stated point is that a pure channel adds nothing.
- **Principles.** PR-L04, PR-L07
- **Source.** Derech Mitzvosecha (Tzemach Tzedek), `Chassidus-txt/R. Menachem Mendel Schneersohn (Tzemach Tzedek) (1789-1866)/Derekh Mitzvotekha (Lubavitch, 1813-1827).txt` line 59: «ועד"מ השליח שהוא איננו מדבר שום דבר מדעתו כ"א מה שהושם בפיו» (like a messenger who says nothing of his own, only what was placed in his mouth).
- **Recurs.** Maimonides; Tanya ch. 39 (angels as messengers).
- **Guide.** Sometimes the best thing you can be is a clear pipe: let the good thing pass through you without adding yourself.

#### SB2-TZ-09. The seed-drop holds the whole child *Domain:* body; birth

- **Mashal.** A tiny drop contains all the limbs of the child as one: head, feet, hair, nails. While it is a drop, a foot could become a head. Once grown, each limb is fixed.
- **Nimshal.** Before the fallen sparks are fully sorted, they can be transformed (a 'foot' can rise to a 'head'); in this world, teshuvah can still change what one is.
- **Parts.** the drop → the unsorted state; limbs mixed as one → potential for transformation; the grown body → the fixed state after sorting.
- **Breaks** [ours]. Ours: in biology the drop cannot choose; in a person, teshuvah is a choice.
- **Principles.** PR-L04, PR-L09
- **Source.** Derech Mitzvosecha (Tzemach Tzedek), `Chassidus-txt/R. Menachem Mendel Schneersohn (Tzemach Tzedek) (1789-1866)/Derekh Mitzvotekha (Lubavitch, 1813-1827).txt` line 86: «והוא כמשל הטפה שכוללת כל איברי הולד הראש והרגל והשערות וצפרנים כא'» (and it is like the drop that contains all the child's limbs, the head and the foot, the hair and the nails, as one).
- **Recurs.** DM line 265 (growth of the child, the seed and the tree).
- **See also in SB2.** SB2-MAG-11, SB2-MAG-12, SB2-RSB-05.
- **Guide.** While something is still young in you, it can still become anything. That is why change is possible now.

#### SB2-TZ-10. Pearls in a tied bundle *Domain:* commerce; wealth

- **Mashal.** A rich man is glad of his bag of pearls lying with him, even though he doesn't see them every moment.
- **Nimshal.** A person can rejoice in knowing G-d's unity even though he has not grasped His essence; the knowledge itself, kept close, gives joy.
- **Parts.** the pearls → knowledge of the unity; the closed bundle → not seeing it now; the joy → steady gladness of faith.
- **Breaks** [ours]. Ours: the rich man once saw his pearls; we never 'see' the essence.
- **Principles.** PR-L09, PR-L12
- **Source.** Derech Mitzvosecha (Tzemach Tzedek), `Chassidus-txt/R. Menachem Mendel Schneersohn (Tzemach Tzedek) (1789-1866)/Derekh Mitzvotekha (Lubavitch, 1813-1827).txt` line 97: «ועד"מ כמו ששמח העשיר מהון מרגליות הצרור ומונח אצלו» (like the rich man who rejoices in his wealth of pearls, bundled and lying with him).
- **Recurs.** Tanya ch. 33 (Alter Rebbe, source); Sefer HaChakirah line 617 (gold in a locked chest); Maharash, Toras Shmuel line 2146.
- **See also in SB2.** SB2-MHS-09, SB2-MHS-11, SB2-RSB-23.
- **Guide.** You don't have to look at what you treasure all the time. Knowing it is there can be enough to warm the day.

#### SB2-TZ-11. Before a king, a small slip is a rebellion *Domain:* king and kingdom

- **Mashal.** Before a king, even a small motion that throws off the awe counts as rebellion, and all one's efforts do not look like much to the king.
- **Nimshal.** 'We have sinned': before the truth, a hairsbreadth seems like a mountain, so the righteous truly confess.
- **Parts.** the king → G-d; the slight movement → a small lapse; the king's view → the true measure.
- **Breaks** [ours]. Ours: a human king can be offended; G-d is not hurt, only the closeness is.
- **Principles.** PR-L04, PR-L08
- **Source.** Derech Mitzvosecha (Tzemach Tzedek), `Chassidus-txt/R. Menachem Mendel Schneersohn (Tzemach Tzedek) (1789-1866)/Derekh Mitzvotekha (Lubavitch, 1813-1827).txt` line 129: «כמשל מי שעומד לפני מלך שגם תנועה קלה בפריקת עול האימה כמרד יחשב» (like one who stands before a king: even a slight movement of throwing off awe is counted as rebellion).
- **Recurs.** Talmud ('around Him it storms greatly'); the Rebbe Rashab on teshuvah.
- **See also in SB2.** SB2-MAG-20, SB2-MAG-21, SB2-TZ-13, SB2-MHS-12, SB2-RSB-07, SB2-RSB-24, SB2-RYZ-17.
- **Guide.** The closer you are to someone, the more small things matter. That's not harshness; it's closeness.

#### SB2-TZ-12. The weight on the scale *Domain:* commerce; tools

- **Mashal.** When a stone weight is put on one pan of a scale, it lifts the merchandise on the other pan up from the ground by as much as it weighs.
- **Nimshal.** Malchus 'weighs' and lifts the fallen sparks; what goes down on one side raises the precious sparks on the other.
- **Parts.** the weight → malchus, the lowering; the goods on the ground → the fallen sparks; lifting → raising them.
- **Breaks** [ours]. Ours: a scale balances; birurim don't just balance, they transform.
- **Principles.** PR-L04
- **Source.** Derech Mitzvosecha (Tzemach Tzedek), `Chassidus-txt/R. Menachem Mendel Schneersohn (Tzemach Tzedek) (1789-1866)/Derekh Mitzvotekha (Lubavitch, 1813-1827).txt` line 131: «שזהו כמשל האבן ששוקלים בה וכשמניחים אותו על כף א' מכפי המשקולת» (this is like the stone used for weighing: when one places it on one pan of the scale).
- **Recurs.** Zohar, 'to weigh'.
- **See also in SB2.** SB2-TZ-03, SB2-RSB-11, SB2-RSB-13, SB2-RSB-30, SB2-RSB-34.
- **Guide.** Sometimes going down on one side lifts something precious on the other.

#### SB2-TZ-13. A great king lodging with a pauper *Domain:* king and kingdom; gratitude

- **Mashal.** When a great king stays at a poor man's house, the poor man cannot reach him with love or closeness, but he can thank and praise him.
- **Nimshal.** On Chanukah we 'thank and praise' (hallel and hoda'ah): a light too high to grasp is reached through thanks alone.
- **Parts.** the great king → the light above understanding; the pauper → a person; praise → hoda'ah (acknowledgment).
- **Breaks** [ours]. Ours: the poor man still sees the king; hoda'ah thanks without seeing.
- **Principles.** PR-L04, PR-L12
- **Source.** Derech Mitzvosecha (Tzemach Tzedek), `Chassidus-txt/R. Menachem Mendel Schneersohn (Tzemach Tzedek) (1789-1866)/Derekh Mitzvotekha (Lubavitch, 1813-1827).txt` line 138: «כמשל מלך גדול המתאכסן אצל עני ופחות ערך שאין העני יכול להגיעו בשום אהבה וקירוב» (like a great king who lodges with a poor and lowly man, who cannot reach him with any love or closeness).
- **Recurs.** Ayin Beis line 3715 (hoda'ah as admitting); Tanya ch. 'thanking'.
- **See also in SB2.** SB2-MAG-20, SB2-MAG-21, SB2-TZ-11, SB2-MHS-12, SB2-RSB-07, SB2-RSB-24, SB2-RYZ-17.
- **Guide.** When something is too big to love or understand, you can still say thank you. That reaches.

#### SB2-TZ-14. The lizard in the king's palace *Domain:* king and kingdom; animals

- **Mashal.** A lizard lives in the king's palace. It's not that the king wants it there; he is so exalted he doesn't bother to notice it.
- **Nimshal.** The husks (kelipos) get a little life from the surrounding light, not because they are wanted, but because the surrounding light is too great to exclude them.
- **Parts.** the palace → the surrounding light; the lizard → kelipah; the king not noticing → the light that doesn't 'mind' what draws from it.
- **Breaks** [ours]. Ours: the king could throw it out; the stated nimshal says the kelipah's life is only an 'overflow'.
- **Principles.** PR-L04, PR-L07
- **Source.** Derech Mitzvosecha (Tzemach Tzedek), `Chassidus-txt/R. Menachem Mendel Schneersohn (Tzemach Tzedek) (1789-1866)/Derekh Mitzvotekha (Lubavitch, 1813-1827).txt` line 145: «וכמשל השממית שעם היותה בהיכלי מלך לא שהיא רצויה אצלו» (like the lizard which, though it is in the king's palaces, is not wanted by him).
- **Recurs.** Proverbs 30:28; Tanya ch. 22.
- **Guide.** Something can live off what is good without being invited. That doesn't make it welcome.

#### SB2-TZ-15. The barrel that overflows *Domain:* water; vessels

- **Mashal.** A barrel full past the brim spills water on every side, unlike water flowing through a pipe and tap to the right vessel only.
- **Nimshal.** The surrounding light overflows and some reaches even the unworthy; light through the inner channels reaches only the proper place.
- **Parts.** the overflowing barrel → the surrounding light (makif); the pipe and tap → the ordered inner flow; spilled water → light that reaches far places.
- **Breaks** [ours]. Ours: spilled water is wasted; the nimshal says the spill shows the fullness.
- **Principles.** PR-L04
- **Source.** Derech Mitzvosecha (Tzemach Tzedek), `Chassidus-txt/R. Menachem Mendel Schneersohn (Tzemach Tzedek) (1789-1866)/Derekh Mitzvotekha (Lubavitch, 1813-1827).txt` line 145: «וכמשל החבית המליאה על כל גדותיה נשפך ממנה מים לכל צד» (like a barrel full over its brims: water spills from it on every side).
- **Recurs.** Alter Rebbe, Siddur (Baruch She'amar); DM line 165; the Rebbe, Melukat lines 339, 1291.
- **See also in SB2.** SB2-TZ-17, SB2-TZ-18, SB2-TZ-19, SB2-TZ-28, SB2-MHS-10, SB2-RSB-26, SB2-RSB-37, SB2-RYZ-11, SB2-PIA-05.
- **Guide.** When something is really full, it spills. What reaches you from far away may be the overflow of something very full.

#### SB2-TZ-16. One letter and the speaking soul *Domain:* the soul's faculties: speech

- **Mashal.** One letter is nothing next to the whole speaking soul, which can speak words without end.
- **Nimshal.** All the created worlds are like one 'word' next to G-d; they are null before Him.
- **Parts.** one letter → all the worlds; the speaking soul → G-d's power of speech; endless speech → His infinity.
- **Breaks** [ours]. Ours: the soul can tire; His speech never ends.
- **Principles.** PR-L09, PR-L04, PR-L07
- **Source.** Derech Mitzvosecha (Tzemach Tzedek), `Chassidus-txt/R. Menachem Mendel Schneersohn (Tzemach Tzedek) (1789-1866)/Derekh Mitzvotekha (Lubavitch, 1813-1827).txt` line 236: «וכמשל ביטול אות א' לגבי כללות נפש המדברת» (like the nullity of one letter next to the whole speaking soul).
- **Recurs.** Tanya, Shaar HaYichud ch. 6-7 (source); Maamarei 1855 line 409; the Rebbe Rashab, Samach Vav; the Rebbe, Likkutei Sichos line 22359.
- **See also in SB2.** SB2-MAG-15, SB2-MAG-17, SB2-TZ-21, SB2-RSB-04, SB2-RSB-10.
- **Guide.** One word you say is tiny next to all you could ever say. The whole world may be like that word.

#### SB2-TZ-17. Water held back by a board *Domain:* water

- **Mashal.** When a board is put in the path of rushing water, it stops the flow. When the water breaks through, it rushes far stronger than before.
- **Nimshal.** Love that comes from being far and blocked becomes boundless when it breaks out.
- **Parts.** the board → distance or obstacle; the rushing water → the soul's love; breaking through → teshuvah or deep longing.
- **Breaks** [ours]. Ours: water has no choice; a soul can let the dam stand.
- **Principles.** PR-L04, PR-L09
- **Source.** Derech Mitzvosecha (Tzemach Tzedek), `Chassidus-txt/R. Menachem Mendel Schneersohn (Tzemach Tzedek) (1789-1866)/Derekh Mitzvotekha (Lubavitch, 1813-1827).txt` line 259: «וכמשל מרוצת המים כשמעכבים מרוצתם ע"י דף» (like rushing water when its run is held back by a board).
- **Recurs.** DM line 298; Ayin Beis line 2464 (water channel that breaks the dam); Maharash lines 2023, 9082; the Rebbe, Likkutei Sichos index line 13602.
- **See also in SB2.** SB2-TZ-15, SB2-TZ-18, SB2-TZ-19, SB2-TZ-28, SB2-MHS-10, SB2-RSB-26, SB2-RSB-37, SB2-RYZ-11, SB2-PIA-05.
- **Guide.** What held you back can make you stronger when you break through. Don't despise the dam; it is building pressure.

#### SB2-TZ-18. Fish in the sea *Domain:* nature; water

- **Mashal.** Fish are one with the sea: all their life comes from it, and they cannot live a moment out of the water.
- **Nimshal.** The souls in their root are like 'fish of the sea', not separate at all from G-d, wholly living from Him.
- **Parts.** the sea → G-d (the hidden world); fish → souls; dying out of water → being cut off.
- **Breaks** [ours]. Ours: fish are still separate bodies in the sea; the nimshal says the souls are not separate at all.
- **Principles.** PR-L04, PR-L09
- **Source.** Derech Mitzvosecha (Tzemach Tzedek), `Chassidus-txt/R. Menachem Mendel Schneersohn (Tzemach Tzedek) (1789-1866)/Derekh Mitzvotekha (Lubavitch, 1813-1827).txt` line 292: «כמשל הדגים שהם לאחדים עם הים וכל חיותם הוא ממנו» (like the fish, which are one with the sea, and all their life is from it).
- **Recurs.** R. Akiva's parable (Talmud, Berachos 61b); Ayin Beis line 5746; Rayatz line 797; the Rebbe, Likkutei Sichos line 32252.
- **See also in SB2.** SB2-TZ-15, SB2-TZ-17, SB2-TZ-19, SB2-TZ-28, SB2-MHS-10, SB2-RSB-26, SB2-RSB-37, SB2-RYZ-11, SB2-PIA-05.
- **Guide.** A fish doesn't think about water; it just lives in it. Maybe you live in something like that, all the time.

#### SB2-TZ-19. Groundwater purified through the earth *Domain:* water; nature

- **Mashal.** Water from the deep spreads through the thick earth, which is lower than water; by passing through, it is purified and becomes better.
- **Nimshal.** The soul comes down into a body for the sake of going higher: passing through the physical refines it and lets it love 'with all your might'.
- **Parts.** the deep water → the soul; thick earth → the body and world; purified water → the refined soul; the spring → its new greater love.
- **Breaks** [ours]. Ours: water is filtered passively; the soul must do the work.
- **Principles.** PR-L04, PR-L09
- **Source.** Derech Mitzvosecha (Tzemach Tzedek), `Chassidus-txt/R. Menachem Mendel Schneersohn (Tzemach Tzedek) (1789-1866)/Derekh Mitzvotekha (Lubavitch, 1813-1827).txt` line 292: «כמשל התפשטות מי התהום בעובי כדור הארץ» (like the spreading of the deep waters through the thickness of the earth).
- **Recurs.** the Rebbe Rashab, Samach Vav (descent for ascent).
- **See also in SB2.** SB2-TZ-15, SB2-TZ-17, SB2-TZ-18, SB2-TZ-28, SB2-MHS-10, SB2-RSB-26, SB2-RSB-37, SB2-RYZ-11, SB2-PIA-05.
- **Guide.** Going through a hard, heavy time can clear you, the way water comes up clean after passing through stone and soil.

#### SB2-TZ-20. Light through a pane of glass *Domain:* light and sun

- **Mashal.** Sunlight shines through white glass, but it is not of the glass. Take the glass away and put in another, and the same light shines in it.
- **Nimshal.** G-d's light shines in wisdom but is not of wisdom's nature, just as it is not of any other attribute.
- **Parts.** the sunlight → the infinite light; the glass → the vessel of wisdom; replacing the glass → the light belonging to none of the vessels.
- **Breaks** [ours]. Ours: glass slightly colors light; here the stated point is that the light stays itself.
- **Principles.** PR-L04, PR-L07
- **Source.** Derech Mitzvosecha (Tzemach Tzedek), `Chassidus-txt/R. Menachem Mendel Schneersohn (Tzemach Tzedek) (1789-1866)/Derekh Mitzvotekha (Lubavitch, 1813-1827).txt` line 296: «והוא כמשל אור השמש שמאיר בזכוכית לבנה» (and it is like sunlight shining through white glass).
- **Recurs.** Tanya ch. 51 (source); DM line 119; Rayatz line 876.
- **See also in SB2.** SB2-TZ-01, SB2-TZ-02, SB2-TZ-06, SB2-RSB-03, SB2-RSB-38, SB2-RYZ-01, SB2-RYZ-15, SB2-RBE-17.
- **Guide.** Light comes through you but isn't made of you. That's a relief: you don't have to be the light, just let it through.

#### SB2-TZ-21. One idea split into many words *Domain:* the soul's faculties: thought and speech

- **Mashal.** A single insight, when spoken, splits into many words, each carrying a small part of it.
- **Nimshal.** Through divine speech the one life is divided into countless separate creatures, each with a small portion.
- **Parts.** the insight → the one divine life; the many words → the many creatures; each word's share → each creature's spark.
- **Breaks** [ours]. Ours: words are made by the speaker after the thought; creatures are made from nothing.
- **Principles.** PR-L09, PR-L04
- **Source.** Derech Mitzvosecha (Tzemach Tzedek), `Chassidus-txt/R. Menachem Mendel Schneersohn (Tzemach Tzedek) (1789-1866)/Derekh Mitzvotekha (Lubavitch, 1813-1827).txt` line 316: «כמשל השכלה א' שבדיבור נחלקת לכמה וכמה תיבות» (like one insight that in speech is divided into many words).
- **Recurs.** DM line 58; the Rebbe Rashab, Samach Vav line 5404.
- **See also in SB2.** SB2-MAG-15, SB2-MAG-17, SB2-TZ-16, SB2-RSB-04, SB2-RSB-10.
- **Guide.** One big feeling can come out as many small sentences. The world may be one thought, spoken out in many pieces.

#### SB2-TZ-22. A mashal versus a riddle *Domain:* the mashal itself

- **Mashal.** Some parables are thin and barely hide the meaning; others hide it more, like a riddle. All are garments, but not all equally thick.
- **Nimshal.** The garments that hide G-d's light differ in thickness: some show it nearly openly, others hide it like a riddle.
- **Parts.** thin parable → a light garment (Beriah); riddle → a thick garment (Asiyah); the meaning → the light.
- **Breaks** [stated]. Stated: a parable is still a 'foreign' thing; the riddle hides more, but both reveal something.
- **Principles.** PR-L01, PR-L05, PR-L14
- **Source.** Derech Mitzvosecha (Tzemach Tzedek), `Chassidus-txt/R. Menachem Mendel Schneersohn (Tzemach Tzedek) (1789-1866)/Derekh Mitzvotekha (Lubavitch, 1813-1827).txt` line 12: «שיש משל דק שאינו מעלים הנמשל כ"כ ויש שמעלימו יותר כמו חידה» (there is a thin parable that does not hide the nimshal much, and one that hides it more, like a riddle).
- **Recurs.** the Rebbe Rashab, Ayin Beis lines 3406, 3414 (Beriah like a parable, Asiyah like a riddle).
- **See also in SB2.** SB2-BST-30, SB2-MAG-24, SB2-MHS-04, SB2-RYZ-06, SB2-RBE-07, SB2-RBE-08, SB2-RSB-35.
- **Guide.** Some pictures almost say the thing outright; some make you dig. Both are trying to show you something.

#### SB2-TZ-23. The melody that still moves us *Domain:* music

- **Mashal.** A melody is not new, yet when people sing it, they are stirred more than by words.
- **Nimshal.** Song and melody in prayer draw an arousal deeper than understanding.
- **Parts.** the melody → song in divine service; being moved → the soul's arousal; not new → beyond novelty or reason.
- **Breaks** [ours]. Ours: music moves the body too; the nimshal wants the soul's movement.
- **Principles.** PR-L09, PR-L04, PR-L13
- **Source.** Maamarei Admur HaTzemach Tzedek, `Chassidus-txt/R. Menachem Mendel Schneersohn (Tzemach Tzedek) (1789-1866)/Maamarei Admur HaTzemach Tzedek (Lubavitch, 1855).txt` line 78: «וכמשל הניגון אף שאינו דבר חדש אעפ"כ כשמשוררים הניגון מתפעלים» (like a melody: though it is nothing new, when they sing the melody they are moved).
- **Recurs.** the Rayatz (on niggun); the Alter Rebbe ('song is the quill of the soul').
- **Guide.** An old tune can still move you. Some things don't need to be new to reach you.

#### SB2-TZ-24. Torah and prayer: mountain and valley *Domain:* travel; nature

- **Mashal.** Two people, one on top of a mountain, one in the valley below. Either the one above comes down to meet, or the one below climbs up.
- **Nimshal.** Torah is G-d coming down to us; prayer is us climbing up to Him.
- **Parts.** the one on the mountain → G-d; the one in the valley → the person; coming down → Torah; climbing up → prayer.
- **Breaks** [ours]. Ours: on a mountain the two are equals; here One is infinitely above.
- **Principles.** PR-L04
- **Source.** Maamarei Admur HaTzemach Tzedek, `Chassidus-txt/R. Menachem Mendel Schneersohn (Tzemach Tzedek) (1789-1866)/Maamarei Admur HaTzemach Tzedek (Lubavitch, 1855).txt` line 61: «הוא כמשל שני ב"א זה עומד בגובה ההר וזה עומד בשפולי» (it is like two people, one standing on the height of the mountain and one in the lowlands).
- **Recurs.** Ayin Beis lines 3096, 3105, 4486, 5227; Maharash line 1397.
- **Guide.** Sometimes you climb toward what is higher; sometimes it comes down to meet you. Both are a meeting.

#### SB2-TZ-25. The seal shows in wax, not in the gem *Domain:* craft; light

- **Mashal.** A seal engraved on a gem can't be seen because of the gem's brilliance; it shows clearly when pressed into wax.
- **Nimshal.** The higher a thing is, the lower it must come to be revealed: the deepest root of the mitzvos shows itself in plain physical deeds.
- **Parts.** the engraved gem → the high source; the brilliance → too much light to see; the wax → physical deed; the clear impression → revelation below.
- **Breaks** [ours]. Ours: the wax shows the letters reversed; the nimshal doesn't claim a reversal.
- **Principles.** PR-L04, PR-L09
- **Source.** Maamarei Admur HaTzemach Tzedek, `Chassidus-txt/R. Menachem Mendel Schneersohn (Tzemach Tzedek) (1789-1866)/Maamarei Admur HaTzemach Tzedek (Lubavitch, 1855).txt` line 564: «וכמשל מהחותם שא"א לראות מחמת בהירות אבן טוב והוא ניכר דוקא בשעוה» (like the seal that cannot be seen because of the brilliance of the gem, and is seen only in wax).
- **Recurs.** TZM line 192; Maharash lines 1799, 3226; Rayatz lines 172, 1645 (letters engraved on a gem).
- **Guide.** The highest things often show up most clearly in the plainest acts.

#### SB2-TZ-26. The burning palace *Domain:* house; perception

- **Mashal.** A man passing from place to place saw a palace in flames and asked: could this palace have no owner? The owner looked out and said, 'I am the owner.'
- **Nimshal.** Avraham saw the world and asked who runs it, and G-d answered him; the world itself raises the question that leads to Him.
- **Parts.** the palace → the world; burning → its turmoil or its brilliance; the traveler's question → searching; the owner's answer → revelation.
- **Breaks** [ours]. Ours (and debated): the parable can mean 'lit up' or 'on fire'; either way, the answer comes from the Owner, not only from the reasoning.
- **Principles.** PR-L04, PR-L03
- **Source.** Sefer HaChakirah (Tzemach Tzedek), `Chassidus-txt/R. Menachem Mendel Schneersohn (Tzemach Tzedek) (1789-1866)/Sefer HaChakirah (Lubavitch, c. 1840s).txt` line 125: «משל לאחד שהיה עובר ממקום למקום וראה בירה אחת דולקת» (like one passing from place to place who saw a palace burning).
- **Recurs.** Genesis Rabbah 39:1 (source); Ayin Beis line 3675; Rayatz line 1036; the Rebbe, Melukat line 2613.
- **See also in SB2.** SB2-RSB-02, SB2-RBE-13, SB2-RSB-16, SB2-MHS-01, SB2-MHS-02.
- **Guide.** When the world looks lit up, or on fire, ask: who is in charge here? Sometimes someone answers.

#### SB2-TZ-27. The ship and the man walking on it *Domain:* travel; science

- **Mashal.** A ship crosses the river from west to east, and a man walks inside it from east to west. He moves two ways at once, by the ship and by his own feet.
- **Nimshal.** In astronomy, a sphere can have its own motion while carried by another; the Tzemach Tzedek uses it to test the philosophers' arguments about the heavens.
- **Parts.** the ship → the outer sphere; the walker → the inner sphere; two motions → combined movements.
- **Breaks** [stated]. Stated: the parable fails if the spheres are fused together like one body, 'like a man chained to the ship's walls'.
- **Principles.** PR-L07, PR-L03
- **Source.** Sefer HaChakirah (Tzemach Tzedek), `Chassidus-txt/R. Menachem Mendel Schneersohn (Tzemach Tzedek) (1789-1866)/Sefer HaChakirah (Lubavitch, c. 1840s).txt` line 63: «והמשל משל נמרץ. הנה ספינה אחת עוברת את הנהר ממערב למזרח» (and the parable is a strong parable: a ship crossing the river from west to east).
- **Recurs.** philosophical sources cited in Sefer HaChakirah.
- **Guide.** You can be carried one way and walk another. Both motions are really yours.

#### SB2-TZ-28. The spring that never stops *Domain:* water; nature

- **Mashal.** Water from a spring is measured as it flows, but the spring itself never stops flowing from its source.
- **Nimshal.** G-d renews creation every moment, from nothing to something, without a pause, for six thousand years.
- **Parts.** the spring → G-d's creative power; each measured flow → each moment of the world; never stopping → constant renewal.
- **Breaks** [ours]. Ours: a spring can dry up; the nimshal cannot.
- **Principles.** PR-L04
- **Source.** Sefer HaChakirah (Tzemach Tzedek), `Chassidus-txt/R. Menachem Mendel Schneersohn (Tzemach Tzedek) (1789-1866)/Sefer HaChakirah (Lubavitch, c. 1840s).txt` line 598: «וה"ז כמשל הנביעה ממעיין שאין לו הפסק ממקורו» (and this is like the flowing of a spring that has no break from its source).
- **Recurs.** CHAK line 797; Maamarei 1855 lines 719-720; Maharash lines 7960, 8425.
- **See also in SB2.** SB2-TZ-15, SB2-TZ-17, SB2-TZ-18, SB2-TZ-19, SB2-MHS-10, SB2-RSB-26, SB2-RSB-37, SB2-RYZ-11, SB2-PIA-05.
- **Guide.** Right now, this moment is coming fresh from somewhere, like water from a spring that never stops.

## Rebbe Maharash (16)

#### SB2-MHS-01. The map and the land *Domain:* knowledge; nature

- **Mashal.** A map shows the whole earth, its seas, fields and trees, but in tiny form: one small sign stands for whole forests. The map is only a 'mashal' for the land itself.
- **Nimshal.** All of our world, and even its directions (south, north, up, down), is only a map, a mashal, for its roots above: south for kindness, and so on. And the Torah itself is 'the parable of the Ancient One'.
- **Parts.** the map → our world; the land → its spiritual source; a small sign for a forest → a creature for a divine attribute; reading the map → seeing the world as a parable of G-dliness.
- **Breaks** [stated + ours]. Stated: the map is 'not in proportion at all' to the land; so too the world to its source. Ours: a map is made after the land; the world is not drawn from a land we could ever visit.
- **Principles.** PR-L04, PR-L07, PR-L05
- **Source.** Toras Shmuel (Maharash), `Chassidus-txt/R. Shmuel Schneersohn (Rebbe Maharash) (1834-1882)/Toras Shmuel (Lubavitch, 1867-1881).txt` line 309: «והרי המפה היא רק משל לבד לגבי כללות הארץ וכל אשר עליה הימים» (and the map is only a parable, relative to the whole earth and all on it, the seas).
- **Recurs.** Maharash, Toras Shmuel lines 8047-8056 (everything below is a mashal for above); R. Aharon's 'the lower world is like the upper'; the Rebbe Rashab, Ayin Beis line 1094 ('the mashal is the nimshal').
- **See also in SB2.** SB2-RSB-02, SB2-TZ-26, SB2-RBE-13, SB2-RSB-16, SB2-MHS-02.
- **Guide.** Think of the world as a map. A map is not the place, but if you know how to read it, it takes you there.

#### SB2-MHS-02. Everything below is a mashal for above *Domain:* nature; the mashal itself

- **Mashal.** Day and night here (light and dark) are a picture of 'day and night' above. Moshe on the mountain knew day from night by the angels' song: 'holy' was day, 'blessed' was night.
- **Nimshal.** Whatever exists below is only a mashal for what is above it, and every level is a mashal for the next one up.
- **Parts.** day and night below → 'holy' and 'blessed' above; the lion below → the lion-face of the Chariot; each level → a parable of the level over it.
- **Breaks** [stated]. Stated: the lion of the attributes is only a 'mashal' to the lion of wisdom; they are 'beyond comparison'.
- **Principles.** PR-L04, PR-L05
- **Source.** Toras Shmuel (Maharash), `Chassidus-txt/R. Shmuel Schneersohn (Rebbe Maharash) (1834-1882)/Toras Shmuel (Lubavitch, 1867-1881).txt` line 8047: «שכל מה שנברא ונתהוה למטה הוא רק משל לגבי מה שלמעלה» (that whatever is created and comes into being below is only a parable relative to what is above).
- **Recurs.** TS lines 1787-1791, 3216, 3428, 8049-8056; Zohar 'the lower world is like the upper' (quoted by R. Aharon); Samach Vav line 3112 (Solomon's 3000 levels).
- **See also in SB2.** SB2-RSB-02, SB2-TZ-26, SB2-RBE-13, SB2-RSB-16, SB2-MHS-01.
- **Guide.** Day and night, warm and cold, near and far: each one is a hint of something more. Start noticing the hints.

#### SB2-MHS-03. A name is only for others *Domain:* the soul's faculties; speech

- **Mashal.** A person's name is only for others, so they can call him; for himself he does not need a name at all.
- **Nimshal.** All the worlds come only from His 'name', a mere glow, not His essence; the king's rule over his land is only his name spreading.
- **Parts.** the person → G-d; his name → the source of the worlds; others calling → the worlds' need for Him.
- **Breaks** [ours]. Ours: a person's name is given by others; His 'name' is His own choice to turn toward us (as the Tzemach Tzedek notes, DM line 287).
- **Principles.** PR-L06, PR-L09
- **Source.** Toras Shmuel (Maharash), `Chassidus-txt/R. Shmuel Schneersohn (Rebbe Maharash) (1834-1882)/Toras Shmuel (Lubavitch, 1867-1881).txt` line 710: «וכמשל ענין השם של האדם הוא רק לזולתו שיקראו אותו בשמו» (and like a person's name: it is only for others, that they may call him by his name).
- **Recurs.** Tzemach Tzedek, DM line 251 and 287; the Rebbe Rashab, Samach Vav line 2479; depths MH-C12.
- **See also in SB2.** SB2-TZ-04, SB2-TZ-05, SB2-RSB-14.
- **Guide.** Your name is for others. The real you doesn't need it. Maybe the whole world is just a name He answers to.

#### SB2-MHS-04. The mashal is higher than the idea *Domain:* the mashal itself; teacher and student

- **Mashal.** Only a very wise person can make good parables. Solomon, the wisest, spoke many; R. Meir, who 'lit up the eyes of the wise', spoke parables. So the mashal is higher than the plain idea, and that is why it can come down into a parable.
- **Nimshal.** The Torah is 'the parable of the Ancient One': a garment through which the Infinite can be grasped, and its root is higher than plain revelation.
- **Parts.** the wise maker of parables → the higher source; the parable → the Torah as garment; the plain idea → ordinary revelation.
- **Breaks** [stated]. Stated elsewhere (Maharash line 9401): the mashal is lower than the idea, yet not everyone can make one, which shows its root is higher.
- **Principles.** PR-L03, PR-L05, PR-L01
- **Source.** Toras Shmuel (Maharash), `Chassidus-txt/R. Shmuel Schneersohn (Rebbe Maharash) (1834-1882)/Toras Shmuel (Lubavitch, 1867-1881).txt` line 4369: «הרי מוכרח שהמשל גבוה מהשכל בעצמו ולכן נשפל במשל» (it must be that the mashal is higher than the intellect itself, and therefore it lowers itself into a parable).
- **Recurs.** R. Aharon's first condition (only one who knows the root can make a mashal); Tzemach Tzedek, Maamarei line 179; Rayatz, Sefer HaMaamarim line 582; depths MH-C21.
- **See also in SB2.** SB2-BST-30, SB2-MAG-24, SB2-TZ-22, SB2-RYZ-06, SB2-RBE-07, SB2-RBE-08, SB2-RSB-35.
- **Guide.** Simple pictures are not for simple minds. It takes deep understanding to find the right picture.

#### SB2-MHS-05. A home where the man himself lives *Domain:* house

- **Mashal.** A house is not just where a man's things or messages are; it is where he himself lives, with all of himself.
- **Nimshal.** 'A dwelling in the lowest world' means G-d's very essence revealed here, not only His glow; heaven and earth being filled with Him is still hidden.
- **Parts.** the house → this world; the man living in it → His essence; his things or glow → partial revelations.
- **Breaks** [ours]. Ours: a man can leave his house; G-d's dwelling is meant to be permanent.
- **Principles.** PR-L04, PR-L06
- **Source.** Toras Shmuel (Maharash), `Chassidus-txt/R. Shmuel Schneersohn (Rebbe Maharash) (1834-1882)/Toras Shmuel (Lubavitch, 1867-1881).txt` line 7777: «כמשל הדירה בגשמי' שעצמיות האדם דר בהבית» (like a physical dwelling, where the person's very self dwells in the house).
- **Recurs.** Midrash Tanchuma (dwelling below); Tanya ch. 36; the Rebbe, Melukat lines 456, 2487; depths MH-C13.
- **See also in SB2.** SB2-RBE-01, SB2-RYZ-04, SB2-PIA-09.
- **Guide.** Make your life a place where something real can actually live, not just visit.

#### SB2-MHS-06. The child on his father's shoulders *Domain:* father and son

- **Mashal.** A son riding on his father's shoulders asked passers-by, 'Have you seen my father?' The father set him down, a dog came and bit him.
- **Nimshal.** Israel, carried by G-d out of Egypt, asked 'Is G-d among us or not?' and right away Amalek came.
- **Parts.** the father → G-d; riding on the shoulders → being carried by miracles; asking 'where is my father' → doubt while held; the dog → Amalek.
- **Breaks** [ours]. Ours: the father 'throws down' the son as a lesson; the Maharash explains the doubt itself, not that G-d punishes questions.
- **Principles.** PR-L04
- **Source.** Toras Shmuel (Maharash), `Chassidus-txt/R. Shmuel Schneersohn (Rebbe Maharash) (1834-1882)/Toras Shmuel (Lubavitch, 1867-1881).txt` line 480: «משל לבן שהי' מורכב על כתפו של אביו ושאל» (like a son riding on his father's shoulder who asked).
- **Recurs.** Exodus Rabbah 26 (source); the Piaseczner, Derech HaMelech line 1059 ('a father who carries his son on his shoulders').
- **See also in SB2.** SB2-BST-20, SB2-MAG-03, SB2-RBE-03, SB2-RSB-06.
- **Guide.** Sometimes we ask 'where is he?' while we are being carried. Look down and see whose shoulders you are on.

#### SB2-MHS-07. The bird that speaks before the king *Domain:* king and kingdom; animals

- **Mashal.** A bird that speaks before the king, even nonsense, gives him more delight than all the ministers' fine poems, because it is a new thing.
- **Nimshal.** The service of souls in bodies, struggling below, moves the King more than the angels' steady praise.
- **Parts.** the bird → the person in a body; its awkward words → human prayer; the ministers' poems → angels' praise; the king's delight → G-d's pleasure in the new thing.
- **Breaks** [ours]. Ours: the bird doesn't know what it says; a person can.
- **Principles.** PR-L04
- **Source.** Toras Shmuel (Maharash), `Chassidus-txt/R. Shmuel Schneersohn (Rebbe Maharash) (1834-1882)/Toras Shmuel (Lubavitch, 1867-1881).txt` line 878: «כמשל הנ"ל מצפור המדברת שע"י הדבר חידוש מעורר לב המלך» (like the parable above, of the speaking bird: through the novelty it wakes the king's heart).
- **Recurs.** Maggid Devarav LeYaakov line 157; Keter Shem Tov line 496 (same); TS lines 1198, 1441.
- **Guide.** Your clumsy words can matter more than polished ones, because they come from a hard place.

#### SB2-MHS-08. The prisoner in the dark *Domain:* captivity; light

- **Mashal.** A man sitting in a dark prison, when someone brings him a candle, rushes toward it with longing.
- **Nimshal.** In exile the soul hurries toward the light from above: the 'haste' of leaving Egypt.
- **Parts.** the prisoner → the soul in exile; the dark cell → the hidden state; the candle → a revelation; rushing → the urgency of redemption.
- **Breaks** [stated + ours]. Ours: the prisoner can't make the candle; the stated nimshal has the haste on both sides, above and below.
- **Principles.** PR-L04, PR-L09
- **Source.** Toras Shmuel (Maharash), `Chassidus-txt/R. Shmuel Schneersohn (Rebbe Maharash) (1834-1882)/Toras Shmuel (Lubavitch, 1867-1881).txt` line 1917: «והרי הוא כמשל מי שיושב בבית האסורים בחשך» (and it is like one who sits in prison in darkness).
- **Recurs.** Rayatz, Sefer HaMaamarim line 13 (the condemned man's cry); TS line 9241 (the merchant who left at night).
- **Guide.** When you've been in the dark a long time, even a small light pulls you hard. Let it.

#### SB2-MHS-09. Treasure locked in a chest *Domain:* commerce; wealth

- **Mashal.** A person has great wealth hidden in a chest. He doesn't see it and doesn't carry it, but it is there.
- **Nimshal.** All the light drawn down by Torah and mitzvos now is real, though hidden; in the future it will be revealed below.
- **Parts.** the chest → the hidden worlds; the wealth → the effects of good deeds; not seeing it → the hiddenness now; opening it → the future redemption.
- **Breaks** [ours]. Ours: the owner put the wealth in himself; we don't see where our deeds go.
- **Principles.** PR-L04
- **Source.** Toras Shmuel (Maharash), `Chassidus-txt/R. Shmuel Schneersohn (Rebbe Maharash) (1834-1882)/Toras Shmuel (Lubavitch, 1867-1881).txt` line 2146: «וה"ז כמשל מי שיש לו עושר מופלג והוא גנוז בתיבה» (and this is like one who has great wealth hidden in a chest).
- **Recurs.** Tzemach Tzedek, DM line 97 and Sefer HaChakirah line 617; Tanya ch. 33.
- **See also in SB2.** SB2-TZ-10, SB2-MHS-11, SB2-RSB-23.
- **Guide.** Good you did that you can't see is not gone. It is put away somewhere safe.

#### SB2-MHS-10. The dry river dug deeper *Domain:* water; nature

- **Mashal.** When a river stops flowing, you have to dig it out deeper to bring the water back.
- **Nimshal.** After a flaw, one has to draw G-d's Name again from a deeper place: 'From the depths I call You.'
- **Parts.** the river → the flow of divine life; stopping → the damage of sin; digging deeper → teshuvah from the depths.
- **Breaks** [ours]. Ours: digging is physical labor; teshuvah is inner.
- **Principles.** PR-L04, PR-L09
- **Source.** Toras Shmuel (Maharash), `Chassidus-txt/R. Shmuel Schneersohn (Rebbe Maharash) (1834-1882)/Toras Shmuel (Lubavitch, 1867-1881).txt` line 2451: «וכמשל הנהר שנפסקי' מימיו צריכים לחפור אותו בעומק יותר» (and like the river whose waters stopped, which must be dug more deeply).
- **Recurs.** Rayatz, Sefer HaMaamarim line 1079 (digging a well); the Rebbe Rashab on teshuvah.
- **See also in SB2.** SB2-TZ-15, SB2-TZ-17, SB2-TZ-18, SB2-TZ-19, SB2-TZ-28, SB2-RSB-26, SB2-RSB-37, SB2-RYZ-11, SB2-PIA-05.
- **Guide.** If what used to flow has stopped, don't just wait. Dig deeper than before.

#### SB2-MHS-11. Praising a millionaire for a silver coin *Domain:* commerce; praise

- **Mashal.** If someone owns a million gold coins and you praise him for having silver, it is an insult.
- **Nimshal.** Praising G-d for the miracle of splitting the sea as 'might' falls short; next to His real greatness it is nothing.
- **Parts.** the millionaire → G-d; the silver coin → the revealed miracle; the insult → praise that limits Him.
- **Breaks** [ours]. Ours: the rich man has a real amount; His greatness has no amount at all.
- **Principles.** PR-L06, PR-L12
- **Source.** Toras Shmuel (Maharash), `Chassidus-txt/R. Shmuel Schneersohn (Rebbe Maharash) (1834-1882)/Toras Shmuel (Lubavitch, 1867-1881).txt` line 7840: «וכמשל מי שיש לו אלף אלפי' דינרי זהב, ומשבחי' אותו בשל כסף» (and like one who has a million gold coins, and they praise him for silver).
- **Recurs.** Talmud, Berachos 33b (source parable).
- **See also in SB2.** SB2-TZ-10, SB2-MHS-09, SB2-RSB-23.
- **Guide.** Sometimes the nicest thing you can say about something great still makes it smaller. Then quiet is better praise.

#### SB2-MHS-12. Bowing very close to the king *Domain:* king and kingdom; body

- **Mashal.** One who bows right before the king, very close, loses any sense of himself because of the closeness; the farther away, the more he feels himself.
- **Nimshal.** True self-nullification comes from being near; the further from the Source, the stronger the sense of self.
- **Parts.** bowing close → full bittul; distance → self-feeling; the king → G-d's creative power.
- **Breaks** [ours]. Ours: some people bow close and feel more, not less; the nimshal is about a state, not a posture.
- **Principles.** PR-L04, PR-L09
- **Source.** Toras Shmuel (Maharash), `Chassidus-txt/R. Shmuel Schneersohn (Rebbe Maharash) (1834-1882)/Toras Shmuel (Lubavitch, 1867-1881).txt` line 7946: «כמשל המשתחוה לפני המלך בקרוב מאד שיהי' בו ביטול הרגש עצמותו מכל וכל מפני הקירוב» (like one who bows before the king very closely, so that his sense of self is entirely nullified because of the closeness).
- **Recurs.** Maggid Devarav LeYaakov line 238; the Rebbe Rashab, Samach Vav line 4477.
- **See also in SB2.** SB2-MAG-20, SB2-MAG-21, SB2-TZ-11, SB2-TZ-13, SB2-RSB-07, SB2-RSB-24, SB2-RYZ-17.
- **Guide.** When you stand near something huge, your own size stops mattering. That isn't loss; it's relief.

#### SB2-MHS-13. The merchant who left the inn at night *Domain:* commerce; travel

- **Mashal.** A merchant left the inn at night in a hurry; the innkeeper made claims against him. He swore never to leave at night again.
- **Nimshal.** Israel left Egypt 'in haste' and so Egypt chased them; the future redemption will not be in haste.
- **Parts.** the merchant → Israel; leaving at night in haste → the Exodus; the innkeeper's claim → Egypt's pursuit; never again at night → the calm final redemption.
- **Breaks** [ours]. Ours: the merchant was in the wrong; the nimshal is about the nature of the redemption, not guilt.
- **Principles.** PR-L04
- **Source.** Toras Shmuel (Maharash), `Chassidus-txt/R. Shmuel Schneersohn (Rebbe Maharash) (1834-1882)/Toras Shmuel (Lubavitch, 1867-1881).txt` line 9241: «כי בחפזון יצאת, כמשל הסוחר שיצא מהפונדק בלילה» ('for in haste you went out', like the merchant who left the inn at night).
- **Recurs.** TS line 9638; Midrash (source).
- **Guide.** Leaving something in a rush often means it follows you. When you can, leave calmly and fully.

#### SB2-MHS-14. Crumbs from the king's feast *Domain:* king and kingdom; food

- **Mashal.** The leftover crumbs from a great king's feast are a big gift for poor people, because of how rich the feast was.
- **Nimshal.** Because all is as nothing before Him, even the outermost leftovers of His flow are abundant; so even the unworthy receive much, though only the outside of it.
- **Parts.** the feast → G-d's flow; the crumbs → the 'back side' that reaches the husks; abundance → His greatness.
- **Breaks** [stated]. Stated: they receive only 'the dregs and outer side', never His glory.
- **Principles.** PR-L04
- **Source.** Toras Shmuel (Maharash), `Chassidus-txt/R. Shmuel Schneersohn (Rebbe Maharash) (1834-1882)/Toras Shmuel (Lubavitch, 1867-1881).txt` line 3317: «כמשל הידוע שפירורי הפקר דסעודה שעושה המלך ברוממותו לשפע רב יחשב» (like the known parable: the stray crumbs of a feast the king makes in his greatness count as great abundance).
- **Recurs.** the Rebbe Rashab, Kuntres U'Maayan line 131 (the king's feast and the leftovers); TS line 6472.
- **Guide.** Even leftovers from something truly generous can feed you. And there is always more at the real table.

#### SB2-MHS-15. The dream that clears the mind *Domain:* body; sleep

- **Mashal.** All night a dreamer's mind throws off its waste in dreams; in the morning, the mind shines stronger.
- **Nimshal.** Exile is like a dream; through it, the 'health' of the redemption is drawn, and the mind of the soul will shine more after.
- **Parts.** the night of dreaming → exile; dream images → confusion and waste; morning clarity → redemption.
- **Breaks** [ours]. Ours: not every dream clears the mind; the nimshal is a hope, not a law of nature.
- **Principles.** PR-L04, PR-L09
- **Source.** Toras Shmuel (Maharash), `Chassidus-txt/R. Shmuel Schneersohn (Rebbe Maharash) (1834-1882)/Toras Shmuel (Lubavitch, 1867-1881).txt` line 6082: «כמשל החולם חלום שהוא הדמיון שבשכל בחי' הפסולת שבו יוצאים כל הלילה» (like one who dreams a dream: the imagination in the intellect, its waste, comes out all night).
- **Recurs.** the Alter Rebbe (cited by the Maharash); Rayatz line 928 (exile as sleep).
- **Guide.** A confused time can be the mind clearing itself. Morning comes clearer for it.

#### SB2-MHS-16. Ten idlers who guard the town *Domain:* community; work

- **Mashal.** Ten men sit in the synagogue and do no work, yet by their merit the whole town is protected; their guarding is hidden.
- **Nimshal.** Higher levels (the sefiros of Yetzirah) seem idle from the world's work, yet they secretly sustain what acts below.
- **Parts.** the idlers → the higher levels; the town → the lower world; hidden guarding → unseen influence.
- **Breaks** [ours]. Ours: the town may never know who guards it; above, the influence is real but hidden.
- **Principles.** PR-L04
- **Source.** Toras Shmuel (Maharash), `Chassidus-txt/R. Shmuel Schneersohn (Rebbe Maharash) (1834-1882)/Toras Shmuel (Lubavitch, 1867-1881).txt` line 1757: «וה"ז כמשל עשרה בטלנים שבטלים ממלאכתן ויושבין בביהכנ"ס» (and this is like ten idlers who are free of work and sit in the synagogue).
- **Recurs.** Talmud, Megillah 5a (the ten batlanim).
- **Guide.** Some of what holds your life together does nothing you can see. Thank it anyway.

## Rebbe Rashab (38)

#### SB2-RSB-01. Breath in, breath out *Domain:* body; breath

- **Mashal.** In a person, at every moment life comes from the soul's source, and at once it goes back up, and new life comes again: like breathing.
- **Nimshal.** The life of all creatures 'runs and returns' (ratzo vashov): it is withdrawn and renewed each moment, and this pulse is the root of time.
- **Parts.** the breath → the divine life-force; breathing in and out → coming and withdrawing; each breath → each moment of existence.
- **Breaks** [ours]. Ours: breath is automatic and we can hold it; the divine renewal never pauses and is not mechanical.
- **Principles.** PR-L09, PR-L04
- **Source.** Hemshech Samach Vav (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Samach Vav (scans, OCR).txt` line 682 **OCR**: «וכמשל נשימת רוח החיים שבאדם, שבכל רגע נמשך החיות מן מקור נפשו» (like the breath of the spirit of life in a person: at every moment life is drawn from the source of his soul).
- **Recurs.** Tzemach Tzedek, DM lines 117, 277 (pulse); the Rebbe, Likkutei Sichos line 35739 (the one who blows); depths SV1-C07.
- **Guide.** Notice your breathing for a minute. Every breath is new, and every breath goes back. Life may come to you like that, fresh each moment.

#### SB2-RSB-02. The strong man and the stone *Domain:* war; strength

- **Mashal.** A strong man came to a town, and no one knew his strength. A clever man said: look at the stone he wrestles with and you'll know his power.
- **Nimshal.** 'The heavens tell the glory of G-d': from the size of the creation one can sense the power of the Creator.
- **Parts.** the strong man → G-d; the stone → heaven and earth; the clever man → the one who contemplates; knowing his strength → recognizing G-d's might.
- **Breaks** [ours]. Ours: a strong man's strength is limited by the stone; G-d's power is not measured by the world.
- **Principles.** PR-L04, PR-L03
- **Source.** Hemshech Samach Vav (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Samach Vav (scans, OCR).txt` line 884 **OCR**: «משל לגבור שנכנס למדינה ולא היו יודעין גבורתו» (like a strong man who entered a land, and they did not know his strength).
- **Recurs.** Midrash Tehillim 19 (source); Tzemach Tzedek, Maamarei line 431; Ayin Beis lines 772, 3996; Rayatz lines 613, 1327.
- **See also in SB2.** SB2-TZ-26, SB2-RBE-13, SB2-RSB-16, SB2-MHS-01, SB2-MHS-02.
- **Guide.** You can tell how strong someone is by what they carry. Look at what is holding up the world.

#### SB2-RSB-03. A gem that shines *Domain:* light and sun; stones

- **Mashal.** The sun is all light; that is what it is. A precious gem shines, but the gem itself is a stone, something other than its shine.
- **Nimshal.** G-d is not 'made of light' as the sun is; the gem fits better, because He is something beyond being a source of light.
- **Parts.** the gem → G-d's essence; its shine → the light; the sun → a wrong picture of Him as pure light.
- **Breaks** [stated]. Stated (Samach Vav line 2440): even the gem only has the power of shining, not light itself, and the Infinite is beyond both.
- **Principles.** PR-L06, PR-L07
- **Source.** Hemshech Samach Vav (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Samach Vav (scans, OCR).txt` line 2420 **OCR**: «דמשו"ז המשל דאבן טוב המאיר, יותר מכוון ממשל אור השמש» (for this reason the parable of the shining gem is more exact than the parable of sunlight).
- **Recurs.** Samach Vav line 2440; Ayin Beis lines 5401 (gem in Yetzirah); Tzemach Tzedek on the sun (DM line 252).
- **See also in SB2.** SB2-TZ-01, SB2-TZ-02, SB2-TZ-06, SB2-TZ-20, SB2-RSB-38, SB2-RYZ-01, SB2-RYZ-15, SB2-RBE-17.
- **Guide.** You shine, but you are more than your shine. So is the One who lights everything.

#### SB2-RSB-04. Letters joined in a word *Domain:* the soul's faculties: speech

- **Mashal.** Letters joined in a word, like ב-ר-ו-ך (Baruch), carry a meaning together. Taken apart, each letter loses the light it had in the word.
- **Nimshal.** In the higher worlds, all is joined in one meaning; when separated (as in the 'breaking'), each part is dim and needs to be rejoined.
- **Parts.** the word → unity of the lights; separate letters → separated beings; the lost meaning → the dimming of light.
- **Breaks** [stated]. Stated (Ayin Beis line 155): the parable needs adjusting, because lights also have inner and outer parts.
- **Principles.** PR-L09, PR-L04
- **Source.** Hemshech Samach Vav (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Samach Vav (scans, OCR).txt` line 2681 **OCR**: «המשל ע"ז כמו כמה אותיות מצורפים יחד בתיבה אחת» (the parable for this is like several letters joined together in one word).
- **Recurs.** Ayin Beis lines 147-167 (the letter ב of ברוך); Tanya.
- **See also in SB2.** SB2-MAG-15, SB2-MAG-17, SB2-TZ-16, SB2-TZ-21, SB2-RSB-10.
- **Guide.** Alone, a letter means little. Join it with others and it says something. So do you.

#### SB2-RSB-05. The seed has to rot first *Domain:* nature; plants

- **Mashal.** A seed sown in the ground can't sprout unless it first rots and is undone.
- **Nimshal.** Something new cannot come from something existing unless there is 'nothing' in between.
- **Parts.** the seed → what exists; rotting → passing through ayin; the sprout → the new reality.
- **Breaks** [ours]. Ours: a seed must decay by nature; a person must agree to let go.
- **Principles.** PR-L04, PR-L09
- **Source.** Hemshech Samach Vav (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Samach Vav (scans, OCR).txt` line 2683 **OCR**: «וכידוע* המשל ע"ז מזריעת הגרעין בארץ, דא"א להיות ממנו צמיחה אם לא שיורקב תחלה» (and, as is known, the parable for this is the sowing of the seed in the ground: no growth can come of it unless it first rots).
- **Recurs.** Maggid, MDL lines 115, 173; Samach Vav line 7230; Rayatz lines 1522, 1598.
- **See also in SB2.** SB2-MAG-11, SB2-MAG-12, SB2-TZ-09.
- **Guide.** Before something new grows in you, something old may have to come apart. That's not failure; it's how seeds work.

#### SB2-RSB-06. Dancers who step apart *Domain:* music and dance; love

- **Mashal.** Dancers facing each other step back, and the distance brings them closer in a truer way than if they had not stepped apart.
- **Nimshal.** Distance from G-d (the 'desert' of exile) leads to a deeper closeness: from complete distance comes complete nearness.
- **Parts.** the dancers → G-d and the soul; stepping apart → exile or hiding; coming together → the return and redemption.
- **Breaks** [ours]. Ours: dancers plan the step back; a person in distance doesn't feel any plan.
- **Principles.** PR-L04, PR-L09
- **Source.** Hemshech Samach Vav (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Samach Vav (scans, OCR).txt` line 3733 **OCR**: «וכידוע* במשל המרקדים זה כנגד זה, דבסיבת הריחוק יתקרבו אחר כך בקירוב אמיתי יותר» (as known from the parable of dancers facing each other: because of the distance, afterward they come closer in a truer closeness).
- **Recurs.** depths SV2-C07; Maggid MDL line 183; the Rebbe on exile and redemption.
- **See also in SB2.** SB2-BST-20, SB2-MAG-03, SB2-RBE-03, SB2-MHS-06.
- **Guide.** Sometimes stepping back is part of the dance. The distance can make the coming together truer.

#### SB2-RSB-07. Too close to speak *Domain:* king and kingdom; speech

- **Mashal.** One who stands very close before the king is so overwhelmed that he can't say a word.
- **Nimshal.** At the highest level of nearness to G-d, speech fails; 'there are no words on my tongue'.
- **Parts.** standing near the king → closeness to G-d; losing speech → bittul beyond words.
- **Breaks** [ours]. Ours: silence before a king can be fear; this silence is fullness.
- **Principles.** PR-L04, PR-L09
- **Source.** Hemshech Samach Vav (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Samach Vav (scans, OCR).txt` line 4477 **OCR**: «כמשל העומד לפני המלך בקירוב עצום, שמתבטל בעצם לגמרי מכל וכל, ולא יוכל» (like one standing before the king in great closeness, who is completely nullified, and cannot).
- **Recurs.** Maggid, MDL line 238; Maharash line 7946; Rayatz line 775.
- **See also in SB2.** SB2-MAG-20, SB2-MAG-21, SB2-TZ-11, SB2-TZ-13, SB2-MHS-12, SB2-RSB-24, SB2-RYZ-17.
- **Guide.** When something is too close and too big, you may go quiet. That quiet can be the deepest prayer.

#### SB2-RSB-08. The son who earns on his own *Domain:* father and son; commerce

- **Mashal.** A father is pleased when his son can support himself, more than with any wealth he could give him. More so if the son, far from home with nothing of his father's, earns by his own craft and grows richer than his father.
- **Nimshal.** Effort in Torah and service, especially when far away and in hiding, makes something new 'from nothing'; this pleases G-d more than gifts He gives.
- **Parts.** the father → G-d; the son's own earnings → a person's work; being far away → exile, the hidden state; new wealth → renewal from nothing.
- **Breaks** [ours]. Ours: a son's earnings are his own; in the nimshal even the power to earn comes from the Father.
- **Principles.** PR-L04, PR-L07
- **Source.** Hemshech Samach Vav (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Samach Vav (scans, OCR).txt` line 4601 **OCR**: «וכ"ש אם הבן מפרנס להאב מיגיע כפו בכלי אומנתו» (and all the more if the son supports the father by the toil of his hands with his craft).
- **Recurs.** Samach Vav lines 4610, 4621, 7423-7450; the Maggid on 'bread of shame'.
- **See also in SB2.** SB2-MAG-04, SB2-MAG-05, SB2-MAG-22, SB2-BST-13, SB2-BST-22, SB2-RYZ-10.
- **Guide.** What you build by your own effort, even far from home, can be a bigger gift than anything handed to you.

#### SB2-RSB-09. Refining silver in two stages *Domain:* craft; metal

- **Mashal.** To refine silver, first the coarse dross is removed, then the finer dross, until pure silver remains.
- **Nimshal.** There are two kinds of refinement in serving G-d: first the obvious, then the subtle.
- **Parts.** the silver → the soul's powers; coarse dross → obvious faults; fine dross → subtle self-interest; pure silver → the refined self.
- **Breaks** [ours]. Ours: silver doesn't feel the fire.
- **Principles.** PR-L04, PR-L09
- **Source.** Hemshech Samach Vav (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Samach Vav (scans, OCR).txt` line 4754 **OCR**: «והנה* המשל בב' מיני בירורים הנ"ל ידוע עד"מ בצירוף הכסף» (the parable for the two kinds of refinement is known, as in the refining of silver).
- **Recurs.** Samach Vav line 7435; Rayatz line 505 (silver mixed).
- **Guide.** Getting better happens in rounds: first the obvious stuff, then the quiet stuff underneath.

#### SB2-RSB-10. Thought passing through the finger *Domain:* the soul's faculties; writing

- **Mashal.** When you write down an idea, the light of the idea passes through your finger, and the idea does not change at all.
- **Nimshal.** When a higher level only 'passes through' a lower one, it stays the same; when it settles into it, it takes on the lower nature.
- **Parts.** the idea → the higher light; the finger → the lower level it passes through; writing → the effect.
- **Breaks** [stated]. Stated: unlike 'enclothing', where the thought becomes feelings and changes.
- **Principles.** PR-L09, PR-L04
- **Source.** Hemshech Samach Vav (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Samach Vav (scans, OCR).txt` line 5096 **OCR**: «והמשל בזה, כמו אור השכל העובר דרך האצבע בכתיבת איזה שכל» (and the parable: like the light of the intellect passing through the finger in writing some idea).
- **Recurs.** Tzemach Tzedek, DM line 112 (writing with the finger).
- **See also in SB2.** SB2-MAG-15, SB2-MAG-17, SB2-TZ-16, SB2-TZ-21, SB2-RSB-04.
- **Guide.** Some things pass through you and leave you the same. Some settle in and change you. Notice which is which.

#### SB2-RSB-11. The stone thrown upward *Domain:* nature; motion

- **Mashal.** A stone thrown up keeps going only while the thrower's force is in it; when the force stops, it falls.
- **Nimshal.** Anything renewed from nothing needs its Maker in it every moment; without Him it would drop back to nothing.
- **Parts.** the thrower's force → the creative power; the stone in the air → the world; falling → returning to nothing.
- **Breaks** [stated]. Stated in the Alter Rebbe (Tanya, Shaar HaYichud ch. 2): the stone's rising is against nature, while creation from nothing is far more.
- **Principles.** PR-L04, PR-L07
- **Source.** Hemshech Samach Vav (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Samach Vav (scans, OCR).txt` line 5251 **OCR**: «וכידוע המשל ע"ז מזריקת האבן מלמטה למעלה» (and the known parable for this is throwing a stone from below upward).
- **Recurs.** Tanya, Shaar HaYichud ch. 2 (source); Rayatz lines 176, 194, 1042, 1649.
- **See also in SB2.** SB2-TZ-03, SB2-TZ-12, SB2-RSB-13, SB2-RSB-30, SB2-RSB-34.
- **Guide.** Whatever keeps you up right now is not leftover force from long ago. It is being given now.

#### SB2-RSB-12. Hairs that grow through the skull *Domain:* body

- **Mashal.** Hairs draw life from the brain, but through the barrier of the skull, so their life is very small: you can cut them without pain.
- **Nimshal.** Some divine flows come only by 'leaping' a barrier, reaching far below with a tiny trace of the source.
- **Parts.** the brain → the inner source; the skull → the barrier (tzimtzum); the hair → the far-reaching thin flow.
- **Breaks** [ours]. Ours: hair is almost dead; the flow below is still divine.
- **Principles.** PR-L04, PR-L09
- **Source.** Hemshech Samach Vav (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Samach Vav (scans, OCR).txt` line 5556 **OCR**: «וכידוע המשל בזה*"י מהמשכת השערות דרך הפסק עצם הגולגלת» (and the known parable for this is the drawing of the hairs through the break of the skull-bone).
- **Recurs.** Tzemach Tzedek, DM lines 89, 189, 255; Ayin Beis line 69; the Rebbe, Melukat line 1164.
- **Guide.** Even the thinnest thread of life still comes from the center.

#### SB2-RSB-13. The lever lifts from below *Domain:* tools; craft

- **Mashal.** To lift something with a lever, you have to put it under the very bottom of the load.
- **Nimshal.** A person was made with the highest soul and lowest body, so he can lift all creation from the bottom; and the deed is what lifts all the soul's powers.
- **Parts.** the lever → the soul in a body; the bottom of the load → the physical world; lifting → elevating everything.
- **Breaks** [ours]. Ours: a lever is a machine; the soul has to want to lift.
- **Principles.** PR-L04
- **Source.** Hemshech Samach Vav (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Samach Vav (scans, OCR).txt` line 5909 **OCR**: «כשצריכים להגביה איזה דבר מן הארץ ע"י כלי ההגבהה הנק' ליווער» (when one needs to lift something from the ground by the lifting tool called a lever).
- **Recurs.** Samach Vav line 7549; Ayin Beis line 1442; the Rebbe, Melukat lines 1076, 1647, 2484, 2698; depths SV3-C24.
- **See also in SB2.** SB2-TZ-03, SB2-TZ-12, SB2-RSB-11, SB2-RSB-30, SB2-RSB-34.
- **Guide.** To lift something heavy, you start at the bottom. Your plain daily deeds are the place to start.

#### SB2-RSB-14. The king is not his kingship *Domain:* king and kingdom

- **Mashal.** A human king is a person in himself. Being called king over countries doesn't spread his essence there; only his name is called over them.
- **Nimshal.** G-d's kingship over the worlds is their life, but it does not touch His essence.
- **Parts.** the king → G-d's essence; being called king → malchus; his name over the land → the life in the worlds.
- **Breaks** [ours]. Ours: a king needs a people to be a king; G-d does not need the worlds.
- **Principles.** PR-L06, PR-L07
- **Source.** Hemshech Samach Vav (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Samach Vav (scans, OCR).txt` line 6372 **OCR**: «כמשל המלך ב"ויי, שהוא מהות בפ"ע, ומה שנקרא מלך על המדינות» (like a human king, who is an entity in himself, and that he is called king over the lands).
- **Recurs.** Maharash line 710; Tzemach Tzedek DM line 251.
- **See also in SB2.** SB2-TZ-04, SB2-TZ-05, SB2-MHS-03.
- **Guide.** Your roles are real, but you are more than them. So is He.

#### SB2-RSB-15. Wanting without a reason you can give *Domain:* the soul's faculties: will

- **Mashal.** When someone wants something and has no reason he can explain, he does have a reason inside, more like a taste than a thought. He can't show it to anyone, so he says 'that's what I want'.
- **Nimshal.** The hidden 'reason' in the crown (keser) can never come out as revealed wisdom; it is a reason above reason.
- **Parts.** the wanting → the will above wisdom; the hidden taste → the concealed reason; 'that's my will' → the decree beyond explanation.
- **Breaks** [ours]. Ours: a person's hidden taste might be found later; the highest reason never becomes reason.
- **Principles.** PR-L09, PR-L12
- **Source.** Hemshech Samach Vav (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Samach Vav (scans, OCR).txt` line 4988 **OCR**: «כשירצה אדם באיזה דבר, ואין לו טעם גלוי ע"ז למה ירצה כך» (when a person wants something and has no revealed reason why he wants it).
- **Recurs.** Ayin Beis (will and pleasure, depths AB1-C1).
- **Guide.** Some of your deepest wants can't be explained. That doesn't mean they have no reason; the reason is just deeper than words.

#### SB2-RSB-16. The world is the parable itself *Domain:* the mashal itself; nature

- **Mashal.** Every physical thing is a parable for the divine power behind it. When a person finds all the details of the meaning in the parable, the parable becomes clear and looks to him like divine power itself.
- **Nimshal.** 'The mashal is the nimshal': the world, rightly seen, does not hide G-d but shows Him.
- **Parts.** the physical thing → the mashal; the divine force → the nimshal; studying the details → contemplation; the mashal becoming clear → seeing G-dliness in the world.
- **Breaks** [stated]. Stated (Ayin Beis line 1549): even refined, it still comes to us through physical images, so it remains a kind of corporeality.
- **Principles.** PR-L04, PR-L01, PR-L09
- **Source.** Hemshech Ayin Beis (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Ayin Beis (Lubavitch and Rostov, 1912-1916).txt` line 1094: «והיינו שכל הדברים הגשמי' הן כמו משל אל הנמשל להכח האלקי, והמשל הוא הנמשל ממש» (that is, all physical things are like a parable for the nimshal, the divine power, and the parable is the nimshal itself).
- **Recurs.** Ayin Beis lines 1549-1551, 1849 ('in truth the mashal is the nimshal; that is "from my flesh"'); Samach Vav line 2938; depths AB1-C6; Maharash line 309.
- **See also in SB2.** SB2-RSB-02, SB2-TZ-26, SB2-RBE-13, SB2-MHS-01, SB2-MHS-02.
- **Guide.** Look at something ordinary for a long while. It may stop hiding what is behind it, and start showing it.

#### SB2-RSB-17. The king's daughter and the pot scrapings *Domain:* king and kingdom; food

- **Mashal.** A princess, used to the finest foods, smelled the spicy scrapings at the bottom of a pot. If she says she wants them, it's a shame; if she doesn't, it pains her. So her servants brought them to her quietly.
- **Nimshal.** The Shechinah 'desires' the sharp, refined taste that comes from sorting the physical world; so we say 'Blessed be the name of His kingdom' quietly.
- **Parts.** the princess → malchus, the Shechinah; the fine foods → angels' praise; the pot scrapings → the birurim of the physical; bringing it quietly → saying Baruch Shem in a whisper.
- **Breaks** [ours]. Ours: the princess has a craving; G-d has no lack.
- **Principles.** PR-L04, PR-L07
- **Source.** Hemshech Ayin Beis (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Ayin Beis (Lubavitch and Rostov, 1912-1916).txt` line 1760: «משל לבת מלך שהריחה ציקי קדרה תאמר יש לה גנאי» (like a king's daughter who smelled the scrapings of a pot; if she says so, it is a shame).
- **Recurs.** Talmud, Pesachim 56a (source); Kuntres Eitz HaChaim lines 241-251; Maggid, MDL line 136; depths RK-C05.
- **Guide.** The sharp, real taste of ordinary struggle may be wanted more than polished perfection. You don't have to announce it.

#### SB2-RSB-18. The interpreter in between *Domain:* teacher and student; speech

- **Mashal.** In the days of the sages, a great teacher's words were too far above the people, so an interpreter heard him and passed it on in terms the people could take in.
- **Nimshal.** Some intermediaries connect without separating: they receive from above and give below in a way the receiver can hold.
- **Parts.** the teacher → the higher level; the interpreter → a connecting middle (malchus); the people → the lower worlds.
- **Breaks** [stated]. Stated: unlike a rope held by two people, which joins them but also stands between them.
- **Principles.** PR-L04, PR-L14
- **Source.** Hemshech Ayin Beis (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Ayin Beis (Lubavitch and Rostov, 1912-1916).txt` line 1782: «וידוע המשל בזה כמו המתורגמן שבין המשפיע להמקבל» (and the known parable is like the interpreter between the giver and the receiver).
- **Recurs.** Ayin Beis line 3354.
- **See also in SB2.** SB2-MAG-01, SB2-MAG-02, SB2-MAG-10, SB2-RBE-08, SB2-PIA-07.
- **Guide.** Sometimes you need someone in between who speaks both languages. That person doesn't separate you; they connect you.

#### SB2-RSB-19. Lost in a beautiful picture *Domain:* perception; art

- **Mashal.** When a person looks at a beautiful picture, his soul attaches to it until all his senses are lost in it.
- **Nimshal.** Wisdom (chochmah) is seeing, and seeing unites: this is why wisdom brings total self-nullification.
- **Parts.** the picture → the divine light seen in wisdom; losing oneself → bittul; sight → chochmah.
- **Breaks** [ours]. Ours: one can be lost in a picture and still be self-centered; the stated bittul is complete.
- **Principles.** PR-L09, PR-L04
- **Source.** Hemshech Ayin Beis (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Ayin Beis (Lubavitch and Rostov, 1912-1916).txt` line 2104: «וכידוע המשל מהראי' באיזה דבר כמו באיזה ציור נאה שמתאחד ונדבק נפשו בזה» (and as known, the parable of seeing something, like a beautiful picture, with which one's soul unites and clings).
- **Recurs.** Ayin Beis line 2835 (sight reaches the physical); Tanya ch. 'sight'.
- **Guide.** When you really look at something beautiful, you forget yourself for a moment. That forgetting can be a door.

#### SB2-RSB-20. A wick that won't hold the flame *Domain:* fire

- **Mashal.** A wick that stays solid and doesn't burn away can't hold the flame; the fire jumps and leaves it. The right wick and oil are those that are used up by the flame.
- **Nimshal.** A vessel that is too much its own 'something' can't hold the light; the vessels broke because they lacked bittul.
- **Parts.** the wick → the vessel; the flame → the light; not burning → too much self; the flame leaping off → the light departing.
- **Breaks** [ours]. Ours: a wick has no choice; the soul can learn to give way.
- **Principles.** PR-L04, PR-L09
- **Source.** Hemshech Ayin Beis (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Ayin Beis (Lubavitch and Rostov, 1912-1916).txt` line 2416: «וכמשל הפתילה שהיא קיימת בישותה והאור בלתי מתיישב בהפתילה» (like the wick that stays in its existence, and the light does not settle on the wick).
- **Recurs.** Ayin Beis line 2423; Rayatz line 259 (lamp: oil and wick); the Piaseczner, Derech HaMelech line 169.
- **See also in SB2.** SB2-BST-04, SB2-BST-23, SB2-RSB-21, SB2-RYZ-03, SB2-RYZ-13, SB2-PIA-11, SB2-PIA-12, SB2-PIA-13.
- **Guide.** If you hold yourself too tightly, light has nowhere to rest on you. Let a little of yourself burn.

#### SB2-RSB-21. Ash: what remains after the fire *Domain:* fire; nature

- **Mashal.** When wood burns, three elements go up in the fire and the ash remains; the ash is the essence of the wood.
- **Nimshal.** The animal soul at its core is only a power of desire; burning away its bad forms leaves an essence that can want G-d.
- **Parts.** the wood → the animal soul; burning → offering, refining; the ash → its pure essence.
- **Breaks** [ours]. Ours: ash is lifeless; the essence left in the soul is alive.
- **Principles.** PR-L04
- **Source.** Hemshech Ayin Beis (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Ayin Beis (Lubavitch and Rostov, 1912-1916).txt` line 3613: «ועד"מ עץ ששורפין באש הוא שהג' יסודות נשרפין ויוצאין בהאש ונשאר האפר» (and like wood burned in fire: the three elements burn and go out in the fire, and the ash remains).
- **Recurs.** Ayin Beis line 186 (the red heifer's ash).
- **See also in SB2.** SB2-BST-04, SB2-BST-23, SB2-RSB-20, SB2-RYZ-03, SB2-RYZ-13, SB2-PIA-11, SB2-PIA-12, SB2-PIA-13.
- **Guide.** When the fire is over, what stays is the real you. That part can still want good things.

#### SB2-RSB-22. One foot always on the ground *Domain:* body; motion

- **Mashal.** A person walking keeps one foot on the ground while lifting the other; even a runner always has one foot touching earth.
- **Nimshal.** Even when G-d 'skips' and leaps (the line of light), He stays clothed in the lowest levels.
- **Parts.** walking → divine descent; the foot on the ground → presence in the lowest worlds; the lifted foot → the leap above.
- **Breaks** [ours]. Ours: walking is in space; the nimshal is not spatial.
- **Principles.** PR-L04, PR-L09
- **Source.** Hemshech Ayin Beis (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Ayin Beis (Lubavitch and Rostov, 1912-1916).txt` line 3694: «ועד"מ מי שהוא הולך כדרכו גופו עומד על הארץ ממש» (like one who walks in his usual way: his body stands on the ground itself).
- **Recurs.** Ayin Beis line 3695.
- **Guide.** Even when you leap ahead, keep one foot on the ground. So does everything good.

#### SB2-RSB-23. Admitting your friend is right *Domain:* friendship; speech

- **Mashal.** A person admits to his friend that the friend is right and not as he thought until now.
- **Nimshal.** Hoda'ah (acknowledgment) is admitting a truth above one's understanding: knowing that it is so without knowing what it is.
- **Parts.** the friend → G-d's truth; admitting → bowing of the mind; 'not as I thought' → beyond understanding.
- **Breaks** [ours]. Ours: a friend can explain himself; here the truth stays beyond reach.
- **Principles.** PR-L12, PR-L09
- **Source.** Hemshech Ayin Beis (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Ayin Beis (Lubavitch and Rostov, 1912-1916).txt` line 3715: «וכמשל אדם המודה לחברו שעמו האמת ולא כמו שנדמה לו עד עתה» (like a person who admits to his friend that the truth is with him and not as it seemed to him until now).
- **Recurs.** Tzemach Tzedek, DM line 138 (great king and pauper); the Modim blessing.
- **See also in SB2.** SB2-TZ-10, SB2-MHS-09, SB2-MHS-11.
- **Guide.** Saying 'you were right and I didn't see it' can open more than any proof.

#### SB2-RSB-24. The commoner who sees the ministers bow *Domain:* king and kingdom

- **Mashal.** A simple man seeing the king doesn't grasp his greatness, but when he sees great ministers and nobles bow to the king, awe falls on him too.
- **Nimshal.** Contemplating how the angels, who see G-d, are nullified before Him brings awe even to the animal soul.
- **Parts.** the commoner → the animal soul; the ministers bowing → angels' bittul; awe falling → the body's fear of G-d.
- **Breaks** [ours]. Ours: he reasons from others; the angels' awe is real knowledge.
- **Principles.** PR-L04
- **Source.** Hemshech Ayin Beis (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Ayin Beis (Lubavitch and Rostov, 1912-1916).txt` line 4056: «וה"ז כמשל איש המוני כשרואה את המלך הנה להיותו המוני אינו מבין כ"כ גדולת המלך» (and this is like a simple man who sees the king: being simple, he does not understand the king's greatness so much).
- **Recurs.** Maharash line 6112 (same); Tanya ch. 'the angels'.
- **See also in SB2.** SB2-MAG-20, SB2-MAG-21, SB2-TZ-11, SB2-TZ-13, SB2-MHS-12, SB2-RSB-07, SB2-RYZ-17.
- **Guide.** If you can't feel something great yourself, watch the people who do. Their awe can teach you.

#### SB2-RSB-25. The sealed flask of perfume *Domain:* nature; scent

- **Mashal.** A flask of perfume, sealed and lying in a corner, gives off no smell; when you move it around, its fragrance spreads.
- **Nimshal.** 'Go forth': Avraham was told to move from place to place so that G-d's name would spread; moving draws the hidden light out.
- **Parts.** the flask → the soul or Avraham; sealed in a corner → staying put; moving it → going out; the scent → G-dliness revealed.
- **Breaks** [ours]. Ours: the perfume loses some of itself; the soul gains by going.
- **Principles.** PR-L04
- **Source.** Hemshech Ayin Beis (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Ayin Beis (Lubavitch and Rostov, 1912-1916).txt` line 4648: «משל לצלוחית של אפופולסימון שהיתה מוקפת צמיד פתיל ומונחת בקרן זוית» (like a flask of balsam, sealed and lying in a corner).
- **Recurs.** Genesis Rabbah 39 (source); Ayin Beis line 1816; Maharash line 7579.
- **Guide.** Something good kept sealed in a corner stays hidden. Move, go out, and it spreads.

#### SB2-RSB-26. The river overflowing its banks *Domain:* water

- **Mashal.** When rains and melting snow fill a river, it spreads over all its banks.
- **Nimshal.** When love of G-d is very strong, it spreads into all the powers of the soul, beyond its normal channel.
- **Parts.** the river → love; overflowing → filling all of one's powers.
- **Breaks** [ours]. Ours: a flood can harm; this overflow brings life.
- **Principles.** PR-L04, PR-L09
- **Source.** Hemshech Ayin Beis (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Ayin Beis (Lubavitch and Rostov, 1912-1916).txt` line 4829: «וכמ"ש במ"א המשל ע"ז כמו הנהר המתפשט על כל גדותיו מפני ריבוי הגשמים» (as explained elsewhere, the parable for this is like a river spreading over all its banks because of much rain).
- **Recurs.** Ayin Beis line 3984.
- **See also in SB2.** SB2-TZ-15, SB2-TZ-17, SB2-TZ-18, SB2-TZ-19, SB2-TZ-28, SB2-MHS-10, SB2-RSB-37, SB2-RYZ-11, SB2-PIA-05.
- **Guide.** When a feeling grows strong enough, it fills everything. Let it.

#### SB2-RSB-27. What your life depends on *Domain:* life and death

- **Mashal.** A person deepens his mind, heart and thought in something his life depends on, that touches his very soul.
- **Nimshal.** Inner love of G-d comes from deep thought, and the love in turn deepens the thought, as when life hangs on it.
- **Parts.** life-and-death matter → G-d; deep thought → contemplation; being touched → inner feeling.
- **Breaks** [ours]. Ours: fear for life is self-centered; this depth is for Him.
- **Principles.** PR-L09, PR-L13
- **Source.** Hemshech Ayin Beis (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Ayin Beis (Lubavitch and Rostov, 1912-1916).txt` line 4831: «ועד"מ כאדם המעמיק מוחו ולבו ומחשבתו בדבר שחייו תלוים בו» (like a person who deepens his mind, heart and thought in a matter on which his life depends).
- **Recurs.** Ayin Beis line 4837 (litigants before judges); the Rayatz (fleeing death).
- **Guide.** Think about this the way you'd think about something your life depends on. Maybe it does.

#### SB2-RSB-28. The judge is not moved *Domain:* law

- **Mashal.** A judge who rules 'guilty' or 'innocent' is not himself stirred by the judgment or by mercy.
- **Nimshal.** The philosophers' view: G-d is called merciful by His effects, not because He feels. The Rashab cites it and then says the truth is otherwise: there are real attributes in Atzilus.
- **Parts.** the judge → G-d per the philosophers; the verdict → the effect in the world; not being moved → no change in Him.
- **Breaks** [stated]. Stated: 'the truth is not so', for there are real sefiros of kindness and might; the judge parable is too cold.
- **Principles.** PR-L07, PR-L08
- **Source.** Hemshech Ayin Beis (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Ayin Beis (Lubavitch and Rostov, 1912-1916).txt` line 5557: «והמשל בזה כמו השופט שפוסק שזה חייב או זכאי אינו מתפעל בעצמו» (and the parable is like a judge who rules this one guilty or innocent and is not himself affected).
- **Recurs.** Maimonides, Guide I:54; Kuzari II; Ayin Beis line 2699.
- **Guide.** Fair isn't the same as cold. Real care can be steady and still feel.

#### SB2-RSB-29. Fruit from high up falls farther *Domain:* nature; plants

- **Mashal.** Fruit at the top of a tree, when it falls, lands farther from the tree than fruit from low branches.
- **Nimshal.** A higher soul, when it falls, falls lower; so a lack of love and awe in a high soul is more serious.
- **Parts.** the tree → the tree of souls; high fruit → a lofty soul; falling far → falling low.
- **Breaks** [ours]. Ours: fruit can't climb back; a soul can.
- **Principles.** PR-L04
- **Source.** Hemshech Ayin Beis (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Ayin Beis (Lubavitch and Rostov, 1912-1916).txt` line 589: «ועד"מ עץ פרי הרי הפירות שהן בגובה האילן כשנופלים על הארץ ה"ה נופלי' במרחק יותר» (like a fruit tree: the fruits at the top of the tree, when they fall, fall farther away).
- **Recurs.** Ayin Beis line 594; Rayatz line 1549 (stone at top of wall); Maharash lines 7870, 10190; the Rebbe, Melukat line 2616.
- **Guide.** If you fell far, it may be because you started high. That height is still yours.

#### SB2-RSB-30. The rope tied above *Domain:* tools; connection

- **Mashal.** A rope tied at its top end above and its bottom end below: shake the bottom and the top moves too.
- **Nimshal.** 'Jacob is the rope of His inheritance': what the souls do below moves things above.
- **Parts.** the rope → the soul; the top end → its root above; shaking the bottom → deeds below.
- **Breaks** [ours]. Ours: a rope is passive; souls choose.
- **Principles.** PR-L04
- **Source.** Hemshech Ayin Beis (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Ayin Beis (Lubavitch and Rostov, 1912-1916).txt` line 1395: «ועד"מ החבל שקצהו העליון קשור למע' וקצהו התחתון למטה» (like a rope whose upper end is tied above and its lower end below).
- **Recurs.** Deuteronomy 32:9; the Rebbe Rashab, Kuntres U'Maayan line 77; the Rebbe, Likkutei Sichos line 36517.
- **See also in SB2.** SB2-TZ-03, SB2-TZ-12, SB2-RSB-11, SB2-RSB-13, SB2-RSB-34.
- **Guide.** What you do down here pulls on something far above you. You are tied to it.

#### SB2-RSB-31. The craftsman who loves the work *Domain:* craft

- **Mashal.** A good craftsman making a vessel for his master works to make it beautiful, not just for the master's honor but for the pleasure he has in the thing itself.
- **Nimshal.** A Jew can delight in a mitzvah itself, without knowing what it is, because G-d's delight in it is his delight.
- **Parts.** the craftsman → the person doing a mitzvah; the beautiful vessel → the mitzvah done with care; his own pleasure → joy in the deed itself.
- **Breaks** [ours]. Ours: the craftsman knows the vessel's use; we often don't know a mitzvah's reason.
- **Principles.** PR-L04, PR-L09
- **Source.** Hemshech Ayin Beis (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Ayin Beis (Lubavitch and Rostov, 1912-1916).txt` line 1419: «והמשל בזה הוא כמו העבד העושה מלאכה להאדון כמו כלי וכה"ג שמהדר בהמלאכה» (and the parable is like a servant making work for his master, like a vessel, who beautifies the work).
- **Recurs.** the Rebbe on 'joy in a mitzvah'.
- **See also in SB2.** SB2-MAG-16, SB2-MAG-09, SB2-MAG-18, SB2-RSB-32.
- **Guide.** Do the thing well because you like doing it well. That pleasure counts.

#### SB2-RSB-32. Praising the axe instead of the builder *Domain:* craft

- **Mashal.** Someone who sees a magnificent building does not praise the axe that built it; he praises the craftsman, and the building is called by his name.
- **Nimshal.** The forces of nature are G-d's axe; praise belongs to Him, not to nature.
- **Parts.** the building → the world; the axe → nature; the craftsman → G-d.
- **Breaks** [ours]. Ours: an axe is a dead tool; nature is alive, though only by Him.
- **Principles.** PR-L04
- **Source.** Kuntres U'Maayan (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Kuntres Umaayan (Lubavitch, 1903).txt` line 476: «ועל דרך משל אדם הרואה בנין גדול ומפואר האם יעלה על הדעת שישבח את הגרזן» (like a person who sees a great, splendid building: would it occur to him to praise the axe).
- **Recurs.** Isaiah 10:15; Tzemach Tzedek DM line 107 (the axe); the Rebbe, Melukat line 1548.
- **See also in SB2.** SB2-MAG-16, SB2-MAG-09, SB2-MAG-18, SB2-RSB-31.
- **Guide.** When something amazing happens, don't just thank the tool. Look for the hand.

#### SB2-RSB-33. The merchant's year-end accounting *Domain:* commerce

- **Mashal.** A big merchant sells on credit all year. At the end of the year he asks his customers to settle accounts, glad of the business, and reminds them that next year's credit depends on paying now.
- **Nimshal.** Elul is the time of accounting; the 'credit' of next year's blessing depends on settling up through teshuvah.
- **Parts.** the merchant → G-d; credit → the year's blessings; year-end accounting → Elul and teshuvah; next year's credit → the new year's flow.
- **Breaks** [ours]. Ours: the merchant needs his money; G-d needs nothing, and the blessing is for Torah and mitzvos.
- **Principles.** PR-L04
- **Source.** Kuntres U'Maayan (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Kuntres Umaayan (Lubavitch, 1903).txt` line 496: «והמשל בזה סוחר גדול שמוכר סחורתו בהקפה» (and the parable for this is a great merchant who sells his goods on credit).
- **Recurs.** Kuntres U'Maayan line 505.
- **Guide.** Once a year, settle your accounts: see what you owe and to whom. It makes room for next year.

#### SB2-RSB-34. A thick rope of 613 threads *Domain:* craft; connection

- **Mashal.** A thick rope is twisted from 613 thin strands. If one strand breaks, the whole rope gets weaker; for the worst sins, the rope is cut altogether.
- **Nimshal.** The bond between the soul and G-d is made of the 613 commandments.
- **Parts.** the rope → the bond with G-d; the strands → the mitzvos; a broken strand → a sin; the whole rope cut → being cut off.
- **Breaks** [ours]. Ours: a rope can't fix itself; teshuvah ties it again (Tanya, Iggeres HaTeshuvah: the knotted rope is doubled).
- **Principles.** PR-L04
- **Source.** Kuntres U'Maayan (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Kuntres Umaayan (Lubavitch, 1903).txt` line 77: «וכמו על דרך משל מחבל עב שזור מתרי"ג חבלים דקים» (like a thick rope twisted from 613 thin ropes).
- **Recurs.** Tanya, Iggeres HaTeshuvah ch. 3 (the knotted rope, cited by the Rebbe, Likkutei Sichos lines 34953, 36050).
- **See also in SB2.** SB2-TZ-03, SB2-TZ-12, SB2-RSB-11, SB2-RSB-13, SB2-RSB-30.
- **Guide.** Every small good thing you do is one thread in a rope. A break weakens it, and a knot can make it stronger.

#### SB2-RSB-35. Sea water that covers is not like nature *Domain:* water; the mashal's break

- **Mashal.** Water covering something hidden under the sea is a different thing from what it covers; neither made the other.
- **Nimshal.** The Rashab says this parable is 'not a true mashal' for nature hiding G-d: G-d made the garments of nature and gives them life; the covering is itself His.
- **Parts.** the sea → nature; the hidden thing → G-d; covering → concealment.
- **Breaks** [stated]. Stated: the parable fails because water and the hidden object are two separate things.
- **Principles.** PR-L07, PR-L11
- **Source.** Kuntres U'Maayan (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Kuntres Umaayan (Lubavitch, 1903).txt` line 519: «ובאמת הנה המשל של מי הים המכסים על דבר המכוסה אינו משל אמיתי» (but in truth the parable of sea water covering a hidden thing is not a true parable).
- **Recurs.** Tanya ch. 'water covers the sea' (the Alter Rebbe's 'creatures of the sea'); Tzemach Tzedek on fish.
- **See also in SB2.** SB2-BST-30, SB2-MAG-24, SB2-TZ-22, SB2-MHS-04, SB2-RYZ-06, SB2-RBE-07, SB2-RBE-08.
- **Guide.** What hides G-d is also from Him. The cover is not a stranger.

#### SB2-RSB-36. Your own foot or another's head *Domain:* body; self

- **Mashal.** A person prefers his own foot to someone else's head.
- **Nimshal.** What a person finds by his own work in contemplation means more to him than a greater idea he only received.
- **Parts.** one's own foot → one's own small discovery; another's head → a greater idea from outside.
- **Breaks** [ours]. Ours: this is a fact about people, not a value judgment.
- **Principles.** PR-L09, PR-L03
- **Source.** Kuntres HaTefillah (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Kuntres HaTefillah (Lubavitch, 1900).txt` line 54 **OCR**: «עד"מ שיותר טוב לאדם רגל שלו מהראש של זולתו» (as it were, a person prefers his own foot to another's head).
- **Recurs.** Kuntres HaTefillah lines 125, 185.
- **Guide.** The small thing you figured out yourself may move you more than a big thing someone told you. Use that.

#### SB2-RSB-37. Water dripping on stone *Domain:* water; nature

- **Mashal.** Water dripping drop by drop on a stone, soft against hard, still leaves a mark by keeping at it.
- **Nimshal.** Torah studied steadily melts even a heart of stone.
- **Parts.** the drops → steady learning; the stone → a hard heart; the mark → change over time.
- **Breaks** [ours]. Ours: the stone does nothing; the heart can resist or help.
- **Principles.** PR-L04
- **Source.** Kuntres Eitz HaChaim (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Kuntres Eitz HaChaim (scans, OCR).txt` line 185 **OCR**: «וכמשל מים שהולכים טיף טיף ע"ג אבן אם כי חאבן הוא קשה והמים רכים» (like water going drop by drop on a stone: though the stone is hard and the water soft).
- **Recurs.** R. Akiva (Avos d'Rabbi Nassan 6).
- **See also in SB2.** SB2-TZ-15, SB2-TZ-17, SB2-TZ-18, SB2-TZ-19, SB2-TZ-28, SB2-MHS-10, SB2-RSB-26, SB2-RYZ-11, SB2-PIA-05.
- **Guide.** Small, steady effort wears down hard things. Keep dripping.

#### SB2-RSB-38. Light through windows of many colors *Domain:* light and sun

- **Mashal.** Sunlight is simple and has no color of its own; when it shines through many windows of different colors, it seems to take on many colors.
- **Nimshal.** The divisions of the sefiros come from the vessels, not from the simple light.
- **Parts.** sunlight → the infinite light; colored windows → the vessels; colors → the different sefiros.
- **Breaks** [stated]. Stated (Ayin Beis line 85): in some levels the lights really do differ, not only by the vessel.
- **Principles.** PR-L04, PR-L07
- **Source.** Hemshech Ayin Beis (Rashab), `Chassidus-txt/R. Shalom Dovber Schneersohn (Rebbe Rashab) (1860-1920)/Hemshech Ayin Beis (Lubavitch and Rostov, 1912-1916).txt` line 3686: «ועד"מ אור השמש שהוא אור פשוט אין בו שום גוון מצ"ע» (like sunlight, which is simple light and has no color of its own).
- **Recurs.** Pardes (source); Tzemach Tzedek DM line 108 (water in colored vessels).
- **See also in SB2.** SB2-TZ-01, SB2-TZ-02, SB2-TZ-06, SB2-TZ-20, SB2-RSB-03, SB2-RYZ-01, SB2-RYZ-15, SB2-RBE-17.
- **Guide.** The light is one; the windows make the colors. You are one of the windows.

## Rebbe Rayatz (18)

#### SB2-RYZ-01. A candle at noon *Domain:* light and sun; fire

- **Mashal.** A candle gives light and can be seen even from far away. In daylight it doesn't light anything and can't even be seen, yet it hasn't stopped existing; next to the day it simply takes up no room.
- **Nimshal.** 'Counts as nothing before Him' (kulla kamei k'la chashiv) is like the candle at noon: creation exists, but takes up no space before Him. Higher still, 'there is nothing else' means no existence at all apart from Him.
- **Parts.** the candle → creation; daylight → G-d's revealed presence; burning but unseen → existing but taking no place.
- **Breaks** [stated]. Stated: this fits only 'counts as nothing'; the deeper 'there is nothing else' (ein od) goes beyond the parable, since the candle still exists.
- **Principles.** PR-L07, PR-L04, PR-L08
- **Source.** Sefer HaMaamarim (Rayatz), `Chassidus-txt/R. Yosef Yitzchak Schneersohn (Rebbe Rayatz) (1880-1950)/Sefer HaMaamarim (Riga and Otwock, 1929-1933).txt` line 244: «והמשל בזה כמו שרגא בטיהרא, דהנר ענינו להאיר» (and the parable for this is like a candle at noon: a candle's purpose is to give light).
- **Recurs.** Talmud, Chullin 60b (source idiom); the Alter Rebbe, Tanya ch. 33 and Shaar HaYichud; depths MH-C01; the Rebbe Rashab, Samach Vav.
- **See also in SB2.** SB2-TZ-01, SB2-TZ-02, SB2-TZ-06, SB2-TZ-20, SB2-RSB-03, SB2-RSB-38, SB2-RYZ-15, SB2-RBE-17.
- **Guide.** Light a candle at noon. It's still burning, it just doesn't take up room. Maybe you are like that, held in something brighter.

#### SB2-RYZ-02. Too busy to feel hungry *Domain:* body; attention

- **Mashal.** When a person is deeply absorbed in something, he can go a day or two without eating or drinking, as if he forgot them. It's not that he doesn't want to eat; he is just tied up in what absorbs him.
- **Nimshal.** People don't hear the call from above not because they can't, but because they are tied up in other things.
- **Parts.** the absorbed person → someone caught in worldly concerns; not feeling hunger → not hearing the call; the hidden hunger → the soul's real wish.
- **Breaks** [ours]. Ours: hunger comes back by itself; the soul's call must be listened for.
- **Principles.** PR-L09, PR-L04
- **Source.** Sefer HaMaamarim (Rayatz), `Chassidus-txt/R. Yosef Yitzchak Schneersohn (Rebbe Rayatz) (1880-1950)/Sefer HaMaamarim (Riga and Otwock, 1929-1933).txt` line 256: «והמשל בזה כמו שאנו רואין במוחש בטבעי בנ"א דכאשר הוא טרוד באיזה ענין» (the parable is as we see plainly in human nature: when a person is busy with some matter).
- **Recurs.** RY line 962; RY line 1636 (house without windows).
- **Guide.** You may not feel what you need because you're busy. When you stop, the deeper hunger is still there.

#### SB2-RYZ-03. The lamp: oil, wick and flame *Domain:* fire; light

- **Mashal.** In a lamp the wick draws the oil, and the light holds on the wick; the oil makes the wick burn long, while a wick alone burns out fast. The quality of the light depends on oil and wick together.
- **Nimshal.** The soul is 'the lamp of G-d': the body is the wick, the mitzvos are the oil, and the light is the soul's G-dliness revealed.
- **Parts.** the flame → the soul; the wick → the body; the oil → the mitzvos; good light → a life that shows G-dliness.
- **Breaks** [ours]. Ours: oil and wick are used up; mitzvos and the body are lifted up.
- **Principles.** PR-L04, PR-L09
- **Source.** Sefer HaMaamarim (Rayatz), `Chassidus-txt/R. Yosef Yitzchak Schneersohn (Rebbe Rayatz) (1880-1950)/Sefer HaMaamarim (Riga and Otwock, 1929-1933).txt` line 259: «אמנם טיב האור וזכותה זה תלוי בשמן ופתילה כאחד. וככל המשל הזה נבין בנשמה ג"כ» (but the light's quality and clarity depend on oil and wick together; and by this whole parable we will understand the soul too).
- **Recurs.** Proverbs 20:27; RY line 552, 969; Ayin Beis line 2416 (the wick); the Piaseczner, Derech HaMelech line 169 (oil, wick and flame become one).
- **See also in SB2.** SB2-BST-04, SB2-BST-23, SB2-RSB-20, SB2-RSB-21, SB2-RYZ-13, SB2-PIA-11, SB2-PIA-12, SB2-PIA-13.
- **Guide.** Your body is the wick, your good deeds the oil, and something bright burns on top. You need all three.

#### SB2-RYZ-04. Cleaning the house for the king *Domain:* king and kingdom; house

- **Mashal.** A house the king will enter must be swept and washed so no dirt or filth is found in it.
- **Nimshal.** For the heart to be a home for G-d's light, it must be cleansed of all bad, both by avoiding wrong and by mastering bad traits.
- **Parts.** the house → the heart; cleaning → 'turn from evil', the negative commandments; the king entering → G-d's presence.
- **Breaks** [ours]. Ours: a house is cleaned once; a heart needs it over and over.
- **Principles.** PR-L04
- **Source.** Sefer HaMaamarim (Rayatz), `Chassidus-txt/R. Yosef Yitzchak Schneersohn (Rebbe Rayatz) (1880-1950)/Sefer HaMaamarim (Riga and Otwock, 1929-1933).txt` line 283: «וכמשל הבית שרוצים להכניס שם המלך שצריך כיבוד ורחיצה» (like the house into which they want to bring the king, which needs sweeping and washing).
- **Recurs.** Kuntres HaTefillah line 185 (the king's dwelling must be clean); the Rebbe on 'a dwelling below'.
- **See also in SB2.** SB2-MHS-05, SB2-RBE-01, SB2-PIA-09.
- **Guide.** Before someone important comes over, you clean. Do the same for the best thing you want to let into your heart.

#### SB2-RYZ-05. Stepping just off the road *Domain:* travel

- **Mashal.** Someone steps just slightly off the road, sure he knows the way and won't get lost, and keeps going further until he's deep in a thick forest, sometimes in danger.
- **Nimshal.** The evil inclination starts with a small 'bend' that seems like nothing and leads step by step into deep trouble.
- **Parts.** the road → the straight way; the small step aside → a small wrong; the forest → serious sin.
- **Breaks** [ours]. Ours: a lost walker can see the forest; the slide in a person is often not noticed.
- **Principles.** PR-L04
- **Source.** Sefer HaMaamarim (Rayatz), `Chassidus-txt/R. Yosef Yitzchak Schneersohn (Rebbe Rayatz) (1880-1950)/Sefer HaMaamarim (Riga and Otwock, 1929-1933).txt` line 353: «והמשל בזה כמו הסר מן הדרך והולך בצדי דרכים» (and the parable is like one who turns from the road and walks on the sides of the roads).
- **Recurs.** Talmud (the yetzer's gradual method); RY line 352 (the walled city).
- **Guide.** Big detours start with small steps sideways. Notice the first one.

#### SB2-RYZ-06. The root of the mashal is higher *Domain:* the mashal itself; teacher and student

- **Mashal.** A student understands a deep idea through a parable, which is something foreign to the idea. It seems the parable is lower than the idea, yet only the very wisest, like Solomon, can make parables.
- **Nimshal.** The root of a mashal is above the nimshal; that is why it can reveal what is below it. Only one with power and permission can make a true and exact mashal.
- **Parts.** the wise maker → the higher source; the parable → a garment that reveals; the idea → what is revealed.
- **Breaks** [stated]. Stated: on its face the mashal is lower (a foreign thing), so this is a paradox: lower in form, higher in root.
- **Principles.** PR-L03, PR-L05, PR-L01
- **Source.** Sefer HaMaamarim (Rayatz), `Chassidus-txt/R. Yosef Yitzchak Schneersohn (Rebbe Rayatz) (1880-1950)/Sefer HaMaamarim (Riga and Otwock, 1929-1933).txt` line 582: «דהנה שרש המשל הוא למעלה מהנמשל ולכן דוקא מי שהוא חכם גדול ביותר יכול לאמר משלים» (for the root of the mashal is above the nimshal, and therefore only one who is very wise can tell parables).
- **Recurs.** Maharash, Toras Shmuel line 4369; Tzemach Tzedek, Maamarei line 179; R. Aharon's first condition.
- **See also in SB2.** SB2-BST-30, SB2-MAG-24, SB2-TZ-22, SB2-MHS-04, SB2-RBE-07, SB2-RBE-08, SB2-RSB-35.
- **Guide.** A good picture comes from someone who understands more than the picture shows. Trust pictures from people who know.

#### SB2-RYZ-07. A small child is not ashamed *Domain:* father and son; shame

- **Mashal.** A small child is not ashamed of anything, because he has no understanding of what is fine and what is ugly.
- **Nimshal.** One pulled after physical things, who thinks bitter is sweet, has not yet developed the understanding to feel shame.
- **Parts.** the child → one immersed in physicality; no shame → no awareness; growing up → gaining understanding.
- **Breaks** [ours]. Ours: the child is innocent; the adult is responsible.
- **Principles.** PR-L04
- **Source.** Sefer HaMaamarim (Rayatz), `Chassidus-txt/R. Yosef Yitzchak Schneersohn (Rebbe Rayatz) (1880-1950)/Sefer HaMaamarim (Riga and Otwock, 1929-1933).txt` line 719: «ועד"מ תינוק קטן שאינו מתבייש כלל כי אין בינות לו במה שהוא נאה ומגונה» (like a small child who is not ashamed at all, since he has no understanding of what is fine and what is ugly).
- **Recurs.** (Rayatz).
- **Guide.** Not feeling bad about something may mean you haven't grown into seeing it yet. That's a place to grow from, not to stay.

#### SB2-RYZ-08. The first juice from olives and grapes *Domain:* food; nature

- **Mashal.** The first juice pressed from olives or grapes is the best, the essence; because of its quality, other drinks are mixed into it.
- **Nimshal.** Shemini Atzeres draws down the essence for the whole year; it later mixes into the year's daily service.
- **Parts.** the first juice → the holiday's essential flow; mixing in → the rest of the year.
- **Breaks** [ours]. Ours: juice is used up; the holiday's essence keeps flowing.
- **Principles.** PR-L04
- **Source.** Sefer HaMaamarim (Rayatz), `Chassidus-txt/R. Yosef Yitzchak Schneersohn (Rebbe Rayatz) (1880-1950)/Sefer HaMaamarim (Riga and Otwock, 1929-1933).txt` line 918: «ועד"מ פירות של משקה כמו זתים וענבים, הנה משקה הראשונה היוצא מהפרי» (like fruits that give drink, such as olives and grapes: the first drink to come out of the fruit).
- **Recurs.** Midrash on Shemini Atzeres (the king's small meal), MDL line 276, Melukat line 334.
- **Guide.** The best of something comes first and flavors everything after. Start your days and years from the best part.

#### SB2-RYZ-09. Exile is sleep *Domain:* body; sleep

- **Mashal.** When a person is awake, all his powers shine in order. In sleep they withdraw, and the imagination rules.
- **Nimshal.** 'I am asleep': exile is like sleep, when the soul's powers are hidden.
- **Parts.** waking → redemption; sleep → exile; the hidden powers → the soul's concealed light.
- **Breaks** [ours]. Ours: sleep is needed and healthy; exile is not chosen.
- **Principles.** PR-L04, PR-L09
- **Source.** Sefer HaMaamarim (Rayatz), `Chassidus-txt/R. Yosef Yitzchak Schneersohn (Rebbe Rayatz) (1880-1950)/Sefer HaMaamarim (Riga and Otwock, 1929-1933).txt` line 928: «שהגלות נמשל לשינה, ועד"מ אדם כשהוא ער אז הנה כל כחות נפשו מאירים בו בגילוי» (exile is compared to sleep; like a person: when awake, all his soul's powers shine in him openly).
- **Recurs.** Song of Songs 5:2; Zohar; Maharash line 6082 (the dream).
- **Guide.** Some seasons of life feel like sleep. The powers are still in you, waiting for morning.

#### SB2-RYZ-10. The father who guides his son *Domain:* father and son

- **Mashal.** A father guiding his son draws him near with much good if the son accepts it; if not, he scolds and disciplines him so he will go straight.
- **Nimshal.** G-d wakes people in two ways: with kindness when they accept, with hardship when they don't, always aiming for good.
- **Parts.** the father → G-d; drawing near with good → kind awakening; discipline → hard events; the son returning → a sign his inside is good.
- **Breaks** [ours]. Ours: a father can be wrong; the parable assumes perfect intent.
- **Principles.** PR-L04, PR-L07
- **Source.** Sefer HaMaamarim (Rayatz), `Chassidus-txt/R. Yosef Yitzchak Schneersohn (Rebbe Rayatz) (1880-1950)/Sefer HaMaamarim (Riga and Otwock, 1929-1933).txt` line 1061: «וכמשל האב המדריך את בנו אם הבן הוא במזג טוב ומקבל ההדרכה» (like a father guiding his son: if the son is good-natured and accepts the guidance).
- **Recurs.** Deuteronomy 8:5; the Maggid on the father's love.
- **See also in SB2.** SB2-MAG-04, SB2-MAG-05, SB2-MAG-22, SB2-BST-13, SB2-BST-22, SB2-RSB-08.
- **Guide.** Hard times aren't always punishment. Sometimes they're guidance that we wouldn't take the easy way.

#### SB2-RYZ-11. A river fed by springs *Domain:* water; nature

- **Mashal.** A river with many springs in it is not only full and wide; its water is living water. A river without springs can run dry, but springs keep it alive. The more obstacles, the more strongly they push.
- **Nimshal.** When obstacles are strong, they wake a deeper inner power in the soul, like living springs that do not fail.
- **Parts.** the river → the person; the springs → inner essential powers; obstacles → difficulties; living water → strength that doesn't run out.
- **Breaks** [ours]. Ours: rivers don't choose; the soul can call on its springs.
- **Principles.** PR-L04, PR-L09
- **Source.** Sefer HaMaamarim (Rayatz), `Chassidus-txt/R. Yosef Yitzchak Schneersohn (Rebbe Rayatz) (1880-1950)/Sefer HaMaamarim (Riga and Otwock, 1929-1933).txt` line 1352: «והמשל בזה כמו נהר שיש בו מעינות הרבה» (and the parable is like a river with many springs in it).
- **Recurs.** Tzemach Tzedek (water held back, DM line 259).
- **See also in SB2.** SB2-TZ-15, SB2-TZ-17, SB2-TZ-18, SB2-TZ-19, SB2-TZ-28, SB2-MHS-10, SB2-RSB-26, SB2-RSB-37, SB2-PIA-05.
- **Guide.** Problems can stir something deep in you that easy days never touch. That's a spring, not a flood.

#### SB2-RYZ-12. The painter of the apple tree *Domain:* art; nature

- **Mashal.** A painted apple tree has many details: roots, trunk, branches, leaves, fruit. But the viewer sees mainly the life of the tree that carries all the details.
- **Nimshal.** After learning all the details of an idea, one should rise to its 'point': the depth that carries all the parts.
- **Parts.** the painting → the idea studied; details → its parts; the tree's life → the core insight.
- **Breaks** [ours]. Ours: a painter gives the life; in study, the student must find it.
- **Principles.** PR-L03, PR-L09
- **Source.** Sefer HaMaamarim (Rayatz), `Chassidus-txt/R. Yosef Yitzchak Schneersohn (Rebbe Rayatz) (1880-1950)/Sefer HaMaamarim (Riga and Otwock, 1929-1933).txt` line 1374: «והמשל בזה הוא כמו המצייר אילן של תפוחים או שארי פירות» (and the parable is like one who paints an apple tree or other fruit tree).
- **Recurs.** the Rebbe Rashab on 'nekudas hatamtzis' (the point of an idea).
- **Guide.** After all the details, step back and ask: what is the one living thing all of this is about?

#### SB2-RYZ-13. A spark rising into the torch *Domain:* fire

- **Mashal.** A small spark rises and is drawn to merge into a big torch, because it is made of the torch; its being a separate spark does not stop it from rising.
- **Nimshal.** The soul longs to be included in its Source because it is of His essence; its separateness does not cancel its nature.
- **Parts.** the spark → the soul; the torch → G-d; rising → the soul's natural longing.
- **Breaks** [ours]. Ours: a spark burns out when it merges; the soul is meant to come back down too ('run and return').
- **Principles.** PR-L04, PR-L09
- **Source.** Sefer HaMaamarim (Rayatz), `Chassidus-txt/R. Yosef Yitzchak Schneersohn (Rebbe Rayatz) (1880-1950)/Sefer HaMaamarim (Riga and Otwock, 1929-1933).txt` line 1453: «והנה המשל בזה הוא כמו הניצוץ קטן שעולה ונמשך להכלל באבוקה גדולה» (the parable for this is like a small spark rising and drawn to be included in a great torch).
- **Recurs.** Tanya ch. 19 (the flame rises); Tzemach Tzedek, Maamarei line 499 (fire rises); Ayin Beis line 5287.
- **See also in SB2.** SB2-BST-04, SB2-BST-23, SB2-RSB-20, SB2-RSB-21, SB2-RYZ-03, SB2-PIA-11, SB2-PIA-12, SB2-PIA-13.
- **Guide.** Part of you wants to go home to something bigger. That pull is natural; you came from there.

#### SB2-RYZ-14. The rich man and the sufferer *Domain:* commerce; prayer

- **Mashal.** A rich man needs a lot of thought to rouse himself in prayer; a poor man in pain needs no thought: as soon as he remembers his situation, he cries.
- **Nimshal.** When a person truly feels before Whom he stands, prayer comes by itself, without long preparation.
- **Parts.** the rich man → one who feels no need; the sufferer → one who feels his state; the cry → real prayer.
- **Breaks** [ours]. Ours: this doesn't wish suffering on anyone; it shows what real awareness does.
- **Principles.** PR-L09, PR-L13
- **Source.** Sefer HaMaamarim (Rayatz), `Chassidus-txt/R. Yosef Yitzchak Schneersohn (Rebbe Rayatz) (1880-1950)/Sefer HaMaamarim (Riga and Otwock, 1929-1933).txt` line 1588: «וכמ"ש בשערים משל ע"ז דהעשיר צריך כמה התבוננו' לעורר א"ע» (as written in Sha'arim, a parable: the rich man needs much contemplation to rouse himself).
- **Recurs.** the Mitteler Rebbe, Sha'arei Teshuvah (source 'Sha'arim'); the Piaseczner, Bnei Machshava Tova line 269 (two people saying Psalms).
- **Guide.** When you know what you need, words come easily. Before praying, remember where you really stand.

#### SB2-RYZ-15. A house with no windows *Domain:* light and sun; house

- **Mashal.** The sun can blaze, but a house without windows stays dark. Make a small hole and the sunlight bursts in with all its force.
- **Nimshal.** Body and animal soul cover the soul so it does not hear the call from above; yet the soul's essence hears everything, and a small opening lets it shine through.
- **Parts.** the sun → the call from above; the windowless house → the covered person; a small hole → a small opening of the heart.
- **Breaks** [ours]. Ours: the house can't make its own hole; a person can.
- **Principles.** PR-L04, PR-L09
- **Source.** Sefer HaMaamarim (Rayatz), `Chassidus-txt/R. Yosef Yitzchak Schneersohn (Rebbe Rayatz) (1880-1950)/Sefer HaMaamarim (Riga and Otwock, 1929-1933).txt` line 1636: «ועד"מ בית שאין בו חלונות דהגם דאור השמש זורח בתוקף גדול הנה בהבית לא יאיר» (like a house without windows: though sunlight blazes strongly, in the house it does not shine).
- **Recurs.** RY line 256 (too busy to hear); the Rebbe ('open for me an opening like the eye of a needle').
- **See also in SB2.** SB2-TZ-01, SB2-TZ-02, SB2-TZ-06, SB2-TZ-20, SB2-RSB-03, SB2-RSB-38, SB2-RYZ-01, SB2-RBE-17.
- **Guide.** You don't need a big window. A small hole lets the sun in.

#### SB2-RYZ-16. Gems in the mud *Domain:* stones; nature

- **Mashal.** Precious, shining stones grow in rock crevices or buried in sand, coated with dirt and dust. They must be taken out of their muddy covering and cleaned; only then do they shine with the beauty put in them.
- **Nimshal.** A person's worth is like a gem: it comes covered, and must be dug out and cleaned to shine. The Rayatz adds that unlike building a house, a person does not get clean materials to work with.
- **Parts.** the gem → the soul; the mud → the covering of habits and the body; cleaning → the work of Chassidus; shining → the soul's natural light.
- **Breaks** [stated]. Stated: 'the mashal is not like the nimshal': a builder has all the materials and skill, and labor builds the house; a person's materials come mixed and covered.
- **Principles.** PR-L04, PR-L07
- **Source.** Kuntres Toras HaChassidus (Rayatz), `Chassidus-txt/R. Yosef Yitzchak Schneersohn (Rebbe Rayatz) (1880-1950)/Kuntres Toras HaChassidus (scans, OCR).txt` line 94 **OCR**: «והמשל בזה: אבנים טובות ומאירות אופז גידולם הוא שנמצאים בנקיקי סלעים או טמונים בחול» (and the parable: precious, shining stones, whose way of growing is that they are found in rock crevices or buried in sand).
- **Recurs.** KTH line 92 (the break); depths MH-C20.
- **Guide.** What is best in you may be covered in mud. That doesn't make it less precious. Clean a little and see it shine.

#### SB2-RYZ-17. The condemned man who meets the king *Domain:* king and kingdom; law

- **Mashal.** A man sentenced to death who meets the king is set free from his punishment.
- **Nimshal.** In the light of the King's face there is only life: at the inner level of G-d there is no 'left side', only kindness.
- **Parts.** the king's face → the inner Infinite light; the condemned man → a person under judgment; release → the sweetening that comes from the inner light.
- **Breaks** [ours]. Ours: in the parable it is the king's mercy by chance; in the nimshal it is the nature of that level.
- **Principles.** PR-L04, PR-L08
- **Source.** Sefer HaMaamarim (Rayatz), `Chassidus-txt/R. Yosef Yitzchak Schneersohn (Rebbe Rayatz) (1880-1950)/Sefer HaMaamarim (Riga and Otwock, 1929-1933).txt` line 692: «דר"ל מי שנידן למיתה כשפגש בהמלך הוא נפטר מהעונש» (that one sentenced to death, when he meets the king, is released from the punishment).
- **Recurs.** Proverbs 16:15; Maggid, MDL line 204; RY line 707.
- **See also in SB2.** SB2-MAG-20, SB2-MAG-21, SB2-TZ-11, SB2-TZ-13, SB2-MHS-12, SB2-RSB-07, SB2-RSB-24.
- **Guide.** Some faces just make the bad stuff fall away. Find that face, and let it look at you.

#### SB2-RYZ-18. The prisoner condemned to death cries out *Domain:* captivity; life and death

- **Mashal.** A prisoner condemned to death longs for life even more; when a chance to escape appears, he runs and cries out loud. His running is toward life, but mostly away from death.
- **Nimshal.** Teshuvah that comes from distance is loud and open, like the escape of a condemned man, unlike quiet inner closeness.
- **Parts.** the prisoner → the soul far away; the death sentence → distance from G-d; the cry and run → teshuvah from distance.
- **Breaks** [ours]. Ours: a prisoner's danger is outside him; the soul's 'death' is distance it often doesn't feel.
- **Principles.** PR-L04, PR-L09
- **Source.** Sefer HaMaamarim (Rayatz), `Chassidus-txt/R. Yosef Yitzchak Schneersohn (Rebbe Rayatz) (1880-1950)/Sefer HaMaamarim (Riga and Otwock, 1929-1933).txt` line 13: «והמשל בזה במי שר"ל יושב בבית אסורים ונדון למיתה» (and the parable is of one who, heaven forbid, sits in prison condemned to death).
- **Recurs.** the Rebbe, Likkutei Sichos lines 26318, 29515 (the Rayatz's parable of fleeing death); Maharash line 1917.
- **Guide.** When you realize how far you've drifted, it's alright to run back loudly. That's not drama; it's life.

## the Rebbe (17)

#### SB2-RBE-01. Living in a friend's house *Domain:* house

- **Mashal.** A man living in his friend's house lives there with all of himself, just as in his own home, though the house still belongs to his friend.
- **Nimshal.** 'A dwelling in the lowest world': G-d's very essence is revealed here while the world stays a world. It is not erased or lifted out of itself; it stays 'lower', and still He lives in it fully.
- **Parts.** the man → G-d's essence; the friend's house → the physical world; the house staying the friend's → the world remaining itself; living there fully → complete presence.
- **Breaks** [stated + ours]. Stated: the parable was chosen exactly to show that the lower stays lower. Ours: a guest can leave; the dwelling is meant to be permanent.
- **Principles.** PR-L04, PR-L06
- **Source.** Sefer HaMaamarim Melukat (the Rebbe), `Chassidus-txt/R. Menachem Mendel Schneerson (Lubavitcher Rebbe) (1902-1994)/Sefer HaMaamarim Melukat (Brooklyn, New York, 1951-1992).txt` line 456: «דענין דירה בתחתונים הוא כמשל אדם הדר בבית חבירו, שכל עצמותו כמו שהוא דר בביתו הוא דר בבית חבירו» (the idea of a dwelling below is like a man living in his friend's house: with all his self, as he lives in his own house, he lives in his friend's).
- **Recurs.** depths RB-C25; Maharash, Toras Shmuel line 7777; the Rebbe, Melukat line 2487 (a king's permanent dwelling).
- **See also in SB2.** SB2-MHS-05, SB2-RYZ-04, SB2-PIA-09.
- **Guide.** You don't have to become someone else for something holy to live in your life. It can move in with you as you are.

#### SB2-RBE-02. The king in the field *Domain:* king and kingdom

- **Mashal.** Before a king enters his city, the townspeople go out to greet him in the field. Anyone who wants may meet him there, and he receives all with a smiling face. Later, in his palace, only the chosen may enter, and only with permission.
- **Nimshal.** In Elul, G-d is 'in the field': He is close and approachable to everyone, as they are, in ordinary life.
- **Parts.** the king → G-d; the field → ordinary life in Elul; the palace → the High Holidays and holy places; the smiling face → the Thirteen Attributes of Mercy shown.
- **Breaks** [ours]. Ours: a king in the field is still traveling to his palace; in Elul the closeness is meant to come home with us.
- **Principles.** PR-L04
- **Source.** Sefer HaMaamarim Melukat (the Rebbe), `Chassidus-txt/R. Menachem Mendel Schneerson (Lubavitcher Rebbe) (1902-1994)/Sefer HaMaamarim Melukat (Brooklyn, New York, 1951-1992).txt` line 2970: «ע"פ משל למלך שקודם בואו לעיר יוצאין אנשי העיר לקראתו ומקבלין פניו בשדה» (by a parable of a king: before he comes to the city, the people go out to meet him and greet him in the field).
- **Recurs.** the Alter Rebbe, Likkutei Torah, Re'eh (source); the Rayatz's addition 'and they can'; Likkutei Sichos lines 15491, 37497; Maggid, MDL line 69 (king on the road).
- **See also in SB2.** SB2-BST-01, SB2-BST-27, SB2-MAG-08, SB2-PIA-15.
- **Guide.** There are times when the most important presence comes out to where you already are. You don't have to dress up. Just go out and meet it.

#### SB2-RBE-03. The father hides from his little son *Domain:* father and son; play

- **Mashal.** A father hides from his little son to bring out the son's cleverness, so the son understands that the hiding is only so he will search and find him.
- **Nimshal.** G-d's hiddenness in the world is there so that we will search for Him in everything, and the Torah promises: 'you will find'.
- **Parts.** the hiding father → G-d hidden in the world; the child's search → our search; understanding the game → knowing that hiding is for finding.
- **Breaks** [ours]. Ours: the father's hiding is short and safe; ours can feel long and real.
- **Principles.** PR-L04, PR-L09
- **Source.** Sefer HaMaamarim Melukat (the Rebbe), `Chassidus-txt/R. Menachem Mendel Schneerson (Lubavitcher Rebbe) (1902-1994)/Sefer HaMaamarim Melukat (Brooklyn, New York, 1951-1992).txt` line 421: «וכמשל האב המסתיר את עצמו מבנו הקטן בכדי להראות את חכמת הבן» (like a father who hides from his small son in order to show the son's wisdom).
- **Recurs.** Baal Shem Tov (the father who hides, cited across Chassidus); Maggid, MDL line 183; Samach Vav line 7276 (editors' summary); Keter Shem Tov line 279.
- **See also in SB2.** SB2-BST-20, SB2-MAG-03, SB2-RSB-06, SB2-MHS-06.
- **Guide.** If it feels like what you are looking for is hiding, maybe it is the kind of hiding that wants to be found.

#### SB2-RBE-04. Stumbling with the foot, falling on the head *Domain:* body

- **Mashal.** When a person stumbles with his foot, his head falls too.
- **Nimshal.** A failing at the soul's 'foot' (action) affects even its highest level, the 'head'; so the call 'return, Israel' speaks to the head.
- **Parts.** the foot → the soul's lowest level, deed; the head → the soul's highest level; the fall → the effect of sin through all levels.
- **Breaks** [stated]. Stated: the soul's essence itself is never truly captured; only the covering on it needs redeeming.
- **Principles.** PR-L09, PR-L04
- **Source.** Sefer HaMaamarim Melukat (the Rebbe), `Chassidus-txt/R. Menachem Mendel Schneerson (Lubavitcher Rebbe) (1902-1994)/Sefer HaMaamarim Melukat (Brooklyn, New York, 1951-1992).txt` line 2765: «וכמשל אדם הנכשל ברגלו, שעי"ז נופל גם ראשו» (like a man who stumbles with his foot, by which his head falls too).
- **Recurs.** the Alter Rebbe, Likkutei Torah, Shuvah Yisrael (source; Melukat line 1653).
- **Guide.** A small slip in what you do can bring all of you down for a moment. And a small good step can lift all of you up.

#### SB2-RBE-05. The beloved vessel never seems finished *Domain:* craft; love

- **Mashal.** A person with a beautiful vessel or building keeps fixing it; the more he loves it, the more it seems to still need work.
- **Nimshal.** 'The heavens are not pure in His eyes' is not harsh judgment but love: what is most precious gets the most care.
- **Parts.** the owner → G-d; the beloved vessel → the soul or the world; endless fixing → demands that come from love.
- **Breaks** [ours]. Ours: a human owner may be a perfectionist; the nimshal is pure love.
- **Principles.** PR-L04
- **Source.** Sefer HaMaamarim Melukat (the Rebbe), `Chassidus-txt/R. Menachem Mendel Schneerson (Lubavitcher Rebbe) (1902-1994)/Sefer HaMaamarim Melukat (Brooklyn, New York, 1951-1992).txt` line 3181: «וכמשל האדם שיש לו כלי נאה או בנין נאה, שכל מה שהכלי חביב עליו יותר הוא מתקנה יותר» (like a man who has a beautiful vessel or building: the more the vessel is dear to him, the more he repairs it).
- **Recurs.** Zohar on Job 15:15.
- **Guide.** When someone who loves you keeps asking more of you, it may be because you are precious to them.

#### SB2-RBE-06. Rich in himself *Domain:* commerce; wealth

- **Mashal.** Being rich doesn't just mean having plenty. Someone who has a great deal, all received from others, is still poor: a receiver. A rich person has it from himself.
- **Nimshal.** Moshe's prayer was a 'rich man's prayer', not for himself; and true knowing (da'as) is being rich from within, not just receiving ideas.
- **Parts.** the rich man → one who gives from himself; the poor man with much → one who only receives; true wealth → inner awareness.
- **Breaks** [ours]. Ours: no one is rich from himself before G-d; the parable is about how we stand toward others.
- **Principles.** PR-L09
- **Source.** Sefer HaMaamarim Melukat (the Rebbe), `Chassidus-txt/R. Menachem Mendel Schneerson (Lubavitcher Rebbe) (1902-1994)/Sefer HaMaamarim Melukat (Brooklyn, New York, 1951-1992).txt` line 2590: «שגם כשיש לו שפע מרובה אבל השפע שיש לו הוא לא משל עצמו אלא שקיבל מאחרים, הוא עני» (even when he has much plenty, but the plenty is not his own but received from others, he is poor).
- **Recurs.** depths RB-C20; Midrash Tehillim (three who came to the king).
- **Guide.** You can have a lot and still feel empty if none of it comes from inside you. Find one thing that does.

#### SB2-RBE-07. Three parables: the torch, the barrel, the seed *Domain:* fire; water; birth

- **Mashal.** A big torch shows its strength by lighting far away, even if the far light is faint. A barrel full past its brim shows its fullness by spilling outside. A seed brings a new being, unlike passing on an idea.
- **Nimshal.** 'The higher it is, the lower it comes': the greatness of the source is shown precisely in the lowest place. Each parable shows a different side (light, water, a new being).
- **Parts.** the torch's far light → G-d's light in the lowest world; the overflow → wisdom's 'leftovers'; the seed → creation of something new.
- **Breaks** [stated]. Stated (the Rebbe's rule, Melukat line 2732): several meshalim are used because no one mashal fits all the details.
- **Principles.** PR-L07, PR-L05, PR-L04, PR-L14
- **Source.** Sefer HaMaamarim Melukat (the Rebbe), `Chassidus-txt/R. Menachem Mendel Schneerson (Lubavitcher Rebbe) (1902-1994)/Sefer HaMaamarim Melukat (Brooklyn, New York, 1951-1992).txt` line 1291: «ג' משלים בענין כל הגבוה גבוה ביותר יורד ומתלבש ומתגלה בנמוך נמוך יותר» (three parables on how whatever is highest goes down and is clothed and revealed in what is lowest).
- **Recurs.** the Mitteler Rebbe (source, cited by the Rebbe); Tzemach Tzedek, DM line 145 and 236; Maharash line 6014.
- **See also in SB2.** SB2-BST-30, SB2-MAG-24, SB2-TZ-22, SB2-MHS-04, SB2-RYZ-06, SB2-RBE-08, SB2-RSB-35.
- **Guide.** You can measure how strong a light is by how far it reaches. The far, dim places show how bright the source is.

#### SB2-RBE-08. The teacher-student parable does not fit *Domain:* teacher and student

- **Mashal.** A teacher's mind is above what he gives his student, and that is for himself, not for the student.
- **Nimshal.** But above, every revelation, even the highest, exists so that later, through many contractions, the ten utterances of creation will come from it.
- **Parts.** the teacher's own mind → G-d's light above the world; teaching → creation; the student → the worlds.
- **Breaks** [stated]. Stated: 'the teacher-student parable is not like the nimshal', because the teacher's wisdom is for himself, while every divine revelation is for the sake of the world.
- **Principles.** PR-L07
- **Source.** Sefer HaMaamarim Melukat (the Rebbe), `Chassidus-txt/R. Menachem Mendel Schneerson (Lubavitcher Rebbe) (1902-1994)/Sefer HaMaamarim Melukat (Brooklyn, New York, 1951-1992).txt` line 2316: «דלכאורה, המשל דרב ותלמיד אינו דומה להנמשל» (for seemingly, the parable of teacher and student is not like the nimshal).
- **Recurs.** the Rebbe Rashab, Samach Vav line 131; Rayatz lines 32, 34, 1182; MEL 2319, 2738.
- **See also in SB2.** SB2-MAG-01, SB2-MAG-02, SB2-MAG-10, SB2-RSB-18, SB2-PIA-07, SB2-BST-30, SB2-MAG-24, SB2-TZ-22, SB2-MHS-04, SB2-RYZ-06, SB2-RBE-07, SB2-RSB-35.
- **Guide.** Even a good comparison has a point where it stops working. Noticing that point is part of understanding.

#### SB2-RBE-09. The small child who gets angry *Domain:* father and son; emotion

- **Mashal.** A small child who has no understanding gets angry right away when he doesn't get what he wants; an adult with understanding can bear the opposite.
- **Nimshal.** Quarrels come from 'small understanding'; when 'the earth is full of knowledge of G-d', no one will harm or destroy.
- **Parts.** the child → small-minded people; anger → fighting; the adult → one with da'as; knowledge → peace.
- **Breaks** [ours]. Ours: adults get angry too; the parable is about understanding, not age.
- **Principles.** PR-L04, PR-L09
- **Source.** Sefer HaMaamarim Melukat (the Rebbe), `Chassidus-txt/R. Menachem Mendel Schneerson (Lubavitcher Rebbe) (1902-1994)/Sefer HaMaamarim Melukat (Brooklyn, New York, 1951-1992).txt` line 235: «וידוע המשל על זה, שהקטן שאין לו דעת, כאשר אין ממלאים רצונו, מיד הוא מתרגז» (and the parable is known: the small child, who has no understanding, when his wish isn't met, immediately gets angry).
- **Recurs.** Tanya ch. 1 (the child angers over small things); the Rebbe on Sukkos and peace.
- **Guide.** When you're about to blow up over something small, ask: what would a bigger me understand here?

#### SB2-RBE-10. The gem ground to save the prince *Domain:* king and kingdom; medicine

- **Mashal.** A prince fell gravely ill, and the only cure was to take the precious gem in the king's crown, the one the crown's worth depends on, grind it, mix it in water and pour it between the prince's lips, in hope that even one drop would go in and save his life.
- **Nimshal.** Spreading the secrets of Torah (Chassidus), the jewel in the King's crown, is worth it to save the life of the prince, the Jewish people, even if only a drop gets in.
- **Parts.** the gem → the inner Torah; grinding it → making it known widely; the sick prince → the people of each generation; one drop → even a little Chassidus.
- **Breaks** [ours]. Ours: grinding the gem wastes most of it; teaching the inner Torah does not lose it.
- **Principles.** PR-L04, PR-L03
- **Source.** Likkutei Sichos (the Rebbe), `Chassidus-txt/R. Menachem Mendel Schneerson (Lubavitcher Rebbe) (1902-1994)/Likkutei Sichos (Brooklyn, New York, 1951-1992).txt` line 1220: «לקחת את האבן היקרה הקבועה בכתר מלכותו של המלך» (to take the precious stone set in the crown of the king's kingship).
- **Recurs.** the Alter Rebbe's parable to R. Pinchas of Koretz (source, HaTamim); Likkutei Sichos lines 1221-1251, 22672, 24226.
- **See also in SB2.** SB2-BST-11, SB2-BST-18, SB2-BST-24, SB2-MAG-06, SB2-MAG-07, SB2-PIA-01, SB2-PIA-03, SB2-PIA-14, SB2-PIA-17.
- **Guide.** The most precious thing you know is worth sharing if it can help even one person, even a drop of it.

#### SB2-RBE-11. Electricity *Domain:* nature; science

- **Mashal.** Electricity is a hidden force: none of the five senses can grasp it, and we know it only by what it does; yet this hidden force pushes away the darkness of night.
- **Nimshal.** The hidden part of the Torah, revealed through Chassidus and a Chassidic way of life, drives away the darkness of material life.
- **Parts.** the hidden force → the secrets of the Torah; its effects → Chassidus in practice; lit-up night → a lit-up life.
- **Breaks** [stated + ours]. The Rebbe marks it as 'by way of wit' (al derech hatzachus); ours: electricity must be wired; inner Torah must be lived.
- **Principles.** PR-L04, PR-L05
- **Source.** Likkutei Sichos (the Rebbe), `Chassidus-txt/R. Menachem Mendel Schneerson (Lubavitcher Rebbe) (1902-1994)/Likkutei Sichos (Brooklyn, New York, 1951-1992).txt` line 21739: «הנה כוח החשמל הוא מהכוחות הנסתרים שבטבע» (electricity is one of the hidden forces in nature).
- **Recurs.** Likkutei Sichos index line 22482.
- **Guide.** Some of the strongest things are invisible; you know them only by what they light up.

#### SB2-RBE-12. Owner and employee *Domain:* commerce; work

- **Mashal.** A faithful employee works hard with his visible powers and then goes home in peace, having done his part. The owner can't sleep calmly even after doing all he can, because the business is his own.
- **Nimshal.** Devotion that comes from 'it's mine' reaches deeper than devotion from duty.
- **Parts.** the employee → service from obligation; the owner → service from identification; sleepless care → essential devotion.
- **Breaks** [ours]. Ours: the owner worries for his profit; in the nimshal it's love, not profit.
- **Principles.** PR-L09
- **Source.** Likkutei Sichos (the Rebbe), `Chassidus-txt/R. Menachem Mendel Schneerson (Lubavitcher Rebbe) (1902-1994)/Likkutei Sichos (Brooklyn, New York, 1951-1992).txt` line 12148: «מהחילוק שבין מסירותו של פקיד או שכיר העושה ענין באמונה, למסירותו של בעל הבית» (from the difference between the devotion of a clerk or hired worker who does a matter faithfully and the devotion of the owner).
- **Recurs.** Likkutei Sichos index line 13600.
- **Guide.** When something is really yours, you care differently. Find what in your life you treat as truly yours.

#### SB2-RBE-13. The child in the factory *Domain:* craft; knowledge

- **Mashal.** A small child brought into a huge factory says that if he could understand every detail, he'd admit someone planned the machines. Since some things look senseless to him and he has hard questions, he decides there is no plan at all.
- **Nimshal.** Doubting G-d's wisdom because we don't understand parts of His world is like the child in the factory.
- **Parts.** the factory → the world; the child → the human mind; his questions → the hard parts of life; the planner → G-d.
- **Breaks** [ours]. Ours: a child can grow up and learn the factory; we may never fully understand.
- **Principles.** PR-L12, PR-L04
- **Source.** Likkutei Sichos (the Rebbe), `Chassidus-txt/R. Menachem Mendel Schneerson (Lubavitcher Rebbe) (1902-1994)/Likkutei Sichos (Brooklyn, New York, 1951-1992).txt` line 13151: «משל למה הדבר דומה, לילד קטן שהכניסוהו לבית חרושת גדול ביותר» (a parable: to what is this like? To a small child brought into a very large factory).
- **Recurs.** Likkutei Sichos line 13145 (the book and its author).
- **See also in SB2.** SB2-RSB-02, SB2-TZ-26, SB2-RSB-16, SB2-MHS-01, SB2-MHS-02.
- **Guide.** Not understanding how something works doesn't prove nobody made it. You might just be new in the factory.

#### SB2-RBE-14. Colored lenses *Domain:* perception; body

- **Mashal.** A person born with beautiful eyes can put in colored lenses. Someone looking can't tell if it's his eye color or the lens, and if the lenses are ugly, he sees the whole world twisted.
- **Nimshal.** Every Jew's true nature is good; habit becomes second nature and covers it, until he can't see things as they are.
- **Parts.** the eyes → the true nature; the lenses → habits; the twisted world → a distorted view of life.
- **Breaks** [ours]. Ours: lenses come off easily; habits take work.
- **Principles.** PR-L09, PR-L04
- **Source.** Likkutei Sichos (the Rebbe), `Chassidus-txt/R. Menachem Mendel Schneerson (Lubavitcher Rebbe) (1902-1994)/Likkutei Sichos (Brooklyn, New York, 1951-1992).txt` line 32510: «ומשל למה הדבר דומה לאדם שנברא יפה­עינים» (to what is this like? To a person created with beautiful eyes).
- **Recurs.** Song of Songs 1:15.
- **Guide.** If the world looks gray and ugly, check the lenses you've been wearing. Your eyes underneath may be fine.

#### SB2-RBE-15. Putting out a fire with gasoline *Domain:* fire; house

- **Mashal.** Someone has a great fire in his house, life is in danger, and he 'puts it out' by pouring gasoline on it.
- **Nimshal.** Trying to fix a crisis with what feeds it only makes it worse.
- **Parts.** the fire → the danger; the gasoline → the wrong cure.
- **Breaks** [ours]. Ours: the parable is stark on purpose; real situations have mixed results.
- **Principles.** PR-L04
- **Source.** Likkutei Sichos (the Rebbe), `Chassidus-txt/R. Menachem Mendel Schneerson (Lubavitcher Rebbe) (1902-1994)/Likkutei Sichos (Brooklyn, New York, 1951-1992).txt` line 17174: «למי שאירע בביתו שריפה גדולה» (to one in whose house a great fire broke out).
- **Recurs.** (a letter of the Rebbe).
- **Guide.** Before you try to fix something, ask whether your fix might be fuel.

#### SB2-RBE-16. Planting in untouched soil *Domain:* nature; plants

- **Mashal.** Sowing and planting in virgin soil needs no work to uproot foreign vines first.
- **Nimshal.** Where Torah has not yet been planted, it is easier to plant it fresh, without first clearing away wrong growth.
- **Parts.** virgin soil → a new place or new person; foreign vines → wrong habits or ideas; planting → teaching.
- **Breaks** [ours]. Ours: virgin soil may also be dry; fresh beginnings have their own difficulty.
- **Principles.** PR-L04
- **Source.** Likkutei Sichos (the Rebbe), `Chassidus-txt/R. Menachem Mendel Schneerson (Lubavitcher Rebbe) (1902-1994)/Likkutei Sichos (Brooklyn, New York, 1951-1992).txt` line 32890: «וכידוע המשל שזריעה ונטיעה בקרקע בתולה אין דורשת עבודה ויגיעה לעקור זמורות זרות» (and as the known parable says: sowing and planting in virgin soil needs no labor to uproot foreign vines).
- **Recurs.** Likkutei Sichos index line 33226.
- **Guide.** Starting fresh somewhere new can be easier than fixing old ground. Don't be afraid to begin.

#### SB2-RBE-17. Light through a window and through a screen *Domain:* light and sun; house

- **Mashal.** Light through a window or a small hole is less, but it's the same light. Light through a screen is changed in its nature; what comes after the screen is a 'born' light, a different light.
- **Nimshal.** Atzilus comes from G-d by contraction (tzimtzum) only, the same light lessened; the lower worlds come through a 'screen' (parsa), a changed light.
- **Parts.** the window → tzimtzum; the screen → parsa; the same light → Atzilus; the changed light → the lower worlds.
- **Breaks** [ours]. Ours: a window and a screen are both outside the light; tzimtzum is within Him.
- **Principles.** PR-L04, PR-L07
- **Source.** Sefer HaMaamarim Melukat (the Rebbe), `Chassidus-txt/R. Menachem Mendel Schneerson (Lubavitcher Rebbe) (1902-1994)/Sefer HaMaamarim Melukat (Brooklyn, New York, 1951-1992).txt` line 3086: «וההפרש בין צמצום ופרסא הוא כמשל ההפרששאנו רואים למטה בין האור שמאיר דרך חלון או דרך נקב» (and the difference between tzimtzum and parsa is like the difference we see below between light shining through a window or through a hole).
- **Recurs.** Ayin Beis line 3743; Tzemach Tzedek DM line 241 (the physical screen).
- **See also in SB2.** SB2-TZ-01, SB2-TZ-02, SB2-TZ-06, SB2-TZ-20, SB2-RSB-03, SB2-RSB-38, SB2-RYZ-01, SB2-RYZ-15.
- **Guide.** Some light reaches you thinner but still itself. Some reaches you changed. Both came from the same sun.

## Piaseczner Rebbe (18)

#### SB2-PIA-01. The father who visits his imprisoned son *Domain:* father and son; captivity

- **Mashal.** A man's son was falsely accused and jailed; he can see him only when the warden opens the cell to look into his case. The foolish father, since the door was opened for the trial, talks only about the trial. The wise father says: true, the warden opened it for that, but it is open and my son is before me; I'll hug him and kiss him and speak to him with love.
- **Nimshal.** When a prayer or a holy time opens a door for some practical reason, use the open door for closeness itself, not only for the business that opened it.
- **Parts.** the son in jail → the soul in the body; the warden opening → a holy moment that opens; talking only of the trial → praying only for needs; hugging the son → simple closeness.
- **Breaks** [ours]. Ours: the warden opened for another purpose; in the nimshal, G-d opened it for exactly this.
- **Principles.** PR-L04, PR-L09
- **Source.** Bnei Machshava Tova (Piaseczner), `Chassidus-txt/R. Kalonymus Kalman Shapira of Piaseczno (1889-1943)/Bnei Machshava Tova (Piaseczno, 1917-1923).txt` line 101: «משל לאיש שהעלילו על בנו ונתנוהו במאסר» (like a man whose son they falsely accused and put in prison).
- **Recurs.** Keter Shem Tov line 109 (asking the king to speak with you); the Piaseczner's other prince parables.
- **See also in SB2.** SB2-BST-11, SB2-BST-18, SB2-BST-24, SB2-MAG-06, SB2-MAG-07, SB2-PIA-03, SB2-PIA-14, SB2-PIA-17, SB2-RBE-10.
- **Guide.** When a door opens for some practical reason, don't only handle the business. The door is open; go in and be close.

#### SB2-PIA-02. Drums so the father won't hear *Domain:* father and son; idolatry

- **Mashal.** The priests of Molech beat drums so that the father would not hear his son crying from between the flames.
- **Nimshal.** The noise of physical sensations is so loud that the soul's trembling is lost: a 'miscarriage' of the soul's feeling.
- **Parts.** the drums → bodily noise; the child's cry → the soul's call; the father not hearing → a person deaf to his own soul.
- **Breaks** [ours]. Ours: the drums were beaten on purpose by others; we often beat our own.
- **Principles.** PR-L09, PR-L04
- **Source.** Bnei Machshava Tova (Piaseczner), `Chassidus-txt/R. Kalonymus Kalman Shapira of Piaseczno (1889-1943)/Bnei Machshava Tova (Piaseczno, 1917-1923).txt` line 141: «משל לכמרי המלך שהכו בתפים למען לא ישמע האב המית בנו המתחנן» (like the king's priests who beat drums so that the father would not hear the sound of his son pleading).
- **Recurs.** Rashi on Jeremiah 7:31 (source); Rayatz line 256 (too busy to hear).
- **Guide.** Some noise in our lives exists so we won't hear a small voice inside. Turn it down and listen.

#### SB2-PIA-03. The last moment before exile *Domain:* king and kingdom; father and son

- **Mashal.** A prince was sentenced to be sent away from his father into prison. In the last moment before parting, he presses closer to his father, holds him, clings, longs, and cries from the depths: 'Even if I walk in the valley of death, I will fear no evil, for You are with me.'
- **Nimshal.** At the third meal of Shabbos, as the holy day leaves and the weekday approaches, the soul clings to G-d with longing and fear before the parting.
- **Parts.** the prince → the soul; the prison → the weekday; the last moment → the end of Shabbos; clinging → the soul's longing.
- **Breaks** [ours]. Ours: the prince is truly sent away; the soul can bring the closeness into the week.
- **Principles.** PR-L04, PR-L09
- **Source.** Bnei Machshava Tova (Piaseczner), `Chassidus-txt/R. Kalonymus Kalman Shapira of Piaseczno (1889-1943)/Bnei Machshava Tova (Piaseczno, 1917-1923).txt` line 159: «משל לבן מלך שנגזר עליו להרחיקו מעל אביו ולהשליכו אל הסהר» (like a prince decreed to be sent away from his father and thrown into prison).
- **Recurs.** the Piaseczner, Hachsharas HaAvreichim line 108 (same).
- **See also in SB2.** SB2-BST-11, SB2-BST-18, SB2-BST-24, SB2-MAG-06, SB2-MAG-07, SB2-PIA-01, SB2-PIA-14, SB2-PIA-17, SB2-RBE-10.
- **Guide.** Before something good ends, hold it closer. That hug can carry you through what comes next.

#### SB2-PIA-04. Two people saying Psalms *Domain:* prayer; speech

- **Mashal.** Two people say Psalms. One lacks nothing; he reads David's words like a story. The other is drowning in troubles; he cries 'I am sunk in deep mud' as his own cry, as if David gave him the words only to bring out his own heart.
- **Nimshal.** Prayer is real when the words become your own cry: 'a prayer of the poor man when he is wrapped': he wraps himself in his prayer and his prayer in him.
- **Parts.** the comfortable reader → prayer as reading; the sufferer → prayer as one's own cry; David's words → the given text; wrapping → total identification.
- **Breaks** [ours]. Ours: one need not suffer to pray; the parable shows how to own the words.
- **Principles.** PR-L09, PR-L13
- **Source.** Bnei Machshava Tova (Piaseczner), `Chassidus-txt/R. Kalonymus Kalman Shapira of Piaseczno (1889-1943)/Bnei Machshava Tova (Piaseczno, 1917-1923).txt` line 269: «משל לשני בני אדם שאומרים תהלים» (like two people saying Psalms).
- **Recurs.** Rayatz line 1588 (the rich man and the sufferer); Keter Shem Tov on prayer.
- **Guide.** Try reading a prayer or a poem as if it were written for your exact situation. Let the words become yours.

#### SB2-PIA-05. Clean water in a dirty flask *Domain:* water; vessels

- **Mashal.** Clean water in a dirty flask looks dirty too.
- **Nimshal.** Good powers and feelings, if a person doesn't know how to handle them, look bad, because of the vessel they are in.
- **Parts.** the clean water → one's good energies; the dirty flask → bad habits or untrained self; looking dirty → seeming bad.
- **Breaks** [ours]. Ours: water can be poured out to be cleaned; a person must clean the flask from inside.
- **Principles.** PR-L04, PR-L09
- **Source.** Chovat HaTalmidim (Piaseczner), `Chassidus-txt/R. Kalonymus Kalman Shapira of Piaseczno (1889-1943)/Chovat HaTalmidim (Warsaw, 1928-1932).txt` line 146: «משל למים זכים בצלוחית מזוהמה, שגם המים נראים מזוהמים» (like clear water in a dirty flask: the water too looks dirty).
- **Recurs.** Tzemach Tzedek DM line 108 (water takes the vessel's color, reversed in purpose).
- **See also in SB2.** SB2-TZ-15, SB2-TZ-17, SB2-TZ-18, SB2-TZ-19, SB2-TZ-28, SB2-MHS-10, SB2-RSB-26, SB2-RSB-37, SB2-RYZ-11.
- **Guide.** What feels like a bad part of you might be a good force in the wrong container. Change the container.

#### SB2-PIA-06. The fainting man and the drops *Domain:* body; medicine

- **Mashal.** A man faints and is given various drops, and his spirit returns. But then he has to strengthen himself on his own.
- **Nimshal.** Inspiration from a talk or a teacher wakes you, but the main thing is to work on yourself afterwards in each detail.
- **Parts.** the faint → spiritual numbness; the drops → inspiring words; strengthening himself → one's own work.
- **Breaks** [ours]. Ours: a fainting man can't do anything until revived; a person can start himself too.
- **Principles.** PR-L04, PR-L09
- **Source.** Chovat HaTalmidim (Piaseczner), `Chassidus-txt/R. Kalonymus Kalman Shapira of Piaseczno (1889-1943)/Chovat HaTalmidim (Warsaw, 1928-1932).txt` line 168: «משל לאיש מתעלף ונתנו לו טיפות שונות ושב רוחו אליו» (like a fainting man given various drops, and his spirit returned to him).
- **Recurs.** the Piaseczner's educational writings.
- **Guide.** Inspiration can wake you up. What you do next keeps you awake.

#### SB2-PIA-07. The child learning the alphabet *Domain:* teacher and student; learning

- **Mashal.** A child just starting the alphabet sees a big book in the teacher's hands and wants to know everything in it right now. The wise teacher says: if you're worthy, you'll learn all that later; for now be content with this letter and that. If you grab too fast, you won't even know the alphabet.
- **Nimshal.** In spiritual matters, understand what is put before you now, and don't demand the whole of the higher things at once.
- **Parts.** the child → the beginner; the big book → the deep secrets; the letters → today's step; grabbing → impatience.
- **Breaks** [ours]. Ours: the child will surely grow; in the spirit, the pace is less certain.
- **Principles.** PR-L03, PR-L05, PR-L14
- **Source.** Chovat HaTalmidim (Piaseczner), `Chassidus-txt/R. Kalonymus Kalman Shapira of Piaseczno (1889-1943)/Chovat HaTalmidim (Warsaw, 1928-1932).txt` line 273: «משל למה הדבר דומה, לילד שהתחילו ללמוד עמו אלף בית» (to what is this like? To a child they began to teach the alphabet).
- **Recurs.** R. Aharon's first condition (don't jump ahead of the root); the Maggid's father and child.
- **See also in SB2.** SB2-MAG-01, SB2-MAG-02, SB2-MAG-10, SB2-RSB-18, SB2-RBE-08.
- **Guide.** You don't have to understand everything now. Learn the letter in front of you.

#### SB2-PIA-08. The short-sighted man and the palace *Domain:* perception; king and kingdom

- **Mashal.** A short-sighted man sees from afar something white surrounded by green and black and can't make it out. A sharp-eyed man tells him: the white is the king's palace, the green is the garden, the black is the crowd of ministers. Now the short-sighted man says: yes, now I see it, and even the king seems to shine among them; he is moved with awe.
- **Nimshal.** When we sing or pray old words, we add the new light our soul felt; a guide helps us see what we already half-see.
- **Parts.** the blur → our dim perception; the sharp-eyed man → the teacher or tradition; naming the shapes → explanation; the awe → inner feeling.
- **Breaks** [stated]. Stated: it works only if the short-sighted man sees at least a little.
- **Principles.** PR-L09, PR-L03
- **Source.** Chovat HaTalmidim (Piaseczner), `Chassidus-txt/R. Kalonymus Kalman Shapira of Piaseczno (1889-1943)/Chovat HaTalmidim (Warsaw, 1928-1932).txt` line 299: «משל לאיש קצר ראי' שעומד מרחוק ורואה ואינו יודע להבחין מהו רואה» (like a short-sighted man standing far off who sees and can't tell what he sees).
- **Recurs.** Chovat HaTalmidim; the Rayatz on contemplation.
- **Guide.** You may already see more than you think. Someone just needs to help you name it.

#### SB2-PIA-09. The enemy hiding in the palace *Domain:* king and kingdom; war

- **Mashal.** An enemy sneaked into the king's palace. If the palace keeper fights him with all his strength, the king isn't angry and even helps; every room the enemy is pushed out of, the king quickly moves into. But if the keeper is lazy and secretly makes peace with the enemy, the king is furious.
- **Nimshal.** You can't clear out your bad all at once; start, and give yourself fully to it, and G-d will help and move into every place you clear.
- **Parts.** the palace → the heart; the enemy → bad traits; the keeper → the person; the king moving in → G-d dwelling in the cleared places.
- **Breaks** [ours]. Ours: a king doesn't need a keeper; G-d chose to let us do it.
- **Principles.** PR-L04, PR-L09
- **Source.** Chovat HaTalmidim (Piaseczner), `Chassidus-txt/R. Kalonymus Kalman Shapira of Piaseczno (1889-1943)/Chovat HaTalmidim (Warsaw, 1928-1932).txt` line 125: «משל למה הדבר דומה, למלך שהתגנב אויבו ובא והתקנן בארמונו» (to what is this like? To a king whose enemy sneaked in and settled in his palace).
- **Recurs.** Rayatz line 283 (cleaning the house for the king).
- **See also in SB2.** SB2-MHS-05, SB2-RBE-01, SB2-RYZ-04.
- **Guide.** You don't have to fix everything at once. Clear one room, and something good moves in there.

#### SB2-PIA-10. Climbing a high mountain *Domain:* travel; nature

- **Mashal.** Is someone climbing a mountain only 'there' when he reaches the top? Every step up is already part of the climb.
- **Nimshal.** Every preparation for a mitzvah is already part of the mitzvah, an ascent toward it.
- **Parts.** the climb → the preparation; the summit → the mitzvah; each step → a part of the deed.
- **Breaks** [ours]. Ours: a climber may never reach the top; the preparation still counts.
- **Principles.** PR-L04
- **Source.** Derech HaMelech (Piaseczner), `Chassidus-txt/R. Kalonymus Kalman Shapira of Piaseczno (1889-1943)/Derekh HaMelekh (Warsaw, 1931).txt` line 167: «משל למי שעולה להר גבוה, האם רק בשעה שנמצא כבר על ראש הה» (like one who climbs a high mountain: is it only when he is already on the top).
- **Recurs.** Derech HaMelech line 175.
- **Guide.** Getting ready is part of doing. Every step on the way up is already the climb.

#### SB2-PIA-11. A burning lamp: oil and wick become one flame *Domain:* fire

- **Mashal.** A burning lamp has oil and a wick in it, but do we call it oil and wick? We call it fire; the flame is one.
- **Nimshal.** When soul and body both turn to holiness, they become one holiness.
- **Parts.** oil and wick → body and soul; the flame → the one holy life; calling it fire → seeing the person as holy.
- **Breaks** [ours]. Ours: oil and wick are consumed; body and soul are lifted, not burned up.
- **Principles.** PR-L04, PR-L09
- **Source.** Derech HaMelech (Piaseczner), `Chassidus-txt/R. Kalonymus Kalman Shapira of Piaseczno (1889-1943)/Derekh HaMelekh (Warsaw, 1931).txt` line 169: «משל לנר הדולק, מה יש באש הזה שמן ופתילה» (like a burning lamp: what is in this fire? Oil and a wick).
- **Recurs.** Rayatz line 259 (lamp: oil, wick, light); Ayin Beis line 2416 (the wick).
- **See also in SB2.** SB2-BST-04, SB2-BST-23, SB2-RSB-20, SB2-RSB-21, SB2-RYZ-03, SB2-RYZ-13, SB2-PIA-12, SB2-PIA-13.
- **Guide.** When everything in you burns for one thing, you stop being parts and become one flame.

#### SB2-PIA-12. Holding the candle versus straining to see *Domain:* light; teacher and student

- **Mashal.** One who holds a candle can light for this one and that one. One who has no light in his hand, and strains to see from his dark place, can't help others.
- **Nimshal.** A teacher who is G-d's messenger in his Torah can light up his students; one who only struggles for himself cannot.
- **Parts.** the candle in hand → Torah lived as G-d's mission; straining to see → private struggle; lighting others → teaching.
- **Breaks** [ours]. Ours: struggling people can still help others by honesty.
- **Principles.** PR-L03, PR-L04
- **Source.** Derech HaMelech (Piaseczner), `Chassidus-txt/R. Kalonymus Kalman Shapira of Piaseczno (1889-1943)/Derekh HaMelekh (Warsaw, 1931).txt` line 348: «משל למי שהנר בידו להאיר. גם לזה גם לזה יאיר» (like one who has a candle in his hand to light: he lights for this one and that one).
- **Recurs.** Talmud, Chagigah 15b ('if the teacher is like an angel'); Proverbs 'a candle of mitzvah'.
- **See also in SB2.** SB2-BST-04, SB2-BST-23, SB2-RSB-20, SB2-RSB-21, SB2-RYZ-03, SB2-RYZ-13, SB2-PIA-11, SB2-PIA-13.
- **Guide.** To light someone else's way, hold the light yourself; don't only peer at it from the dark.

#### SB2-PIA-13. The one who sees fire and the blind man who touches it *Domain:* perception; fire

- **Mashal.** One man sees a fire from far off and says he saw something shining. A blind man touched it and says he got burned today. The fire wasn't split into light and heat; each grasped only a part because of his limited sense.
- **Nimshal.** Knowledge in a person and in the Torah is one, though we grasp it in parts.
- **Parts.** the fire → the one truth; light seen far → one aspect; heat felt → another aspect; the limited senses → our limited grasp.
- **Breaks** [stated]. Stated: 'a kind of physical parable, though not fully like it'.
- **Principles.** PR-L07, PR-L08
- **Source.** Derech HaMelech (Piaseczner), `Chassidus-txt/R. Kalonymus Kalman Shapira of Piaseczno (1889-1943)/Derekh HaMelekh (Warsaw, 1931).txt` line 402: «והרי זה כעין משל גופני אף שאינו דומה לו לגמרי, משל לאדם אחד שראה מרחוק אש» (and this is like a physical parable, though not entirely like it: one man saw a fire from afar).
- **Recurs.** the blind men and the elephant (non-Jewish analogue, ours); R. Aharon's 'one person with many powers'.
- **See also in SB2.** SB2-BST-04, SB2-BST-23, SB2-RSB-20, SB2-RSB-21, SB2-RYZ-03, SB2-RYZ-13, SB2-PIA-11, SB2-PIA-12.
- **Guide.** Two people can tell very different stories about the same thing and both be right. Each touched a different side.

#### SB2-PIA-14. The prince who asks for shoes *Domain:* king and kingdom; prayer

- **Mashal.** A prince, far from his father, worries about being far. But after a long time among simple people, suffering from simple things, when his father comes he cries: 'Father, make me shoes!' His real pain is still the distance, but he no longer knows how to say it, so it comes out as 'shoes'.
- **Nimshal.** When we pray only for bodily needs, our real wish deep inside is to be close to G-d; it just comes out dressed as everyday requests.
- **Parts.** the prince → the soul; being far → exile; asking for shoes → prayers for needs; the real pain → longing for closeness.
- **Breaks** [ours]. Ours: shoes are a real need too; the parable doesn't despise them.
- **Principles.** PR-L09, PR-L04
- **Source.** Derech HaMelech (Piaseczner), `Chassidus-txt/R. Kalonymus Kalman Shapira of Piaseczno (1889-1943)/Derekh HaMelekh (Warsaw, 1931).txt` line 1061: «משל לבן מלך שנתרחק מאביו ודואג ומיצר על שהוא רחוק מאביו» (like a prince who went far from his father and worries and grieves that he is far from his father).
- **Recurs.** Derech HaMelech line 459; Esh Kodesh line 62; Maggid, MDL line 112.
- **See also in SB2.** SB2-BST-11, SB2-BST-18, SB2-BST-24, SB2-MAG-06, SB2-MAG-07, SB2-PIA-01, SB2-PIA-03, SB2-PIA-17, SB2-RBE-10.
- **Guide.** Underneath many small requests is one big one: to be close. When you ask for something, notice the bigger ask underneath.

#### SB2-PIA-15. The king who removes his garments *Domain:* king and kingdom; clothing

- **Mashal.** A king wears many garments and removes them one by one; each time, more of himself is seen: first through ten garments, then nine, then eight.
- **Nimshal.** First the light was clothed in the physical; then the Oral Torah revealed higher worlds; then Rabbi Shimon and his companions removed another garment, the Zohar and Kabbalah; each generation sees more.
- **Parts.** the king → G-d's light; the garments → levels of concealment in the Torah; removing one → each new revelation; seeing more → deeper Torah.
- **Breaks** [ours]. Ours: a king undresses by his own choice; revelations also come through the effort of the generations.
- **Principles.** PR-L04, PR-L05
- **Source.** Mevo HaShe'arim (Piaseczner), `Chassidus-txt/R. Kalonymus Kalman Shapira of Piaseczno (1889-1943)/Mevo HaShearim (Piaseczno, 1931-1943).txt` line 95: «משל למלך שנתלבש בהרבה לבושים, ובכל פעם מפשיט את אחד ממלבושיו ורואים יותר את עצמותו» (like a king wearing many garments, and each time he removes one, more of his self is seen).
- **Recurs.** the Rebbe on the spreading of Chassidus; Rayatz on inner Torah.
- **See also in SB2.** SB2-BST-01, SB2-BST-27, SB2-MAG-08, SB2-RBE-02.
- **Guide.** The truth may be under many layers. Each layer you understand shows a bit more of what was there all along.

#### SB2-PIA-16. The man under a heavy load *Domain:* body; speech

- **Mashal.** A man has a heavy load put on him and calls 'So-and-so, so-and-so, come quickly and take it off me!' without pausing between the names.
- **Nimshal.** G-d called 'Moshe, Moshe' from the bush with no pause, because He was in distress with Israel's suffering.
- **Parts.** the load → Israel's suffering; the man calling → G-d's urgent call; no pause → shared pain.
- **Breaks** [ours]. Ours: G-d needs no rescue; the midrash says 'in all their pain He is pained'.
- **Principles.** PR-L04, PR-L07
- **Source.** Esh Kodesh (Piaseczner), `Chassidus-txt/R. Kalonymus Kalman Shapira of Piaseczno (1889-1943)/Esh Kodesh (Warsaw Ghetto, 1941).txt` line 147: «משל לאדם שנתן עליו משוי גדול וקורא פלוני פלוני» (like a man who had a heavy load put on him and calls, 'So-and-so, so-and-so').
- **Recurs.** Exodus Rabbah 2 (source); Esh Kodesh lines 323, 563 (repeated in the Warsaw Ghetto).
- **Guide.** When someone calls your name twice with no pause, they need you now. In hard times, maybe that is how you are being called too.

#### SB2-PIA-17. The captive prince who feels the king near *Domain:* king and kingdom; captivity

- **Mashal.** A prince taken captive among wild, empty men who torment him suddenly feels that the king is near him, and he begins to cry out.
- **Nimshal.** On Rosh Hashanah, in the darkest exile, the soul feels the King near and the shofar is its cry.
- **Parts.** the captive prince → the Jew in suffering; the tormentors → the oppressors; feeling the king near → Rosh Hashanah; the cry → the shofar and prayer.
- **Breaks** [ours]. Ours: in the parable the king's nearness promises rescue; in the ghetto, the Piaseczner does not promise it, only the nearness.
- **Principles.** PR-L04, PR-L09
- **Source.** Esh Kodesh (Piaseczner), `Chassidus-txt/R. Kalonymus Kalman Shapira of Piaseczno (1889-1943)/Esh Kodesh (Warsaw Ghetto, 1941).txt` line 62: «משל לבן מלך שנשבה בין פוחזים ורקים שמענים אותו, והרגיש פתאום שהמלך קרוב אליו» (like a prince captured among wild and empty men who torment him, who suddenly felt the king near him).
- **Recurs.** Maggid, MDL lines 44, 112; Keter Shem Tov line 358; the Rebbe, Melukat line 404.
- **See also in SB2.** SB2-BST-11, SB2-BST-18, SB2-BST-24, SB2-MAG-06, SB2-MAG-07, SB2-PIA-01, SB2-PIA-03, SB2-PIA-14, SB2-RBE-10.
- **Guide.** Even in the worst place, you might suddenly feel someone near. Cry out then. That cry is the realest prayer.

#### SB2-PIA-18. The sleeper stung by a fly *Domain:* body; sleep

- **Mashal.** A man asleep is stung by a fly on his forehead. If he's a merchant, he dreams the sting is a creditor demanding money; if he's something else, the dream fits his own concerns.
- **Nimshal.** A person hears even the soul's call in the language of what fills his mind; to hear the soul's voice as it is, he must first quiet the world's noise.
- **Parts.** the sting → the call from above; the dream → one's own interpretation; the merchant's dream → hearing it as worldly business.
- **Breaks** [ours]. Ours: a sleeper can't choose his dream; a waking person can choose how to hear.
- **Principles.** PR-L09, PR-L04
- **Source.** Hachsharas HaAvreichim (Piaseczner), `Chassidus-txt/R. Kalonymus Kalman Shapira of Piaseczno (1889-1943)/Hakhsharat HaAvrekhim (Warsaw, 1930-1940).txt` line 84: «משל לאיש ישן אשר עקץ אותו זבוב במצחו» (like a sleeping man whom a fly stung on his forehead).
- **Recurs.** Rayatz line 256 (too busy to feel hunger).
- **Guide.** A small sting from inside often turns into whatever story is already on your mind. Try to hear it fresh.

## 5. Counts

- By principle: PR-L01 9, PR-L03 17, PR-L04 158, PR-L05 11, PR-L06 10, PR-L07 38, PR-L08 9, PR-L09 85, PR-L10 1, PR-L11 3, PR-L12 8, PR-L13 4, PR-L14 5, PR-L15 3 - Breaks: ours 154, stated+ours 6, stated 29 - Top domains: king and kingdom 43, nature 26, father and son 22, body 19, craft 17, water 15, commerce 14, speech 13, fire 13, travel 9, teacher and student 9, house 8
