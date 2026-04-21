import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("outputs/backtests/returns.csv", parse_dates=["date"])

df["equity"] = (1 + df["return"]).cumprod()

plt.figure(figsize=(10,5))
plt.plot(df["date"], df["equity"])
plt.title("Equity Curve")
plt.xlabel("Date")
plt.ylabel("Portfolio Value")
plt.grid()

plt.savefig("outputs/backtests/equity_curve.png")
plt.show()