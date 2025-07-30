import requests
from datetime import datetime

# ---------------------------
# User details (update as needed)
GENDER = "male"
WEIGHT_KG = 66
HEIGHT_CM = 180
AGE = 17

# ---------------------------
# API Credentials & Endpoints
# NOTE: Replace these placeholders with your actual API credentials and endpoints
APP_ID = "your_app_id_here"
API_KEY = "your_api_key_here"
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = "https://api.sheety.co/your_project/workoutTracking/workouts"
TOKEN = "Bearer your_bearer_token_here"

# ---------------------------
# Get user's exercise input
exercise_text = input("Tell me which exercises you did: ")

# ---------------------------
# Headers for Nutritionix API request
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

# Parameters for Nutritionix API request
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Send POST request to Nutritionix to parse exercise info
response = requests.post(EXERCISE_ENDPOINT, json=parameters, headers=headers)
result = response.json()

# ---------------------------
# Prepare date and time strings for logging
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Headers for Sheety API with Bearer Token authentication
sheet_header = {
    "Authorization": TOKEN
}

# ---------------------------
# Loop through each parsed exercise and send to Sheety API
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Send POST request to Sheety API to log workout data
    sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_inputs, headers=sheet_header)

    # Optional: Print response from Sheety API for debugging
    print(sheet_response.text)
