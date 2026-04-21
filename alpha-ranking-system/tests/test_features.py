def test_feature_exists():
    import pandas as pd
    from src.feature_engineering import add_features

    df = pd.DataFrame({
        "date": ["2020-01-01"]*10,
        "asset": ["A"]*10,
        "close": range(10),
        "volume": range(10)
    })

    df = add_features(df)

    assert "momentum_5" in df.columns