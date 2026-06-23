import pandas as pd

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Dataset Information
shape = df.shape
columns = df.columns.tolist()
missing_values = df.isnull().sum()
type_counts = df["type"].value_counts()

# Fill missing values
df.fillna("Unknown", inplace=True)

# Top Countries
top_countries = df["country"].value_counts().head(10)

# Top Ratings
top_ratings = df["rating"].value_counts()

# Release Years
top_years = df["release_year"].value_counts().head(10)

# Save everything to output.txt
with open("output.txt", "w", encoding="utf-8") as f:

    f.write("NETFLIX EXPLORATORY DATA ANALYSIS REPORT\n")
    f.write("=" * 60 + "\n\n")

    f.write("1. DATASET SHAPE\n")
    f.write(str(shape))
    f.write("\n\n")

    f.write("2. COLUMN NAMES\n")
    for col in columns:
        f.write(col + "\n")
    f.write("\n")

    f.write("3. MISSING VALUES\n")
    f.write(str(missing_values))
    f.write("\n\n")

    f.write("4. MOVIES VS TV SHOWS\n")
    f.write(str(type_counts))
    f.write("\n\n")

    f.write("5. TOP 10 CONTENT PRODUCING COUNTRIES\n")
    f.write(str(top_countries))
    f.write("\n\n")

    f.write("6. CONTENT RATINGS DISTRIBUTION\n")
    f.write(str(top_ratings))
    f.write("\n\n")

    f.write("7. TOP 10 RELEASE YEARS\n")
    f.write(str(top_years))
    f.write("\n\n")

print("EDA Report saved successfully in output.txt")