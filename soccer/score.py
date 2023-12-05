from pico2d import *
import soccer
import end_mode
class Score:
    def __init__(self):
        self.font = load_font('ENCR10B.TTF', 15)
        self.image = load_image('soccer_score.png')
        self.player_score = 0
        self.anemy_score = 0
        self.time = int(get_time()) + 60
        self.timer = int(get_time())

        # fill here
        self.x = 150
        self.y = 550

        pass

    def draw(self):
        # fill here
        self.image.draw(self.x, self.y)
        self.font.draw(self.x - 92, self.y, f'{self.player_score:02d}', (255, 255, 255))
        self.font.draw(self.x + 66, self.y, f'{self.anemy_score:02d}', (255, 255, 255))
        self.font.draw(self.x - 10 , self.y, f'{self.time - self.timer:02d}', (255, 255, 255))



    def update(self):
            # fill here
            if soccer.player.stop == 0:
                self.timer = int(get_time())


            pass

    def handle_event(self, event):
        pass

