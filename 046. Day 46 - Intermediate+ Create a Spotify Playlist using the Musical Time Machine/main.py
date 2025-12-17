import requests
from bs4 import BeautifulSoup
from datetime import datetime
from spotify import SpotifyClient


# while True:
#     date = input("What date do you want to go back to (format: YYYY-MM-DD)? ")
#     try:
#         date = str(datetime.strptime(date, "%Y-%m-%d").date())
#         break
#     except ValueError:
#         print("Invalid date, use YYYY-MM-DD")

spotify_client = SpotifyClient()

spotify_client.create_playlist(
    name="Vibes Only", description="Nostalgic songs", is_public=False)

# date = "2004-02-01"

# header = {
#     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
# }
# response = requests.get(
#     f"https://www.billboard.com/charts/hot-100/{date}/", headers=header)
# webpage = response.text

# soup = BeautifulSoup(webpage, "html.parser")

# song_titles = soup.select(".o-chart-results-list-row .c-title")
# for i, song in enumerate(song_titles, 1):
#     print(f"{i}. {song.get_text().strip()}")
