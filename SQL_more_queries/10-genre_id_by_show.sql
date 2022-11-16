-- Genre ID by Show
-- This SQL list all with at least one genere linked
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows JOIN tv_show_genres
WHERE tv_show_genres.show_id = tv_shows.id 
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
