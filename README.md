
#  Automated Data Preprocessing Platform (Backend-Driven)

A **production-style data preprocessing platform** that automates dataset cleaning, profiling, feature engineering, and data dictionary generation using a **FastAPI backend** and a **Streamlit frontend**.

This project is designed to reflect **real-world analytics and ML preprocessing workflows**, with a clear separation between **UI and data logic**.

---

## 🔗 Live Demo

* **(Live App):**
  https://data-preprocessing-backend-platform-snsv5p275mzpxgh7dtousp.streamlit.app/

##  Key Features

### 🔹 Backend-Driven Data Processing

* All data cleaning, feature engineering, profiling, and dictionary generation are handled by a **FastAPI backend**
* Frontend acts only as a **thin UI layer**

### 🔹 Automated Data Cleaning

* Duplicate removal
* Snake_case column standardization
* Type inference & numeric conversion
* Missing value handling (median / mode)
* Constant column removal
* Optional outlier removal (IQR-based)

### 🔹 Feature Engineering

* Safe one-hot encoding for categorical features
* Automatic identifier column detection
* Original features preserved (additive engineering)
* Schema-safe transformations

### 🔹 Dataset Profiling

* Row & column counts
* Data types
* Missing value summary
* Duplicate detection

### 🔹 Data Dictionary Generation

* Column name
* Data type
* Non-null & missing counts
* Unique values
* Sample values
* Downloadable as CSV

### 🔹 Deployment-Ready Architecture

* Backend deployed on **Render**
* Frontend deployed on **Streamlit Cloud**
* Git-safe handling of user-uploaded data

---

## Why Backend-First Design?

Instead of performing data processing directly in Streamlit, this project uses a **dedicated backend** to:

* Improve **reusability** of preprocessing logic
* Enable **future ML model integration**
* Support **scalability and maintainability**
* Follow **industry-standard API-based architecture**


##  Architecture Overview

```
[ User Uploads CSV ]
          |
          v
[ Streamlit Frontend ]
          |
          |  (HTTP Request)
          v
[ FastAPI Backend ]
   ├── Cleaning Service
   ├── Feature Engineering Service
   ├── Profiling Service
   └── Data Dictionary Service
          |
          v
[ Processed Dataset + Metadata ]
```

##  Tech Stack

### Backend

* **FastAPI**
* **Pandas**
* **NumPy**
* **Uvicorn**

### Frontend

* **Streamlit**
* **Requests**

### Deployment

* **Render** (Backend)
* **Streamlit Cloud** (Frontend)
* **GitHub** (Version Control)

---

##  Project Structure

```
data-preprocessing-backend-platform/
│
├── backend/
│   └── data_preprocessing_backend/
│       ├── app/
│       │   ├── main.py
│       │   ├── routes/
│       │   ├── services/
│       │   └── utils/
│       ├── data/
│       │   ├── raw/
│       │   └── processed/
│       ├── requirements.txt
│       └── render.yaml
│
├── frontend/
│   └── streamlit_app/
│       ├── app.py
│       └── requirements.txt
│
├── .gitignore
└── README.md
```

##  How to Run Locally

### Backend

```bash
cd backend/data_preprocessing_backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

### Frontend

```bash
cd frontend/streamlit_app
pip install -r requirements.txt
streamlit run app.py
```

---

## Use Cases

* Preparing datasets for **EDA**
* Generating clean data for **ML pipelines**
* Creating **analysis-ready datasets**
* Teaching **data preprocessing best practices**
* Demonstrating **backend-first analytics systems**

---

## Future Enhancements

* Configurable cleaning rules via UI
* Advanced feature generation
* Column-level statistics & distributions
* Database-backed dataset storage
* ML model inference integration

---

##  Author

**Khirod Kumar Patro**
📍 Paralakhemundi, Odisha
📧 [khirodkumarpatro03@gmail.com](mailto:khirodkumarpatro03@gmail.com)


