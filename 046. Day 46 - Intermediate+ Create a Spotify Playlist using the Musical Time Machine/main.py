from spotify import SpotifyClient
from ui import *


def main():
    spotify_client = SpotifyClient()

    date = prompt_date()
    tracks = get_tracks_from_date(date)
    playlist_id = prompt_create_playlist(spotify_client)

    add_tracks_to_playlist(spotify_client, playlist_id, tracks)


if __name__ == "__main__":
    main()
