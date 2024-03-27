# Write your MySQL query statement below
select w1.id from Weather w1, Weather w2 where DATE_SUB(w1.recordDate, INTERVAL 1 DAY) = w2.recordDate and w1.temperature > w2.temperature;