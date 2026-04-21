import os
import pandas as pd
import yaml

from src.predict import predict
from src.backtest import backtest
from src.evaluate import sharpe, max_drawdown, cagr

config = yaml.safe_load(open("config.yaml"))

os.makedirs("outputs/backtests", exist_ok=True)
os.makedirs("outputs/metrics", exist_ok=True)

df = predict()

# NEW IDEA: quantile-based portfolio
def quantile_portfolio(df, n_quantiles=5):
    portfolios = []

    for date, g in df.groupby("date"):
        g["quantile"] = pd.qcut(g["score"], n_quantiles, labels=False)

        long = g[g["quantile"] == n_quantiles - 1]
        short = g[g["quantile"] == 0]

        long["weight"] = 1 / len(long)
        short["weight"] = -1 / len(short)

        portfolios.append(pd.concat([long, short]))

    return pd.concat(portfolios)

portfolio = quantile_portfolio(df)

returns = backtest(portfolio, config["portfolio"]["transaction_cost"])

metrics = {
    "sharpe": sharpe(returns),
    "max_drawdown": max_drawdown(returns),
    "cagr": cagr(returns)
}

pd.DataFrame([metrics]).to_csv("outputs/metrics/metrics_exp002.csv", index=False)

print("EXP002:", metrics)

