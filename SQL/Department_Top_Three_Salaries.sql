/*
185. Department Top Three Salaries

Table: Employee
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+-------------+---------+

Table: Department
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
A company's executives are interested in seeing who earns the most money in each of the company's departments. 
A high earner in a department is an employee who has a salary in the top three unique salaries for that department.
Write a solution to find the employees who are high earners in each of the departments.

Return the result table in any order.
*/

-- we use CTE to gather data we need
WITH cte AS (
    SELECT
        e.DepartmentId,
        e.Name AS Employee,
        e.Salary,
        d.Name AS Department,
        DENSE_RANK() OVER (PARTITION BY e.DepartmentId ORDER BY e.Salary DESC) AS Rank -- using window function to group by dep and get highest salaries
    FROM Employee e
    JOIN Department d ON e.DepartmentId = d.Id
)

SELECT Department, Employee, Salary
FROM cte
WHERE Rank <= 3
order by salary desc;



-- Another alternative solution would be in postgresql without window function
-- This method is easier to read in my opinion

SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM department AS d
JOIN employee AS e
  ON e.departmentId = d.id
WHERE d.id = 1 AND e.salary IN (    -- we just specify what the salaries should be
  SELECT DISTINCT salary 
  FROM employee 
  WHERE departmentId = 1
  ORDER BY salary DESC
  LIMIT 3
)
UNION   -- we do the same for second dep as well and join the results
SELECT d.name, e.name, e.salary
FROM department AS d
JOIN employee AS e
  ON e.departmentId = d.id
WHERE d.id = 2 AND e.salary IN (
  SELECT DISTINCT salary 
  FROM employee 
  WHERE departmentId = 2
  ORDER BY salary DESC
  LIMIT 3
);

-- https://leetcode.com/problems/department-top-three-salaries/description/