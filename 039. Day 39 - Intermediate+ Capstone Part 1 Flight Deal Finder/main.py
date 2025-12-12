import requests
from pathlib import Path
from dotenv import load_dotenv
from gsheet import GSheetClient
from amadeus import AmadeusClient
import json
import os
import datetime
from amadeus import FlightData
from notification import NotificationManager

load_dotenv()
root = Path(__file__).parent
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
full_range = "A:C"

amadeus = AmadeusClient()
gsheet = GSheetClient(SPREADSHEET_ID, SCOPES)


def print_rows(rows):
    for row in rows:
        print(row)


def save_json(file, file_name: str | None = None):
    if file_name is None:
        file_name = "temp.json"

    with open(root/file_name, "w") as f:
        json.dump(obj=file, fp=f, indent=2)


def fill_iata_columns():
    cities = gsheet.get_values("A2:A")["values"]  # type: ignore
    iata_codes = []
    print("Filling IATA Columns...")
    for city in cities:
        response = amadeus.city_search(city[0], max=3)
        data = response["data"][0]
        iata_code = data["iataCode"]
        iata_codes.append([iata_code])

    result = gsheet.update_values("B2:B", iata_codes, "USER_ENTERED")
    if result:
        print("Successfully updated IATA Codes in Google Sheets.")


def get_from_to_dates() -> tuple[str, str]:
    from_date = datetime.datetime.now()
    to_date = from_date + datetime.timedelta(days=30*6)

    from_date, to_date = from_date.strftime(
        "%Y-%m-%d"), to_date.strftime("%Y-%m-%d")

    return from_date, to_date


def get_sheet_values() -> tuple[list, list, list]:
    values = gsheet.get_values("A2:C")["values"]  # type: ignore
    cities, iata_codes, prices = [], [], []
    for city, code, price in values:
        cities.append(city)
        iata_codes.append(code)
        prices.append(int(price))

    return cities, iata_codes, prices


def find_cheap_flights():
    """Searches for flights cheaper than the prices define in Google Sheet"""
    departure_date, return_date = get_from_to_dates()
    cities, iata_codes, prices = get_sheet_values()

    origin_location = input("Enter IATA code to depart from: ").upper()

    for i, dest in enumerate(iata_codes):
        flight_data = FlightData(
            origin_location, dest, departure_date, return_date)
        response = amadeus.search_offers(flight_data)
        data = response["data"]
        if not data:
            print(
                f"Flight offers `{origin_location} to {dest}` not found.")
            continue

        # save_json(response, f"temp{i}.json")
        first_item = data[0]
        id = first_item["id"]
        lowest_price = float(first_item["price"]["total"])
        print(f"Lowest price: £{lowest_price}")

        is_price_cheaper = lowest_price < float(prices[i])
        if is_price_cheaper:
            message = f"Low price alert! Only £{lowest_price} only to fly from {origin_location} to {dest}, from {departure_date} to {return_date}"
            print(message)
            NotificationManager.twilio_notify(message)


def main():
    find_cheap_flights()


if __name__ == "__main__":
    main()
