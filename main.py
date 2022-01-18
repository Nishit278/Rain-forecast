import requests 
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY=os.getenv("API_KEY")
REQ_ENDPOINT=os.getenv("REQ_ENDPOINT")

weather_params = {
    "lat": "28.6139",
    "lon":  "77.2090",
    "appid": API_KEY,
    "units": "metric",
    "exclude": "current,minutely,daily"
    }
res = requests.get(REQ_ENDPOINT, params=weather_params)
# print(res.status_code)
data = res.json()
# hourly = data["hourly"]
carry_umbrella = False
weather_hourly = data["hourly"][:12]
# print(weather_hourly)
for hour_data in weather_hourly:
    if hour_data["weather"][0]["id"] < 700:
        carry_umbrella = True
# for i in range(0,12):
#     # print(hourly[i]["weather"][0]["id"])
    
#     if weather_hourly["id"] < 700:
#         carry_umbrella = True

if carry_umbrella:
    print("Carry an umbrella with you to be safe! Have a nice day king!")
else:
    print("It's clear today, have a nice day king !")