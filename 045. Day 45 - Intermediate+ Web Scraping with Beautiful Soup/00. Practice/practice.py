from pathlib import Path
from bs4 import BeautifulSoup

root = Path(__file__).parent

with open(root/"website.html", "r") as f:
    content = f.read()


soup = BeautifulSoup(content, "html.parser")

# print(soup.prettify())
# print(soup.title.string)


all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    print(tag.get_text())
    print(tag.get("href"))
    print("")

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.name)


company_url = soup.select_one(selector=".heading")
print(company_url.get_text())
