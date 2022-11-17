"""
file: app.py
author: A. Patterson
purpose: contain flask app functions
"""
# first had to install flask using:
# pip install flask
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, make_response, session

# flask object
app = Flask(__name__)

# may have to use for sessions or something
app.config['SECRET_KEY'] = 'peanutbutter'

# run in terminal with:
# flask --app app --debug run

# when run, website is found at:
# http://127.0.0.1:5000


def database_connection():
    """
    :return: connection to database (file?)
    """
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection


# below is a decorator, this one changes the return value into an http response
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def hello():
    """
    function changes content to display depending on request method and input from POST
    still need to add temporary playlist session situation and format displayed content in the html file
    :return: rendered page
    """
    if request.method == "POST":
        connection = database_connection()
        select = request.form.get('dances')
        sql_try = f'SELECT title, artist from songs JOIN dances on songs.song_id = dances.song_id and step_id = {select}'
        songs = connection.execute(sql_try).fetchall()
        steps = connection.execute('SELECT * from step_sheets').fetchall()
        connection.close()
        return render_template('index.html', songs=songs, steps=steps)
    else:
        connection = database_connection()
        home = 1
        sql_try = f'SELECT title, artist from songs JOIN dances on songs.song_id = dances.song_id and step_id = {home}'
        songs = connection.execute(sql_try).fetchall()
        steps = connection.execute('SELECT * from step_sheets').fetchall()
        connection.close()
        return render_template('index.html', songs=songs, steps=steps)


@app.route('/playlist')
def playlist():
    """
    need to add html form and functionality for playlist info, token, etc.
    need to connect to spotify here
    :return: rendered page
    """
    return render_template('playlist.html')


@app.route('/add_song/', methods=('GET', 'POST'))
def add_song():
    """
    currently grabs info and structured to enter data into old database
    need to add 2 more forms and update to enter information into new database appropriately
    would like to add search for a single song from spotify to this page may not have time
    :return: rendered page
    """
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



