from pico2d import *
import soccer
class Field:
    def __init__(self):
        self.y = 450
        self.image = load_image('field.png')

    def update(self):
        self.y = 450 - soccer.ball.y
        if self.y < 100:
            self.y = 100
        pass

    def draw(self):
        self.image.draw(0, self.y)


