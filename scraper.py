import requests
from bs4 import BeautifulSoup
import smtplib #enables you to send emails
import time

URL = 'https://www.crutchfield.com/p_575R165X3/Rockford-Fosgate-R165X3.html?tp=78072'

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.137 Safari/537.36 Viv/2.7.1628.33"}

def check_price():

    #Collects the headers of the website URL
    page = requests.get(URL, headers=headers
    #Parses through the html data. Still need to look more into this
    soup = BeautifulSoup(page.content, "html.parser")

    #Prints the entire HTML code fo the webpage
    #print(soup.prettify())

    #Collects the title and price of the device
    title = soup.find(class_=["prod-title"]).get_text()
    price = soup.find(class_=["price js-price"]).get_text().strip()
    converted_price = float(price[1:6])

    #Sends email if the price is less than specified amount
    if(converted_price <= 35):
        print("the price is at least as low as you wanted. Sending an email!")
        send_email()

def send_email():
    #Sets up server for the email. Must be port 587!
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo() #command sent to identify itself when connecting to another email
    server.starttls() #encrypts connection
    #login request
    server.login(user="ozunaclay@gmail.com", password="fctxjgvvivjxhxda")

    subject = "Price has dropped on the speakers you wanted!"
    body = "Check the link to crutchfield here: https://www.crutchfield.com/p_575R165X3/Rockford-Fosgate-R165X3.html?tp=78072"
    msg = f"Subject: {subject}\n\n{body}"
    #Who the email is coming from, where it's coming from, and the message
    server.sendmail(
    'ozunaclay@gmail.com',
    'ozunaclay@gmail.com',
    msg
    )
    print("Email has been sent about price drop!")

    server.quit()
    
while(True):
    check_price()
