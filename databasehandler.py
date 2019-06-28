import win32api
import sqlite3
import os
import sys
import json
from ScrappingAPI import WebScrapper
import time
import threading

class DatabaseHandler:

    def __init__(self,cwd_):
        self.current_instance_of_db = []
        self.data = {}
        self.currentStatus_db = []
        self.rejected = {}
        self.films_not_in_database = []
        self.cwd = cwd_
        self.no_more_items = False
        self.scan_progress = False
        self.scan_memory()

    def function_that_scraps(self):

        '''extraction of details needs to be done here'''

        if(len(self.films_not_in_database) == 0):
            self.no_more_items = True
            return

        count = 0
        conn_ = sqlite3.connect(os.path.join(sys.path[0],'movies_.db'))
        c_obj = conn_.cursor()

        file_valid = None

        with open(os.path.join(sys.path[0],'rejectedFiles.json'),'r+') as rejected:

            with open(os.path.join(sys.path[0],'temp_data.json'),'r+') as json_file: 

                '''loop through the movies for which we need info'''
                for films in self.films_not_in_database:

                    if(count >1):
                        break
                    
                    print("working with the file : ",films)
                    WebScrapper_instance = WebScrapper(films)
                    count+=1
                    STATUS = "COMPLETE"
                    if("Null" in list(WebScrapper_instance.information.values())):
                        STATUS = "INCOMPLETE"
                    
                    a = films
                    b = str(WebScrapper_instance.information['Name'])
                    c = str(WebScrapper_instance.information['Rating'])
                    d = str(WebScrapper_instance.information['Year'])
                    e = str(WebScrapper_instance.information['Directors'])
                    f = str(WebScrapper_instance.information['Genre'])
                    g = str(WebScrapper_instance.information['Summary'])
                    h = str(WebScrapper_instance.information['Poster'])
                    i = STATUS

                    if(b != "Null" and c != "Null" and d != "Null"):
                        c_obj.execute("INSERT OR REPLACE INTO local_movies (file_name,name,rating,release_date,director,genre,synopsis,poster,information) VALUES(?,?,?,?,?,?,?,?,?)",(a,b,c,d,e,f,g,h,i))
                        self.data['names'].append(films)
                        file_valid = True
                        conn_.commit()

                        if(len(self.currentStatus_db) == 0):
                            c_obj.execute("SELECT file_name FROM local_movies")
                            for results in c_obj.fetchall():
                                self.currentStatus_db.append(results)
                        else:
                            self.currentStatus_db.append((a,))

                        if(len(self.current_instance_of_db) == 0):
                            c_obj.execute("SELECT * FROM local_movies")
                            for results in c_obj.fetchall():
                                self.current_instance_of_db.append(results)
                        else:
                            self.current_instance_of_db.append((a,b,c,d,e,f,g,h,i))
                        
                    else:
                        file_valid = False
                        if(len(self.rejected) == 0):
                            self.rejected['names'] = films
                        else:
                            self.rejected['names'].append(films)
                    
                    if file_valid == True:

                        '''saving the movie recently added in the json file'''
                        json_file.seek(0)
                        json.dump(self.data,json_file)
                        json_file.truncate()

                    elif file_valid == False:
                        
                        '''saving the file name in the rejected list'''  
                        rejected.seek(0)
                        json.dump(self.rejected,rejected)
                        rejected.truncate()

                    time.sleep(8)
                    del WebScrapper_instance

                print("Files Entered!")

                   
            

        
            

        '''tO DELETE THE DUPLICATE ENTRIES'''
        c_obj.execute("DELETE FROM local_movies WHERE name == 'Null'")

        conn_.commit()
        
        conn_.close()

    def scan_memory(self):

        a = self.cwd
        '''connecting to database and creating object'''
        conn = sqlite3.connect(os.path.join(sys.path[0],'movies_.db'))
        c = conn.cursor()

        '''The main function of temp_data is to serve as a temporary storage to keep track of the files that are in the database'''
        with open(os.path.join(sys.path[0],'temp_data.json'),'r+') as fp:
            try:
                self.data = json.load(fp)
            except:
                self.data = {'names':[]}
                try:
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
                except:
                    print()

        with open(os.path.join(sys.path[0],'rejectedFiles.json'),'r+') as rejected:
            try:
                self.rejected = json.load(rejected)
            except:
                self.rejected = {'names':[]}

        '''to get a list of scannable drives except the system drive'''
        drives = []
        for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
            drives.append(drive)
        systemdrive = os.environ['SYSTEMDRIVE']
        filenames = []
        paths = {}

        '''scanning all media files in the system and storing their names and paths'''
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
                                    #print(filename)
                                    os.chdir(top)
                    except(FileNotFoundError):
                        continue

        '''creating the json to store paths'''
        with open(os.path.join(sys.path[0],'path.json'),'r+') as pathfile:
            json.dump(paths,pathfile)

        '''TO FIND OUT WHICH MOVIES HAVE A RECORD IN DATABASE ANND WHICH MOVIES ARE STILL NOT THERE IN DATABASE'''
        for movies in filenames:
            if movies not in self.data['names'] and movies not in self.rejected['names']:
                self.films_not_in_database.append(movies)

        # c.execute("SELECT * FROM local_movies WHERE information = 'INCOMPLETE' AND name = 'Null'")
        # for result in c.fetchall():
        #     films_not_in_database.append(result[0])

        conn.close()

        self.scan_progress = True

        '''Calling the threaded function'''
        download_thread = threading.Thread(target=self.function_that_scraps)
        download_thread.start()   