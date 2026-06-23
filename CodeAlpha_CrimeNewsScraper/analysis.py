# analysis.py

import pandas as pd

df = pd.read_csv("crime_news.csv")

print("\nTotal Headlines:", len(df))

df["Length"] = df["Headline"].apply(len)

print("\nAverage Headline Length:")
print(df["Length"].mean())

print("\nTop 10 Headlines:")
print(df.head(10))