from pico2d import *
import soccer
class Field:
    def __init__(self):
        self.image = load_image('field.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(370, 670)


