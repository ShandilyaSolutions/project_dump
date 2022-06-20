"""Coding tasks :
    1. Get the covid data for India/Karnataka from Google
    2. Send data as a message on whatsapp
    3. Set this code on a server so that it runs continuously."""
import datetime

"""Documentation goes here"""
import requests
from bs4 import BeautifulSoup as bs
from datetime import date

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
    for element in all_spans[:: -1]:
        # implementing error handling
        try:
            d, m, y = element.split('.')
            try:
                if datetime.datetime(int(y), int(m), int(d)) == True:
                    all_spans.remove(element)
            except:
                continue
        except:
            continue

    print(all_spans)

    counter = 0
    requited_data = []  # holds fields necessary for our use
    message = "as on : " + date_today + ", 08:00 IST (GMT+5:30)"
    for span in all_spans:
        counter = counter + 1

    print(counter)
    counter = 0
    pass
    # return requited_data


def main():
    # print(dataGetter())
    dataGetter()


if __name__ == '__main__':
    main()
