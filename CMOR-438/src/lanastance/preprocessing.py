
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
    raise RuntimeError("THIS IS THE FUNCTION I EDITED")
