import pandas as pd

def backtest(portfolio, cost=0.001):
    portfolio = portfolio.copy()

    portfolio["gross"] = portfolio["weight"] * portfolio["fwd_return"]
    portfolio["turnover"] = portfolio.groupby("asset")["weight"].diff().abs().fillna(0)
    portfolio["cost"] = portfolio["turnover"] * cost

    portfolio["net"] = portfolio["gross"] - portfolio["cost"]

    return portfolio.groupby("date")["net"].mean()