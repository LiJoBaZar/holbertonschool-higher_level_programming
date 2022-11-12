-- print with AS function
-- This sql at number by score with AS attribute
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score DESC;
