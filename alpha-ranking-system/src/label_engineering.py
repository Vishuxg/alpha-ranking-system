import pandas as pd

def add_labels(df, horizon=5):
    df = df.copy()

    df["fwd_return"] = (
        df.groupby("asset")["close"]
        .shift(-horizon) / df["close"] - 1
    )

    # ✅ SAFE ranking (no qcut)
    df["target"] = df.groupby("date")["fwd_return"].transform(
        lambda x: x.rank(method="first")
    )

    # Drop only rows where fwd_return missing
    df = df.dropna(subset=["fwd_return"])

    df["target"] = df["target"].astype(int)

    return df