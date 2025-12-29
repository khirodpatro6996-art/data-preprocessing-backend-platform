from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
import pandas as pd

from app.services.cleaning import clean_dataset
from app.services.feature_engineering import feature_engineer_dataset
from app.services.profiling import profile_dataset
from app.services.data_dictionary import generate_data_dictionary
from app.utils.file_handler import save_raw, save_processed

router = APIRouter()

@router.post("/preprocess")
async def preprocess(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)

    save_raw(df)

    profile_before = profile_dataset(df)

    cleaned_df, cleaning_summary = clean_dataset(df)
    final_df, fe_summary = feature_engineer_dataset(cleaned_df)

    save_processed(final_df)

    data_dictionary = generate_data_dictionary(final_df)

    return {
        "rows_before": profile_before["num_rows"],
        "rows_after": final_df.shape[0],
        "columns_before": profile_before["num_columns"],
        "columns_after": final_df.shape[1],
        "preview": final_df.head(5).to_dict(orient="records"),
        "columns": list(final_df.columns),
        "cleaning_summary": cleaning_summary,
        "feature_engineering_summary": fe_summary,
        "profiling": profile_before,
        "data_dictionary": data_dictionary.head(10).to_dict(orient="records")
    }


@router.get("/download/cleaned")
def download_cleaned():
    return FileResponse(
        "data/processed/cleaned_dataset.csv",
        filename="cleaned_dataset.csv"
    )
