# Write your MySQL query statement below
-- with cte as (SELECT
-- num,
-- LAG(num, 1) OVER (ORDER BY ID) as prev,
-- LAG(num, 2) OVER (ORDER BY ID) as prev1
-- FROM logs)

-- SELECT Distinct(num) as ConsecutiveNums
-- FROM cte
-- WHERE num = prev AND prev = prev1


-- SELECT DISTINCT(l1.num) as ConsecutiveNums
-- FROM logs l1
-- JOIN logs l2
-- ON l1.id = l2.id - 1 AND l1.num = l2.num
-- JOIN logs l3
-- ON l2.id = l3.id - 1 AND l2.num = l3.num



WITH numbered AS (
    SELECT id, num,
    ROW_NUMBER() OVER (ORDER BY id) as rn_all,
    ROW_NUMBER() OVER (PARTITION BY num ORDER BY id) as rn_num
    FROM logs
),
grouped AS (
SELECT num, rn_all - rn_num as grp
FROM numbered
)

SELECT DISTINCT num as ConsecutiveNums
FROM grouped
GROUP BY num, grp
HAVING count(*) >= 3
