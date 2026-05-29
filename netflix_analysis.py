
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------
# Configuration
# ---------------------------
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

DATA_PATH = "data/netflix_titles.csv"
OUTPUT_FOLDER = "outputs"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ---------------------------
# Load Dataset
# ---------------------------
print("Loading dataset...")

df = pd.read_csv(DATA_PATH)

print("\nDataset Loaded Successfully")
print(df.head())

# ---------------------------
# Data Cleaning
# ---------------------------
print("\nCleaning dataset...")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Fill missing values
df["country"] = df["country"].fillna("Unknown")
df["director"] = df["director"].fillna("Not Available")
df["cast"] = df["cast"].fillna("Not Available")
df["rating"] = df["rating"].fillna("Unknown")
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

# Extract year and month
df["year_added"] = df["date_added"].dt.year
df["month_added"] = df["date_added"].dt.month_name()

print("\nMissing Values After Cleaning:\n")
print(df.isnull().sum())

# ---------------------------
# Basic Information
# ---------------------------
print("\nDataset Information:\n")
print(df.info())

print("\nSummary Statistics:\n")
print(df.describe(include="all"))

# ---------------------------
# Content Type Distribution
# ---------------------------
plt.figure(figsize=(8, 5))

content_counts = df["type"].value_counts()

sns.barplot(
    x=content_counts.index,
    y=content_counts.values
)

plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Content Type")
plt.ylabel("Count")

plt.tight_layout()
plt.savefig(f"{OUTPUT_FOLDER}/content_type_distribution.png")
plt.close()

# ---------------------------
# Release Year Trend
# ---------------------------
release_trend = df["release_year"].value_counts().sort_index()

plt.figure(figsize=(14, 6))

sns.lineplot(
    x=release_trend.index,
    y=release_trend.values
)

plt.title("Netflix Content Release Trend")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.tight_layout()
plt.savefig(f"{OUTPUT_FOLDER}/release_trend.png")
plt.close()

# ---------------------------
# Top Genres
# ---------------------------
genres = df["listed_in"].str.split(", ").explode()

top_genres = genres.value_counts().head(10)

plt.figure(figsize=(12, 6))

sns.barplot(
    x=top_genres.values,
    y=top_genres.index
)

plt.title("Top 10 Genres on Netflix")
plt.xlabel("Count")
plt.ylabel("Genre")

plt.tight_layout()
plt.savefig(f"{OUTPUT_FOLDER}/top_genres.png")
plt.close()

# ---------------------------
# Ratings Distribution
# ---------------------------
rating_counts = df["rating"].value_counts().head(10)

plt.figure(figsize=(10, 5))

sns.barplot(
    x=rating_counts.index,
    y=rating_counts.values
)

plt.title("Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig(f"{OUTPUT_FOLDER}/ratings_distribution.png")
plt.close()

# ---------------------------
# Top Countries Producing Content
# ---------------------------
countries = df["country"].str.split(", ").explode()

top_countries = countries.value_counts().head(10)

plt.figure(figsize=(12, 6))

sns.barplot(
    x=top_countries.values,
    y=top_countries.index
)

plt.title("Top 10 Content Producing Countries")
plt.xlabel("Number of Titles")
plt.ylabel("Country")

plt.tight_layout()
plt.savefig(f"{OUTPUT_FOLDER}/top_countries.png")
plt.close()

# ---------------------------
# Key Insights
# ---------------------------
print("\nKey Insights:\n")

most_common_genre = top_genres.index[0]
top_country = top_countries.index[0]

print(f"1. Most content on Netflix consists of: {content_counts.idxmax()}")
print(f"2. Most common genre: {most_common_genre}")
print(f"3. Top content-producing country: {top_country}")
print(f"4. Total titles available: {len(df)}")

print("\nAnalysis Completed Successfully!")
print(f"Visualizations saved inside '{OUTPUT_FOLDER}' folder.")
