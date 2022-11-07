"""
file: app.py
author: A. Patterson
purpose: contain flask app functions
"""
# first had to install flask using:
# pip install flask

# second had to
# import Flask object
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect

# third had to
# create a flask object in the project
app = Flask(__name__)
app.config['SECRET_KEY'] = 'peanutbutter'


def database_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection


# fourth add decorator
# a decorator is:
@app.route('/')  # this one in particular changes the return value into an http response
@app.route('/index')
def hello():
    connection = database_connection()
    songs = connection.execute('SELECT * from songs').fetchall()
    connection.close()
    return render_template('index.html', songs=songs)
# fifth write function with decorator

# sixth run flask in debug mode using
# flask --app app --debug run


# seventh add another page
@app.route('/playlist')
def playlist():
    return render_template('playlist.html')
# now when using local url/port whatever can add /about to end and be at new page
# http://127.0.0.1:5000


@app.route('/add_song/', methods=('GET', 'POST'))
def add_song():
    if request.method == 'POST':
        artist = request.form['artist']
        title = request.form['title']
        if not artist:
            flash('Artist is required')
        elif not title:
            flash('Title is required')
        else:
            connection = database_connection()
            connection.execute('INSERT INTO songs (artist, title) VALUES (?, ?)', (artist, title))
            connection.commit()
            connection.close()
            return redirect(url_for('hello'))
    return render_template('add_song.html')
