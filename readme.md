# 🌤️ Weather Buddy - MCP Project

A beginner-friendly weather-checking API built with **FastAPI** and the **OpenWeatherMap API**.  
Just type your city, hit the endpoint, and get the current weather info in a clean JSON format!

---

## 🚀 Features

- ⚡ Superfast API built with FastAPI
- 🌍 Real-time weather data from OpenWeatherMap
- 🧠 Simple logic, ideal for learning or prototyping
- 🔐 API key is safely stored using environment variables
- 🌐 Accepts any city name via query parameter

---

## 🧩 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Requests](https://docs.python-requests.org/)
- [OpenWeatherMap API](https://openweathermap.org/api)

---

## 🛠️ Setup Instructions

### 1. Clone this repository

```bash
git clone https://github.com/your-username/weather-buddy.git
cd weather-buddy

python -m venv mcp-env
mcp-env\Scripts\activate      # On Windows
# OR
source mcp-env/bin/activate  # On Mac/Linux


pip install fastapi uvicorn requests


get your api key ; https://home.openweathermap.org/api_keys

uvicorn weather_mcp:app --reload

