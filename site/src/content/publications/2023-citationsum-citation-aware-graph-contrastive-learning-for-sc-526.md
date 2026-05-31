---
title: 'CitationSum: Citation-aware Graph Contrastive Learning for Scientific Paper Summarization'
authors:
- Luo, Z.
- Xie, Q.
- Ananiadou, S.
authorSlugs:
- zheheng-luo-alum-2025
- qianqian-xie
- sophia-ananiadou
venue: Proceedings of the ACM Web Conference, pages 1843–1852
venueShort: Proceedings of the ACM Web Conference
venueType: conference
year: 2023
doi: http://dx.doi.org/10.1145/3543507.3583505
url: https://dl.acm.org/doi/10.1145/3543507.3583505
aigaionId: 526
pubType: Inproceedings
bibtexKey: luo:2023
pages: 1843–1852
keywords: []
abstract: Citation graphs can be helpful in generating high-quality summaries of scientific papers, where references of a scientific paper and their correlations can provide additional knowledge for contextualising its background and main contributions. Despite the promising contributions of citation graphs, it is still challenging to incorporate them into summarization tasks. This is due to the difficulty of accurately identifying and leveraging relevant content in references for a source paper, as well as capturing their correlations of different intensities. Existing methods either ignore references or utilize only abstracts indiscriminately from them, failing to tackle the challenge mentioned above. To fill that gap, we propose a novel citation-aware scientific paper summarization framework based on the citation graph, able to accurately locate and incorporate the salient contents from references, as well as capture varying relevance between source papers and their references. Specifically, we first build a domain-specific dataset PubMedCite with about 192K biomedical scientific papers and a large citation graph preserving 917K citation relationships between them. It is characterized by preserving the salient contents extracted from full texts of references, and the weighted correlation between the salient contents of references and the source paper. Based on it, we design a self-supervised citation-aware summarization framework (CitationSum) with graph contrastive learning, which boosts the summarization generation by efficiently fusing the salient information in references with source paper contents under the guidance of their correlations. Experimental results show that our model outperforms the state-of-the-art methods, due to efficiently leveraging the information of references and citation correlations.
topics:
- Language Models
- Computer Science
- full text
- Sophia Ananiadou
- Paul Thompson
- language models
- rich information
paperTerms:
- Scientific Paper Summarization
- Zheheng Luo
- zheheng.luo @ postgrad.manchester.ac.uk
- Qianqian Xie
- qianqian.xie @ manchester.ac.uk
- Sophia Ananiadou
- Sophia.Ananiadou @ manchester.ac.uk
- Citation graphs
- high-quality sum-
- scientific papers
---
