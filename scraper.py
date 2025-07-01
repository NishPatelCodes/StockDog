import requests
from bs4 import BeautifulSoup
company_name = "Google"

url = (f"https://techcrunch.com/?s={company_name}")
r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
newsLink = {}

for news in soup.find_all(class_="loop-card__title-link"):
    newsLink[news.get("data-destinationlink")] = news.get_text(strip=True)
print(newsLink)

