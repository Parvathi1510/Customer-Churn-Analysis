import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned data
df = pd.read_csv("data/cleaned_churn.csv")

# Create output folder if needed
os.makedirs("output", exist_ok=True)

sns.set_theme(style="whitegrid")

# Chart 1: Customer churn distribution
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="Churn")
plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("output/churn_distribution.png", dpi=300)
plt.close()

# Chart 2: Churn rate by contract type
contract_churn = (
    df.groupby("Contract")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .reset_index(name="ChurnRate")
    .sort_values("ChurnRate", ascending=False)
)

plt.figure(figsize=(8, 5))
sns.barplot(data=contract_churn, x="Contract", y="ChurnRate")
plt.title("Churn Rate by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Churn Rate (%)")
plt.tight_layout()
plt.savefig("output/churn_by_contract.png", dpi=300)
plt.close()

# Chart 3: Monthly charges by churn status
plt.figure(figsize=(7, 5))
sns.boxplot(data=df, x="Churn", y="MonthlyCharges")
plt.title("Monthly Charges by Churn Status")
plt.xlabel("Churn")
plt.ylabel("Monthly Charges")
plt.tight_layout()
plt.savefig("output/monthly_charges_by_churn.png", dpi=300)
plt.close()

print("Charts created successfully!")
print("Check the output folder for your three PNG files.")