import numpy as np
import pickle
import streamlit as st
loaded_data = pickle.load(open('trained_model.sav','rb'))

def diabetes_prediction(input_data):
    input_np = np.array(input_data)
    input_reshaped = input_np.reshape(1,-1)
    prediction = loaded_data.predict(input_reshaped)
    if prediction[0] == 0:
        return 'The person is not Diabetic'
    else:
        return 'The person is Diabetic'
    
def main():
    st.title("Diabetes Prediction Web App")
    Pregnancies = st.number_input("How many pregnancies did you have?",min_value=0)
    Glucose = st.number_input("Glucose Level",min_value=0.0)
    BloodPressure = st.number_input("Blood Pressure Value ",min_value=0.0)
    SkinThickness = st.number_input("Skin Thickness ",min_value=0.0)
    Insulin = st.number_input("Insulin Level",min_value=0.0)
    BMI	= st.number_input("BMI value",min_value=0.0)
    DiabetesPedigreeFunction = st.number_input("Diabetes Peidgree Function",min_value=0.0)
    Age = st.number_input("Your age ",min_value=1)

    diagnosis = ''
    if st.button("Diabetes test result"):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    
    st.success(diagnosis)

if __name__ == '__main__':
    main()