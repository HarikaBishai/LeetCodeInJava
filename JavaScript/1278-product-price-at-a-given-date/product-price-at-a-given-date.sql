# Write your MySQL query statement below
with ranked AS (

    SELECT *,
        ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS rn
    FROM products
    WHERE change_date<='2019-08-16'
)

SELECT
p.product_id , IFNULL(r.new_price,10) AS price
FROM (SELECT distinct product_id FROM products) p
LEFT JOIN ranked r
ON p.product_id = r.product_id AND r.rn = 1
