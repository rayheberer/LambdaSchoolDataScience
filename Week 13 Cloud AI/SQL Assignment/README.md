# SQL

See [the Lambda page on Relational
Databases](https://github.com/LambdaSchool/Relational-Databases) for more
information. (Note that page is for PostgreSQL, but the SQL information is valid
here.)

## SQLite

SQLite is a popular, simple SQL database.

You can launch into a memory-only DB by running:

```
sqlite3
```

You can specify a persistent DB file with:

```
sqlite3 mydatabase.db
```

When you get to the prompt, you can type `.help` for commands.

Some helpful ones:

* `.mode column` turn on column output for `SELECT`.
* `.header on` turn on column headers for `SELECT`.
* `.read filename` execute the SQL in `filename`.
* `.open dbname` re-open a memory-only DB to a persistent file.
* `.quit` exit SQLite. (Note that if you're using a memory-only DB, all
  data is lost at this point.)

Another potentially useful third-party tool is [DB Browser for
SQLite](https://sqlitebrowser.org/), a GUI-based SQLite viewer and data
manipulator that can also run SQL queries.


## Create a Music Database

Make an albums table to hold album information:

```sql
CREATE TABLE album (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(128) NOT NULL,
    release_year INTEGER
);
```

Make an artists table to hold artist information:

```sql
CREATE TABLE artist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(128) NOT NULL
);
```


### Exercises

Before you begin, look at the queries in `setup.sql` to get a hint as to the
column names in the following tables. We'll use `setup.sql` later.

* Create a table called `track` that holds information about a music track. It should contain:
  * An autoincrementing `id`
  * A title (of type `VARCHAR`, probably)
  * A reference to an `id` in table `album` (the album the track is on). This
    should be a _foreign key_.

* Create a table called `artist_album` to connect artists to albums. (Note that
  an artist might have several albums and an album might be created by multiple
  artists.)
  * Use foreign keys for this, as well.
 
* Run the queries in the file `setup.sql`. This will populate the tables.
  * Fix any errors at this point by making sure your tables are correct.
  * `DROP TABLE` can be used to delete a table so you can recreate it with
    `CREATE TABLE`.

* Write SQL `SELECT` queries that:
  * Show all albums.
  * Show all albums made between 1975 and 1990.
  * Show all albums whose names start with `Super D`.
  * Show all albums that have no release year.

* Write SQL `SELECT` queries that:
  * Show all track titles from `Super Funky Album`.
  * Same query as above, but rename the column from `title` to `Track_Title` in
    the output.

  * Select all album titles by `Han Solo`.

  * Select the average year all albums were released.

  * Select the average year all albums by `Leia and the Ewoks` were released.

  * Select the number of artists.

  * Select the number of tracks on `Super Dubstep Album`.

## Create a database for taking notes.

* What are the columns that a note table needs?

* If you have a timestamp field, how do you auto-populate it with the date?

* A note should have a foreign key pointing to an author in an author table.

* What columns are needed for the author table?

### Exercises

Write queries that:

* Insert authors to the author table.

* Insert notes to the note table.

* Select all notes by an author's name.

* Select author for a particular note by note ID.

* Select the names of all the authors along with the number of notes they each have. (Hint: `GROUP BY`.)

* Delete authors from the author table.
  > Note that SQLite doesn't enforce foreign key constrains by default. You have
  > to enable them by running `PRAGMA foreign_keys = ON;` before your queries.
  
  * What happens when you try to delete an author with an existing note?
  * How can you prevent this?

Submit a file `notes.sql` with the queries that build (`CREATE TABLE`/`INSERT`)
and query the database as noted above.