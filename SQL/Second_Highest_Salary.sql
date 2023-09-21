/*
176. Second Highest Salary

Write a solution to find the second highest salary from the Employee table. 
If there is no second highest salary, return null (return None in Pandas).

*/

select max(salary) SecondHighestSalary
from employee e
where salary < (select max(salary) from employee);

-- Runtime: Beats 95.62%of users with MySQL || Memory: Beats 100.00%of users with MySQL
-- https://leetcode.com/problems/second-highest-salary/description/