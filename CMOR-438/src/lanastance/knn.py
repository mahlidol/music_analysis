"""
k-Nearest Neighbors classifier.
"""

import numpy as np
from collections import Counter


class KNNClassifier:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X = np.array(X)
        self.y = np.array(y)

    def predict(self, X):
        X = np.array(X)
        predictions = []

        for x in X:
            distances = np.linalg.norm(self.X - x, axis=1)
            nearest_indices = distances.argsort()[: self.k]
            nearest_labels = self.y[nearest_indices]
            label = Counter(nearest_labels).most_common(1)[0][0]
            predictions.append(label)

        return predictions

