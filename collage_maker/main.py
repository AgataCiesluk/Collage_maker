from collage_maker.src.collage.creation import create_photo_collage
from collage_maker.src.collage.effects import custom_photo_brightness

if __name__ == '__main__':

    photo_collage = create_photo_collage(['photos/cat1.png', 'photos/cat0.png'], 'RGB',
                                         (4000, 4000), 4, 4, custom_photo_brightness)
    photo_collage.show()
