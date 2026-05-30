---
title: 'GenerativeRE: Incorporating a Novel Copy Mechanism and Pretrained Model for Joint Entity and Relation Extraction'
authors:
- Cao, J.
- Ananiadou, S.
authorSlugs:
- jiarun-cao-alum-2024
- sophia-ananiadou
venue: Findings of EMNLP, pages 2119–2126
venueShort: EMNLP
venueType: conference
year: 2021
doi: http://dx.doi.org/10.18653/v1/2021.findings-emnlp.182
url: https://aclanthology.org/2021.findings-emnlp.182
aigaionId: 492
pubType: Inproceedings
bibtexKey: cao:2021
pages: 2119–2126
keywords: []
abstract: Previous neural seq2seq models have shown the effectiveness for jointly extracting relation triplets. However, most of these models suffer from incompletion and disorder problems when they extract multi-token entities from input sentences. To tackle these problems, we propose a generative, multi-task learning framework, named GenerativeRE. We firstly propose a special entity labelling method on both input and output sequences. During the training stage, GenerativeRE fine-tunes the pretrained generative model and learns the special entity labels simultaneously. During the inference stage, we propose a novel copy mechanism equipped with three mask strategies, to generate the most probable tokens by diminishing the scope of the model decoder. Experimental results show that our model achieves 4.6% and 0.9% F1 score improvements over the current state-of-the-art methods in the NYT24 and NYT29 benchmark datasets respectively.
---
