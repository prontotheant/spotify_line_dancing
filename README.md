# Line Dancing with Spotify #
Website that allows users to search line dances by name, to find songs they can do the dances to. They can add songs they want to a temporary playlist and then export that temporary playlist to spotify with a dev auth token and username.

## Built with Flask ##
To run, in terminal:

pip install flask

flask --app app --debug run

## What's Complete ##

Connects to spotify
- have to use dev token
- successfully creates playlist with title grabbed from input and hardcoded built with dancing with spotify description

Database
- displays content from database and search by drop down method is successful

Cookies
- the flask session dynamically accepts content from page input and is able to store content while switching from page to page

Temporary Playlist
- able to add to playlist up to imposed song limit, allows multiple selections of the same song

## What Needs Work ##

Connects to spotify
- should absolutely use spotify log in pop up

Database
- should be able to easily add songs, instead of hardcoding information in database creation

Search
- would be a cool addition to embed video demonstration for each dance that could be played on page during search

Temporary Playlist
- should be able to remove songs from temporary playlist while still searching
