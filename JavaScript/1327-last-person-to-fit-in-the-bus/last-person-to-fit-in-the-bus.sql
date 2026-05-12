# Write your MySQL query statement below
WITH ranked as (SELECT 
*,
SUM(weight) OVER (ORDER BY turn) as rn

FROM queue
)
SELECT person_name
FROM ranked
WHERE rn <= 1000
ORDER BY turn DESC
LIMIT 1


