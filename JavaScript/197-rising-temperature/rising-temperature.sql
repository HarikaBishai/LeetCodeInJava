# Write your MySQL query statement below
SELECT f.id FROM 
(
    SELECT id, recordDate, temperature,
    LAG(temperature) OVER (ORDER BY recordDate) AS prevTemp,
    LAG(recordDate) OVER (ORDER BY recordDate) AS prevDate
FROM Weather) AS f
WHERE f.temperature > f.prevTemp
AND DATEDIFF(f.recordDate, f.prevDate) = 1
;
