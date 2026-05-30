---
title: Disentangled Variational Autoencoder for Emotion Recognition in Conversations
authors:
- Yang, K
- Zhang, T.
- Ananiadou, S.
authorSlugs:
- ''
- tianlin-zhang-alum-2024
- sophia-ananiadou
venue: 'in: IEEE Transactions on Affective Computing(1-12)'
venueShort: 'in: IEEE Transactions on Affective Computing(1-12)'
venueType: journal
year: 2023
doi: http://dx.doi.org/10.1109/TAFFC.2023.3280038
url: https://ieeexplore.ieee.org/abstract/document/10135132
aigaionId: 551
pubType: Article
bibtexKey: yang:2023d
pages: 1-12
keywords: []
abstract: In Emotion Recognition in Conversations (ERC), the emotions of target utterances are closely dependent on their context. Therefore, existing works train the model to generate the response of the target utterance, which aims to recognise emotions leveraging contextual information. However, adjacent response generation ignores long-range dependencies and provides limited affective information in many cases. In addition, most ERC models learn a unified distributed representation for each utterance, which lacks interpretability and robustness. To address these issues, we propose a <bold xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xlink="http://www.w3.org/1999/xlink">VAD</b> -disentangled <bold xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xlink="http://www.w3.org/1999/xlink">V</b> ariational <bold xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xlink="http://www.w3.org/1999/xlink">A</b> uto <bold xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xlink="http://www.w3.org/1999/xlink">E</b> ncoder (VAD-VAE), which first introduces a target utterance reconstruction task based on Variational Autoencoder, then disentangles three affect representations Valence-Arousal-Dominance (VAD) from the latent space. We also enhance the disentangled representations by introducing VAD supervision signals from a sentiment lexicon and minimising the mutual information between VAD distributions. Experiments show that VAD-VAE outperforms the state-of-the-art model on two datasets. Further analysis proves the effectiveness of each proposed module and the quality of disentangled VAD representations. The code is available at <uri xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xlink="http://www.w3.org/1999/xlink">https://github.com/SteveKGYang/VAD-VAE</uri> .
---
