import requests
from data import config
import json


def get_weather():
    location = requests.get("https://ipinfo.io").json()
    [latitude, longitude] = location['loc'].split(",")

    weather_info = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=metric&appid={config.weather_api_key}").json()

    return weather_info  # ['main']


def get_place_weather(state):
    state_list = {
        "Andaman & Nicobar Islands": "Port Blair",
        "Arunachal Pradesh": "Itanagar",
        "Assam & Meghalaya": "Guwahati",
        "Bihar": "Patna",
        "Chhattisgarh": "Chhattisgarh",
        "Coastal Andhra Pradesh": "Amaravati",
        "Coastal Karnataka": "Mangaluru",
        "East Madhya Pradesh": "Bhopal",
        "East Rajasthan": "Jaipur",
        "East Uttar Pradesh": "Lucknow",
        "Gangetic West Bengal": "Kolkata",
        "Gujarat Region": "Ahmedabad ",
        "Haryana Delhi & Chandigarh": "Delhi",
        "Himachal Pradesh": "Shimla",
        "Jammu & Kashmir": "Srinagar",
        "Jharkhand": "Ranchi",
        "Kerala": "Thiruvananthapuram",
        "Konkan & Goa": "Goa",
        "Lakshadweep": "Kavaratti",
        "Madhya Maharashtra": "Mumbai",
        "Matathwada": "Pune",
        "Naga Mani Mizo Tripura": "Agartala",
        "North Interior Karnataka": "Hampi",
        "Orissa": "Bhubaneswar",
        "Punjab": "Amritsar",
        "Rayalseema": "Chittoor",
        "Saurashtra & Kutch": "Rajkot",
        "South Interior Karnataka": "Bengaluru",
        "Sub Himalayan West Bengal & Sikkim": "Gangtok",
        "Tamil Nadu": "Chennai",
        "Telangana": "Visakhapatnam",
        "Uttarakhand": "Dehradun",
        "Vidarbha": "Nagpur",
        "West Madhya Pradesh": "Bhopal",
        "West Rajasthan": "Jodhpur",
        "West Uttar Pradesh": "Lucknow"
    }
    weather_info = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={state_list[state]}&units=metric&appid={config.weather_api_key}").json()

    return weather_info


# print(json.dumps(get_weather()['weather'][0]['main'], indent=4))
# print(json.dumps(get_place_weather('Assam & Meghalaya'), indent=4))
