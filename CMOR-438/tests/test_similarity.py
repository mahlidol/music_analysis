import pandas as pd
from lanastance.similarity import knn_song_similarity


def test_knn_similarity_runs():
    df = pd.DataFrame({
        "song": ["a", "b", "c"],
        "repetition_rate": [0.1, 0.2, 0.15],
        "lexical_entropy": [5.0, 5.1, 4.9],
        "first_person_rate": [50, 60, 55],
    })

    neighbors = knn_song_similarity(df, n_neighbors=2)

    assert isinstance(neighbors, dict)
    assert "a" in neighbors
    assert len(neighbors["a"]) == 1
