import sqlite3
import os

cwd = os.getcwd()
con = sqlite3.connect(os.path.join(cwd,'movies_.db'))

c = con.cursor()

c.execute("SELECT DISTINCT file_name,name,rating,release_date,director,genre,synopsis,poster,information FROM local_movies WHERE name <> 'Null'")

count = 0
for result in c.fetchall():
    print(result)
    count+=1

c.execute("SELECT * from local_movies")

count1 = 0
for result in c.fetchall():
    print(result)
    count1+=1

print(count1)
con.close()
