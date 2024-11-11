import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load the pre-trained model
model = pickle.load(open("best_model.pkl", "rb"))

# Load any preprocessing steps (e.g., LabelEncoder, StandardScaler)
scaler = pickle.load(open("scaler.pkl", "rb"))
label_encoders = pickle.load(open("label_encoders.pkl", "rb"))

# Title for the web app
st.title("Cybersecurity Attack Type Prediction")

# Input fields for the user to input the data
st.subheader("Enter the features for prediction")

# Example features (adjust to match the feature set in your model)
year = st.number_input("Year", min_value=2000, max_value=2025)
month = st.number_input("Month", min_value=1, max_value=12)
day = st.number_input("Day", min_value=1, max_value=31)
hour = st.number_input("Hour", min_value=0, max_value=23)

# Select other categorical features if any (using label encoding)
# Example feature - replace with actual columns and names from your model
category = st.selectbox("Category", ["Category1", "Category2", "Category3"])

# Collect the input data into a DataFrame
input_data = pd.DataFrame({
    'Year': [year],
    'Month': [month],
    'Day': [day],
    'Hour': [hour],
    'Category': [category]
})

# Preprocess the input data
input_data['Category'] = label_encoders['Category'].transform(input_data['Category'])
input_data = scaler.transform(input_data)

# Make a prediction using the trained model
prediction = model.predict(input_data)

# Display the result
st.subheader("Prediction")
st.write(f"Predicted Attack Type: {prediction[0]}")
