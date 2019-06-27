from bs4 import BeautifulSoup
import urllib.request
import re

class WebScrapper:

    def __init__(self,movie_name):
        self.movie = movie_name
        self.information = {}
        self.scrapper()

    def scrapper(self):
        
        string = self.movie.replace(" ","+")
        
        try:
            url = 'https://www.google.com/search?q='
            url2 = '+imdb&ie=UTF-8&oe=UTF-8'

            # class AppURLopener(urllib.request.FancyURLopener):
            #     version = "Mozilla/5.0"


            # opener = AppURLopener()
            # req = opener.open(url+string+url2)
            headers = { 'User-agent' : 'Mozilla/5.0' }
            mid = urllib.request.Request((url+string+url2),None,headers)
            req = urllib.request.urlopen(mid).read()

            soup = BeautifulSoup(req)
            print("Hi")

            soup.prettify()

            links_for_movie = []
            for link in soup.findAll('a'):
                links = link.get('href')
                if("imdb.com" in links):
                    links_for_movie.append(links)

            String = re.findall('https://www.imdb.com/title/[a-zA-Z0-9]+/',links_for_movie[0])

            # req = opener.open(String[0])
            mid = urllib.request.Request((String[0]),None,headers)
            req = urllib.request.urlopen(mid).read()

            soup = BeautifulSoup(req)

        except Exception as e:
            self.information["Name"] = "Null"
            self.information["Year"] = "Null"
            self.information["Rating"] = "Null"
            self.information["Genre"] = "Null"
            self.information["Directors"] = "Null"
            self.information["Summary"] = "Null"
            self.information["Poster"] = "Null"

            print(e)
            return

        try:
            self.information["Name"] = soup.find('h1').text.strip()
        except:
            self.information["Name"] = "Null"

        try:
            self.information["Year"] = re.findall('(\d\d\d\d)',soup.find('h1').text.strip())[0]
        except:
            self.information["Year"] = "Null"

        try:
            self.information["Rating"] = soup.findAll('span',{'itemprop':'ratingValue'})[0].text.strip()
        except:
            self.information["Rating"] = "Null"

        try:
            buffer_list_to_store_genres = []
            for stuff in soup.findAll('div',{'class':'subtext'})[0].findAll('a'):
                strings = stuff.text.strip()
                buffer_list_to_store_genres.append(strings)
            self.information["Genre"] = [buffer_list_to_store_genres[i] for i in range(0,len(buffer_list_to_store_genres)-1)]
        except:
            self.information["Genre"] = "Null"

        try: 
            buffer_list_of_directors = []
            for stuff in soup.findAll('div',{'class':'credit_summary_item'})[0].findAll('a'):
                buffer_list_of_directors.append(stuff.text.strip())
            self.information["Directors"] = buffer_list_of_directors
        except:
            self.information["Directors"] = "Null"

        try: 
            self.information["Summary"] = soup.findAll('div',{'class':'summary_text'})[0].text.strip()
        except:
            self.information["Summary"] = "Null"

        try:
            self.information["Poster"] = soup.findAll('div',{'class':'poster'})[0].findAll('img')[0].get('src')
        except:
            self.information["Poster"] = "Null"

    


obj = WebScrapper("Jackie Brown - Tarantino 1997 - x264 - AC3 Ita - AAC Eng - Subs - Dvdrip RODJA.mkv")
print(obj.information)

'''Name,Year,Rating,Genre,Directors,Summary,Poster'''
