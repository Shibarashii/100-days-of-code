import os
import smtplib
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
import datetime as dt
import random

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


load_dotenv()

root = Path(__file__).parent
csv_path = root / "birthdays.csv"


def get_random_letter_path():
    letters_path = root / "letter_templates"
    letters = [f"letter_{i}.txt" for i in range(1, 4)]
    random_letter = random.choice(letters)

    return letters_path / random_letter


now = dt.datetime.now()
month_now = now.month
day_now = now.day

birthdays = pd.read_csv(csv_path).to_dict(orient="records")

random_letter = get_random_letter_path()
for row in birthdays:
    if row["month"] == month_now and row["day"] == day_now:
        sender_email = os.getenv("SENDER_EMAIL")
        receiver_email = row["email"]
        app_password = os.getenv("APP_PASSWORD")

        subject = f"Happy birthday {row["name"]}!"
        with open(random_letter, "r") as f:
            body = f.read()
            body = body.replace("[NAME]", row["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(sender_email, app_password)
            connection.sendmail(
                from_addr=sender_email, to_addrs=receiver_email, msg=f"Subject:{subject}\n\n{body}")

            print(f"Message sent to {receiver_email}")
