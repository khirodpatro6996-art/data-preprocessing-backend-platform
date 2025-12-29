import pandas as pd
import numpy as np
import re


def to_snake_case(col: str) -> str:
    col = col.strip()
    col = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", col)
    col = re.sub(r"[^a-zA-Z0-9]+", "_", col)
    col = re.sub(r"_+", "_", col)
    return col.lower().strip("_")


def clean_dataset(df: pd.DataFrame, remove_outliers: bool = False):
    df = df.copy()

    summary = {
        "initial_rows": df.shape[0],
        "initial_columns": df.shape[1],
        "rows_removed": 0,
        "columns_dropped": [],
        "missing_values_handled": [],
        "outliers_removed": False,
        "final_rows": None,
        "final_columns": None
    }

    # 1. Remove duplicates
    dupes = df.duplicated().sum()
    df = df.drop_duplicates()
    summary["rows_removed"] = int(dupes)

    # 2. Force snake_case
    df.columns = [to_snake_case(c) for c in df.columns]

    # 3. Trim strings
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype(str).str.strip()

    # 4. Convert numeric-like strings
    for col in df.select_dtypes(include="object").columns:
        converted = pd.to_numeric(df[col], errors="coerce")
        if converted.notna().sum() >= 0.8 * len(df):
            df[col] = converted

    # 5. Handle missing values
    for col in df.columns:
        if df[col].isna().sum() == 0:
            continue

        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].median())
            summary["missing_values_handled"].append(f"{col} → median")
        else:
            df[col] = df[col].fillna(df[col].mode().iloc[0])
            summary["missing_values_handled"].append(f"{col} → mode")

    # 6. Drop constant columns
    constant_cols = [c for c in df.columns if df[c].nunique(dropna=False) <= 1]
    if constant_cols:
        df = df.drop(columns=constant_cols)
        summary["columns_dropped"].extend(constant_cols)

    # 7. Optional outlier removal
    if remove_outliers:
        for col in df.select_dtypes(include=np.number).columns:
            Q1, Q3 = df[col].quantile([0.25, 0.75])
            IQR = Q3 - Q1
            df = df[(df[col] >= Q1 - 1.5 * IQR) &
                    (df[col] <= Q3 + 1.5 * IQR)]
        summary["outliers_removed"] = True

    summary["final_rows"] = df.shape[0]
    summary["final_columns"] = df.shape[1]

    return df, summary
