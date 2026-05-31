---
title: 'THCM-CAL: Temporal-Hierarchical Causal Modelling with Conformal Calibration for Clinical Risk Prediction'
authors:
- Zhang, X.
- Wei, Q.
- Zhu, Y.
- Wu, F.
- Ananiadou, S.
authorSlugs:
- xin-zhang
- ''
- ''
- ''
- sophia-ananiadou
venue: 'Findings of the Association for Computational Linguistics: EMNLP 2024, pages 916–928'
venueShort: EMNLP 2024
venueType: conference
year: 2025
doi: http://dx.doi.org/10.18653/v1/2025.findings-emnlp.48
url: https://aclanthology.org/2025.findings-emnlp.48/
aigaionId: 615
pubType: Inproceedings
bibtexKey: zhang:2025b
pages: 916–928
keywords: []
abstract: 'Automated clinical risk prediction from electronic health records (EHRs) demands modeling both structured diagnostic codes and unstructured narrative notes.However, most prior approaches either handle these modalities separately or rely on simplistic fusion strategies that ignore the directional, hierarchical causal interactions by which narrative observations precipitate diagnoses and propagate risk across admissions.In this paper, we propose THCM-CAL, a Temporal-Hierarchical Causal Model with Conformal Calibration.Our framework constructs a multimodal causal graph where nodes represent clinical entities from two modalities: Textual propositions extracted from notes and ICD codes mapped to textual descriptions.Through hierarchical causal discovery, THCM-CAL infers three clinically grounded interactions: intra-slice samemodality sequencing, intra-slice cross-modality triggers, and inter-slice risk propagation.To enhance prediction reliability, we extend conformal prediction to multi-label ICD coding, calibrating per-code confidence intervals under complex co-occurrences.Experimental results on MIMIC-III and MIMIC-IV demonstrate the superiority of THCM-CAL.'
topics:
- Language Models
- Sophia Ananiadou
- language models
---
