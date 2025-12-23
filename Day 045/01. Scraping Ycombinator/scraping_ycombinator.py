from bs4 import BeautifulSoup
import requests


response = requests.get(url="https://news.ycombinator.com/news")
yc_webpage = response.text


soup = BeautifulSoup(yc_webpage, "html.parser")
article_titles = soup.select(selector=".titleline > a")

subtexts = soup.select(selector=".subtext")

scores = []
for subtext in subtexts:
    score_raw = subtext.select_one(".score")
    if score_raw is None:
        scores.append(0)
    else:
        score = score_raw.get_text().split()[0]
        scores.append(int(score))

for i in range(len(article_titles)):
    print(f"Title: {article_titles[i].get_text()}")
    print(f"Link: {article_titles[i].get("href")}")
    print(f"Score: {scores[i]}")
    print("")

max_score = max(scores)
max_index = scores.index(max_score)
max_article = article_titles[max_index].get_text()

print(f"Article with highest upvotes: {max_article}")
print(f"Score: {max_score}")
