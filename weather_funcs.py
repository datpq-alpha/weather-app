import requests
import streamlit as st

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    try:
        api_key = st.secrets["API_KEY"]
        params = {
            "q": city_name,
            "appid": api_key,
            "units": "metric",
            "lang": "vi"
        }
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            return {
                "city": data["name"],
                "temp": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"],
                "icon": data["weather"][0]["icon"]
            }
        else:
            return None
    except Exception:
        return None
    # return {
    #     "city": f"{city_name} (Demo)",
    #     "temp": 28.5,
    #     "humidity": 75,
    #     "description": "nắng đẹp (giả lập)",
    #     "icon": "01d"  # Icon mặt trời
    # }
