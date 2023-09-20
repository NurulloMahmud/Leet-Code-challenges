/*
-- 570. Managers with at Least 5 Direct Reports

Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+

Write a solution to find managers with at least five direct reports.

https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/?envType=study-plan-v2&envId=top-sql-50
*/


select name
from employee e
where id in (
    select managerId
    from employee
    group by managerId
    having count(managerId)>=5  
);

-- Memory: Beats 100.00%of users with MySQL
-- Runtime: Beats 56.31%of users with MySQL