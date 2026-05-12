# Write your MySQL query statement below
SELECT e1.employee_id

FROM employees e1
LEFT JOIN employees e2
ON e1.manager_id = e2.employee_id
WHERE e2.employee_id is NULL AND e1.salary < 30000 AND e1.manager_id IS NOT NULL

order by e1.employee_id