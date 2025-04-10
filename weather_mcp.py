from fastapi import FastAPI, Query
import requests
import os

app = FastAPI()

# OPENWEATHER_API_KEY = os.getenv("")
OPENWEATHER_API_KEY = ""


@app.get("/weather")
def get_weather(city: str = Query(..., description="Name of the city")):
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code != 200:
        return {
            "status": "error",
            "message": data.get("message", "Something went wrong")
        }

    weather_info = {
        "location": data["name"],
        "temperature_celsius": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed_kph": data["wind"]["speed"] * 3.6
    }

    return {
        "status": "success",
        "weather_data": weather_info
    }
