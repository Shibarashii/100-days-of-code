from twilio.rest import Client
import os

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

sender_num = str(os.getenv("SENDER"))
receiver_num = str(os.getenv("RECEIVER"))


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
        print(message.status)
        print(f"Message sent to {to}")
