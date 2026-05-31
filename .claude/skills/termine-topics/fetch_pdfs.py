#!/usr/bin/env python3
"""
Download PDFs for a corpus of papers from two sources, then extract text:

1. Frontmatter `pdfUrl` field (e.g. Aigaion-hosted PDFs we already know).
2. OpenAlex `open_access.oa_url` for papers with a DOI (resolved on the fly).

Saves PDFs under `.cache/pdfs/<key>.pdf` and extracted text under
`.cache/pdftext/<key>.txt`, where <key> is the aigaionId (or a slug
derived from the file path).

Usage:

    python fetch_pdfs.py --input "site/src/content/publications/*.md" \
        --email name@example.com

Skips files that are already cached. Use --force to redownload.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
import time
import http.cookiejar
import urllib.parse
import urllib.request

import fitz  # PyMuPDF


HEADERS = {
    "User-Agent": "Mozilla/5.0 (termine-topics-skill/1.0; +https://github.com/jiminHuang/jiminHuang.github.io)",
}

# Shared cookie jar (Aigaion sets a session cookie on first hit that gates downloads)
_jar = http.cookiejar.CookieJar()
_opener = urllib.request.build_opener(
    urllib.request.HTTPCookieProcessor(_jar),
    urllib.request.HTTPRedirectHandler(),
)
_opener.addheaders = list(HEADERS.items())


def _warm_aigaion_session() -> None:
    """Hit the Aigaion landing page once to pick up an AigaionInstance cookie."""
    if any(c.name.startswith("AigaionInstance") for c in _jar):
        return
    try:
        _opener.open(
            "https://www.nactem.ac.uk/aigaion2/index.php/publications.html",
            timeout=20,
        )
    except Exception:
        pass


def parse_frontmatter(text: str) -> dict:
    m = re.match(r"---\n(.+?)\n---", text, re.S)
    if not m:
        return {}
    fm: dict = {}
    for line in m.group(1).split("\n"):
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        v = v.strip()
        # very simple — handles single-line scalars, ignores lists/blocks
        v = re.sub(r'^["\']|["\']$', "", v)
        fm[k.strip()] = v
    return fm


def fetch(url: str, timeout: int = 60) -> bytes | None:
    """GET and return bytes; follow redirects + carry cookies; return None on failure."""
    if "nactem.ac.uk/aigaion2" in url:
        _warm_aigaion_session()
    try:
        with _opener.open(url, timeout=timeout) as r:
            if r.status != 200:
                return None
            return r.read()
    except Exception:
        return None


def lookup_oa(doi: str, cache_dir: str, email: str | None) -> str | None:
    """Get OA URL for a DOI from cached OpenAlex JSON or live."""
    safe = doi.replace("/", "_")
    p = os.path.join(cache_dir, safe + ".json")
    data = None
    if os.path.isfile(p):
        try:
            data = json.load(open(p))
        except Exception:
            data = None
    if data is None:
        url = f"https://api.openalex.org/works/doi:{urllib.parse.quote(doi, safe='/')}"
        if email:
            url += f"?mailto={urllib.parse.quote(email)}"
        body = fetch(url, timeout=20)
        if not body:
            return None
        try:
            data = json.loads(body)
            os.makedirs(cache_dir, exist_ok=True)
            open(p, "w").write(body.decode("utf-8", "replace"))
        except Exception:
            return None
    return ((data.get("open_access") or {}).get("oa_url")) or None


def normalise_doi(raw: str) -> str | None:
    if not raw:
        return None
    m = re.search(r"(10\.\d+/[^\s\"']+)", raw)
    return m.group(1) if m else None


def extract_text(pdf_bytes: bytes, max_pages: int = 25) -> str | None:
    """Use PyMuPDF to pull text; cap pages."""
    try:
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    except Exception:
        return None
    pages = []
    for i, page in enumerate(doc):
        if i >= max_pages:
            break
        try:
            pages.append(page.get_text("text"))
        except Exception:
            continue
    doc.close()
    text = "\n".join(pages).strip()
    if not text:
        return None
    # Collapse runs of whitespace
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--pdf-cache", default=".cache/pdfs")
    p.add_argument("--text-cache", default=".cache/pdftext")
    p.add_argument("--openalex-cache", default=".cache/openalex")
    p.add_argument("--email", default=None)
    p.add_argument("--force", action="store_true")
    p.add_argument("--max-pages", type=int, default=25)
    args = p.parse_args()

    os.makedirs(args.pdf_cache, exist_ok=True)
    os.makedirs(args.text_cache, exist_ok=True)

    files = sorted(glob.glob(args.input))
    if not files:
        sys.exit(f"no files: {args.input}")

    n_aigaion, n_oa, n_have_text, n_fail = 0, 0, 0, 0
    for i, path in enumerate(files, 1):
        text = open(path).read()
        fm = parse_frontmatter(text)
        pid = fm.get("aigaionId") or os.path.basename(path)[:-3]
        text_path = os.path.join(args.text_cache, f"{pid}.txt")
        if not args.force and os.path.isfile(text_path) and os.path.getsize(text_path) > 200:
            n_have_text += 1
            continue

        pdf_path = os.path.join(args.pdf_cache, f"{pid}.pdf")
        pdf_bytes = None
        source = None
        if not args.force and os.path.isfile(pdf_path) and os.path.getsize(pdf_path) > 1024:
            pdf_bytes = open(pdf_path, "rb").read()
            source = "cached"
        else:
            # 1. Try Aigaion pdfUrl
            url = fm.get("pdfUrl")
            if url:
                pdf_bytes = fetch(url)
                if pdf_bytes and pdf_bytes[:4] == b"%PDF":
                    source = "aigaion"
                    open(pdf_path, "wb").write(pdf_bytes)
                    n_aigaion += 1
            # 2. Fall back to OpenAlex OA
            if not pdf_bytes:
                doi = normalise_doi(fm.get("doi"))
                if doi:
                    oa = lookup_oa(doi, args.openalex_cache, args.email)
                    if oa:
                        pdf_bytes = fetch(oa)
                        if pdf_bytes and pdf_bytes[:4] == b"%PDF":
                            source = "openalex"
                            open(pdf_path, "wb").write(pdf_bytes)
                            n_oa += 1
                time.sleep(0.05)

        if not pdf_bytes:
            n_fail += 1
            continue

        body = extract_text(pdf_bytes, args.max_pages)
        if not body:
            n_fail += 1
            continue
        open(text_path, "w").write(body)

        if i % 25 == 0:
            print(f"  ... {i}/{len(files)} aigaion={n_aigaion} oa={n_oa} cached={n_have_text} fail={n_fail}",
                  file=sys.stderr)

    print(
        f"[fetch_pdfs] aigaion={n_aigaion} openalex={n_oa} "
        f"already_cached={n_have_text} failed={n_fail}",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
