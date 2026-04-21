import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import os

np.random.seed(42)

def generate_price_series(n_days, start_price, factor):
    prices = [start_price]

    for i in range(1, n_days):
        # persistent alpha signal
        drift = factor * 0.005

        noise = np.random.normal(0, 0.02)

        new_price = prices[-1] * (1 + drift + noise)
        prices.append(max(new_price, 1))

    return np.array(prices)


def generate_ohlcv(prices):
    close = prices
    open_ = close * (1 + np.random.normal(0, 0.002, len(close)))

    high = np.maximum(open_, close) * (1 + np.random.uniform(0, 0.01, len(close)))
    low = np.minimum(open_, close) * (1 - np.random.uniform(0, 0.01, len(close)))

    volume = np.random.randint(1e5, 1e6, len(close))

    return open_, high, low, close, volume


def generate_dataset(
    n_assets=100,
    n_days=2000,
    start_date="2015-01-01"
):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")

    all_data = []

    for i in range(n_assets):
     asset_name = f"Asset_{i}"

    
    factor = np.random.uniform(-1, 1)

    start_price = np.random.uniform(20, 200)

    prices = generate_price_series(n_days, start_price, factor)

    open_, high, low, close, volume = generate_ohlcv(prices)

    for t in range(n_days):
            date = start_date + timedelta(days=t)

            all_data.append([ 
                date,
                asset_name,
                open_[t],
                high[t],
                low[t],
                close[t],
                volume[t]
            ])

    df = pd.DataFrame(all_data, columns=[
        "date", "asset", "open", "high", "low", "close", "volume"
    ])

    return df


if __name__ == "__main__":
    df = generate_dataset(
        n_assets=100,
        n_days=2000
    )

    os.makedirs("data/raw", exist_ok=True)

    df.to_csv("data/raw/data.csv", index=False)

    print(" Synthetic data generated at data/raw/data.csv")
    print(df.head())