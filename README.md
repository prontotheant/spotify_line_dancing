# network-spotify-api-project

Alex Patterson and Jamie Parra  


Project Idea:  

 - For line dancing instructors or practicing dancers to create playlists around they need to teach or the dances they know 
  
 

 - Create a database for line dances and the songs that the dances can be done to  

 - Create a wesbite to be able to access/search database  

 - Wesbite should host a temporary small playlist user can add songs to from the seach  

 - Should be able to create a playlist in spotify, export temporary playlist to that playlist  



Using: Spotify API, sqlite3, HTML/CSS, Flask

## Next Steps ##
design better database

populate database with test data

implement temporary playlist with flask's session library

get temp playlist to export to spotify
   - log in to spotify
   - data from session variable to database to grab song ids
   - html form to grab playlist name and description
   - format song ids and other information and make/populate playlist
   
get add songs page to be able to search for specific songs from API 
   -  confirm correct song from 5 results or search again
   -  html form to grab dance info once confirmed
   -  put data into database
   -  may use session library for this as well
