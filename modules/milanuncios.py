
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options

from urllib.parse import urlencode

from time import sleep

import re


USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
DEBUG = True
LOAD_DATA = False
SAVE_DATA = False
SLEEP = 3



class Milanuncios:



    #########################################################
    #
    #   Open webdriver
    #
    #########################################################

    def __init__(self):
        opts = Options()
        opts.add_argument("--user-agent="+USER_AGENT)
        #opts.add_argument("user-data-dir=/home/bytes/.config/google-chrome/Default")
        opts.add_argument('--disable-extensions')
        opts.add_argument('--profile-directory=Default')
        opts.add_argument("--incognito")
        opts.add_argument("--disable-plugins-discovery");
        opts.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=opts)
        #sleep(29493)
        return



    #########################################################
    #
    #   Close webdriver
    #
    #########################################################
    def __del__(self):
        if DEBUG: sleep(10*60)
        self.driver.close()



    #########################################################
    #
    #   Helpers
    #
    #########################################################


    # Funcińo para obtener el tiempo del anuncio en minutos
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



    #########################################################
    #
    #   Go through webpages
    #
    #########################################################

    def __get_results(
            self,
            zona,
            desde,
            hasta,
            query,
            filtros,
            max_pag,
            max_minutes,
            max_ads=99999,
            pag=1,
            num_ads=0
        ):

        # debug case
        if LOAD_DATA:
            with open('debug_milanuncios.txt', 'r') as f:
                html = f.read()
                results = self.__parse_results(html, filtros, max_minutes)
        else:

            # Real case

            url_query = 'https://www.milanuncios.com/anuncios-en-{0}/{1}.htm'.format(
                zona,
                '-'.join(query.lower().split(' '))
            )

            print("Pagina {0}".format(pag))

            data = {
                'desde' :   desde,
                'hasta' :   hasta,
                'cerca' :   's',
                'demanda'   :   'n',
                'vendedor'  :   'part',
                'pagina'    :   pag
            }

            data = urlencode(data)

            self.driver.get(url_query + '?' + data)
            self.espera_pagina_cargada()

            sleep(SLEEP) # Minimum delay between requests

            html = self.driver.page_source

            results, b_minutes_reached, bNextPage = self.__parse_results(html, filtros, max_minutes)

            num_ads_new = num_ads + len(results)

            if (
                b_minutes_reached or
                num_ads_new >= max_ads or
                SAVE_DATA   # No more pages or save just 1 if debugging
            ):
                print('Finished (max minutes or ads)')

            else:

                if bNextPage and pag < max_pag:
                    
                    #print("Going to page {0}".format(pag+1))
                    next_page_results = self.__get_results(
                        zona,
                        desde,
                        hasta,
                        query,
                        filtros,
                        max_pag,
                        max_minutes,
                        max_ads,
                        pag + 1,
                        num_ads_new
                    )
                    results.extend(next_page_results)

                else:
                    print("Finished (max pag reached)")

        return results



    #########################################################
    #
    #   Espera que se haya cargado la página
    #
    #########################################################

    def espera_pagina_cargada(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.contenidoPie")))



    #########################################################
    #
    #   Open webdriver
    #
    #########################################################

    def __parse_results(self, html, filtros, max_minutes):

        soup = BeautifulSoup(html, 'html.parser')


        #########################################################
        #
        #   Test whether there is a next page or not
        #
        #########################################################

        container_paginator = soup.select_one('div.adlist-paginator-pages')
        b_next_page = container_paginator!=None and 'siguiente' in container_paginator.get_text().lower()



        #########################################################
        #
        #   Get ads
        #
        #########################################################

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

        if DEBUG: print('Detected {0} ads (in total at current page)'.format(len(items)))



        #########################################################
        #
        #   Filter interesting ads
        #
        #########################################################

        items_with_phone = []
        for item in items:

            # Max time reached?
            if not item['time'] is None and item['time'] > max_minutes:
                return items_with_phone, True, b_next_page # that true is b_minutes_reached

            # Test ad filters
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

            # Ad filters ok?
            if filtro_ok:

                # If so, look for phone info
                item_with_phone = item
                contact_info = self.__get_phone(item['id'])
                if contact_info and len(contact_info['telefonos']) > 0:
                    item_with_phone.update(contact_info)
                items_with_phone.append(item_with_phone)
                if DEBUG:
                    print(item_with_phone)
            
            last_time = item['time']

        if DEBUG: print('Found {0} interesting ads on current page'.format(len(items_with_phone)))
        return items_with_phone, False, b_next_page  # that true is b_minutes_reached



    #########################################################
    #
    #   Open webdriver
    #
    #########################################################

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



    #########################################################
    #
    #   The function to call!!!
    #
    #########################################################

    def query(self,
              zona,
              desde,
              hasta,
              query,
              filtros,
              max_pag=3,
              max_minutes=60*24,
              max_ads=99999
              ):

        args = locals()
        del args['self']
        return self.__get_results(**args)
