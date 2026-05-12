# Write your MySQL query statement below
with cte as (SELECT
num,
LAG(num, 1) OVER (ORDER BY ID) as prev,
LAG(num, 2) OVER (ORDER BY ID) as prev1
FROM logs)

SELECT Distinct(num) as ConsecutiveNums
FROM cte
WHERE num = prev AND prev = prev1