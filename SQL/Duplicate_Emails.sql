/*
182. Duplicate Emails
Table: Person
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
Write a solution to report all the duplicate emails. 
Note that it's guaranteed that the email field is not NULL.
*/

select email
from person
group by email
having count(email)>1;