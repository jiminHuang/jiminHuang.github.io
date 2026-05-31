---
title: 'GENA: A knowledge graph for nutrition and mental health'
authors:
- Dang, L. D.
- Phan, U. T. P.
- Nguyen, N. T. H.
authorSlugs:
- ''
- ''
- ''
venue: 'in: Journal of Biomedical Informatics, 145(10446)'
venueShort: JBI
venueType: journal
year: 2023
doi: http://dx.doi.org/10.1016/j.jbi.2023.104460
url: https://www.sciencedirect.com/science/article/pii/S1532046423001818
aigaionId: 545
pubType: Article
bibtexKey: DANG2023104460
pages: '10446'
keywords: []
topics:
- entity recognition
abstract: While a large number of knowledge graphs have previously been developed by automatically extracting and structuring knowledge from literature, there is currently no such knowledge graph that encodes relationships between food, biochemicals and mental illnesses, even though a large amount of knowledge about these relationships is available in the form of unstructured text in biomedical literature articles. To address this limitation, this article describes the development of GENA - (Graph of mEntal-health and Nutrition Association), a knowledge graph that represents relations between nutrition and mental health, extracted from biomedical abstracts. GENA is constructed from PubMed abstracts that contain keywords relating to chemicals, food, and health. A hybrid named entity recognition (NER) model is firstly applied to these abstracts to identify various entities of interest. Subsequently, a deep syntax-based relation extraction model is used to detect binary relations between the identified entities. Finally, the resulting relations are used to populate the GENA knowledge graph, whose relationships can be accessed in an intuitive and interpretable manner using the Neo4J Database Management System. To evaluate the reliability of GENA, two annotators manually assessed a subset of the extracted relations. The evaluation results show that our methods obtain high precision for the NER task and acceptable precision and relative recall for the relation extraction task. GENA consists of 43,367 relationships that encode information about nutrition and health, of which 94.04% are new relations that are not present in existing ontologies of food and diseases. GENA is constructed based on scientific principles, and has the potential to be used within further applications to contribute towards scientific research within the domain. It is a pioneering knowledge graph in nutrition and mental health, containing a diverse range of relationship types. All of our source code and results are publicly available at https://github.com/ddlinh/gena-db.
paperTerms:
- knowledge graph
- mental health
- knowledge graphs
- mental illnesses
- unstructured text
- biomedical literature articles
- Nutrition Association
- entity recognition
- binary relations
- GENA knowledge graph
---
