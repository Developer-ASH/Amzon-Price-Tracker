import requests
from bs4 import BeautifulSoup
import smtplib
import re

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

URL = 'https://www.amazon.in/Sony-ILCE-7M3-Full-Frame-Mirrorless-Interchangeable/dp/B07CJ7NJHG/ref=sr_1_2?dchild=1&keywords=sony+a7s+iii&qid=1621537396&sr=8-2'



    
#Check the price off the Cammera

def check_price():
    page = requests.get(URL, headers=headers)
    
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = price[0:10]
    final_price = re.sub("[₹]", "", converted_price)
    final_price1 = float(re.sub("[,]", "", final_price))

    print(final_price1)
    print(title.strip())


    if (final_price1 <150000.0):
        send_mail()

def send_mail():
    
    mailID = ''
    mailPWD = ''
    server = smtplib.SMTP('smtp.google.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(mailID, mailPWD)
    subject = 'Price fell down!'
    body = 'Check the link https://www.amazon.in/Sony-ILCE-7M3-Full-Frame-Mirrorless-Interchangeable/dp/B07CJ7NJHG/ref=sr_1_2?dchild=1&keywords=sony+a7s+iii&qid=1621537396&sr=8-2'
    msg  = f"Subject: {subject} \n\n{body}"
    server.sendmail(
        'dinakar.pathakota@gmail.com',
        'dev.dinakar.pathakota@gmail.com',
        msg
    )
    server.quit()
    print('Mail SENT...')

check_price()
