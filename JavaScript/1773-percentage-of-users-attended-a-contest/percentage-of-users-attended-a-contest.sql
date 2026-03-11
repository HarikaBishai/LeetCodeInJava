# Write your MySQL query statement below



Select contest_id , ROUND((count(user_id) / (SELECT count(*) FROM USERS)) * 100, 2) AS percentage FROM Register

GROUP BY contest_id
ORDER BY percentage DESC,  contest_id ; 
