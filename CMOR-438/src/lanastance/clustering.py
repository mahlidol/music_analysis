from sklearn.cluster import KMeans
import pandas as pd


def kmeans_song_clustering(
    df: pd.DataFrame,
    feature_cols=None,
    n_clusters: int = 2,
    random_state: int = 42
):
    """
    Cluster songs using k-means in feature space.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing song-level features.
    feature_cols : list
        Columns to use as features.
    n_clusters : int
        Number of clusters.
    random_state : int
        Random seed for reproducibility.

    Returns
    -------
    pd.Series
        Cluster label for each song.
    """
    if feature_cols is None:
        feature_cols = [
            "repetition_rate",
            "lexical_entropy",
            "first_person_rate",
        ]

    X = df[feature_cols].values

    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    labels = kmeans.fit_predict(X)

    return pd.Series(labels, index=df.index)
