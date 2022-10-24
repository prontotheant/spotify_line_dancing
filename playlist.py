import sqlite3

songs = [
	"bye",
	"purple rain",
	"only for tomorrow"
]

songs = sorted(songs)

connection = sqlite3.connect("spotify_list.db")
cursor = connection.cursor()

cursor.execute("create table songs (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
for i in range(len(songs)):
	cursor.execute("insert into songs (name) values (?)",[songs[i]])
	print("added ", songs[i])

connection.commit()
connection.close()