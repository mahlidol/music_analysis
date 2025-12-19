
"""
Preprocessing and feature aggregation utilities.
"""
from lanastance.structure import (
    phonetic_endings,
    phonetic_repetition_rate,
    phonetic_entropy,
)

from typing import Dict
from lanastance.pronouns import pronoun_rates
from lanastance.structure import structure_features


def extract_song_features(text: str) -> Dict[str, float]:
    """
    Extract all linguistic features for a single song.

    Parameters
    ----------
    text : str
        Full song lyric text.

    Returns
    -------
    dict
        Combined feature dictionary.
    """
    features = {}

    features.update(pronoun_rates(text))
    features.update(structure_features(text))

    from lanastance.structure import (
    phonetic_endings,
    phonetic_repetition_rate,
    phonetic_entropy,
    )

    endings = phonetic_endings(text)
    
    features["phonetic_repetition_rate"] = phonetic_repetition_rate(endings)
    features["phonetic_entropy"] = phonetic_entropy(endings)
    
    print("DEBUG features keys:", features.keys())

    return features
