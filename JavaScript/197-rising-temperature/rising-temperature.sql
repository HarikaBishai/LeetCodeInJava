# Write your MySQL query statement below

SELECT w1.id
FROM weather w1
WHERE w1.temperature >
(SELECT temperature 
FROM weather w2
WHERE w2.recordDate = w1.recordDate - INTERVAL 1 DAY)