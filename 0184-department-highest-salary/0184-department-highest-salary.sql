# Write your MySQL query statement below
SELECT
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM Employee e
JOIN Department d
    ON e.departmentId = d.id
JOIN (
    SELECT
        departmentId,
        MAX(salary) AS max_salary
    FROM Employee
    GROUP BY departmentId
) AS temp
    ON e.departmentId = temp.departmentId
    AND e.salary = temp.max_salary;