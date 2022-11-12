-- print with AS function
-- This sql at number by score with AS attribute
	SELECT score, COUNT(*) AS number
	FROM second_table
	GROUP BY score
	ORDER BY score DESC;
