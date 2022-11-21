"""
file: app.py
author: A. Patterson
purpose: contain flask app functions
"""

# first had to install flask using:
# pip install flask
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, session
import random
import math
from spotify_playlist import spot_api_playlist

# flask object
app = Flask(__name__)

# may have to use for sessions or something
key = math.floor(random.random() * 23456)
app.config['SECRET_KEY'] = f'{key}'

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
    temp_count = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    if request.method == "POST":
        if 'dances' in request.form:
            session['dance_choice'] = request.form['dances']
        if 'huck' in request.form:
            gel = request.form['huck']
            for y in gel:
                session['temp_playlist'].append(int(y))
                # I spent at least 2 hours discovering that to more permanently affect the session['tem...]
                # you must be reassigning it, so append alone doesn't work
                rock = session['temp_playlist']
                if len(rock) < 11:
                    session['temp_playlist'] = rock
                # trying to implement an else here messes with the session[tem...] list and makes it add continuously
                # ignoring the conditional for whatever strange reasons

        sql_try = f"SELECT title, artist, songs.song_id from songs JOIN dances on songs.song_id = dances.song_id and " \
                  f"step_id = {session['dance_choice']}"
        connection = database_connection()
        songs = connection.execute(sql_try).fetchall()
        steps = connection.execute('SELECT * from step_sheets').fetchall()
        song_info = []
        for x in session['temp_playlist']:
            sql_temp = f"SELECT title, artist from songs where song_id={x}"
            song_info.append(connection.execute(sql_temp).fetchall())
        connection.close()
        return render_template('index.html', songs=songs, steps=steps, temp=temp_count, play=song_info)

    else:
        connection = database_connection()
        session['dance_choice'] = 1
        session['temp_playlist'] = []
        sql_try = f"SELECT title, artist, songs.song_id from songs JOIN dances on songs.song_id = dances.song_id and " \
                  f"step_id = {session['dance_choice']}"
        songs = connection.execute(sql_try).fetchall()
        steps = connection.execute('SELECT * from step_sheets').fetchall()
        song_info = []
        for x in session['temp_playlist']:
            sql_temp = f"SELECT title, artist from songs where song_id={x}"
            song_info.append(connection.execute(sql_temp).fetchall())
        connection.close()
        return render_template('index.html', songs=songs, steps=steps, temp=temp_count, play=song_info)


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


@app.route('/test', methods=('GET', 'POST'))
def test():
    rock = session['temp_playlist']
    connection = database_connection()
    spotify_ids = []
    for x in rock:
        sp_id = connection.execute(f"SELECT spotify_id from songs where song_id={x}").fetchall()
        spotify_ids.append(sp_id[0]['spotify_id'])


    cool = spot_api_playlist(
       "BQBcfjz6AAyvLi4cCCqUcdM-iMimz2YJuHhKq504TR6tIyWxTeyW-XLHSKSkv2KC84TtaAHaEN_PBH6wpiRHf_XFoonSDx3jPtp_2cE-d5nSNaOL1IzYQNQot7vzVhdOOlYejvvYECXqEpnqQUCg31rdcNVAReSH2UAcOv10_jrjzYuktATPmCihpbqtJP9KEv-P9HbUoZQ5q4Dz3Q",
       "prontotheant",
        spotify_ids,
        "test-bro3",
        "testing code for realsies"
    )
    return render_template('test.html', test=cool)

