# Media Manager

Greetings everyone! Welcome to my sad life where I go on ranting about one more of a thing i made because
I wanted to. Behold Media Manager(Yeah name sucks)

Anyways as an avid movie watcher and broke students, I cant afford streaming services as of now and hence I have 
a huge collection of movies that are present in my hard drive. I intend to keep those files and very often I find myself  going 
back to watching old movies. However there's a problem with havig multiple movies. It becomes hard to track everything. Lots and lots of folders. 
Pretty sure even Monica Bing would find it hard to organise the movie files properly was she given a chance to do so. 

That is where our beloved Media Manager comes in. This PyQT desktop application is aimed to manage your movie files and 
keep information on them for offline use. Of course you've seen lots of projects which do this but let me tell you about a problem. 

Usually most softwares use omdb API that fetches you the information when you pass in the name of the movie - THE EXACT NAME OF THE MOVIE.
But the name of the movie is not present in the file name in proper form and thus it becomes a tedious task to manually get the information and create the
database. Here our Media Manager automatically scans your memory and reads the names of the movie files and extracts information on them without
your intervention! (Thanks to Google) However as spamming too many requests would temporarily ban the ip, hence our friend only fetches information of 50
movies in one go. Every time you hit that scan button, the application downloads information for 50 movies. Be sure not to spam that button too frequently!

The information loading procedure occurs as a multithreaded process in the background. The application also provides some basic features like file
searching based on movie attributes like name, rating, directors, year and so on. A play button has also been included that enables the direct 
playing of the selected movie file. 

### Dependancies :

* Vlc media player
* PyQT5 (pip install pyqt5)

### Lets see some screenshots?

Here is the main screen of the application. The left pane lists all the movies while the 
right pane lists information on the selected movie.

![general](https://github.com/Arnie09/media_manager/blob/master/screenshots/general.PNG "Homescreen")

Next up is the demonstration of the search functionality 

![searching](https://github.com/Arnie09/media_manager/blob/master/screenshots/search.PNG "Search")

Coming up is the delete feature 

![deleting](https://github.com/Arnie09/media_manager/blob/master/screenshots/delete.PNG "Delete")


### Queries:

In case of any query feel free to contact me on any of my social media or raise an issue in case of a bug. This project is still under development so its likely
to get better. 
