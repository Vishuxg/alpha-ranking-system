import os
import pandas as pd
import yaml

from src.predict import predict
from src.portfolio import construct_portfolio
from src.backtest import backtest
from src.evaluate import sharpe, max_drawdown, cagr

# Load config
config = yaml.safe_load(open("config.yaml"))

# Ensure output folders exist
os.makedirs("outputs/predictions", exist_ok=True)
os.makedirs("outputs/backtests", exist_ok=True)
os.makedirs("outputs/metrics", exist_ok=True)

# 1. Predict
df = predict()

# SAVE predictions
df.to_csv("outputs/predictions/predictions.csv", index=False)

# 2. Portfolio
portfolio = construct_portfolio(df, config["portfolio"]["top_k"])

# 3. Backtest
returns = backtest(portfolio, config["portfolio"]["transaction_cost"])

# SAVE backtest returns
returns_df = returns.reset_index()
returns_df.columns = ["date", "return"]
returns_df.to_csv("outputs/backtests/returns.csv", index=False)

# 4. Metrics
metrics = {
    "sharpe": sharpe(returns),
    "max_drawdown": max_drawdown(returns),
    "cagr": cagr(returns)
}

# SAVE metrics
pd.DataFrame([metrics]).to_csv("outputs/metrics/metrics.csv", index=False)

# Print
print(metrics)

