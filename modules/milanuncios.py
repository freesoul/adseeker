
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from urllib.parse import urlencode

from time import sleep

import re




DEBUG = True
LOAD_DATA = False
SAVE_DATA = False
MAX_RESULT_POR_PAGINA = 25
SLEEP = 1



class Milanuncios:

    results = []

    def __init__(self):
        self.driver = webdriver.Firefox()
        return



    def __del__(self):
        self.driver.close()



    def __get_results(self,
              zona,
              desde,
              hasta,
              query,
              filtros,
              max_pag
              ):

        self.results = []

        if LOAD_DATA:
            with open('debug_milanuncios.txt', 'r') as f:
                html = f.read()
                self.results = self.__parse_results(html, filtros)
        else:

            url_query = 'https://www.milanuncios.com/anuncios-en-{0}/{1}.htm'.format(zona,'-'.join(query.split(' ')))

            for pagina in range(1,max_pag+1):

                print("Pagina {0}".format(pagina))

                data = {
                    'desde' :   desde,
                    'hasta' :   hasta,
                    'cerca' :   's',
                    'demanda'   :   'n',
                    'vendedor'  :   'part',
                    'pagina'    :   pagina
                }

                data = urlencode(data)

                self.driver.get(url_query + '?' + data)
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.contenidoPie")))
                html = self.driver.page_source

                results, num_total_ads = self.__parse_results(html, filtros)
                self.results.extend(results)

                if SAVE_DATA or num_total_ads < MAX_RESULT_POR_PAGINA: # No more pages or save just 1 if debugging
                    print('Finished')
                    break

                print("-"*80)

                sleep(SLEEP)

        return self.results



    def __parse_results(self, html, filtros):
        soup = BeautifulSoup(html, 'html.parser')

        #container = soup.find("div", {"id":"cuerpo"})
        container = soup.select_one('div#cuerpo')

        items = container.select("div.aditem")
        items = [item for item in items if not 'DESTACADO' in item.get_text()]

        items = [{
            'name'      :   item.select_one('a.aditem-detail-title').get_text(),
            'link'      :   'https://www.milanuncios.com'+item.select_one('a.aditem-detail-title')['href'],
            'time'      :   self.__time_to_min(item.select_one('div.aditem-header').select_one('div.x6.display-desktop').get_text()),
            'id'        :   item.select_one('div.aditem-header').select_one('div.x5').get_text().replace('\n','').replace(' ',''),
            'precio'    :   int(item.select_one('div.aditem-price').get_text()[:-1]),
            'coin'      :   item.select_one('div.aditem-price').get_text()[-1:],
            'abstract'  :   item.select_one('div.tx').get_text()
        } for item in items]

        if DEBUG: print('Detected {0} ads'.format(len(items)))

        items_with_phone = []
        for item in items:

            filtro_ok = False
            for filtro in filtros:

                sin_ok = True
                for sin in filtro['sin']:
                    if re.search(sin, item['abstract'], flags=re.IGNORECASE):
                        sin_ok = False
                        if DEBUG: print('Skipping item (\'{0}\' found)'.format(sin))
                        break

                con_ok = False
                for con_list in filtro['con']:
                    con_list_ok = True
                    for con in con_list:
                        if not re.search(con, item['abstract'], flags=re.IGNORECASE):
                            con_list_ok = False
                            break
                    if con_list_ok:
                        if DEBUG: print('Item OK, list:', con_list)
                        con_ok = True
                        break

                if sin_ok and con_ok:
                    filtro_ok = True
                    break

            if filtro_ok:
                contact_info = self.__get_phone(item['id'])
                if contact_info and len(contact_info['telefonos']) > 0:
                    item_with_phone = item
                    item_with_phone.update(contact_info)
                    items_with_phone.append(item_with_phone)
                    if DEBUG:
                        print(item_with_phone)

        if DEBUG: print('Found {0} interesting ads'.format(len(items_with_phone)))
        return items_with_phone, len(items)

    def __time_to_min(self, time_string):
        time_data = time_string.split()

        if time_data[1]=='min':
            time_multiplier = 1
        elif time_data[1]=='horas':
            time_multiplier = 60
        elif 'día' in time_data[1]:
            time_multiplier = 60*24
        else:
            return None # años?

        return int(time_data[0])  * time_multiplier


    def __get_phone(self, _id):
        try:
            url_query='https://www.milanuncios.com/datos-contacto/?usePhoneProxy=0&id={0}'.format(_id[1:])

            self.driver.get(url_query)
            wait = WebDriverWait(self.driver, 15)
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.telefonos")))
            html_contactos = self.driver.page_source

            soup = BeautifulSoup(html_contactos, 'html.parser')

            return {
                'nombre'    : soup.select_one('div.texto').findChildren()[0].get_text(),
                'telefonos' : [tlf.get_text() for tlf in soup.select('div.telefonos')]
            }
        except:
            return {}



    def query(self,
              zona,
              desde,
              hasta,
              query,
              filtros,
              max_pag=3
              ):

        args = locals()
        del args['self']
        self.__get_results(**args)
