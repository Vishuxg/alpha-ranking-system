import joblib
import pandas as pd

def predict():
    model = joblib.load("outputs/model.pkl")
    df = pd.read_csv("data/processed/test.csv", parse_dates=["date"])

    features = [c for c in df.columns if "momentum" in c or "volatility" in c]

    df["score"] = model.predict(df[features])

    return df