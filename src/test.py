import sqlite3
import os
import sys

cwd = os.getcwd()
con = sqlite3.connect(os.path.join(cwd,'movies_.db'))

c = con.cursor()

# c.execute("SELECT DISTINCT file_name,name,rating,release_date,director,genre,synopsis,poster,information FROM local_movies WHERE name <> 'Null'")

# count = 0
# for result in c.fetchall():
#     print(result)
#     count+=1

# c.execute("SELECT name from local_movies")

# count1 = 0
# for result in c.fetchall():
#     print(result[0])
#     count1+=1
# print(sys.path[0])
# print(count1)
# con.close()
c.execute("CREATE TABLE local_movies")

con.commit()
con.close()