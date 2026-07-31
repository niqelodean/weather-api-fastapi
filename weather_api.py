from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Weather API"}

@app.get("/weather")
def get_weather(city: str):
    try:
        response = requests.get(f"https://wttr.in/{city}?format=j1")
        if response.status_code != 200:
            return {"error": f"City '{city}' not found"}

        data = response.json()
        if not data.get("current_condition"):
            return {"error": f"City '{city}' not found"}
        temp_c = data["current_condition"][0]["temp_C"]
        humidity = data["current_condition"][0]["humidity"]
        weather_desc = data["current_condition"][0]["weatherDesc"][0]["value"]
        return {
            "city": city,
            "temperature": temp_c,
            "humidity": humidity,
            "weather": weather_desc
        }
    except Exception as e:
        return {"error": str(e)}
