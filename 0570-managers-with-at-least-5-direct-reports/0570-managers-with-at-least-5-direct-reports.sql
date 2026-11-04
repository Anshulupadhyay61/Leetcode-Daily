# Write your MySQL query statement below
select m.name as name
from employee e
join employee m
on e.managerId = m.id
GROUP BY m.id,m.name
HAVING COUNT(*) >= 5;