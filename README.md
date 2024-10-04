


# IntelGenAI (Hackathon)

**DreamFarm** is an innovative solution that leverages AI-powered tools and seamless integration of various services to provide smart farming solutions. The project is powered by DreamFarm (a Flutter-based frontend) and a robust backend infrastructure with GenAI, Django, FastAPI for web scraping, and Streamlit for an end-to-end Gemini chat experience.

## Features of DreamFarm
- Real-time weather information for efficient crop management.
- Soil testing services to help farmers monitor soil conditions.
- AI-based crop recommendations based on location, soil type, and weather conditions.
- AI-based pest disease detection and its possible remedies.
- Integration with the Gemini chat app for personalized advice and interaction.
- Marketplace and community features for farmers to buy, sell, and connect.
- FastAPI-based web scraping to retrieve agricultural data from relevant sources.
- AI-based crop yield predictor.

---

## Requirements to Run the Software

Before proceeding, ensure the following dependencies are installed on your machine:

- **Python** (Version 3.7 or above)
- **Node.js** (Version 14 or above)
- **Flutter** (Stable version)

---

## Running the Software

### 1. Run the Flutter Frontend
1. Navigate to the frontend folder:
   ```bash
   cd Frontend/dreamfarm
   ```
2. Install the required packages by running:
   ```bash
   flutter pub get
   ```
3. Run the Flutter app using the following command (ensure your emulator or physical device is running):
   ```bash
   flutter run
   ```

### 2. Run the GenAI Server
1. Navigate to the GenAI server backend folder:
   ```bash
   cd Backend/genai
   ```
2. Install the required Node.js packages:
   ```bash
   npm install
   ```
3. Start the GenAI server:
   ```bash
   npm run start
   ```

### 3. Run the Django Server
1. Navigate to the Django server folder:
   ```bash
   cd Backend/server
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the Django server:
   ```bash
   python manage.py runserver
   ```

### 4. Run the Web Scraping FastAPI Server
1. Navigate to the web scraping service folder:
   ```bash
   cd Backend/server/webscraping/scraping
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the FastAPI server:
   ```bash
   uvicorn main:app --host 127.0.0.1 --port 8001
   ```

### 5. Run the Gemini Streamlit App
1. Navigate to the Gemini chat project folder:
   ```bash
   cd Backend/server/Gemini_chat/End-To-End-Gemini-Project
   ```
2. Install Streamlit:
   ```bash
   pip install streamlit
   ```
3. Start the Streamlit server:
   ```bash
   streamlit run main.py
   ```

### 6. Train the Data
1. Install the scikit-learn-intelex package:
   ```bash
   pip install scikit-learn-intelex
   ```
2. Navigate to the intelex directory:
   ```bash
   cd Backend/intelex
   ```
3. Download the dataset from the following link: [Crop Yield Dataset](https://www.kaggle.com/datasets/samuelotiattakorah/agriculture-crop-yield)
4. Train the model by running:
   ```bash
   python main.py
   ```
   This will generate two pickle files: one using `RandomForestRegressor` and another using `Linear Regression`. Modify the pickle files accordingly in the `app.py` for the Streamlit application.

### 7. Run the Yield Predictor Streamlit App
1. Ensure Streamlit is installed:
   ```bash
   pip install streamlit
   ```
2. Navigate to the intelex directory:
   ```bash
   cd Backend/intelex
   ```
3. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

## Additional Notes
- Ensure all services are running properly to facilitate communication between different components of the application.
- You can access the respective services through the following URLs:
  - Django Server: `http://127.0.0.1:8000`
  - FastAPI Server: `http://127.0.0.1:8001`
  - Streamlit Apps: `http://localhost:8501`
  
Feel free to reach out if you have any questions or need further assistance!
```

### Notes:
- Adjust the Python version requirement as necessary based on your dependencies.
- Include any other dependencies or setup instructions specific to your project.
- Ensure to replace placeholder links with actual links if needed.