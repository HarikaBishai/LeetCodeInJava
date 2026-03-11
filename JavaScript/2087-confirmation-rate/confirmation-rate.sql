# Write your MySQL query statement below

SELECT s.user_id,  IFNULL(ROUND(confirm_count.count/total.count, 2), 0) AS confirmation_rate FROM Signups s
LEFT JOIN ( select user_id, count(*) as count FROM confirmations  GROUP BY user_id) total ON s.user_id = total.user_id
LEFT JOIN ( select user_id,action, count(*) as count FROM confirmations WHERE action='confirmed' GROUP BY user_id ) confirm_count ON s.user_id = confirm_count.user_id
GROUP BY s.user_id
ORDER BY confirmation_rate
