from lanastance.knn import KNNClassifier


def test_knn_simple():
    X = [[0], [1], [2], [3]]
    y = [0, 0, 1, 1]

    model = KNNClassifier(k=3)
    model.fit(X, y)

    preds = model.predict([[1.1], [2.9]])
    assert preds == [0, 1]

