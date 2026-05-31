---
title: Interpreting Arithmetic Mechanism in Large Language Models through Comparative Neuron Analysis
authors:
- Yu, Z.
- Ananiadou, S.
authorSlugs:
- zeping-yu
- sophia-ananiadou
venue: Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pages 3293–3306
venueShort: Proceedings of the 2024 Conference on Empirical Methods in N
venueType: conference
year: 2024
doi: http://dx.doi.org/10.18653/v1/2024.emnlp-main.193
url: https://aclanthology.org/2024.emnlp-main.193/
aigaionId: 592
pubType: Inproceedings
bibtexKey: yu:2024interpreting
pages: 3293–3306
keywords: []
abstract: 'We find arithmetic ability resides within a limited number of attention heads, with each head specializing in distinct operations.To delve into the reason, we introduce the Comparative Neuron Analysis (CNA) method, which identifies an internal logic chain consisting of four distinct stages from input to prediction: feature enhancing with shallow FFN neurons, feature transferring by shallow attention layers, feature predicting by arithmetic heads, and prediction enhancing among deep FFN neurons.Moreover, we identify the human-interpretable FFN neurons within both feature-enhancing and feature-predicting stages.These findings lead us to investigate the mechanism of LoRA, revealing that it enhances prediction probabilities by amplifying the coefficient scores of FFN neurons related to predictions.Finally, we apply our method in model pruning for arithmetic tasks and model editing for reducing gender bias.Code is on https://github.com/ zepingyu0512/arithmetic-mechanism.'
topics:
- Language Models
- Computer Science
- Zeping Yu
- Sophia Ananiadou
- National Centre
- Text Mining
- language models
- text mining
paperTerms:
- Empirical Methods
- Natural Language Processing
- Interpreting Arithmetic Mechanism
- Large Language Models
- Comparative Neuron Analysis
- Zeping Yu
- Sophia Ananiadou
- Computer Science
- National Centre
- Text Mining
---
