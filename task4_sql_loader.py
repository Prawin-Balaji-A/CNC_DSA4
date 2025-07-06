import pandas as pd
import sqlite3

# Load cleaned data
df_clean = pd.read_csv("cleaned_data.csv")  # Use the file saved from Task 2

# Create SQLite DB connection
conn = sqlite3.connect("data_analytics.db")

# Write DataFrame to SQL table
df_clean.to_sql("cleaned_data", conn, if_exists="replace", index=False)

print("✅ Data saved into SQLite database (data_analytics.db).")

# Example SQL query
query_result = pd.read_sql_query("SELECT * FROM cleaned_data LIMIT 5", conn)
print("\nSample Records from SQL Table:\n", query_result)

conn.close()
