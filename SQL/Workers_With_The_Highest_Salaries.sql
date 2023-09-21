/*
Workers With The Highest Salaries.

You have been asked to find the job titles of the highest-paid employees.
Your output should include the highest-paid title or multiple titles with the same salary.

https://platform.stratascratch.com/coding/10353-workers-with-the-highest-salaries?code_type=1
*/

select t.worker_title as best_paid_title
from worker w
join title t
    on t.worker_ref_id = w.worker_id
where salary = (select max(salary) from worker)