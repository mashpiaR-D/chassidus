"""Re-check the Hebrew quotes in the manuscripts against a copy of the source texts.

    python3 verification/check_quotes.py --texts PATH/TO/TEXTS

TEXTS is a folder of source books, one passage a line ("reference ⟶ text"), as plain .txt or gzipped .txt.gz;
files whose names start with "Research-" are skipped (those are the research itself). The texts are not part of
this repository: they are study copies, and the release quotes them only in short passages.

The check is the one the research used, done again independently. Every run of four or more Hebrew words in a
manuscript is taken as a quote; a quote broken by an ellipsis is checked piece by piece. Quote and source are both
reduced to Hebrew letters only (no vowel points, punctuation or spaces), so a vocalised and a plain copy of the
same words match, and a changed or missing word does not. A quote is FOUND when it occurs in some line of some
book. It is NOT FOUND HERE when it does not, which most often means its book is not among the texts given.

Writes verification/catalogue.md, verification/catalogue.yaml and verification/quotes.json.
"""
from __future__ import annotations

import argparse
import bisect
import collections
import gzip
import json
import re
import unicodedata
from multiprocessing import Pool
from pathlib import Path

HERE = Path(__file__).resolve().parent
RELEASE = HERE.parent
LETTERS = re.compile(r"[^א-ת]")
WORD = r"[֑-״]+(?:[\"'׳״][֑-״]+)*[\"'׳״]?"
RUN = re.compile(rf"{WORD}(?:[ \t,.:;!?()\[\]\-–—־/]+{WORD})+")
ELLIPSIS = re.compile(r"…|\.\.\.|\(\.\.\.\)|\[\.\.\.\]")
MIN_WORDS, MIN_LETTERS = 4, 12


def letters(s: str) -> str:
    return LETTERS.sub("", unicodedata.normalize("NFKC", s))


def quotes_in(md: str) -> list[str]:
    """Runs of Hebrew long enough to be a quote. A run is cut at an ellipsis and at "/" (Hebrew references are
    written "volume / section / page"); a comma list of short terms is a list of words, not a quote."""
    out = []
    md = unicodedata.normalize("NFKC", md)
    for piece in re.split(rf"{ELLIPSIS.pattern}|/", md):
        for m in RUN.finditer(piece):
            q = m.group(0).strip(" ,.:;-–—()[]")
            if len(re.findall(WORD, q)) < MIN_WORDS or len(letters(q)) < MIN_LETTERS:
                continue
            chunks = [c for c in re.split(r"[,;]", q) if c.strip()]
            if len(chunks) >= 3 and all(len(c.split()) <= 3 for c in chunks):
                continue
            out.append(q)
    return out


# ---- the texts, as one long string of letters with a map back to book and line -------------------------------

BIG = ""
STARTS: list[int] = []
WHERE: list[tuple[int, int]] = []
BOOKS: list[str] = []


def load_texts(folder: Path) -> None:
    global BIG
    titles = {}
    if (folder / "works.json").exists():
        titles = {k: f"{v.get('title')} ({v.get('author')})"
                  for k, v in json.loads((folder / "works.json").read_text(encoding="utf-8")).items()}
    parts, pos = [], 0
    for path in sorted(list(folder.glob("*.txt")) + list(folder.glob("*.txt.gz"))):
        if path.name.startswith("Research-"):
            continue
        BOOKS.append(titles.get(path.name, path.name.removesuffix(".gz").removesuffix(".txt")))
        opener = gzip.open if path.suffix == ".gz" else open
        with opener(path, "rt", encoding="utf-8") as fh:
            for n, line in enumerate(fh, 1):
                text = line.partition(" ⟶ ")[2] if " ⟶ " in line else line
                t = letters(text)
                if not t:
                    continue
                STARTS.append(pos)
                WHERE.append((len(BOOKS) - 1, n))
                parts.append(t)
                pos += len(t) + 1
    BIG = "|".join(parts)


def find(q: str):
    i = BIG.find(letters(q))
    if i < 0:
        return None
    k = bisect.bisect_right(STARTS, i) - 1
    book, line = WHERE[k]
    return BOOKS[book], line


# ---- the run -------------------------------------------------------------------------------------------------------

# Results that read one book line by line, where that book is among the texts packed with the guide. Their
# quotes should all be found; a miss there is worth a look.
SINGLE_BOOK = {"006", "007", "008", "009", "010", "011", "012", "013", "030", "031"}


def fill(path: Path, numbers: dict) -> None:
    if path.exists():
        text = path.read_text(encoding="utf-8")
        for key, value in numbers.items():
            text = re.sub(rf"<!-- n:{key} -->.*?<!-- /n -->", f"<!-- n:{key} -->{value}<!-- /n -->", text)
        path.write_text(text, encoding="utf-8")


def status(found: int, total: int) -> str:
    if total == 0:
        return "no Hebrew quotes"
    if found == total:
        return "all found"
    return "partly found" if found else "none found here"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--texts", required=True, type=Path)
    ap.add_argument("--jobs", type=int, default=4)
    args = ap.parse_args()

    load_texts(args.texts)
    records = json.loads((RELEASE / "manuscripts.json").read_text(encoding="utf-8"))
    jobs = []
    for r in records:
        md = (RELEASE / "manuscripts" / r["folder"] / "manuscript.md").read_text(encoding="utf-8")
        seen = list(dict.fromkeys(quotes_in(md)))
        r["quotes"] = seen
        jobs.extend(seen)
    unique = list(dict.fromkeys(jobs))
    with Pool(args.jobs) as pool:
        hits = dict(zip(unique, pool.map(find, unique, chunksize=50)))

    detail, by_result = [], collections.OrderedDict()
    for r in records:
        found = [q for q in r["quotes"] if hits[q]]
        r["found"], r["total"] = len(found), len(r["quotes"])
        r["status"] = status(r["found"], r["total"])
        r["books"] = collections.Counter(hits[q][0] for q in found).most_common(3)
        r["longest"] = max((len(q.split()) for q in r["quotes"]), default=0)
        by_result.setdefault(r["result"], []).append(r)
        for q in r["quotes"]:
            detail.append(dict(manuscript=r["folder"], quote=q,
                               found=bool(hits[q]), book=hits[q][0] if hits[q] else None,
                               line=hits[q][1] if hits[q] else None))

    total_q = sum(r["total"] for r in records)
    total_f = sum(r["found"] for r in records)
    counts = collections.Counter(r["status"] for r in records)
    (HERE / "quotes.json").write_text(json.dumps(detail, ensure_ascii=False, indent=0), encoding="utf-8")
    (HERE / "catalogue.yaml").write_text(yaml_out(by_result, len(BOOKS)), encoding="utf-8")
    (HERE / "catalogue.md").write_text(md_out(by_result, total_q, total_f, counts, len(BOOKS)), encoding="utf-8")
    single = [r for r in records if r["result"] in SINGLE_BOOK]
    sq, sf = sum(r["total"] for r in single), sum(r["found"] for r in single)
    fill(HERE / "README.md", dict(books=len(BOOKS), quotes=f"{total_q:,}", found=f"{total_f:,}",
                                  pct=f"{100 * total_f / max(total_q, 1):.1f}%", single_quotes=f"{sq:,}",
                                  single_found=f"{sf:,}", **{s.replace(" ", "_"): counts.get(s, 0) for s in
                                  ("all found", "partly found", "none found here", "no Hebrew quotes")}))
    print(f"{len(BOOKS)} books, {len(records)} manuscripts, {total_q:,} quotes, {total_f:,} found "
          f"({100 * total_f / max(total_q, 1):.1f}%). {dict(counts)}")


def yaml_out(by_result, n_books: int) -> str:
    out = ["# Quote check, manuscript by manuscript. Written by verification/check_quotes.py.",
           f"books_checked: {n_books}", "results:"]
    for res, rs in by_result.items():
        out += [f"  - result: \"{res}\"", "    manuscripts:"]
        for r in rs:
            out += [f"      - folder: {r['folder']}",
                    f"        quotes: {r['total']}",
                    f"        found: {r['found']}",
                    f"        status: {r['status']}"]
            if r["books"]:
                out.append("        found_in: [" + ", ".join(json.dumps(b) for b, _ in r["books"]) + "]")
    return "\n".join(out) + "\n"


def md_out(by_result, total_q, total_f, counts, n_books: int) -> str:
    out = ["# Quote check", "",
           "Every manuscript in this collection quotes its sources in Hebrew. When the research was done, each "
           "quote was checked against its line in the source text before it was kept, and the manuscripts say so "
           "in their opening notes. This page records a second, independent check, made for the release by "
           f"`check_quotes.py`, against the {n_books} books packed with the Only One guide. See [README.md](README.md) "
           "for what the check does and does not show.", "",
           f"**{total_q:,} quotes in all; {total_f:,} found word for word in those {n_books} books "
           f"({100 * total_f / max(total_q, 1):.1f}%).** The rest are not found *here*: most quote one of the "
           "other books in the full library, which this check did not have.", "",
           "| Status | Manuscripts |", "|---|---:|"]
    for s in ("all found", "partly found", "none found here", "no Hebrew quotes"):
        out.append(f"| {s} | {counts.get(s, 0)} |")
    out.append("")
    for res, rs in by_result.items():
        q = sum(r["total"] for r in rs)
        f = sum(r["found"] for r in rs)
        out += [f"### Result {res}", "", f"[{rs[0]['family']}](../CONTENTS.md#{res}). "
                f"{q:,} quotes, {f:,} found here.", "",
                "| Manuscript | Quotes | Found here | Status | Found in |", "|---|---:|---:|---|---|"]
        for r in rs:
            books = "; ".join(b for b, _ in r["books"])
            out.append(f"| <a name=\"{r['folder'].lower()}\"></a>[{r['title']}](../manuscripts/{r['folder']}/manuscript.md) "
                       f"| {r['total']} | {r['found']} | {r['status']} | {books} |")
        out.append("")
    return "\n".join(out)


if __name__ == "__main__":
    main()
