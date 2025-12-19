import pandas as pd
from lanastance.clustering import kmeans_song_clustering


def test_kmeans_clustering_runs():
    df = pd.DataFrame({
        "song": ["a", "b", "c", "d"],
        "repetition_rate": [0.1, 0.2, 0.15, 0.3],
        "lexical_entropy": [5.0, 5.1, 4.9, 5.2],
        "first_person_rate": [50, 60, 55, 65],
    })

    labels = kmeans_song_clustering(df, n_clusters=2)

    assert len(labels) == len(df)
    assert labels.nunique() == 2
