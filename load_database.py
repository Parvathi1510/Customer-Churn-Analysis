import pandas as pd
import sqlite3

# Load cleaned data
df = pd.read_csv("data/cleaned_churn.csv")

# Connect to SQLite database
conn = sqlite3.connect("churn.db")

# Save data to a SQL table
df.to_sql("customers", conn, if_exists="replace", index=False)

print("Database created successfully!")
print("Rows loaded:", len(df))

conn.close()