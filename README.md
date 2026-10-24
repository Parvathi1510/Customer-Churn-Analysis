# Customer Churn Analysis

## Project Overview
This project analyzes customer churn for a telecommunications company using **Python, SQL, and Power BI**. The goal is to understand how many customers leave, explore patterns associated with churn, and present findings in an interactive dashboard.

## Business Objectives
- Calculate the total number of customers and the overall churn rate.
- Compare churn across contract types.
- Explore the relationship between monthly charges and churn.
- Provide clear, data-based findings that can help a business investigate customer retention.

## Tools and Technologies
- **Python:** data inspection, cleaning, and visualization
- **pandas:** data manipulation
- **Matplotlib and Seaborn:** charts
- **SQLite and SQL:** querying and aggregating customer data
- **Power BI Desktop:** interactive dashboard and KPI cards

## Dataset
The project uses the IBM Telco Customer Churn dataset. It contains customer and service information such as contract type, tenure, monthly charges, total charges, payment method, and churn status.

Original dataset source:  
[IBM Telco Customer Churn CSV](https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv)

The dataset is used for learning and portfolio demonstration. Check the source repository for its applicable terms and attribution details before redistributing the raw data.

## Project Workflow
1. **Inspect the data** — review the number of rows and columns, column names, missing values, and churn distribution.
2. **Clean the data** — remove duplicate rows, standardize column names, convert `TotalCharges` to a numeric type, and handle rows where `TotalCharges` is missing.
3. **Load into SQLite** — create `churn.db` and load the cleaned records into a `customers` table.
4. **Analyze with SQL** — calculate customer totals, churn distribution, churn rate, and churn by contract.
5. **Create charts with Python** — generate charts for churn distribution, churn rate by contract, and monthly charges by churn status.
6. **Build the Power BI report** — create KPI cards, contract and churn comparisons, and a Contract slicer to explore the data interactively.

## Repository Structure
```text
Customer-Churn-Analysis/
├── data/
│   ├── Telco-Customer-Churn.csv
│   └── cleaned_churn.csv
├── output/
│   ├── churn_distribution.png
│   ├── churn_by_contract.png
│   └── monthly_charges_by_churn.png
├── sql/
│   └── churn_analysis.sql
├── inspect_data.py
├── clean_data.py
├── load_database.py
├── run_sql_analysis.py
├── create_charts.py
├── requirements.txt
├── README.md
├── .gitignore
├── churn.db
└── Customer-Churn-Analysis.pbix
```

> Your actual files may differ slightly. Update this tree to match your folder. Do not commit `.venv/` or other unnecessary generated files.

## Setup and Run

### 1. Create and activate a virtual environment
Run these commands in the VS Code terminal from the project folder on Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell activation is blocked or does not work, you can run the scripts with the virtual-environment Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 2. Install Python packages
Create a `requirements.txt` file with:

```text
pandas
numpy
matplotlib
seaborn
```

Then install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

### 3. Place the source dataset
Save the downloaded CSV as:

```text
data/Telco-Customer-Churn.csv
```

### 4. Run the analysis scripts
Run these commands in order from the project root:

```powershell
python inspect_data.py
python clean_data.py
python load_database.py
python run_sql_analysis.py
python create_charts.py
```

If you use the virtual-environment Python directly, replace `python` with `.\.venv\Scripts\python.exe`.

### 5. Open the Power BI report
Open `Customer-Churn-Analysis.pbix` in Power BI Desktop. If needed, refresh or reconnect the report to `data/cleaned_churn.csv` on your own computer.

## Dashboard
The Power BI report is designed to include:
- **Total Customers** KPI
- **Churned Customers** KPI
- **Churn Rate** KPI
- **Churn Rate by Contract** chart
- **Average Monthly Charges by Churn Status** chart
- **Contract** slicer for interactive filtering
- A second page for additional churn insights, if included in your final report

## Key Findings
Add your verified results here after running the scripts and checking the Power BI report. For example:
- Which contract type has the highest churn rate?
- How does the average monthly charge compare for customers who left versus customers who stayed?
- What is the overall churn rate in the cleaned dataset?

Only include values that you have confirmed from your own analysis. If the cleaning script removes records with missing `TotalCharges`, report counts from the **cleaned** dataset, not the original CSV.

## Business Recommendations
Use the analysis to investigate possible retention actions, such as:
- Review the customer journey for contract groups with higher churn.
- Explore whether pricing, service experience, or payment preferences are associated with churn.
- Test suitable retention offers and measure their impact before adopting them broadly.

These are hypotheses to investigate, not proof that any one factor causes churn.

## Limitations
- This is an exploratory analysis of a sample dataset, not a live customer system.
- Associations in the data do not establish causation.
- Missing-value handling may affect the final row count and should be documented.
- Dashboard results depend on the version of the dataset and the measures used.

## Skills Demonstrated
- Data inspection and cleaning with Python
- Data manipulation with pandas
- SQL aggregation and analysis
- Data visualization
- KPI and dashboard design in Power BI
- Communicating findings and potential business actions

## Author
** DOPPALAPUDI SIVA PARVATHI **  
Aspiring Data Analyst


