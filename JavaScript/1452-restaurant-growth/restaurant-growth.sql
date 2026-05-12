# Write your MySQL query statement below

WITH daily as (
    SELECT visited_on, sum(amount) AS amount
    FROM customer
    GROUP BY visited_on
),

rolling as (SELECT visited_on , 
    ROUND(SUM(amount) OVER (
            ORDER BY visited_on
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ), 2) AS amount, 
    
    ROUND(AVG(amount) OVER (
            ORDER BY visited_on
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ), 2) AS average_amount,

    ROW_NUMBER() OVER (ORDER BY visited_on) as rn
    FROM daily
)
SELECT visited_on, amount, average_amount
FROM rolling
WHERE rn >= 7


