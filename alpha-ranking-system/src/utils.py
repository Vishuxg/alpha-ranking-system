import os

def ensure_dirs():
    os.makedirs("outputs", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)