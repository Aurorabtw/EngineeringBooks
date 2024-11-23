# Step 1: Import required library
import pandas as pd

# Step 2: Load the CSV file
df = pd.read_csv('C:/Users/tasne/Documents/Code/Project/bestsellers_with_categories.csv')

# Step 3: Initial exploration
print(df.head())  # First 5 rows
print(df.shape)  # Shape of the data
print(df.columns)  # Column names
print(df.describe())  # Summary statistics

# Step 4: Clean and preprocess the dataset
df.drop_duplicates(inplace=True)  # Remove duplicates
df["Price"] = df["Price"].astype(float)  # Convert Price to float
df.rename(columns={"Name": "Title", "User Rating": "Rating", "Year": "Publication Year"}, inplace=True)  # Rename columns

# Step 5: Analyze the dataset
# Count occurrences of each author
author_counts = df['Author'].value_counts()
print(author_counts)

# Calculate the average rating by genre
avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)

# Step 6: Export results
author_counts.head(10).to_csv("top_authors.csv")  # Export top authors
avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")  # Export average rating by genre
