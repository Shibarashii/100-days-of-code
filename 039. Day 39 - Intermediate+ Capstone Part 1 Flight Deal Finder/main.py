import requests
from pathlib import Path
from dotenv import load_dotenv
from gsheet import GSheetClient
from amadeus import AmadeusClient
import json
import os

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


def save_json(file):
    with open(root/"temp.json", "w") as f:
        json.dump(obj=file, fp=f, indent=2)


def fill_iata_columns():
    cities = gsheet.get_values("A2:A")["values"]  # type: ignore
    iata_codes = []
    for city in cities:
        response = amadeus.city_search(city[0], max=3).json()
        data = response["data"][0]
        iata_code = data["iataCode"]
        iata_codes.append([iata_code])

    result = gsheet.update_values("B2:B", iata_codes, "USER_ENTERED")
    if result:
        print("Successfully updated IATA Codes in Google Sheets.")


def main():
    # response = amadeus.city_search("paris", max=5).json()
    # data = response["data"][0]
    # iata_code = data["iataCode"]

    return


if __name__ == "__main__":
    main()
