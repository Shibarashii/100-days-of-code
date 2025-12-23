import datetime as dt
import random
from pathlib import Path
from dotenv import load_dotenv
import smtplib
import os


load_dotenv()

root = Path(__file__).parent
quotes_path = root / "quotes.txt"

now = dt.datetime.now()
day_now = now.weekday()

days = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

if days[day_now] == "Tuesday":
    with open(quotes_path, "r") as f:
        content = f.readlines()
        random_quote = random.choice(content)

    sender_email = os.getenv("SENDER_EMAIL")
    receiver_email = os.getenv("RECEIVER_EMAIL")
    app_password = os.getenv("APP_PASSWORD")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=app_password)

        to_send = f"Subject:{days[day_now]} Motivation\n\n{random_quote}"

        connection.sendmail(from_addr=sender_email,
                            to_addrs=receiver_email,
                            msg=to_send)
