import os
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


# def create_collage(photos: list, color, collage_size: tuple, collage_rows: int):
#     collage = Image.new(color, collage_size)
#     for photo in photos:
#         photo.resize(collage_size[0]/collage_rows, collage_size[1]/collage_rows)
#         collage.paste(photo, )

# def create_same_photo_collage(photo_path,  color, collage_size: tuple, collage_rows: int, collage_columns: int):
#     collage = Image.new(color, collage_size)
#     if collage_columns > 0 and collage_rows > 0 and collage_size[0] > 0 and collage_size[1] > 0:
#         photo = Image.open(photo_path).resize(collage_size[0]/collage_columns, collage_size[1]/collage_rows)
#     #     TO DO: paste photo on appropriate coords based on collage_size, columns and rows
#         for i in range(collage_rows):
#             for j in range(collage_columns):
#                 collage.paste(photo, (float(i * (collage_size[0]/collage_columns)),
#                                       float(i * (collage_size[1]/collage_columns))))
#
#     else:
#         raise ValueError("Collage columns, rows and size should be greater than 0.")
#     return collage


if __name__ == '__main__':
    download_photos()

    #     Create small collage

    small_collage = Image.new("RGBA", (1000, 1000))

    cat0_img = Image.open("photos/cat0.png").resize((500, 500))
    cat1_img = Image.open("photos/cat1.png").resize((500, 500))

    small_collage.paste(cat0_img, (0, 0))
    small_collage.paste(cat1_img, (500, 500))

    small_collage.show()

