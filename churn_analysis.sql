-- 1. Total customers
SELECT COUNT(*) AS total_customers
FROM customers;

-- 2. Customers who left and stayed
SELECT Churn, COUNT(*) AS customer_count
FROM customers
GROUP BY Churn;

-- 3. Overall churn rate
SELECT
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*), 2
    ) AS churn_rate_percentage
FROM customers;

-- 4. Churn by contract type
SELECT
    Contract,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers
FROM customers
GROUP BY Contract
ORDER BY churned_customers DESC;