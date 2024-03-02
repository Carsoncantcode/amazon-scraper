import requests
from bs4 import BeautifulSoup
from single import *

HEADERS = ({'User-Agent':'', 'Accept-Language': 'en-US, en;q=0.5'})

URL = "https://www.amazon.com/s?k=playstation+5+controller&crid=O6SMRR3W2D6B&sprefix=playstar%2Caps%2C137&ref=nb_sb_ss_ts-doa-p_3_8"

site = requests.get(URL, headers=HEADERS)

soup = BeautifulSoup(site.content, "html.parser")

links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})


for link in links:
        link_href = link.get('href')
        print(f'Link: {link_href}')
        scrapePage(link_href)
