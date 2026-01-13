# AI-Based Multiple Disease Prediction System

A production-oriented machine learning application designed to predict multiple diseases such as **Diabetes** and **Heart Disease** using patient symptom data.  
This project demonstrates the complete lifecycle of an ML system — from data preprocessing and model training to deployment via a web-based interface.

---

## Overview

The AI-Based Multiple Disease Prediction System provides an intelligent decision-support tool that enables early-stage disease risk assessment.  
The application processes user inputs, applies trained machine learning models, and returns real-time predictions through a Flask-powered web interface.

This project was developed as part of academic work at **SRM Institute of Science and Technology** with an emphasis on industry best practices.

---

## Key Features

- End-to-end machine learning pipeline implementation  
- Multi-model training and performance comparison  
- Optimized data preprocessing and feature engineering  
- Real-time predictions via a web application  
- Clean, maintainable, and extensible codebase  

---

## Technology Stack

- **Language:** Python  
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

Model selection was based on accuracy, precision, recall, and overall reliability.

---

## System Workflow

1. User submits health-related input parameters  
2. Input data undergoes preprocessing and normalization  
3. Trained machine learning models analyze the data  
4. Disease prediction is generated  
5. Results are displayed instantly through the web interface  

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

