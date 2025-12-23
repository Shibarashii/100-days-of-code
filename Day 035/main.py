import requests
from pathlib import Path
import json
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

root = Path(__file__).parent

API_OWM = os.getenv("API_OWM")
URL = "https://api.openweathermap.org/data/2.5/forecast"
LAT = "14.1407"
LONG = "121.4692"

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
SENDER = os.getenv("SENDER")
RECEIVER = os.getenv("RECEIVER")
params = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_OWM,
    "cnt": 4
}

response = requests.get(url=URL, params=params)
response.raise_for_status()
data = response.json()

with open(root/"data.json", "w") as f:
    json.dump(data, fp=f, indent=4)

forecasts = data["list"]

will_rain = False

for forecast in forecasts:
    weather = forecast["weather"]
    weather_code = weather[0]["id"]
    if weather_code < 700:
        will_rain = True

if will_rain:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    print(f"SENDER: {SENDER}")
    print(f"RECEIVER: {RECEIVER}")
    message = client.messages.create(
        body="It might rain, bring an umbrella",
        from_=SENDER,
        to=RECEIVER  # type: ignore
    )
    print(message.sid)
    print(message.status)
