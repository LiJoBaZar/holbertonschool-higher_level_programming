-- Id can´t be NULL
-- This SQL create a table with defaull value ID
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1, 
	name VARCHAR(256)
	);
