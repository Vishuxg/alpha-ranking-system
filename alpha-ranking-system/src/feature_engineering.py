import numpy as np

def add_features(df):
    df = df.copy()

    df["log_ret"] = df.groupby("asset")["close"].transform(lambda x: np.log(x).diff())

    
    for w in [5, 10, 20]:
        df[f"momentum_{w}"] = df.groupby("asset")["close"].pct_change(w)

    
    df["volatility_10"] = (
        df.groupby("asset")["log_ret"]
        .rolling(10)
        .std()
        .reset_index(level=0, drop=True)
    )

    
    df["cs_momentum"] = df.groupby("date")["momentum_10"].rank()

    
    df["mean_reversion"] = -df.groupby("date")["log_ret"].rank()

    
    df["vol_rank"] = df.groupby("date")["volatility_10"].rank()

    df["alpha_signal"] = (
    df["momentum_10"]
    - df["volatility_10"]
)

    
    cols = ["momentum_5","momentum_10","momentum_20","volatility_10",
            "cs_momentum","mean_reversion","vol_rank","alpha_signal"]

    for c in cols:
        df[c] = df.groupby("date")[c].transform(
            lambda x: (x - x.mean()) / (x.std() + 1e-9)
        )

    return df