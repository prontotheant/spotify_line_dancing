"""
file: initialize_database.py
author: A. Patterson
purpose: create the database
"""
import sqlite3

connection = sqlite3.connect('database.db')

with open('songs_and_dances.sql') as sql:
    connection.executescript(sql.read())

cursor = connection.cursor()

cursor.execute("INSERT INTO songs(artist, title, spotify_id) VALUES(?,?,?)", ('Delbert McClinton', 'Mary Lou',
                                                                              '7dzOdXamLpHJlWJiI70gyA'))
cursor.execute("INSERT INTO songs(artist, title, spotify_id) VALUES(?,?,?)", ('Old Crow Medicine Show', 'Wagon Wheel',
                                                                              '2XgGdD5d2MW4RNx8KnIjVh'))
cursor.execute("INSERT INTO songs(artist, title, spotify_id) VALUES(?,?,?)", ('Darius Rucker', 'Wagon Wheel',
                                                                              '3xdjjKMcMOFgo1eQrfbogM'))
cursor.execute("INSERT INTO songs(artist, title, spotify_id) VALUES(?,?,?)", ('Scooter Lee',
                                                                              'Roll Back The Rug (and dance)',
                                                                               '2hHmGQgxwWrMhBt0WmKEcU'))
cursor.execute("INSERT INTO songs(artist, title, spotify_id) VALUES(?,?,?)", ('Ernest Tubb', 'Waltz Across Texas',
                                                                              '2sRQWq9NELigoO4xRB9s3r'))
cursor.execute("INSERT INTO songs(artist, title, spotify_id) VALUES(?,?,?)", ('Kay Starr', 'Rock and Roll Waltz',
                                                                              '7te9DUttzNePdSlkIgSTdz'))
cursor.execute("INSERT INTO step_sheets(step_name, walls) VALUES(?,?)", ('Cut a Rug', '2'))
cursor.execute("INSERT INTO step_sheets(step_name, walls) VALUES(?,?)", ('Waltz Across Texas', '4'))
cursor.execute("INSERT INTO step_sheets(step_name, walls) VALUES(?,?)", ('Rose Moon', '2'))
cursor.execute("INSERT INTO dances(step_id, song_id) VALUES(?,?)", (1, 1))
cursor.execute("INSERT INTO dances(step_id, song_id) VALUES(?,?)", (1, 2))
cursor.execute("INSERT INTO dances(step_id, song_id) VALUES(?,?)", (1, 3))
cursor.execute("INSERT INTO dances(step_id, song_id) VALUES(?,?)", (1, 4))
cursor.execute("INSERT INTO dances(step_id, song_id) VALUES(?,?)", (2, 5))
cursor.execute("INSERT INTO dances(step_id, song_id) VALUES(?,?)", (2, 6))
cursor.execute("INSERT INTO dances(step_id, song_id) VALUES(?,?)", (3, 6))


connection.commit()
connection.close()
