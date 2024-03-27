# Write your MySQL query statement below
WITH ranked_employees_by_salary AS (
    SELECT *, 
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS salary_rank
    FROM employee
)

SELECT 
    d.name as Department,
    r.name as Employee, 
    r.salary as Salary
FROM ranked_employees_by_salary r 
INNER JOIN department d ON r.departmentId = d.id
WHERE salary_rank <= 3