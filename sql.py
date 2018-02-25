import sqlite3

conn = sqlite3.connect('mydatabase.db')

cursor = conn.cursor()

#create a table

#cursor.execute('''CREATE TABLE albums
                #(title text, artist text, release_date text,
                #publisher text, media_type text)
                #''')

#add data to the database
cursor.execute('''INSERT INTO albums
                VALUES ('The Suburbs', 'Arcade Fire', '2013',
                'Independent', 'MP3')
                ''')

#save data to db
conn.commit()

#Insert multiple records using secure method
albums = [('Rock Spectacle', 'Barenaked Ladies','1995','Sony','MP3'),
          ('You Forget It In People', 'Broken Social Scene','2001','Independent','Record'),
          ('We Were Dead Before The Ship Even Sank', 'Modest Mouse','2007','Glacial Pace','MP3')]
cursor.executemany('INSERT INTO albums VALUES(?,?,?,?,?)', albums)
conn.commit()






