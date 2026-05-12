# Write your MySQL query statement below


WITH highest_ratings AS (SELECT u.user_id, u.name, count(DISTINCT movie_id) as cnt
FROM users u
LEFT JOIN movieRating m
ON u.user_id = m.user_id
GROUP BY u.user_id, u.name
ORDER BY cnt DESC, u.name
LIMIT 1),
highest_avg as (

    SELECT mr.movie_id, m.title, AVG(rating) as avg_rating

    FROM movieRating mr
    JOIN movies m
    ON mr.movie_id = m.movie_id
    WHERE MONTH(mr.created_at) = 2 AND YEAR(mr.created_at) = 2020
    GROUP BY mr.movie_id, m.title
    ORDER BY avg_rating DESC,  m.title
    LIMIT 1

)

SELECT name AS results FROM highest_ratings
UNION ALL
SELECT title AS results FROM highest_avg


