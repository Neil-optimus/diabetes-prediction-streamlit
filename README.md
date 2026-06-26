# Diabetes Prediction Web Application using SVM and Streamlit

## 🚀 Live Demo

👉 **Try the application here:**

https://diabetes-prediction-app-neil.streamlit.app/

---

## Overview

This project predicts whether a person is diabetic based on various medical attributes using a Support Vector Machine (SVM) model. The prediction system is deployed as an interactive web application using Streamlit.

---

## Technologies Used

- Python
- NumPy
- Pandas
- Scikit-Learn
- Streamlit
- Pickle

---

## Dataset

This project uses the **PIMA Indians Diabetes Dataset**, which contains several medical diagnostic measurements used to predict whether a patient has diabetes.

---

## Features

- Interactive Streamlit Web Application
- Real-time Diabetes Prediction
- Machine Learning Model (SVM)
- Clean and User-Friendly Interface
- Deployed on Streamlit Community Cloud

---

## Project Structure

```text
diabetes-prediction-streamlit/
│
├── dataset/
│   └── diabetes.csv
│
├── notebook/
│   └── Diabetes_Prediction.ipynb
│
├── screenshots/
│   ├── home.png
│   ├── prediction.png
│   └── model_accuracy.png
│
├── app.py
├── trained_model.sav
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Screenshots

### Home Page

![Home](screenshots/home.png)

### Prediction Result

![Prediction](screenshots/prediction.png)

### Model Performance

![Model Performance](screenshots/model_accuracy.png)

---

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Model Performance

- **Model:** Support Vector Machine (SVM)
- **Accuracy:** 77%

---

## Disclaimer

This project is developed for educational and demonstration purposes only. It should not be used as a substitute for professional medical advice or diagnosis.

---

## Author

**Neil Kesarkar**