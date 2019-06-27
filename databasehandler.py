import win32api
import sqlite3
import os
import json
from ScrappingAPI import WebScrapper
import time
import threading

cwd = os.getcwd()
data = {}

conn = sqlite3.connect(os.path.join(cwd,'movies_.db'))

c = conn.cursor()

'''The main function of temp_data is to serve as a temporary storage to keep track of the files that are in the database'''
with open(os.path.join(cwd,'temp_data.json'),'r+') as fp:
    try:
        data = json.load(fp)
    except:
        data = {'names':[]}
        sql = """CREATE TABLE local_movies(
        file_name text,
        name text,
        rating text,
        release_date text,
        director text,
        genre text,
        synopsis text,
        poster text,
        information text
        )"""
        c.execute(sql)

        conn.commit()
        


print(data)

drives = []
for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
    drives.append(drive)
systemdrive = os.environ['SYSTEMDRIVE']
filenames = []
paths = {}

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
                            paths[filename] = os.path.join(dirName,filename)
                            print(filename)
                            os.chdir(top)
            except(FileNotFoundError):
                continue

films_in_db = {}
films_in_db["names"] = filenames

with open(os.path.join(cwd,'path.json'),'r+') as pathfile:
    json.dump(paths,pathfile)

films_not_in_database = []

for movies in films_in_db['names']:
    if movies not in data['names']:
        films_not_in_database.append(movies)

c.execute("SELECT * FROM local_movies WHERE information = 'INCOMPLETE' AND name = 'Null'")
for result in c.fetchall():
    films_not_in_database.append(result[0])


conn.close()


def function_that_scraps():

    '''extraction of details needs to be done here'''
    count = 0
    for films in films_not_in_database:
        WebScrapper_instance = WebScrapper(films)
        # print(WebScrapper_instance.information)
        STATUS = "COMPLETE"
        if("Null" in list(WebScrapper_instance.information.values())):
            STATUS = "INCOMPLETE"
        conn_ = sqlite3.connect(os.path.join(cwd,'movies_.db'))
        c_obj = conn_.cursor()
        c_obj.execute("INSERT OR REPLACE INTO local_movies (file_name,name,rating,release_date,director,genre,synopsis,poster,information) VALUES(?,?,?,?,?,?,?,?,?)",(films,str(WebScrapper_instance.information['Name']),str(WebScrapper_instance.information['Rating']),str(WebScrapper_instance.information['Year']),str(WebScrapper_instance.information['Directors']),str(WebScrapper_instance.information['Genre']),str(WebScrapper_instance.information['Summary']),str(WebScrapper_instance.information['Poster']),STATUS))
        data['names'].append(films)
        conn_.commit()
        if(len(WebScrapper_instance.information) == 1):
            count+=1
        time.sleep(15)
        del WebScrapper_instance

    print("Number of errors:",count)

    with open(os.path.join(cwd,'temp_data.json'),'r+') as json_file:            
        json.dump(data,json_file)

    
    '''tO DELETE THE DUPLICATE ENTRIES'''
    c_obj.execute("DELETE FROM local_movies WHERE name == 'Null'")

    conn_.commit()
    
    conn_.close()

download_thread = threading.Thread(target=function_that_scraps)
download_thread.start()