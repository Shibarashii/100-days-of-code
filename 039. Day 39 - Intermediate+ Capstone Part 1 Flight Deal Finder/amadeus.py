import requests
from dotenv import load_dotenv
import os
from typing import Optional
import json
from pathlib import Path

load_dotenv()

root = Path(__file__).parent


class AmadeusClient:
    def __init__(self):
        self.server = "https://test.api.amadeus.com/v1"
        self.auth_headers = self._auth()
        self.client_id = os.getenv("AMADEUS_APPKEY")
        self.secret = os.getenv("AMADEUS_SECRET")

    def _get_credentials(self) -> dict:
        cred_path = root/"amadeus.credentials.json"
        if not os.path.exists(cred_path):
            raise FileNotFoundError(cred_path)

        with open(cred_path, "r") as f:
            creds = json.load(fp=f)

        return creds

    def _auth(self):
        creds = self._get_credentials()
        token_type = creds["token_type"]
        access_token = creds["access_token"]  # type: ignore

        token = f"{token_type} {access_token}"

        headers = {
            "Authorization": token
        }
        return headers

    def refresh_access_token(self):
        endpoint = f"https://test.api.amadeus.com/v1/security/oauth2/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        params = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.secret
        }

        response = requests.post(url=endpoint, data=params, headers=headers)
        response.raise_for_status()

        with open(root/"amadeus.credentials.json", "w") as f:
            json.dump(obj=response.json(), fp=f, indent=2)

        self.auth_headers = self._auth()
        return response

    def city_search(self, keyword: str, country_code: str | None = None, max: int | None = None, include: str | None = None):
        endpoint = f"{self.server}/reference-data/locations/cities"

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
        return response
