# scraper.py

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.bbc.com/news"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.find_all(["h2", "h3"])

    data = []

    for headline in headlines:
        text = headline.get_text(strip=True)

        crime_keywords = [
            "crime",
            "murder",
            "police",
            "arrest",
            "fraud",
            "theft",
            "court",
            "investigation",
            "criminal",
            "violence"
        ]

        if any(word.lower() in text.lower() for word in crime_keywords):
            data.append(text)

    df = pd.DataFrame(data, columns=["Headline"])

    df.to_csv("crime_news.csv", index=False)

    print(f"{len(df)} crime-related headlines saved!")

else:
    print("Failed to access website.")