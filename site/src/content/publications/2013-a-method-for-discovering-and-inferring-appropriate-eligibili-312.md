---
title: A method for discovering and inferring appropriate eligibility criteria in clinical trial protocols without labeled data
authors:
- Restificar, A.
- Korkontzelos, I.
- Ananiadou, S.
authorSlugs:
- ''
- ''
- sophia-ananiadou
venue: 'in: BMC Medical Informatics and Decision Making, 13:Suppl 1(S6)'
venueShort: BMC
venueType: journal
year: 2013
doi: http://dx.doi.org/10.1186/1472-6947-13-S1-S6
url: http://www.biomedcentral.com/1472-6947/13/S1/S6
aigaionId: 312
pubType: Article
bibtexKey: 'Journal:'
pages: S6
keywords: []
abstract: 'BACKGROUND: We consider the user task of designing clinical trial protocols and propose a method that discovers and outputs the most appropriate eligibility criteria from a potentially huge set of candidates. Each document d in our collection D is a clinical trial protocol which itself contains a set of eligibility criteria. Given a small set of sample documentsD'',|D''|≪|D|, a user has initially identified as relevant e.g., via a user query interface, our scoring method automatically suggests eligibility criteria from D, D ⊃ D'', by ranking them according to how appropriate they are to the clinical trial protocol currently being designed. The appropriateness is measured by the degree to which they are consistent with the user-supplied sample documents D''. METHOD: We propose a novel three-step method called LDALR which views documents as a mixture of latent topics. First, we infer the latent topics in the sample documents using Latent Dirichlet Allocation (LDA). Next, we use logistic regression models to compute the probability that a given candidate criterion belongs to a particular topic. Lastly, we score each criterion by computing its expected value, the probability-weighted sum of the topic proportions inferred from the set of sample documents. Intuitively, the greater the probability that a candidate criterion belongs to the topics that are dominant in the samples, the higher its expected value or score. RESULTS: Our experiments have shown that LDALR is 8 and 9 times better (resp., for inclusion and exclusion criteria) than randomly choosing from a set of candidates obtained from relevant documents. In user simulation experiments using LDALR, we were able to automatically construct eligibility criteria that are on the average 75% and 70% (resp., for inclusion and exclusion criteria) similar to the correct eligibility criteria. CONCLUSIONS: We have proposed LDALR, a practical method for discovering and inferring appropriate eligibility criteria in clinical trial protocols without labeled data. Results from our experiments suggest that LDALR models can be used to effectively find appropriate eligibility criteria from a large repository of clinical trial protocols.'
---
