import requests
import os
from datetime import datetime
import smtplib
from dotenv import load_dotenv
import time

load_dotenv()

MY_LAT = 12.983691  # Your latitude
MY_LONG = 121.781551  # Your longitude


# Your position is within +5 or -5 degrees of the ISS position.

def check_iss_in_range():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    return False


def check_if_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now.hour >= sunset and time_now.hour <= sunrise:
        return True
    return False


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
iss_in_range = check_iss_in_range()
is_dark = check_if_dark()

while True:
    if iss_in_range and is_dark:
        SENDER_EMAIL = os.getenv("SENDER_EMAIL")
        RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
        APP_PASSWORD = os.getenv("APP_PASSWORD")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=APP_PASSWORD)
            connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=RECEIVER_EMAIL,
                                msg="Subject:ISS is close\n\nLook up")
        print(f"Mail sent to {RECEIVER_EMAIL}")
    else:
        print("Mail not sent")
        print(f"ISS is in range: {iss_in_range}")
        print(f"Is dark: {is_dark}")
    time.sleep(60)
