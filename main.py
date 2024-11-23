# Step 1
import pandas as pd

# Step 2
#df = pd.read_csv('C:/Users/tasne/Documents/Code/owo/bestsellerswithcategories.csv')
df= pd.read_csv('C:/Users/tasne/Documents/Code\owo/Engineering_books_data.csv')

# Step 3
# Get the first 5 rows of the spreadsheet
print(df.head())

# Get the shape of the spreadsheet
print(df.shape)

# Get the column names of the spreadsheet
print(df.columns)

# Get summary statistics for each column
print(df.describe())

# Step 4
df.drop_duplicates(inplace=True)

df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)

df["Price"] = df["Price"].astype(float)


# Step 5
author_counts = df['Author'].value_counts()
print(author_counts)

avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)

#step 6
# Export top selling authors to a CSV file
author_counts.head(10).to_csv("top_authors.csv")

# Export average rating by genre to a CSV file
avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")