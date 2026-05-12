# Write your MySQL query statement below



WITH CTE AS (SELECT * FROM delivery d1
WHERE order_date = 
(SELECT order_date
FROM delivery d2
WHERE d1.customer_id = d2.customer_id
ORDER BY order_date
LIMIT 1
))
SELECT ROUND(SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END)*100.0 / count(*), 2) AS immediate_percentage
FROM cte
