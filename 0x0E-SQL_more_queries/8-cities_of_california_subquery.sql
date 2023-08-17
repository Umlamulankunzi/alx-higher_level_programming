-- List all cities of CA in the DB hbtn_0d_usa.
-- Results ordered by cities.id in ASC order
SELECT 'id', 'name'
FROM 'cities'
WHERE 'state_id' = (
    SELECT 'id'
	FROM 'states'
	WHERE 'name' = "California"
)
ORDER BY 'id' ASC;
