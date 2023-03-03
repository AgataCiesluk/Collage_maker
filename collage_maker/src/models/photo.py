from PIL import Image


class Photo(Image):
    path: str

    def __init__(self, path):
        self.path = path

    @property
    def width(self):
        return self.width

    @property
    def height(self):
        return self.height
