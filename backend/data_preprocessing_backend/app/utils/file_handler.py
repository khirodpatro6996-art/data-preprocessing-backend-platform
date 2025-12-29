import os
import pandas as pd

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"

os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

def save_raw(df: pd.DataFrame):
    df.to_csv(f"{RAW_DIR}/raw.csv", index=False)

def save_processed(df: pd.DataFrame):
    df.to_csv(f"{PROCESSED_DIR}/cleaned_dataset.csv", index=False)
