# visualize.py

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("crime_news.csv")

df["Length"] = df["Headline"].apply(len)

plt.figure(figsize=(10,6))

plt.hist(df["Length"], bins=10)

plt.title("Crime News Headline Length Distribution")
plt.xlabel("Headline Length")
plt.ylabel("Frequency")

plt.tight_layout()

plt.show()