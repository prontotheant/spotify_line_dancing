# Project Breakdown #
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
Basic text, rudimentary css
Contains flask subservice jinja specific formatting that only looks good when run from terminal with flask

#### playlist.html ####
Basic text, uses form
Contains flask subservice jinja specific formatting that only looks good when run from terminal with flask

would like to:
 -  add some sort of log in or security feature to reach this page
 -  connect this page with spotify to grab song id for entering songs into the database
 -  add that functionality along with fields specific to the dance information
      - possible connect to copperknob.co.uk may require webscraping if so

#### add_song.html ####



