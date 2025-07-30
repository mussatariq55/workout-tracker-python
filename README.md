# 🏋️‍♂️ Workout Tracker in Python
A natural language workout logger built in Python that interprets exercise descriptions like "I ran 5 miles" or "I did 20 minutes of yoga" and logs them into a Google Sheet in real-time. This project demonstrates the use of modern web APIs, secure token authentication, and dynamic data logging — perfect for automating personal fitness records.

<img width="3072" height="2048" alt="5598655a-5336-4f83-8870-a49b68543ed3" src="https://github.com/user-attachments/assets/2cd4599d-cf01-47d0-9ede-c53e0075caf1" />



---

## 🚀 Features
- Parses human language (e.g., "I ran 5 km") into structured workout data using the Nutritionix API
- Logs exercise, duration, and calories into your Google Sheet using Sheety API  
- Securely handles API keys and tokens using environment variables  
- Auto-timestamping of each entry with date and time
- Easily extensible to support reminders, reports, or charts

---

## 🧠 Built With
- Python 3.10+
- `requests` for interacting with external APIs 
- `datetime` for accurate timestamping
- `os` and `dotenv` for secure handling of sensitive credentials
- Nutritionix API for parsing workout input   
- Sheety API for writing data to Google Sheets

---

## 💻 How It Works
1. The user inputs a sentence describing their workout.
2. The script sends the text to the Nutritionix API which analyzes and returns structured data.
3. It appends each exercise with its name, duration, and calories burned, along with the current time and date.
4. The data is pushed to your connected Google Sheet using a POST request to the Sheety API.

---

## 🏋️‍♂️ Workout Sheets in Google & Python Program Running Preview

![workout](https://github.com/user-attachments/assets/848d20b2-9768-4f4a-af03-f7c911485a55)

 
![sheets](https://github.com/user-attachments/assets/47b699c4-7724-4787-8db2-e3c9b67a12f3)

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/workout-tracker-python.git
cd workout-tracker-python
```

### 2. Install Dependencies
```bash
pip install requests python-dotenv
```

### 3. Set Environment Variables

#### On Linux/macOS:
Create a .env file in the root directory:
```bash
APP_ID=your_nutritionix_app_id
API_KEY=your_nutritionix_api_key
EXERCISE_ENDPOINT=https://trackapi.nutritionix.com/v2/natural/exercise
SHEET_ENDPOINT=https://api.sheety.co/your_project/workoutTracking/workouts
TOKEN=Bearer your_sheety_bearer_token
```
🛡️ Keep your .env file private. Never commit it to version control.

---
## 🧪 API Setup Manual

### 🔹 Nutritionix API Setup

1. Visit [https://developer.nutritionix.com](https://developer.nutritionix.com)
2. Sign up for a free account.
3. Create a new application and get your:
   - `APP_ID`
   - `API_KEY`
4. Use the following endpoint in your code:  
   `https://trackapi.nutritionix.com/v2/natural/exercise`

📌 **Note:** This API converts natural language text into structured workout data.

---

### 🔹 Sheety API Setup

1. Visit [https://sheety.co](https://sheety.co) and sign in with your Google account.
2. Create a new project and connect a Google Sheet (make sure it includes the headers: `date`, `time`, `exercise`, `duration`, `calories`).
3. Enable **Bearer Authentication** in your Sheety project settings.
4. Copy your endpoint URL and token:
   - Example endpoint:  
     `https://api.sheety.co/your_project/workoutTracking/workouts`
   - Example token:  
     `Bearer abc123xyz456...`

📌 **Note:** This API allows reading/writing Google Sheets via secure HTTP requests.

---
## ▶️ Running the Script
After setting the environment variables, run the script:

```bash
python main.py
```
Then input your workouts in plain English. Each logged activity will show up in your Google Sheet with a timestamp.

---

## 🌐 APIs Used

| API                | Purpose                                            |
|--------------------|----------------------------------------------------|
| Nutritionix        | Converts natural language input into exercise data |
| Sheety             | Sends formatted exercise data to your Google Sheet |

---

## 🧠 What You’ll Learn
- How to build a Python app using multiple APIs
- How to interpret natural language data with external services
- How to structure and send authenticated HTTP requests
- How to use environment variables for secure authentication
- How to automate personal fitness tracking effectively


---

## 🙌 Credits
- 👨‍💻 **Built by: Mussa Tariq
- LinkedIn: https://www.linkedin.com/in/mussa-tariq-0652712a0/
- 🔍 Nutritionix API – https://developer.nutritionix.com
- 📊 Sheety API – https://sheety.co
- 📌 Inspired by real-world use cases of fitness tracking automation

---

## 📬 Final Note
Stop guessing your progress. Start tracking it — automatically, securely, and in real-time. Whether you're biking, running, or lifting, let your code keep the score while you keep moving.


