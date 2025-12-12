import requests
from dotenv import load_dotenv
import os
from typing import Optional
import json
from pathlib import Path
import time

load_dotenv()
root = Path(__file__).parent


class FlightData:
    def __init__(self, origin: str, dest: str, departure_date: str, return_date: str, currency_code: str = "GBP"):
        self.origin = origin
        self.destination = dest
        self.departure_date = departure_date
        self.return_date = return_date
        self.currency_code = currency_code


class AmadeusClient:
    def __init__(self):
        self.server = "https://test.api.amadeus.com"
        self.client_id = os.getenv("AMADEUS_APPKEY")
        self.secret = os.getenv("AMADEUS_SECRET")
        self.auth_headers = None
        self.refresh_access_token()

    def _get_credentials(self) -> dict:
        """Load credentials from saved json file"""
        cred_path = root/"amadeus.credentials.json"
        if not os.path.exists(cred_path):
            return {}  # Return empty dict instead of raising error
        with open(cred_path, "r") as f:
            creds = json.load(fp=f)
        return creds

    def _build_auth_headers(self) -> dict:
        """Build authorization headers from stored credentials"""
        creds = self._get_credentials()
        if not creds or "access_token" not in creds:
            return {}

        token_type = creds["token_type"]
        access_token = creds["access_token"]
        token = f"{token_type} {access_token}"
        headers = {
            "Authorization": token
        }
        return headers

    def _is_token_expired(self, creds: dict) -> bool:
        return not creds or time.time() >= creds.get("expires_at", 0)

    def refresh_access_token(self):
        """Refresh the access token and update auth headers"""
        creds = self._get_credentials()

        # Only refresh if token is expired or doesn't exist
        if not self._is_token_expired(creds):
            self.auth_headers = self._build_auth_headers()
            print("Using existing valid token")
            return

        print("Refreshing access token...")
        endpoint = f"{self.server}/v1/security/oauth2/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        params = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.secret
        }

        response = requests.post(url=endpoint, data=params, headers=headers)
        response.raise_for_status()

        data = response.json()
        data["expires_at"] = time.time() + data["expires_in"]

        # Save credentials
        path = root/"amadeus.credentials.json"
        with open(path, "w") as f:
            json.dump(obj=data, fp=f, indent=2)
            print(f"Successfully refreshed access token. Saved to: {path}")

        # Update auth headers with new token
        self.auth_headers = self._build_auth_headers()
        return response

    def city_search(self, keyword: str, country_code: str | None = None, max: int | None = None, include: str | None = None) -> dict:
        """Search for a city using keyword or country code"""
        endpoint = f"{self.server}/v1/reference-data/locations/cities"
        params = {
            "keyword": keyword.upper(),
            "countryCode": country_code,
            "max": max,
            "include": include
        }
        params = {k: v for k, v in params.items() if v is not None}

        response = requests.get(
            url=endpoint, params=params, headers=self.auth_headers)
        response.raise_for_status()

        return response.json()

    def search_offers(self, flight_data: FlightData) -> dict:
        """Search for flight offers"""
        endpoint = f"{self.server}/v2/shopping/flight-offers"
        params = {
            "originLocationCode": flight_data.origin,
            "destinationLocationCode": flight_data.destination,
            "departureDate": flight_data.departure_date,
            "returnDate": flight_data.return_date,
            "adults": 1,
            "nonStop": "true",
            "currencyCode": flight_data.currency_code,
            "max": 5
        }

        print(
            f"\nSearching flights from {flight_data.origin} to {flight_data.destination}...")
        response = requests.get(
            url=endpoint, params=params, headers=self.auth_headers)

        return response.json()
