import pandas as pd


def generate_data_dictionary(df: pd.DataFrame):
    records = []

    for col in df.columns:
        series = df[col]
        records.append({
            "column_name": col,
            "data_type": str(series.dtype),
            "non_null_count": int(series.notna().sum()),
            "missing_count": int(series.isna().sum()),
            "unique_values": int(series.nunique(dropna=True)),
            "sample_value": (
                series.dropna().iloc[0]
                if series.notna().any()
                else None
            )
        })

    return pd.DataFrame(records)
