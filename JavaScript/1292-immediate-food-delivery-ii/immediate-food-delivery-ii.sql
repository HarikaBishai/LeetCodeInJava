# Write your MySQL query statement below


/*
WITH CTE AS (SELECT * FROM delivery d1
WHERE order_date = 
(SELECT order_date
FROM delivery d2
WHERE d1.customer_id = d2.customer_id
ORDER BY order_date
LIMIT 1
))
SELECT ROUND(SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END)*100.0 / count(*), 2) AS immediate_percentage
FROM cte*/

/*
WITH CTE AS (
SELECT customer_id , MIN(order_date) as first_order
FROM delivery
GROUP BY customer_id)

SELECT 
    ROUND(SUM(CASE WHEN d.order_date = d.customer_pref_delivery_date THEN 1 ELSE 0 END)*100.0 / count(*), 2) AS immediate_percentage 
FROM delivery d
JOIN CTE c
ON d.customer_id = c.customer_id AND d.order_date = c.first_order

*/

WITH ranked AS (
    SELECT *, 
        ROW_NUMBER() OVER(
            PARTITION BY customer_id
            ORDER BY order_date)
        as rn
    FROM delivery
)
SELECT ROUND(SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END)*100.0 / count(*), 2) AS immediate_percentage
FROM ranked
WHERE rn = 1
