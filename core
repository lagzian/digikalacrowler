import requests 
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
import datetime
import os

# Set the website URL
url = 'https://www.digikala.com/incredible-offers/'

# Set the keywords to search for 
keywords = ['روغن', 'هدفون', 'ماوس']

# Set the email parameters
sender = 'nimahdx2000@gmail.com'
recipient = 'tech@zistarvin.ir'  
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Fetch the website content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Check if any of the keywords are present
keyword_found = False
for kw in keywords:
  if kw in soup.text:
    keyword_found = True
    break

# Send an email if a keyword was found  
if keyword_found:

  # Get password from environment variable
  password = os.environ['EMAIL_PASS']
  
  message = EmailMessage()
  message['From'] = sender
  message['To'] = recipient
  message['Subject'] = 'Keyword Found on Website'

  content = f'One of the keywords ({keywords}) was found on {url} on {datetime.datetime.now()}'
  message.set_content(content)

  smtp = smtplib.SMTP(smtp_server, smtp_port)
  smtp.ehlo()
  smtp.starttls()  
  smtp.login(sender, password)
  smtp.send_message(message)
  smtp.quit()
  
print('Script execution complete!')
