# AI-Based Disease Prediction System

A machine learning-based web application to predict multiple diseases (e.g., diabetes, heart disease) from user-provided symptoms. Built with Python, Flask, and ML algorithms.

## Features
- Predicts multiple diseases using Logistic Regression, Random Forest, and SVM.
- High accuracy with preprocessing, feature selection, and hyperparameter tuning.
- Real-time web interface for easy interaction.

## Technologies
Python | Flask | Scikit-learn | Pandas | NumPy | HTML/CSS

## Project Structure
- `src/` - Python scripts for ML models and Flask app
- `models/` - Saved trained ML models
- `data/` - Sample datasets
- `templates/` - HTML files
- `static/` - CSS/JS

## Setup
```bash
git clone <repo-url>
cd ai-disease-prediction
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python src/app.py
