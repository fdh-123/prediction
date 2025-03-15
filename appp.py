import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the model
def load_model():
    try:
        with open(r"C:\Users\hp\Desktop\render-demo\model.pkl", "rb") as file:
            model = pickle.load(file)
        st.success("✅ Model loaded successfully!")
        return model
    except FileNotFoundError:
        st.error("❌ Model file not found. Please check the path.")
        return None

# Prediction function
def predict(features, model):
    prediction = model.predict([features])
    return "Approved" if prediction[0] == 1 else "Rejected"

# Streamlit UI
st.title("🏦 Loan Approval Prediction App")

# Input Fields
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", [0, 1, 2, 3])
applicant_income = st.number_input("Applicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
credit_history = st.selectbox("Credit History", [1, 0])

# Load Model
model = load_model()

if st.button("Predict Loan Status"):
    if model:
        features = [gender == "Male", married == "Yes", dependents, applicant_income, loan_amount, credit_history]
        result = predict(features, model)
        st.subheader(f"Result: {result}")

     