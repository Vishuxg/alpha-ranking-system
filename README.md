# 🧠 Alpha Ranking System

An end-to-end quantitative research pipeline for ranking assets using machine learning and constructing systematic long-short portfolios.

---

# 🚀 Overview

This project builds a **complete quant workflow**:

```text
Raw Data → Features → Labels → ML Model → Ranking → Portfolio → Backtest
```

Instead of predicting prices, the system learns:

> **Which assets will outperform others (cross-sectional ranking)**

---

# ⚙️ Full Pipeline Explained

---

## 📊 1. Data

Input format:

```
date, asset, open, high, low, close, volume
```

Data is either:

* Generated synthetically (`scripts/generate_data.py`)
* Or can be replaced with real market data

---

## ⚙️ 2. Feature Engineering (`feature_engineering.py`)

Creates signals using past data:

### Features:

* Momentum (5, 10, 20 day)
* Volatility (rolling std)
* Log returns
* Cross-sectional normalization (z-score)

Example:

```python
momentum_10 = price[t] / price[t-10] - 1
```

👉 These features describe **current market state**

---

## 🏷️ 3. Label Engineering (`label_engineering.py`)

Creates future-based labels:

```python
fwd_return = (price[t+5] / price[t]) - 1
```

Then converts to ranking:

```python
target = rank(fwd_return across assets per day)
```

👉 Model learns:

```text
Which assets outperform others (not exact returns)
```

---

## 🧱 4. Dataset Builder (`dataset_builder.py`)

* Selects features
* Handles missing values
* Builds:

```python
X → features  
y → target  
groups → number of assets per date
```

👉 Groups are required for ranking models

---

## 🤖 5. Model Training (`model.py`, `train.py`)

Uses:

👉 **LightGBM LambdaRank**

Why?

* Designed for ranking problems
* Learns relative ordering

Training:

```bash
python src/train.py
```

---

## 🔮 6. Prediction (`predict.py`)

Model outputs:

```text
Asset A → 0.82  
Asset B → 0.21  
Asset C → 0.65  
```

👉 Converted into ranking:

```text
A > C > B
```

---

## 💼 7. Portfolio Construction (`portfolio.py`)

Strategy:

* Long top-K assets
* Short bottom-K assets

Weights:

```python
long weight = +1/K
short weight = -1/K
```

👉 Market-neutral long-short portfolio

---

## 📊 8. Backtesting (`backtest.py`)

Calculates:

```python
return = weight × forward_return
```

Includes:

* Transaction costs
* Turnover calculation

Aggregates:

```python
daily_return = mean(position_returns)
```

---

## 📈 9. Evaluation (`evaluate.py`)

Metrics:

* Sharpe Ratio
* CAGR
* Max Drawdown
* Information Coefficient (IC)

---

# ▶️ How to Run

---

## 1. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 2. Generate data

```bash
python scripts/generate_data.py
```

---

## 3. Train model

```bash
python src/train.py
```

---

## 4. Run experiment

```bash
python -m experiments.exp_001.run
```

---

## 5. Plot results

```bash
python scripts/plot_equity.py
```

---

## 📁 Project Structure

```text
.
├── alpha-ranking-system/
│   ├── src/                # Core pipeline (features, model, backtest)
│   ├── experiments/        # Strategy experiments (exp_001, exp_002)
│   ├── scripts/            # Utility scripts (data generation, plotting)
│
│   ├── data/               # Data storage
│   │   ├── raw/            # Raw input data
│   │   └── processed/      # Processed datasets
│
│   ├── outputs/            # Results
│   │   ├── predictions/    # Model predictions
│   │   ├── backtests/      # Backtest results
│   │   └── metrics/        # Performance metrics
│
│   ├── config.yaml         # Configuration file
│   ├── requirements.txt    # Dependencies
│   └── README.md           # Module-level docs (optional)
│
└── README.md               # Main project documentation
```


---

# 🧠 Key Concepts

---

## 🔹 Ranking vs Prediction

❌ Predict price
❌ Predict return

✅ Rank assets (best → worst)

---

## 🔹 No Data Leakage

* Features → past only
* Labels → future only

---

## 🔹 Cross-Sectional Learning

Model learns:

```text
At a given time → which asset is better
```

---

# 🔬 Experiments

---

## exp_001

* Top-K long-short strategy

## exp_002

* Quantile-based portfolio

---

# ⚠️ Notes

* Synthetic data may not contain strong alpha
* Model performance depends heavily on feature quality
* This project focuses on **pipeline + methodology**, not guaranteed profitability

---

# 🧠 Summary

This project demonstrates:

* End-to-end ML pipeline for quant trading
* Learning-to-rank modeling
* Feature engineering for financial data
* Portfolio construction & backtesting
* Clean, modular system design

---

# 🚀 Future Improvements

* Factor models (market, sector)
* Risk-neutral portfolios
* Walk-forward training
* Feature importance analysis
* Deep learning ranking models

---

# 📌 Final Thought

> Alpha is not in the model — it is in the data and features.

---
