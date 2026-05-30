---
title: Graph Contrastive Topic Model
authors:
- Luo, Z.
- Liu, L.
- Ananiadou, S.
- Xie, Q.
authorSlugs:
- zheheng-luo-alum-2025
- ''
- sophia-ananiadou
- qianqian-xie
venue: 'in: Expert Systems with Applications, 255:Part C(124631)'
venueShort: 'in: Expert Systems with Applications'
venueType: journal
year: 2024
doi: http://dx.doi.org/10.1016/j.eswa.2024.124631
url: https://www.sciencedirect.com/science/article/pii/S0957417424014982
aigaionId: 588
pubType: Article
bibtexKey: luo:2024d
pages: '124631'
keywords: []
abstract: Contrastive learning has recently been introduced into neural topic models (NTMs) to improve latent semantic discovery, but existing methods suffer from the sample bias problem owing to word frequency-based sampling strategy, which may result in false negative samples with similar semantics to the prototypes. We propose the novel graph contrastive neural topic model (GCTM), based on the graph-based sampling strategy, guided by the in-depth correlation and irrelevance information among documents and words. We model the input document as the document word bipartite graph (DWBG) and construct positive and negative word co-occurrence graphs (WCGs), to capture in-depth semantic correlation and irrelevance among words. Based on the DWBG and WCGs, we design the document-word information propagation (DWIP) process to perform the edge perturbation of DWBG, based on multi-hop correlations/irrelevance among documents and words. This yields the desired negative and positive samples, which are utilized for GCL together with the prototypes to improve learning document topic representations and latent topics. Experiments on several benchmark datasets demonstrate the effectiveness of our method for topic coherence and document representation learning compared with existing state-of-the-art methods.
---
