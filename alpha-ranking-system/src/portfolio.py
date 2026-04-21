import pandas as pd

def construct_portfolio(df, top_k):
    portfolios = []

    for date, g in df.groupby("date"):
        g = g.sort_values("score", ascending=False)

        long = g.head(top_k).copy()
        short = g.tail(top_k).copy()

    
        long["weight"] = 1.0 / top_k
        short["weight"] = -1.0 / top_k

        portfolios.append(long)
        portfolios.append(short)

    return pd.concat(portfolios)