---
title: An Ensemble of Neural Models for Nested Adverse Drug Events and Medication Extraction with Subwords
authors:
- Ju., M.
- Nguyen, N. T. H.
- Miwa, M.
- Ananiadou, S.
authorSlugs:
- ''
- ''
- ''
- sophia-ananiadou
venue: 'in: Journal of the American Medical Informatics Association, 27:1(22-30)'
venueShort: 'in: Journal of the American Medical Informatics Association'
venueType: journal
year: 2019
doi: http://dx.doi.org/10.1093/jamia/ocz075
aigaionId: 463
pubType: Article
bibtexKey: 'Journal:'
pages: 22-30
keywords: []
abstract: 'OBJECTIVE: This article describes an ensembling system to automatically extract adverse drug events and drug related entities from clinical narratives, which was developed for the 2018 n2c2 Shared Task Track 2. MATERIALS AND METHODS: We designed a neural model to tackle both nested (entities embedded in other entities) and polysemous entities (entities annotated with multiple semantic types) based on MIMIC III discharge summaries. To better represent rare and unknown words in entities, we further tokenized the MIMIC III data set by splitting the words into finer-grained subwords. We finally combined all the models to boost the performance. Additionally, we implemented a featured-based conditional random field model and created an ensemble to combine its predictions with those of the neural model. RESULTS: Our method achieved 92.78% lenient micro F1-score, with 95.99% lenient precision, and 89.79% lenient recall, respectively. Experimental results showed that combining the predictions of either multiple models, or of a single model with different settings can improve performance. DISCUSSION: Analysis of the development set showed that our neural models can detect more informative text regions than feature-based conditional random field models. Furthermore, most entity types significantly benefit from subword representation, which also allows us to extract sparse entities, especially nested entities. CONCLUSION: The overall results have demonstrated that the ensemble method can accurately recognize entities, including nested and polysemous entities. Additionally, our method can recognize sparse entities by reconsidering the clinical narratives at a finer-grained subword level, rather than at the word level.'
---
