from lanastance.structure import structure_features


def test_structure_features_returns_expected_keys():
    text = """Hello hello
    This is a test
    Hello hello"""

    features = structure_features(text)

    assert isinstance(features, dict)
    assert "repetition_rate" in features
    assert "lexical_entropy" in features
    assert "line_end_similarity" in features
