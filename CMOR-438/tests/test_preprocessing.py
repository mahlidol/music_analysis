from lanastance.preprocessing import extract_song_features


def test_extract_song_features_combines_modules():
    text = "I love you\nI love you\nI love you"

    features = extract_song_features(text)

    assert isinstance(features, dict)
    assert "repetition_rate" in features
    assert "lexical_entropy" in features
    assert "first_person_rate" in features
