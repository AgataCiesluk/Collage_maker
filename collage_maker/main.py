import os
import urllib.request

import requests
from dotenv import load_dotenv
from json.decoder import JSONDecodeError
from PIL import Image

load_dotenv()
API_ACCESS_KEY = os.getenv('API_ACCESS_KEY')


def get_url_for_given_photos_params(topic, photos_quantity, api_key):
    return f'https://api.unsplash.com/search/photos?client_id={api_key}&page=2&query={topic}&per_page={photos_quantity}'


def download_photos():
    response = requests.get(get_url_for_given_photos_params('cat', 4, API_ACCESS_KEY))

    if response.status_code == 200:
        data = response.json()
        if not data:
            raise JSONDecodeError

        urls_small_photos = []
        for element in data['results']:
            urls_small_photos.append(element['urls']['small'])

        for index, url in enumerate(urls_small_photos):
            urllib.request.urlretrieve(url, f'photos/cat{index}.png')
    else:
        response.raise_for_status()


if __name__ == '__main__':
    download_photos()

    #     Create small collage

    small_collage = Image.new("RGBA", (1000, 1000))

    cat0_img = Image.open("photos/cat0.png").resize((500, 500))
    cat1_img = Image.open("photos/cat1.png").resize((500, 500))

    small_collage.paste(cat0_img, (0, 0))
    small_collage.paste(cat1_img, (500, 500))

    small_collage.show()
