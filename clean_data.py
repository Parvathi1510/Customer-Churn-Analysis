import pandas as pd

# Load the original dataset
df = pd.read_csv("data/Telco-Customer-Churn.csv")

print("Original rows:", len(df))

# Remove duplicate records
df = df.drop_duplicates()

# Remove unnecessary spaces from column names
df.columns = df.columns.str.strip()

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"], errors="coerce"
)

# Check missing values
print("\nMissing values before handling:")
print(df.isnull().sum())

# Remove rows where TotalCharges is missing
df = df.dropna(subset=["TotalCharges"])

# Save the cleaned dataset
df.to_csv("data/cleaned_churn.csv", index=False)

print("\nCleaning completed!")
print("Cleaned rows:", len(df))
print("Cleaned dataset saved to data/cleaned_churn.csv")