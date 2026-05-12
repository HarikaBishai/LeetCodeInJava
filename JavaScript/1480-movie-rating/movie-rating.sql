# Write your MySQL query statement below


WITH highest_ratings AS (SELECT u.name
FROM users u
LEFT JOIN movieRating m
ON u.user_id = m.user_id
GROUP BY u.user_id, u.name
ORDER BY count(movie_id) DESC, u.name
LIMIT 1),
highest_avg as (

    SELECT m.title

    FROM movieRating mr
    JOIN movies m
    ON mr.movie_id = m.movie_id
    WHERE MONTH(mr.created_at) = 2 AND YEAR(mr.created_at) = 2020
    GROUP BY mr.movie_id, m.title
    ORDER BY AVG(mr.rating)  DESC,  m.title
    LIMIT 1

)

SELECT name AS results FROM highest_ratings
UNION ALL
SELECT title AS results FROM highest_avg


