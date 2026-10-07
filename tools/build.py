"""Build the research release from the packed research shelves.

    python3 research-release/tools/build.py            # from the OnlyOne repo root
    python3 tools/build.py PATH/TO/OnlyOne/shelf       # from this repository, given the shelves

Reads `shelf/Research-*.txt.gz`, groups the documents into the families in `families.py`, and writes:

    manuscripts/<Title-Month-Day-Year>/manuscript.md and CITATION.bib    one folder per document
    briefs/                                                                the questions the studies were given
    CONTENTS.md                                                            the manuscript map
    OVERVIEW.md                                                            the families, area by area
    manuscripts.json                                                       the same map, for programs

Then run `verification/check_quotes.py` to re-check the Hebrew quotes and write the verification catalogue.
The README is written by hand; this script only fills in its numbers (between the <!-- n:... --> marks).
"""
from __future__ import annotations

import calendar
import collections
import json
import re
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from families import AREAS, FAMILIES, LEFT_OUT  # noqa: E402
from shelfdocs import Doc, cut_words, first_added, plain, read_shelf, relink  # noqa: E402

RELEASE = HERE.parent
SHELF = Path(sys.argv[1]) if len(sys.argv) > 1 else RELEASE.parent / "shelf"   # the packed shelves (OnlyOne/shelf)
REPO_URL = "https://github.com/mashpiaR-D/chassidus"     # where the release lives
VERSION = "0.1"

ABSTRACT_FROM = ("The short answer", "What this cluster shows", "What this slice adds (one page)", "Summary",
                 "What this range is", "1. What the range is", "The shape of the range", "Read this first",
                 "What it comes to, for a person", "1. The book as one meditative journey", "What this is",
                 "In one paragraph", "At a glance", "Overview")


SKIP_LEAD = re.compile(r"(How to read|Marks\b|Method\b|Stated vs ours|Files\b|Machine)", re.I)


# ---- gathering -----------------------------------------------------------------------------------------

def left_out(doc: Doc) -> bool:
    return doc.shelf in LEFT_OUT or (doc.shelf, doc.key) in LEFT_OUT


def load() -> tuple[list[Doc], list[Doc]]:
    docs, briefs = [], []
    for path in sorted(SHELF.glob("Research-*.txt.gz")):
        shelf_docs = read_shelf(path)
        dates = collections.Counter(d.date for d in shelf_docs if d.date)
        fallback = dates.most_common(1)[0][0] if dates else first_added(path)
        for d in shelf_docs:
            d.date = d.date or fallback
            if d.key.startswith("Brief:"):
                briefs.append(d)
            elif not left_out(d):
                docs.append(d)
    return docs, briefs


def matches(doc: Doc, shelf: str, title: str) -> bool:
    if doc.shelf != shelf:
        return False
    if title == "*":
        return True
    if title.endswith("*"):
        return doc.key.startswith(title[:-1])
    return doc.key == title


def assign(docs: list[Doc]) -> list[dict]:
    taken: set[int] = set()
    fams = []
    for n, fam in enumerate(FAMILIES, 1):
        members = []
        for shelf, title in fam["members"]:
            found = [d for d in docs if id(d) not in taken and matches(d, shelf, title)]
            if not found and title != "*":
                sys.exit(f"family {n:03d}: nothing on {shelf} matches {title!r}")
            if title == "*" or title.endswith("*"):
                found.sort(key=lambda d: natural(d.title))
            for d in found:
                taken.add(id(d))
                members.append(d)
        fams.append(dict(fam, number=f"{n:03d}", docs=members))
    loose = [d for d in docs if id(d) not in taken]
    if loose:
        sys.exit("documents in no family:\n" + "\n".join(f"  {d.shelf}: {d.key}" for d in loose))
    return fams


def natural(s: str):
    """Sort 'lines 588-1167' after 'lines 1-587', and 'K02' after 'K01'."""
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", s)]


# ---- naming ------------------------------------------------------------------------------------------------

def long_date(iso: str) -> str:
    y, m, d = (int(x) for x in iso.split("-"))
    return f"{calendar.month_name[m]} {d}, {y}"


def slug(title: str, iso: str, used: set[str]) -> str:
    ascii_title = title.replace("G-d", "God").replace("'", "").replace("’", "")
    words = re.findall(r"[A-Za-z0-9]+", ascii_title)
    out = []
    for w in words:
        if len("-".join(out + [w])) > 80:
            break
        out.append(w)
    y, m, d = (int(x) for x in iso.split("-"))
    base = "-".join(out) + f"-{calendar.month_name[m]}-{d}-{y}"
    name, k = base, 2
    while name.lower() in used:
        name, k = f"{base}-{k}", k + 1
    used.add(name.lower())
    return name


# ---- abstracts ------------------------------------------------------------------------------------------------

def abstract(doc: Doc, words: int = 90) -> str:
    for want in ABSTRACT_FROM:
        for head, paras in doc.sections:
            if head.lower().startswith(want.lower()):
                text = prose(paras)
                if text:
                    return cut_words(text, words)
    for head, paras in doc.sections:
        text = prose(paras)
        if text:
            return cut_words(text, words)
    return ""


def prose(paras: list[str]) -> str:
    """The first real paragraphs: not a table, not a provenance note in italics, not a bare list of files."""
    keep = []
    for p in paras:
        s = p.strip()
        if s.startswith("|") or s.startswith("---"):
            continue
        if s.startswith("*") and s.endswith("*") and not s.startswith("**"):
            continue                      # an italic note on how the file was made
        if s.startswith("`") or SKIP_LEAD.match(plain(s)):
            continue                      # a file path, or a note on how to read the file
        t = plain(s)
        if len(t) < 60:
            continue
        keep.append(t)
        if sum(len(k.split()) for k in keep) > 60:
            break
    return " ".join(keep)


# ---- writing --------------------------------------------------------------------------------------------------

def bib_key(name: str) -> str:
    return "onlyone2026-" + re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")[:60]


def bib(doc: Doc, name: str, fam: dict, k: int) -> str:
    y, m, _ = doc.date.split("-")
    title = doc.title.replace("{", "").replace("}", "")
    return (f"@misc{{{bib_key(name)},\n"
            f"  title        = {{{{{title}}}}},\n"
            f"  author       = {{{{Only One research}}}},\n"
            f"  year         = {{{y}}},\n"
            f"  month        = {calendar.month_abbr[int(m)].lower()},\n"
            f"  note         = {{Result {fam['number']}, manuscript {k} of {len(fam['docs'])}. Version {VERSION}.}},\n"
            f"  howpublished = {{\\url{{{REPO_URL}/tree/main/manuscripts/{name}}}}}\n"
            f"}}\n")


def manuscript(doc: Doc, name: str, fam: dict, k: int) -> str:
    head = [f"# {doc.title}", ""]
    meta = [f"**Only One research** · {long_date(doc.date)} · early draft {VERSION}",
            f"Result [{fam['number']}](../../CONTENTS.md#{fam['number']}) · manuscript {k} of {len(fam['docs'])}",
            "[Cite](CITATION.bib)",
            f"[Quote check](../../verification/catalogue.md#{name.lower()})"]
    head += [" · ".join(meta), ""]
    if doc.meta.get("source") or doc.meta.get("range"):
        bits = []
        if doc.meta.get("source"):
            bits.append(f"*Text read:* {doc.meta['source']}")
        if doc.meta.get("range"):
            bits.append(f"*Range:* {doc.meta['range']}")
        head += ["  \n".join(bits), ""]
    head += ["---", ""]
    return "\n".join(head) + drop_dead_anchors(relink(doc.markdown()))


def drop_dead_anchors(md: str) -> str:
    """Some in-page links pointed at sub-headings the packing flattened away: keep their words, drop the link."""
    have = set(re.findall(r'<a (?:name|id)="([^"]+)"', md))
    for h in re.findall(r"^#+ (.*)$", md, flags=re.M):
        have.add(re.sub(r"[^\w\- ]", "", h.strip().lower()).replace(" ", "-"))
    return re.sub(r"\[([^\]]+)\]\(#([^)\s]+)\)", lambda m: m.group(0) if m.group(2) in have else m.group(1), md)


def contents(fams: list[dict], names: dict, n_docs: int) -> str:
    out = ["# Chassidus research collection", "",
           f"**{n_docs} manuscripts covering {len(fams)} result families.** An early snapshot, about one month "
           "into the work, with a lot more to come.", "",
           "[**Read the overview**](OVERVIEW.md).", "",
           "## Manuscript map", "",
           "Each result description is followed by its manuscripts and their abstracts. "
           "Titles link to the manuscripts. The first manuscript in each result is its principal one; "
           "the others carry it (readings of single ranges, slices by author, source books).", ""]
    for area, area_title in AREAS.items():
        out += [f"### {area}. {area_title}", "", "<table>", "<thead><tr><th>Result</th></tr></thead>", "<tbody>"]
        for fam in (f for f in fams if f["area"] == area):
            out += ["<tr>", "<td>", "", f'<a name="{fam["number"]}"></a>', ""]
            out += [f"**{fam['number']}. {fam['title']}.** {fam.get('summary', '').strip()} "
                    f"([Quote check](verification/catalogue.md#result-{fam['number']}))", ""]
            for k, doc in enumerate(fam["docs"], 1):
                name = names[id(doc)]
                out += [f"&emsp;[{doc.title}](manuscripts/{name}/manuscript.md)", ""]
                text = abstract(doc, 90 if k == 1 else 60)
                if text:
                    out += [text, ""]
            out += ["</td>", "</tr>"]
        out += ["</tbody>", "</table>", ""]
    return "\n".join(out)


def overview(fams: list[dict], names: dict, words: dict) -> str:
    out = [(RELEASE / "tools" / "overview_intro.md").read_text(encoding="utf-8").rstrip(), ""]
    for area, area_title in AREAS.items():
        out += [f"## {area}. {area_title}", ""]
        for fam in (f for f in fams if f["area"] == area):
            lead = fam["docs"][0]
            n, w = len(fam["docs"]), sum(words[id(d)] for d in fam["docs"])
            out += [f"### {fam['number']}. {fam['title']}", "",
                    fam.get("summary", "").strip(), "",
                    f"*{n} manuscript{'s' if n > 1 else ''}, about {w:,} words.* "
                    f"Start with [{lead.title}](manuscripts/{names[id(lead)]}/manuscript.md).", ""]
    return "\n".join(out)


def briefs_index(briefs: list[Doc], names: dict, fams: list[dict]) -> str:
    by_shelf = {}
    for fam in fams:
        for d in fam["docs"]:
            by_shelf.setdefault(d.shelf, fam)
    out = ["# Briefs", "",
           "Each study in this collection began from a written brief: what to read, the question to ask of every "
           "line, what to bring back, and the rules (above all: every Hebrew quote checked against its line in the "
           "text, nothing invented). These are the briefs that were kept with the research, unchanged.", "",
           "| Brief | Result |", "|---|---|"]
    for d in sorted(briefs, key=lambda d: natural(d.title)):
        fam = by_shelf.get(d.shelf)
        res = f"[{fam['number']}](../CONTENTS.md#{fam['number']}) {fam['title']}" if fam else "—"
        out.append(f"| [{d.title.removeprefix('Brief: ')}]({names[id(d)]}.md) | {res} |")
    return "\n".join(out) + "\n"


def fill_numbers(path: Path, numbers: dict) -> None:
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    for key, value in numbers.items():
        text = re.sub(rf"<!-- n:{key} -->.*?<!-- /n -->", f"<!-- n:{key} -->{value}<!-- /n -->", text)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    docs, briefs = load()
    fams = assign(docs)
    used: set[str] = set()
    names, words = {}, {}
    for d in [d for f in fams for d in f["docs"]]:
        names[id(d)] = slug(d.title, d.date, used)
        words[id(d)] = len(d.text().split())

    out = RELEASE / "manuscripts"
    if out.exists():
        shutil.rmtree(out)
    records = []
    for fam in fams:
        for k, d in enumerate(fam["docs"], 1):
            folder = out / names[id(d)]
            folder.mkdir(parents=True)
            (folder / "manuscript.md").write_text(manuscript(d, names[id(d)], fam, k), encoding="utf-8")
            (folder / "CITATION.bib").write_text(bib(d, names[id(d)], fam, k), encoding="utf-8")
            records.append(dict(result=fam["number"], area=fam["area"], family=fam["title"], k=k,
                                title=d.title, date=d.date, folder=names[id(d)], words=words[id(d)],
                                shelf=d.shelf, abstract=abstract(d)))

    bdir = RELEASE / "briefs"
    if bdir.exists():
        shutil.rmtree(bdir)
    bdir.mkdir()
    bused: set[str] = set()
    for d in briefs:
        names[id(d)] = slug(d.title.removeprefix("Brief: "), d.date, bused)
        (bdir / f"{names[id(d)]}.md").write_text(f"# {d.title}\n\n" + relink(d.markdown()), encoding="utf-8")
    (bdir / "README.md").write_text(briefs_index(briefs, names, fams), encoding="utf-8")

    (RELEASE / "CONTENTS.md").write_text(contents(fams, names, len(records)), encoding="utf-8")
    (RELEASE / "OVERVIEW.md").write_text(overview(fams, names, words), encoding="utf-8")
    (RELEASE / "manuscripts.json").write_text(json.dumps(records, ensure_ascii=False, indent=1), encoding="utf-8")

    total = sum(words.values())
    numbers = dict(manuscripts=len(records), families=len(fams), briefs=len(briefs),
                   words=f"{round(total, -5) / 1e6:.1f} million", areas=len(AREAS))
    fill_numbers(RELEASE / "README.md", numbers)
    fill_numbers(RELEASE / "OVERVIEW.md", numbers)
    print(f"{len(records)} manuscripts in {len(fams)} families, {len(briefs)} briefs, {total:,} words")


if __name__ == "__main__":
    main()
