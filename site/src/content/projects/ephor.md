---
name: EPHOR
tagline: Mining occupational exposure data to protect worker health across Europe.
status: Active
domain: Public health
yearStart: 2020
yearEnd: 2026
funder: European Commission (Horizon 2020)
partners:
  - University of Utrecht
  - INSERM
  - University of Manchester
  - Karolinska Institutet
lead: Sophia Ananiadou
tools:
  - EventMine
  - TerMine
  - Argo
publications:
  - title: "Mining exposure-disease associations from occupational health literature"
    venue: "Journal of Biomedical Informatics"
    year: 2024
  - title: "An ontology of workplace chemical hazards for text mining"
    venue: "Bioinformatics"
    year: 2023
website: https://www.ephor-project.eu/
---

EPHOR (the **Exposome Project for Health and Occupational Research**) is a
pan-European consortium investigating how lifelong occupational exposures —
chemicals, dust, noise, shift work, psychosocial stress — combine to shape
worker health.

NaCTeM's role is the **textual exposome**: extracting structured exposure
records from decades of occupational-medicine literature and turning them into
an open, queryable resource that complements EPHOR's biomarker and cohort
data.

## What we built

- A custom **exposure–outcome event extraction pipeline** on top of
  EventMine, fine-tuned to the occupational-health domain
- The **Occupational Exposure corpus**: 7,200 sentence-level annotations of
  exposures, durations, and health outcomes across 18 industrial sectors
- An **ontology of workplace chemical hazards** aligned with ChEBI and the
  ECHA chemical inventory
- Argo workflows so partner epidemiologists can re-run the pipeline on their
  own document sets

## Outcomes so far

Over **140,000 exposure–outcome relations** extracted from PubMed and grey
literature, feeding into EPHOR's cross-cohort meta-analyses. The annotated
corpus is openly available for benchmarking.
