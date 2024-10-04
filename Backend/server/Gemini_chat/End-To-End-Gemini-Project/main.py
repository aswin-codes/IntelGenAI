from dotenv import load_dotenv
load_dotenv()  # Loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    response.resolve()  # Ensure complete iteration
    return response


# Function to get grain and farming storage facilities
def get_grain_and_storage_facilities(location):
    # Use the location parameter to query Google Generative AI about grain and farming storage facilities
    question = f"Grain and farming storage facilities near {location} kilometre radius of me. Please return the name, phone number and address"
    return get_gemini_response(question)

# Function to get input suppliers of seeds and farming products
def get_input_suppliers(location):
    # Use the location parameter to query Google Generative AI about input suppliers
    question = f"Input suppliers of seeds and farming products near {location} kilometre radius of me. Please return the name, phone number and address"
    return get_gemini_response(question)

# Function to get soil testing services
def get_soil_testing_services(location):
    # Use the location parameter to query Google Generative AI about soil testing services
    question = f"Soil testing services near {location} kilometre radius of me. Please return the name, phone number and address"
    return get_gemini_response(question)

# Initialize streamlit app
st.set_page_config(page_title="Services provider")
st.header("Enter location radius within which you want to access services")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Get user input
input_location = st.text_input("Location: ", key="location")
submit = st.button("Submit")

if submit and input_location:
    # Get responses based on user queries
    response_grain_storage = get_grain_and_storage_facilities(input_location)
    response_input_suppliers = get_input_suppliers(input_location)
    response_soil_testing = get_soil_testing_services(input_location)

    # Display responses
    st.subheader("Grain and Farming Storage Facilities:")
    for chunk in response_grain_storage:
        st.write(chunk.text)

    st.subheader("Input Suppliers of Seeds and Farming Products:")
    for chunk in response_input_suppliers:
        st.write(chunk.text)

    st.subheader("Soil Testing Services:")
    for chunk in response_soil_testing:
        st.write(chunk.text)

    # Add user queries and responses to session state chat history
    st.session_state['chat_history'].append(("You", f"Location: {input_location}"))
    st.session_state['chat_history'].append(("Bot", "Grain and Farming Storage Facilities:"))
    st.session_state['chat_history'].extend([("Bot", chunk.text) for chunk in response_grain_storage])
    st.session_state['chat_history'].append(("Bot", "Input Suppliers of Seeds and Farming Products:"))
    st.session_state['chat_history'].extend([("Bot", chunk.text) for chunk in response_input_suppliers])
    st.session_state['chat_history'].append(("Bot", "Soil Testing Services:"))
    st.session_state['chat_history'].extend([("Bot", chunk.text) for chunk in response_soil_testing])

# Display chat history
st.subheader("The Chat History is")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
