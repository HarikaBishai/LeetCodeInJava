# Write your MySQL query statement below
SELECT e1.name FROM Employee e1
WHERE 5 <= (
    SELECT count(*) FROM Employee e2
    WHERE e1.id = e2.managerId
)
