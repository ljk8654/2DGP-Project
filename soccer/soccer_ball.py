from pico2d import *




class Ball:
    def __init__(self):
        Ball.image = load_image('ball21x21.png')

    def update(self):
        pass
    def handle_event(self, event):
        pass

    def draw(self):
        self.image.draw(400, 300)
