---
title: 'Locate-then-Merge: Neuron-Level Parameter Fusion for Mitigating Catastrophic Forgetting in Multimodal LLMs'
authors:
- Yu, Z.
- Ananiadou, S.
authorSlugs:
- zeping-yu
- sophia-ananiadou
venue: 'Findings of the Association for Computational Linguistics: EMNLP 2024, pages 7065–7078'
venueShort: EMNLP 2024
venueType: conference
year: 2025
doi: http://dx.doi.org/10.18653/v1/2025.findings-emnlp.372
url: https://aclanthology.org/2025.findings-emnlp.372/
aigaionId: 610
pubType: Inproceedings
bibtexKey: yu:2025c
pages: 7065–7078
keywords: []
abstract: Although multimodal large language models (MLLMs) have achieved impressive performance, the multimodal instruction tuning stage often causes catastrophic forgetting of the base LLM's language ability, even in strong models like Llama3.To address this, we propose Locate-then-Merge, a training-free parameter fusion framework that first locates important parameters and then selectively merges them.We further introduce Neuron-Fusion, a neuronlevel strategy that preserves the influence of neurons with large parameter shifts-neurons likely responsible for newly acquired visual capabilities-while attenuating the influence of neurons with smaller changes that likely encode general-purpose language skills.This design enables better retention of visual adaptation while mitigating language degradation.Experiments on 13 benchmarks across both language and visual tasks show that Neuron-Fusion consistently outperforms existing model merging methods.Further analysis reveals that our method effectively reduces context hallucination in generation.
---
