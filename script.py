import subprocess
import sys

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'selenium'])

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os
import smtplib  
from email.message import EmailMessage
import datetime
from bs4 import BeautifulSoup

options = Options()
options.headless = True
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

msg = EmailMessage()
msg['From'] = sender
msg['To'] = recipient
msg['Subject'] = 'Test Email'
msg.set_content(test_message)

smtp = smtplib.SMTP(smtp_server,smtp_port) 
smtp.starttls()
smtp.login(sender, password)  
smtp.send_message(msg)
smtp.quit()

if keyword_found:
  
  msg = EmailMessage()
  msg['From'] = sender
  msg['To'] = recipient
  msg['Subject'] = 'Keyword Found'
  content = f'Keywords ({keywords}) found on {url}'
  msg.set_content(content)

  smtp.send_message(msg)

print('Done')
