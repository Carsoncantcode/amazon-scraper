import requests
from bs4 import BeautifulSoup
import pandas as pd

HEADERS = ({'User-Agent':'', 'Accept-Language': 'en-US, en;q=0.5'})



def scrapePage(url):
    fullURL = f'https://amazon.com{url}'

    response = requests.get(fullURL, headers=HEADERS)

    soup = BeautifulSoup(response.content, 'html.parser')

    title_element = soup.find('span', {'id': 'productTitle'})
    title = title_element.text.strip() 

    description_element = soup.find('div', {'id': 'feature-bullets'})
    description = description_element.text.strip() 

    price_element = soup.find('span', {'class': 'a-price-whole'})
    price = f'${price_element.text.strip()}' 

    rating_element = soup.find('span', {'class': 'a-icon-alt'})
    rating = rating_element.text.strip() 

    data = {
        'Product Title': [title],
        'Product Description': [description],
        'Product Price': [price],
        'Product Rating': [rating]
    }
    df = pd.DataFrame(data)

    df.to_csv('product_details.csv', mode='a', index=False, header=not pd.read_csv('product_details.csv').shape[0], encoding='utf-8')

    print("Data saved to product_details.csv")