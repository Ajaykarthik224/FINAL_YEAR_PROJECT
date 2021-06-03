import requests
import config


def get_weather():
    location = requests.get("https://ipinfo.io").json()
    [latitude, longitude] = location['loc'].split(",")

    weather_info = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=metric&appid={config.weather_api_key}").json()

    return weather_info['main']


# print(get_weather())
