from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os
import smtplib
from email.message import EmailMessage
import datetime

options = Options()
options.headless = True

browser = webdriver.Firefox(options=options)

url = 'https://www.digikala.com/incredible-offers/'
browser.get(url)

import time
time.sleep(5) 

source = browser.page_source

from bs4 import BeautifulSoup 
soup = BeautifulSoup(source, 'html.parser')

keywords = ['روغن', 'هدفون', 'ماوس']

test_message = "این یک ایمیل آزمایشی است"
sender = 'nimahdx2000@gmail.com'
recipient = 'tech@zistarvin.ir'
smtp_server = 'smtp.gmail.com'
smtp_port = 587

keyword_found = False
for kw in keywords:
  if kw in soup.text:
    keyword_found = True
    break
    
browser.close()

# Send test email
message = EmailMessage()
message['From'] = sender
message['To'] = recipient  
message['Subject'] = 'Test Email'

message.set_content(test_message)
password = os.environ['EMAIL_PASS']  

smtp = smtplib.SMTP(smtp_server, smtp_port)
smtp.ehlo()  
smtp.starttls()
smtp.login(sender, password)
smtp.send_message(message)
smtp.quit()

# Send keyword email
if keyword_found:

  message = EmailMessage()
  message['From'] = sender
  message['To'] = recipient
  message['Subject'] = 'Keyword Found on Website' 
  
  content = f'Keywords ({keywords}) found on {url} on {datetime.datetime.now()}'
  message.set_content(content)
  
  smtp = smtplib.SMTP(smtp_server, smtp_port)
  smtp.ehlo()
  smtp.starttls()
  smtp.login(sender, password)
  smtp.send_message(message)
  smtp.quit()
  
print('Script execution complete!')
