"""
Structure and predictability features.

These features capture repetition, return, and linguistic
constraint without claiming to measure poetic quality.
"""

import re
import math
from collections import Counter
from typing import Dict, List


TOKEN_PATTERN = re.compile(r"\b\w+'?\w*\b")


def _get_lines(text: str) -> List[str]:
    """Split lyrics into non-empty lines."""
    lines = [line.strip().lower() for line in text.splitlines()]
    return [line for line in lines if line]


def _tokenize(text: str) -> List[str]:
    """Tokenize text into lowercase word tokens."""
    return TOKEN_PATTERN.findall(text.lower())


def repetition_rate(lines: List[str]) -> float:
    """Proportion of repeated lines."""
    if not lines:
        return 0.0
    counts = Counter(lines)
    repeated = sum(count - 1 for count in counts.values() if count > 1)
    return repeated / len(lines)


def lexical_entropy(tokens: List[str]) -> float:
    """Shannon entropy of token distribution."""
    if not tokens:
        return 0.0

    counts = Counter(tokens)
    total = len(tokens)
    entropy = 0.0

    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)

    return entropy


def line_end_similarity(lines: List[str], n_chars: int = 3) -> float:
    """Approximate rhyme via line-ending overlap."""
    if len(lines) < 2:
        return 0.0

    endings = [line[-n_chars:] for line in lines if len(line) >= n_chars]
    counts = Counter(endings)
    matches = sum(count - 1 for count in counts.values() if count > 1)
    return matches / len(endings)


def structure_features(text: str) -> Dict[str, float]:
    """
    Compute structure and predictability features for a song.
    """
    if not isinstance(text, str):
        raise ValueError("Input text must be a string.")

    lines = _get_lines(text)
    tokens = _tokenize(text)

    return {
        "repetition_rate": round(repetition_rate(lines), 4),
        "lexical_entropy": round(lexical_entropy(tokens), 4),
        "line_end_similarity": round(line_end_similarity(lines), 4),
    }
