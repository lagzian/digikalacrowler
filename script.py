# Install Selenium 
import sys
!{sys.executable} -m pip install selenium

# Import modules
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os
import smtplib
from email.message import EmailMessage
import datetime

# Selenium driver
options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)

# Parameters
url = 'https://www.digikala.com/incredible-offers/'
keywords = ['روغن', 'هدفون', 'ماوس']
test_message = "این یک ایمیل آزمایشی است"
sender = 'your_email@gmail.com'
recipient = 'recipient@email.com'
smtp_server = 'smtp.gmail.com'
smtp_port = 587  

# Load page
browser.get(url)
time.sleep(5)
source = browser.page_source
soup = BeautifulSoup(source, 'html.parser')

# Check keywords
keyword_found = False
for kw in keywords:
  if kw in soup.text:
    keyword_found = True
    break

# Close browser  
browser.close()   

# Send emails 
password = os.environ['EMAIL_PASS']

# Send test email
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

# Send keyword email
if keyword_found:
  msg = EmailMessage()
  msg['From'] = sender
  msg['To'] = recipient
  msg['Subject'] = 'Keyword Found'
  content = f'Keywords ({keywords}) found on {url}'
  msg.set_content(content)
  
  smtp.send_message(msg) 
print('Done')
