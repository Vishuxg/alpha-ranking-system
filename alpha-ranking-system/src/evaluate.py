import numpy as np
import pandas as pd

def sharpe(returns):
    return np.mean(returns) / np.std(returns) * np.sqrt(252)

def max_drawdown(returns):
    cum = (1 + returns).cumprod()
    peak = np.maximum.accumulate(cum)
    dd = (cum - peak) / peak
    return dd.min()

def cagr(returns):
    total = (1 + returns).prod()
    years = len(returns) / 252
    return total ** (1 / years) - 1


def information_coefficient(df):
    ic_values = []

    for date, g in df.groupby("date"):
        if g["score"].nunique() > 1:
            ic = g["score"].corr(g["fwd_return"], method="spearman")
            ic_values.append(ic)

    return pd.Series(ic_values).mean()