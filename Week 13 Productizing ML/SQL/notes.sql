CREATE TABLE author (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(128) NOT NULL
);

CREATE TABLE note (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content VARCHAR(256) NOT NULL,
    timestamp DEFAULT CURRENT_TIMESTAMP,
    author_id INTEGER NOT NULL,
    FOREIGN KEY (author_id) REFERENCES author(id)
);

CREATE TABLE authors_notes (
    note_id INTEGER NOT NULL,
    author_id INTEGER NOT NULL,
    FOREIGN KEY (note_id) REFERENCES note(id),
    FOREIGN KEY (author_id) REFERENCES author(id)
);

/* Insert authors to the author table. */
INSERT INTO author (name) VALUES ("Ainz Ooal Gown");
INSERT INTO author (name) VALUES ("Mare Bello Fiore");
INSERT INTO author (name) VALUES ("Aura Bella Fiora");
INSERT INTO author (name) VALUES ("Demiurge");
INSERT INTO author (name) VALUES ("Pandora's Actor");

/* Insert notes to the note table. */
INSERT INTO note (content, author_id) VALUES ("Umu.", 1);
INSERT INTO note (content, author_id) VALUES ("I, I would rather not have to meet intruders...they, they're scary...", 2);
INSERT INTO note (content, author_id) VALUES ("...I'm only 76, and I've got lots more time to grow, unlike an undead with no future like you.", 3);
INSERT INTO note (content, author_id) VALUES ("Perfume is essential for ladies? Isn't it just for stinky people?", 3);
INSERT INTO note (content, author_id) VALUES ("This is still too irrational, naive; a purely emotional judgment.", 4);
INSERT INTO note (content, author_id) VALUES ("Reading the movements of a slightly-above-average intellect that imagines himself a genius is easier than trying to predict the actions of a complete moron.", 4);
INSERT INTO note (content, author_id) VALUES ("Indeed! I burst with energy every day!", 5);

/* Select all notes by an author's name. */
SELECT * FROM note 
WHERE author_id = (SELECT id FROM author
                   WHERE name = "Demiurge");

/* Select author for a particular note by note ID. */
SELECT * FROM author
WHERE id = (SELECT author_id FROM note
            WHERE id = 3);

/* Select the names of all the authors along with the number of notes they each have. */
SELECT name, Count(note_id)
FROM authors_notes
INNER JOIN author on authors_notes.author_id = author.id
group by author_id;

/* Delete authors from the author table. */
DELETE FROM author
WHERE name = ("Ainz Ooal Gown"); 