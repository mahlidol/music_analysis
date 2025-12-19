A Case Study of Lana Del Rey’s Born to Die and Norman F**ing Rockwell!

Results

This project analyzes song-level lyrics from two Lana Del Rey albums—Born to Die and Norman Fucking Rockwell!—using three classes of features: structural repetition, lexical surprise, and pronoun orientation. Rather than assuming a simple tradeoff between structure and unpredictability, the analysis examines how songs occupy a shared expressive space and how self-oriented language distributes within it.

Structure vs. Surprise

A scatter plot of repetition rate (structure) versus lexical entropy (surprise) reveals no strong linear correlation between the two features. Instead, songs cluster within a bounded region of the structure–surprise space. This suggests that lyrical language does not move freely from rigid to chaotic, but instead operates within stylistic constraints that balance return and variation.

At the album level, Born to Die exhibits greater variance in lexical entropy, including several high-entropy outliers, despite relatively higher repetition rates. In contrast, Norman Fucking Rockwell! shows tighter clustering with reduced variance, indicating greater stylistic cohesion even as repetition decreases. These results complicate the intuition that later work is necessarily more lexically unpredictable.

Album-Level Summary Statistics

Aggregated statistics reinforce these observations. While average repetition and entropy values are comparable across albums, Born to Die shows higher dispersion in lexical entropy, whereas Norman Fucking Rockwell! displays compression around its mean. This suggests a shift from lexical volatility toward consistency rather than a simple increase in randomness.

Pronoun Orientation Overlay

Overlaying first-person pronoun rates onto the structure–surprise space reveals that self-orientation does not align cleanly with either repetition or entropy alone. Highly self-referential songs tend to occupy intermediate regions of the space, rather than extremes of structure or surprise. This pattern suggests that confessional or intimate lyrical voice may emerge most strongly under moderate constraint rather than maximal unpredictability.

When album identity is reintroduced via marker shape, both albums share this tendency, though they differ in how tightly songs cluster within the space. Overall, pronoun orientation appears to function as a third, partially independent linguistic dimension rather than a direct proxy for emotional intensity or stylistic freedom.

Summary

Taken together, these results support the idea of a dynamic “sweet spot” between structure and surprise in lyrical language. Rather than trading off against one another, repetition, lexical unpredictability, and self-orientation interact in nuanced ways that shift across albums while remaining bounded by stylistic constraints.

## Machine Learning Methods

This project implements two classical machine learning algorithms
operating on engineered song-level features:

- **k-Nearest Neighbors (kNN)** is used to identify stylistically similar
  songs in feature space based on repetition, lexical entropy, and
  pronoun orientation.
- **Logistic Regression** is implemented as a supervised baseline model
  operating on the same feature representations, demonstrating how
  learned linguistic features can support classification-oriented
  modeling.

Together, these methods demonstrate how machine learning techniques
can be applied to linguistic feature representations to explore
stylistic similarity and structure in creative text.


See `notebooks/02_structure_surprise.ipynb` for all figures and analysis code.
