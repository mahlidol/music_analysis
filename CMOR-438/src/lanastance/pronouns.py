"""
Pronoun-based orientation features.

This module computes pronoun usage rates as signals of
linguistic orientation, not as direct measures of intimacy
or confession.
"""

import re
from typing import Dict

# ----------------------------
# Pronoun sets
# ----------------------------

FIRST_PERSON = {
    "i", "me", "my", "mine",
    "i'm", "i’ve", "i've", "i’ll", "i'd"
}

SECOND_PERSON = {
    "you", "your", "yours",
    "you're", "you’ve", "you've", "you’ll", "you'd"
}

THIRD_PERSON = {
    "he", "him", "his",
    "she", "her", "hers",
    "they", "them", "their", "theirs"
}

# Simple word tokenizer
TOKEN_PATTERN = re.compile(r"\b\w+'?\w*\b")


# ----------------------------
# Core function
# ----------------------------

def pronoun_rates(text: str) -> Dict[str, float]:
    """
    Compute pronoun-based orientation rates for a song.

    Parameters
    ----------
    text : str
        Full song lyric text.

    Returns
    -------
    dict
        Dictionary containing pronoun rates per 1,000 tokens.
    """
    if not isinstance(text, str):
        raise ValueError("Input text must be a string.")

    tokens = TOKEN_PATTERN.findall(text.lower())
    total_tokens = len(tokens)

    if total_tokens == 0:
        return {
            "first_person_rate": 0.0,
            "second_person_rate": 0.0,
            "third_person_rate": 0.0
        }

    first = 0
    second = 0
    third = 0

    for tok in tokens:
        if tok in FIRST_PERSON:
            first += 1
        elif tok in SECOND_PERSON:
            second += 1
        elif tok in THIRD_PERSON:
            third += 1

    scale = 1000 / total_tokens

    return {
        "first_person_rate": round(first * scale, 3),
        "second_person_rate": round(second * scale, 3),
        "third_person_rate": round(third * scale, 3)
    }

