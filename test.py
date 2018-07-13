# -*- encoding: utf-8 -*-


from datetime import timedelta, datetime
from threading import Timer
from time import sleep

def hello_world():
    print("it works")
    #...


last_time = datetime.now()

while True:
	if (datetime.now() - last_time).total_seconds() >= 5:
		last_time = datetime.now()

		hello_world()








exit(0)




import smtplib

fromaddr = 'kener18@gmail.com'
toaddrs  = 'kener18@gmail.com'

username = 'kener18@gmail.com'
password = 'dpn6j12m16-e2'

msg = "\r\n".join([
  "From: {0}".format(fromaddr),
  "To: {0}".format(toaddrs),
  "Subject: Just a message",
  "",
  "Why, oh why"
  ])

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()







exit(0)

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