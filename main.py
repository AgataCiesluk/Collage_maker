import os
import urllib.request

import requests
from dotenv import load_dotenv

if __name__ == '__main__':

    topic = 'cat'

    load_dotenv()
    API_ACCESS_KEY = os.getenv('API_ACCESS_KEY')

    response = requests.get(f'https://api.unsplash.com/search/photos?client_id={API_ACCESS_KEY}&page=1&query={topic}')

    data = {}
    if response.status_code == 200:
        data = response.json()

    urls_small_photos = []
    for element in data['results']:
        urls_small_photos.append(element['urls']['small'])

    for index, url in enumerate(urls_small_photos):
        urllib.request.urlretrieve(url, f'photos/cat{index}.png')
