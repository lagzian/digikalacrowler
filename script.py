import subprocess
import sys
import time

from selenium import webdriver 
from selenium.webdriver.firefox.options import Options

import os
import smtplib
from email.message import EmailMessage
import datetime
from bs4 import BeautifulSoup

options = Options()
options.add_argument('-headless')
browser = webdriver.Firefox(options=options)

url = 'https://www.digikala.com/incredible-offers/'
keywords = ['روغن', 'هدفون', 'ماوس']

browser.get(url)
time.sleep(5)
source = browser.page_source
soup = BeautifulSoup(source, 'html.parser')

keyword_found = False 
for kw in keywords:
  if kw in soup.text:
    keyword_found = True
    break
    
browser.close()

test_message = "این یک ایمیل آزمایشی است"  
sender = 'nimahdx2000@gmail.com'
recipient = 'tech@zistarvin.ir'
smtp_server = 'smtp.gmail.com'
smtp_port = 587
password = os.environ['EMAIL_PASS']

smtp = smtplib.SMTP(smtp_server, smtp_port)
smtp.connect() # Connect to SMTP server
smtp.ehlo()
smtp.starttls()
smtp.login(sender, password)
smtp.send_message(msg)
smtp.quit()

if keyword_found:

  # Send keyword email 
  smtp.connect()
  smtp.send_message(msg) 

print('Done')
