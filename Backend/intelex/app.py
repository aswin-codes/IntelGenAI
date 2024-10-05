import streamlit as st
import pandas as pd
import pickle

# Load the trained Random Forest model
with open('crop_yield_random_forest_model.pkl', 'rb') as file:
    rf_model = pickle.load(file)

# Set up the Streamlit app layout
st.title("Crop Yield Prediction")

# User input for prediction
region = st.selectbox("Select Region", options=["North", "East", "South", "West"])
soil_type = st.selectbox("Select Soil Type", options=["Clay", "Sandy", "Loam", "Silt", "Peaty", "Chalky"])
crop = st.selectbox("Select Crop", options=["Wheat", "Rice", "Maize", "Barley", "Soybean", "Cotton"])
rainfall = st.number_input("Rainfall (mm)", min_value=0)
temperature = st.number_input("Temperature (°C)", min_value=18, max_value=50)
fertilizer_used = st.selectbox("Fertilizer Used", options=[True, False])
irrigation_used = st.selectbox("Irrigation Used", options=[True, False])
weather_condition = st.selectbox("Select Weather Condition", options=["Sunny", "Rainy", "Cloudy"])
days_to_harvest = st.number_input("Days to Harvest", min_value=0)

# Prepare the input data for prediction
input_data = {
    'Region': region,
    'Soil_Type': soil_type,
    'Crop': crop,
    'Rainfall_mm': rainfall,
    'Temperature_Celsius': temperature,
    'Fertilizer_Used': fertilizer_used,
    'Irrigation_Used': irrigation_used,
    'Weather_Condition': weather_condition,
    'Days_to_Harvest': days_to_harvest
}

# Create a DataFrame from the input data
df_input = pd.DataFrame([input_data])

# One-hot encode the input data
try:
    df_input = pd.get_dummies(df_input, columns=['Region', 'Soil_Type', 'Crop', 'Weather_Condition'], drop_first=True)
except KeyError as e:
    st.error(f"KeyError: {e}. Ensure that the input fields match the expected columns.")
    st.stop()

# Align the columns to match the trained model
missing_cols = set(rf_model.feature_names_in_) - set(df_input.columns)
for col in missing_cols:
    df_input[col] = 0

df_input = df_input[rf_model.feature_names_in_]

# Make predictions using the Random Forest model
rf_prediction = rf_model.predict(df_input)[0]

# Display the Random Forest prediction result
st.write(f"Predicted Crop Yield : {rf_prediction:.2f} tons per hectare")
