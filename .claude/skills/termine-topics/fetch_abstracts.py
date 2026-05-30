#!/usr/bin/env python3
"""
Fetch missing abstracts for a collection of papers via OpenAlex (by DOI).
Writes the abstract back to each markdown's frontmatter as `abstract:`.

OpenAlex stores abstracts as an inverted index ({word: [positions]}) for
copyright reasons; we reconstruct the running text. The endpoint is free,
no auth needed, but please pass `--email you@example.com` to opt into the
polite pool (higher rate limits).

Usage:

    python fetch_abstracts.py \
        --input "site/src/content/publications/*.md" \
        --doi-field frontmatter:doi \
        --email name@example.com
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
import urllib.request


def parse_frontmatter(text: str) -> tuple[dict, str]:
    m = re.match(r"---\n(.+?)\n---\n?(.*)", text, re.S)
    if not m:
        return {}, text
    fm: dict = {}
    for line in m.group(1).split("\n"):
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        v = v.strip()
        v = re.sub(r'^["\']|["\']$', "", v)
        fm[k.strip()] = v
    return fm, m.group(2)


def write_frontmatter_field(path: str, field: str, value: str) -> None:
    text = open(path).read()
    if not text.startswith("---"):
        return
    fm_raw_m = re.match(r"---\n(.+?)\n---", text, re.S)
    if not fm_raw_m:
        return
    fm_raw = fm_raw_m.group(1)
    lines = fm_raw.split("\n")
    # Use YAML literal block scalar (|-) for safe long strings with special chars.
    # Strip carriage returns and trailing whitespace, indent each line with 2 spaces.
    cleaned = value.replace("\r", "").rstrip()
    indented = "\n".join("  " + ln for ln in cleaned.split("\n"))
    new_block = f"{field}: |-\n{indented}"
    # Skip-existing: drop the old field block (may span multiple lines)
    out_lines = []
    skip_until_dedent = False
    for ln in lines:
        if skip_until_dedent:
            if ln.startswith(" ") or ln.startswith("\t") or ln == "":
                continue
            skip_until_dedent = False
        if ln.startswith(f"{field}:"):
            skip_until_dedent = True
            continue
        out_lines.append(ln)
    out_lines.append(new_block)
    new_fm = "\n".join(out_lines)
    replacement = f"---\n{new_fm}\n---"
    new_text = re.sub(r"---\n.+?\n---", lambda _m: replacement, text, count=1, flags=re.S)
    open(path, "w").write(new_text)


def normalise_doi(raw: str) -> str | None:
    if not raw:
        return None
    raw = raw.strip()
    m = re.search(r"(10\.\d+/[^\s\"']+)", raw)
    return m.group(1) if m else None


def reconstruct_abstract(inverted: dict | None) -> str | None:
    if not inverted:
        return None
    pos = {}
    for word, positions in inverted.items():
        for p in positions:
            pos[p] = word
    if not pos:
        return None
    return " ".join(pos[i] for i in sorted(pos))


def fetch_openalex(doi: str, email: str | None, timeout: int = 30) -> dict | None:
    encoded = urllib.parse.quote(doi, safe="/")
    url = f"https://api.openalex.org/works/doi:{encoded}"
    if email:
        url += f"?mailto={urllib.parse.quote(email)}"
    req = urllib.request.Request(url, headers={"User-Agent": f"termine-topics-skill ({email or 'anon'})"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            if r.status != 200:
                return None
            return json.loads(r.read().decode("utf-8"))
    except urllib.request.HTTPError as e:
        if e.code == 404:
            return None
        raise
    except Exception:
        return None


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--doi-field", default="frontmatter:doi")
    p.add_argument("--abstract-field", default="abstract")
    p.add_argument("--email", default=None, help="OpenAlex polite-pool email")
    p.add_argument("--cache-dir", default=".cache/openalex")
    p.add_argument("--skip-existing", action="store_true", default=True)
    p.add_argument("--force", action="store_true", help="Re-fetch even if abstract already set")
    args = p.parse_args()

    os.makedirs(args.cache_dir, exist_ok=True)
    files = sorted(glob.glob(args.input))
    if not files:
        sys.exit(f"no files matched: {args.input}")

    fetched, cached, missing_doi, no_abs, already = 0, 0, 0, 0, 0
    for i, path in enumerate(files, 1):
        text = open(path).read()
        fm, _ = parse_frontmatter(text)
        if args.skip_existing and not args.force and fm.get(args.abstract_field):
            already += 1
            continue
        doi = normalise_doi(fm.get(args.doi_field.split(":", 1)[1]))
        if not doi:
            missing_doi += 1
            continue
        cache_path = os.path.join(args.cache_dir, doi.replace("/", "_") + ".json")
        if os.path.isfile(cache_path):
            data = json.load(open(cache_path))
            cached += 1
        else:
            data = fetch_openalex(doi, args.email)
            if data:
                open(cache_path, "w").write(json.dumps(data))
            fetched += 1
            time.sleep(0.1)
        if not data:
            no_abs += 1
            continue
        abstract = reconstruct_abstract(data.get("abstract_inverted_index"))
        if not abstract:
            no_abs += 1
            continue
        write_frontmatter_field(path, args.abstract_field, abstract)
        if i % 25 == 0:
            print(f"  ... {i}/{len(files)} done (fetched={fetched} cached={cached})", file=sys.stderr)

    print(
        f"[fetch_abstracts] fetched={fetched} cached={cached} "
        f"already={already} missing_doi={missing_doi} no_abstract={no_abs}",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
