# Write your MySQL query statement below
WITH cte AS
(SELECT machine_id, process_id,
    MIN(CASE WHEN activity_type = 'start' THEN timestamp END) AS start_time,
    MAX(CASE WHEN activity_type = 'end' THEN timestamp END) AS end_time
FROM activity
GROUP BY machine_id, process_id)
SELECT machine_id , ROUND(AVG(end_time-start_time), 3) AS processing_time
FROM cte
GROUP BY machine_id

-- WITH cte AS (SELECT machine_id, process_id,
--     CASE WHEN activity_type = 'start' THEN timestamp END AS start_time,
--     CASE WHEN activity_type = 'end' THEN timestamp END AS end_time
-- FROM activity)

-- SELECT machine_id,  (end_time - start_time)/COUNT(process_id)
-- FROM cte 
-- GROUP BY machine_id
