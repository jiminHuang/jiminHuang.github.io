---
title: Global information-aware argument mining based on a top-down multi-turn QA model
authors:
- Liu, B
- Schlegel, V.
- Thompson, P.
- Batista-Navarro, R.
- Ananiadou, S.
authorSlugs:
- ''
- ''
- paul-thompson
- ''
- sophia-ananiadou
venue: 'in: Information Processing & Management, 60:5(103445)'
venueShort: Information Processing
venueType: journal
year: 2023
doi: http://dx.doi.org/10.1016/j.ipm.2023.103445
url: https://www.sciencedirect.com/science/article/pii/S0306457323001826?via%3Dihub
aigaionId: 555
pubType: Article
bibtexKey: liu:2023b
pages: '103445'
keywords: []
abstract: 'Argument mining (AM) aims to automatically generate a graph that represents the argument structure of a document. Most previous AM models only pay attention to a single argument component (AC) to classify the type of the AC or a pair of ACs to identify and classify the argumentative relation (AR) between the two ACs. These models ignore the impact of global argument structure of the documents, which is important, especially in some highly structured genres such as scientific papers, where the process of argumentation is relatively fixed. Inspired by this, we propose a novel two-stage model which leverages global structure information to support AM. The first stage uses a multi-turn question-answering model to incrementally generate an initial argumentative graph that identifies relations among ACs. At each turn, all ACs related to the query AC are generated simultaneously, such that the sibling global information between the answer ACs is considered. In addition, the partially constructed graph is used as global structure information to support the extension of the graph with additional ACs. After the whole initial graph structure has been determined, the second stage assigns semantic types to both the ACs and ARs among them, leveraging information from this initial graph as global structure information. We test the proposed methods on two scientific datasets (one is the AbstRCT dataset including 659 abstracts about cancer research and the other is the SciARG dataset that consists of 225 computer linguistic abstracts and 285 biomedical abstracts) and a student essay dataset PE with 402 essays. Our experiments show that our model improves the state-of-the-art performance on two scientific datasets for different AM subtasks, with average improvements of 1%, 2.41%, 1.1% for the ACC, ARI and ARC task respectively on the AbstRCT dataset, and 2.36%, 1.84%, 8.87% for the ACC, ARI and ARC task on the SciARG dataset. Our model also achieves comparative results on the PE datasets: 87.7% of F1 scores for the ACC task, 81.4% for the ARI task and 78.8% for the ARC task.'
paperTerms:
- argument structure
- AM models
- single argument component
- argumentative relation
- global argument structure
- scientific papers
- two-stage model
- global structure information
- multi-turn question-answering model
- initial argumentative graph
---
