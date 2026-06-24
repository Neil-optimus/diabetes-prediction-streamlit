# Diabetes Prediction using Machine Learning

## Overview

This project predicts whether a person is diabetic based on medical attributes using a Logistic Regression model. A Streamlit web application is used to provide an interactive user interface for predictions.

## Technologies Used

- Python
- NumPy
- Pandas
- Scikit-Learn
- Streamlit

## Dataset

The project uses the PIMA Indians Diabetes Dataset.

## Features

- Interactive Streamlit Web App
- Real-time Predictions
- Trained Machine Learning Model
- User-friendly Interface

## Project Structure

DIABETES/
│
├── dataset/
│   └── diabetes.csv
│
├── notebook/
│   └── Diabetes_Prediction.ipynb
│
├── screenshots/
│   ├── home.png
│   ├── model_accuracy.png
│   └── prediction.png
│
├── .gitignore
├── app.py
├── README.md
├── requirements.txt
└── trained_model.sav

## Screenshots

### Home Page

![Home](screenshots/home.png)

### Prediction Result

![Prediction](screenshots/prediction.png)

### Model Performance

![Accuracy](screenshots/model_accuracy.png)

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py

## Author

Neil Kesarkar   