import requests
from pathlib import Path
from dotenv import load_dotenv
from gsheet import GSheetClient
import os

load_dotenv()
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
full_range = "A:C"


def print_rows(rows):
    for row in rows:
        print(row)


def main():
    gsheet = GSheetClient(SPREADSHEET_ID, SCOPES)
    results = gsheet.get_values(full_range)
    rows = results["values"]  # type: ignore

    print_rows(rows)


if __name__ == "__main__":
    main()
