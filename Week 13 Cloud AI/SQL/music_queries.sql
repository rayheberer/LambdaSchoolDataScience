/* Show all albums. */
SELECT * FROM album;

/* Show all albums made between 1975 and 1990. */
SELECT * FROM album
WHERE release_year >= 1975
AND release_year <= 1990;

/* Show all albums whose names start with Super D */
SELECT * FROM album
WHERE title LIKE "Super D%";

/* Show all albums that have no release year. */
SELECT * FROM album
WHERE release_year IS NULL;

/* Show all track titles from Super Funky Album. */
SELECT title FROM track 
WHERE album_id = (SELECT id FROM album
                  WHERE title="Super Funky Album");

/* Same query as above, but rename the column from title to Track_Title in the output. */
SELECT title AS Track_Title FROM track
WHERE album_id = (SELECT id FROM album
                  WHERE title="Super Funky Album");

/* Select all album titles by Han Solo. */
SELECT title FROM album
WHERE id = (SELECT album_id FROM artist_album
            WHERE artist_id = (SELECT id FROM artist
            	               WHERE name = "Han Solo"));

/* Select the average year all albums were released. */
SELECT AVG(release_year) FROM album;

/* Select the average year all albums by Leia and the Ewoks were released. */
SELECT AVG(release_year) FROM album
WHERE id = (SELECT album_id FROM artist_album
            WHERE artist_id = (SELECT id FROM artist
            	               WHERE name = "Leia and the Ewoks"));

/* Select the number of artists. */
SELECT DISTINCT COUNT(id) FROM artist;

/* Select the number of tracks on Super Dubstep Album. */
SELECT DISTINCT COUNT(id) FROM track
WHERE album_id = (SELECT id FROM album
                  WHERE title = "Super Dubstep Album")