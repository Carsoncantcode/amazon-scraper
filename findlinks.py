import requests
from bs4 import BeautifulSoup
from single import *

HEADERS = ({'User-Agent':'', 'Accept-Language': 'en-US, en;q=0.5'})

URL = "https://www.amazon.com/s?k=blow+dryer&crid=211AEJNCXPB12&sprefix=blow+dryer%2Caps%2C127&ref=nb_sb_noss_1"

site = requests.get(URL, headers=HEADERS)

soup = BeautifulSoup(site.content, "html.parser")

links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})


for link in links:
        link_href = link.get('href')
        print(f'Link: {link_href}')
        scrapePage(link_href)
