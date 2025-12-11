import requests
from dotenv import load_dotenv
import os
from typing import Optional
import json
from pathlib import Path
import time

load_dotenv()
root = Path(__file__).parent


class AmadeusClient:
    def __init__(self):
        self.server = "https://test.api.amadeus.com"
        self.client_id = os.getenv("AMADEUS_APPKEY")
        self.secret = os.getenv("AMADEUS_SECRET")
        self.auth_headers = None
        self.refresh_access_token()

    def _get_credentials(self) -> dict:
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

    def city_search(self, keyword: str, country_code: str | None = None, max: int | None = None, include: str | None = None):
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

        if 200 <= response.status_code < 300:
            print(f"Successfully searched cities for: {keyword.title()}")
        return response

    def search_offers(self, origin_iata: str, dest_iata: str, from_time: str, to_time: str):
        endpoint = f"{self.server}/v2/shopping/flight-offers"
        params = {
            "originLocationCode": origin_iata,
            "destinationLocationCode": dest_iata,
            "departureDate": from_time,
            "returnDate": to_time,
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": 5
        }

        print(f"Searching flights: {params}")
        response = requests.get(
            url=endpoint, params=params, headers=self.auth_headers)
        print(response.json())

        if 200 <= response.status_code < 300:
            print("Successfully retrieved flight offers")
        return response
