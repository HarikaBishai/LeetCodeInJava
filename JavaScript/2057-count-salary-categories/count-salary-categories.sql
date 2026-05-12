# Write your MySQL query statement below

WITH categories AS (
    SELECT 'Low Salary' AS category
    UNION
    SELECT 'Average Salary'
    UNION
    SELECT 'High Salary'
),

categorized AS (
    SELECT account_id,
        CASE 
            WHEN income < 20000 THEN 'Low Salary'
            WHEN income >= 20000 AND income <= 50000  THEN 'Average Salary'
            WHEN income > 50000 THEN 'High Salary'
        END AS category
    FROM accounts
)

SELECT 
    c.category, COUNT(cz.account_id) AS accounts_count
FROM categories c
LEFT JOIN categorized cz
ON c.category = cz.category
GROUP BY c.category