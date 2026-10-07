# METHOD: how the Rebbeim make a mashal, and how to make a new one

**Only One research** · October 1, 2026 · early draft 0.1 · Result [044](../../CONTENTS.md#044) · manuscript 2 of 5 · [Cite](CITATION.bib) · [Quote check](../../verification/catalogue.md#method-how-the-rebbeim-make-a-mashal-and-how-to-make-a-new-one-october-1-2026)

---
*Strand METHOD of the meshalim research for "Only One". Everything here is **ours** (analysis of the data), unless a law or a Rebbe is cited. Data: the 388 meshalim of `SB1` (199) and `SB2` (189); laws: `PRINCIPLES.md` (PR-L01..L15, PR-O01..O14). Machine version: `method.json`. New meshalim built by this recipe: `NEW.md` / `new.json`.*

## In one page

- **Where the Rebbeim look.** The king (65 of 388), craft and building (46), the body (37), father and child (35), the soul's own powers of speech, thought and will (30), and nature (30) make up two thirds of all meshalim. Sun and light, water, fire, commerce and teacher follow. Music, food, travel and love are rare. Counting every domain an entry names, nature and the body rise (49 and 45): many meshalim join a human scene to a natural one.
- **From my flesh.** 154 of 388 (40%) can be checked on one's own body or mind (R. Aharon's law PR-L09). This is the single strongest trait of the corpus.
- **Breaks are stated where the subject is G-d Himself.** Only 65 of 388 breaks are said in the text (17%). They cluster in meshalim of light and sun (11 of 21), the soul's powers (8 of 30) and the mashal about the mashal (5 of 5), and almost vanish in meshalim of service: king 4/65, father 2/35, commerce 1/21, food 0/7, music 0/5. The Baal Shem Tov states none of 30; R. Aharon states 10 of 24.
- **Chaining.** Meshalim are laddered (a word < speech < thought < self), replaced by a better one (the gem over the sun, the name over flint), paired so each carries a different detail (the Rebbe's rule), or surpassed (the candle at noon fits 'counts as nothing' but not 'there is nothing else').
- **Two styles.** Story parables for the heart (the Baal Shem Tov, the Maggid, the Piaseczner) and structural meshalim for the mind (from the Alter Rebbe, and above all the Tzemach Tzedek and the Rashab). A guide needs both.
- **The recipe** (12 steps) starts from the teaching, not the picture; finds the one hinge; looks first in the self; picks a near domain; maps parts; states the break; tests for a body; chains if needed; strips the picture; lands in life; writes a plain version; and runs the test.

## 1. The data

Counted by script from sb1.json (199) and sb2.json (189) = 388 meshalim. Each entry's free-text 'domain' was mapped to one of 19 families; 'primary' uses the first domain named, 'any_mention' counts every family an entry names (so it sums past 388). SB1 'water/fire' entries were split by reading the mashal text. Marker counts are a crude letters-only count over 53 non-OCR files of the Chabad Rebbeim and R. Aharon in Chassidus-txt (OCR scans and reference volumes left out). All counts are ours.

## 1.1 Domains (primary domain of each mashal)

| Domain | Primary | Any mention | Breaks stated in the text |
| --- | ---: | ---: | ---: |
| king and kingdom | 65 | 66 | 4/65 |
| craft, tools and building | 46 | 55 | 4/46 |
| the body and its life | 37 | 45 | 5/37 |
| father and child | 35 | 38 | 2/35 |
| the soul's own powers (speech, thought, will) | 30 | 43 | 8/30 |
| nature (plants, animals, seasons, science) | 30 | 49 | 6/30 |
| commerce, wealth and work | 21 | 24 | 1/21 |
| sun and light | 21 | 25 | 11/21 |
| water (spring, river, sea, vessel) | 19 | 32 | 4/19 |
| fire and light-source (flame, coal, lamp) | 18 | 29 | 3/18 |
| teacher and student | 13 | 20 | 4/13 |
| love, marriage and friendship | 12 | 14 | 1/12 |
| war, captivity and law | 8 | 17 | 3/8 |
| seeing and perception | 8 | 10 | 2/8 |
| food | 7 | 9 | 0/7 |
| music and dance | 5 | 6 | 0/5 |
| travel and the road | 5 | 9 | 1/5 |
| the mashal about the mashal | 5 | 8 | 5/5 |
| inner states and other (joy, shame, prayer, repentance...) | 3 | 19 | 1/3 |

**Reading (ours).** The Rebbeim draw from three rings. The inner ring is the person himself: body, speech, thought, will, sleep, breath (about 67 primary, and many more as a second domain). The middle ring is the household and the court: father, teacher, king, craftsman, merchant (about 180). The outer ring is nature: sun, water, fire, seeds, animals (about 88). The king leads because one picture holds both awe and closeness, both distance and a son. Craft and building lead next because 'making' is the subject of creation, and the craftsman is the picture the Alter Rebbe uses to say what creation is *not* (SB1-029).

## 1.2 By author

| Author | Meshalim | From my flesh (PR-L09) | Breaks stated | King parables |
| --- | ---: | ---: | ---: | ---: |
| Alter Rebbe | 113 | 45/113 | 18/113 | 10/113 |
| Mitteler Rebbe | 62 | 20/62 | 2/62 | 8/62 |
| Rebbe Rashab | 38 | 18/38 | 9/38 | 4/38 |
| Baal Shem Tov | 30 | 12/30 | 0/30 | 14/30 |
| Tzemach Tzedek | 28 | 11/28 | 8/28 | 3/28 |
| R. Aharon of Strashelye | 24 | 4/24 | 10/24 | 5/24 |
| Maggid of Mezritch | 24 | 12/24 | 3/24 | 9/24 |
| Rebbe Rayatz | 18 | 9/18 | 3/18 | 2/18 |
| Piaseczner Rebbe | 18 | 12/18 | 2/18 | 6/18 |
| the Rebbe | 17 | 6/17 | 5/17 | 2/17 |
| Rebbe Maharash | 16 | 5/16 | 5/16 | 3/16 |

## 1.3 Which of R. Aharon's laws the meshalim show

| Law | Count |
| --- | ---: |
| PR-L01 | 18 |
| PR-L03 | 24 |
| PR-L04 | 305 |
| PR-L05 | 18 |
| PR-L06 | 32 |
| PR-L07 | 78 |
| PR-L08 | 20 |
| PR-L09 | 154 |
| PR-L10 | 10 |
| PR-L11 | 7 |
| PR-L12 | 8 |
| PR-L13 | 4 |
| PR-L14 | 6 |
| PR-L15 | 14 |

PR-L04 (the lower is built like the upper) underlies almost every entry (305). PR-L09 (from my flesh) is next (154), then PR-L07 (name the one point and the break, 78). The laws about the reader (stripping PR-L10, literalism PR-L11, wonder PR-L12, felt life PR-L13, sizing PR-L14) are rarely visible inside a single mashal; they belong to how a mashal is *used*. That is why the recipe below gives them their own steps.

## 1.4 Markers of method in the library

Rough letters-only counts across 53 non-OCR files of the Chabad Rebbeim and R. Aharon (ours):

- אין המשל דומה לנמשל (the mashal is not like the subject): 61 - לשכך / לשבר את האזן (only to settle / break the ear): 50 - על דרך משל, spelled out: 209 - כביכול (as if it were possible): 2229 - ומבשרי אחזה (from my flesh I see): 345 - נמשל: 3179

'From my flesh I see G-d' (ומבשרי אחזה) appears about 345 times: the method has a name in the texts, and they use it.

## 2.1 Correspondences that recur (what the meshalim say)

**MP-01 · The part against the whole.** A small thing set beside the larger thing it comes from, to show that it is nothing next to it: one word next to the power of speech, a ray inside the sun, a drop next to the sea, a candle at noon, a penny in a fortune. The most used picture for 'nothing but Him' and 'counts as nothing before Him'. Its break is almost always stated: the part is still the same stuff as the whole, and the world is not 'His stuff'. *Examples:* SB1-009 (One word against the whole speaker), SB1-018 (Sunlight under the open sky), SB1-086 (A drop against the ocean), SB1-183 (A penny to a man with millions), SB2-TZ-06 (The ray of the sun), SB2-TZ-16 (One letter and the speaking soul), SB2-RYZ-01 (A candle at noon)

**MP-02 · Held up every moment.** Something that stays only while a force keeps acting on it: the sea held back by the wind, the stone thrown upward, the spring that never stops, breath in and out. Set against the craftsman's vessel, which stays when he walks away; that picture is brought only to be refuted. *Examples:* SB1-030 (The sea held up by the wind), SB1-029 (The craftsman's vessel), SB2-RSB-11 (The stone thrown upward), SB2-TZ-28 (The spring that never stops), SB2-RSB-01 (Breath in, breath out), SB1-166 (The spring that never stops)

**MP-03 · One life in many parts.** One power that shows up differently in each receiver without dividing: the soul in every limb, the sun's one heat that melts wax and hardens clay, clear water in colored glass, the sun through many windows. This is R. Aharon's model case (PR-L08). *Examples:* SB1-028 (The soul fills the body, but lives in the brain), SB2-TZ-02 (The sun that melts and hardens), SB2-TZ-01 (Water takes the color of the glass), SB2-RSB-38 (Light through windows of many colors), SB1-020 (Sun through many windows), SB1-192 (Names from deeds)

**MP-04 · Narrowing for the receiver.** A great mind makes itself small out of love so a small one can receive: the father who plays at his child's level, the teacher who grinds the idea fine, the funnel, the interpreter, the bridge with measured channels. The picture of tzimtzum and of Torah; and the picture of the mashal itself (PR-L15). *Examples:* SB2-MAG-01 (Father lowers his mind for his child), SB1-046 (A father teaching a small son), SB2-MAG-10 (The funnel), SB2-RSB-18 (The interpreter in between), SB1-165 (The bridge with chambers), SB1-195 (The wise man's foreign garment)

**MP-05 · Hiding in order to be found.** The one who hides wants to be found: the father who steps back so the child walks, who hides so the child searches, the king's walls that are illusion, the king in disguise known by the thickness of the guard. The hiding is part of the love. *Examples:* SB2-BST-20 (A small child learning to walk), SB2-RBE-03 (The father hides from his little son), SB2-MAG-03 (Father shows himself and walks on), SB2-BST-01 (Walls that are only an illusion), SB2-BST-27 (The king in disguise at war), SB1-182 (The son bowed when the father hides)

**MP-06 · The low shows the high.** The greatness of a source shows at the lowest point it reaches: the seal clear only in dark wax, the torch seen from far, the overflowing barrel, the highest stone falls farthest. The picture of 'a home in the lowest place'. *Examples:* SB1-119 (A seal in a brilliant gem), SB2-TZ-25 (The seal shows in wax, not in the gem), SB1-057 (A great fire seen from far), SB1-058 (The barrel that overflows), SB2-RBE-07 (Three parables: the torch, the barrel, the seed), SB1-076 (The falling wall)

**MP-07 · Down in order to go up.** A loss or descent that is the way to a greater rise: the seed that must rot, the arrow drawn back, water made sweet by passing through earth, dancers who step apart. The picture of the soul's descent and of teshuvah. *Examples:* SB1-079 (The seed must rot), SB2-MAG-12 (The seed must rot), SB1-101 (The arrow drawn back), SB1-065 (Living water through the earth), SB2-TZ-19 (Groundwater purified through the earth), SB2-RSB-06 (Dancers who step apart)

**MP-08 · The flame that wants its source.** Fire's upward pull and the spark drawn into the torch picture the soul's longing; the coal with one spark pictures the love that is never fully out. *Examples:* SB1-008 (The flame that pulls upward), SB2-RYZ-13 (A spark rising into the torch), SB1-107 (Glowing coals and dim ones), SB1-148 (The spark near the flame), SB2-BST-04 (Keep a spark in the coals)

**MP-09 · The reaction from the core.** What a person does before he decides: the hands that clap at good news, the plain scream, the love of one's own life, the thing all of life hangs on. These point to the essence of the soul, above reasons. *Examples:* SB1-121 (Clapping at good news), SB1-122 (The plain scream), SB1-064 (Loving like you love your own life), SB1-042 (The thing your life hangs on), SB1-159 (Wanting to live), SB2-RSB-27 (What your life depends on)

**MP-10 · The prince far from home.** The king's son in captivity, exile or a village; he forgets, asks for shoes, presses close at the last moment, feels the king near. The largest story family; it carries the soul in the body and in exile. *Examples:* SB1-017 (The prince freed from prison), SB1-140 (The king's son sent into exile), SB2-BST-11 (The minister who dressed like the prince), SB2-MAG-06 (The captive prince), SB2-PIA-14 (The prince who asks for shoes), SB2-PIA-03 (The last moment before exile), SB2-PIA-17 (The captive prince who feels the king near)

**MP-11 · The rope and the bond.** A rope of 613 threads, pulled at the bottom and moving at the top, doubled at the knot; a covenant cut from one thing. The picture of the soul's tie through mitzvos and of teshuvah. *Examples:* SB1-037 (The rope of many threads), SB1-038 (Pull the bottom of the rope), SB1-039 (The retied rope is doubled), SB2-RSB-30 (The rope tied above), SB2-RSB-34 (A thick rope of 613 threads), SB1-141 (The covenant: one thing cut in two)

**MP-12 · Before the king.** What closeness does to a self: the courtier who stands always before the king like a stone, the one too close to speak, the commoner who learns awe from the ministers' bowing. The picture of bittul and awe. *Examples:* SB1-115 (Always standing before the king), SB2-MAG-20 (A minister who stands always before the king), SB2-MHS-12 (Bowing very close to the king), SB2-RSB-07 (Too close to speak), SB1-176 (Seeing the king, hearing of the king), SB2-RSB-24 (The commoner who sees the ministers bow)

**MP-13 · Holding the person through the garment.** You hug a king in his robes, a wise man through his body, lead a soul by taking the hand. The picture of Torah and mitzvos: plain physical things through which one holds Him. *Examples:* SB1-002 (Hugging the king in his robes), SB1-060 (Hugging a wise man), SB1-063 (Take him by the hand), SB1-153 (The teacher who reaches a small child)

**MP-14 · Asleep, not gone.** Sleep, a locked treasure, a scholar who stopped studying: something present but not showing. The picture of the hidden love and of what remains under hiding. *Examples:* SB1-174 (Sleep: the life is still there), SB1-006 (Evil asleep during prayer), SB1-138 (The scholar who stopped studying), SB2-MHS-09 (Treasure locked in a chest), SB2-RYZ-09 (Exile is sleep)

## 2.2 Mechanics (how the meshalim are built)

**MP-15 · Marking the break out loud.** The text names where the mashal fails, with fixed formulas: 'the mashal is not like the subject at all' (about 61 times in the Chabad texts), 'only to settle the ear' (about 50), 'if it were possible', 'even this is too little', 'not like it in every way'. Only 65 of 388 breaks are stated (17%), and they cluster where the subject is what G-d is: sun and light 11/21, the mashal about the mashal 5/5, the soul's powers 8/30, against king 4/65, father 2/35, commerce 1/21, food 0/7, music 0/5. So: picture His unity and say where it fails; picture how to serve and the break can stay quiet (it is supplied by the listener's sense). By author the Baal Shem Tov states 0/30, R. Aharon 10/24, the Alter Rebbe 18/113. *Examples:* SB1-031 (Soul in body, G-d in world: the warning), SB1-086 (A drop against the ocean), SB1-099 (A fly in the corner), SB1-032 (Light inside the sun's ball), SB1-183 (A penny to a man with millions), SB2-RYZ-01 (A candle at noon), SB2-RSB-35 (Sea water that covers is not like nature)

**MP-16 · The break is the next step.** The place where the mashal fails becomes the next question, and the answer brings Him nearer, not further (PR-O02, PR-O05). Sunlight in the air is far from the sun, but creatures never leave their source; a king gets only obedience, He gives life; 'king' over trees and stones does not fit, so only His choice makes it fit. *Examples:* SB1-018 (Sunlight under the open sky), SB1-071 (A king of trees and stones), SB1-029 (The craftsman's vessel), SB1-183 (A penny to a man with millions), SB2-RSB-03 (A gem that shines), SB1-180 (Fire in the flint)

**MP-17 · Chaining: mashal on mashal.** Four ways one mashal is joined to another. (a) A ladder inside one picture: a word is little next to speech, less next to thought, nothing next to the self. (b) Replacing a weaker mashal with a better one: the gem fits better than the sun, the name better than flint or coal. (c) Two or three meshalim for one teaching, each carrying a different detail (the Rebbe's rule). (d) A higher step beyond the last mashal: the candle at noon fits 'counts as nothing', but 'there is nothing else' goes past it. Behind all four: every level is a mashal for the one above (Shlomo's 3,000; Maharash, Rashab). *Examples:* SB1-009 (One word against the whole speaker), SB2-RSB-03 (A gem that shines), SB2-TZ-04 (A person's name), SB2-TZ-05 (Flame bound in a coal, fire in a flint), SB2-RBE-07 (Three parables: the torch, the barrel, the seed), SB2-RYZ-01 (A candle at noon), SB1-190 (The twinkling star), SB2-MHS-02 (Everything below is a mashal for above)

**MP-18 · The impossible case.** A mashal built on what cannot happen, so the listener feels the gap: if the sun's ball itself came in the window; walls that are pure illusion; the eye allowed to see the life in each thing. *Examples:* SB1-131 (The sun's ball through a window), SB2-BST-01 (Walls that are only an illusion), SB1-099 (A fly in the corner)

**MP-19 · From my flesh: test it on yourself.** About 40% of all 388 (154) are tagged PR-L09: the listener can check the mashal on his own body or mind right now. Speech and thought (one word against the speaker), the soul in the limbs (the brain feels the toe), attention (you feel your own affairs because you never look away), the self that does not age, the will to live. Sometimes the self is used as an argument, not a picture: you cannot grasp your own soul, how much less Him. The Piaseczner has the highest share (12/18), R. Aharon the lowest (4/24, he writes about method). *Examples:* SB1-009 (One word against the whole speaker), SB1-024 (The brain feels the toe), SB1-073 (Knowing you are there), SB1-074 (Your own matters feel bigger), SB1-059 (The self that never ages), SB1-072 (Can you grasp your own soul?), SB2-RSB-15 (Wanting without a reason you can give)

**MP-20 · How much more (a fortiori).** The mashal shows a human case and then says 'how much more': if love wakes love between equals, how much more when a king stoops; if a craftsman pities his handiwork, how much more He. The mashal sets a floor, the nimshal goes past it. *Examples:* SB1-026 (The great king and the lowly man), SB1-117 (True height raises the low), SB1-136 (Pity for your own handiwork), SB2-MAG-14 (The craftsman paid for labor), SB1-072 (Can you grasp your own soul?)

**MP-21 · Story parable and structural mashal.** Two styles. The Baal Shem Tov and the Maggid tell stories (14 of the Baal Shem Tov's 30 are king stories) aimed at the heart, with unstated breaks. From the Alter Rebbe and strongly from the Tzemach Tzedek on, the mashal is a structure (sun and ray, name, letters, colored glass) aimed at the mind, compared, chosen and broken in the text. The Piaseczner returns to story and inner psychology. A guide needs both: the story to move, the structure to be exact. *Examples:* SB2-BST-01 (Walls that are only an illusion), SB2-BST-24 (The prince who gets a letter in the village), SB2-TZ-04 (A person's name), SB2-TZ-01 (Water takes the color of the glass), SB2-PIA-01 (The father who visits his imprisoned son), SB2-PIA-14 (The prince who asks for shoes)

**MP-22 · The mashal about the mashal.** Meshalim that describe the mashal itself: the wise man's foreign garment, the vessel for the idea, thin parable and riddle, the mashal higher than the idea, the teacher-student mashal that does not fit. They teach that the method is itself a case of the teaching: G-d hiding in a world is a teacher hiding wisdom in a mashal. *Examples:* SB1-195 (The wise man's foreign garment), SB2-MAG-24 (The mashal is a vessel for the idea), SB2-TZ-22 (A mashal versus a riddle), SB2-MHS-04 (The mashal is higher than the idea), SB2-RYZ-06 (The root of the mashal is higher), SB2-RBE-08 (The teacher-student parable does not fit)

**MP-23 · The mashal that turns to a deed.** The strongest service meshalim end in something to do now: use the open door for closeness (not only for the business that opened it), turn your face around, keep one spark in the coals all day, do not answer the heckler, go to the King not to his messenger. *Examples:* SB2-PIA-01 (The father who visits his imprisoned son), SB1-105 (Back to back), SB2-BST-04 (Keep a spark in the coals), SB1-015 (The heckler at prayer), SB2-BST-16 (The angry messenger and the loving messenger)

## 3. What makes the strongest ones strong

- You can test it on yourself in ten seconds (one word against your power to speak; you feel your soul without seeing it). - It has one hinge you can say in a sentence, and every other detail serves that hinge. - The break is named, and the break itself teaches something nearer (the sun's light is far from the sun; you never are). - The picture is ordinary and daily (bread, rope, candle, sleep), so life keeps reminding you of it. - It ends in a turn of the heart or a deed: turning your face, using the open door. - It recurs: the sun and its ray passes from the Alter Rebbe to the Tzemach Tzedek, the Rashab and the Rayatz, each sharpening its break.

*Our ten strongest from the source books:* SB1-009 (One word against the whole speaker), SB1-018 (Sunlight under the open sky), SB1-105 (Back to back), SB1-030 (The sea held up by the wind), SB1-039 (The retied rope is doubled), SB2-RBE-01 (Living in a friend's house), SB2-RYZ-01 (A candle at noon), SB2-PIA-01 (The father who visits his imprisoned son), SB2-BST-01 (Walls that are only an illusion), SB2-PIA-14 (The prince who asks for shoes).

The weakest meshalim in the corpus, by the same tests, are those that need a story to be accepted before they work (an angry king who must be appeased, a harlot hired by a king): they carry their point but invite the listener to run the details (SB1-004, SB2-BST-22). The Rebbeim use them with the break understood; a guide today must say it.

## 4. The recipe: making a new true mashal

For a person or an AI guide. Each step has a check and the laws it serves.

**Step 1. Hold the teaching first.** Write the teaching (the nimshal) in one plain sentence, and find a verified source line for it. Know which kind it is: how He fills and holds the world and the soul, or how a person serves. Do not start from a nice picture and look for a teaching to hang on it. *Check:* Can I say the point without any picture, and show the line it comes from? Do I hold it from inside, not only as words? *Laws:* PR-L03, PR-L02, PR-O06, PR-O10

**Step 2. Name the hinge.** Say the one point the mashal must carry: one in many; made every moment; nothing next to its source; hidden so as to be found; low shows high; down in order to go up; the bond moves both ends. *Check:* One sentence, one point. If there are two points, plan two meshalim (step 8). *Laws:* PR-L07, PR-L08

**Step 3. Look in the self first.** Ask where the listener already lives this point from inside: breath, speech and thought, attention, waking from sleep, loving a child, a name called across a room, the body obeying the will. Only then look outside to nature and to modern life (screens, music, cooking, travel, sport, medicine). *Check:* Can the listener test it on himself, now, without believing anything? *Laws:* PR-L09, PR-L04, PR-O04

**Step 4. Pick a near domain.** Choose a picture from the listener's own day so that it comes back to him as a reminder. The farther the listener is from the source, the more detail and the more familiar the picture must be; for someone near, a short hint is enough. Prefer things that work, not things that are fashionable. *Check:* Would this person meet this picture again this week? Does it need its own explaining (then it is too far)? *Laws:* PR-L14, PR-L15, PR-L01

**Step 5. Map the parts.** List each part of the picture and what it stands for. Keep the parts that point to something true; cut the rest, because a listener will ask about every detail. *Check:* Is every detail either meaningful or harmless? Could someone 'run' a detail into a false claim? *Laws:* PR-O14, PR-L07

**Step 6. Find the break and say it.** Look for where the picture is two and He is one; where the picture changes or is affected and He is not; where the picture is made from something that was already there and the world is made from nothing; where the picture is in space or time. Choose the break that brings Him nearer. Write it down; say it aloud when the subject is what G-d is. *Check:* Have I stated at least one break? Does the break point to more closeness, not less? *Laws:* PR-L07, PR-O01, PR-O02, PR-O05

**Step 7. Test for a body.** Read the mashal as a literal-minded person would. Does it give G-d a body, a place, a size, a mood, a need, parts, or make Him one more thing in the world (a bigger computer, a stronger signal)? Does it picture what He is in Himself rather than how He relates to the world? *Check:* If taken literally, would it make Him physical or divided? If yes, fix the picture or drop it. *Laws:* PR-L06, PR-L11

**Step 8. Chain if needed.** If one picture cannot carry everything, add a second for the other detail, or build a ladder: 'this is like X; more than that, Y; and even Y falls short'. Name which picture carries which point. *Check:* Does each mashal in the chain carry its own detail? Does the chain end above the last picture? *Laws:* PR-O12, PR-L05, PR-L12

**Step 9. Strip the picture.** After the mashal lands, say the point again without it, and return to the source line. The picture was a handle; put it down. *Check:* Can the listener say the point without the picture? Is what is left in his mind His unity, not the image? *Laws:* PR-L10, PR-O08, PR-L01

**Step 10. Land it in life.** End in something felt or done: a moment of noticing, a turn of attention, one deed, and in wonder rather than 'now I have it figured out'. *Check:* What will the listener do or notice differently in the next hour? Does it end in wonder? *Laws:* PR-L13, PR-L12

**Step 11. Write the plain version and the risk.** Write a 1-3 sentence version with no religious words, for someone who would stop listening at the first technical term. Write who it suits and what could go wrong. Mark it as ours. *Check:* Would a twelve-year-old follow it? Would someone in pain be hurt by it? *Laws:* PR-L14, PR-L15

**Step 12. Run the test.** Run the ten-point checklist of PRINCIPLES.md and the failure tests below. If it fails one, go back to the step that fixes it. *Check:* All tests pass, or the risk is written down. *Laws:* PR-L02

### A worked example (ours) *Teaching:* every thing is being brought into being now, from nothing, by His word (Shaar HaYichud ch. 1). *Hinge:* it stays only while it is being given. *Self first:* breath; attention. *Near domain:* a phone screen. *Parts:* the still picture = the world; the many redraws each second = His word renewing it; the power = His giving. *Break:* the screen's pixels and glass exist without the power and the maker is outside; the world has nothing of its own under the 'picture', and He is not outside. *Body test:* He is not 'electricity'; the picture is of the world's dependence, not of Him. *Strip:* 'everything you see is being given right now'. *Land:* look at one object and say 'now'. This is NEW-02 in `NEW.md`.

## 5. Failure modes

**Corporealizing.** The picture gives Him a body, a place, a size or a location: 'G-d is a giant server', 'He is up there', 'He is the biggest energy'. Higher becomes taller, infinite becomes very big. *Fix:* Move the picture from what He is to how He gives life and is one with what He gives (PR-L06). Add a break that names the bodily feature that does not apply. Prefer pictures of relation (a voice and its speaker, a life and its limbs) over pictures of a large object. (PR-L06, PR-L11)

**The mashal taken literally.** The listener keeps the picture as the truth: 'so the world is a simulation and He is the programmer', 'so my soul is a piece cut off Him'. Then the picture divides Him and makes the listener think he understands. *Fix:* State the break; strip the picture (step 9); return to the source line; avoid domains that already carry their own theory (simulation, 'the universe', energy-healing talk) or name and deny that theory in the break. (PR-L11, PR-L10, PR-L12)

**Cute but untrue.** A clever surface likeness with no true correspondence at the root, e.g. 'G-d is like Wi-Fi: invisible and everywhere'. It misses the point (we are not connected to Him from outside; we exist from Him), and it makes Him one more invisible thing. *Fix:* Check the hinge against the teaching (step 2). If the hinge is not the teaching's own point, drop the picture even if it delights. If you keep it, make the break carry the truth. (PR-L03, PR-L07, PR-O14)

**Too abstract.** The mashal itself needs explaining (quantum fields, set theory, a technical feature most people do not use). It moves nothing and lets the speaker feel clever. *Fix:* Go back to the self and to daily life (step 3). Use what the listener touches. Keep the technical version for the person who lives in it. (PR-L09, PR-L14, PR-L13)

**Preachy.** The mashal is a stick: it is told to make someone feel guilty or small. It aims at the speaker's point, not at the listener's seeing. *Fix:* Aim at sight and feeling, not at blame (PR-L13). Let the listener find himself in it; speak at his level as the minister dressed like the prince (SB2-BST-11). Put the deed as an invitation. (PR-L13, PR-L15)

**Running every detail.** Once the hinge works, the listener (or the speaker) runs the other details: 'if He is the author, are we just characters with no choice?', 'if the soul is a battery, does it run out?' *Fix:* Name the one point (step 2) and cap the correspondences (step 5). Say ahead of time which details do not carry over. (PR-L07, PR-L08)

**A break that pushes Him away.** The picture leaves Him far: the clockmaker who winds the world and walks off, the landlord who owns but does not live here. This is the craftsman error the Alter Rebbe refutes (SB1-029). *Fix:* Choose pictures where the source stays present (step 6). If the picture is distant, the break must say: He is nearer than this. (PR-O02, PR-O05, PR-L07)

**Making pain small.** Using a mashal to explain someone's suffering to them ('it is like a workout', 'like a vaccine'). Even a true mashal said at the wrong time is cruel, and can be heard as 'your pain is not real'. *Fix:* For pain, use meshalim of being held, not of being explained. Offer the explaining ones only to someone who asks, for his own reflection, and say in the break that the picture does not make the pain less real (compare SB2-BST-17). (PR-L13, PR-L14)

**Cliché.** The picture is so worn that it brings no wonder (the 'ocean and the wave' said without care). The listener nods and nothing moves. *Fix:* Find the one fresh detail the listener has not noticed in a familiar thing, or use the self (step 3). End in wonder, not in recognition. (PR-L12, PR-L13)

**Wrong size for the listener.** Too thin for someone far (a hint that does not reach), or too long for someone near (a lecture where a word would do). *Fix:* Size the mashal to the listener (PR-L14): more detail and a more familiar picture for the one far away; a short hint for the one near. (PR-L14)

## 6. The test (run before using a new mashal)

1. Can I state the teaching without the picture and cite a verified line for it? (PR-L03)
2. Is the picture about how He gives life to and is one with the world and the soul, not about what He is in Himself? (PR-L06)
3. Can the listener check it on himself, now? (PR-L09)
4. Can I name the one hinge in one sentence? (PR-L07, PR-L08)
5. Have I written at least one break, and does it bring Him nearer? (PR-L07, PR-O02, PR-O05)
6. If someone took it literally, would He become a body, a place, a part or a mood? (PR-L11)
7. Does any detail, if pushed, lead to a false claim? Have I said which details do not carry over? (PR-O14)
8. Is it the right size for this listener? (PR-L14)
9. After it lands, can the listener say the point without the picture? (PR-L10)
10. Does it end in a felt moment or a deed, and in wonder? (PR-L12, PR-L13)
11. Is it free of blame, and safe to say to someone in pain? (failure: preachy; making pain small)
12. Is it ours, and marked as ours, with no imported copyrighted wording?

--- *Status: all counts, patterns, rankings, recipe and failure modes are ours. The laws cited are R. Aharon's and the Rebbeim's as set out (with verified Hebrew) in `PRINCIPLES.md`; mashal ids point to `SB1.md` / `SB2.md`, where each has its verified source.*
