from bs4 import BeautifulSoup
import requests
from smtplib import SMTP
from dotenv import load_dotenv
import os

load_dotenv()

target_price = 35_000


def get_soup() -> BeautifulSoup:
    url = "https://www.amazon.com/Crucial-6400MHz-Overclocking-Desktop-Compatible/dp/B0FQNB9WBD"
    print(f"Getting soup from {url}...")

    headers = {
        "Accept-Language": "en-PH,en;q=0.9",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
        "Referer": "https://www.amazon.com/"
    }

    response = requests.get(url=url, headers=headers)
    response.raise_for_status()
    webtext = response.text
    soup = BeautifulSoup(webtext, "html.parser")
    print("Successfully retrieved soup!")

    return soup


def send_email(sender: str,
               receiver: str,
               msg: str):
    try:
        print(f"Sending mail to {receiver}...")
        app_password = os.getenv("GOOGLE_APP_PASSWORD")
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(sender, password=app_password)
            connection.sendmail(sender, receiver, msg)
    except Exception as e:
        print(f"Failed. {e}")
    else:
        print(f"Mail sent successfully!")


def parse_int(price: str):
    price_int = int(price.replace(",", "").replace(".", ""))
    return price_int


def main():
    soup = get_soup()

    product_title = soup.select_one("#productTitle").get_text().strip()
    symbol_text = soup.select_one(".a-price-symbol").get_text()
    price_text = soup.select_one(".a-price-whole").get_text()
    price = parse_int(price_text)

    if price < target_price:
        print(
            f"Price ({symbol_text} {price}) lower than target price of {symbol_text} {target_price}!")
        message = f"Subject: Low price alert!\n\nLow price alert!\n\n{product_title}\nTarget Price: {symbol_text} {target_price:,}\nCurrent Price: {symbol_text} {price:,}"
        sender = os.getenv("SENDER_GMAIL")
        receiver = os.getenv("RECEIVER_GMAIL")
        send_email(sender=sender, receiver=receiver, msg=message)


if __name__ == "__main__":
    main()
