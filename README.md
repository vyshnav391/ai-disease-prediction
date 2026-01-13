# AI-Based Multiple Disease Prediction System

A production-oriented machine learning application designed to predict multiple diseases such as **Diabetes** and **Heart Disease** using patient symptom data.  
This project demonstrates the complete lifecycle of an ML system — from data preprocessing and model training to deployment via a web-based interface.

---

## Overview

The AI-Based Multiple Disease Prediction System serves as an intelligent decision-support tool for early-stage disease risk assessment.  
The application processes user inputs, applies trained machine learning models, and delivers real-time predictions through a Flask-powered web interface.

Developed as part of academic work at **SRM Institute of Science and Technology**, the project emphasizes industry-aligned engineering practices.

---

## Key Features

- End-to-end machine learning pipeline  
- Multiple model training and performance comparison  
- Advanced data preprocessing and feature engineering  
- Real-time prediction via a web interface  
- Clean, modular, and extensible design  

---

## Technology Stack

- **Programming Language:** Python  
- **Machine Learning:** Scikit-learn  
- **Web Framework:** Flask  
- **Data Processing:** Pandas, NumPy  
- **Frontend:** HTML, CSS  
- **Deployment:** Local / Cloud-ready  

---

## Machine Learning Models

The following algorithms were implemented and evaluated:

- Logistic Regression  
- Random Forest Classifier  
- Support Vector Machine (SVM)  

Models were compared using metrics such as accuracy, precision, recall, and robustness before final selection.

---

## System Workflow

1. User submits health-related input parameters  
2. Input data is preprocessed and normalized  
3. Trained ML models analyze the data  
4. Disease risk prediction is generated  
5. Results are displayed instantly via the web interface  

---

## Results & Performance

- Achieved high prediction accuracy through feature selection and hyperparameter tuning  
- Random Forest and SVM models demonstrated strong generalization performance  
- System delivers low-latency predictions suitable for real-time use  

---

## Installation & Execution

```bash
git clone <repository-url>
cd ai-disease-prediction
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
pip install -r requirements.txt
python app.py

