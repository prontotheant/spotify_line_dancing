# Project Breakdown #
Code was written separately by Jamie and Alex at the same time, next phase would be synthesizing the best parts of each individual effort into one and expanding functionality and connectivity
## As of 11/7/2022 ##
### app.py ###
Can run project in pycharm terminal targeting app.py with: flask --app app --debug run

Currently has navigation support for index, playlist, and add_song

Currently connects to database.db

This file also hosts the functionality for
-  grabbing content from database and displaying that content on index
-  getting content from the add_song page, connecting to the database, and entering the content into it

Started to look into cookie functionality and secret keys and what not, for the information storage of the temporary playlist


### database.db ###
Currently contains test content in a single table, with columns: id, time added, title, artist

Need to make a more robust database design, which is in basic stage, need to consider content emailed by professor Greenwell

### initialize_database.py ###
Currently grabs sql from songs_and_dances.sql and overwrites the database content and structure when run

### songs_and_dances.sql ###
Contains sql to create a table with the columns: id, time added, title, artist

This is the file that would need to be edited once a database design has been finalized, followed by a run of the initialize_database.py to implement the changes

#### index.html ####
Contains flask subservice jinja specific formatting that only looks good when run from terminal with flask

Currently displays database

Hope to add search and temporary playlist to this page

#### playlist.html ####
Currently no content

Future for this page would be:
- add a form for playlist name, playlist description
- display temporary playlist content
- adding spotify log in or enter token
- information confirmation alert 
- then export to spotify functionality which will require another .py 

#### add_song.html ####
Contains flask subservice jinja specific formatting that only looks good when run from terminal with flask

Currently has post functionality that connects to database, has a form to gather content

would like to:
 -  add some sort of log in or security feature to reach this page
 -  connect this page with spotify to grab song id for entering songs into the database
 -  add that functionality along with fields specific to the dance information
      - possible connect to copperknob.co.uk may require webscraping if so

## learning_spotifyAPI ##
- confirmed how to grab songs with seed information
- confirmed how to make a playlist, with a specific name, added songs, etc.. tested with personal account

- confirmed what format of information must be sent to the API to populate with songs, 
     - meaning the information needed to be stored in the database was discovered
     - as well as the best way to modify the format of the raw information after extracting from database, before sending to spotify, in python

- need to figure out what the best way to log in/get token would be, code support for this functionality is not written in python so may need to be translated
- need to confirm how searching a specifc song would work


