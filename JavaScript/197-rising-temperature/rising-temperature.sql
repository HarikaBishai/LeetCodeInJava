# Write your MySQL query statement below

-- SELECT w1.id
-- FROM weather w1
-- WHERE w1.temperature >
-- (SELECT temperature 
-- FROM weather w2
-- WHERE w2.recordDate = w1.recordDate - INTERVAL 1 DAY)


with cte AS (

    SELECT id, recordDate, temperature,
        LAG(temperature) OVER(ORDER BY recordDate) as prev_temp,
        LAG(recordDate) OVER(ORDER BY recordDate) as prev_date
    FROM weather

)
SELECT id
FROM cte
WHERE temperature > prev_temp AND recordDate = prev_date + INTERVAL 1 DAY