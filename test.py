# -*- encoding: utf-8 -*-


from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from urllib.parse import urlencode
from time import sleep
import re



driver = webdriver.Chrome()

driver.get("http://www.milanuncios.es")


print(driver.page_source)