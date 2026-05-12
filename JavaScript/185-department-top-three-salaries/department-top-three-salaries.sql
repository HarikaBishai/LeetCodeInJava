# Write your MySQL query statement below
WITH ranked as (SELECT *,
    DENSE_RANK() OVER (partition by departmentId ORDER BY salary DESC) AS rn
    FROM Employee
    )

SELECT d.name as Department, r.name as Employee, r.salary as Salary
FROM 
Department d
LEFT JOIN ranked r
ON d.id = r.departmentId
WHERE rn <= 3