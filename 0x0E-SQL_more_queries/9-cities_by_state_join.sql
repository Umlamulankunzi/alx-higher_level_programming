-- Lists all cities in the database hbtn_0d_usa.
-- Records are sorted by cities.id in ASC order
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;