import win32api
import sqlite3
import os
import json
from ScrappingAPI import WebScrapper
import time


cwd = os.getcwd()
data = {}

with open(os.path.join(cwd,'temp_data.json'),'r+') as fp:
    try:
        data = json.load(fp)
    except:
        data = {'names':[]}

print(data)

# c.execute("""CREATE TABLE local_movies(
#         serial integer,
#         file_name text,
#         name text,
#         rating real,
#         release_date text,
#         director text,
#         language text,
#         synopsis text,
#         poster text
#         )""")

drives = []
for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
    drives.append(drive)
systemdrive = os.environ['SYSTEMDRIVE']
filenames = []

for drive in drives:
    if(systemdrive not in drive):
        top = drive
        for dirName, subdirList, fileList in os.walk(drive):
            try:
                for filename in fileList:
                    os.chdir(dirName)
                    if ((filename.endswith(".mp4") or filename.endswith(".mkv") or filename.endswith(".avi") or filename.endswith(".m4v") or filename.endswith(".flv")) and os.stat(os.path.join(os.getcwd(),filename)).st_size > 500000000):
                        if(filename not in filenames):
                            filenames.append(filename)
                            print(filename)
                            os.chdir(top)
            except(FileNotFoundError):
                continue

films_in_db = {}
films_in_db["names"] = filenames

films_not_in_database = []

for movies in films_in_db['names']:
    if movies not in data['names']:
        films_not_in_database.append(movies)

conn = sqlite3.connect('movies.db')

c = conn.cursor()


'''extraction of details needs to be done here'''
count = 0
for films in films_not_in_database:
    WebScrapper_instance = WebScrapper(films)
    print(WebScrapper_instance.information)
    if(len(WebScrapper_instance.information) == 1):
        count+=1
    time.sleep(2)
    del WebScrapper_instance

print("Number of errors:",count)

with open(os.path.join(cwd,'temp_data.json'),'r+') as json_file:
    for films in films_not_in_database:
        data['names'].append(films)
    json.dump(data,json_file)

conn.commit()
conn.close()