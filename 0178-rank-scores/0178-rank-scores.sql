# Write your MySQL query statement below
select score,
dense_rank() over(ORDER BY score DESC) AS `rank`
from scores