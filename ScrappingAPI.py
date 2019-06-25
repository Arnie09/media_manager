from bs4 import BeautifulSoup
import urllib.request
import re

class WebScrapper:

    def __init__(self,movie_name):
        self.movie = movie_name
        self.information = {}
        self.scrapper()

    def scrapper(self):
        
        string = self.movie
        url = 'https://www.google.com/search?q='
        url2 = '+imdb&ie=UTF-8&oe=UTF-8'

        class AppURLopener(urllib.request.FancyURLopener):
            version = "Mozilla/5.0"

        opener = AppURLopener()
        req = opener.open(url+string+url2)
        soup = BeautifulSoup(req)

        soup.prettify()

        links_for_movie = []
        for link in soup.findAll('a'):
            links = link.get('href')
            if("imdb.com" in links):
                links_for_movie.append(links)

        String = re.findall('https://www.imdb.com/title/[a-zA-Z0-9]+/',links_for_movie[0])

        req = opener.open(String[0])
        soup = BeautifulSoup(req)

        self.information["Name"] = soup.find('h1').text.strip()

        self.information["Year"] = re.findall('(\d\d\d\d)',soup.find('h1').text.strip())[0]

        self.information["Rating"] = soup.findAll('span',{'itemprop':'ratingValue'})[0].text.strip()

        buffer_list_to_store_genres = []
        for stuff in soup.findAll('div',{'class':'subtext'})[0].findAll('a'):
            strings = stuff.text.strip()
            buffer_list_to_store_genres.append(strings)

        self.information["Genre"] = [buffer_list_to_store_genres[i] for i in range(0,len(buffer_list_to_store_genres)-1)]
        
        buffer_list_of_directors = []
        for stuff in soup.findAll('div',{'class':'credit_summary_item'})[0].findAll('a'):
            buffer_list_of_directors.append(stuff.text.strip())

        self.information["Directors"] = buffer_list_of_directors

        self.information["Summary"] = soup.findAll('div',{'class':'summary_text'})[0].text.strip()

        self.information["Poster"] = soup.findAll('div',{'class':'poster'})[0].findAll('img')[0].get('src')

        req.close()

obj = WebScrapper("21.Jump.Street.2012.720p.BluRay.x264.YIFY")
print(obj.information)
