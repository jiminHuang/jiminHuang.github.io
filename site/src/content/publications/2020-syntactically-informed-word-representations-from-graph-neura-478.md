---
title: Syntactically-Informed Word Representations from Graph Neural Network
authors:
- Tran, T. T.
- Miwa, M.
- Ananiadou, S.
authorSlugs:
- ''
- ''
- sophia-ananiadou
venue: 'in: Neurocomputing, 413(431-443)'
venueShort: 'in: Neurocomputing'
venueType: journal
year: 2020
doi: http://dx.doi.org/10.1016/j.neucom.2020.06.070
url: https://www.sciencedirect.com/science/article/abs/pii/S0925231220310584?via=ihub
aigaionId: 478
pubType: Article
bibtexKey: tran:2020b
pages: 431-443
keywords: []
topics:
- entity recognition
- raw text
abstract: Most deep language understanding models depend only on word representations, which are mainly based on language modelling derived from a large amount of raw text. These models encode distributional knowledge without considering syntactic structural information, although several studies have shown benefits of including such information. Therefore, we propose new syntactically-informed word representations (SIWRs), which allow us to enrich the pre-trained word representations with syntactic information without training language models from scratch. To obtain SIWRs, a graph-based neural model is built on top of either static or contextualised word representations such as GloVe, ELMo and BERT. The model is first pre-trained with only a relatively modest amount of task-independent data that are automatically annotated using existing syntactic tools. SIWRs are then obtained by applying the model to downstream task data and extracting the intermediate word representations. We finally replace word representations in downstream models with SIWRs for applications. We evaluate SIWRs on three information extraction tasks, namely nested named entity recognition (NER), binary and n-ary relation extractions (REs). The results demonstrate that our SIWRs yield performance gains over the base representations in these NLP tasks with 3–9% relative error reduction. Our SIWRs also perform better than fine-tuning BERT in binary RE. We also conduct extensive experiments to analyse the proposed method.
---
