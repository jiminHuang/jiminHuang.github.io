---
title: Cluster-Level Contrastive Learning for Emotion Recognition in Conversations
authors:
- Yang, K
- Zhang, T.
- Alhuzali, H.
- Ananiadou, S.
authorSlugs:
- ''
- tianlin-zhang-alum-2024
- hassan-alhuzali-alum-2021
- sophia-ananiadou
venue: 'in: IEEE Transactions on Affective Computing(1-12)'
venueShort: 'in: IEEE Transactions on Affective Computing(1-12)'
venueType: journal
year: 2023
doi: http://dx.doi.org/10.1109/TAFFC.2023.3243463
url: https://ieeexplore.ieee.org/abstract/document/10040720
aigaionId: 523
pubType: Article
bibtexKey: yang:2023
pages: 1-12
keywords: []
abstract: 'A key challenge for Emotion Recognition in Conversations (ERC) is to distinguish semantically similar emotions. Some works utilise Supervised Contrastive Learning (SCL) which uses categorical emotion labels as supervision signals and contrasts in high-dimensional semantic space. However, categorical labels fail to provide quantitative information between emotions. ERC is also not equally dependent on all embedded features in the semantic space, which makes the high-dimensional SCL inefficient. To address these issues, we propose a novel low-dimensional Supervised Cluster-level Contrastive Learning (SCCL) method, which first reduces the high-dimensional SCL space to a three-dimensional affect representation space Valence-Arousal-Dominance (VAD), then performs cluster-level contrastive learning to incorporate measurable emotion prototypes. To help modelling the dialogue and enriching the context, we leverage the pre-trained knowledge adapters to infuse linguistic and factual knowledge. Experiments show that our method achieves new state-of-the-art results with <inline-formula><tex-math notation="LaTeX">$69.81\%$</tex-math></inline-formula> on IEMOCAP, <inline-formula><tex-math notation="LaTeX">$65.7\%$</tex-math></inline-formula> on MELD, and <inline-formula><tex-math notation="LaTeX">$62.51\%$</tex-math></inline-formula> on DailyDialog datasets. The analysis also proves that the VAD space is not only suitable for ERC but also interpretable, with VAD prototypes enhancing its performance and stabilising the training of SCCL. In addition, the pre-trained knowledge adapters benefit the performance of the utterance encoder and SCCL. Our code is available at: <uri>https://github.com/SteveKGYang/SCCL</uri>'
---
