from PIL import Image, ImageEnhance


def custom_photo_brightness(photo: Image, bright_factor: float):
    custom_photo = ImageEnhance.Brightness(photo).enhance(bright_factor)
    return custom_photo


def custom_photo_color(photo: Image, color_factor: float):
    custom_photo = ImageEnhance.Color(photo).enhance(color_factor)
    return custom_photo
