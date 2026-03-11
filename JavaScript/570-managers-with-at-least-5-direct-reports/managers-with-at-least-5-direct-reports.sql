# Write your MySQL query statement below
SELECT e1.name FROM Employee e1
WHERE e1.id IN (
    SELECT e2.managerId FROM Employee e2
    WHERE e1.id = e2.managerId
    GROUP BY e2.managerId
    HAVING COUNT(*) >= 5
)
