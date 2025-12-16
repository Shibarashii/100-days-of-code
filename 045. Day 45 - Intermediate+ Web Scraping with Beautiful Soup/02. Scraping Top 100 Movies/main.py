from bs4 import BeautifulSoup
from pathlib import Path
import requests
import os

root = Path(__file__).parent

# response = requests.get(
#     "https://letterboxd.com/brianformo/list/top-100-of-the-21st-century-so-far/")
# response.raise_for_status()

# webpage = response.text

with open(root/"top100.html") as f:
    webpage = f.read()

soup = BeautifulSoup(webpage, "html.parser")

titles = soup.select(".frame-title")


path = root/"movies.txt"
if path.exists():
    path.unlink()

with open(root/"movies.txt", "a") as f:
    for i, title in enumerate(titles, 1):
        title_text = " ".join(title.get_text().split())  # removes white spaces
        f.write(f"{i}. {title_text}\n")
