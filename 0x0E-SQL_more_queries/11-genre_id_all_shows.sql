-- Lists all shows contained in the database hbtn_0d_tvshows.
-- Display NULL for shows without genres.
-- Results ordered by tv_shows.title and tv_show_genres.genre_id in ASC order
SELECT show.title, genre.genre_id
FROM tv_shows AS show
LEFT JOIN tv_show_genres AS genre
ON show.id = genre.show_id
ORDER BY show.title, genre.genre_id;
