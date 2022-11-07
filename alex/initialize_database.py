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

cursor.execute("INSERT INTO songs(artist, title) VALUES(?,?)", ('bro', 'neat banjo dude'))

connection.commit()
connection.close()