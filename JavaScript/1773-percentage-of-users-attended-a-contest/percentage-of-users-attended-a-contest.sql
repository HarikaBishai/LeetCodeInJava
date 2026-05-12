/* Write your T-SQL query statement below */
-- WITH total_users AS (
-- SELECT SUM(1) as user_count FROM users)
-- SELECT 
-- contest_id , ROUND(count(user_id) * 100.0 / user_count , 2) as percentage

-- FROM register 
-- CROSS JOIN total_users
-- GROUP BY contest_id
-- ORDER BY percentage DESC, contest_id 


SELECT contest_id, ROUND(count(*) * 100.0/ (SELECT SUM(1) as user_count FROM users), 2) AS percentage
FROM register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id 

