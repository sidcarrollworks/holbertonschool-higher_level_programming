-- list genres and the number of shows linked to each
SELECT tv_genres.name as genre, COUNT(tv_shows.title) as number_shows
FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
GROUP BY tv_genres.name
ORDER BY number_shows desc;
