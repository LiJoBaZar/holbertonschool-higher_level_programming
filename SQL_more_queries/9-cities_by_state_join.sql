-- Cities by states
-- This SQL show all cities in a state
SELECT cities.id, cities.name, states.name FROM states JOIN cities WHERE cities.state_id = states.id 
ORDER BY cities.id ASC;
