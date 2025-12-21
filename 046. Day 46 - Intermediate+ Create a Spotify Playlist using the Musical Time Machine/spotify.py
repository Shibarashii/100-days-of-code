from urllib.parse import urlparse, parse_qs
import os
from dotenv import load_dotenv
import requests
from pathlib import Path
import json
import secrets
import webbrowser
import base64
from pathlib import Path
import json

load_dotenv()
root = Path(__file__).parent
credentials_path = root / "spotify.credentials.json"


def save_to_json(data: dict):
    with open(root/"response.json", "w") as f:
        json.dump(obj=data, fp=f, indent=2)


class SpotifyClient:
    def __init__(self) -> None:
        self.auth = SpotifyAuth()
        self.username = os.getenv("SPOTIFY_USERNAME")

    def create_playlist(self,
                        name: str,
                        description: str,
                        is_public: bool = True,
                        is_collaborative: bool = False) -> dict:
        """
        Create a spotify playlist.

        :param name: Name of playlist
        :type name: str

        :param description: Description of playlist
        :type description: str

        :param is_public: Playlist is public or private 
        :type is_public: bool

        :param is_collaborative: Playlist is collaborative or not
        :type is_collaborative: bool

        :return: `response.json()`
        :rtype: dict[Any, Any]
        """
        print("Creating playlist...")
        endpoint = f"https://api.spotify.com/v1/users/{self.username}/playlists"
        query = {
            "name": name,
            "public": is_public,
            "collaborative": is_collaborative,
            "description": description
        }

        response = requests.post(
            url=endpoint, json=query, headers=self.auth.auth_headers)
        response.raise_for_status()
        data = response.json()

        print(f"Successfully created playlist {name}")
        print(f"Link: {data["external_urls"]["spotify"]}")
        print(f"Playlist ID: {data["id"]}")

        return data

    def add_to_playlist(self, playlist_id: str, uris: list[str]) -> dict:
        """
        Add tracks to a playlist.

        :param playlist_id: The `ID` of the playlist. 
        :type playlist_id: str
        :param uris: A list of URIs of tracks. 
        :type uris: list[str]

        :return: `response.json()`
        :rtype: dict[Any, Any]
        """
        print("Adding to playlist...")
        endpoint = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
        query = {
            "playlist_id": playlist_id,
            'uris': uris
        }

        response = requests.post(
            url=endpoint, json=query, headers=self.auth.auth_headers)
        response.raise_for_status()
        data = response.json()
        print("Successfully added to playlist!")
        return data

    def search_track(self,
                     track: str,
                     artist: str | None = None,
                     limit: int = 1) -> dict:
        """
        Search a track from spotify.

        :param track: Track name.
        :type track: str
        :param artist: Artist of the track.
        :type artist: str | None
        :param limit: How many responses to get? 
        :type limit: int
        :return: `response.json()`
        :rtype: dict[Any, Any]
        """
        print("\nSearching...")

        q = f"track:{track}"
        if artist:
            q += f" artist:{artist}"

        endpoint = "https://api.spotify.com/v1/search"
        query = {
            "q": q,
            "type": "track",
            "limit": limit
        }
        response = requests.get(
            url=endpoint, params=query, headers=self.auth.auth_headers)
        response.raise_for_status()
        data = response.json()["tracks"]["items"][0]

        artists = data["artists"]
        if data:
            print("Found track!")
            print(f"Track: {data["name"]}")
            print(
                f"Artist: {", ".join([artist['name'] for artist in artists])}")
            print(f"Album: {data["album"]["name"]}")
        else:
            print(f"{track} by {artist} not found.")

        return data


class SpotifyAuth:
    def __init__(self):
        self.client_id = os.getenv("SPOTIFY_CLIENT_ID")
        self.client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
        self.scopes = "playlist-read-private playlist-modify-private playlist-modify-public"
        self._base_url = "https://api.spotify.com."
        self.creds = self._get_set_credentials()
        self.base64_auth = self._build_base64_auth()
        self.request_user_authorization()
        self.auth_headers = self._build_auth_headers()

    def _get_set_credentials(self) -> dict:
        if not Path.exists(credentials_path):
            return {}

        with open(credentials_path) as f:
            creds = json.load(fp=f)
        return creds

    def _build_auth_headers(self):
        if not self.creds:
            return {}

        token_type = self.creds["token_type"]
        access_token = self.creds["access_token"]
        token = f"{token_type}  {access_token}"
        header = {
            "Authorization": token
        }

        return header

    def _get_auth_code(self, state: str):
        redirect_uri = input("Paste the FULL redirect URL here: ")

        parsed_url = urlparse(redirect_uri)
        params = parse_qs(parsed_url.query)

        returned_state = params.get("state", [None])[0]
        if returned_state != state:
            raise Exception(
                "Security Error: State mismatch! The request may have been tampered with.")

        code = params.get("code", [None])[0]
        if not code:
            raise Exception("Failed to find 'code' in the URL.")

        return code

    def _build_base64_auth(self):
        auth_str = f"{self.client_id}:{self.client_secret}"

        auth_bytes = auth_str.encode("utf-8")
        auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

        return f"Basic {auth_base64}"

    def request_user_authorization(self):
        if self.creds and "refresh_token" in self.creds:
            print("Using existing token...")
            self.refresh_access_token()
            return

        endpoint = "https://accounts.spotify.com/authorize"
        redirect_uri = "https://example.com"
        state = secrets.token_hex(16)

        query = {
            "client_id": self.client_id,
            "response_type": "code",
            "redirect_uri": "https://example.com",
            "scope": self.scopes,
            "state": state
        }

        response = requests.Request(
            "GET", url=endpoint, params=query).prepare()

        print(f"Opening browser for authorization...")
        webbrowser.open(response.url)  # type: ignore

        code = self._get_auth_code(state=state)

        self.request_access_token(code, redirect_uri)

    def request_access_token(self, code: str, redirect_uri: str):
        print("Requesting access token...")
        endpoint = "https://accounts.spotify.com/api/token"
        query = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": redirect_uri
        }

        header = {
            "Authorization": self.base64_auth,
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = requests.post(url=endpoint, data=query, headers=header)
        response.raise_for_status()
        data = response.json()
        print("Successfully acquired access token!")

        with open(credentials_path, "w") as f:
            json.dump(obj=data, fp=f, indent=2)

        print(f"Access token saved to: {credentials_path}")

    def refresh_access_token(self):
        print("Refreshing access token...")
        endpoint = "https://accounts.spotify.com/api/token"
        query = {
            "grant_type": "refresh_token",
            "refresh_token": self.creds["refresh_token"]
        }

        header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": self.base64_auth
        }

        response = requests.post(url=endpoint, data=query, headers=header)
        response.raise_for_status()
        data = response.json()

        self.creds["access_token"] = data["access_token"]
        self.creds["expires_in"] = data["expires_in"]
        self.creds["token_type"] = data["token_type"]
        self.creds["scope"] = data["scope"]

        if "refresh_token" in data:
            self.creds["refresh_token"] = data["refresh_token"]
            print("Received new refresh token from Spotify.")

        with open(credentials_path, "w") as f:
            json.dump(obj=self.creds, fp=f, indent=2)
        print(f"New access token saved to: {credentials_path}")
