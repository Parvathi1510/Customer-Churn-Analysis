import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("churn.db")

queries = {
    "Customer Count": """
        SELECT COUNT(*) AS total_customers
        FROM customers;
    """,

    "Churn Distribution": """
        SELECT Churn, COUNT(*) AS customer_count
        FROM customers
        GROUP BY Churn;
    """,

    "Overall Churn Rate": """
        SELECT ROUND(
            100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
            / COUNT(*), 2
        ) AS churn_rate_percentage
        FROM customers;
    """,

    "Churn by Contract": """
        SELECT
            Contract,
            COUNT(*) AS total_customers,
            SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
                AS churned_customers,
            ROUND(
                100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
                / COUNT(*), 2
            ) AS churn_rate_percentage
        FROM customers
        GROUP BY Contract
        ORDER BY churn_rate_percentage DESC;
    """
}

for title, query in queries.items():
    print("\n" + "=" * 45)
    print(title)
    print("=" * 45)

    result = pd.read_sql_query(query, conn)
    print(result.to_string(index=False))

conn.close()