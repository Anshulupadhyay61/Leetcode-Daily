# Write your MySQL query statement below
select customer_number from Orders 
group by customer_number 
ORDER BY COUNT(*) DESC
LIMIT 1;