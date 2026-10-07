# The technique library: forty-seven ways in, for anyone

**Only One research** · October 1, 2026 · early draft 0.1 · Result [042](../../CONTENTS.md#042) · manuscript 2 of 3 · [Cite](CITATION.bib) · [Quote check](../../verification/catalogue.md#the-technique-library-forty-seven-ways-in-for-anyone-october-1-2026)

---
*Chassidus Unity Index, transformation strand TQ, 2026-10-01. Machine-readable twin: `techniques.json` (an array of the 47 techniques below, every field the page needs). Written for "Only One", its chat guide and its live guided-sitting room.*

**What this is.** Forty-seven real meditative and contemplative techniques, each taken from a Chabad or wider Chassidic practice, restated so anyone can do them without belief, and specified for a live session: the exact lines the guide speaks, the silence after each line, a one-tap check-in, and what to do for each answer. Each also has a second script for someone who believes in G-d, wherever the wording differs.

**The aim (the owner's words).** "Ultimately the goal is to bring people closer to G-d, not the dogmatic version but the Chassidic one: you find G-d within yourself. A path of bringing people closer to their true self, using the methodology of Chassidus." So every technique here is framed as a way toward the person's true self, the place where the self at its root and its Source meet. The Piaseczner says it in one line:

> «שידיעת ד׳ היא בידיעת עצמו» (*the knowledge of G-d is in the knowledge of oneself*) · Esh Kodesh (the Piaseczner), `Chassidus-txt/R. Kalonymus Kalman Shapira of Piaseczno (1889-1943)/Esh Kodesh (Warsaw Ghetto, 1941).txt`, line 542

The universal script speaks of the deepest self, of what gives you being, of the Source. The believer's script names the meeting with G-d openly. Neither asks anyone to believe anything in order to begin (`universal/TRANSLATION.md` section 1: the moment of silence as the pattern).

**What this builds on, and does not repeat.** `meditation-technology/CATALOGUE.md` (39 techniques, 7 families, with sources) and `TECHNOLOGY.md` (25 techniques as protocols for a text chat) are the ingredients; this file turns them into live, timed, branching sittings. States are cited from `consciousness-map/MAP.md` (MAP S01-S86) and `depths/FULL-DESCENT.md` (FD S01-S35); stages from `stage-book/BOOK.md` and `integration/MAP.md`; methods from `animal-soul/METHODS.md` (M01-M71); guards from `lights-and-vessels/PS.md` (PS-14: the transparent self; unreality is a stop sign), `VS.md` (readiness), `GM.md` (the teachers' sittings) and `clinic/` (DX, P1, P2, BODY). The framework that sequences these techniques in a session and over weeks is the sister strand, `transformation/FRAMEWORK.md`.

**Marks.** *Stated* means a source says it: the line "the practice in the source" and every Hebrew quotation. Everything else is **ours**: the universal restatement, the true-self framing of each technique, the mechanism in plain words, every dose and silence, every scripted line (both versions), the check-ins and adaptations, the counterfeit fixes, the contraindications, the body notes and the daily-life forms. Every Hebrew line (91 distinct lines) was copied from the earlier research files and re-checked with `python3 "Chabad Library/medicine-map/tools/find_he.py" verify FILE "..." --line N` in strict mode, run from `/home/user/Research`: all FOUND. No new Hebrew was added. OCR marks an uncorrected scan. The science is in our own words, with links (section 6); none of it has been tested on these techniques as practised.

**Contents.** 1 How a technique is built · 2 Rules that hold for every technique · 3 The library at a glance · 4 Where to start: from the person's state now · 5 The techniques, by the state they open · 6 The science, with links · 7 Whose is what

## 1. How a technique is built

Every entry has the same parts, in the same order, so the page can render any of them (field names from `techniques.json` in brackets).

| Part | What it holds |
| --- | --- |
| Aim (`aim`) | Which universal state it opens (ST01-ST13, below), with the source states it maps to. |
| Level (`level`) | L1 first session · L2 weeks 1-2 · L3 later. |
| Toward the true self (`toward_the_true_self`) | How this technique brings the person closer to who they are at the root. |
| The practice in the source (`source`) | The Chassidic practice it comes from, the verified lines, and the earlier files it builds on. |
| How it works (`how_it_works`, `science`) | The mechanism in plain words, with the contemplative science that fits it. |
| Dose (`dose`) | Minutes and how often. |
| The live script (`script`, `script_believer`) | One line per step, the silence after it in seconds. The believer's version marks only the lines that change. |
| Check-in and adapt (`checkin`, `adapt`) | One question, three or four taps, plus the always-present exit. Each tap has an action. |
| Counterfeit and fixes (`counterfeit`) | What the fake version looks like, and what the guide does. |
| Contraindications (`contraindications`) | Who should not do it, or when. |
| Body (`body`) | Posture, eyes, hands. Breath only as something noticed, never the object. |
| In daily life (`daily_life`) | The seconds-long form that carries it into the day. |

**The thirteen states** are the framework's (`FRAMEWORK.md` section 2, `framework.json` states, same ids). This file only says which techniques open each one.

| id | State | In plain words | Source states | Tier |
| --- | --- | --- | --- | --- |
| ST01 | Here | The flood slows. You are in one place, in this body, in this room, and not being dragged. Not asleep and not blank: there is room for one true thing. | MAP S32 Quiet; MAP out of S01 Scattered | door |
| ST02 | The watcher | You can see a thought, a mood or a verdict about yourself from one step to the side. It is something you have. It is not all you are. The one who looks is still here, warm, in the body. | MAP S34 Two voices; MAP S11 The verdict (from outside); FD S04 Don't leave yourself out | door |
| ST03 | Before | The room changes posture. You are not alone in it. You are seen, and kindly. Something like dignity, not dread. | MAP S33 Before Whom | door |
| ST04 | Given right now | This moment is being given, not kept. The cup, the room, the floor, and you too, are not holding yourselves up. There is a floor under the floor. | MAP S65 Given right now; MAP S84 Trust; FD S01 Made right now | middle |
| ST05 | Held | Held all around by something too big to grasp, and filled from inside, each thing to its own size. Safe at the level of being, while you still do your part. | MAP S66 Filled from inside; MAP S67 Surrounded; MAP S84 Trust; FD S02 All of it is His word | middle |
| ST06 | It is so | The idea stops being an idea and becomes a fact you see, as plain as the table. You no longer have to argue for it. | MAP S25 The line takes hold; MAP S27 Knowing that holds; FD S03 From knowing to seeing | middle |
| ST07 | The heart answers | Something moves under the thinking: warmth, tenderness, a pull toward what is good that you did not make and that wants nothing back. Often a feather, not a fire. | MAP S39 The heart answers; MAP S41 The hidden love wakes; MAP S42 Love like water; MAP S54 Compassion for the soul; FD S24 Asleep, not dead; FD S25 The want of the want | middle |
| ST08 | Awe, small and glad | Hushed before something vast and near. Small, but not crushed. Light and glad at the same time. | MAP S45 Lower awe; MAP S46 Higher awe; MAP S50 Joy and bittul together; FD S10 Never reaching, always longing; FD S11 The mind touches and bows | middle |
| ST09 | Less in the way | For a moment you are not holding yourself up. Nothing to defend, nothing to prove. Someone is still here, lighter, and what is true comes through. | MAP S56 The self quieted; MAP S58 A ray in the sun; FD S05 The humility that watches itself; FD S06 Love still has a lover; FD S07 You never stood apart | deep |
| ST10 | The self beneath the layers | Under every mood, role and verdict there is a simple self that nothing ever reached, and a will in it that you did not choose and cannot be argued out of. Here knowing yourself and knowing what gives you being turn out to be one knowing. | MAP S60 The essential bond; MAP S61 Will and delight above reason; FD S13 Under the love, a will; FD S14 Under all your names; FD S15 Cannot be separated, from either side | deep |
| ST11 | The world see-through | The world comes back real, solid and other, and not on its own. The cup is a cup, and it is given. Plain, no drama. | MAP S63 The world held; MAP S64 The plainest thing; MAP S68 The hiding seen as His; FD S29 The world given back as His; FD S34 Plainness is His simplicity | deep |
| ST12 | The quiet after | The reaching settles. You come back down into the room carrying it, and nothing is lost. The coming back is the deeper half. | MAP S48 Returning; FD S27 The bottom does not drown you; FD S28 The return is the deeper half | return |
| ST13 | Acting from it | It goes into the hand: one act, done plainly, for its own sake. The person in front of you is real, and held by the same One. | MAP S81 The deed in the hand; MAP S82 The home below; MAP S86 The other held; FD S32 The deed in the hand; FD S33 Found only below; FD S34 Plainness is His simplicity | return |

**Key to the framework's technique names** (`framework.json` techniques_key slugs, mapped to ids here; also in each record as `framework_keys`).

| framework key | technique(s) |
| --- | --- |
| `arrive` | T01 Arrive as you are |
| `quieting` | T04 Watch the thoughts until the head empties |
| `watcher` | T05 Look at it, not in it, T06 Since when? |
| `moment-of-silence` | T02 The minute of silence |
| `before-whom` | T07 Before whom, T08 Seen |
| `held-word` | T21 The held word |
| `given-now` | T10 Made, now, T11 The breath that comes by itself |
| `held-around` | T15 The child before the parent, T16 Nothing else holds power |
| `detail` | T13 Walking it down to one thing, T18 One line, held long |
| `mashal` | T12 The picture, and where it breaks |
| `picture` | T15 The child before the parent |
| `binding` | T20 Come back without a fight |
| `two-knowings` | T19 Two knowings |
| `layers` | T34 Under all your names |
| `niggun` | T24 The hum that sings itself |
| `own-words` | T28 Your own words, T29 One word only |
| `cry` | T30 The silent cry, T27 The cry of one who feels nothing |
| `want-of-want` | T27 The cry of one who feels nothing |
| `mercy` | T26 Mercy for the spark |
| `good-point` | T25 Gather the good points |
| `shema-one` | T09 The Shema of One |
| `edge` | T31 The edge of knowing |
| `quiet-after` | T40 The quiet after, T41 Transparent, not gone |
| `plainest` | T38 The meal received |
| `other-held` | T47 Loving the next person first |
| `slow-deed` | T43 The deed done slowly |
| `carry-line` | T44 The carried line |
| `waking-thanks` | T14 The first words on waking |
| `bedtime-return` | T46 The evening look-back that ends in good, T17 The bedtime return |
| `grounding-exit` | T42 Come down: feet, hands, the room |

**The one-tap actions** *(ours; the page implements exactly these six)*.

| do | meaning |
| --- | --- |
| `deepen` | Go one step further: run the named technique next (or repeat this one at its longer dose). |
| `again_smaller` | Repeat this technique, shorter and simpler (half the silences, the easiest version of each line). |
| `switch` | Change technique: run the named one, which reaches the same state another way. |
| `come_up` | Bring the person up gently: run T42 (feet, hands, the room), then consolidate. No further depth this session. |
| `close` | It has done its work: go to consolidate (name it in their words), then carry (one act, one line). |
| `stop` | Stop the sitting now. Safety protocol: ground (T42), plain words, check danger, offer a person. No more depth today. |

## 2. Rules that hold for every technique

*Ours, built on the guards already stated in PS-14, VS-19, VS-25, MAP S20 and S21, clinic BODY, and the research on adverse effects (section 6).*

1. **An exit on every check-in.** Every check-in carries a fourth or fifth tap, "I need to stop", which runs `stop` and T42. The page never hides it.
2. **Stop signs end depth for the day.** Feeling unreal or not oneself, panic, a trauma memory flooding in, racing thoughts with no sleep, a sense of being chosen or receiving messages, a grief flood, or any thought of not wanting to live: stop the technique, run T42, speak plainly, check for danger, offer a person. Never answer a stop sign with a deeper technique. (PS-14: unreality is a stop sign, not a summit.)
3. **Down before out.** Every sitting that went deep (T31, T34, T32, or any `deepen` past two steps) ends with T41, then T43. Running out without coming back does not last (PS-15) and is where harm starts.
4. **Ask for the thinking, never demand the feeling.** No line ever tells the person what they should feel. If nothing comes, that is an answer, and the practice still counts (TECHNOLOGY heart_after; MAP S03).
5. **Never forceful.** Lines are said softly; the Piaseczner warns that force wakes the ego and the Tanya forbids sadness during the practice. Silences are offered, not imposed: the page may let the person tap "next" early.
6. **Breath is noticed, never worked.** The sources contain no breathing technique (CATALOGUE B6). No counting, holding or pacing anywhere in this library. If attention to breath causes tightness, the anchor moves to the feet.
7. **The believer's script only when it fits.** The guide reads which script fits from the person's own words, never by asking about religion (TRANSLATION section 4). Jewish ritual words (the Shema, Modeh Ani, the blessing) are offered only to someone for whom they are their own.
8. **Dose stays small.** Single sittings in the library run 1-15 minutes. Intensity, length and solitude are the dials that raise risk (Britton 2019; Schlosser 2019), so nothing here is a retreat dose, and L3 techniques are never stacked.
9. **Every sitting ends in the day.** Close with one act (T43) and one carried line (T44). A state that never reaches a deed is a flame in the air.
10. **The level gate.** A tap may point to a technique of a higher level (L1 to L2). If the person has not yet reached that level (first session: L1 only; weeks 1-2: L1 and L2; L3 only after weeks, on a steady day), the page runs `again_smaller` on the current technique instead. In `techniques.json` such options carry `level_gate`.
11. **The guide is not a therapist.** For lasting low mood, numbness, panic, trauma, eating problems, mania or psychosis, the guide says plainly that a professional is the right next step, and keeps practices to the gentlest (T01, T42, T11, T14, T38, T25).

## 3. The library at a glance

Grouped by the state each technique opens first (many open more than one), with its difficulty.

| id | Technique | Opens | Level | From the practice of | Minutes |
| --- | --- | --- | --- | --- | --- |
| T01 | Arrive as you are | ST01 | L1 | TECHNOLOGY arrive | 1-2 minutes |
| T02 | The minute of silence | ST01, ST03 | L1 | universal/TRANSLATION section 1 (TR03-TR11) | 60 seconds, once a day, at the start of the day |
| T03 | Wake the body, then be still | ST01 | L1 | CATALOGUE B2 | 2-3 minutes |
| T04 | Watch the thoughts until the head empties | ST02, ST01 | L1 | CATALOGUE E2 | 3-7 minutes |
| T05 | Look at it, not in it | ST02 | L1 | GM-05 | 1-3 minutes |
| T06 | Since when? | ST02 | L2 | CATALOGUE C5 | 3-5 minutes |
| T07 | Before whom | ST03, ST08 | L1 | CATALOGUE C2 | 30-60 seconds |
| T08 | Seen | ST03, ST08 | L2 | CATALOGUE C3 | 3-5 minutes; then a few seconds at times during the day |
| T09 | The Shema of One | ST03, ST08, ST10 | L2 | CATALOGUE L5 | 1-2 minutes |
| T10 | Made, now | ST04, ST11 | L1 | FULL-DESCENT S01 | 3-6 minutes |
| T11 | The breath that comes by itself | ST04 | L1 | CATALOGUE B6 | 1-3 minutes |
| T12 | The picture, and where it breaks | ST04, ST06, ST09 | L2 | TECHNOLOGY mashal | 5-8 minutes |
| T13 | Walking it down to one thing | ST04, ST06 | L2 | TECHNOLOGY walk_down | 6-10 minutes |
| T14 | The first words on waking | ST04, ST13 | L1 | clinic BODY B13 | 30 seconds, every morning |
| T15 | The child before the parent | ST05, ST07 | L2 | CATALOGUE I2 | 5-8 minutes |
| T16 | Nothing else holds power | ST05, ST06 | L2 | CATALOGUE C4 | 2-5 minutes |
| T17 | The bedtime return | ST05, ST13 | L1 | clinic BODY B12 | 2-4 minutes, every night |
| T18 | One line, held long | ST06, ST07 | L2 | CATALOGUE C1 | 8-15 minutes; the core sitting from week 2 |
| T19 | Two knowings | ST06, ST08, ST09, ST11 | L2 | stage-book Stage 6 | 8-15 minutes; can be split into two sittings, one knowing each |
| T20 | Come back without a fight | ST06, ST02 | L1 | CATALOGUE E3 (the dispute) | Inside any technique |
| T21 | The held word | ST06, ST01, ST12 | L2 | CATALOGUE L3 | 3-5 minutes |
| T22 | Borrow a love you already have | ST07 | L1 | TECHNOLOGY arrive (step 3) | 3-5 minutes |
| T23 | Love answers love | ST07 | L2 | TECHNOLOGY heart_after | 5-8 minutes |
| T24 | The hum that sings itself | ST07, ST01, ST05 | L1 | CATALOGUE B1 | 2-5 minutes |
| T25 | Gather the good points | ST07, ST02 | L2 | CATALOGUE S3 | 3-6 minutes |
| T26 | Mercy for the spark | ST07, ST10 | L2 | clinic DX K12 | 4-6 minutes |
| T27 | The cry of one who feels nothing | ST07, ST10 | L2 | FULL-DESCENT S25, S26 | 3-5 minutes |
| T28 | Your own words | ST07, ST03, ST05, ST10 | L1 | CATALOGUE S1 | 5-15 minutes |
| T29 | One word only | ST07 | L1 | GM-20 | 1-3 minutes |
| T30 | The silent cry | ST07, ST10 | L2 | CATALOGUE S2 | 2-4 minutes |
| T31 | The edge of knowing | ST08, ST09 | L3 | TECHNOLOGY edge | 5-10 minutes, after T18 on a steady day |
| T32 | Standing in the between | ST09 | L3 | CATALOGUE E1 | 3-6 minutes |
| T33 | The afterward test | ST09, ST13 | L2 | CATALOGUE C6 | 2 minutes, hours later or that evening |
| T34 | Under all your names | ST10, ST02, ST09 | L2 | FULL-DESCENT S14 | 8-12 minutes |
| T35 | The flame that leans upward | ST10, ST07 | L2 | CATALOGUE I1 (the candle, image only) | 3-6 minutes |
| T36 | The child who knows its parent | ST10, ST05 | L3 | FULL-DESCENT S12 | 5-8 minutes |
| T37 | Seeing the garment | ST11 | L2 | CATALOGUE I4 | 3-5 minutes sitting; then seconds at a time through the day |
| T38 | The meal received | ST11, ST13 | L1 | CATALOGUE A2 | The first three bites of any meal |
| T39 | Where the beauty comes from | ST11, ST07 | L3 | CATALOGUE I4, E3 | 1-3 minutes, when beauty moves you (music, a landscape, a face in a painting) |
| T40 | The quiet after | ST12, ST09 | L1 | TECHNOLOGY hold | 1-3 minutes, after any technique that opened something |
| T41 | Transparent, not gone | ST12, ST09 | L2 | PS-14 | 1-2 minutes, after every deep technique (T31, T34, T32, T40) |
| T42 | Come down: feet, hands, the room | ST12, ST01 | L1 | MAP S20 | 1-2 minutes |
| T43 | The deed done slowly | ST13 | L1 | CATALOGUE A5 | 1 minute to choose; the act itself today |
| T44 | The carried line | ST13, ST04 | L1 | TECHNOLOGY carry, chazarah | Seconds, many times a day |
| T45 | The declared intention | ST13 | L2 | CATALOGUE A4 | 5 seconds before chosen acts |
| T46 | The evening look-back that ends in good | ST13, ST05 | L2 | CATALOGUE C5 | 3-5 minutes, before the bedtime return (T17) |
| T47 | Loving the next person first | ST13, ST07 | L1 | CATALOGUE S4 | 1-3 minutes before people; 5 minutes as a sitting |

- **L1, First session (safe for anyone on day one):** T01 Arrive as you are, T02 The minute of silence, T03 Wake the body, then be still, T04 Watch the thoughts until the head empties, T05 Look at it, not in it, T07 Before whom, T10 Made, now, T11 The breath that comes by itself, T14 The first words on waking, T17 The bedtime return, T20 Come back without a fight, T22 Borrow a love you already have, T24 The hum that sings itself, T28 Your own words, T29 One word only, T38 The meal received, T40 The quiet after, T42 Come down: feet, hands, the room, T43 The deed done slowly, T44 The carried line, T47 Loving the next person first.
- **L2, Weeks 1-2 (after a few sittings):** T06 Since when?, T08 Seen, T09 The Shema of One, T12 The picture, and where it breaks, T13 Walking it down to one thing, T15 The child before the parent, T16 Nothing else holds power, T18 One line, held long, T19 Two knowings, T21 The held word, T23 Love answers love, T25 Gather the good points, T26 Mercy for the spark, T27 The cry of one who feels nothing, T30 The silent cry, T33 The afterward test, T34 Under all your names, T35 The flame that leans upward, T37 Seeing the garment, T41 Transparent, not gone, T45 The declared intention, T46 The evening look-back that ends in good.
- **L3, Later (after weeks of practice, on a steady day):** T31 The edge of knowing, T32 Standing in the between, T36 The child who knows its parent, T39 Where the beauty comes from.

- **ST01 Here:** T01 (L1), T02 (L1), T03 (L1), T04 (L1), T21 (L2), T24 (L1), T42 (L1).
- **ST02 The watcher:** T04 (L1), T05 (L1), T06 (L2), T20 (L1), T25 (L2), T34 (L2).
- **ST03 Before:** T02 (L1), T07 (L1), T08 (L2), T09 (L2), T28 (L1).
- **ST04 Given right now:** T10 (L1), T11 (L1), T12 (L2), T13 (L2), T14 (L1), T44 (L1).
- **ST05 Held:** T15 (L2), T16 (L2), T17 (L1), T24 (L1), T28 (L1), T36 (L3), T46 (L2).
- **ST06 It is so:** T12 (L2), T13 (L2), T16 (L2), T18 (L2), T19 (L2), T20 (L1), T21 (L2).
- **ST07 The heart answers:** T15 (L2), T18 (L2), T22 (L1), T23 (L2), T24 (L1), T25 (L2), T26 (L2), T27 (L2), T28 (L1), T29 (L1), T30 (L2), T35 (L2), T39 (L3), T47 (L1).
- **ST08 Awe, small and glad:** T07 (L1), T08 (L2), T09 (L2), T19 (L2), T31 (L3).
- **ST09 Less in the way:** T12 (L2), T19 (L2), T31 (L3), T32 (L3), T33 (L2), T34 (L2), T40 (L1), T41 (L2).
- **ST10 The self beneath the layers:** T09 (L2), T26 (L2), T27 (L2), T28 (L1), T30 (L2), T34 (L2), T35 (L2), T36 (L3).
- **ST11 The world see-through:** T10 (L1), T19 (L2), T37 (L2), T38 (L1), T39 (L3).
- **ST12 The quiet after:** T21 (L2), T40 (L1), T41 (L2), T42 (L1).
- **ST13 Acting from it:** T14 (L1), T17 (L1), T33 (L2), T38 (L1), T43 (L1), T44 (L1), T45 (L2), T46 (L2), T47 (L1).

## 4. Where to start: from the person's state now

*Ours, from the sources' own pairings (CATALOGUE section 4 table; VS decision table; MAP 'grows' and 'blocks').* Read the person from what they say, or from one tap on "What is loudest right now?" (T01). Then choose the technique for the gap between where they are and the next state.

| If the person is... | Start with | Then, if it opens | Avoid |
| --- | --- | --- | --- |
| Scattered, racing (MAP S01) | T04, or T03 if heavy | T18 one line | T31, T34, T32 |
| Holding it all up, anxious (MAP S02) | T10, then T16 | T15, T17 at night | T08 if they feel judged |
| Numb, flat, dry (MAP S03, S16) | T27, or T22 | T24, T28 | Demanding feeling; T31 |
| Low and heavy (MAP S04) | T03 seated, T25 | T24, T43 (tiny act) | T46 accounting, T08, T31 |
| Angry at someone (MAP S15) | T05 on the anger | T47 (not toward someone who harmed them) | T08 |
| Grieving (MAP S14) | T28 with company | T22 (a place or animal if the person is the loss) | T06, T31, T32 |
| Understands but doesn't feel (MAP S16) | T18 with detail | T24 (same line on a tune), T23 | New ideas; more explaining |
| Chasing the high, or after it (MAP S18, S19) | T33 | T43, T41 | Any deepen |
| Already quiet (MAP S32) | T07, then T18 | T34, T40; later T31 | Stacking L3 |
| Feeling unreal, spacey, frightened (MAP S20) | T42 only | T38 (the meal), plain day, a person | Everything opening ST02, ST09, ST10; all L3 |
| In danger (MAP S21) | No technique. Safety protocol. |  | All |

**A first session** *(ours)*: T01 arrive (1 min) → T02 the minute or T07 before whom (1 min) → one of T10, T04 or T22 by the check-in (4-6 min) → T40 the quiet after (1-2 min) → T43 one act and T44 one line (2 min). About 12 minutes.

**Weeks 1-2** *(ours)*: the same frame, with the middle drawn from L2: T18 one line held long (same line all week), T15, T37, T34, T28. Mornings T14; evenings T46 then T17.

**Later** *(ours)*: L3 (T39, T31, T36, T32) only on a steady day, one per sitting, always followed by T41 and T43, and never in a week with any stop sign.

## ST01 · Here

*The flood slows. You are in one place, in this body, in this room, and not being dragged. Not asleep and not blank: there is room for one true thing.*

## T01 · Arrive as you are

*Opens: ST01 Here · Level: First session (safe for anyone on day one) · Dose: 1-2 minutes. The opening of every session.*

**Toward the true self** *(ours)*. The way in to the deepest self is through what is actually here. Nothing has to be faked to begin, so the person who arrives is the real one.

**The practice in the source** *(stated)*. The Piaseczner's 'key to the soul': start from whatever is already stirring, even a bodily want or a worry, never from a holier feeling one does not have.

> «כל התעוררות אפלו אם גופנית, היא מפתח לנפש» (*every stirring, even a bodily one, is a key to the soul*) · Bnei Machshava Tova (the Piaseczner), `Bnei Machshava Tova (Piaseczno, 1917-1923).txt`, line 100
> «ועליך להשתדל רק להכיר אותך ואת אשר בך מתרחש» (*you need only work to know yourself and what is happening in you*) · Hakhsharat HaAvrekhim (the Piaseczner), `Hakhsharat HaAvrekhim (Warsaw, 1930-1940).txt`, line 87

*Builds on:* TECHNOLOGY arrive; VS-23; manual part1 stage 1.

**How it works** *(ours)*. Naming what is present (a mood, a pressure, a want) turns it from something that runs you into something you can see. Starting where you are removes the strain of trying to feel something else, and strain is the first thing that blocks inner quiet. *(R09 Lieberman et al., R25 Kircanski, Lieberman & Craske)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | You don't need to be calm to do this. Come in exactly as you are. | 4s |
| 2 | Let your body find the chair. Let the floor take your feet. | 8s |
| 3 | Notice what is loudest in you right now. A worry, a tiredness, a want. Whatever it is. | 12s |
| 4 | Give it a plain name, silently. One or two words. | 10s |
| 5 | That is where we start. Not somewhere better. Here. | 6s |
| 6 | Notice that you are the one who noticed it. That one is here too. | 12s |
| 7 | Good. You've arrived. | 3s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 5: That is where we start. Even this is a key; G-d is found from exactly here. - Step 6: Notice that you are the one who noticed it. That one stands before G-d right now, as you are.

**Check-in** *(one tap)*: "What is loudest right now?"

| Tap | Then | The guide says |
| --- | --- | --- |
| A worry | `switch` → T16 Nothing else holds power | Let's set it where it belongs for a few minutes. |
| Tired or flat | `switch` → T10 Made, now | Flat is a fine place to start. Let's look at something simple. |
| Restless, busy head | `switch` → T04 Watch the thoughts until the head empties | Then let's watch that busy head for a minute. |
| Fairly settled | `deepen` → T07 Before whom | Good. Then let's go through the door. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Waiting for a spiritual feeling before starting.* Say: 'Not much' is an answer. Start from the plain thing.
- *The worry becomes the whole session.* Name it once, then move to T16 or T10; do not analyse it.

**Not for** *(contraindications)*. None for the practice. If what is loudest is danger, despair or wanting not to live, stop and use the safety protocol, not a technique.

**Body.** Sit any way that is steady. Eyes open or closed. Hands resting. Breath left alone.

**In daily life.** Before any hard moment (a call, a meeting): one breath of noticing, one plain name for what is loud. Then begin.

## T02 · The minute of silence

*Opens: ST01 Here, ST03 Before · Level: First session (safe for anyone on day one) · Dose: 60 seconds, once a day, at the start of the day. Can grow to 3 minutes.*

**Toward the true self** *(ours)*. In silence no one is performing. What a person turns to when nobody tells them what to think shows them their own center.

**The practice in the source** *(stated)*. The Rebbe's moment of silence: at least sixty seconds, at the start of the day, for thought about the Creator and Ruler of the world, in thought only, so each person thinks in their own words and no one copies or fears anyone.

> «ניתנים לרשותו 60 שניות (לפחות). כדי להתבונן» (*he is given sixty seconds (at least) to contemplate*) · Hisvaaduyos 5744 (the Rebbe, on the moment of silence), OCR, `Hisvaaduyos (scans, OCR).txt`, line 6561 · OCR
> «לא בדיבור כי אם במחשבה בלבד, הרי כאו"א יכול לחשוב מה שרוצה» (*not in speech but only in thought, so each one can think what he wishes*) · Hisvaaduyos 5744 (the Rebbe, on the moment of silence), OCR, `Hisvaaduyos (scans, OCR).txt`, line 54754 · OCR

*Builds on:* universal/TRANSLATION section 1 (TR03-TR11); GM-22; GM-23.

**How it works** *(ours)*. A short, fixed, daily pause is the smallest unit of practice that can become a habit. The fixed time and place do the remembering for you; the silence gives the mind one minute without input, which is when deeper things can surface. *(R14 Lally et al., R32 Birtwell et al., R29 Lutz, Mattout & Pagnoni)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | For one minute, nothing to do and nothing to say. | 3s |
| 2 | Let the eyes close or rest low. | 5s |
| 3 | Turn your thought toward what is greatest. The source of everything. In your own words, or without words. | 20s |
| 4 | If the mind wanders, let it come back. No one is grading this. | 20s |
| 5 | One more breath of quiet. | 12s |
| 6 | That was your minute. It's yours every day. | 3s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 3: Turn your thought to the One who made the world and runs it, who sees and hears. In your own words, inside. - Step 6: That was your minute before G-d. It's yours every day.

**Check-in** *(one tap)*: "How was the minute?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Quiet came | `deepen` → T40 The quiet after | Then stay in it a little longer. |
| Busy head the whole time | `switch` → T04 Watch the thoughts until the head empties | That's normal. Let's look at the busy head itself. |
| Nothing much | `close` | A minute given is a minute given. That counts. |
| Something stirred | `deepen` → T28 Your own words | Then say a word about it, inside, to whoever you were facing. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Using the minute to plan the day.* Next time put the plan on paper first, then sit.
- *Judging the minute as good or bad.* The minute is kept, not graded. Keep it tomorrow.

**Not for** *(contraindications)*. None. It is the safest door in the library.

**Body.** Seated, feet down. Eyes closed or resting on the floor. Hands still. Breath left alone.

**In daily life.** Same minute, same place, every morning, before the phone. In a group (a class, a team), it can be done together in silence.

## T03 · Wake the body, then be still

*Opens: ST01 Here · Level: First session (safe for anyone on day one) · Dose: 2-3 minutes. Good when heavy, sleepy or numb.*

**Toward the true self** *(ours)*. The body is not in the way of the deeper self; it is the first door to it. Waking it lets the person be present with all of themselves.

**The practice in the source** *(stated)*. The Baal Shem Tov: when the soul will not catch, first rouse the body with all your strength so the soul's power can shine in it; sway at the start, then stand still and serve in thought alone.

> «וצריך לעורר עצמו בתחלה בגוף שלו בכל כחו כדי שתאיר בו כח הנשמה» (*first he must rouse himself in his body with all his strength so the power of the soul will shine in him*) · Tzava'at HaRivash (the Baal Shem Tov, as collected), `Tzava'at HaRivash (Medzhibozh and Mezritch, c. 1740-1770).txt`, line 111
> «ואח"כ יוכל לעבוד במחשבה לבד בלי תנועות הגוף» (*afterwards he can serve in thought alone, without movements of the body*) · Tzava'at HaRivash (the Baal Shem Tov, as collected), `Tzava'at HaRivash (Medzhibozh and Mezritch, c. 1740-1770).txt`, line 111

*Builds on:* CATALOGUE B2; VS-08; clinic BODY B09.

**How it works** *(ours)*. Movement raises alertness and clears heaviness; stopping after movement leaves a vivid stillness that is easier to notice than stillness from sitting cold. It works from the outside in. *(R01 Lutz, Slagter, Dunne & Davidson)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Stand up if you can, or sit tall. | 4s |
| 2 | Let your body move gently. Sway a little, side to side or forward and back. | 20s |
| 3 | A bit more life in it. Not for show. Just wake up. | 20s |
| 4 | Now ask yourself, while moving: why am I moving? Who am I waking up for? | 10s |
| 5 | Slow down. | 6s |
| 6 | And stop. Completely still. | 15s |
| 7 | Feel how alive the stillness is after the movement. | 20s |
| 8 | Stay in that stillness. Nothing to add. | 20s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 4: Ask yourself while moving: why am I moving? Because G-d is right here in front of me. - Step 8: Stay in that stillness before Him. Nothing to add.

**Check-in** *(one tap)*: "How is the stillness?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Alive and quiet | `deepen` → T10 Made, now | Good. Let's look at something from inside that stillness. |
| Still heavy | `again_smaller` | Let's do it once more, a little stronger, a little shorter. |
| Dizzy or shaky | `come_up` → T42 Come down: feet, hands, the room | Sit down. Feet on the floor. We go slower. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Moving as a routine with no thought in it.* Add the question: why am I moving?
- *Moving harder and harder, getting worked up.* Cap it at a minute; the point is the stillness after.

**Not for** *(contraindications)*. Any condition that makes standing or swaying unsafe: do it seated, with small shoulder movements. Stop if dizzy.

**Body.** Standing or seated tall. Eyes open while moving, then closed in the stillness. Hands loose. Breath free, never paced.

**In daily life.** Before a task you are dreading: thirty seconds of moving, then still for ten seconds, then begin.

## ST02 · The watcher

*You can see a thought, a mood or a verdict about yourself from one step to the side. It is something you have. It is not all you are. The one who looks is still here, warm, in the body.*

## T04 · Watch the thoughts until the head empties

*Opens: ST02 The watcher, ST01 Here · Level: First session (safe for anyone on day one) · Dose: 3-7 minutes. Daily for the first weeks.*

**Toward the true self** *(ours)*. You are not your thoughts. The one who watches them is closer to who you are. The Piaseczner adds that the busy 'I' is what blocks the light; when it quiets, the deeper self can be reached.

**The practice in the source** *(stated)*. The Piaseczner's quieting: look at your thoughts for a few minutes, asking 'what am I thinking?'; little by little the head empties; then tie it to one line, said softly, never forcefully.

> «שיתחיל האיש להביט על מחשבותיו שעה קלה לערך איזה רגעים היינו מה אני חושב» (*that a person begin to look at his thoughts for a short while, a few minutes: what am I thinking?*) · Derekh HaMelekh (the Piaseczner), `Derekh HaMelekh (Warsaw, 1931).txt`, line 1556
> «אז ירגיש לאט לאט שראשו מתרוקן ומחשבותיו עמדו משטפן הרגיל» (*then he will feel little by little that his head is emptying and his thoughts have stopped their usual flood*) · Derekh HaMelekh (the Piaseczner), `Derekh HaMelekh (Warsaw, 1931).txt`, line 1556
> «אבל לא שיאמר זאת בחזקה כי כל הענין הוא רק להשקיט מחשבותיו» (*but not that he say it forcefully, for the whole thing is only to quiet his thoughts*) · Derekh HaMelekh (the Piaseczner), `Derekh HaMelekh (Warsaw, 1931).txt`, line 1556

*Builds on:* CATALOGUE E2; TECHNOLOGY quieting; GM-04; PIASECZNO step 2-3.

**How it works** *(ours)*. Looking at a thought from outside (instead of thinking it) weakens its pull; this is called decentering. Thoughts slow on their own when they are watched and not fed. Then one line gives the quiet mind something true to rest on, so it does not drift. *(R03 Bernstein et al., R02 Hasenkamp et al., R04 Brewer et al., R26 Killingsworth & Gilbert)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Sit, and for a few minutes do only one thing: watch your thoughts. | 5s |
| 2 | Ask quietly: what am I thinking now? | 15s |
| 3 | Don't chase any thought away. Just see it, like someone passing a window. | 25s |
| 4 | Again: what am I thinking now? | 25s |
| 5 | Notice the gap after a thought ends, before the next one starts. | 25s |
| 6 | Slowly the stream thins. Let it. | 30s |
| 7 | Now, softly, one line: 'Something real is here, under all of this.' | 10s |
| 8 | Say it once more, slower. Then stop saying it and stay. | 30s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 7: Now, softly, one line: 'G-d alone is real; all of this is His light.' - Step 8: Say it once more, slower, not hard. Then stay with Him.

**Check-in** *(one tap)*: "How is your head now?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Quieter, more space | `deepen` → T40 The quiet after | Then rest in the space a little. |
| Still busy | `again_smaller` | That's fine. Two more minutes, just the question 'what am I thinking?' |
| One thought keeps coming back | `switch` → T05 Look at it, not in it | Then let's look straight at that one. |
| Blank in a strange way | `come_up` → T42 Come down: feet, hands, the room | Let's come back to the room for a moment. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Fighting the thoughts or forcing the head empty.* The sources say force wakes the ego. Only look; never push.
- *Staying in blankness as the goal.* The quiet is a door. Tie it at once to one true line (step 7).

**Not for** *(contraindications)*. Not for someone already feeling unreal, numb in a frightening way, or dissociating (MAP S20): use T42 and T38 instead. Keep short for someone with intrusive trauma memories.

**Body.** Seated. Eyes closed, or open facing a plain wall (the Piaseczner's own option). Hands still in the lap. Breath not used.

**In daily life.** Waiting in line or at a red light: one 'what am I thinking?' and one look.

## T05 · Look at it, not in it

*Opens: ST02 The watcher · Level: First session (safe for anyone on day one) · Dose: 1-3 minutes. Whenever one thought or feeling keeps returning.*

**Toward the true self** *(ours)*. A repeating thought feels like 'me'. Looking at it shows it is something passing through me, and the one looking is steadier than it.

**The practice in the source** *(stated)*. The Piaseczner: when we look at one of our thoughts, it melts; for twenty seconds I may stop and think only about the thought itself, instead of thinking from inside it.

> «שכאשר מביטים על מחשבה אחת שבנו, היא נמסת» (*when we look at one of our thoughts, it melts*) · Mevo HaShe'arim (the Piaseczner), `Mevo HaShearim (Piaseczno, 1931-1943).txt`, line 390
> «הלא על עשרים רגעים [סעקונדעס] רשות לי להפסיק ממנה ולחשוב רק אודותה» (*surely for twenty seconds I may stop it and think only about it*) · Hakhsharat HaAvrekhim (the Piaseczner), `Hakhsharat HaAvrekhim (Warsaw, 1930-1940).txt`, line 302

*Builds on:* GM-05; TECHNOLOGY binding; P1-05.

**How it works** *(ours)*. Thinking about a thought (rather than with it) moves it from the foreground to an object you can see. Its emotional charge drops, much as naming a feeling lowers its intensity. *(R03 Bernstein et al., R09 Lieberman et al., R19 Wang, Hagger & Chatzisarantis)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Pick the one thought that keeps coming back. | 5s |
| 2 | Don't think it. Look at it. As if it were written on a card in front of you. | 15s |
| 3 | Where is it? Is it words, a picture, a feeling in the body? | 15s |
| 4 | Watch it for twenty seconds without arguing with it. | 20s |
| 5 | Notice: it is there, and you are here, looking. | 15s |
| 6 | See if it has grown fainter. Whatever it does, let it. | 20s |
| 7 | Now turn back to the plain room. | 5s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 7: Now leave it with G-d, who holds it better than you can, and turn back to the room.

**Check-in** *(one tap)*: "What happened to the thought?"

| Tap | Then | The guide says |
| --- | --- | --- |
| It faded | `deepen` → T04 Watch the thoughts until the head empties | Good. Now watch the whole stream the same way. |
| Still there | `again_smaller` | Let's look once more, for only ten seconds, from a little further away. |
| It got stronger | `switch` → T20 Come back without a fight | Then we won't look at it. We'll just come back to something else. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Arguing with the thought while 'looking'.* Looking means no answer. Describe it, don't debate it.
- *Looking becomes brooding over the content.* Shorten to ten seconds; ask only where it is and what shape it has.

**Not for** *(contraindications)*. Not for traumatic memories or images (do not look into them alone); not in acute panic. Use T42 instead and refer if needed.

**Body.** Seated, eyes closed or soft. Hands open on the knees. Breath left alone.

**In daily life.** When a resentment or worry loops: twenty seconds of looking at it as a thing, then back to the task.

## T06 · Since when?

*Opens: ST02 The watcher · Level: Weeks 1-2 (after a few sittings) · Dose: 3-5 minutes. Evenings, or when a mood will not lift.*

**Toward the true self** *(ours)*. A mood that has no name runs a person from behind. Finding where it started gives the person back to themselves.

**The practice in the source** *(stated)*. The Piaseczner: gather the thoughts of a full day and look at them; for a mood with no name, search from what hour it began.

> «אז העצה שיתחיל לחפש בקרבו מאיזה שעה התחילה קשיות ערפו» (*the advice is to search in himself from what hour his stiffness began*) · Hakhsharat HaAvrekhim (the Piaseczner), `Hakhsharat HaAvrekhim (Warsaw, 1930-1940).txt`, line 313
> «יצבור נא האדם מחשבות מן המעת לעת ויסתכל בהם» (*let a person gather the thoughts of a full day and look at them*) · Derekh HaMelekh (the Piaseczner), `Derekh HaMelekh (Warsaw, 1931).txt`, line 1337

*Builds on:* CATALOGUE C5; TECHNOLOGY cheshbon; PIASECZNO step 3.

**How it works** *(ours)*. Tracing a mood back to its trigger turns a vague state into a specific event that can be understood and answered. Recalling the moment with fresh understanding is the kind of re-opening that lets an emotional memory be updated. *(R09 Lieberman et al., R07 Lane, Ryan, Nadel & Greenberg, R08 Webb, Miles & Sheeran)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Notice the mood you're in. Don't name it yet. Just feel its shape. | 10s |
| 2 | Ask: since when? Was I like this this morning? | 15s |
| 3 | Walk back through the day, hour by hour. When did it start? | 25s |
| 4 | Find the moment. A word someone said, a message, a thought. | 20s |
| 5 | Look at that moment as if watching it on a screen. | 20s |
| 6 | Now say what it really was, in plain words. | 15s |
| 7 | Notice: the mood has a beginning. So it isn't you. It happened to you. | 15s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 7: It has a beginning, so it is not who you are. It came; it can be given to G-d and it can go.

**Check-in** *(one tap)*: "Did you find where it started?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Yes, and it eased | `close` | Good. Let's choose one small thing to do about it, or nothing. |
| Yes, and it hurts | `switch` → T28 Your own words | Then let's say it, in your own words, to Someone. |
| No | `switch` → T04 Watch the thoughts until the head empties | That's fine. Let's just watch it for a minute instead. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Turning the search into blame of the person who 'caused' it.* The aim is to see the moment, not to judge anyone. Move to T47 if anger rises.
- *Endless self-analysis.* One search, five minutes. Then stop.

**Not for** *(contraindications)*. Not for trauma, grief floods or long low moods; there use company and a professional. Not on a crushed day.

**Body.** Seated, eyes closed or looking at nothing in particular. Hands still. Breath left alone.

**In daily life.** When irritable for no reason: 'since when?' Often the answer takes thirty seconds and frees the afternoon.

## ST03 · Before

*The room changes posture. You are not alone in it. You are seen, and kindly. Something like dignity, not dread.*

## T07 · Before whom

*Opens: ST03 Before, ST08 Awe, small and glad · Level: First session (safe for anyone on day one) · Dose: 30-60 seconds. At the start of any session, task or day.*

**Toward the true self** *(ours)*. The question 'before what am I standing?' changes the one who asks it. You stand up straighter inside, and that straightness is yours.

**The practice in the source** *(stated)*. The entrance thought: the Baal Shem Tov makes awe the gate to enter before Him; the Alter Rebbe has a person think, the moment he wakes, before Whom he is lying.

> «מתחלה כשרוצה להתפלל יהי' ביראה שהוא השער לכנוס לפניו» (*at first, when he wants to pray, let him be in awe, which is the gate to enter before Him*) · Tzava'at HaRivash (the Baal Shem Tov, as collected), `Tzava'at HaRivash (Medzhibozh and Mezritch, c. 1740-1770).txt`, line 121
> «יחשב בלבו לפני מי הוא שוכב» (*let him think in his heart before Whom he is lying*) · Shulchan Arukh HaRav, Orach Chayim (the Alter Rebbe), `Shulchan Arukh HaRav (Liozna, c. 1770-1805).txt`, line 70

*Builds on:* CATALOGUE C2; TECHNOLOGY before_whom; P1-04 stage 1.

**How it works** *(ours)*. A brief threshold act changes the frame before the content: the same minute, entered on purpose, is experienced differently. Awe narrows the sense of self in a healthy way and is linked to openness and connection. *(R16 Yaden et al., R34 Hobson et al., R27 Leary, Adams & Tate)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Pause at the edge of what you're about to do. | 4s |
| 2 | Ask: before what am I standing right now? | 10s |
| 3 | Not the room. What is larger than the room, and was here before you. | 15s |
| 4 | You didn't make this moment. You've been given it. | 10s |
| 5 | Let yourself feel a little small, and steady. | 15s |
| 6 | Now step in. | 2s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 2: Ask: before Whom am I standing? - Step 3: Before the King who brings all worlds into being, here, now. - Step 6: Now step in before Him.

**Check-in** *(one tap)*: "What happened at the door?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Small and steady | `deepen` → T18 One line, held long | Good. Now one line, held long. |
| Nothing much | `deepen` → T08 Seen | If it doesn't reach you at once, the source says: go deeper into it. Let's try. |
| I felt judged or watched | `switch` → T15 The child before the parent | Then not the King watching. The child before a loving parent. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Fear of punishment instead of awe.* Awe is steadiness before greatness, not dread. Switch to T15.
- *A ritual phrase said without stopping.* Stop for three real seconds.

**Not for** *(contraindications)*. For people who grew up with a punishing image of G-d or authority: use the warm form (T15) first.

**Body.** Standing or seated. Eyes may close for the question. Hands still. Breath left alone.

**In daily life.** Before opening email, a meeting, a meal: 'before what am I standing?' Three seconds.

## T08 · Seen

*Opens: ST03 Before, ST08 Awe, small and glad · Level: Weeks 1-2 (after a few sittings) · Dose: 3-5 minutes; then a few seconds at times during the day.*

**Toward the true self** *(ours)*. Being fully seen, without a mask, is how a person finds out who they are when they are not performing.

**The practice in the source** *(stated)*. Shiviti as awareness: the Alter Rebbe asks a person to take to heart that the great King stands over him and sees his deeds, and if it does not reach him at once, to go deep into it until it does; the Baal Shem Tov: he looks at the Creator and the Creator looks at him.

> «כל שכן כשישים האדם אל לבו, שהמלך הגדול, מלך מלכי המלכים הקדושברוךהוא, עומד עליו ורואה במעשיו» (*all the more when a person takes to heart that the great King, the King of kings, stands over him and sees his deeds*) · Shulchan Arukh HaRav, Orach Chayim (the Alter Rebbe), `Shulchan Arukh HaRav (Liozna, c. 1770-1805).txt`, line 71
> «והוא מסתכל על הבורא ית'. והבורא ית' מסתכל בו» (*he looks at the Creator, and the Creator looks at him*) · Tzava'at HaRivash (the Baal Shem Tov, as collected), `Tzava'at HaRivash (Medzhibozh and Mezritch, c. 1740-1770).txt`, line 288

*Builds on:* CATALOGUE C3; GM-09; animal-soul M59.

**How it works** *(ours)*. People act and feel differently in the presence of one who sees. Imagining a kind, all-seeing presence increases honesty and steadiness, and repeated through the day it becomes a background awareness. *(R21 Luhrmann & Morgain, R31 Granqvist, Mikulincer & Shaver)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Sit as you would if someone you deeply respect were in the room. | 8s |
| 2 | Imagine you are being seen. Completely. Not judged; seen. | 15s |
| 3 | Everything about you, the good and the rest, in full view. | 15s |
| 4 | Notice what changes in how you sit, in how you breathe, in what you want. | 20s |
| 5 | Look back toward the one who sees you. | 15s |
| 6 | Seen, and seeing. Stay there. | 25s |
| 7 | If it hasn't reached you yet, go a little deeper. It's allowed to take time. | 20s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 2: Take to heart: the King of kings stands over you and sees you. - Step 5: Look back toward Him. You look at Him; He looks at you.

**Check-in** *(one tap)*: "What is it like to be seen?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Steadying, honest | `deepen` → T28 Your own words | Then speak to the one who sees, in your own words. |
| Exposed, ashamed | `switch` → T25 Gather the good points | Let's look with kind eyes. Find what is good in you. |
| Doesn't reach me | `again_smaller` | The source says: go deeper until it reaches you. One more, slower. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Feeling surveilled, anxious, scrupulous.* Switch to warmth (T15, T25). Being seen is meant to steady, not frighten.
- *Performing for the imagined watcher.* The watcher sees through performance. Drop it.

**Not for** *(contraindications)*. Not for people with paranoia, shame-based depression or scrupulosity: use T15 or T25 instead.

**Body.** Seated upright with dignity. Eyes closed or open. Hands resting. Breath left alone.

**In daily life.** Through the day, a few seconds: 'seen'. Especially before a word you might regret.

## T09 · The Shema of One

*Opens: ST03 Before, ST08 Awe, small and glad, ST10 The self beneath the layers · Level: Weeks 1-2 (after a few sittings) · Dose: 1-2 minutes. Morning and night.*

**Toward the true self** *(ours)*. For a moment nothing is held back. Saying 'One' with your whole self gathers every scattered part of you into one, as the world is one.

**The practice in the source** *(stated)*. The Shema as unity, for those it fits: say the first verse as if it were a new decree never heard before, aloud, with the hands over the eyes; on the last word, 'One', lengthen in thought (not in sound) long enough to think that He alone fills the four directions. The universal version keeps the form and the word 'One'.

> «וצריך שתהיה בעיניו כפרוטגמא חדשה שלא שמעה מעולם» (*and it should be in his eyes like a new decree he never heard*) · Shulchan Arukh HaRav, Orach Chayim (the Alter Rebbe), `Shulchan Arukh HaRav (Liozna, c. 1770-1805).txt`, line 768
> «ונוהגין לתן ידיהם על פניהם בקריאת פסוק ראשון, כדי שלא יסתכל בדבר אחר שמונעו מלכון» (*and the custom is to put their hands over their faces during the first verse, so as not to look at something else that would keep him from intending*) · Shulchan Arukh HaRav, Orach Chayim (the Alter Rebbe), `Shulchan Arukh HaRav (Liozna, c. 1770-1805).txt`, line 771
> «אבל בדלי"ת צריך להאריך יותר, כדי שעור שיחשב שהקדוש ברוך הוא יחיד בעולמו ומושל בד' רוחות העולם» (*but on the dalet he must lengthen more, long enough to think that the Holy One is alone in His world and rules the four directions*) · Shulchan Arukh HaRav, Orach Chayim (the Alter Rebbe), `Shulchan Arukh HaRav (Liozna, c. 1770-1805).txt`, line 772

*Builds on:* CATALOGUE L5; TECHNOLOGY lips; GM-22.

**How it works** *(ours)*. Covering the eyes cuts out distraction; saying a short phrase aloud raises attention; lingering in thought on one word lets its meaning expand to fill the field of awareness. A short, total act repeated daily becomes a fixed point in the day. *(R34 Hobson et al., R01 Lutz, Slagter, Dunne & Davidson)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Sit, and cover your eyes with your hand. | 5s |
| 2 | Nothing else to look at now. | 5s |
| 3 | Say, as if you'd never heard it before: 'Listen. All of it is One.' | 8s |
| 4 | Stay on the word 'One'. Not by stretching the sound. In your mind. | 10s |
| 5 | Let 'One' fill above you and below you. | 10s |
| 6 | Let it fill east, west, north and south. Every direction. One. | 20s |
| 7 | Nothing outside it. You inside it. | 15s |
| 8 | Uncover your eyes slowly. Look at the room. The same One. | 10s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 3: Say, as a new decree you never heard: 'Shema Yisrael, Hashem Elokeinu, Hashem Echad.' - Step 4: On 'Echad', don't rush the ches; make Him King of heaven and earth. Stay longer on the dalet, in thought. - Step 6: He alone in His world, ruling the four directions. - Step 7: Then quietly: 'Baruch shem kevod malchuso le'olam va'ed.' His kingdom, here too.

**Check-in** *(one tap)*: "How was the word 'One'?"

| Tap | Then | The guide says |
| --- | --- | --- |
| It filled everything | `deepen` → T40 The quiet after | Stay in the quiet after. |
| Just words | `again_smaller` | Once more, slower, as if you'd never heard it. |
| I wanted to give myself to it | `deepen` → T45 The declared intention | Then say what you're giving today, truthfully. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Said fast, as a formula.* As a new decree, never heard; slow.
- *Stretching the sound of the word.* The lengthening is in thought (SAH 61:7).

**Not for** *(contraindications)*. The believer's form is for those for whom the Shema is theirs; never put Jewish ritual words in the mouth of someone for whom they are not (TRANSLATION section 5). The handing-over images of the Arizal (martyrdom) are not used by the guide.

**Body.** Seated. Right hand covering the eyes. Spine upright. Voice aloud for the first line, then silence. Breath left alone.

**In daily life.** Morning and bedtime. At bedtime it becomes T17's closing line.

## ST04 · Given right now

*This moment is being given, not kept. The cup, the room, the floor, and you too, are not holding yourselves up. There is a floor under the floor.*

## T10 · Made, now

*Opens: ST04 Given right now, ST11 The world see-through · Level: First session (safe for anyone on day one) · Dose: 3-6 minutes. A first-session favorite.*

**Toward the true self** *(ours)*. The plainest fact about you, that you are here at all, is not something you made. At that point, being here, the self touches what gives it being.

**The practice in the source** *(stated)*. The analysis of an object being given now: the Alter Rebbe's teaching that creation is renewed every moment, like a word that lasts only while it is said; the Rebbe asks that this be recognized, not only understood.

> «כי אילו היו האותיות מסתלקות כרגע חס ושלום וחוזרות למקורן, היו כל השמים אין ואפס ממש» (*if the letters withdrew for an instant and went back to their source, all the heavens would be truly nothing*) · Tanya (the Alter Rebbe), Chabad Library text, `Tanya — Hebrew text.txt`, line 785
> «שיכיר (ולא רק שיבין)» (*that he recognize, not only understand*) · Inyanah Shel Toras HaChassidus (the Rebbe), `Inyanah Shel Toras HaChassidus (Brooklyn, New York, 1965).txt`, line 93

*Builds on:* FULL-DESCENT S01; TECHNOLOGY walk_down; stage-book Stage 4; MAP S65.

**How it works** *(ours)*. A concrete object and a simple question ('did it make itself?') turn an abstract idea into a felt recognition. Insight that is felt, not only understood, is what shifts deep beliefs ('I hold everything up'). *(R28 Teasdale, R07 Lane, Ryan, Nadel & Greenberg, R16 Yaden et al.)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Look at your hand. Just look at it. | 8s |
| 2 | Did it make itself? | 8s |
| 3 | Could it keep itself here one more second by its own strength? | 10s |
| 4 | Anything that can stop being here isn't holding itself up. | 8s |
| 5 | So right now, this second, it is being given. | 15s |
| 6 | Not once, long ago. Now. And now. | 15s |
| 7 | The same with you. Not your thoughts or your mood: the plain fact that you are here. | 15s |
| 8 | Say quietly: given, now. | 10s |
| 9 | Stay with that, and keep looking at the hand. | 20s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 5: So right now, this second, G-d is giving it being, the way a word lasts only while it is being said. - Step 7: The same with you. The plain fact that you are here is the part only G-d makes. - Step 8: Say quietly: made by You, now.

**Check-in** *(one tap)*: "How does it land?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Real, like noticing something obvious | `deepen` → T11 The breath that comes by itself | Then let's feel the next breath arrive the same way. |
| Just an idea | `switch` → T12 The picture, and where it breaks | Let's give it a picture, and see where the picture breaks. |
| Something like thanks | `deepen` → T28 Your own words | Say thank you, in your own words. |
| Things feel less solid | `come_up` → T42 Come down: feet, hands, the room | Being given makes things more real, not less. Let's feel the floor. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *A nice sentence that changes nothing ('sure, everything is created').* Go slower; stay on the one hand, one second.
- *A dizzy sense that nothing is solid.* Stop; T42. The world is real; it is given, not illusory.

**Not for** *(contraindications)*. Not for someone already feeling unreal or detached (MAP S20). With them use T38 (the meal) or T42.

**Body.** Seated. Eyes open, resting on the hand in the lap. Hands still. Breath left alone.

**In daily life.** On waking, and once at midday: look at your hand, 'given, now'. One second.

## T11 · The breath that comes by itself

*Opens: ST04 Given right now · Level: First session (safe for anyone on day one) · Dose: 1-3 minutes. Three breaths in any pause; up to ten at the start of a sitting.*

**Toward the true self** *(ours)*. You did not start your breathing and you are not running it now. Noticing that is noticing that your life is received.

**The practice in the source** *(stated)*. The Maggid on 'for each breath, praise': the life goes into the body and at once returns upward, and this is the breath. The breath is a sign of life being given, not a drill (the sources have no breathing technique).

> «על כל נשימה ונשימה תהלל יה» (*for each and every breath, praise God*) · Maggid Devarav leYaakov (the Maggid of Mezritch), `Maggid Devarav leYaakov (Mezritch, Volhynia, 1760-1780).txt`, line 215
> «לפיכך הולך החיות בגוף מיד חוזר למעלה וזהו ההבל» (*so the life goes into the body and at once returns upward, and this is the breath*) · Maggid Devarav leYaakov (the Maggid of Mezritch), `Maggid Devarav leYaakov (Mezritch, Volhynia, 1760-1780).txt`, line 215

*Builds on:* CATALOGUE B6; clinic BODY B08; P1-02 stage 2.

**How it works** *(ours)*. Breath is a natural anchor that is always present. Here it is not controlled or counted; it is only noticed as arriving by itself, which pairs the body's rhythm with gratitude rather than effort. *(R13 Emmons & McCullough, R01 Lutz, Slagter, Dunne & Davidson)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Don't change your breath. Just notice it. | 8s |
| 2 | Notice that you aren't making it happen. It comes by itself. | 12s |
| 3 | When it comes in, think: given. | 10s |
| 4 | When it goes out, think: thank you. | 10s |
| 5 | Given. Thank you. Let it set its own pace. | 25s |
| 6 | Three more, like that. | 25s |
| 7 | Now let the breath go back to being background. | 5s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 3: When it comes in, think: given by You. - Step 4: When it goes out, think: thank You.

**Check-in** *(one tap)*: "How was that?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Calm, grateful | `deepen` → T10 Made, now | Then let's look at what else is given right now. |
| Fine, nothing special | `close` | Three breaths noticed is enough. Take it into the day. |
| Tight, anxious, dizzy | `come_up` → T42 Come down: feet, hands, the room | Let's leave the breath alone and feel the feet instead. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Turning it into breath control (counting, holding, slowing).* Leave the breath alone; only notice and thank.
- *Watching the breath anxiously.* Switch the anchor to the feet on the floor.

**Not for** *(contraindications)*. If attention to breathing raises panic, dizziness or tightness, stop at once and use the feet or hands instead (clinic BODY B08 guard). Never breath-holding or paced breathing.

**Body.** Seated upright and relaxed. Eyes closed or low. Hands resting. Breath only noticed, never the thing worked on.

**In daily life.** Three breaths of 'given, thank you' before eating, before answering a hard message, before sleep.

## T12 · The picture, and where it breaks

*Opens: ST04 Given right now, ST06 It is so, ST09 Less in the way · Level: Weeks 1-2 (after a few sittings) · Dose: 5-8 minutes. After T10, or when an idea stays dry.*

**Toward the true self** *(ours)*. Every picture of the deepest things fails at some point, and the failure points past the picture. The same is true of every picture you have of yourself.

**The practice in the source** *(stated)*. The mashal and its break: Chassidus clothes a truth in a picture so even a child can grasp it, then says where the picture fails, since the parable only settles the ear and does not truly resemble the thing.

> «רק שמשל זה, אינו אלא לשכך את האזן, אבל באמת, אין המשל דומה לנמשל כלל» (*this parable only settles the ear; in truth the parable does not resemble the thing at all*) · Tanya (the Alter Rebbe), Chabad Library text, `Tanya — Hebrew text.txt`, line 637
> «כי יותר בקל יפנה ע"י קריאת שמו משיאחזנו בגופו» (*he turns more easily by being called by his name than if someone took hold of his body*) · Maamarei Admur HaEmtzai (the Mitteler Rebbe), `Maamarei Admur HaEmtzai (Lubavitch, 1813-1827).txt`, line 2389

*Builds on:* TECHNOLOGY mashal; PS-02; FULL-DESCENT S01 step 3.

**How it works** *(ours)*. An image makes an idea vivid and emotional; the 'break' then stops the image from hardening into a belief about something smaller than the truth. It is insight in two steps: grasp, then go beyond. *(R10 Holmes & Mathews, R28 Teasdale)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | A picture. Someone calls your name across a room. | 6s |
| 2 | You turn, all of you, at once. Not because anyone grabbed you. Because you were called. | 12s |
| 3 | Now imagine that the world is like that. It stands because it is being called. | 15s |
| 4 | You too. You are here because you are being called, right now. | 15s |
| 5 | Now where the picture breaks: a person exists before anyone calls him. | 8s |
| 6 | The world doesn't. It exists only in the calling. | 12s |
| 7 | Let the picture fall away. Stay with what it pointed to. | 25s |
| 8 | Being called. Being here. The same thing. | 15s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 3: Now imagine the world is like that. It stands because G-d keeps calling it by name. - Step 8: Called by Him. Here. The same thing.

**Check-in** *(one tap)*: "Where did the picture take you?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Past the picture, to something quiet | `deepen` → T40 The quiet after | Stay there; don't explain it. |
| I'm stuck on the picture | `again_smaller` | Let's go straight to where it breaks. |
| Lost me | `switch` → T10 Made, now | Let's go back to something simpler: your hand. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Holding the picture as the truth (a literal voice, a literal caller).* Always say where it breaks.
- *Collecting pictures instead of staying.* The Piaseczner: once the feeling is there, stop hunting images.

**Not for** *(contraindications)*. None special. Keep images gentle; avoid any image that frightens the person.

**Body.** Seated. Eyes closed for the picture, open for the break if that helps. Hands resting. Breath left alone.

**In daily life.** When someone calls your name today, let it remind you: called, here.

## T13 · Walking it down to one thing

*Opens: ST04 Given right now, ST06 It is so · Level: Weeks 1-2 (after a few sittings) · Dose: 6-10 minutes. Weeks 1-2 onward.*

**Toward the true self** *(ours)*. If even a stone has a word inside it that keeps it alive, so do you. The inner word that keeps you here is the most yourself you can be.

**The practice in the source** *(stated)*. Hishtalshelus applied to one object: the Tanya traces the life of a stone down from the Ten Utterances to the combination of letters that is its name; that is the stone's life.

> «עד שמשתלשל מעשרה מאמרות ונמשך מהן צירוף שם ״אבן״, והוא חיותו של האבן» (*until it comes down from the Ten Utterances and the combination of the name even, stone, is drawn from them, and that is the stone's life*) · Tanya (the Alter Rebbe), Chabad Library text, `Tanya — Hebrew text.txt`, line 788

*Builds on:* TECHNOLOGY walk_down; ONE-PROCESS; ontology/LADDER.

**How it works** *(ours)*. Moving step by step from the most general idea to one specific thing in front of you is elaboration: it builds a detailed inner model that the heart can respond to, instead of a vague general belief that stays cold. *(R28 Teasdale, R06 Dahl, Wilson-Mendenhall & Davidson)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Pick one small thing near you. A stone, a cup, a leaf. | 6s |
| 2 | Start from the largest thing you can think of: everything that exists, being given now. | 15s |
| 3 | Now narrow it: this planet, this city, this room. | 15s |
| 4 | Now this one thing. Out of everything, this, here. | 12s |
| 5 | Inside it, something like a word, saying: be. Be this. Be here. | 20s |
| 6 | That inner word is its life. Without it, nothing would be left. | 15s |
| 7 | Look at the thing with that knowledge. | 25s |
| 8 | Now turn the same knowledge to yourself. A word inside you, saying: be. | 25s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 2: Start from the largest: all worlds, coming down from G-d's ten sayings at creation. - Step 5: Inside it, the letters of its name, His word, saying: be. - Step 8: Now yourself. His word inside you, saying: be.

**Check-in** *(one tap)*: "Where did it land?"

| Tap | Then | The guide says |
| --- | --- | --- |
| The thing feels alive | `deepen` → T18 One line, held long | Then let's hold one line about it, longer. |
| It landed on me | `deepen` → T34 Under all your names | Then let's go down through the layers of you. |
| Too abstract | `switch` → T10 Made, now | Let's take one step only: your hand, given now. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Turning it into a lecture about the worlds.* Spend most of the time on the one thing and on yourself.
- *Magical thinking about objects.* The point is that it is given, not that it has powers.

**Not for** *(contraindications)*. As T37. Keep the believer's language for those who welcome it.

**Body.** Seated, the object in hand or in view. Eyes open on the object. Breath left alone.

**In daily life.** Carry the small object (a pebble) in a pocket. Touching it: 'a word says be'.

## T14 · The first words on waking

*Opens: ST04 Given right now, ST13 Acting from it · Level: First session (safe for anyone on day one) · Dose: 30 seconds, every morning.*

**Toward the true self** *(ours)*. The first moment of the day, before roles and messages, is when you are most plainly yourself. Meeting it with thanks starts the day as someone receiving it, not someone holding it all up.

**The practice in the source** *(stated)*. Gratitude on waking: the order of the day begins with Modeh Ani, the thanks for the soul given back, said before anything else.

> «דער סדר פון טאג הויבט זיך אן מיט מודה אני» (*the order of the day begins with Modeh Ani*) · Hayom Yom (the Rebbe, from the Rebbeim), `Hayom Yom (Brooklyn, New York, 1942).txt`, line 84

*Builds on:* clinic BODY B13; WAYS W13; FULL-DESCENT S01 (deed).

**How it works** *(ours)*. A fixed first act tied to waking becomes automatic within weeks and sets the frame for the day. Gratitude practice reliably lifts mood and shifts attention toward what is given. *(R13 Emmons & McCullough, R14 Lally et al., R15 Gollwitzer & Sheeran)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Before you reach for anything, stay still in bed for a moment. | 5s |
| 2 | You woke up. You didn't arrange that. | 6s |
| 3 | Say, inside or in a whisper: thank you for giving me back to myself today. | 8s |
| 4 | Feel your body lying there for one breath. Given back too. | 8s |
| 5 | Sit up slowly. | 4s |
| 6 | Now the day. | 2s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 3: Say: Modeh ani lefanecha, I thank You, living King, for giving my soul back to me with kindness.

**Check-in** *(one tap)*: "Did you say it before the phone?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Yes | `close` | Good. Tomorrow the same. |
| I forgot | `again_smaller` | Put a note on the phone tonight: 'thank you first'. |
| I woke with dread | `switch` → T42 Come down: feet, hands, the room | Then keep it to one line and get up. Feet on the floor first. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Saying it on autopilot every day.* Once a week, say it slowly, meaning each word.
- *Lingering in bed with heavy thoughts and calling it practice.* One line, then up.

**Not for** *(contraindications)*. For people who wake with panic or dread: one line and getting up; do not linger (BODY B13 guard).

**Body.** Lying, then sitting up. Eyes may stay closed for the line. Hands open on the blanket. Breath left alone.

**In daily life.** It is the daily form. Pair it with washing the hands and a glass of water.

## ST05 · Held

*Held all around by something too big to grasp, and filled from inside, each thing to its own size. Safe at the level of being, while you still do your part.*

## T15 · The child before the parent

*Opens: ST05 Held, ST07 The heart answers · Level: Weeks 1-2 (after a few sittings) · Dose: 5-8 minutes. Weeks 1-2 onward.*

**Toward the true self** *(ours)*. A child asks without pretending. The picture lets the person speak from the plain, unguarded self they were before they learned to hold everything up.

**The practice in the source** *(stated)*. The Piaseczner's picturing: stand before the Throne of Glory and ask simply, like a child pleading with a father; the picture is a handrail for a mind made of clay, and once the feeling comes it falls away by itself.

> «ציר לך שאתה עומד לפני כסא כבודו ואתה מתפלל ומבקש ממנו ית' פשוט כבן שעומד ומתחנן מאביו» (*picture yourself standing before His Throne of Glory, praying and asking Him simply, like a son standing and pleading with his father*) · Bnei Machshava Tova (the Piaseczner), `Bnei Machshava Tova (Piaseczno, 1917-1923).txt`, line 91
> «אז התמונה הציור גופני הזה ממילא יתבטלו» (*then this bodily picture falls away of itself*) · Bnei Machshava Tova (the Piaseczner), `Bnei Machshava Tova (Piaseczno, 1917-1923).txt`, line 90

*Builds on:* CATALOGUE I2; TECHNOLOGY picturing; GM-06.

**How it works** *(ours)*. Imagery engages emotion far more than words alone. Picturing a safe, greater presence draws on the attachment system (feeling held and safe), which calms threat and makes honesty easier. Letting the picture go keeps it from becoming literal. *(R10 Holmes & Mathews, R31 Granqvist, Mikulincer & Shaver, R21 Luhrmann & Morgain)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Let your eyes close. | 5s |
| 2 | Picture yourself standing before something vast and kind. Larger than everything, and turned toward you. | 15s |
| 3 | You know it has no shape. The picture is only a handrail. Hold it lightly. | 8s |
| 4 | Stand there the way a small child stands before a parent who loves them. | 15s |
| 5 | Say plainly what is true. The thing you are carrying. No need to make it nice. | 25s |
| 6 | Notice you are not holding it alone now. | 20s |
| 7 | If the picture starts to fade, let it. Stay with the feeling that's left. | 25s |
| 8 | Stay a little longer. | 20s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 2: Picture yourself standing before the Throne of Glory. G-d, the King, turned toward you as a father. - Step 4: Stand there like a child before a father who loves you. - Step 5: Ask Him plainly for what you need. Name the thing. No need to make it nice. - Step 6: Notice you are not holding it alone. He is.

**Check-in** *(one tap)*: "How is it now?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Held, lighter | `deepen` → T40 The quiet after | Let the picture go and rest in what's left. |
| Tears or a lump | `deepen` → T28 Your own words | Let the words come. Say it to Him, or to whoever is there. |
| Can't picture anything | `switch` → T22 Borrow a love you already have | Then let's start from a love you already know. |
| Uneasy, a stern figure | `switch` → T11 The breath that comes by itself | Let's drop the picture. Just the breath that comes by itself. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Treating the picture as a real vision or a voice.* The source says the picture is a handrail and falls away. Say so.
- *Straining to make the picture vivid.* The Piaseczner: the harder you strain, the more it leaves. Go lightly.

**Not for** *(contraindications)*. Not for people whose experience of a parent or authority is of harm, unless they choose a different picture (a safe teacher, a sky). Not for people prone to visions or voices; imagery can increase unusual experiences.

**Body.** Seated or standing. Eyes closed. Hands open, palms up if that feels natural. Breath left alone.

**In daily life.** At a hard moment, a two-second picture: standing before the vast and kind, asking plainly.

## T16 · Nothing else holds power

*Opens: ST05 Held, ST06 It is so · Level: Weeks 1-2 (after a few sittings) · Dose: 2-5 minutes. When afraid of a person, an outcome or a power.*

**Toward the true self** *(ours)*. Fear tells you that you are small and alone against powerful things. Under the fear, at the root, you are joined to the only real power, and nothing else owns you.

**The practice in the source** *(stated)*. Ein od milvado (R. Chaim of Volozhin): fix in the heart that there is no other power at all besides Him, and pay no attention to any other power or will; the Piaseczner adds: say it softly, never forcefully, only to quiet the thoughts.

> «כשהאדם קובע בלבו לאמר הלא ה' הוא האלקים האמתי ואין עוד מלבדו יתברך שום כח בעולם» (*when a person fixes in his heart to say: God is the true God and there is no other power in the world besides Him*) · Nefesh HaChayim (R. Chaim of Volozhin), `Nefesh HaChayim.txt`, line 728
> «אבל לא שיאמר זאת בחזקה כי כל הענין הוא רק להשקיט מחשבותיו» (*but not that he say it forcefully, for the whole thing is only to quiet his thoughts*) · Derekh HaMelekh (the Piaseczner), `Derekh HaMelekh (Warsaw, 1931).txt`, line 1556

*Builds on:* CATALOGUE C4; P1-02; clinic DX K11.

**How it works** *(ours)*. A short, true sentence repeated softly is a form of reappraisal: it changes what the threat means, not the facts. Said gently and repeatedly, it lowers arousal; said forcefully, it becomes a fight and fails. *(R08 Webb, Miles & Sheeran, R34 Hobson et al.)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Bring to mind the thing you're afraid of. Just name it. | 8s |
| 2 | Notice how big it feels. How much power you've given it. | 10s |
| 3 | Now ask: where does its strength come from? Did it make itself? | 15s |
| 4 | Whatever power it has, it was given. It is not the source. | 10s |
| 5 | Softly, not hard: 'There is one Source. Nothing else holds power of its own.' | 15s |
| 6 | Say it again, slower. | 20s |
| 7 | Do the next practical step you need to do. Leave the rest with the Source. | 15s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 5: Softly: 'G-d is the true G-d. There is no other power besides Him.' - Step 7: Do the next practical step with your hands. Leave the outcome in His hands.

**Check-in** *(one tap)*: "How is the fear now?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Smaller, calmer | `close` | Let's choose the one practical step and the line to carry. |
| About the same | `again_smaller` | Once more, softer. Not to win an argument. Only to quiet. |
| Rising, panicky | `come_up` → T42 Come down: feet, hands, the room | Let's put it down and feel the floor first. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Using the sentence to deny a real danger or skip a needed action.* Always pair with the practical step (step 7).
- *Saying it forcefully, like a battle cry.* The source: not forcefully. Whisper it.

**Not for** *(contraindications)*. Not a substitute for safety in a real threat (abuse, medical emergency): act first. Not for anxiety disorders as treatment; use alongside care.

**Body.** Seated, feet down. Eyes closed or open. Hands on the knees. Breath left alone.

**In daily life.** Before a feared meeting or call: the sentence once, softly, then the step.

## T17 · The bedtime return

*Opens: ST05 Held, ST13 Acting from it · Level: First session (safe for anyone on day one) · Dose: 2-4 minutes, every night.*

**Toward the true self** *(ours)*. At night you set down everything you did and played. What remains to be handed back is just you, which is the part that was always given.

**The practice in the source** *(stated)*. The Baal Shem Tov: when going to sleep, think that the mind is going to the Holy One and will be strengthened; the bedtime Shema hands the soul back for the night.

> «וכשהולך לישן יחשוב הלא המוחין שלו ילכו להקב"ה ויתחזקו לעבודתו» (*when he goes to sleep let him think: my mind is going to the Holy One and will be strengthened for His service*) · Tzava'at HaRivash (the Baal Shem Tov, as collected), `Tzava'at HaRivash (Medzhibozh and Mezritch, c. 1740-1770).txt`, line 41

*Builds on:* clinic BODY B12; WAYS W12; P1-02 stage 4.

**How it works** *(ours)*. A fixed wind-down routine improves sleep and closes the day's loops. Ending on what was good, and on letting go, reduces the night-time rumination that keeps people awake. *(R13 Emmons & McCullough, R14 Lally et al.)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Lie down. Let the bed take your whole weight. | 8s |
| 2 | One thing that was good today. Just one. | 15s |
| 3 | If someone hurt you today, set it down for tonight. You can pick it up tomorrow if you need to. | 15s |
| 4 | Whatever is unfinished, it will keep until morning. | 8s |
| 5 | Now hand yourself over for the night. Say inside: I give myself back to be kept. | 10s |
| 6 | Let your body be held. | 20s |
| 7 | Sleep is the practice now. | 0s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 2: One thing that was good today. Thank G-d for it. - Step 3: If someone hurt you today, forgive them for tonight, as the bedtime prayer does. - Step 5: Say the Shema, or: Into Your hand I give my spirit.

**Check-in** *(one tap)*: "How are you, lying there?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Settled, ready to sleep | `close` | Good night. Tomorrow starts with thank you. |
| Mind still racing | `switch` → T20 Come back without a fight | Pick one soft word and come back to it each time, until sleep. |
| Sad or lonely | `switch` → T15 The child before the parent | Then let yourself be held, like a child before sleep. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Turning it into a long self-review that keeps you awake.* One good thing only. The accounting belongs earlier (T46).
- *Forcing forgiveness you don't feel.* Set it down for tonight; that is enough.

**Not for** *(contraindications)*. For someone low or crushed: only 'one good thing'; no review of failures. Persistent insomnia: a check-up.

**Body.** Lying down. Eyes closed. Hands open by the sides or on the chest. Breath left alone.

**In daily life.** It is the daily form: screens off a little before, then this.

## ST06 · It is so

*The idea stops being an idea and becomes a fact you see, as plain as the table. You no longer have to argue for it.*

## T18 · One line, held long

*Opens: ST06 It is so, ST07 The heart answers · Level: Weeks 1-2 (after a few sittings) · Dose: 8-15 minutes; the core sitting from week 2. Same line for a week.*

**Toward the true self** *(ours)*. What you hold in your mind for a long time becomes part of you. Holding one true line until it is real is how the deepest truth becomes your own, not borrowed.

**The practice in the source** *(stated)*. Hisbonenus: deepen the mind in one idea and fix the thought on it with strength until it is as vivid as a thing seen with the eyes; the Mitteler Rebbe calls this standing on the idea and looking into it, the opposite of speed.

> «להעמיק דעתו בגדולת ה׳, ולתקוע מחשבתו בה׳ בחוזק ואומץ הלב והמוח» (*to deepen his mind in the greatness of God and fix his thought on God with strength and firmness of heart and mind*) · Tanya (the Alter Rebbe), Liozna text, `Tanya (Liozna, 1786-1796).txt`, line 607
> «שעומד על דבר המושכל ומעיין בו הרבה מאד, שהוא העיכוב היפך המהירות» (*he stands on the idea and looks into it very much: the pausing, the opposite of speed*) · Sha'ar HaYichud, the Gate of Unity (the Mitteler Rebbe), `The Gate of Unity (Lubavitch, pub. 1820).txt`, line 24

*Builds on:* CATALOGUE C1; TECHNOLOGY choose_line, breadth, length, depth; GM-10; GM-16; integration MAP I2-I4.

**How it works** *(ours)*. Elaboration (breadth: many angles; length: down to one's own life; depth: the point itself) turns 'knowing that' into 'feeling that'. Sustained attention on one meaning is the core mechanism by which an insight changes a person. *(R28 Teasdale, R06 Dahl, Wilson-Mendenhall & Davidson, R01 Lutz, Slagter, Dunne & Davidson)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Today's line: 'Everything here is being given, right now, from one Source.' | 8s |
| 2 | Say it slowly. Then just hold it. | 15s |
| 3 | Widen it: the sky, the city, your body, this chair. All of it, given now. | 30s |
| 4 | Bring it down: your morning. The coffee. The person you spoke with. Given. | 30s |
| 5 | Bring it into one detail: this one breath. This one heartbeat. | 25s |
| 6 | When the mind wanders, come back to the line without a fight. | 20s |
| 7 | Now stop adding. Stand on the line. Look into it. | 40s |
| 8 | What is it, at its point? Don't answer in words. | 40s |
| 9 | Say the line once more. | 10s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 1: Today's line: 'G-d is giving all of this being, right now. There is nothing apart from Him.' - Step 3: Widen it: the heavens and earth, all of them, His, given now. - Step 9: Say the line once more, to Him.

**Check-in** *(one tap)*: "How is the line now?"

| Tap | Then | The guide says |
| --- | --- | --- |
| It feels true, not just an idea | `deepen` → T40 The quiet after | Then stop thinking and stay in it. |
| Something warm or awed | `deepen` → T23 Love answers love | Let the heart answer. |
| Still just words | `switch` → T24 The hum that sings itself | Let's carry the same line on a hum. |
| Couldn't stay on it | `switch` → T20 Come back without a fight | Let's practice coming back, with a shorter line. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *General thoughts about 'the universe' that never reach your day.* The Rashab: general is no contemplation. Go into details from your own life.
- *Working up a feeling on purpose.* Ask for the thinking; never demand the feeling.

**Not for** *(contraindications)*. Needs a settled mind: after T04 if scattered. Not on a crushed day (use T22, T25). For people in crisis, never.

**Body.** Seated, upright. Eyes closed. Hands still. A quiet tune may carry it (T24). Breath left alone.

**In daily life.** Carry the same line all week (T44). Say it once each hour on the hour if possible.

## T19 · Two knowings

*Opens: ST06 It is so, ST08 Awe, small and glad, ST09 Less in the way, ST11 The world see-through · Level: Weeks 1-2 (after a few sittings) · Dose: 8-15 minutes; can be split into two sittings, one knowing each.*

**Toward the true self** *(ours)*. You are both: really here, a real person with a real life, and wholly from the Source. Holding both at once is how you stop choosing between being yourself and being close to what is deepest.

**The practice in the source** *(stated)*. The Tanya (Iggeret HaKodesh 20): 'before Him' is His knowledge from above downward, in which all is as nothing; in the knowledge from below upward, the created thing is a completely separate thing. Both are true. The Baal Shem Tov: if a person knows that the Holy One is hiding there, it is no hiding.

> «היינו קמיה דוקא, שהיא ידיעתו יתברך מלמעלה למטה» (*that is 'before Him' precisely: His knowledge from above downward*) · Tanya (the Alter Rebbe), Chabad Library text, `Tanya — Hebrew text.txt`, line 1289
> «אבל בידיעה שממטה למעלה – היש הנברא הוא דבר נפרד לגמרי» (*but in the knowledge from below upward, the created 'something' is a completely separate thing*) · Tanya (the Alter Rebbe), Chabad Library text, `Tanya — Hebrew text.txt`, line 1290
> «שאם ידע האדם שהקב"ה מסתתר שם אין זה הסתרה» (*if a person knows that the Holy One is hiding there, it is no hiding*) · Keter Shem Tov (the Baal Shem Tov), `Keter Shem Tov (Medzhibozh, Ukraine, c. 1740-1760).txt`, line 92

*Builds on:* stage-book Stage 6; manual L03, L05; ONE-PROCESS step 5.

**How it works** *(ours)*. Holding two true perspectives at once, without collapsing them, is a known mark of mature thinking and guards against two errors: a cold 'nothing matters' and a flat 'there is only the world'. Perspective-taking of this kind is a form of reappraisal that keeps both meaning and reality. *(R08 Webb, Miles & Sheeran, R28 Teasdale)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Today we hold two true things at once. Don't merge them. | 6s |
| 2 | First knowing. From the side of the Source, everything is being given, every second. Nothing stands on its own. | 25s |
| 3 | Stay there a minute. Let it be true. | 40s |
| 4 | Second knowing. From your side, this table is really a table. You are really you. Your life is real. | 25s |
| 5 | Stay there a minute. Let that be true too. | 40s |
| 6 | Now both. Like looking up and down at the same time. Don't make them one. | 30s |
| 7 | Notice: the world seems to run by itself. That seeming is the Source hiding. Once you know it is hiding there, it is not hidden. | 20s |
| 8 | Choose the thing today that seemed emptiest. You'll say a quiet thank-you over it. | 10s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 2: First knowing. Before G-d, all is as nothing; only He truly is. - Step 7: The world seems to run by itself. That is G-d hiding. If you know He is hiding there, it is no hiding. - Step 8: Choose the thing today that seemed emptiest of Him. Say a blessing over it slowly.

**Check-in** *(one tap)*: "Can you hold both?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Yes, both at once | `deepen` → T37 Seeing the garment | Then look at the world with both eyes: solid, and see-through. |
| One keeps swallowing the other | `again_smaller` | Say the other one aloud whenever you notice. One minute each again. |
| It turned into a debate in my head | `switch` → T38 The meal received | Leave the philosophy. One plain thing, one thank-you. |
| The world feels unreal | `come_up` → T42 Come down: feet, hands, the room | The second knowing is just as true. Feel the table. Feet down. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *'It's all one, so right and wrong melt.'* The unity does not cancel the distinctions (stage-book Stage 6, Korach's error). Right is still right.
- *Using 'it's hidden' to explain someone else's suffering.* Never. This is for your own heart only.

**Not for** *(contraindications)*. Not for someone feeling unreal or detached (the first knowing can feed it); not as a first practice. Never applied to another person's pain.

**Body.** Seated. Eyes closed for the first knowing, open on a solid object for the second. Hands on the table. Breath left alone.

**In daily life.** Heart above, eyes below: once a day, over something ordinary, both knowings and a thank-you.

## T20 · Come back without a fight

*Opens: ST06 It is so, ST02 The watcher · Level: First session (safe for anyone on day one) · Dose: Inside any technique. As a drill: 3-5 minutes on one line or object.*

**Toward the true self** *(ours)*. Every return is a small act of choosing what you care about most. The returning, not the never-wandering, is where the self shows itself.

**The practice in the source** *(stated)*. The Tanya: when stray thoughts fall in during prayer, act as one who does not know or hear them; do not argue with them and do not fall into sadness over them. The Piaseczner: the more you push them away, the stronger they get.

> «רק יעשה עצמו כלא יודע ולא שומע ההרהורים שנפלו לו» (*rather let him act as one who does not know and does not hear the thoughts that fell into him*) · Tanya (the Alter Rebbe), Liozna text, `Tanya (Liozna, 1786-1796).txt`, line 379
> «כי כל מה שירצה לדחותם הם יתחזקו בו» (*the more he tries to push them away, the stronger they get*) · Derekh HaMelekh (the Piaseczner), `Derekh HaMelekh (Warsaw, 1931).txt`, line 1551

*Builds on:* CATALOGUE E3 (the dispute); TECHNOLOGY binding; PS-19.

**How it works** *(ours)*. Minds wander in a cycle: wander, notice, return, stay. The skill is the return, done gently. Fighting a thought makes it come back more (the ironic effect of suppression); quietly returning trains attention without feeding the stray thought. *(R02 Hasenkamp et al., R19 Wang, Hagger & Chatzisarantis, R01 Lutz, Slagter, Dunne & Davidson)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Choose one simple thing to rest on: a line, a word, or the feeling of your hands. | 5s |
| 2 | Rest your attention there. | 20s |
| 3 | When you notice you've drifted, that noticing is the practice. Good. | 5s |
| 4 | Don't argue with the stray thought. Don't follow it. Just come back. | 20s |
| 5 | Come back again, as many times as it takes. Each time is one repetition. | 30s |
| 6 | No scolding. A drift is not a failure; the return is a success. | 30s |
| 7 | Last return. Stay a moment. | 15s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 1: Choose one simple thing to rest on: a verse, a word of prayer, or 'You are here'. - Step 6: No scolding, and no sadness over it. Every return is a turning back to Him.

**Check-in** *(one tap)*: "How was coming back?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Got easier | `deepen` → T18 One line, held long | Then you're ready to hold one line longer. |
| I kept drifting | `again_smaller` | That's every beginner. Let's do two minutes, with a shorter line. |
| I got frustrated with myself | `switch` → T25 Gather the good points | Let's put the scolding down and find what's good. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Turning each drift into a verdict on oneself.* Say: the Tanya forbids sadness over it during the practice. Count returns as wins.
- *Wrestling with the content of the stray thought.* Act as if you did not hear it. Return only.

**Not for** *(contraindications)*. None. Keep it short for people prone to self-criticism, and praise returns.

**Body.** Any steady posture. Eyes as the person prefers. Hands still. Breath not used as the object; if someone likes it as a resting place, it may be one natural anchor, never counted or controlled.

**In daily life.** In conversation or at work: notice the drift, come back without comment. Same skill.

## T21 · The held word

*Opens: ST06 It is so, ST01 Here, ST12 The quiet after · Level: Weeks 1-2 (after a few sittings) · Dose: 3-5 minutes.*

**Toward the true self** *(ours)*. When you put all of yourself into one word, there is no room left for the scattered self. You are wholly in it, and wholly you.

**The practice in the source** *(stated)*. The Baal Shem Tov: every word is a complete stature, so put all your strength in it; when a word holds you, lengthen it, not wanting to part from it; begin slowly.

> «דע כי כל תיבה הוא קומה שלימה וצריך להיות כל כחו בה» (*know that every word is a complete stature, and all his strength must be in it*) · Tzava'at HaRivash (the Baal Shem Tov, as collected), `Tzava'at HaRivash (Medzhibozh and Mezritch, c. 1740-1770).txt`, line 58
> «שמחמת דביקות אינו רוצה לפרוד עצמו מהתיבה ולכך מאריך באותה תיבה» (*because of devekus he does not want to part from the word, so he lengthens that word*) · Tzava'at HaRivash (the Baal Shem Tov, as collected), `Tzava'at HaRivash (Medzhibozh and Mezritch, c. 1740-1770).txt`, line 126

*Builds on:* CATALOGUE L3; TECHNOLOGY lips; CATALOGUE L1.

**How it works** *(ours)*. Slow, full-attention speech of one word or phrase narrows attention and steadies the body (slow vocal rhythm). Lingering on one word lets its meaning open, instead of rushing past it. *(R01 Lutz, Slagter, Dunne & Davidson, R34 Hobson et al.)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Choose a short phrase that matters to you. For example: 'Here I am.' | 8s |
| 2 | Say it aloud, slowly, with your whole strength in each word. Not loud. Full. | 12s |
| 3 | Again. Each word complete, like a whole person standing. | 15s |
| 4 | Now find the word that holds you most. Stay on it. | 10s |
| 5 | Lengthen it in your mind. Don't want to leave it. | 30s |
| 6 | Let it fill you. | 30s |
| 7 | Say the whole phrase once more, and rest. | 15s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 1: Choose a word of prayer that matters to you, or 'Hineni', here I am. - Step 6: Let it fill you. G-d is in the letters of that word.

**Check-in** *(one tap)*: "How was it to stay on one word?"

| Tap | Then | The guide says |
| --- | --- | --- |
| The word held me | `deepen` → T40 The quiet after | Rest in what the word left. |
| It went mechanical | `switch` → T24 The hum that sings itself | Let's carry it on a tune instead. |
| My mind wandered off | `switch` → T20 Come back without a fight | Then we'll practise coming back, gently. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Repeating the phrase faster and faster.* Slow start, the source says; one word at a time.
- *Straining the voice.* Full is not loud.

**Not for** *(contraindications)*. None special.

**Body.** Seated or standing. Eyes closed, or open on the written words if that helps (the Baal Shem Tov: at a beginning level, looking at the letters helps). Breath follows the speaking naturally.

**In daily life.** One word of a daily prayer or a phrase you love, said fully once a day.

## ST07 · The heart answers

*Something moves under the thinking: warmth, tenderness, a pull toward what is good that you did not make and that wants nothing back. Often a feather, not a fire.*

## T22 · Borrow a love you already have

*Opens: ST07 The heart answers · Level: First session (safe for anyone on day one) · Dose: 3-5 minutes. Good for a cold or numb day.*

**Toward the true self** *(ours)*. The ability to love is already in you; it is one of the plainest signs of who you are. You don't have to manufacture a new love, only let the one you have flow back to its source.

**The practice in the source** *(stated)*. The Piaseczner: when the heart is cold, let a person remind himself of his love for his children, even for his money, and point that love one step further.

> «יזכיר לו אהבתו לבניו אף לממונו» (*let him remind himself of his love for his children, even for his money*) · Esh Kodesh (the Piaseczner), `Esh Kodesh (Warsaw Ghetto, 1941).txt`, line 213

*Builds on:* TECHNOLOGY arrive (step 3); animal-soul M15-M17; P1-03.

**How it works** *(ours)*. Recalling a real, felt love activates warmth that can then be widened. Loving-kindness practice works this way: start from someone easy to love and extend. Positive emotions built this way grow lasting resources. *(R12 Fredrickson et al., R11 Weng et al.)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Think of someone or something you love without trying. A child, a friend, an animal, even a place. | 10s |
| 2 | See them clearly. Let the warmth come up by itself. | 20s |
| 3 | Notice where you feel it. Chest, face, hands. | 15s |
| 4 | Now ask: where does this love come from? You didn't invent it. | 15s |
| 5 | Let it go one step further, past them, toward where love itself comes from. | 25s |
| 6 | Stay in the warmth, without needing an object for it. | 30s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 5: Let it go one step further, toward G-d, the source of every love. - Step 6: Stay in the warmth before Him.

**Check-in** *(one tap)*: "What happened to the warmth?"

| Tap | Then | The guide says |
| --- | --- | --- |
| It got wider | `deepen` → T23 Love answers love | Then let it answer the love that is already coming to you. |
| It stayed with them | `close` | That's good too. Do one kind thing for them today. |
| I couldn't feel it | `switch` → T27 The cry of one who feels nothing | That's all right. There's a practice for exactly this. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Sentimental feeling that ends with the sitting.* Close with one act for someone (T43).
- *Grief rising instead of warmth.* If the loved one is lost, honor the grief; go to T28 and do not push further.

**Not for** *(contraindications)*. Choose a safe love. If thinking of loved ones brings grief or fear, use a place or an animal, or another technique.

**Body.** Seated. Eyes closed. One hand on the chest if that feels natural. Breath left alone.

**In daily life.** When you feel love for someone today, add one silent step: 'and further'.

## T23 · Love answers love

*Opens: ST07 The heart answers · Level: Weeks 1-2 (after a few sittings) · Dose: 5-8 minutes.*

**Toward the true self** *(ours)*. You were wanted before you did anything. Love that answers that is not effort; it is the self recognizing where it comes from.

**The practice in the source** *(stated)*. The Tanya: as water gives back a face to a face, so the heart of a person answers a person; considering how one is loved draws out love in return.

> «כמים הפנים לפנים, כן לב האדם אל האדם» (*as water gives back face to face, so the heart of a person to a person*) · Tanya (the Alter Rebbe), Chabad Library text, `Tanya — Hebrew text.txt`, line 680

*Builds on:* TECHNOLOGY heart_after; GM-11; animal-soul M23.

**How it works** *(ours)*. Feeling loved and secure is a strong base for warmth toward others and toward life (attachment research). Reflecting on care received is a well-tested way to raise gratitude and connection. *(R31 Granqvist, Mikulincer & Shaver, R13 Emmons & McCullough, R12 Fredrickson et al.)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Bring to mind that you are here because you are wanted. Your existence is given, every second. | 15s |
| 2 | Nobody gives something every second to what they don't want. | 10s |
| 3 | Let that sink in: wanted. Not for what you do. For being. | 25s |
| 4 | Like a face in water, the heart answers what faces it. | 10s |
| 5 | Let your heart face the one that wants you, and see what it answers. | 30s |
| 6 | Whatever comes, warmth or only a little, let it go back. | 25s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 1: Bring to mind that G-d wants you. He gives you being every second. - Step 3: Let it sink in: G-d wants you, not for what you do, for being. - Step 5: Let your heart face Him, and see what it answers.

**Check-in** *(one tap)*: "What does your heart answer?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Love, warmth | `deepen` → T43 The deed done slowly | Let it go into one act today. Love that stays inside is a flame in the air. |
| Tears | `deepen` → T28 Your own words | Let them come. Say a word to whoever you're facing. |
| I don't feel wanted | `switch` → T10 Made, now | Let's go back to the plain fact first: given, now. The feeling can come later. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Chasing a feeling of being loved; disappointment when it doesn't come.* Ask for the thinking, never demand the feeling.
- *Love that never reaches a person or an act.* Close with T43.

**Not for** *(contraindications)*. For people with deep rejection wounds the line 'you are wanted' can hurt at first; go slowly, start with T10.

**Body.** Seated. Eyes closed. Hands open. Breath left alone.

**In daily life.** When someone shows you care today, let it remind you of the larger care, and answer both.

## T24 · The hum that sings itself

*Opens: ST07 The heart answers, ST01 Here, ST05 Held · Level: First session (safe for anyone on day one) · Dose: 2-5 minutes. Any time; especially when cold or dry.*

**Toward the true self** *(ours)*. At first you sing the tune. After a while the tune sings itself, and you find a part of you that longs and rises without being told to. That part is you too, the deepest part.

**The practice in the source** *(stated)*. The niggun: the Piaseczner says take a turn of melody, face the wall or close your eyes, and little by little you will feel your soul has begun to sing by itself; a whispered hum is enough; the Rebbe Rashab: through melody the soul is moved most.

> «קח לך איזו תנועה של ניגון, תסב את פניך אל הקיר, או רק תסגור את עיניך» (*take some turn of melody, turn your face to the wall, or just close your eyes*) · Hakhsharat HaAvrekhim (the Piaseczner), `Hakhsharat HaAvrekhim (Warsaw, 1930-1940).txt`, line 279
> «מעט מעט תרגיש שנפשך התחילה כבר לנגן מעצמה» (*little by little you will feel your soul has begun to sing by itself*) · Hakhsharat HaAvrekhim (the Piaseczner), `Hakhsharat HaAvrekhim (Warsaw, 1930-1940).txt`, line 279
> «כי יש מי שמנגן רק המיה בלחש וקולו נשמע במרום» (*for there is one who sings only a whispered hum, and his voice is heard on high*) · Bnei Machshava Tova (the Piaseczner), `Bnei Machshava Tova (Piaseczno, 1917-1923).txt`, line 245

*Builds on:* CATALOGUE B1; TECHNOLOGY niggun; GM-07; VS-09.

**How it works** *(ours)*. Music strongly moves emotion and reward systems, and wordless humming bypasses the analytic mind. A slow repeated tune also steadies the body and gives the moment a container. *(R22 Salimpoor et al., R34 Hobson et al.)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Close your eyes, or turn toward a wall. | 5s |
| 2 | Hum a slow, simple tune. Any tune that has some longing in it. Quietly. | 30s |
| 3 | Don't perform it. Let it be slow. | 30s |
| 4 | Let the tune carry a feeling you can't put into words. | 30s |
| 5 | Keep going. See if, after a while, it starts to hum itself. | 40s |
| 6 | Let it fade on its own. | 20s |
| 7 | Sit in the quiet it leaves. | 20s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 4: Let the tune carry what you want to say to G-d and can't put into words.

**Check-in** *(one tap)*: "What did the tune do?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Something opened | `deepen` → T28 Your own words | Say a few words, now, from where the tune left you. |
| Quiet and settled | `deepen` → T40 The quiet after | Stay in the quiet. |
| Nothing, felt silly | `close` | That's fine. A niggun is a preparation; it can work later. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Singing for the sound, with nothing behind it.* The Baal Shem Tov's warning: not like one just playing an instrument. Let it carry something.
- *Getting worked up and loud.* Keep it soft; a whisper is enough.

**Not for** *(contraindications)*. None special. If a tune brings back painful memories, choose another.

**Body.** Seated, facing a wall or with eyes closed. Hands still. The breath follows the tune naturally; never controlled.

**In daily life.** Hum the same tune walking or doing dishes. It brings back the sitting in seconds.

## T25 · Gather the good points

*Opens: ST07 The heart answers, ST02 The watcher · Level: Weeks 1-2 (after a few sittings) · Dose: 3-6 minutes. Good after a failure, or in the evening.*

**Toward the true self** *(ours)*. Under the verdict 'I'm my mistakes' are points of good that were never erased. Gathering them is finding the self that the mistakes covered.

**The practice in the source** *(stated)*. Azamra (Rebbe Nachman): search and find in a person some little good in which he is not bad, and then another; do the same with yourself, gathering the good points still in you.

> «צריך לחפש ולמצא בו איזה מעט טוב, שבאותו המעט אינו רשע» (*one must search and find in him some little good, in which he is not wicked*) · Likutei Moharan (Rebbe Nachman), `Likutei Moharan (Bratslav, Ukraine, 1802-1808).txt`, line 5332
> «לחפש הרוח טובה, דהינו הנקדות טובות שיש בו עדין» (*to seek the good spirit, that is, the good points still in him*) · Likkutei Etzot (Rebbe Nachman), `Likkutei Etzot (Bratslav, Ukraine, 1790-1810).txt`, line 333

*Builds on:* CATALOGUE S3; P2-03; clinic DX K12.

**How it works** *(ours)*. Self-criticism keeps the threat system on; deliberately finding real good shifts attention and builds self-compassion, which supports change better than shame. It is specific, so it is believable. *(R11 Weng et al., R12 Fredrickson et al., R08 Webb, Miles & Sheeran)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Think of today, or of yourself in general. Don't argue with the hard parts. | 8s |
| 2 | Search for one small good thing. A kind word. A moment you held back. Something you tried. | 25s |
| 3 | Found one? Hold it. That point is really you. | 15s |
| 4 | Now look for another. However small. | 25s |
| 5 | And another. | 25s |
| 6 | Notice: the good points are still there. Nothing erased them. | 15s |
| 7 | Let a little gladness come from that. | 20s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 3: Hold it. That point is really you, the part of you that is from G-d. - Step 6: The good points are still there. Nothing erased them, and G-d sees them.

**Check-in** *(one tap)*: "How do you feel about yourself now?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Lighter, kinder | `deepen` → T24 The hum that sings itself | Hum something glad. The good points make a tune. |
| I found very few | `again_smaller` | Even one is enough. Let's look for just one more, tiny one. |
| I can't find any | `switch` → T34 Under all your names | Let's go under the deeds, to a point nothing touched. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Denying real wrongs.* It looks for the point in which you are not bad; it doesn't erase the rest.
- *Praising oneself to feel superior.* Do the same for someone else today (T47).

**Not for** *(contraindications)*. Safe for most. For severe depression or self-hatred, use it gently and alongside professional care; never leave someone alone with 'I can't find any'.

**Body.** Seated. Eyes closed. Hands open. Breath left alone.

**In daily life.** After a mistake today: one good point, before any self-blame. Then the repair.

## T26 · Mercy for the spark

*Opens: ST07 The heart answers, ST10 The self beneath the layers · Level: Weeks 1-2 (after a few sittings) · Dose: 4-6 minutes. For the verdict, numbness, or feeling far.*

**Toward the true self** *(ours)*. Under the struggle there is something in you that is pure and was dragged through all of it. Feeling for it, not against yourself, is how you come close to it again.

**The practice in the source** *(stated)*. The Tanya (ch. 45): first rouse in your thought great compassion before G-d for the spark of G-dliness that gives life to your soul, which has gone down into exile in the body. The pity is for the spark, not self-pity.

> «לעורר במחשבתו תחלה רחמים רבים לפני ה׳ על ניצוץ אלהות המחיה» (*to rouse first in his thought great compassion before G-d for the spark of G-dliness that gives life (to his soul)*) · Tanya (the Alter Rebbe), Chabad Library text, `Tanya — Hebrew text.txt`, line 675

*Builds on:* clinic DX K12; MAP S54; FULL-DESCENT S20; animal-soul M22.

**How it works** *(ours)*. Compassion turned toward one's own deepest core, rather than toward the struggling surface self or against it, softens self-criticism without becoming self-pity. Self-compassion is linked to more change, not less, because it lowers threat. *(R11 Weng et al., R12 Fredrickson et al.)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Think of the deepest good in you. Not your achievements. The part that is pure, that wanted good from the start. | 15s |
| 2 | Picture it as a small child, or a small light, carried through everything you've been through. | 15s |
| 3 | All the noise, the mistakes, the hard years. It was there, inside, through all of it. | 20s |
| 4 | Let your heart go out to it. Not pity for yourself. Tenderness for that small light. | 25s |
| 5 | Ask for it, not for yourself: may it have room. May it come out. | 20s |
| 6 | Stay with the tenderness. | 25s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 1: Think of the spark of G-d in you, the soul that gives you life. - Step 4: Let your heart go out to it, before G-d. Great compassion, for the spark. - Step 5: Ask G-d for it: may it come out of exile.

**Check-in** *(one tap)*: "What is there now?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Tenderness | `deepen` → T28 Your own words | Speak for that light, in your own words. |
| Feeling sorry for myself | `switch` → T25 Gather the good points | Let's turn it: find the good points instead. |
| Tears | `close` | Let them be. They are not sadness here. One gentle act today. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Self-pity that stays in itself.* The pity is for the light, and it ends in asking for it and in one act.
- *Sadness that deepens.* The Besht: guard against sadness. Close with T25 or T24.

**Not for** *(contraindications)*. For depression, keep short and end in an act; not alone in a crisis. Not for someone who uses it to stay stuck.

**Body.** Seated. Eyes closed. One hand on the chest if natural. Breath left alone.

**In daily life.** When you speak harshly to yourself today: 'the small light'. Then one kind act toward yourself.

## T27 · The cry of one who feels nothing

*Opens: ST07 The heart answers, ST10 The self beneath the layers · Level: Weeks 1-2 (after a few sittings) · Dose: 3-5 minutes. For numb, dry, flat days.*

**Toward the true self** *(ours)*. Numbness is not the absence of a self; it is a self asleep. The ache of feeling nothing is itself the deepest self, missing what it is made for.

**The practice in the source** *(stated)*. The Rebbe Rayatz: one who has no feeling at all for the Infinite, and cries from the depth of the heart only from the pain of his distance, reveals the essence of the soul; the Mitteler Rebbe: even with no feeling in the heart he will come to a great stirring.

> «בהצעקה שצועק מעומקא דליבא מתגלה עצם הנשמה ברצוא» (*in the cry he cries from the depth of the heart, the essence of the soul is revealed in longing*) · Sefer HaMaamarim (the Rebbe Rayatz), `Sefer HaMaamarim (Riga and Otwock, 1929-1933).txt`, line 1417
> «גם שעדיין אין בלבו שום התפעלות יבא לכלל התפעלות גדולה בעצמות הנפש» (*even with no feeling in his heart, he will come to a great stirring*) · Toras Chaim (the Mitteler Rebbe), `Toras Chaim (Lubavitch, c. 1820-1827).txt`, line 2589

*Builds on:* FULL-DESCENT S25, S26; P1-03; MAP S03; GM-13.

**How it works** *(ours)*. Naming numbness honestly, instead of pretending to feel, removes the strain that keeps it frozen. Turning the ache itself into the object of attention (the want of a want) is often the first real feeling to return. *(R09 Lieberman et al., R25 Kircanski, Lieberman & Craske)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | You feel nothing right now. That's all right. We start there. | 6s |
| 2 | Don't try to feel anything else. | 8s |
| 3 | Notice instead: is there any part of you that wishes you felt something? | 20s |
| 4 | Even a little 'I wish'. That wish is a feeling. | 15s |
| 5 | Let that wish say something, even one word. Silently. 'Please.' Or 'Where are you?' | 20s |
| 6 | Say it from the bottom, not loudly. From far away is fine. | 25s |
| 7 | That cry from far away is real. It is the deepest part of you, awake. | 20s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 5: Let that wish say something to G-d. Even one word. 'Please.' 'Where are You?' - Step 7: That cry from far away is the essence of your soul calling Him. It is heard.

**Check-in** *(one tap)*: "What is there now?"

| Tap | Then | The guide says |
| --- | --- | --- |
| A small something | `deepen` → T28 Your own words | Let it say a few more words. |
| Still nothing | `close` | Asleep, not dead. You did the practice. One small deed now, and that counts. |
| Heavy, hopeless | `stop` | Thank you for telling me. Let's talk plainly for a minute about how you've been. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Performing a cry that isn't there.* Only the wish, as small as it really is.
- *Measuring yourself by feelings ('I'm dead inside').* The sources: asleep, not dead. Judge by acts, not feelings.

**Not for** *(contraindications)*. Persistent numbness with low mood, hopelessness or loss of interest for weeks is a reason to see a doctor or therapist; this practice is not treatment.

**Body.** Seated or lying. Eyes closed. Hands open. Breath left alone.

**In daily life.** On a flat day: one 'I wish', and one small good act anyway (T43).

## T28 · Your own words

*Opens: ST07 The heart answers, ST03 Before, ST05 Held, ST10 The self beneath the layers · Level: First session (safe for anyone on day one) · Dose: 5-15 minutes. Daily if possible; start with 5.*

**Toward the true self** *(ours)*. Saying what is really true, in your own words, is how you meet yourself. Rebbe Nachman adds that it is also how you meet the One you are speaking to.

**The practice in the source** *(stated)*. Hisbodedus (Rebbe Nachman): set a time to pour out your heart in your own language, as one talks to a teacher or a friend; the Piaseczner: speech itself loosens the knots in the soul.

> «וצריך כל אחד לקבע לו על זה איזה שעות ביום, שיפרש שיחתו לפני השם יתברך בלשון שמדברים בו» (*each person must set some hours in the day for this, to pour out his speech before God in the language he speaks*) · Likkutei Etzot (Rebbe Nachman), `Likkutei Etzot (Bratslav, Ukraine, 1790-1810).txt`, line 338
> «שידבר עם השם יתברך כמו שמדבר עם רבו או חברו» (*that he speak with God as he speaks with his teacher or his friend*) · Likkutei Etzot (Rebbe Nachman), `Likkutei Etzot (Bratslav, Ukraine, 1790-1810).txt`, line 345
> «הדבור בעצמו גדול כחו להוציא את החרצובות מקרב הנפש» (*speech itself has great power to loosen the knots inside the soul*) · Tzav VeZeruz (the Piaseczner), `Tzav VeZeruz (Warsaw, 1930-1940).txt`, line 15

*Builds on:* CATALOGUE S1; TECHNOLOGY own_words; GM-19; VS-22.

**How it works** *(ours)*. Putting experience into words (spoken or written) reduces emotional intensity and helps the mind make sense of it. Speaking to a 'You' adds the felt presence of a listener, which increases honesty and comfort. *(R20 Pennebaker, R09 Lieberman et al., R21 Luhrmann & Morgain)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Find a place where no one will hear you, or speak inside. | 5s |
| 2 | Begin with 'You'. Speak to the One who hears, the way you'd talk to a close friend. | 8s |
| 3 | Say what's going on. Plain words. Your own language. | 40s |
| 4 | Say what you want to leave behind. | 30s |
| 5 | Say what you long for. | 30s |
| 6 | If words stop, wait. Or say 'I don't know what to say.' That's speech too. | 20s |
| 7 | End with one sentence of thanks, or one request for today. | 15s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 2: Begin: 'Master of the world'. Speak to G-d the way you'd talk to a close friend. - Step 7: End with thanks to Him, and one request for today.

**Check-in** *(one tap)*: "How was talking?"

| Tap | Then | The guide says |
| --- | --- | --- |
| It flowed | `deepen` → T40 The quiet after | Rest a moment in the quiet after. |
| Words wouldn't come | `switch` → T29 One word only | Then one word only. That's enough. |
| I cried | `close` | Tears are not sadness here. Let's close gently and pick one act. |
| It went somewhere dark | `stop` | Thank you. Let's pause and talk about it together, plainly. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Waiting for tears to prove it worked.* Rebbe Nachman: watching for tears is itself a stray thought.
- *Endless complaint that circles.* End with thanks and one request (step 7).

**Not for** *(contraindications)*. Safe for most. For grief floods or trauma, keep company close; for someone in danger, a person, not a practice.

**Body.** Alone if possible, walking outside or seated. Eyes open or closed. Hands free. Speak aloud softly, or inside. Breath left alone.

**In daily life.** A walk with five minutes of talking. Or one sentence to 'You' at each transition.

## T29 · One word only

*Opens: ST07 The heart answers · Level: First session (safe for anyone on day one) · Dose: 1-3 minutes.*

**Toward the true self** *(ours)*. When you can't say anything else, one word repeated honestly is still your voice, and it keeps the door open.

**The practice in the source** *(stated)*. Rebbe Nachman: even if one says only 'Master of the world', that too is very good; and even if it seems one speaks without heart, it is still very good.

> «ואפלו אם לא יאמר רק "רבונו של עולם", גם זה טוב מאד» (*and even if he says only 'Master of the world', that too is very good*) · Likkutei Etzot (Rebbe Nachman), `Likkutei Etzot (Bratslav, Ukraine, 1790-1810).txt`, line 341
> «אף על פי שנדמה לאדם שמדבר בלא לב, אף על פי כן גם זה טוב מאד» (*even though it seems to a person that he speaks without heart, even so this too is very good*) · Likkutei Etzot (Rebbe Nachman), `Likkutei Etzot (Bratslav, Ukraine, 1790-1810).txt`, line 343

**How it works** *(ours)*. A single repeated word gives attention a place to rest and keeps a relationship going on low days. Speaking even without feeling can lead to feeling (the mouth before the heart). *(R34 Hobson et al., R21 Luhrmann & Morgain)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | No sentences needed today. | 4s |
| 2 | Choose one word. 'Please.' Or 'Here.' Or 'You.' | 8s |
| 3 | Say it, softly, inside or aloud. | 10s |
| 4 | Again. Slower. | 15s |
| 5 | Again. Let it mean whatever it means today. | 20s |
| 6 | Even said without heart, it counts. | 10s |
| 7 | Once more, and rest. | 15s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 2: Say only: 'Ribbono shel olam', Master of the world. - Step 6: Even said without heart, it is very good before Him.

**Check-in** *(one tap)*: "How was the word?"

| Tap | Then | The guide says |
| --- | --- | --- |
| More words want to come | `switch` → T28 Your own words | Then let them come. |
| That was enough | `close` | It was. Take the word with you. |
| Empty | `close` | Rebbe Nachman says even that is very good. Done for today. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Turning the word into a mechanical mantra for calm.* It is addressed to Someone, not a sound effect.
- *Judging it as too little.* The source says it is very good.

**Not for** *(contraindications)*. None.

**Body.** Any posture. Eyes as preferred. Breath left alone.

**In daily life.** Your word at red lights, in queues, before sleep.

## T30 · The silent cry

*Opens: ST07 The heart answers, ST10 The self beneath the layers · Level: Weeks 1-2 (after a few sittings) · Dose: 2-4 minutes. Not daily; when something is too big to hold.*

**Toward the true self** *(ours)*. Some things in you are too big for words and too private for sound. The silent cry lets the whole self speak, without anyone else needing to hear.

**The practice in the source** *(stated)*. Rebbe Nachman: one can cry out in a still small voice, a very great cry, and no one will hear at all; picture the cry in thought, bring its sound into thought, until you are truly crying out silently.

> «דע, שיכולין לצעק בקול דממה דקה בצעקה גדולה מאד ולא ישמע שום אדם כלל» (*know that one can cry out in a still, small voice, a very great cry, and no one will hear at all*) · Sichot HaRan (Rebbe Nachman), `Sichot HaRan (Bratslav, Ukraine, 1803-1810).txt`, line 70
> «שיציר במחשבתו הצעקה ויכנס קול הצעקה במחשבה» (*he pictures the cry in his thought and brings the sound of the cry into thought*) · Sichot HaRan (Rebbe Nachman), `Sichot HaRan (Bratslav, Ukraine, 1803-1810).txt`, line 70

*Builds on:* CATALOGUE S2; L3 whisper-cry.

**How it works** *(ours)*. Expressing strong feeling, even only in imagination, releases pressure that suppression keeps in. Done inwardly it is safe in any setting and gives grief or longing a shape and an end. *(R20 Pennebaker, R10 Holmes & Mathews)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Something in you wants to cry out. Let it, but silently. | 6s |
| 2 | Picture the cry. Imagine the sound of it, the way people cry out. | 15s |
| 3 | Bring that sound inside your thought. Let it be as loud as it needs to be, inside. | 25s |
| 4 | No one hears. Only you, and whoever you are crying to. | 20s |
| 5 | Let it go as long as it needs. | 30s |
| 6 | Now let it quiet down by itself. | 20s |
| 7 | Feel the space after it. | 20s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 4: No one hears but G-d. He hears the still small voice.

**Check-in** *(one tap)*: "How is it after the cry?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Relief, space | `deepen` → T40 The quiet after | Rest in the space. |
| More is coming | `switch` → T28 Your own words | Let it come out in words, softly. |
| Overwhelmed | `come_up` → T42 Come down: feet, hands, the room | Let's come back to the room together. Feet, hands. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Distress feeding itself, louder and louder.* Cap it; go to T42, then T25.
- *A dramatic display.* It is silent by design.

**Not for** *(contraindications)*. Not during a panic attack or a trauma flashback. For grief floods, company first (P2-04).

**Body.** Seated or lying. Eyes closed. Hands may clench and open. Breath left alone.

**In daily life.** When you can't scream in public and want to: ten seconds of the silent cry, then one breath and back.

## ST08 · Awe, small and glad

*Hushed before something vast and near. Small, but not crushed. Light and glad at the same time.*

## T31 · The edge of knowing

*Opens: ST08 Awe, small and glad, ST09 Less in the way · Level: Later (after weeks of practice, on a steady day) · Dose: 5-10 minutes, after T18 on a steady day.*

**Toward the true self** *(ours)*. The mind is a great part of you, but not the deepest. When it reaches its edge and bows, what remains is the part of you that was never only a thinker.

**The practice in the source** *(stated)*. Bitul hasechel: after thinking as far as one can, the mind reaches what it cannot grasp and stops; the Rebbe Rashab: the end of knowing is that we do not know. It is a stop, not a blank.

> «אך אמיתי' ענין ד"ע הוא כמא' תכלית הידיעה שלא נודע» (*the truth of the higher knowing is, as it is said, the end of knowing is that we do not know*) · Hemshech Ayin Beis (the Rebbe Rashab), `Hemshech Ayin Beis (Lubavitch and Rostov, 1912-1916).txt`, line 4589

*Builds on:* TECHNOLOGY edge; FULL-DESCENT S09-S11; MAP S35, S36.

**How it works** *(ours)*. Pushing a question to its limit and then resting, rather than forcing an answer, produces a state of awe and openness. Theory calls this 'non-action': letting go of the effort to control the mental model. *(R29 Lutz, Mattout & Pagnoni, R16 Yaden et al.)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Take the line you've been holding. Go as far into it as your mind can. | 25s |
| 2 | Ask: what is the Source itself? Not what it does. What it is. | 20s |
| 3 | Notice every answer you get is too small. Let each one go: not that, not that. | 30s |
| 4 | Keep going until the mind simply can't take another step. | 25s |
| 5 | Stop there. Don't fill the space. | 30s |
| 6 | You are at the edge. Bow, inside. | 20s |
| 7 | Now come back. Name one plain thing in the room. | 8s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 2: Ask: who is G-d Himself? Not what He does. Who He is. - Step 6: You are at the edge. Bow before Him, inside.

**Check-in** *(one tap)*: "What is at the edge?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Awe, longing | `deepen` → T40 The quiet after | Rest in it, briefly. Then we come down. |
| Empty, but peaceful | `close` | Good. Come back down and take one plain act into the day. |
| Frustrated | `switch` → T18 One line, held long | Go back to holding the line. The edge comes by itself later. |
| Spacey, unreal | `come_up` → T42 Come down: feet, hands, the room | Let's come down now. Feet, hands, the room. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Blankness or dissociation taken for depth.* The edge leaves you more yourself and more able to act; check with T33.
- *Clever negations as a game.* It is a bowing, not a puzzle.

**Not for** *(contraindications)*. Not for anyone with unreality, dissociation, mania, psychosis history, or in crisis. Not before weeks of T18. Always end with T42.

**Body.** Seated, upright. Eyes closed, then open to come down. Hands resting. Breath left alone.

**In daily life.** When you hit something you can't understand today, a small bow inside instead of irritation.

## ST09 · Less in the way

*For a moment you are not holding yourself up. Nothing to defend, nothing to prove. Someone is still here, lighter, and what is true comes through.*

## T32 · Standing in the between

*Opens: ST09 Less in the way · Level: Later (after weeks of practice, on a steady day) · Dose: 3-6 minutes. Only on a steady day, after weeks.*

**Toward the true self** *(ours)*. Between one mood and the next, one thought and the next, you are not yet anything in particular. That open moment is where real change, and the root of the self, can be met.

**The practice in the source** *(stated)*. The Maggid: between egg and chicken there is a moment that is neither, which no one can pin down; that is ayin, the nothing, and every change passes through it.

> «ויש שעה שאינו לא ביצה ולא תרנגל ואין שום אדם יכול לכוין את השעה כי אז היא בחינת אי"ן» (*there is a moment when it is neither egg nor chicken, and no one can pin down that moment, for then it is ayin*) · Maggid Devarav leYaakov (the Maggid of Mezritch), `Maggid Devarav leYaakov (Mezritch, Volhynia, 1760-1780).txt`, line 82

*Builds on:* CATALOGUE E1; MAP S31 Turned over; clinic DX K03.

**How it works** *(ours)*. Noticing the gap between mental events (the end of one thought before the next) is a known contemplative skill that loosens habitual patterns. Change of a deep pattern needs a moment when the old pattern is open; this practice looks for that moment on purpose. *(R07 Lane, Ryan, Nadel & Greenberg, R29 Lutz, Mattout & Pagnoni, R05 Dahl, Lutz & Davidson)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Notice the state you're in now. Give it one word. | 10s |
| 2 | Watch it closely. It is always ending and something else is always starting. | 20s |
| 3 | Look for the moment between. After one thing, before the next. | 25s |
| 4 | You can't grab it. Just be there, in the not-yet. | 25s |
| 5 | Nothing to be in that moment. Open. | 20s |
| 6 | Now let the next thing come, whatever it is. Choose it if you can: something good. | 15s |
| 7 | Come back to the room. Name one thing you see. | 8s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 5: Open. Before G-d, who makes everything new from nothing. - Step 6: Let the next thing come from Him. Choose something good.

**Check-in** *(one tap)*: "What was the between like?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Open, fresh | `close` | Good. Use that freshness for one thing you want to change today. |
| I couldn't find it | `switch` → T04 Watch the thoughts until the head empties | That's normal. Let's just watch the thoughts for now. |
| Empty in a scary way | `come_up` → T42 Come down: feet, hands, the room | Let's come back down now. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Seeking blankness as a high.* It is a passage, not a place. Always come back with a choice (step 6).
- *Detachment from life.* PS-14: a transparent self, not a vanished one.

**Not for** *(contraindications)*. Not for anyone with dissociation, unreality, trauma history in active treatment, mania or psychosis. Never in an intensive or retreat dose. Always end with T42.

**Body.** Seated, upright. Eyes closed, then open. Hands resting. Breath left alone.

**In daily life.** At the moment a bad mood is ending, or right before you react: notice the gap, then choose.

## T33 · The afterward test

*Opens: ST09 Less in the way, ST13 Acting from it · Level: Weeks 1-2 (after a few sittings) · Dose: 2 minutes, hours later or that evening. Not during the sitting.*

**Toward the true self** *(ours)*. The true self, when touched, leaves you humbler, kinder and freer, not more impressed with yourself. The test protects the real thing from its imitation.

**The practice in the source** *(stated)*. The Mitteler Rebbe's test: false self-nullification leaves a person feeling himself from that very experience; true arousal is followed by true lowliness. The Piaseczner's question: am I truly more my own master now than before? Test at times, and only at times.

> «בא לכלל הרגשת העצמיות מזה עצמו דוקא» (*he comes to feel himself, from that very experience*) · Kuntres HaHitpa'alut (the Mitteler Rebbe), `Kuntres HaHitpa'alut (Lubavitch, 1813).txt`, line 808
> «וסימנו שאחר כך יבוא לכלל שפלות אמיתית» (*and its sign is that afterwards he comes to true lowliness*) · Kuntres HaHitpa'alut (the Mitteler Rebbe), `Kuntres HaHitpa'alut (Lubavitch, 1813).txt`, line 828
> «אם באמת מושל אני על עצמי עתה יותר מאשר לפנים» (*am I truly more my own master now than before?*) · Bnei Machshava Tova (the Piaseczner), `Bnei Machshava Tova (Piaseczno, 1917-1923).txt`, line 252

*Builds on:* CATALOGUE C6; TECHNOLOGY discern; PS-16; VS-21.

**How it works** *(ours)*. Judging an experience by its effects on behavior, not by its intensity, guards against chasing highs and against grandiosity. It is the difference between a state and a trait. *(R06 Dahl, Wilson-Mendenhall & Davidson, R17 Lindahl, Fisher, Cooper, Rosen & Britton, R18 Britton)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Think back to the sitting earlier. | 6s |
| 2 | Don't ask how strong it felt. Ask what it left. | 10s |
| 3 | Am I kinder today, even a little? | 12s |
| 4 | Am I a little more my own master: less pushed around by moods or wants? | 15s |
| 5 | Or am I a little more impressed with myself? | 12s |
| 6 | Whatever the answer, it's useful. No grade. | 6s |
| 7 | Choose one small thing to keep what was real. | 10s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 2: Don't ask how strong it felt. Ask: am I closer to G-d in how I act? - Step 7: Choose one small thing to keep what He gave.

**Check-in** *(one tap)*: "What did it leave?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Kinder, freer | `close` | That's the sign it was real. Keep going. |
| A bit proud of it | `switch` → T47 Loving the next person first | Good catch. Turn it outward: one kindness for someone. |
| Nothing changed | `close` | Change comes in drops. Keep the practice; test again in a week. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Testing constantly, every sitting.* At times, and only at times (the Piaseczner).
- *Harsh self-judgment.* No grade; just information.

**Not for** *(contraindications)*. For anxious or scrupulous people, test weekly, not daily.

**Body.** Any posture. Eyes open. Breath left alone.

**In daily life.** Once a week, the three questions. Note the answers.

## ST10 · The self beneath the layers

*Under every mood, role and verdict there is a simple self that nothing ever reached, and a will in it that you did not choose and cannot be argued out of. Here knowing yourself and knowing what gives you being turn out to be one knowing.*

## T34 · Under all your names

*Opens: ST10 The self beneath the layers, ST02 The watcher, ST09 Less in the way · Level: Weeks 1-2 (after a few sittings) · Dose: 8-12 minutes. Weeks 1-2 onward, on a steady day.*

**Toward the true self** *(ours)*. This is the direct form of the aim. Below body, feelings, thoughts, roles and history there is a plain point you are. The sources say that point and its Source are not two.

**The practice in the source** *(stated)*. The descent through the layers of the self: Chassidus says the soul itself is not its will or its pleasure but like a simple light; its innermost point is a part of the Essence; the Piaseczner: the knowledge of G-d is in the knowledge of oneself.

> «אין הנפש בבחי' מציאות דמזלא בבחי' מהות רצון או עונג רק כמו אור היולי ופשוט» (*the soul is not a will or a pleasure; it is like a simple light*) · Toras Chaim (the Mitteler Rebbe), `Toras Chaim (Lubavitch, c. 1820-1827).txt`, line 3305
> «אבל הנשמה היא חלק מן העצם» (*but the soul is a part of the essence*) · Sefer HaMaamarim (the Rebbe Rayatz), `Sefer HaMaamarim (Riga and Otwock, 1929-1933).txt`, line 1457
> «שידיעת ד׳ היא בידיעת עצמו» (*the knowledge of God is in the knowledge of oneself*) · Esh Kodesh (the Piaseczner), `Esh Kodesh (Warsaw Ghetto, 1941).txt`, line 542

*Builds on:* FULL-DESCENT S14; FULL-DESCENT S15; stage-book Stage 3; PS-12, PS-14.

**How it works** *(ours)*. Moving attention step by step from outer to inner layers of experience (body, emotion, thought, self-image) loosens identification with each one while keeping a steady sense of being present. It reconstructs the self around a deeper, stable reference point rather than dissolving it. *(R05 Dahl, Lutz & Davidson, R03 Bernstein et al., R27 Leary, Adams & Tate)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Feel your body sitting here. You have a body. Notice it, gently. | 15s |
| 2 | You notice the body, so you are a little more than the body. | 10s |
| 3 | Feel your mood right now. You have feelings. Notice them. | 15s |
| 4 | They come and go. You are still here. A little deeper than the feelings. | 12s |
| 5 | Notice your thoughts passing. You have thoughts. You are the one they pass through. | 20s |
| 6 | Your names: your job, your role, your story, what people call you. You have them. | 15s |
| 7 | Under all your names, what is left? Don't answer. Just be it. | 40s |
| 8 | Simple. Plain. Here. Untouched by anything that happened to you. | 30s |
| 9 | Stay as that, and let the body, the feelings, the names come back around it. | 20s |
| 10 | You are still yourself. Only more so. | 10s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 7: Under all your names: the point in you that is a part of G-d. Don't answer. Just be it. - Step 8: Simple. Untouched. Where you and G-d were never apart. - Step 10: You are still yourself, before Him. Only more so.

**Check-in** *(one tap)*: "What did you find under the names?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Something plain and steady | `deepen` → T40 The quiet after | Rest there, and then we'll take it into the day. |
| Close to something greater | `deepen` → T28 Your own words | Speak to it, in your own words. |
| Nothing there | `switch` → T27 The cry of one who feels nothing | That's all right. Let's start from the wish to find something. |
| Floaty, not myself | `come_up` → T42 Come down: feet, hands, the room | We go back up now. Feet, hands, your name. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Self-loss sought as the goal ('I'm not here').* PS-14: the aim is a transparent self, not a vanished one. Always end with step 9.
- *A grand identity ('I am divine, above others').* The point is in everyone equally. Close with T47.

**Not for** *(contraindications)*. Not for unreality, dissociation, trauma flooding, mania or psychosis (MAP S20). Stop at once if the person feels they are disappearing; T42.

**Body.** Seated, upright and steady. Eyes closed. Hands resting on the thighs. Breath left alone.

**In daily life.** When someone calls you by a role today (mom, boss, customer): 'that too, and under it, me'.

## T35 · The flame that leans upward

*Opens: ST10 The self beneath the layers, ST07 The heart answers · Level: Weeks 1-2 (after a few sittings) · Dose: 3-6 minutes.*

**Toward the true self** *(ours)*. Your longing is not a problem to fix. It is the most natural thing in you, the self leaning toward its source like a flame leans up.

**The practice in the source** *(stated)*. The Tanya's image of the soul: like the light of a candle that always flickers upward by its nature, to separate from the wick and cleave to its root. No source instructs gazing at a candle; it is used here as a picture.

> «כאור הנר שמתנענע תמיד למעלה בטבעו» (*like the light of a candle that always flickers upward by its nature*) · Tanya (the Alter Rebbe), Liozna text, `Tanya (Liozna, 1786-1796).txt`, line 264
> «ליפרד מהפתילה ולידבק בשרשו למעלה» (*to separate from the wick and cleave to its root above*) · Tanya (the Alter Rebbe), Liozna text, `Tanya (Liozna, 1786-1796).txt`, line 264

*Builds on:* CATALOGUE I1 (the candle, image only); MAP S41.

**How it works** *(ours)*. A simple image gives an abstract longing a shape the mind can hold, and imagery carries feeling. Recognizing longing as natural reduces the shame of feeling incomplete. *(R10 Holmes & Mathews)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Picture a small flame. A candle in a still room. | 10s |
| 2 | Watch how it moves. Always flickering up. | 15s |
| 3 | It isn't trying. Leaning up is simply what a flame is. | 12s |
| 4 | Now find the longing in you. For something more, something whole. You know it. | 20s |
| 5 | That longing is your flame. It leans up by its nature. | 15s |
| 6 | Don't push it and don't hide it. Let it lean. | 30s |
| 7 | And notice: the flame stays on its wick. It burns here, giving light. | 15s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 4: Find the longing in you for G-d. It's there, even if quiet. - Step 5: That longing is your soul. It leans toward Him by nature, like the flame toward its root.

**Check-in** *(one tap)*: "What is your flame doing?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Leaning up, alive | `deepen` → T28 Your own words | Then let it speak. |
| Small, flickering | `close` | Small flames are real flames. Keep it lit today. |
| It aches | `switch` → T30 The silent cry | Then let the ache cry out, silently. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Wanting to leave life or the body to reach 'the root'.* The flame stays on the wick and gives light here. If there is any wish to die, stop and check safety.
- *Staring at a real candle for effects.* Not the source's practice. It's a picture.

**Not for** *(contraindications)*. Not for anyone with thoughts of death or not wanting to live: the image of leaving the wick is unsafe there. Use T10, T25, and the safety protocol.

**Body.** Seated. Eyes closed (no real candle needed). Hands resting. Breath left alone.

**In daily life.** When restless longing comes today: 'the flame leaning up'. Then one act of light here.

## T36 · The child who knows its parent

*Opens: ST10 The self beneath the layers, ST05 Held · Level: Later (after weeks of practice, on a steady day) · Dose: 5-8 minutes. After weeks of practice.*

**Toward the true self** *(ours)*. Under understanding there is recognition: the plain sense that you belong to something. It doesn't need proof, and it is closer to your essence than any idea.

**The practice in the source** *(stated)*. The Rebbe Rashab: a small child does not know how its father is its father, and there is no revelation in it; it only recognizes that this is its father and is drawn after him with great longing.

> «שהרי אינו יודע איך שהוא אביו ואין בזה שום התגלות רק שהוא בהכרה שמכיר שהוא אביו ונמשך אחריו בגעגועים גדולים» (*he does not know how he is his father, and there is no revelation in it; only he recognizes that this is his father and is drawn after him with great longing*) · Hemshech Ayin Beis (the Rebbe Rashab), `Hemshech Ayin Beis (Lubavitch and Rostov, 1912-1916).txt`, line 3667

*Builds on:* FULL-DESCENT S12; stage-book Stage 11; MAP S60.

**How it works** *(ours)*. Some knowing is pre-verbal and relational, like a child's recognition of a parent. Contacting it bypasses argument and draws on the attachment system, which is felt as safety and belonging. *(R31 Granqvist, Mikulincer & Shaver, R21 Luhrmann & Morgain)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Think of a very small child seeing its parent come into the room. | 10s |
| 2 | The child can't explain anything. It just knows: that's mine. And reaches. | 15s |
| 3 | No proof, no reasons. Recognition. | 10s |
| 4 | Under all your questions and doubts, is there something in you that just recognizes? | 25s |
| 5 | Not an idea. A pull. 'That's where I'm from.' | 25s |
| 6 | Let yourself be the child who reaches. | 30s |
| 7 | You don't need to understand. Only to reach. | 20s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 4: Under all your questions, is there something in you that simply knows G-d is your Father? - Step 5: Not an idea. A pull. 'Father.' - Step 6: Let yourself be the child reaching for Him.

**Check-in** *(one tap)*: "Is there recognition?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Yes, something plain | `deepen` → T28 Your own words | Say the one word a child would say. |
| Faint | `close` | Faint is real. Carry the word 'mine' through the day. |
| My own parent makes this hard | `switch` → T22 Borrow a love you already have | Then not a parent. A love you already have. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Forced childishness or regression.* This is plain recognition, not acting like a child.
- *Certainty used to dismiss others' questions.* Recognition is quiet; it doesn't argue.

**Not for** *(contraindications)*. Not for people with a harmful parent relationship unless they choose another image. Not as a first practice.

**Body.** Seated. Eyes closed. Hands open. Breath left alone.

**In daily life.** A single word through the day, the child's word: 'mine' (or 'Father').

## ST11 · The world see-through

*The world comes back real, solid and other, and not on its own. The cup is a cup, and it is given. Plain, no drama.*

## T37 · Seeing the garment

*Opens: ST11 The world see-through · Level: Weeks 1-2 (after a few sittings) · Dose: 3-5 minutes sitting; then seconds at a time through the day.*

**Toward the true self** *(ours)*. The same eye that sees things as dead and separate can learn to see them as alive from inside. Changing how you look changes who is looking.

**The practice in the source** *(stated)*. Histaklus: the Tanya asks a person to train himself, like a craftsman training his hands, to see all he sees, heaven and earth, as the outer garments of the King; the Baal Shem Tov: whatever he sees, let him remember the Holy One.

> «אשר כל מה שרואה בעיניו, השמים והארץ ומלואה, הכל הם לבושים החיצונים של המלך» (*that all he sees with his eyes, heaven and earth and all in them, are the outer garments of the King*) · Tanya (the Alter Rebbe), Liozna text, `Tanya (Liozna, 1786-1796).txt`, line 622
> «וכל מה שרואה יזכור בהקב"ה» (*and whatever he sees, let him remember the Holy One*) · Tzava'at HaRivash (the Baal Shem Tov, as collected), `Tzava'at HaRivash (Medzhibozh and Mezritch, c. 1740-1770).txt`, line 40

*Builds on:* CATALOGUE I4; TECHNOLOGY garment_look; stage-book Stage 5.

**How it works** *(ours)*. Attention can be trained to a new default way of seeing. Repeated, brief re-framing of ordinary sights (a tree, a face, a cup) builds a habit of perception, much like a craftsman's trained hands. *(R06 Dahl, Wilson-Mendenhall & Davidson, R14 Lally et al., R21 Luhrmann & Morgain)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Open your eyes and let them rest on one thing: a tree, a cup, the sky through a window. | 8s |
| 2 | See it plainly. Color, edges, light. | 15s |
| 3 | Now ask: what is keeping it here? It didn't make itself. | 12s |
| 4 | Look at it as a garment. Something is inside it, giving it being. | 20s |
| 5 | Don't imagine anything extra. The thing stays exactly as it is. | 10s |
| 6 | Only the way you see it changes. Solid, and lit from inside. | 25s |
| 7 | Let your eyes move to one more thing, and see it the same way. | 25s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 4: Look at it as a garment of the King. G-d is inside it, giving it life. - Step 7: Let your eyes move to one more thing. It too is His garment.

**Check-in** *(one tap)*: "How does the thing look now?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Alive, as if lit | `deepen` → T13 Walking it down to one thing | Let's walk that all the way down into one thing. |
| The same | `again_smaller` | That's normal at first. Pick a living thing, and just ask: what keeps it here? |
| Less real, dreamlike | `come_up` → T42 Come down: feet, hands, the room | It should feel more real, not less. Let's touch something solid. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Seeing the world as an illusion or a dream.* Things are real and given; the garment is real cloth. Ground with T42.
- *Staring hard for a special visual effect.* Nothing extra is to be seen. Only a different knowing.

**Not for** *(contraindications)*. Not for people with unreality or detachment (MAP S20). The Baal Shem Tov: not a license to gaze at what one should not.

**Body.** Seated or walking. Eyes open, soft. Hands relaxed. Breath left alone.

**In daily life.** Choose one recurring sight (the view from a window, a face at home). Each time you see it: 'garment'.

## T38 · The meal received

*Opens: ST11 The world see-through, ST13 Acting from it · Level: First session (safe for anyone on day one) · Dose: The first three bites of any meal.*

**Toward the true self** *(ours)*. Pleasure is not the enemy of the deeper self. Taken as a gift, it brings you back to the root you share with the thing you are enjoying.

**The practice in the source** *(stated)*. The Baal Shem Tov: at eating, let his thought be to draw out the life in the food and raise it; he sits here eating and he is in the world of pleasure.

> «וכן בעת האכילה יהי' מחשבתו להוציא החיות שבה להעלותה למעלה» (*at eating let his thought be to draw out the life in it and raise it up*) · Tzava'at HaRivash (the Baal Shem Tov, as collected), `Tzava'at HaRivash (Medzhibozh and Mezritch, c. 1740-1770).txt`, line 260
> «והוא יושב כאן ואוכל והוא בעולם התענוג» (*he sits here eating and he is in the world of pleasure*) · Tzava'at HaRivash (the Baal Shem Tov, as collected), `Tzava'at HaRivash (Medzhibozh and Mezritch, c. 1740-1770).txt`, line 168

*Builds on:* CATALOGUE A2; clinic BODY B02; animal-soul M35.

**How it works** *(ours)*. Slow, attentive eating anchors attention in the senses and in the present. Framing the taste as received turns an automatic act into gratitude, and it grounds the body, which makes it safe for people who drift. *(R13 Emmons & McCullough, R32 Birtwell et al.)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Before the first bite, look at the food. | 5s |
| 2 | Everything it took to reach you: sun, rain, hands. It came to you. | 10s |
| 3 | Take one bite, slowly. | 8s |
| 4 | Notice the taste. Where does it come from? You didn't make it. | 12s |
| 5 | Enjoy it fully. Enjoying it is part of receiving it. | 10s |
| 6 | Think: I will use the strength from this for something good today. | 8s |
| 7 | Eat the next bites the same way. | 0s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 2: It came to you from G-d, through sun, rain and hands. Say the blessing slowly. - Step 4: Notice the taste. Its sweetness is the life G-d put in it. - Step 6: Think: I will serve Him with the strength from this.

**Check-in** *(one tap)*: "Did the meal feel different?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Yes, more present | `close` | Good. Use the strength for one good thing today. |
| I rushed it | `again_smaller` | Just the first bite tomorrow. One bite, slowly. |
| Food is hard for me | `stop` | Thank you for saying so. We'll leave food out of this practice. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Using 'elevation' as a reason to overeat.* The Baal Shem Tov's first rule limits eating to health.
- *Eating slowly while worrying the whole time.* One bite, fully. That's the practice.

**Not for** *(contraindications)*. Not for anyone with an eating disorder or a difficult relationship with food: drop the food practice entirely (clinic BODY guards). No fasting, diets or amounts.

**Body.** Seated at a table. Eyes on the food. Hands slow. Breath left alone.

**In daily life.** Every meal: the first bite slowly, received. One good use of the strength.

## T39 · Where the beauty comes from

*Opens: ST11 The world see-through, ST07 The heart answers · Level: Later (after weeks of practice, on a steady day) · Dose: 1-3 minutes, when beauty moves you (music, a landscape, a face in a painting).*

**Toward the true self** *(ours)*. Every pull toward beauty is, at its root, the self longing for its own source. Followed back, it does not leave you emptier; it brings you home.

**The practice in the source** *(stated)*. The Baal Shem Tov: when you see beauty, ask where it comes from; a body without life has no such beauty, so the root of beauty is a divine power; why be drawn after the part? The Tanya limits raising stray desires to the very advanced, so this is used only for beauty and pleasure that meet you, not for struggling with forbidden pulls.

> «נמצא שורש היופי הוא כח אלוקי ולמה לי למשוך אחר החלק» (*so the root of beauty is a divine power; why should I be drawn after the part?*) · Tzava'at HaRivash (the Baal Shem Tov, as collected), `Tzava'at HaRivash (Medzhibozh and Mezritch, c. 1740-1770).txt`, line 179
> «וגם, אל יהי שוטה לעסוק בהעלאת המדות של המחשבה זרה, כנודע, כי לא נאמרו דברים ההם אלא לצדיקים» (*and let him not be a fool and busy himself with raising the traits of the foreign thought, for those things were said only for tzaddikim*) · Tanya (the Alter Rebbe), Liozna text, `Tanya (Liozna, 1786-1796).txt`, line 373

*Builds on:* CATALOGUE I4, E3; animal-soul M11, M53.

**How it works** *(ours)*. The energy of a strong attraction is not suppressed but redirected toward its deeper object. Reappraising a pull ('what am I really wanting?') keeps the energy while changing its aim. *(R08 Webb, Miles & Sheeran, R19 Wang, Hagger & Chatzisarantis)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Something beautiful has caught you. Let it. | 6s |
| 2 | Ask: where does this beauty come from? | 10s |
| 3 | Not from the paint or the notes or the matter. Something shines through them. | 15s |
| 4 | That shining is what you're really drawn to. | 12s |
| 5 | Follow the pull back to where it comes from, not just to this one thing. | 20s |
| 6 | Rest in that wider beauty for a moment. | 20s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 3: It is G-d's power shining through the matter. That is the root of all beauty. - Step 5: Follow the pull back to Him, the root of all beauty, not only this part.

**Check-in** *(one tap)*: "Where did the pull go?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Wider, warmer | `deepen` → T23 Love answers love | Then let the warmth answer, as love answers love. |
| Still stuck on the thing | `switch` → T20 Come back without a fight | Then don't wrestle with it. Turn back to something plain. |
| I feel guilty | `switch` → T25 Gather the good points | No guilt here. Let's find what's good. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Using it to justify lingering on what pulls you somewhere harmful.* Not for forbidden or compulsive pulls. There, turn away and do something (animal-soul M50).
- *Turning beauty into a cold idea.* Enjoy first, then ask.

**Not for** *(contraindications)*. Not for compulsions, addictions or struggles with desire: for those the sources say turn away and act, do not engage (Tanya 28). Not for beginners.

**Body.** Wherever the beauty is. Eyes open. Breath left alone.

**In daily life.** At a sunset or a piece of music: one question, 'where does this come from?'

## ST12 · The quiet after

*The reaching settles. You come back down into the room carrying it, and nothing is lost. The coming back is the deeper half.*

## T40 · The quiet after

*Opens: ST12 The quiet after, ST09 Less in the way · Level: First session (safe for anyone on day one) · Dose: 1-3 minutes, after any technique that opened something.*

**Toward the true self** *(ours)*. After the work, you don't need to do anything to be yourself. Resting in that is the self without effort.

**The practice in the source** *(stated)*. Lingering (hisakvus): the Piaseczner says the time of stopping is also service; the Mitteler Rebbe says that at the true level a person does not notice whether he is moved, for the movement happens by itself.

> «גם הזמן הזה של החדלה עבודה היא» (*this time of stopping is also service*) · Derekh HaMelekh (the Piaseczner), `Derekh HaMelekh (Warsaw, 1931).txt`, line 224
> «שאז לא ירגיש כלל אם הוא מתפעל, כי אין הכוונה להתפעל רק שההתפעלות מאליו נעשית» (*he does not notice at all whether he is moved, for the aim is not to be moved; the movement happens by itself*) · Kuntres HaHitpa'alut (the Mitteler Rebbe), `Kuntres HaHitpa'alut (Lubavitch, 1813).txt`, line 219
> «דקליטת ההשגה באה ע"י ההתעכבות» (*the grasp is absorbed by lingering*) · Sefer HaMaamarim (the Rebbe Rayatz), `Sefer HaMaamarim (Riga and Otwock, 1929-1933).txt`, line 435

*Builds on:* TECHNOLOGY hold; PS-10, PS-11; MAP S32.

**How it works** *(ours)*. A pause after an emotional or insight experience lets it settle and be stored; rushing on loses it. Not checking 'how am I doing' during the quiet avoids pulling the self back into monitoring. *(R07 Lane, Ryan, Nadel & Greenberg, R29 Lutz, Mattout & Pagnoni, R27 Leary, Adams & Tate)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Stop doing anything now. | 5s |
| 2 | Don't look for a feeling. Don't check how it went. | 8s |
| 3 | Just stay. | 30s |
| 4 | If a thought comes, let it pass. Stay. | 30s |
| 5 | Let what happened sink in on its own. | 30s |
| 6 | When you're ready, notice the room again. | 5s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 3: Just stay, before Him. - Step 5: Let what He gave sink in on its own.

**Check-in** *(one tap)*: "What's here now?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Peace, settled | `close` | Good. Let's put it into words and then into one act. |
| Light, a bit floaty | `come_up` → T41 Transparent, not gone | Let's bring it back into you, so you can carry it. |
| Restless to move on | `close` | Fine. Let's carry it into the day. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Checking and rating the experience.* The source forbids examining the uplift in the moment. Later (T33).
- *Drifting into sleepiness or blankness.* Keep it short; T41 to come back.

**Not for** *(contraindications)*. Short for anyone prone to dissociation. Never extended into long silent periods for beginners.

**Body.** Whatever posture the last technique used. Eyes closed. Still hands. Breath left alone.

**In daily life.** After a good conversation or a moment of beauty: ten seconds of not moving on.

## T41 · Transparent, not gone

*Opens: ST12 The quiet after, ST09 Less in the way · Level: Weeks 1-2 (after a few sittings) · Dose: 1-2 minutes, after every deep technique (T31, T34, T32, T40).*

**Toward the true self** *(ours)*. The goal was never to disappear. It is to be fully yourself and not in the way, like clear glass: solid, real, letting light through.

**The practice in the source** *(stated)*. The Rebbe Rashab: the vessel that can receive is a self that exists and yields; what has no 'something' at all is not a vessel. The Baal Shem Tov: come down several times a day. So after any high moment the self returns, to receive it.

> «והכלי לקבל הוא דוקא בחי' ביטול היש, שהרי מה שבבחי' ביטול במציאות לגמרי שאינו בבחי' יש כלל הרי אינו בבחי' כלי» (*the vessel to receive is specifically bittul hayesh, for what is wholly bittul bimetzius, not a 'something' at all, is not a vessel*) · Hemshech Ayin Beis (the Rebbe Rashab), `Hemshech Ayin Beis (Lubavitch and Rostov, 1912-1916).txt`, line 3509
> «וצריך לירד למטה כמה פעמים ביום לנוח עצמו ממחשבתו מעט» (*and he must come down several times a day to rest a little from his thought*) · Tzava'at HaRivash (the Baal Shem Tov, as collected), `Tzava'at HaRivash (Medzhibozh and Mezritch, c. 1740-1770).txt`, line 281

*Builds on:* PS-14; PS-15; MAP S48 Returning; FULL-DESCENT S28, S30.

**How it works** *(ours)*. States become traits only when the person can integrate them into ordinary self-experience. Re-inhabiting the body and one's own name after a deep moment protects against depersonalization and lets the insight be carried. *(R23 Deane, Miller & Wilkinson, R06 Dahl, Wilson-Mendenhall & Davidson, R18 Britton)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Let's bring what happened back into you. | 4s |
| 2 | Feel your body again, from the feet up. | 12s |
| 3 | Say your name to yourself. | 6s |
| 4 | You're here. Fully you. Nothing was lost. | 8s |
| 5 | Now imagine yourself as clear glass. Solid, real, and the light passes through. | 15s |
| 6 | Whatever you touched just now, it can go through you into your day. | 12s |
| 7 | Open your eyes. | 3s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 5: Clear glass before G-d: solid, yourself, and His light passes through. - Step 6: What He gave you can go through you into your day.

**Check-in** *(one tap)*: "How are you, back here?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Whole, and lighter | `close` | Then let's choose one act to carry it. |
| Still floaty | `come_up` → T42 Come down: feet, hands, the room | Let's do the full grounding. Stand up and walk a little. |
| Sad to come back | `close` | Coming back is the deeper half. The day is where it lives. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Welcoming 'I'm not here' as a spiritual summit.* Unreality is a stop sign (PS-14). T42.
- *Holding on to the high and skipping the return.* Running without returning does not last.

**Not for** *(contraindications)*. None; it is a safety technique.

**Body.** Seated, feet flat. Eyes opening. Hands on thighs. Breath left alone.

**In daily life.** After prayer, music, a moving moment: feet, name, 'clear glass', then go.

## T42 · Come down: feet, hands, the room

*Opens: ST12 The quiet after, ST01 Here · Level: First session (safe for anyone on day one) · Dose: 1-2 minutes. Whenever a session ends, and at once on any stop sign.*

**Toward the true self** *(ours)*. The true self is not found by leaving the body or the world. Coming back down to them is coming back to oneself.

**The practice in the source** *(stated)*. The Baal Shem Tov: one must come down several times a day to rest a little from the thought. The guide's rule for unreality: the answer is always down, to the plain day, the hands and a person.

> «וצריך לירד למטה כמה פעמים ביום לנוח עצמו ממחשבתו מעט» (*and he must come down several times a day to rest a little from his thought*) · Tzava'at HaRivash (the Baal Shem Tov, as collected), `Tzava'at HaRivash (Medzhibozh and Mezritch, c. 1740-1770).txt`, line 281

*Builds on:* MAP S20; PS-14; PS-15; VS-25; manual part5.

**How it works** *(ours)*. Concrete senses (pressure of feet, texture under the hands, naming objects) pull attention out of inner loops and restore a sense of control. It lowers arousal and ends any loosening of the sense of self. *(R23 Deane, Miller & Wilkinson, R17 Lindahl, Fisher, Cooper, Rosen & Britton, R18 Britton)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Let's come back into the room. | 3s |
| 2 | Press your feet into the floor. Feel the floor push back. | 8s |
| 3 | Put your hands on your knees or the table. Feel what they touch. | 8s |
| 4 | Open your eyes. Look around and name three things you see, out loud or inside. | 15s |
| 5 | Name one sound you hear. | 8s |
| 6 | Say your own name to yourself, and where you are. | 6s |
| 7 | You are here. Solid. That's the right place to be. | 4s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 7: You are here, in your body, in the place G-d put you. That is the right place to be.

**Check-in** *(one tap)*: "How are you now?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Back and steady | `close` | Good. Let's name what happened and pick one thing to do. |
| Still a bit unreal or shaky | `again_smaller` | Let's do it again. Stand up, walk a few steps, drink some water. |
| Upset or frightened | `stop` | Thank you for telling me. No more meditation today. Is someone near you? Let's talk plainly. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Treating this as failure ('I couldn't go deep').* Say: coming down is half the practice; the sources require it.
- *Rushing back into deep work after grounding.* No more depth that day after a stop sign.

**Not for** *(contraindications)*. None. If unreality, panic or disorientation lasts after this, or keeps returning, it is a reason to see a professional.

**Body.** Sitting or standing. Eyes open. Hands on something solid. Breath not mentioned; if anything, a sip of water.

**In daily life.** After any long screen session or intense hour: feet, hands, three things in the room.

## ST13 · Acting from it

*It goes into the hand: one act, done plainly, for its own sake. The person in front of you is real, and held by the same One.*

## T43 · The deed done slowly

*Opens: ST13 Acting from it · Level: First session (safe for anyone on day one) · Dose: 1 minute to choose; the act itself today.*

**Toward the true self** *(ours)*. What you do shows who you are more than what you feel. One act done from the deepest place makes that place real in the world, and in you.

**The practice in the source** *(stated)*. Bringing it down into a deed: the Mitteler Rebbe says light has no hold except in a vessel, and arousal that does not reach action is like a flame flying in the air with no endurance; the Piaseczner: when a good thought comes, do a good act with it and so clothe it.

> «הרי זה כשלהבת הפורח באויר שאין לו קיום» (*it is like a flame flying in the air, which has no endurance*) · Kuntres HaHitpa'alut (the Mitteler Rebbe), `Kuntres HaHitpa'alut (Lubavitch, 1813).txt`, line 778
> «שכשבא איזה הרהור טוב באיש יעשה בו מצוה או ילמוד בו, ובזה ילבישו בקדושה» (*when a good thought comes, let him do a mitzvah with it or learn with it, and so clothe it in holiness*) · Hakhsharat HaAvrekhim (the Piaseczner), `Hakhsharat HaAvrekhim (Warsaw, 1930-1940).txt`, line 270
> «טובה פעולה אחת מאלף אנחות» (*better one act than a thousand sighs*) · Hayom Yom (the Rebbe, from the Rebbeim), `Hayom-Yom — Hebrew text.txt`, line 192

*Builds on:* CATALOGUE A5; TECHNOLOGY act; VS-01; PS-22; animal-soul M32.

**How it works** *(ours)*. Tying an inner state to a specific, small action (when and where) greatly raises the chance it happens and builds a habit. Acting on a value is also what turns a passing state into a lasting trait. *(R15 Gollwitzer & Sheeran, R14 Lally et al., R06 Dahl, Wilson-Mendenhall & Davidson)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Before we finish: one small act, today, that comes from what you felt. | 6s |
| 2 | Not a plan. One thing. A call, a kindness, a coin given, a task done well. | 12s |
| 3 | Choose it now. When and where will you do it? | 15s |
| 4 | See yourself doing it, slowly, with your whole attention. | 15s |
| 5 | When you do it, do it a little slower than usual, as if it matters. It does. | 6s |
| 6 | That act is where this sitting lives. | 4s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 2: One mitzvah or one kindness. A coin to charity, a call, a blessing said slowly. - Step 6: That act is how G-d's light gets a home down here.

**Check-in** *(one tap)*: "Did you choose an act?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Yes | `close` | Good. Tell me later if you did it, if you like. |
| I picked something big | `again_smaller` | Make it smaller. Something you'll surely do today. |
| Nothing comes to mind | `close` | Then this: do the next ordinary task slowly and well. That counts. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *A big vow made in the glow.* The source: small and real, not a vow.
- *Doing it for credit.* Do one quietly, unseen.

**Not for** *(contraindications)*. None. For depressed or exhausted people, the act may be tiny (drinking water, opening a window).

**Body.** Seated, eyes open, hands ready. Then the act itself: done with the hands slowly.

**In daily life.** Every sitting ends here. The act is the bridge to the day.

## T44 · The carried line

*Opens: ST13 Acting from it, ST04 Given right now · Level: First session (safe for anyone on day one) · Dose: Seconds, many times a day. Same line for a week.*

**Toward the true self** *(ours)*. A line you return to all day keeps you connected to the self you met in the sitting, so the day doesn't take you away from it.

**The practice in the source** *(stated)*. The Tanya: after contemplating at length, come back to it even with a light contemplation, at any time and any hour; the Baal Shem Tov: even going about your business, keep 'I have set God before me always'.

> «כשיחזור ויתבונן בזה אפילו בהתבוננות קלה, בכל עת ובכל שעה» (*when he comes back and contemplates it, even with a light contemplation, at any time and any hour*) · Tanya (the Alter Rebbe), Chabad Library text, `Tanya — Hebrew text.txt`, line 639
> «אפי' כשהולך לעסקיו יקיים שויתי ה' לנגדו תמיד» (*even when he goes about his business let him keep 'I have set God before me always'*) · Keter Shem Tov (the Baal Shem Tov), `Keter Shem Tov (Medzhibozh, Ukraine, c. 1740-1760).txt`, line 257

*Builds on:* TECHNOLOGY carry, chazarah; animal-soul M42; integration MAP I7.

**How it works** *(ours)*. Brief, repeated retrieval of a meaningful phrase, tied to everyday cues, carries a state across the day and builds it into habit. This is how short practice becomes lasting change. *(R14 Lally et al., R15 Gollwitzer & Sheeran, R32 Birtwell et al.)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Let's pick one line to carry today. Say it in your own words. | 10s |
| 2 | For example: 'Given, now.' Or: 'Here before what is greatest.' | 6s |
| 3 | Make it short enough to say in one breath. | 6s |
| 4 | Choose a reminder: every time you open a door, or pick up your phone. | 10s |
| 5 | At that moment, say the line once, inside. Two seconds. No more. | 6s |
| 6 | Try it now, once. | 6s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 2: For example: 'Only You.' Or: 'You give me being, now.' - Step 5: At that moment, say the line once, to Him.

**Check-in** *(one tap)*: "Your line for today?"

| Tap | Then | The guide says |
| --- | --- | --- |
| I have it | `close` | Carry it. Same line all week; it gets deeper. |
| Not sure which | `close` | Take this one: 'given, now'. |
| I'll forget | `again_smaller` | Then one reminder only: the first sip of every drink. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Saying it automatically with no meaning.* The Piaseczner: a device used every day stops working. Change the wording slightly each week.
- *Making it a long recitation.* Two seconds.

**Not for** *(contraindications)*. None.

**Body.** Anywhere. Eyes open. No change of posture needed.

**In daily life.** It is the daily form. Pair with T43's act.

## T45 · The declared intention

*Opens: ST13 Acting from it · Level: Weeks 1-2 (after a few sittings) · Dose: 5 seconds before chosen acts.*

**Toward the true self** *(ours)*. Saying why you are doing something, truthfully, joins your hands to your deepest aim. Over time the gap between what you do and who you are gets smaller.

**The practice in the source** *(stated)*. R. Elimelech of Lizhensk: before everything, say 'I am doing this for the unity of the Holy One and His Presence', from the heart, and take care to speak truth in your heart; in time a great light is felt in this saying.

> «ובהמשך הזמן ירגיש הארה גדולה באמירה זו» (*and in the course of time he will feel a great illumination in this saying*) · Noam Elimelekh, Tzetl Katan (R. Elimelech of Lizhensk), `Noam Elimelekh (Lizhensk, Galicia, 1786).txt`, line 26
> «אך יזהר שיהיה דובר באמת בלבבו» (*but let him take care to speak truth in his heart*) · Noam Elimelekh, Tzetl Katan (R. Elimelech of Lizhensk), `Noam Elimelekh (Lizhensk, Galicia, 1786).txt`, line 25

*Builds on:* CATALOGUE A4; integration MAP I6.

**How it works** *(ours)*. Stating an intention before an action links the action to a value and makes it more deliberate. Repeated over months, a sincere formula becomes a cue that reliably brings up the state. *(R15 Gollwitzer & Sheeran, R34 Hobson et al.)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Before you begin what you're about to do, stop for a moment. | 4s |
| 2 | Say inside why you're doing it, at the deepest level you can honestly say. | 10s |
| 3 | For example: 'I'm doing this so that there is more good and more oneness in the world.' | 8s |
| 4 | Only say what is true for you right now. Not more. | 6s |
| 5 | Now begin. | 2s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 3: For example: 'I'm doing this for the unity of G-d, to give Him pleasure.'

**Check-in** *(one tap)*: "Was it true when you said it?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Yes | `close` | Then it will grow. Keep saying it before this act. |
| Partly | `close` | Say only the true part. That's the rule. |
| It felt empty | `again_smaller` | Say something smaller and true: 'I want to do this well.' |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Grand words with no truth behind them.* The source's warning: speak truth in your heart; don't fool yourself.
- *Saying it to look holy.* Inside only.

**Not for** *(contraindications)*. None.

**Body.** Wherever the act is. Hands still for a second before beginning.

**In daily life.** Choose two daily acts (work start, a meal) and say it before them.

## T46 · The evening look-back that ends in good

*Opens: ST13 Acting from it, ST05 Held · Level: Weeks 1-2 (after a few sittings) · Dose: 3-5 minutes, before the bedtime return (T17). Never longer.*

**Toward the true self** *(ours)*. Looking honestly at the day, and ending in good, separates what you did from who you are. You can own a mistake without becoming it.

**The practice in the source** *(stated)*. Cheshbon hanefesh: the Tanya has a person make an accounting of the day's thoughts, words and deeds; the Baal Shem Tov's great rule is to guard against sadness as much as possible; Rebbe Nachman: seek the good points still in you.

> «לעשות חשבון עם נפשו, מכל המחשבות והדיבורים והמעשים שחלפו ועברו» (*to make an accounting with his soul of all the thoughts, words and deeds that have passed*) · Tanya (the Alter Rebbe), Liozna text, `Tanya (Liozna, 1786-1796).txt`, line 395
> «וזהו כלל גדול בעבודת הבורא ית' שיזהר מעצבות כל מה שיוכל» (*this is a great rule in serving the Creator: to guard against sadness as much as he can*) · Tzava'at HaRivash (the Baal Shem Tov, as collected), `Tzava'at HaRivash (Medzhibozh and Mezritch, c. 1740-1770).txt`, line 87
> «לחפש הרוח טובה, דהינו הנקדות טובות שיש בו עדין» (*to seek the good spirit, that is, the good points still in him*) · Likkutei Etzot (Rebbe Nachman), `Likkutei Etzot (Bratslav, Ukraine, 1790-1810).txt`, line 333

*Builds on:* CATALOGUE C5; TECHNOLOGY cheshbon; animal-soul M30; clinic BODY B12.

**How it works** *(ours)*. Brief structured reflection with a fixed end in the positive supports learning from the day without rumination. Limiting it in time and closing with gratitude prevents the spiral that open-ended self-review causes. *(R13 Emmons & McCullough, R08 Webb, Miles & Sheeran, R11 Weng et al.)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Look back over today, quickly, like flipping pages. | 10s |
| 2 | One thing you thought, said or did that you'd want to do differently. | 15s |
| 3 | Name it plainly. Decide one small repair, if there is one. | 15s |
| 4 | Now set it down. It's done for today. | 6s |
| 5 | Find one good thing you did. And another. | 25s |
| 6 | Those are you too. End the day on them. | 10s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 4: Set it down before G-d. He forgives abundantly. - Step 6: Those are your soul's good points. Thank Him and end the day on them.

**Check-in** *(one tap)*: "How did the look-back end?"

| Tap | Then | The guide says |
| --- | --- | --- |
| On something good | `switch` → T17 The bedtime return | Now hand yourself back for the night. |
| Stuck on the bad thing | `switch` → T25 Gather the good points | Let's gather good points until you're lighter. |
| Low, heavy | `stop` | Then no accounting tonight. One good thing only, and sleep. Tomorrow we'll talk. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Long, harsh self-trial that ends in sadness.* The Besht: sadness is the enemy. Five minutes, end in good.
- *Skipping the honest part.* One thing to do differently, plainly.

**Not for** *(contraindications)*. Not for someone low, crushed or depressed: only 'one good thing' (MAP S04 blocks self-examination). Not for scrupulous people without a fixed time limit.

**Body.** Seated on the bed or lying. Eyes closed. Hands open. Breath left alone.

**In daily life.** It is the daily evening form, followed by T17.

## T47 · Loving the next person first

*Opens: ST13 Acting from it, ST07 The heart answers · Level: First session (safe for anyone on day one) · Dose: 1-3 minutes before people; 5 minutes as a sitting.*

**Toward the true self** *(ours)*. The deepest point in you and the deepest point in the person in front of you come from the same place. Finding yours makes you able to see theirs.

**The practice in the source** *(stated)*. Before prayer the Arizal takes on 'love your fellow as yourself'; the Baal Shem Tov: before speaking to anyone, first bind yourself in thought to the Creator, and know that your fellow's soul is also bound to Him.

> «צריך שיקבל עליו מצות ואהבת לרעך כמוך ויכוין לאהוב כל אחד מבני ישראל כנפשו» (*he must take upon himself the mitzvah 'love your fellow as yourself' and intend to love every Jew as himself*) · Sha'ar HaKavanot (the Arizal), `Sha'ar HaKavanot.txt`, line 38
> «וכשאומר לב"א יקשור עצמו במחשבה תחילה בבורא ית' ונשמת חבירו ג"כ בבורא מקושרת» (*when he speaks to people, let him first bind himself in thought to the Creator; his fellow's soul is also bound to the Creator*) · Tzava'at HaRivash (the Baal Shem Tov, as collected), `Tzava'at HaRivash (Medzhibozh and Mezritch, c. 1740-1770).txt`, line 192

*Builds on:* CATALOGUE S4; VS-12; P2-01 stage 3.

**How it works** *(ours)*. Compassion and loving-kindness training increase helping behavior and change how the brain responds to others' suffering. Remembering a shared source reduces us-versus-them thinking and softens anger. *(R11 Weng et al., R12 Fredrickson et al.)*

**The live script** *(ours; seconds of silence after each line)*.

| # | The guide says | Silence |
| --- | --- | --- |
| 1 | Bring to mind a person you'll see today. Maybe someone difficult. | 10s |
| 2 | First, come back to yourself: the plain point under your names. | 15s |
| 3 | Now see that the same kind of point is in them. Under their names, their moods, what annoys you. | 20s |
| 4 | Both of you, given being right now, from the same Source. | 15s |
| 5 | Wish them one good thing, simply. | 15s |
| 6 | When you meet them, remember for one second: same Source. | 6s |

**For someone who believes in G-d** *(ours; only the lines that change)*.

- Step 2: First, bind yourself in thought to G-d. - Step 4: Their soul is bound to G-d too, as yours is. Love them as yourself. - Step 6: When you meet them, remember: their soul is His too.

**Check-in** *(one tap)*: "How do you see them now?"

| Tap | Then | The guide says |
| --- | --- | --- |
| Softer | `close` | Good. One kind word or act for them today. |
| Still angry | `switch` → T05 Look at it, not in it | Let's look at the anger itself for a moment, not at them. |
| They hurt me badly | `stop` | Then this isn't the practice for them now. Your safety comes first. Let's talk. |
| I need to stop | `stop` → T42 | Good. We stop here. Feel your feet on the floor. Look at one thing in the room and name it. |

- *Using 'same source' to excuse harm or stay in danger.* Love never means accepting abuse. Safety first.
- *A warm thought that changes nothing in how you treat them.* One kind act (T43).

**Not for** *(contraindications)*. Not to be aimed at someone who harmed or endangers the person (abuse, assault): the guide never asks that. Start with easy people.

**Body.** Seated, or just before meeting someone. Eyes closed for the practice, open before meeting. Breath left alone.

**In daily life.** Before any meeting or call: one second, 'same Source'.

## 6. The science, with links

*Ours: our reading, in plain words, of what contemplative science says about how techniques like these work and where they go wrong. It supports the design; it does not prove any Chassidic claim, and no study has measured these techniques as practised (SCIENCE.md, 'Checked and not used'). References R01-R10 and R14-R34 are from `meditation-technology/SCIENCE.md`; R11-R13 were added here and confirmed against Crossref on 2026-10-01.*

- **State and trait.** A state is how you are during a sitting; a trait is how you are on an ordinary Tuesday. States become traits through repetition, cues in daily life and action, not through intensity (R06, R14, R32). So the library keeps sittings short, ties each to a carried line (T44) and an act (T43), and repeats the same line for a week.
- **Attention training.** Focused practice trains a cycle: the mind wanders, you notice, you return, you stay (R01, R02). The return is the skill, and fighting thoughts makes them come back stronger (R19). T04, T05 and T20 are built on this.
- **The self and the default mode.** When the mind is idle it drifts into self-talk about past and future, and that drifting is linked to unhappiness (R26). Practice quiets this network (R04). Some methods take the self-model apart, others rebuild it around a deeper reference point (R05). Chassidus mostly rebuilds: it fills the mind with one large meaning until the small self gives way. The library follows it (T18, T34) and keeps the 'taking apart' methods gentle and short (T04, T32).
- **Insight and reappraisal.** Knowing a thing is not the same as feeling it (R28). Change comes when the meaning of something shifts, not only the facts known about it (R08). Breadth, length and depth in hisbonenus are a precise recipe for this kind of elaboration (T13, T18).
- **Memory reconsolidation.** An emotional memory or belief becomes open to change when it is recalled while something new and contradicting is felt at the same time (R07). 'I hold everything up' meets 'given, now' (T10); 'I am my mistakes' meets the good points (T25); a mood is traced to its hour and seen afresh (T06).
- **Naming and words.** Putting feelings into words lowers their intensity (R09, R25), and speaking or writing about what matters helps people make sense of it (R20). Hisbodedus (T28, T29) is this, addressed to a listener.
- **Imagery and presence.** Pictures move emotion more than words (R10). Prayer that trains the inner senses makes a presence feel real (R21), and a felt, safe, greater presence works like a secure attachment (R31). T15, T08 and T36 use this, and drop the picture when it has done its work.
- **Compassion and gratitude.** Compassion and loving-kindness training increase care for others and build lasting positive resources (R11, R12). Counting what is given lifts well-being (R13). T22, T23, T25, T47, T11, T14 and T38 use this.
- **Awe and self-transcendence.** Moments of awe and of the self feeling smaller and joined to something larger are common, have known shapes, and usually leave people more connected (R16, R27). The edge (T31) and the quiet after (T40) live here.
- **Ritual, song and the threshold.** A short fixed act at a fixed moment changes how what follows is felt (R34). Music moves emotion and reward strongly (R22). Spiritual framing can add to the effect of meditation for those it fits (R33).
- **Dose and response.** More is not always better: many practice effects follow an inverted U (R18). Short daily practice with informal moments through the day is what predicts benefit (R32).
- **The known risks.** Difficult experiences in meditation are not rare (R24, R30). Britton's team catalogued them across perception, emotion, body and the sense of self, including fear, unreality and re-living trauma (R17). Risk rises with intensity, long retreats, solitude and practice that only takes the self apart. The same loosening of the self that feels like peace in one person can feel like horror in another (R23). Hence rules 2, 3, 6 and 8 in section 2.

| id | Reference | Link |
| --- | --- | --- |
| R01 | Lutz, Slagter, Dunne & Davidson (2008). Attention regulation and monitoring in meditation. Trends in Cognitive Sciences 12(4). | https://doi.org/10.1016/j.tics.2008.01.005 |
| R02 | Hasenkamp et al. (2012). Mind wandering and attention during focused meditation. NeuroImage 59(1). | https://doi.org/10.1016/j.neuroimage.2011.07.008 |
| R03 | Bernstein et al. (2015). Decentering and related constructs. Perspectives on Psychological Science 10(5). | https://doi.org/10.1177/1745691615594577 |
| R04 | Brewer et al. (2011). Meditation experience and default mode network activity. PNAS 108(50). | https://doi.org/10.1073/pnas.1112029108 |
| R05 | Dahl, Lutz & Davidson (2015). Reconstructing and deconstructing the self. Trends in Cognitive Sciences 19(9). | https://doi.org/10.1016/j.tics.2015.07.001 |
| R06 | Dahl, Wilson-Mendenhall & Davidson (2020). The plasticity of well-being. PNAS 117(51). | https://doi.org/10.1073/pnas.2014859117 |
| R07 | Lane, Ryan, Nadel & Greenberg (2015). Memory reconsolidation, emotional arousal, and the process of change in psychotherapy. Behavioral and Brain Sciences 38. | https://doi.org/10.1017/S0140525X14000041 |
| R08 | Webb, Miles & Sheeran (2012). Dealing with feeling: strategies from the process model of emotion regulation. Psychological Bulletin 138(4). | https://doi.org/10.1037/a0027600 |
| R09 | Lieberman et al. (2007). Putting feelings into words: affect labeling. Psychological Science 18(5). | https://doi.org/10.1111/j.1467-9280.2007.01916.x |
| R10 | Holmes & Mathews (2010). Mental imagery in emotion and emotional disorders. Clinical Psychology Review 30(3). | https://doi.org/10.1016/j.cpr.2010.01.001 |
| R11 | Weng et al. (2013). Compassion training alters altruism and neural responses to suffering. Psychological Science 24(7). | https://doi.org/10.1177/0956797612469537 |
| R12 | Fredrickson et al. (2008). Open hearts build lives: positive emotions induced through loving-kindness meditation. JPSP 95(5). | https://doi.org/10.1037/a0013262 |
| R13 | Emmons & McCullough (2003). Counting blessings versus burdens. JPSP 84(2). | https://doi.org/10.1037/0022-3514.84.2.377 |
| R14 | Lally et al. (2010). How are habits formed. European Journal of Social Psychology 40(6). | https://doi.org/10.1002/ejsp.674 |
| R15 | Gollwitzer & Sheeran (2006). Implementation intentions and goal achievement. Advances in Experimental Social Psychology 38. | https://doi.org/10.1016/S0065-2601(06)38002-1 |
| R16 | Yaden et al. (2017). The varieties of self-transcendent experience. Review of General Psychology 21(2). | https://doi.org/10.1037/gpr0000102 |
| R17 | Lindahl, Fisher, Cooper, Rosen & Britton (2017). The varieties of contemplative experience. PLoS ONE 12(5). | https://doi.org/10.1371/journal.pone.0176239 |
| R18 | Britton (2019). Can mindfulness be too much of a good thing? Current Opinion in Psychology 28. | https://doi.org/10.1016/j.copsyc.2018.12.011 |
| R19 | Wang, Hagger & Chatzisarantis (2020). Ironic effects of thought suppression: a meta-analysis. Perspectives on Psychological Science 15(3). | https://doi.org/10.1177/1745691619898795 |
| R20 | Pennebaker (1997). Writing about emotional experiences as a therapeutic process. Psychological Science 8(3). | https://doi.org/10.1111/j.1467-9280.1997.tb00403.x |
| R21 | Luhrmann & Morgain (2012). Prayer as inner sense cultivation. Ethos 40(4). | https://doi.org/10.1111/j.1548-1352.2012.01266.x |
| R22 | Salimpoor et al. (2011). Dopamine release during anticipation and experience of peak emotion to music. Nature Neuroscience 14(2). | https://doi.org/10.1038/nn.2726 |
| R23 | Deane, Miller & Wilkinson (2020). Losing ourselves: active inference, depersonalization, and meditation. Frontiers in Psychology 11. | https://doi.org/10.3389/fpsyg.2020.539726 |
| R24 | Schlosser et al. (2019). Unpleasant meditation-related experiences in regular meditators. PLoS ONE 14(5). | https://doi.org/10.1371/journal.pone.0216643 |
| R25 | Kircanski, Lieberman & Craske (2012). Feelings into words: contributions of language to exposure therapy. Psychological Science 23(10). | https://doi.org/10.1177/0956797612443830 |
| R26 | Killingsworth & Gilbert (2010). A wandering mind is an unhappy mind. Science 330. | https://doi.org/10.1126/science.1192439 |
| R27 | Leary, Adams & Tate (2006). Hypo-egoic self-regulation. Journal of Personality 74(6). | https://doi.org/10.1111/j.1467-6494.2006.00429.x |
| R28 | Teasdale (1993). Emotion and two kinds of meaning. Behaviour Research and Therapy 31(4). | https://doi.org/10.1016/0005-7967(93)90092-9 |
| R29 | Lutz, Mattout & Pagnoni (2019). The epistemic and pragmatic value of non-action. Current Opinion in Psychology 28. | https://doi.org/10.1016/j.copsyc.2018.12.019 |
| R30 | Goldberg, Lam, Britton & Davidson (2022). Prevalence of meditation-related adverse effects. Psychotherapy Research 32(3). | https://doi.org/10.1080/10503307.2021.1933646 |
| R31 | Granqvist, Mikulincer & Shaver (2010). Religion as attachment. Personality and Social Psychology Review 14(1). | https://doi.org/10.1177/1088868309348618 |
| R32 | Birtwell et al. (2019). Formal and informal mindfulness practice and wellbeing. Mindfulness 10(1). | https://doi.org/10.1007/s12671-018-0951-y |
| R33 | Wachholtz & Pargament (2005). Is spirituality a critical ingredient of meditation? Journal of Behavioral Medicine 28(4). | https://doi.org/10.1007/s10865-005-9008-5 |
| R34 | Hobson et al. (2018). The psychology of rituals. Personality and Social Psychology Review 22(3). | https://doi.org/10.1177/1088868317734944 |

## 7. Whose is what

- **The sources'** (stated): each technique's root practice as the source describes it, and the 91 Hebrew lines, each re-verified at the line given. Where a source limits a practice, the limit is kept: raising stray desires is for the very advanced only (Tanya 28, T39); the Shema's lengthening is in thought, not sound (SAH 61:7, T09); no candle-gazing (T35 is an image); no breathing technique (T11).
- **Ours**: turning each practice into a universal technique; the true-self framing; which techniques open which of the framework's thirteen states; every scripted line in both versions and every silence; the check-ins, the six actions and every adapt rule; doses; counterfeit fixes; contraindications; body notes; daily forms; the start table and the session shapes; the science section. Two widenings are ours and marked: the love of the fellow (T47) is stated in the source about every Jew and is offered here toward every person; the moment of silence (T02) is the Rebbe's for every child, Jewish or not, so its universal form is his.
- **Not yet tested.** No script here has been used with real people. The silences are first guesses; the check-in options should be tuned from live use.

## Files

- `transformation/TECHNIQUES.md` (this file) and `transformation/techniques.json` (the same 47 techniques as an array: id, name, aim, level, toward_the_true_self, source with verified quotes and full file paths, how_it_works, science with links, dose, script, script_believer, checkin with options, adapt, counterfeit, contraindications, body, daily_life, marks).
