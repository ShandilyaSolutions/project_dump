"""Coding tasks :
    1. Get the covid data for India/Karnataka from Google
    2. Send data as a message on whatsapp
    3. Set this code on a server so that it runs continuously."""
import datetime

"""Documentation goes here"""
import requests
from bs4 import BeautifulSoup as bs
from datetime import date
import re

# Getting today's date in scraping suitable format
d = date.today()
date = str(d.strftime("%B %d, %Y"))
date_today = ''
for i in date:
    if i == ',':
        continue
    date_today = date_today + i


def dataGetter():
    """This function gets the covid data from the Ministry of Health and Family Welfare of India and scrapes its covid data for a date"""
    url = "https://www.mohfw.gov.in/"
    page = requests.get(url)
    html_code = bs(page.text, 'html.parser')
    # print(html_code.prettify())
    all_spans = html_code.find_all("span")

    # removing all useless lines from the lists
    data = list(all_spans)
    reg = r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$"

    for i in range(len(data)):
        check = str(data[i]).removeprefix('<span>').removesuffix('</span>')
        if re.search(reg, check):
            data = data[:i]
            break

    all_spans = data
    
    #raw_data = 
    """Now we have to select the data that is usefull for us and forward it to another function called messageWriter()"""

def messageWriter(raw_data):
    pass

def main():
    print(dataGetter())
    # dataGetter()


if __name__ == '__main__':
    main()
