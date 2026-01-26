import requests

# --- API KEY (QUAN TRỌNG)---
API_KEY = "1386194825985e3fa8d19f01c3819826"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_weather(city_name):
    try:
        url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric&lang=vi"
        response = requests.get(url)

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
    except:
        return None
    # return {
    #     "city": f"{city_name} (Demo)",
    #     "temp": 28.5,
    #     "humidity": 75,
    #     "description": "nắng đẹp (giả lập)",
    #     "icon": "01d"  # Icon mặt trời
    # }