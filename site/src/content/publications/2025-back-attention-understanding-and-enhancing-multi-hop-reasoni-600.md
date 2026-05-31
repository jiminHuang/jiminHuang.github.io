---
title: 'Back Attention: Understanding and Enhancing Multi-Hop Reasoning in Large Language Models'
authors:
- Yu, Z.
- Belinkov, Y.
- Ananiadou, S.
authorSlugs:
- zeping-yu
- ''
- sophia-ananiadou
venue: Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP), pages 11257–11272
venueShort: EMNLP 2025
venueType: conference
year: 2025
doi: http://dx.doi.org/10.18653/v1/2025.emnlp-main.567
url: https://aclanthology.org/2025.emnlp-main.567/
aigaionId: 600
pubType: Inproceedings
bibtexKey: yu:2025b
pages: 11257–11272
keywords: []
abstract: 'We investigate how large language models (LLMs) perform latent multi-hop reasoning in prompts like "Wolfgang Amadeus Mozart''s mother''s spouse is".To analyze this process, we introduce logit flow, an interpretability method that traces how logits propagate across layers and positions toward the final prediction.Using logit flow, we identify four distinct stages in single-hop knowledge prediction: (A) entity subject enrichment, (B) entity attribute extraction, (C) relation subject enrichment, and (D) relation attribute extraction.Extending this analysis to multi-hop reasoning, we find that failures often stem from the relation attribute extraction stage, where conflicting logits reduce prediction accuracy.To address this, we propose back attention, a novel mechanism that enables lower layers to leverage higher-layer hidden states from different positions during attention computation.With back attention, a 1-layer transformer achieves the performance of a 2-layer transformer.Applied to five LLMs, back attention improves accuracy on five reasoning datasets, demonstrating its effectiveness in enhancing latent multi-hop reasoning ability.'
topics:
- Language Models
- Computer Science
- Catastrophic Forgetting
- Zeping Yu
- Sophia Ananiadou
- language models
paperTerms:
- Empirical Methods
- Natural Language Processing
- Back Attention
- Multi-Hop Reasoning
- Large Language Models
- Israel Institute
- '@ technion.ac.il'
- language models
- latent multi-hop reasoning
- Wolfgang Amadeus Mozart
---
