
from lanastance.logistic_regression import LogisticRegression


def test_logistic_regression_runs():
    X = [[0], [1], [2], [3]]
    y = [0, 0, 1, 1]

    model = LogisticRegression(lr=0.1, n_iters=500)
    model.fit(X, y)

    preds = model.predict([[0.5], [2.5]])
    assert len(preds) == 2
