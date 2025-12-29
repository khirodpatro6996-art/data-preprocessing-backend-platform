import pandas as pd
from app.services.cleaning import to_snake_case


def feature_engineer_dataset(cleaned_df: pd.DataFrame):
    final_df = cleaned_df.copy()
    final_df.columns = [to_snake_case(c) for c in final_df.columns]

    summary = {
        "id_columns_preserved": [],
        "engineered_categorical_features": [],
        "new_features_count": 0
    }

    # Detect ID-like columns
    id_cols = [
        c for c in final_df.select_dtypes(include="object").columns
        if final_df[c].nunique() / len(final_df) > 0.8
    ]
    summary["id_columns_preserved"] = id_cols

    # Categorical columns (excluding IDs)
    cat_cols = [
        c for c in final_df.select_dtypes(include=["object", "category"]).columns
        if c not in id_cols
    ]

    if cat_cols:
        encoded = pd.get_dummies(
            final_df[cat_cols],
            prefix=cat_cols,
            drop_first=True
        )

        encoded.columns = [to_snake_case(c) for c in encoded.columns]

        final_df = pd.concat(
            [final_df.reset_index(drop=True),
             encoded.reset_index(drop=True)],
            axis=1
        )

        summary["engineered_categorical_features"] = encoded.columns.tolist()
        summary["new_features_count"] = len(encoded.columns)

    final_df.columns = [to_snake_case(c) for c in final_df.columns]

    return final_df, summary
