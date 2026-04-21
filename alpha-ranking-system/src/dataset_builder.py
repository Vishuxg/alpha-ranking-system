def build_dataset(df):
    df = df.copy()

    # ✅ Only drop rows where target is missing
    df = df.dropna(subset=["target"])

    # ✅ Define features explicitly
    features = [
        "momentum_5",
        "momentum_10",
        "momentum_20",
        "volatility_10"
    ]

    # ✅ Fill feature NaNs instead of dropping everything
    df[features] = df[features].fillna(0)

    # Debug
    print("Columns:", df.columns.tolist())
    print("Dataset size after cleaning:", df.shape)

    X = df[features]
    y = df["target"]
    group = df.groupby("date").size().values

    print("Final X shape:", X.shape)

    return X, y, group, df