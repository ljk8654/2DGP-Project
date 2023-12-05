from pico2d import *
import soccer
import end_mode

class Goal:
    def __init__(self):
        self.font = load_font('ENCR10B.TTF', 20)
        self.image = load_image('goal.png')
        self.playerimage = load_image('player_goal.png')
        self.anemyimage = load_image('anemy_goal.png')

        self.x = soccer.field.w//4
        self.y = soccer.field.h//2

        pass

    def draw(self):
        if soccer.player.stop == 1:
            if soccer.player.x == 600:
                self.image.draw(self.x, self.y)
                self.playerimage.draw(self.x - 10, self.y + 80)
                self.font.draw(self.x - 110, self.y - 50, f'press "s" to start', (255, 255, 0))
            else:
                self.image.draw(self.x, self.y)
                self.anemyimage.draw(self.x - 10, self.y + 80)
                self.font.draw(self.x - 110, self.y - 50, f'press "s" to start', (255, 255, 0))

    def update(self):
            # fill here

            pass

    def handle_event(self, event):
        pass

