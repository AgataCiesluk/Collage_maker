import random

from PIL import Image


def create_photo_collage(photo_paths: list[str], color, collage_size: tuple,
                         collage_rows: int, collage_columns: int, effect=None):
    collage = Image.new(color, collage_size)
    photos = []

    if collage_columns > 0 and collage_rows > 0 and collage_size[0] > 0 and collage_size[1] > 0:
        for photo_path in photo_paths:
            photo = Image.open(photo_path)
            if effect:
                photo = effect(photo, 1)
            photo = photo.resize(
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
