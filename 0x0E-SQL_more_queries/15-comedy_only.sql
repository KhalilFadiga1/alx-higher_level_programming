-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
-- uses a databse to lists all rows in a table corresponding to all rows in another
SELECT title
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name= 'Comedy'
GROUP BY title
ORDER BY title ASC;
