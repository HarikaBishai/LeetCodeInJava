# Write your MySQL query statement below
WITH friends AS (
    SELECT accepter_id AS id FROM RequestAccepted
    UNION ALL
    SELECT requester_id as id FROM RequestAccepted
)

SELECT id, COUNT(*) AS num
FROM friends
GROUP BY id
ORDER BY num desc
LIMIT 1
