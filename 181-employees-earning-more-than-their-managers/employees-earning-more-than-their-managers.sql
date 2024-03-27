# Write your MySQL query statement below
select e.name Employee 
from Employee e join Employee m on m.id = e.managerId
where e.salary > m.salary;