import streamlit as st
import numpy as np
import joblib


# load model and scaler
model = joblib.load("heart_disease_model.pkl")
scaler = joblib.load("scale.pkl")

st.title("❤️ Heart Disease Prediction App")

st.write("Enter the patient details")

# Inputs (12 features)

male = st.selectbox("Gender (Male=1, Female=0)", [0,1])

age = st.slider("Age", 20, 80, 40)

currentSmoker = st.selectbox("Current Smoker", [0,1])

cigsPerDay = st.slider("Cigarettes Per Day", 0, 40, 5)

prevalentStroke = st.selectbox("Stroke History", [0,1])

prevalentHyp = st.selectbox("Hypertension", [0,1])

diabetes = st.selectbox("Diabetes", [0,1])

totChol = st.slider("Total Cholesterol", 100, 400, 200)

sysBP = st.slider("Systolic BP", 90, 200, 120)

diaBP = st.slider("Diastolic BP", 60, 140, 80)

BMI = st.slider("BMI", 15, 40, 25)

glucose = st.slider("Glucose Level", 60, 300, 100)


# Prediction button

if st.button("Predict"):

    data = [[male, age, currentSmoker, cigsPerDay,
             prevalentStroke, prevalentHyp, diabetes,
             totChol, sysBP, diaBP, BMI, glucose]]

    data_scaled = scaler.transform(data)

    prediction = model.predict(data_scaled)

    prob = model.predict_proba(data_scaled)

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")

    st.write("Heart Disease Probability:", round(prob[0][1]*100,2), "%")