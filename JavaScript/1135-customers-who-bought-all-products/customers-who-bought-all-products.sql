# Write your MySQL query statement below

SELECT grp.customer_id
FROM 
(
    SELECT customer_id, COUNT(DISTINCT product_key) as cnt
    FROM Customer
    GROUP BY customer_id
) AS grp
where grp.cnt = (SELECT COUNT(*) FROM product) 
