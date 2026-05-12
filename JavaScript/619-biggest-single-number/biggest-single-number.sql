# Write your MySQL query statement below


WITH cte AS (SELECT num, COUNT(*) OVER(PARTITION BY num) as counter
FROM myNumbers)

SELECT max(num) as num
FROM cte
WHERE counter = 1