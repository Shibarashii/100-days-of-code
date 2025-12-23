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
prices_sheet = "Prices!"
users_sheet = "Users!"
full_range_prices = f"{prices_sheet}A:C"

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
    cities = gsheet.get_values(f"{prices_sheet}A2:A")["values"]  # type: ignore
    iata_codes = []
    print("Filling IATA Columns...")
    for city in cities:
        response = amadeus.city_search(city[0], max=3)
        data = response["data"][0]
        iata_code = data["iataCode"]
        iata_codes.append([iata_code])

    result = gsheet.update_values(
        f"{prices_sheet}B2:B", iata_codes, "USER_ENTERED")
    if result:
        print("Successfully updated IATA Codes in Google Sheets.")


def get_from_to_dates() -> tuple[str, str]:
    from_date = datetime.datetime.now()
    to_date = from_date + datetime.timedelta(days=30*6)

    from_date, to_date = from_date.strftime(
        "%Y-%m-%d"), to_date.strftime("%Y-%m-%d")

    return from_date, to_date


def get_prices_sheet():
    values = gsheet.get_values(f"{prices_sheet}A2:C")["values"]  # type: ignore
    return values


def get_users_sheet():
    values = gsheet.get_values(f"{users_sheet}B2:D")["values"]  # type: ignore
    return values


def get_flight_data(flight_data):
    """
    Helper: Tries to find direct flights. If none, tries indirect.
    Returns: The list of flight offers, or None if nothing found.
    """
    # 1. Try Direct
    try:
        flight_data.is_direct = True
        print(
            f"\nSearching direct: {flight_data.origin} -> {flight_data.destination}...")
        response = amadeus.search_offers(flight_data)

        if response["data"]:
            return response["data"]

        # 2. Fallback to Indirect
        print(f"Direct flights not found. Trying indirect...")
        flight_data.is_direct = False
        response = amadeus.search_offers(flight_data)

        if response["data"]:
            print("Indirect flights found!")
            return response["data"]

        print("No flights found (direct or indirect).")
        return None
    except Exception as e:
        print(f"Error: {e}")


def process_flight_details(flight_offer):
    """
    Helper: Parses the JSON, prints route segments.
    Returns: (price, route_string, destination_code)
    """
    price = float(flight_offer["price"]["total"])

    segments = flight_offer["itineraries"][0]["segments"]

    # Grab the final destination code (last segment's arrival)
    dest = segments[-1]["arrival"]["iataCode"]
    origin = segments[0]["departure"]["iataCode"]

    # Build the route string
    route_str = " -> ".join([s["departure"]["iataCode"] for s in segments])
    route_str += f" -> {dest}"

    print(f"Route: {route_str}")
    print(f"Price: £{price}")

    # Return all three
    return price, route_str, dest, origin


def send_email_to_users(msg: str):
    users_sheet = get_users_sheet()
    for name, surname, email in users_sheet:
        subject = "Cheap flight deals!"
        body = f"Greetings, {name} {surname}! {msg}"
        message = f"Subject:{subject}\n\n{body}"
        message = message.encode("utf-8")
        NotificationManager.send_email(message, email)


def find_cheap_flights(origin, origin_iata):

    departure_date, return_date = get_from_to_dates()
    prices_sheet = get_prices_sheet()

    for city, code, price in prices_sheet:
        flight_data = FlightData(
            origin=origin_iata,
            dest=code,
            departure_date=departure_date,
            return_date=return_date,
            currency_code="GBP"
        )

        data = get_flight_data(flight_data)

        if not data:
            continue

        lowest_price, route_str, final_dest, origin_iata = process_flight_details(
            data[0])

        target_price = float(price)
        if lowest_price < target_price:
            message = (f"Low price alert! Fly from {origin} ({origin_iata}) to {city} ({final_dest}) at a price of £{lowest_price}"
                       f", which is below your target price of £{target_price}!\nRoute: {route_str}")
            print(f"*** {message} ***")
            NotificationManager.twilio_notify(message)
            send_email_to_users(message)


def main():
    while True:
        origin = input("\nEnter city to depart from: ").title()
        try:
            origin_iata = amadeus.city_search(origin)["data"][0]["iataCode"]
        except:
            print("Invalid city. Try again.")
            continue
        else:
            find_cheap_flights(origin, origin_iata)
            print("Process finished")
            break


if __name__ == "__main__":
    main()
