---
title: PHQ-aware depressive symptoms identification with similarity contrastive learning on social media
authors:
- Zhang, T.
- Yang, K
- Alhuzali, H.
- Liu, B
- Ananiadou, S.
authorSlugs:
- tianlin-zhang-alum-2024
- ''
- hassan-alhuzali-alum-2021
- ''
- sophia-ananiadou
venue: 'in: Information Processing & Management, 60:5(103417)'
venueShort: Information Processing
venueType: journal
year: 2023
doi: http://dx.doi.org/10.1016/j.ipm.2023.103417
url: https://www.sciencedirect.com/science/article/pii/S0306457323001541
aigaionId: 535
pubType: Article
bibtexKey: 'Publication status:'
pages: '103417'
keywords: []
abstract: Depressive symptoms identification on social media aims to identify posts from social media expressing symptoms of depression. This can be beneficial for developing mental health support systems and for understanding the symptoms of depression. The Patient Health Questionnaire-9 (PHQ-9) is an instrument that healthcare professionals widely use to assess and monitor symptoms of depression. However, most existing models only consider capturing semantic information from posts, without considering PHQ-9 descriptive information related to symptoms. In addition, they are not devised to capture features that are specific to each symptom, especially in the case of multi-label symptoms identification. To tackle these challenges, we present a Span-based PHQ-aware and similarity contrastive network (SpanPHQ). We first adopt a novel span-based framework casting depressive symptoms identification task as a span-prediction problem. Then, we introduce context-aware and PHQ-aware self-guided cross-attention modules to enhance the model’s ability to consider both semantic contextual information and PHQ-9 descriptive information. Besides, a similarity contrastive learning is designed to effectively utilise the label information in identifying class-specific features. Our model is evaluated on two depressive symptoms identification datasets, i.e., the D2S dataset with 1,850 Twitter posts and the PRIMATE dataset with 2,000 Reddit posts. Moreover, our model achieves competitive performance compared to existing models on both datasets, with macro-F1 of 63.22%, 68.84%, micro-F1 of 73.34%, 75.92%, weighted-F1 of 72.86%, 76.65%, JacS of 69.94%, 63.82% and HamL of 0.0665, 0.1832 on these two datasets, respectively. The ablation study further provides evidence of the effectiveness of each module we proposed. Furthermore, we include visualisations and case studies verifying the ability of our model to learn PHQ information and its superior performance over existing baselines. Our work is expected to help the future identification and analysis of depressive symptoms on social media.
---
