# Write your MySQL query statement below
WITH CTE AS (
SELECT DISTINCT
	request_at AS 'Day',
    CAST( COUNT(status) OVER(PARTITION BY request_at)  AS DECIMAL(10,2) ) TotalRequest, -- count total request by each day
    COUNT(CASE WHEN status IN ('cancelled_by_driver','cancelled_by_client') THEN 1 ELSE NULL END) OVER(PARTITION BY request_at) TotalCancelRequest -- count total cancel request by each day 
FROM
	Trips T
WHERE
	(T.request_at > '2013-09-29' AND T.request_at < '2013-10-04')
    -- filter request_at from '2013-10-01' to '2013-10-03'
AND
	NOT EXISTS(
		SELECT
			1
		FROM
			Users U
		WHERE
			(T.client_id = U.users_id AND U.banned = 'YES')
		OR
			(T.driver_id = U.users_id AND U.banned = 'YES')
        
    )
)
SELECT 
	Day,
	ROUND(TotalCancelRequest / TotalRequest,2) AS 'Cancellation Rate'
    -- cal cancel rate
FROM
	CTE