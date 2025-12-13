from twilio.rest import Client
from smtplib import SMTP
import os

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

sender_num = str(os.getenv("SENDER"))
receiver_num = str(os.getenv("RECEIVER"))

sender_email = str(os.getenv("SENDER_EMAIL"))
app_password = str(os.getenv("APP_PASSWORD"))


class NotificationManager:
    def __init__(self) -> None:
        pass

    @staticmethod
    def twilio_notify(body: str, from_: str = sender_num, to: str = receiver_num):
        message = client.messages.create(
            body=body,
            from_=from_,
            to=to,
        )
        print(f"Message sent to {to}")

    @staticmethod
    def send_email(msg, to_address: str):
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(sender_email, app_password)
            connection.sendmail(from_addr=sender_email,
                                to_addrs=to_address, msg=msg)
            print(f"Email sent to {to_address}")
