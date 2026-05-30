---
name: termine-topics
description: Extract multi-word technical terms from a corpus and write them back as topic tags. Wraps NaCTeM's TerMine HTTP API (C-value algorithm, Frantzi & Ananiadou 1998) — the canonical statistical term extractor for scientific text. Use this when (a) you want to label a set of documents with their characteristic terminology, (b) you're building a topic filter / facet over an article collection, or (c) you've been tempted to write regex topic rules over a research corpus and want to do the thing properly instead.
---

# termine-topics

This skill turns a corpus of short text records (publication titles, abstracts,
news entries, anything similar) into a vocabulary of multi-word technical
terms, then tags each record with which terms it contains.

## When to use

- You have a folder of markdown / text files and want a topic facet on a UI
  over them.
- You were about to write `if /large language model/.test(title)` rules over
  a research literature corpus. Don't — run this.
- You're building a static site over a content collection and need to add
  topic filters that reflect what the corpus actually talks about, not what
  you assumed.

## When NOT to use

- The corpus is < 50 documents — TerMine needs repetition to find terms.
  Use hand-curated topics instead.
- The text isn't scientific / technical — C-value is tuned for terminology.
  For news or fiction, use BERTopic or LDA.
- You need topic *modelling* with soft assignments. C-value gives hard
  membership ("this paper mentions this term"). For probabilistic topics
  use the `bertopic` route.

## What it does

1. Concatenate the corpus into one text blob (with sentence breaks).
2. POST to `https://www.nactem.ac.uk/cgi-bin/termine/termine_cvalue.cgi`
   with `geniass` as the tagger.
3. Parse the response HTML for ranked term anchors.
4. For each document, mark which top-N terms it contains.
5. Write the terms back to the document's frontmatter (or to a sidecar
   JSON if the documents aren't markdown).

## How to use

### Fast path

```bash
python .claude/skills/termine-topics/extract.py \
  --input "site/src/content/publications/*.md" \
  --field-from frontmatter:title,venueShort \
  --field-write frontmatter:topics \
  --top 30 \
  --min-cvalue 5
```

This reads every matching markdown's frontmatter `title` and `venueShort`,
sends the joined corpus through TerMine, keeps the top 30 terms above
C-value 5, and writes each document's matching terms back as
`topics: ["...", "..."]`.

### With abstracts

```bash
python .claude/skills/termine-topics/extract.py \
  --input "papers/*.md" \
  --field-from frontmatter:title,abstract \
  --field-write frontmatter:topics
```

### Sidecar JSON instead of frontmatter

```bash
python .claude/skills/termine-topics/extract.py \
  --input "data/*.txt" \
  --field-from file:body \
  --field-write sidecar:topics.json
```

### Inspecting just the top terms (no write-back)

```bash
python .claude/skills/termine-topics/extract.py \
  --input "papers/*.md" \
  --field-from frontmatter:title \
  --dry-run --top 50
```

## Notes

- The API is throttled — for very large corpora, chunk into batches of
  ~500 KB of text and merge the term rankings (the script does this for
  you).
- Topics written back are case-preserved as TerMine returned them.
- C-value tends to over-rank long compound terms ("text mining tool
  development framework"). Use `--max-words 3` to cap n-gram size.
- Always commit the result; running TerMine again with new documents
  added will perturb rankings, so frozen results live in git.

## Credit

C-value algorithm: Frantzi, K., Ananiadou, S., Mima, H. (2000).
*Automatic recognition of multi-word terms*. Int. J. Digital Libraries.
The first NaCTeM PhD's thesis algorithm.
