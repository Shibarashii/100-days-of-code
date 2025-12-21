from spotify import SpotifyClient
from datetime import datetime
import requests
from bs4 import BeautifulSoup


def prompt_date() -> str:
    """
    Prompt user for the date they want to go back to.

    :return: The date in string format (YYYY-MM-DD)
    :rtype: str
    """
    while True:
        date = input(
            "\nWhat date do you want to go back to (format: YYYY-MM-DD)? ")
        try:
            date = str(datetime.strptime(date, "%Y-%m-%d").date())
            return date
        except ValueError:
            print("Invalid date, use YYYY-MM-DD.")


def prompt_create_playlist(client: SpotifyClient) -> str:
    """
    Prompt user for the params required to create a playlist.

    :param client: The spotify client
    :type client: SpotifyClient
    :return: ID of the created playlist 
    :rtype: str
    """
    print(f"Create your new playlist!")
    name = input("Playlist name: ")
    description = input("Description: ")
    is_public = input("Is public? y/n: ").lower().strip().startswith("y")
    is_collaborative = input(
        "Is collaborative? y/n: ").lower().strip().startswith("y")

    data = client.create_playlist(
        name, description, is_public, is_collaborative)

    return data["id"]


def get_tracks_from_date(date: str) -> dict[str, str]:
    """
    Get the tracks of the Billboards Hot100 from a specific date

    :param date: Date in format `YYYY-MM-DD`.
    :type date: str
    :return: A dictionary containing the track as key and artist as value .
    :rtype: dict[str, str]
    """
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
    }
    response = requests.get(
        f"https://www.billboard.com/charts/hot-100/{date}/", headers=header)
    webpage = response.text

    soup = BeautifulSoup(webpage, "html.parser")

    raw_tracks_html = soup.select(".o-chart-results-list-row .c-title")

    raw_artists_html = soup.select(".o-chart-results-list-row")
    artists = [row.select_one(".c-label a[href*='/artist/']")
               for row in raw_artists_html]

    tracks = {}

    for i, raw_track in enumerate(raw_tracks_html):
        track = raw_track.get_text().strip()
        tracks[track] = artists[i].get_text().strip(  # type: ignore
        ) if artists[i] is not None else None  # type: ignore

    return tracks


def add_tracks_to_playlist(client: SpotifyClient,
                           playlist_id: str,
                           tracks: dict[str, str]):
    """
    Adds tracks to a playlist.

    :param client: The Spotify client.
    :type client: SpotifyClient
    :param playlist_id: ID of the playlist
    :type playlist_id: str
    :param tracks: A dictionary of tracks, track:artist
    :type tracks: dict[str, str]
    """
    uris = []
    for track, artist in tracks.items():
        data = client.search_track(track, artist)
        uris.append(data["uri"])

    client.add_to_playlist(playlist_id, uris)
