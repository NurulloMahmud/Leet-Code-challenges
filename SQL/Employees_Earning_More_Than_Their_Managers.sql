/*
181. Employees Earning More Than Their Managers
Table: Employee
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |
+-------------+---------+

Write a solution to find the employees who earn more than their managers.

https://leetcode.com/problems/employees-earning-more-than-their-managers/description/
*/

-- we use self join to compare the salaries
select e1.name Employee
from employee e1
join employee e2
    on e2.id = e1.managerId
where e1.salary>e2.salary