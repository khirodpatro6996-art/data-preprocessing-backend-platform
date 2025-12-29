def profile_dataset(df):
    return {
        "num_rows": df.shape[0],
        "num_columns": df.shape[1],
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isna().sum().to_dict(),
        "duplicate_rows": int(df.duplicated().sum())
    }
