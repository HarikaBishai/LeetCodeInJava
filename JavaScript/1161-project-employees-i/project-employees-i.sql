# Write your MySQL query statement below
SELECT p.project_id, Round(AVG( e.experience_years), 2) AS average_years  FROM Project p
LEFT JOIN Employee e ON e.employee_id = p.employee_id
group by p.project_id
