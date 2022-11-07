DROP TABLE IF EXISTS songs;

CREATE TABLE songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    added TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    artist TEXT NOT NULL
);