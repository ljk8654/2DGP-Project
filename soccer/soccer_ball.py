from pico2d import *
import world
import soccer
import game_framework
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 30.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10.0

def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE

def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT


def up_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP


def up_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_UP


def down_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_DOWN


def down_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_DOWN



class Ball:

    def __init__(self):
        self.x, self. y = 400, 300
        Ball.image = load_image('ball21x21.png')
        self.dribble_state = 0
        self.shoot = 0
        self.shoot_range = 100

    def update(self):
        if self.dribble_state != 1 and self.shoot == 1 and self.shoot_range > 0:
            self.shoot_range -= 10
            self.x += soccer.player.x_dir * 10
            self.y += soccer.player.y_dir * 10
        elif self.dribble_state == 1:
            self.x = soccer.player.x + 10 * soccer.player.x_dir
            self.y = soccer.player.y + 10 * soccer.player.y_dir

        if self.shoot_range == 0:
            self.shoot_range = 100
            self.dribble_state = 0
            self.shoot = 0

    def handle_event(self, event):
        pass
    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x-10, self.y-10,self.x+10,self.y+10


    def handle_collision(self, group, other):
        if group == 'player:ball':
            if self.dribble_state == 0:
                self.dribble_state = 1
            pass