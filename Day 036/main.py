import requests
from pathlib import Path
import os
from dotenv import load_dotenv
import json
import html
from twilio.rest import Client

root = Path(__file__).parent
load_dotenv()

ALPHAVANTAGE_API = os.getenv("ALPHAVANTAGE_API")
STOCK = "AMD"
COMPANY_NAME = "AMD"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
alphavantage_url = "https://www.alphavantage.co/query"
alphavantage_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_API
}

response = requests.get(alphavantage_url, alphavantage_params)
response.raise_for_status()
alphavantage_data = response.json()

with open(root/"alphavantage_data.json", "w") as f:
    json.dump(obj=alphavantage_data, fp=f, indent=4)

daily_data: dict = alphavantage_data["Time Series (Daily)"]
latest_day = list(daily_data)[0]
prev_day = list(daily_data)[1]

latest_close = float(daily_data[latest_day]["4. close"])
prev_close = float(daily_data[prev_day]["4. close"])

inc_percent = (latest_close - prev_close) / prev_close * 100

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
NEWSAPI_API = os.getenv("NEWSAPI_API")
newsapi_url = "https://newsapi.org/v2/everything"
newsapi_params = {
    "apiKey": NEWSAPI_API,
    "qInTitle": COMPANY_NAME
}

response = requests.get(newsapi_url, newsapi_params)
response.raise_for_status()
newsapi_data = response.json()

with open(root/"newsapi_data.json", "w") as f:
    json.dump(obj=newsapi_data, fp=f, indent=4)

articles = newsapi_data["articles"]
latest_article = articles[0]
headline = html.unescape(latest_article["title"])
body = latest_article["content"]

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
symbol = "🔺" if inc_percent >= 0.0 else "🔻"

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
SENDER = os.getenv("SENDER")
RECEIVER = os.getenv("RECEIVER")

client = Client()
msg_body = f"""{STOCK}: {symbol}{abs(inc_percent):.2f}\nHeadline: {headline}"""
print(msg_body)
message = client.messages.create(body=msg_body,
                                 from_=SENDER,
                                 to=RECEIVER)  # type: ignore
print("")
print(message.sid)
