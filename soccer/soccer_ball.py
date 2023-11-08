from pico2d import *



class Ball:
    def __init__(self):
        self.x, self. y = 400, 300
        Ball.image = load_image('ball21x21.png')

    def update(self):
        pass
    def handle_event(self, event):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x-10, self.y-10,self.x+10,self.y+10

    def handle_collision(self, group, other):
        if group == 'player:ball':
            self.x +=1
