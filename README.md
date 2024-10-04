# IntelGenAI

IntelGenAI is an innovative solution that leverages AI-powered tools and seamless integration of various services to provide smart farming solutions. The project is powered by DreamFarm (a Flutter-based frontend) and a robust backend infrastructure with GenAI, Django, FastAPI for web scraping, and Streamlit for an end-to-end Gemini chat experience.

## Features of DreamFarm
- Real-time weather information for efficient crop management.
- Soil testing services to help farmers monitor soil conditions.
- AI-based crop recommendations based on location, soil type, and weather conditions.
- Integration with the Gemini chat app for personalized advice and interaction.
- Marketplace and community features for farmers to buy, sell, and connect.
- FastAPI-based web scraping to retrieve agricultural data from relevant sources.

---

## Requirements to run the software

Before proceeding, ensure the following dependencies are installed on your machine:

- **Python**
- **Node.js**
- **Flutter**

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
   npm i
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
   cd Backend/server/webscraping
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

---

