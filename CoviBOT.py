"""Coding tasks :
    1. Get the covid data for India/Karnataka from Google (√)
    2. Send data as a message on whatsapp
    3. Set this code on a server so that it runs continuously."""
import os

"""Documentation goes here"""
import requests
from bs4 import BeautifulSoup as bs
from datetime import date
import json
from twilio.rest import Client

# setting up environment variables required for  twilio API
ACC_SID = ''
AUTH_TOKEN = ''

client = Client(ACC_SID,AUTH_TOKEN)

# Getting today's date in suitable format
d = date.today()
date = str(d.strftime("%B %d, %Y"))
date_today = ''
for i in date:
    if i == ',':
        continue
    date_today = date_today + i


def dataGetter():
    """This function gets the covid data from the Ministry of Health and Family Welfare of India and scrapes its covid data for a date"""
    url = "https://www.mohfw.gov.in/data/datanew.json"
    page = requests.get(url)
    html_code = bs(page.text, 'html.parser')
    # print(html_code.prettify())
    data = json.loads(str(html_code))
    # print(data)
    for item in data:
        # getting the data of Karnataka State situated at sno 16
        if item['sno'] == '16':
            return item


def messageWriter(raw_data):
    """This function converts the raw data acquired from the API into a presentable message format."""
    # print(type(raw_data))
    req = ['state_name', 'active', 'new_positive', 'new_active',]
    message = ""
    message = message + date_today + '\n'
    for itr in req:
        if itr == 'state_name':
            message = message + raw_data[itr] + '\n'
        else :
            message = message + itr.capitalize() + '  ->  ' + raw_data[itr] + '\n'
    return message


def messageSender(msg):
    """This function sends the message to the mobile number using Twilio's Whatsapp API."""
    message = client.messages.create(
        body=msg,
        from_='+16075272711',
        to='+919142861330'
    )
    print("Message Sent !")
    pass


def main():
    raw_data = dataGetter()
    msg = messageWriter(raw_data)
    messageSender(msg)


if __name__ == '__main__':
    main()
