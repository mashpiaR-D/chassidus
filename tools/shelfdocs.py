"""Turn the packed research shelves back into readable Markdown documents.

Each shelf file in `../shelf/Research-*.txt.gz` holds one research folder, flattened for search: one paragraph a
line, written as "Document › Section ⟶ text". Tables, lists and quotes were folded onto one line. This module
reads a shelf file and gives back its documents, with the headings, tables, lists and quotes laid out again.
"""
from __future__ import annotations

import gzip
import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

ARROW, CRUMB = " ⟶ ", " › "
DATE = re.compile(r"\b(20\d\d-\d\d-\d\d)\b")


@dataclass
class Doc:
    shelf: str                      # shelf file stem, e.g. "Research-core"
    key: str                        # the title as the shelf gives it (first crumb)
    title: str                      # the full title (front matter, when there is one)
    meta: dict = field(default_factory=dict)
    sections: list = field(default_factory=list)   # [(heading or "", [paragraph, ...])]
    date: str = ""

    def markdown(self) -> str:
        out = []
        for head, paras in self.sections:
            if head:
                out.append(f"## {head}")
            for p in paras:
                if p.startswith("|") and out and out[-1].startswith("|"):
                    out[-1] += "\n" + p          # a long table was packed as several lines: keep it one table
                else:
                    out.append(p)
        return "\n\n".join(out).strip() + "\n"

    def text(self) -> str:
        return "\n".join(p for _, ps in self.sections for p in ps)


def read_shelf(path: Path) -> list[Doc]:
    docs: dict[str, Doc] = {}
    stem = path.name.removesuffix(".txt.gz")
    with gzip.open(path, "rt", encoding="utf-8") as fh:
        for raw in fh:
            line = raw.rstrip("\n")
            if not line.strip():
                continue
            ref, _, text = line.partition(ARROW)
            crumbs = ref.split(CRUMB)
            key = crumbs[0].strip()
            head = CRUMB.join(crumbs[1:]).strip() if len(crumbs) > 1 else ""
            if head == key:
                head = ""
            doc = docs.get(key)
            if doc is None:
                doc = docs[key] = Doc(shelf=stem, key=key, title=key)
            if text.startswith("---") and text.rstrip().endswith("---") and not doc.sections:
                doc.meta = front_matter(text)
                doc.title = doc.meta.get("title", key)
                continue
            if not doc.sections or doc.sections[-1][0] != head:
                doc.sections.append((head, []))
            doc.sections[-1][1].append(unfold(text))
    for doc in docs.values():
        m = DATE.search(doc.text())
        doc.date = m.group(1) if m else ""
    return list(docs.values())


def front_matter(text: str) -> dict:
    return {k: v for k, v in re.findall(r'(\w+): "((?:[^"\\]|\\.)*)"', text)}


# ---- unfolding what the flattening folded ---------------------------------------------------------------

def unfold(text: str) -> str:
    t = text.strip()
    tail = re.match(r"(\|.*\|)\s+(#{1,6} .*)$", t)
    if tail:                            # a heading packed onto the end of a table
        return unfold(tail.group(1)) + "\n\n" + tail.group(2)
    if t.startswith("|") and t.endswith("|") and "| |" in t:
        return unfold_table(t)
    if t.startswith("> "):
        return "\n> ".join(re.split(r" > (?=\S)", t))
    if re.match(r"1\. ", t):
        return unfold_numbered(t)
    if t.startswith("- "):
        return "\n".join(re.split(r" (?=- (?:\*\*|\[|`|\*[^*\s]))", t))
    return t


def unfold_numbered(t: str) -> str:
    items, rest, n = [], t, 2
    while True:
        m = re.search(rf" (?={n}\. )", rest)
        if not m:
            items.append(rest)
            break
        items.append(rest[: m.start()])
        rest, n = rest[m.end():], n + 1
    return "\n".join(items)


def unfold_table(t: str) -> str:
    parts = t[1:-1].split("|")
    for n in range(1, 30):              # n = number of columns: the separator row follows the header
        sep = parts[n + 1: 2 * n + 1]
        if len(sep) == n and all(re.fullmatch(r"\s*:?-{3,}:?\s*", c) for c in sep) and (len(parts) + 1) % (n + 1) == 0:
            rows = [parts[i: i + n] for i in range(0, len(parts), n + 1)]
            return "\n".join("| " + " | ".join(c.strip() for c in r) + " |" for r in rows)
    for n in range(2, 30):              # the rows after a header packed on its own line: every (n+1)th cell is a gap
        if (len(parts) + 1) % (n + 1) == 0 and all(not c.strip() for c in parts[n::n + 1]):
            rows = [parts[i: i + n] for i in range(0, len(parts), n + 1)]
            return "\n".join("| " + " | ".join(c.strip() for c in r) + " |" for r in rows)
    return " |\n| ".join(re.split(r" \| \| ?(?=\S)", t))     # uneven rows: break at the row gaps only


# ---- small helpers ---------------------------------------------------------------------------------------

def plain(md: str) -> str:
    """Markdown to plain prose, for abstracts."""
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", md)
    s = re.sub(r"`([^`]*)`", r"\1", s)
    s = re.sub(r"\*\*|__", "", s)
    s = re.sub(r"(?<!\w)\*(?!\s)([^*]+?)\*(?!\w)", r"\1", s)
    s = re.sub(r"^\s*(?:[-*>]|\d+\.)\s+", "", s, flags=re.M)
    return re.sub(r"\s+", " ", s).strip()


def cut_words(s: str, limit: int) -> str:
    words = s.split()
    if len(words) <= limit:
        return s
    head = " ".join(words[:limit])
    end = max(head.rfind(". "), head.rfind("? "), head.rfind("! "))
    if end > len(head) * 0.5:
        return head[: end + 1]
    return head.rstrip(",;:") + " …"


def relink(md: str) -> str:
    """Links into the research repo don't exist here: keep the words, drop the link. Keep web links and anchors."""
    return re.sub(r"\[([^\]]+)\]\((?!https?:|#)[^)]*\)", r"\1", md)


def first_added(path: Path) -> str:
    try:
        out = subprocess.run(["git", "log", "--diff-filter=A", "--format=%ad", "--date=short", "--", str(path)],
                             cwd=path.parent, capture_output=True, text=True, check=True).stdout.split()
        return out[-1] if out else ""
    except Exception:
        return ""
