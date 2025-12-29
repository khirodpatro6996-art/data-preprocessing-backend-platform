import streamlit as st
import requests

# =====================
# CONFIG
# =====================
BACKEND_BASE_URL = "https://data-preprocessing-backend-platform.onrender.com"
PREPROCESS_URL = f"{BACKEND_BASE_URL}/api/preprocess"
DOWNLOAD_URL = f"{BACKEND_BASE_URL}/api/download/cleaned"

st.set_page_config(page_title="Data Preprocessing Platform", layout="wide")

st.title("Automated Data Cleaning & Feature Engineering")
st.caption("All preprocessing is handled by backend services.")

uploaded_file = st.file_uploader(
    "Upload CSV dataset",
    type=["csv"]
)

if uploaded_file and st.button("Run Preprocessing"):
    with st.spinner("Processing dataset..."):
        try:
            files = {
                "file": (uploaded_file.name, uploaded_file, "text/csv")
            }

            response = requests.post(PREPROCESS_URL, files=files, timeout=120)

            if response.status_code != 200:
                st.error("Backend processing failed")
                st.stop()

            result = response.json()

        except requests.exceptions.RequestException:
            st.error("Backend service unavailable")
            st.stop()


    with st.expander("Dataset Profile"):
        st.json(result["profiling"])

    # =====================
    # RESULTS
    # =====================
    st.success("Preprocessing completed")

    col1, col2 = st.columns(2)
    col1.metric("Rows Before Preprocessing", result["rows_before"])
    col2.metric("Rows After Preprocessing", result["rows_after"])
    col3, col4 = st.columns(2)
    col3.metric("Columns Before Preprocessing", result["columns_before"])
    col4.metric("Columns After Preprocessing", result["columns_after"])

    # -------- DATA PREVIEW (THIS FIXES YOUR ISSUE) --------
    st.subheader("Processed Dataset Preview")
    st.dataframe(result["preview"])

    

    # -------- SUMMARIES --------
    with st.expander(" Cleaning Summary", expanded=True):
        st.json(result["cleaning_summary"])

    with st.expander("Feature Engineering Summary", expanded=True):
        st.json(result["feature_engineering_summary"])

    

    # -------- DOWNLOAD --------
    st.markdown("### Download Processed Dataset")
    st.markdown(f"[Download CSV]({DOWNLOAD_URL})", unsafe_allow_html=True)
