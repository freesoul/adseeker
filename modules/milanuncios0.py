
from bs4 import BeautifulSoup
#import requests
#from selenium import webdriver
from seleniumrequests import Firefox

class Milanuncios:

    results = []

    def __init__(self):
        # self.session = requests.Session()
        # self.session.headers.update({'User-Agent': ''})
        # #'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/61.0.3163.100 Chrome/61.0.3163.100 Safari/537.36'
        # self.session.verify = False
        self.driver = Firefox()#webdriver.Firefox()

    def __get_query_html(self,
              zona,
              desde,
              hasta,
              query,
              ):
        url_query = 'https://www.milanuncios.com/anuncios-en-{0}/{1}.htm'.format(zona,'-'.join(query.split(' ')))

        data = {
            'desde' :   desde,
            'hasta' :   hasta,
            'cerca' :   's',
            'demanda'   :   'n'
        }

        self.html = self.driver.request('GET', url_query, params=data)._content.decode('iso-8859-1')
        print(self.html)
        # print(self.html)
        # return
        # #self.driver.get("http://www.milanuncios.com")
        # #ret = self.session.get(url_query, params=data)
        # self.html = self.driver.page_source

    def __parse_results(self):
        soup = BeautifulSoup(self.html, 'html.parser')

        print(self.html)
        exit(0)

        container = soup.select("div#cuerpo")

        if not container:
            print("Error in container")
            return

        items = container.find_all("div", {"class":"aditem"})
        items = [item for item in items if not 'DESTACADO' in item.get_text()]

        for item in items:
            print(item.get_text())
            print("-"*80)

        self.results = []



    def query(self,
              zona,
              desde,
              hasta,
              query,
              ):

        args = locals()
        del args['self']
        self.html = self.__get_query_html(**args)
        return
        self.__parse_results()
        return "ok"
