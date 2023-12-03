from pico2d import *
import soccer
class Score:
    def __init__(self):
        self.font = load_font('ENCR10B.TTF', 15)
        self.image = load_image('soccer_score.png')
        # fill here
        self.x = 800
        self.y = 2000

        pass

    def draw(self):
        # fill here
        sx, sy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        self.image.draw(sx, sy)
        self.font.draw(sx - 92, sy, f'{20:02d}', (255, 255, 0))
        self.font.draw(sx + 66, sy, f'{20:02d}', (255, 255, 0))
        self.font.draw(sx - 10 , sy, f'{90:02d}', (255, 255, 0))

        draw_rectangle(*self.get_bb())


    def update(self):
            # fill here
            self.x = soccer.ball.x - self.bg.w//8 - 20
            self.y = soccer.ball.y + self.bg.h//4 + 50
            self.x = clamp(180, self.x, self.bg.w - 600)
            self.y = clamp(550, self.y, self.bg.h - 50)

            pass

    def handle_event(self, event):
        pass

    def get_bb(self):
        sx, sy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        return sx - 10, sy - 10, sx + 10, sy + 10

    def set_background(self, bg):
        # fill here
        self.bg = bg
        self.x = self.bg.w//2
        self.y = self.bg.h - 50
        pass

