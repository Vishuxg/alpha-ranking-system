import yaml
import joblib

from data_loader import load_data
from feature_engineering import add_features
from label_engineering import add_labels
from dataset_builder import build_dataset
from model import train_model

config = yaml.safe_load(open("config.yaml"))

df = load_data(config["data"]["path"])
df = add_features(df)
df = add_labels(df)

train_df = df[df["date"] < config["train"]["train_end"]]
test_df  = df[df["date"] >= config["train"]["train_end"]]

X_train, y_train, g_train, _ = build_dataset(train_df)

model = train_model(X_train, y_train, g_train, config["model"]["params"])

joblib.dump(model, "outputs/model.pkl")

test_df.to_csv("data/processed/test.csv", index=False)

