"""The families of the release: which research documents belong together, in what order, under which area.

A family is one result: its principal document first, then the companion documents that carry it (range readings,
slices, source books). Each member is (shelf, title): `title` is the document's title as the shelf gives it, or
"*" for every remaining document on that shelf. Briefs (titles starting "Brief:") go to `briefs/`, not here.
"""

AREAS = {
    "I": "The Unity Index",
    "II": "Line-by-line readings: the Chabad works",
    "III": "Line-by-line readings: the sources Chassidus stands on",
    "IV": "Contemplation",
    "V": "The person: soul, mind and healing",
    "VI": "Saying it plainly",
}

# Documents left out of the release, and why. They stay in the research; they are build notes for the guide,
# not findings about Chassidus.
LEFT_OUT = {
    "Research-conversation": "voice drafts and simulated chats used to tune the guide",
    "Research-product": "the owner's product direction",
    "Research-ai-stages": "a roadmap for where software can help at each stage of a sitting",
    ("Research-core", "The guide layer: the rungs of the unity"): "instructions for the guide",
    ("Research-core", "REBUILD: every conversation is one movement"): "instructions for the guide",
}

C = "Research-core"

FAMILIES = [
    # ---- I. The Unity Index ----------------------------------------------------------------------------
    dict(area="I", title="The Chassidus Unity Index: Chassidus is one point", members=[
        (C, "Chassidus Unity Index"),
        (C, "The spine of the Chassidus Unity Index"),
        (C, "Subjects of Chassidus — for the Unity Index"),
        (C, "Eight sources on the unity of God: what they say together"),
    ]),
    dict(area="I", title="197 subjects in 16 clusters, each shown as a face of the one idea", members=[
        ("Research-subjects", "*"),
    ]),
    dict(area="I", title="220 works, each read for how it carries the unity", members=[
        ("Research-works", "*"),
    ]),
    dict(area="I", title="The meditation behind every face and every subject", members=[
        (C, "The meditation behind each face"),
        ("Research-meditations", "The meditation behind every subject"),
        ("Research-meditations", "*"),
    ]),
    dict(area="I", title="One process: knowing the unity is meditating on it", members=[
        (C, "One process: knowing the unity is meditating on it"),
    ]),

    # ---- II. Chabad works, line by line ------------------------------------------------------------------
    dict(area="II", title="The Tanya, line by line", members=[
        (C, "The Tanya, line by line: one idea"),
        ("Research-tanya", "*"),
    ]),
    dict(area="II", title="The Mitteler Rebbe's Gate of Unity, line by line", members=[
        (C, "The Gate of Unity, line by line: one idea in every detail"),
        ("Research-gate-of-unity", "*"),
    ]),
    dict(area="II", title="Imrei Binah: the Shema as the place where the one idea is made", members=[
        (C, "Imrei Binah, line by line: the Shema as the place where the one idea is made"),
        ("Research-imrei-binah", "*"),
    ]),
    dict(area="II", title="Kuntres HaHitpa'alut: the real arousal and its counterfeits", members=[
        (C, "Kuntres HaHitpa'alut, line by line: the real arousal and its counterfeits"),
        ("Research-kuntres-hahitpaalut", "*"),
    ]),
    dict(area="II", title="The Rebbe Rashab on prayer: Kuntres HaTefillah and Kuntres HaAvodah", members=[
        (C, "Kuntres HaTefillah, line by line: prayer as the place where knowing the unity becomes real"),
        (C, "Kuntres HaAvodah, line by line: prayer as the place where the unity is felt"),
        ("Research-kuntres-hatefillah", "*"),
        ("Research-kuntres-haavodah", "*"),
    ]),
    dict(area="II", title="Hemshech Samach Vav: the Essence below, through the will that has no reason", members=[
        (C, "Hemshech Samach Vav, line by line: the Essence below, through the will that has no reason"),
        ("Research-samach-vav", "*"),
    ]),
    dict(area="II", title="Hemshech Ayin Beis: the Essence that hides in order to shine", members=[
        (C, "Hemshech Ayin Beis, line by line: the Essence that hides in order to shine, and the one who knows it"),
        ("Research-ayin-beis", "*"),
    ]),
    dict(area="II", title="R. Aharon of Strashelye's Sha'arei HaYichud VeEmunah", members=[
        (C, "Sha'arei HaYichud VeEmunah, line by line: one idea"),
        ("Research-shaarei-hayichud", "*"),
    ]),
    dict(area="II", title="Sefer HaArachim Chabad, volume 9: the entries on the unity", members=[
        ("Research-sefer-haarachim", "*"),
    ]),
    dict(area="II", title="Darkei HaChassidus: how the unity becomes a life", members=[
        (C, "Darkei HaChassidus: how the unity becomes a life"),
        ("Research-darkei-hachassidus", "*"),
    ]),

    # ---- III. The sources Chassidus stands on --------------------------------------------------------------
    dict(area="III", title="The Rambam: one G-d, known by negation, loved by knowing", members=[
        (C, "The Rambam: one G-d, known by negation, loved by knowing, served all day"),
        ("Research-rambam", "*"),
    ]),
    dict(area="III", title="The Kuzari: the G-d of Abraham, known by taste", members=[
        (C, "The Kuzari: the G-d of Abraham, known by taste and served in joy"),
        ("Research-kuzari", "*"),
    ]),
    dict(area="III", title="The Zohar, volumes I and II", members=[
        ("Research-zohar", "The Zohar on Bereshit (volume I): overview"),
        ("Research-zohar", "The Zohar on Shemot (volume II): overview"),
        ("Research-zohar", "Zohar, the Hakdamah (export lines 1-260)"),
        ("Research-zohar", "Zohar, Bereshit I (export lines 261-610)"),
        ("Research-zohar", "Zohar, Bereshit II (export lines 611-931)"),
        ("Research-zohar", "Zohar, Bereshit III (export lines 932-1190)"),
        ("Research-zohar", "Zohar, Noach (export lines 1191-1578)"),
        ("Research-zohar", "Zohar, Lech Lecha (export lines 1579-2054)"),
        ("Research-zohar", "Zohar, Vayera (export lines 2055-2567)"),
        ("Research-zohar", "Zohar, Chayei Sara (export lines 2568-2837)"),
        ("Research-zohar", "Zohar, Toldot (export lines 2838-3045)"),
        ("Research-zohar", "Zohar, Vayetzei (export lines 3046-3441)"),
        ("Research-zohar", "Zohar, Vayishlach (export lines 3442-3719)"),
        ("Research-zohar", "Zohar, Vayeshev (export lines 3720-4004)"),
        ("Research-zohar", "Zohar, Miketz (export lines 4005-4273)"),
        ("Research-zohar", "Zohar, Vayigash (export lines 4274-4408)"),
        ("Research-zohar", "Zohar, Vayechi I (export lines 4409-4706)"),
        ("Research-zohar", "Zohar, Vayechi II (export lines 4707-5268)"),
        ("Research-zohar", "Zohar, Addenda to Volume I (export lines 5269-5659)"),
        ("Research-zohar", "Zohar on Shemot: the Shekhinah goes into exile with them"),
        ("Research-zohar", "Zohar on Vaera and Bo: the voice without its word, and the One without form"),
        ("Research-zohar", "Zohar on Beshalach: the sea, the song, and bread from heaven day by day"),
        ("Research-zohar", "Zohar on Yitro: the hidden trace, the faces of a person, and the voice at Sinai"),
        ("Research-zohar", "Zohar on Mishpatim: the Old Man's journey, the maiden in the palace, and the kiss"),
        ("Research-zohar", "Zohar on Terumah, first half: the order of prayer, the Shema, the kiss, and the soul after death"),
        ("Research-zohar", "Zohar on Terumah, second half: the table, the menorah, the gate of tears, and \"all is one\""),
        ("Research-zohar", "Zohar: Sifra DiTzniuta, Tetzaveh and Ki Tisa: the hidden One, light out of darkness, and the son in exile"),
        ("Research-zohar", "Zohar on Vayakhel: the path of prayer, Shabbat's added soul, and the Shema to Ein Sof"),
        ("Research-zohar", "Zohar on Pekudei, first half: the counted and the hidden, the work that finishes itself, and Ein Sof beyond will"),
        ("Research-zohar", "Zohar on Pekudei, second half: the Heikhalot, the palaces of prayer and their shadows"),
        ("Research-zohar", "Zohar, Addenda to Volume II"),
    ]),
    dict(area="III", title="The Zohar, volume III: the One made whole below", members=[
        ("Research-zohar", "The Zohar on Vayikra, Bamidbar and Devarim, line by line: the One made whole below, and the Lamp that is all its lights"),
        ("Research-zohar", "Zohar, volume 3, part *"),
    ]),
    dict(area="III", title="The Tikkunei Zohar and the Zohar Chadash", members=[
        ("Research-zohar", "Zohar, part 4: the Tikkunei Zohar and the Zohar Chadash"),
        ("Research-zohar", "Tikkunei Zohar*"),
        ("Research-zohar", "Zohar Chadash*"),
    ]),
    dict(area="III", title="R. Meir ibn Gabbai: the service is a need on high", members=[
        (C, "R. Meir ibn Gabbai: the service is a need on high"),
        ("Research-ibn-gabbai", "*"),
    ]),
    dict(area="III", title="The Ramak: one Cause, ten garments, and a person who walks like his Maker", members=[
        (C, "The Ramak: one Cause, ten garments, and a person who walks like his Maker"),
        ("Research-ramak", "*"),
    ]),
    dict(area="III", title="The Maharal: the One who is not a number", members=[
        (C, "The Maharal: the One who is not a number, a world that is one because He is One, and a person who cleaves"),
        ("Research-maharal", "*"),
    ]),
    dict(area="III", title="The Shelah: nothing but His existence, renewed each moment", members=[
        (C, "The Shelah: nothing but His existence, renewed each moment, and a day built to live it"),
        ("Research-shelah", "*"),
    ]),
    dict(area="III", title="The Piaseczner Rebbe: the inner meditative world", members=[
        (C, "The Piaseczner Rebbe: the inner meditative world"),
        ("Research-piaseczno", "*"),
    ]),

    # ---- IV. Contemplation ---------------------------------------------------------------------------------
    dict(area="IV", title="The classic works read as contemplation", members=[
        ("Research-meditative", "The Tanya, Likkutei Amarim: a meditative reading"),
        ("Research-meditative", "The Tanya, Shaar HaYichud to the end: a meditative reading"),
        ("Research-meditative", "The Gate of Unity: a meditative reading"),
        ("Research-meditative", "Imrei Binah: a meditative reading"),
        ("Research-meditative", "Kuntres HaHitpa'alut: a meditative reading"),
        ("Research-meditative", "*"),
    ]),
    dict(area="IV", title="The map of consciousness and meditation in Chassidus", members=[
        ("Research-consciousness-map", "*"),
    ]),
    dict(area="IV", title="Sitting with the One: a meditation manual", members=[
        ("Research-manual", "Sitting with the One: a meditation manual"),
        ("Research-manual", "*"),
    ]),
    dict(area="IV", title="How Jewish meditation works: techniques, method and mechanism", members=[
        ("Research-meditation-technology", "Meditative techniques in Chassidus and the Kabbalah it draws on: a catalogue"),
        ("Research-meditation-technology", "*"),
    ]),
    dict(area="IV", title="The Tanya as a book of consciousness", members=[
        ("Research-tanya-consciousness", "*"),
        ("Research-tanya-meditation", "*"),
    ]),
    dict(area="IV", title="The Tanya, reimagined", members=[
        ("Research-tanya-reimagined", "*"),
    ]),
    dict(area="IV", title="The full depth: reading the Rebbeim through", members=[
        ("Research-depths", "The full depth — digest of the readings"),
        ("Research-depths", "FULL DESCENT: the whole depth, station by station"),
        ("Research-depths", "*"),
    ]),
    dict(area="IV", title="Lights, vessels, and the path of prophecy", members=[
        ("Research-lights-and-vessels", "ON: Ontology. What the unity is, at its deepest"),
        ("Research-lights-and-vessels", "*"),
    ]),
    dict(area="IV", title="The inner world of Achdus Hashem", members=[
        ("Research-inner-world", "The inner world of Achdus Hashem: a map, and the conversation as a Chassidic prayer"),
        ("Research-inner-world", "*"),
    ]),
    dict(area="IV", title="How Chassidus reasons about the unity", members=[
        ("Research-reasoning", "One framework for thinking about the unity of G-d"),
        ("Research-reasoning", "*"),
    ]),

    # ---- V. The person ----------------------------------------------------------------------------------------
    dict(area="V", title="The animal soul: how a G-dly idea reaches it", members=[
        ("Research-animal-soul", "How Chassidus brings a G-dly idea to the animal soul: the merged catalogue"),
        ("Research-animal-soul", "*"),
    ]),
    dict(area="V", title="Being held", members=[
        ("Research-being-held", "Being held: the psychology"),
        ("Research-being-held", "*"),
    ]),
    dict(area="V", title="The Chassidic clinic: how a mashpia reads and treats a person", members=[
        ("Research-clinic", "DX: the diagnostic framework. How a mashpia reads a person"),
        ("Research-clinic", "*"),
    ]),
    dict(area="V", title="The psychological parallel to hisbonenus", members=[
        ("Research-psychology", "*"),
    ]),
    dict(area="V", title="The medicine map: the Chabad library read for everyday problems", members=[
        ("Research-medicine-map", "The Medicine Map · Tier A"),
        ("Research-medicine-map", "The Chabad Library as Medicine"),
        ("Research-medicine-map", "*"),
    ]),
    dict(area="V", title="The integration map: how the unity becomes a person's nature", members=[
        ("Research-integration", "*"),
    ]),
    dict(area="V", title="Transformation: a framework and forty-seven ways in", members=[
        ("Research-transformation", "The transformation framework"),
        ("Research-transformation", "*"),
        ("Research-transformations", "*"),
    ]),
    dict(area="V", title="How a conversation creates change", members=[
        ("Research-translation-layer", "How a conversation creates change"),
        ("Research-translation-layer", "The mechanism map: how each Chassidic process of change works on a person"),
        ("Research-translation-layer", "Safety and contraindications of the translation layer"),
        ("Research-translation-layer", "*"),
    ]),

    # ---- VI. Saying it plainly -----------------------------------------------------------------------------------
    dict(area="VI", title="The mashal: how the Rebbeim make an analogy, and new ones for today", members=[
        ("Research-meshalim", "The laws of the mashal"),
        ("Research-meshalim", "METHOD: how the Rebbeim make a mashal, and how to make a new one"),
        ("Research-meshalim", "*"),
    ]),
    dict(area="VI", title="The teacher: how Chassidus is imparted", members=[
        ("Research-teacher", "The teacher's craft: how Chassidus is imparted"),
        ("Research-teacher", "*"),
    ]),
    dict(area="VI", title="The universal translation: the unity of G-d for anyone", members=[
        ("Research-universal", "The universal translation: the unity of G-d for anyone, anywhere"),
        ("Research-universal", "*"),
        ("Research-universal-framework", "*"),
    ]),
    dict(area="VI", title="The ladder from zero", members=[
        ("Research-ontology", "*"),
        ("Research-stage-book", "*"),
    ]),
]

# One paragraph per family, in plain words: what the result shows. Shown in CONTENTS.md and OVERVIEW.md.
SUMMARIES = {
    "The Chassidus Unity Index: Chassidus is one point":
        "Shows that all of Chassidus is one point, as the Rebbe said of it in 1965: the Essence of G-d, present in "
        "everything, so that \"there is nothing besides Him\" holds even in the lowest place. The index tests that "
        "claim against the whole library. It names the 12 recurring forms (\"faces\") the one idea takes, the 14 moves "
        "by which the sources tie any subject back to it, and files 197 subjects and 220 works under them, with "
        "2,275 Hebrew citations checked at their lines. It marks where a tie is the text's own (*stated*) and where it "
        "is ours (*reading*), keeps nine disagreements between the Rebbeim open, and says where the claim is thin.",
    "197 subjects in 16 clusters, each shown as a face of the one idea":
        "Takes 197 subjects of Chassidus, from tzimtzum and the sefiros to food, money, Shabbos and death, and shows "
        "for each one how the sources themselves make it a way of saying the one idea. Each subject gets a one-line "
        "statement, the steps of its derivation, what each Rebbe says about it, the disagreements, and checked "
        "passages. Where the tie is weak it is marked thin, not forced.",
    "220 works, each read for how it carries the unity":
        "Reads every work in the library, Chabad and the wider Chassidic world, for one thing: how it carries the "
        "unity of G-d. Each entry says what the work is, counts its unity terms per 10,000 words, names the faces "
        "it is built on, and quotes checked passages. The counts show what is distinctively Chabad (the dwelling "
        "below appears at about eighteen times the rate of other schools) and what all schools share.",
    "The meditation behind every face and every subject":
        "Shows that each face and each of the 197 subjects is also a meditation: a movement of the mind, one line "
        "to hold, what opens inside, and where the mind reaches its edge. Built on the Tanya's rule that knowing "
        "(da'at) means binding the mind to a truth until it is as real as something seen.",
    "One process: knowing the unity is meditating on it":
        "Argues, from the sources, that knowing \"there is nothing but Him\" and meditating on it are one process, "
        "not two. Each rung of the unity is known only by a matching depth of contemplation and self-giving (bitul), "
        "each wakes a deeper layer of the soul, and at the bottom, where the mind stops, the heart's simple will is "
        "already one with Him. Then it comes back down, into the body and the day.",

    "The Tanya, line by line":
        "Reads every line of the Tanya (1,639 lines with text) and asks each one how it expresses the unity of G-d. Finds that the Tanya "
        "is not five books on five subjects but one idea said from every side: more than half the lines say it "
        "outright, and more than eight in ten say it or build toward it. Lines with no tie are marked \"none\".",
    "The Mitteler Rebbe's Gate of Unity, line by line":
        "Reads the Mitteler Rebbe's Shaar HaYichud line by line. Where the Tanya says the one idea from every side, "
        "this book walks it down rung by rung, from G-d's first will to the last blade of grass, and shows each rung "
        "one with its source. A person's work is to know this detail by detail until it lives.",
    "Imrei Binah: the Shema as the place where the one idea is made":
        "Reads the Mitteler Rebbe's Imrei Binah line by line. The book takes one verse, \"Hear, O Israel\", and asks "
        "how a person saying it makes the unity happen. Shows how each range builds that one idea.",
    "Kuntres HaHitpa'alut: the real arousal and its counterfeits":
        "Reads the Mitteler Rebbe's tract on arousal in prayer line by line. It is a field guide: what real arousal "
        "is, what it is mistaken for, and the signs that tell them apart, all unpacking one rule, that arousal be "
        "\"only Godly arousal, and not the arousal of the life of flesh\".",
    "The Rebbe Rashab on prayer: Kuntres HaTefillah and Kuntres HaAvodah":
        "Reads the Rebbe Rashab's two tracts on prayer line by line. They are not books about the unity but about "
        "how knowing it becomes real in a person: study is the preparation, and prayer is where the truth is "
        "\"returned to the heart\".",
    "Hemshech Samach Vav: the Essence below, through the will that has no reason":
        "Reads all of Hemshech Samach Vav, range by range. The series asks the sharpest question in the index, why "
        "there are worlds at all, and answers through a will that has no reason: the Essence wants a home in the "
        "lowest place. Thirteen range readings carry it, through to the editor's summaries and the indexes.",
    "Hemshech Ayin Beis: the Essence that hides in order to shine":
        "Reads all 5,750 lines of Hemshech Ayin Beis, the Rebbe Rashab's longest series. It asks how anything comes "
        "from the Essence and still shows it, and turns the usual picture around: the hiding is not the price of "
        "revelation, it is how revelation happens. Gives each movement of the series both as teaching and as "
        "contemplation.",
    "R. Aharon of Strashelye's Sha'arei HaYichud VeEmunah":
        "Reads R. Aharon of Strashelye's book on the unity line by line. It has no other subject: G-d is alone after "
        "creation just as before, and every level, screen and name in the Kabbalah is how He looks from our side.",
    "Sefer HaArachim Chabad, volume 9: the entries on the unity":
        "Reads the encyclopedia's unity entries. Finds that continuous creation is only the first rung (the lower "
        "unity), and that the unity has three rungs: lower, higher, and yachid above both.",
    "Darkei HaChassidus: how the unity becomes a life":
        "Shows that Chassidus is not only the idea that there is nothing but G-d, but a way of making that idea into "
        "a person, and that the sources call this the whole point: \"to change the nature of one's traits\". Lays "
        "out the daily loop of preparation, prayer, study and deed, from the Rebbeim and the wider Chassidic world.",

    "The Rambam: one G-d, known by negation, loved by knowing":
        "Reads the Rambam, the one medieval master every Chabad Rebbe quotes and argues with by name. His unity has "
        "three parts, and each is a practice as well as a teaching: He alone truly is; He is known by what He is "
        "not; and He is loved by knowing and served all day.",
    "The Kuzari: the G-d of Abraham, known by taste":
        "Reads the Kuzari for its teaching on the unity. G-d is known first by meeting, not by proof: the G-d of "
        "Abraham, known by taste and served in joy, against the G-d of the philosophers.",
    "The Zohar, volumes I and II":
        "Reads the Zohar on Genesis and Exodus, portion by portion, for what it says about the One and how a person "
        "comes to Him. Gives the Aramaic with its reference and line, and marks what is ours.",
    "The Zohar, volume III: the One made whole below":
        "Reads the Zohar on Leviticus, Numbers and Deuteronomy, the two Idras included. The volume keeps two things: "
        "G-d is One and does not change, and every name is only a title for His acts toward us. In the Idra's rule, "
        "the faces are \"all one\", and \"it is from our side that they differ\".",
    "The Tikkunei Zohar and the Zohar Chadash":
        "Reads the Tikkunei Zohar and the Zohar Chadash. They say the same thing from two sides: He is one, but not "
        "in number, inside every world as outside it, with no place empty of Him; and a person is made to know Him.",
    "R. Meir ibn Gabbai: the service is a need on high":
        "Reads R. Meir ibn Gabbai's three books. He wrote one idea three times: the service of G-d is a need on "
        "high. The mitzvos and prayer repair and unite the divine Glory, and that is why the world was made and "
        "why a person, not an angel, is its purpose.",
    "The Ramak: one Cause, ten garments, and a person who walks like his Maker":
        "Reads the Ramak, the great organizer of Kabbalah before the Arizal. One simple Cause beyond change; all the "
        "change we see belongs to His ten garments, the sefiros; and a person is asked to walk the way his Maker "
        "acts.",
    "The Maharal: the One who is not a number":
        "Reads the Maharal across his works. He argues from the nature of one and many, simple and composite, cause "
        "and caused, almost without Kabbalistic terms, and his teaching comes down to four sentences: He is simple, "
        "so nothing stands outside Him; the One is not a number; because He is One, the world is one; and a person "
        "reaches Him by cleaving, while twoness is the root of sin.",
    "The Shelah: nothing but His existence, renewed each moment":
        "Reads the Shelah, the bridge between Safed and the Chassidic masters. There is no existence but His, it is "
        "renewed each moment, and the book builds a whole day to live that out.",
    "The Piaseczner Rebbe: the inner meditative world":
        "Reads the Piaseczner Rebbe, who wrote most plainly about what meditation is like from inside. His method "
        "rests on one claim: the soul is already moved and already crying toward G-d, and the work is to hear it, "
        "not to make a feeling.",

    "The classic works read as contemplation":
        "Reads nine central works, in ten readings, not for what they teach but for what they do to a person who "
        "sits with them: the Tanya, the Gate of Unity, Imrei Binah, Kuntres HaHitpa'alut, the Rashab's two tracts on "
        "prayer, Samach Vav, Sha'arei HaYichud and Sefer HaArachim, each walked as one meditative journey, unit by "
        "unit.",
    "The map of consciousness and meditation in Chassidus":
        "Shows that every concept in Chassidus also names a state a person can be in, and maps them: 86 states, "
        "241 movements between them, and 8 currents that every movement serves, each tied to its sources.",
    "Sitting with the One: a meditation manual":
        "A practical manual of contemplation (hisbonenus) built from the sources: how to sit, a ladder of sittings "
        "up the rungs of the unity, programs over weeks, what happens inside, and what to do when it is hard.",
    "How Jewish meditation works: techniques, method and mechanism":
        "Catalogues 39 meditative techniques in Chassidus and the Kabbalah it draws on, in seven families, and "
        "records one absence: no breathing technique appears in these sources. Adds Abulafia's own account of how "
        "meditation works and what research can and cannot say about it.",
    "The Tanya as a book of consciousness":
        "Reads the whole Tanya as a map of the inner life: where a person really is, the states the book names, "
        "and how it moves a person from one to the next.",
    "The Tanya, reimagined":
        "Retells the whole Tanya in plain English, the way a friend would, keeping its argument and its order.",
    "The full depth: reading the Rebbeim through":
        "Fifteen readers each read one slice of the Rebbeim's writing through and brought back the depth as the "
        "texts climb it, step by step, in the texts' own arguments. Finds, among much else, that under every light of the soul there is "
        "one plain point, and that the deepest point is also the lowest and easiest to reach.",
    "Lights, vessels, and the path of prophecy":
        "Asks what the unity is at its deepest, not only how it feels, and how a person becomes a vessel for it. "
        "Finds the Tzemach Tzedek already wrote the ladder (three readings of the mitzvah to know G-d is one), and "
        "traces Chassidus as the continuation of the path of prophecy.",
    "The inner world of Achdus Hashem":
        "Maps the lived unity as a whole inner world: thirteen depths, the regions a person can be in, the doors "
        "in, its shape over weeks and years, and why prayer is the place it happens.",
    "How Chassidus reasons about the unity":
        "Writes out how a maamar thinks, not only what it concludes: it raises a real question, sorts the terms, "
        "argues, gives a picture and marks where the picture fails, climbs to where the clash goes away, and brings "
        "it down to something to do. Includes the Gate of Unity as a step-by-step proof.",

    "The animal soul: how a G-dly idea reaches it":
        "Gathers every way Chassidus describes for bringing a G-dly idea to the animal soul, the part of us that "
        "wants what is good \"for me\". Six readers each read one Rebbe's works, about 230 methods in all. All agree "
        "it can be taught, but it is a different listener.",
    "Being held":
        "Sets the teaching that everything, you included, is being given being right now, beside what psychology "
        "has measured about the feeling \"I am holding everything up\": where it comes from, what it costs, and "
        "what changes when a person stops. Marks where the bridge between the two stops.",
    "The Chassidic clinic: how a mashpia reads and treats a person":
        "Shows that the sources already diagnose. Tanya chapters 25 to 31 sort heaviness by what it is about, when "
        "it falls and whether there is life in it, and give each kind its own remedy. Builds from this a framework "
        "for reading a person and protocols for helping, the way a mashpia works.",
    "The psychological parallel to hisbonenus":
        "Lines up each step of contemplation with what psychology has measured, how strong the findings are, and "
        "where they stop, including adverse effects and counterfeits.",
    "The medicine map: the Chabad library read for everyday problems":
        "Thirty-one readers went through 22 core works and found 322 problems, 210 programs and 314 reframes, "
        "backed by 975 quoted passages (975 of 975 re-checked). Grouped into 43 conditions a person could walk in "
        "with, from worry and guilt to anger and loss, each with what the library says is really going on and what "
        "to do.",
    "The integration map: how the unity becomes a person's nature":
        "Traces, in the Rebbeim's own words, how \"there is nothing but Him\" moves from an idea a person hears to a "
        "truth that lives in the mind, the heart, the body and the day, and becomes the person's nature, in nine "
        "stages.",
    "Transformation: a framework and forty-seven ways in":
        "One road from the surface of the self down to its root, where the self and what gives it being turn out "
        "to be one, and back up into an ordinary day. Comes with forty-seven ways in, for anyone.",
    "How a conversation creates change":
        "Asks what, in one chat and across a few days, actually moves a person, from research on brief help, "
        "chat agents and the helping relationship, with the content kept Chassidus. Includes a map of how each "
        "Chassidic process of change works, and the safety rules and limits.",

    "The mashal: how the Rebbeim make an analogy, and new ones for today":
        "Sets out the laws of the mashal as R. Aharon of Strashelye wrote down his teacher's practice: a mashal is "
        "a handle on a basket, and only one who holds the teaching from its root may make one. Gathers the "
        "Rebbeim's meshalim into two source books and makes new ones for today by the same laws.",
    "The teacher: how Chassidus is imparted":
        "How Chassidus has been handed from teacher to student, moment by moment: the Baal Shem Tov's way of "
        "meeting people, the teacher's craft, and how four teachers present it.",
    "The universal translation: the unity of G-d for anyone":
        "Asks how the unity can reach anyone, of any background. Finds the Rebbe already designed the answer in the "
        "moment of silence: the content fixed, the words each person's own. Gives the core that holds for any mind "
        "and a plain-experience lexicon of the terms.",
    "The ladder from zero":
        "Starts from three things any thinking person grants (something exists, I am aware of it, things change) "
        "and climbs in sixteen small steps to the unity, using the books' own arguments, for a reader who does not "
        "yet believe in G-d.",
}

for _fam in FAMILIES:
    _fam["summary"] = SUMMARIES[_fam["title"]]
