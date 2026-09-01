# Write your MySQL query statement below
select employee_id
from Employees e
where manager_id is not null
and salary < 30000
and not exists (
    select 1 from Employees e2
    where e.manager_id = e2.employee_id
)
order by employee_id;