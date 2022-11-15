DROP TABLE IF EXISTS songs;
DROP TABLE IF EXISTS step_sheets;
DROP TABLE IF EXISTS dances;
CREATE TABLE songs (
    song_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    artist TEXT NOT NULL,
    spotify_id TEXT NOT NULL
);
CREATE TABLE step_sheets (
    step_id INTEGER PRIMARY KEY AUTOINCREMENT,
    step_name TEXT NOT NULL,
    walls CHAR(1)
);
CREATE TABLE dances (
    dance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    song_id INTEGER,
    step_id INTEGER,
    FOREIGN KEY (song_id) REFERENCES songs(song_id)
    FOREIGN KEY (step_id) REFERENCES step_sheets(step_id)
);