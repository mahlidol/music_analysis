from sklearn.neighbors import NearestNeighbors
import pandas as pd


def knn_song_similarity(
    df: pd.DataFrame,
    feature_cols=None,
    n_neighbors: int = 3
):
    """
    Compute k-nearest neighbors between songs in feature space.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing song-level features.
    feature_cols : list
        Columns to use as features.
    n_neighbors : int
        Number of neighbors to compute.

    Returns
    -------
    dict
        Mapping from song name to list of nearest neighbor song names.
    """
    if feature_cols is None:
        feature_cols = [
            "repetition_rate",
            "lexical_entropy",
            "first_person_rate",
        ]

    X = df[feature_cols].values

    nn = NearestNeighbors(n_neighbors=n_neighbors, metric="euclidean")
    nn.fit(X)

    _, indices = nn.kneighbors(X)

    neighbors = {}
    for i, song in enumerate(df["song"]):
        neighbors[song] = df.iloc[indices[i][1:]]["song"].tolist()

    return neighbors
