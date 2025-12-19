
"""
Preprocessing and feature aggregation utilities.
"""

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

    return features
