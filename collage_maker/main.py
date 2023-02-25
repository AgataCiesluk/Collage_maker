import os
import random
import urllib.request

import requests
from dotenv import load_dotenv
from json.decoder import JSONDecodeError
from PIL import Image

load_dotenv()
API_ACCESS_KEY = os.getenv('API_ACCESS_KEY')


def get_url_for_given_photos_params(topic, photos_quantity, api_key):
    return f'https://api.unsplash.com/search/photos?client_id={api_key}&page=1&query={topic}&per_page={photos_quantity}'


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
            urllib.request.urlretrieve(url, f'collage_maker/photos/cat{index}.png')
    else:
        response.raise_for_status()


def create_photo_collage(photo_paths: list[str], color, collage_size: tuple, collage_rows: int, collage_columns: int):
    collage = Image.new(color, collage_size)
    photos = []

    if collage_columns > 0 and collage_rows > 0 and collage_size[0] > 0 and collage_size[1] > 0:
        for photo_path in photo_paths:
            photo = Image.open(photo_path).resize(
                (collage_size[0] // collage_columns,
                 collage_size[1] // collage_rows))
            photos.append(photo)
        for i in range(collage_rows):
            for j in range(collage_columns):
                collage.paste(random.choice(photos),
                              (j * (collage_size[0] // collage_columns),
                               i * (collage_size[1] // collage_rows)))
    else:
        raise ValueError("Collage columns, rows and size should be greater than 0.")
    return collage


if __name__ == '__main__':
    # download_photos()

    photo_collage = create_photo_collage(['photos/cat1.png', 'photos/cat0.png'], 'RGB', (4000, 4000), 4, 4)
    photo_collage.show()
