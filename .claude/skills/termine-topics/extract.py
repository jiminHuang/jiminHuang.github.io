#!/usr/bin/env python3
"""
termine-topics: extract multi-word technical terms from a corpus via NaCTeM
TerMine (C-value algorithm) and write them back as document topics.

See SKILL.md for full usage. Quick example:

    python extract.py \
        --input "site/src/content/publications/*.md" \
        --field-from frontmatter:title,venueShort \
        --field-write frontmatter:topics \
        --top 30
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
import time
import urllib.parse
from html import unescape
from typing import Optional

import urllib.request

TERMINE_URL = "https://www.nactem.ac.uk/cgi-bin/termine/termine_cvalue.cgi"
CHUNK_BYTES = 400_000  # rough cap per request; TerMine is happier with batches
UA = "termine-topics-skill/1.0 (https://github.com/jiminHuang/jiminHuang.github.io)"


# ─────────────────────────── document IO ───────────────────────────


def parse_frontmatter(text: str) -> tuple[dict, str]:
    m = re.match(r"---\n(.+?)\n---\n?(.*)", text, re.S)
    if not m:
        return {}, text
    fm_raw, body = m.group(1), m.group(2)
    fm: dict = {}
    for line in fm_raw.split("\n"):
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        fm[k.strip()] = v.strip()
    return fm, body


def get_field_value(doc_text: str, fm: dict, spec: str) -> str:
    """Resolve a `field:foo,bar` spec to a string from the document."""
    where, _, names = spec.partition(":")
    if not names:
        return ""
    parts = []
    for name in [n.strip() for n in names.split(",")]:
        if where == "frontmatter":
            val = fm.get(name, "")
            # Trim YAML scalar wrapper
            val = re.sub(r'^["\']|["\']$', "", val)
            # If it's a [list,...], extract scalars
            list_m = re.match(r"\[(.+)\]$", val)
            if list_m:
                val = " ".join(
                    re.findall(r'"([^"]+)"', list_m.group(1))
                    or list_m.group(1).split(",")
                )
        elif where == "file":
            val = doc_text if name == "body" else ""
        else:
            val = ""
        if val:
            parts.append(val.strip())
    return " . ".join(parts)


def write_frontmatter_field(path: str, field: str, value: list[str]) -> None:
    text = open(path).read()
    fm, body = parse_frontmatter(text)
    if not text.startswith("---"):
        # No frontmatter — prepend one
        new_fm = f"{field}: [{', '.join(json.dumps(v) for v in value)}]\n"
        open(path, "w").write(f"---\n{new_fm}---\n{text}")
        return
    # Re-emit frontmatter, replacing or appending the field
    fm_raw = re.match(r"---\n(.+?)\n---", text, re.S).group(1)
    lines = fm_raw.split("\n")
    new_line = f"{field}: [{', '.join(json.dumps(v) for v in value)}]"
    replaced = False
    out_lines = []
    for ln in lines:
        if ln.startswith(f"{field}:"):
            out_lines.append(new_line)
            replaced = True
        else:
            out_lines.append(ln)
    if not replaced:
        out_lines.append(new_line)
    new_fm = "\n".join(out_lines)
    replacement = f"---\n{new_fm}\n---"
    new_text = re.sub(r"---\n.+?\n---", lambda _m: replacement, text, count=1, flags=re.S)
    open(path, "w").write(new_text)


# ─────────────────────────── TerMine API ───────────────────────────


def termine_extract(text: str, tagger: str = "geniass", timeout: int = 120) -> list[tuple[str, float]]:
    """POST text to TerMine, return [(term, c_value), ...]."""
    # Build a simple multipart form by hand
    boundary = "----termine-topics-skill"
    body_parts = []
    for name, value in [("type", "text"), ("tagger", tagger), ("prebr", "yes"), ("text", text)]:
        body_parts.append(f"--{boundary}\r\n")
        body_parts.append(f'Content-Disposition: form-data; name="{name}"\r\n\r\n')
        body_parts.append(f"{value}\r\n")
    body_parts.append(f"--{boundary}--\r\n")
    body = "".join(body_parts).encode("utf-8")

    req = urllib.request.Request(
        TERMINE_URL,
        data=body,
        headers={
            "Content-Type": f"multipart/form-data; boundary={boundary}",
            "User-Agent": UA,
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        html = resp.read().decode("utf-8", errors="replace")

    # The HTML embeds <a id="tN" title="t">TERM</a>; ranking is by position.
    # C-values aren't exposed in HTML, so we approximate via rank.
    terms: list[tuple[str, float]] = []
    for m in re.finditer(r'<a id="t\d+"[^>]*title="t">([^<]+)</a>', html):
        term = unescape(m.group(1)).strip()
        if term:
            terms.append(term)
    # Score by inverse rank scaled to [1..100] so callers can threshold
    scored: list[tuple[str, float]] = []
    n = len(terms)
    for i, t in enumerate(terms):
        score = round(100 * (1 - i / max(1, n)), 2)
        scored.append((t, score))
    return scored


def chunked(corpus_texts: list[str]) -> list[str]:
    """Group document texts into chunks under CHUNK_BYTES."""
    chunks: list[str] = []
    buf: list[str] = []
    buf_size = 0
    for t in corpus_texts:
        s = t.strip() + " . "
        if buf_size + len(s) > CHUNK_BYTES and buf:
            chunks.append("".join(buf))
            buf, buf_size = [], 0
        buf.append(s)
        buf_size += len(s)
    if buf:
        chunks.append("".join(buf))
    return chunks


# ─────────────────────────── pipeline ───────────────────────────


STOPLIST = {
    # PDF metadata / boilerplate
    "open access", "submission guidelines", "main content", "research article",
    "supporting information", "supplementary material", "view article",
    "permissions reuse", "creative commons", "available online",
    "abstract introduction", "introduction methods", "results discussion",
    "data availability", "conflicts interest", "competing interests",
    "author contributions", "additional file", "additional files",
    "corresponding author", "et al", "rights reserved", "user license",
    # Journal/venue names — not topics
    "bmc bioinformatics", "bmc medical informatics", "bmj open", "al bmj open",
    "computational linguistics", "biomedical text", "computational approaches",
    "13th workshop", "international workshop", "international journal",
    "third workshop", "shared task", "rel tasks", "ngan nguyen1",
    # Format / page artifacts
    "page  of", "page of", "table  results", "figure  table",
    "natural language", "machine learning", "deep learning",  # too generic
}

def normalise(term: str, max_words: int) -> Optional[str]:
    term = re.sub(r"\s+", " ", term).strip()
    if not term:
        return None
    if len(term.split()) > max_words:
        return None
    if len(term) < 4:
        return None
    # Drop obvious garbage
    if re.fullmatch(r"[\d\W_]+", term):
        return None
    # Stoplist
    if term.lower() in STOPLIST:
        return None
    # Has digits — usually page numbers, DOI fragments, "Nguyen1"
    if re.search(r"\d", term):
        return None
    # ALL CAPS — usually author surname or section header
    if term.isupper() and len(term) > 4:
        return None
    # Single letter or trailing initial like "Lee J"
    if re.search(r"\b[A-Z]\.?\s*$", term):
        return None
    return term


def run_per_paper(docs: list[tuple[str, str]], args) -> None:
    """POST each doc individually to TerMine; write its own top terms to frontmatter."""
    os.makedirs(args.per_paper_cache, exist_ok=True)
    where, _, field = args.field_write.partition(":")
    field = field or "paperTerms"

    n_done = 0
    n_skipped = 0
    n_tagged = 0
    total_terms = 0
    for i, (path, value) in enumerate(docs, 1):
        if len(value) < args.per_paper_min_chars:
            n_skipped += 1
            continue
        # Cache key from filename
        key = os.path.basename(path).rsplit(".", 1)[0]
        cache_path = os.path.join(args.per_paper_cache, key + ".json")
        if os.path.isfile(cache_path):
            try:
                terms = json.load(open(cache_path))
            except Exception:
                terms = None
        else:
            try:
                raw = termine_extract(value, timeout=120)
            except Exception as e:
                print(f"  [{i}/{len(docs)}] {key}: {e}", file=sys.stderr)
                terms = None
            else:
                # Normalise + keep top N
                clean = []
                seen = set()
                for t, s in raw:
                    n = normalise(t, args.max_words)
                    if n and n.lower() not in seen:
                        seen.add(n.lower())
                        clean.append([n, s])
                terms = clean[: args.per_paper_top]
                open(cache_path, "w").write(json.dumps(terms))
                time.sleep(0.6)  # polite
        if not terms:
            continue
        names = [t[0] for t in terms]
        if args.dry_run:
            if i <= 10:
                print(f"  {key[:60]:60} → {names[:5]}")
        else:
            write_frontmatter_field(path, field, names)
        n_tagged += 1
        total_terms += len(names)
        n_done += 1
        if n_done % 25 == 0:
            print(f"  ... {n_done} processed (tagged={n_tagged} skipped_short={n_skipped})",
                  file=sys.stderr)

    print(f"[per-paper] tagged {n_tagged} docs with {total_terms} terms; "
          f"skipped {n_skipped} short docs", file=sys.stderr)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True, help="Glob of input files")
    p.add_argument("--field-from", required=True, help="e.g. frontmatter:title,venueShort or file:body")
    p.add_argument("--field-write", default="frontmatter:topics", help="Where to write topics back")
    p.add_argument("--top", type=int, default=30)
    p.add_argument("--min-score", type=float, default=0)
    p.add_argument("--max-words", type=int, default=4)
    p.add_argument("--dry-run", action="store_true", help="Print top terms only, don't write back")
    p.add_argument("--text-cache", default=None,
                   help="Directory of extracted full-text files (e.g. .cache/pdftext). "
                        "Looked up by <aigaionId>.txt; if found, its content REPLACES "
                        "the frontmatter content for that paper.")
    p.add_argument("--per-paper", action="store_true",
                   help="POST each paper to TerMine individually and write its own top "
                        "terms back. Slow (~1 req/paper) but each paper's terms are "
                        "extracted in isolation.")
    p.add_argument("--per-paper-cache", default=".cache/termine_perpaper",
                   help="Where to cache per-paper TerMine JSON")
    p.add_argument("--per-paper-top", type=int, default=10,
                   help="How many top terms to keep per paper (default 10)")
    p.add_argument("--per-paper-min-chars", type=int, default=400,
                   help="Skip per-paper extraction if doc content is shorter than this")
    args = p.parse_args()

    files = sorted(glob.glob(args.input))
    if not files:
        sys.exit(f"no files matched: {args.input}")
    print(f"[termine-topics] {len(files)} files matched", file=sys.stderr)

    # Read each file → extracted text
    docs: list[tuple[str, str]] = []
    n_full = 0
    for path in files:
        text = open(path).read()
        fm, body = parse_frontmatter(text)
        value = get_field_value(text, fm, args.field_from)
        if args.text_cache:
            pid = fm.get("aigaionId")
            if pid:
                cache_file = os.path.join(args.text_cache, f"{pid}.txt")
                if os.path.isfile(cache_file):
                    cached = open(cache_file).read().strip()
                    if cached and len(cached) > 200:
                        value = cached
                        n_full += 1
        if value:
            docs.append((path, value))
    print(f"[termine-topics] {len(docs)} have content ({n_full} from full-text cache)", file=sys.stderr)

    if args.per_paper:
        run_per_paper(docs, args)
        return

    # Send to TerMine in chunks
    texts = [d[1] for d in docs]
    chunks = chunked(texts)
    print(f"[termine-topics] sending {len(chunks)} chunk(s) to TerMine", file=sys.stderr)
    merged: dict[str, float] = {}
    for i, chunk in enumerate(chunks):
        try:
            terms = termine_extract(chunk)
        except Exception as e:
            print(f"[termine-topics] chunk {i} failed: {e}", file=sys.stderr)
            continue
        for t, s in terms:
            n = normalise(t, args.max_words)
            if n is None:
                continue
            merged[n] = max(merged.get(n, 0), s)
        time.sleep(1)  # be polite

    ranked = sorted(merged.items(), key=lambda x: -x[1])
    top = [(t, s) for t, s in ranked if s >= args.min_score][: args.top]
    print(f"[termine-topics] {len(top)} terms after thresholding (top {args.top})", file=sys.stderr)
    for t, s in top[:25]:
        print(f"   {s:6.2f}  {t}")

    if args.dry_run:
        return

    # Tag each document with which top terms appear in it
    where, _, field = args.field_write.partition(":")
    tagged = 0
    total_assignments = 0
    for path, value in docs:
        text_lc = value.lower()
        hits = [t for t, _ in top if t.lower() in text_lc]
        if not hits:
            continue
        if where == "frontmatter":
            write_frontmatter_field(path, field or "topics", hits)
        else:
            # sidecar JSON next to the file
            sidecar = os.path.splitext(path)[0] + ".topics.json"
            open(sidecar, "w").write(json.dumps(hits))
        tagged += 1
        total_assignments += len(hits)
    print(
        f"[termine-topics] tagged {tagged}/{len(docs)} docs with "
        f"{total_assignments} total topic assignments",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
