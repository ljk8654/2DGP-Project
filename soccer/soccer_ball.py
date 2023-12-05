from pico2d import *
import world
import soccer
import game_framework
PIXEL_PER_METER = (1480 / 10)  # 1480 pixel 100 m
RUN_SPEED_KMPH = 50.0  # Km / Hour
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
        self.x, self. y = 400, 0
        Ball.image = load_image('ball21x21.png')
        self.dribble_state = 0
        self.shoot = 0
        self.shoot_range = 400
        self.x_dir,self.y_dir = 0, 0
        self.player_shoot = 0
        self.anemy_shoot = 0
        self.frame = 0
        self.x_move = 0
        self.y_move = 0
    def update(self):
        # 플레이어 슛

        if self.shoot == 1 and self.shoot_range > 0:
            self.shoot_range -= 10
            self.x += self.x_dir * RUN_SPEED_PPS * game_framework.frame_time
            self.y += self.y_dir * 5
            if self.y > self.bg.h -150 or self.y < 150:
                self.y_dir *= -1
        elif self.dribble_state == 1:
            self.x = soccer.player.x + 20 * soccer.player.x_dir + 2
            self.y = soccer.player.y - 5

        # 적 슛
        if self.shoot == 2 and self.shoot_range > 0:
            self.shoot_range -= 10
            self.x += self.x_dir * RUN_SPEED_PPS * game_framework.frame_time
            self.y += self.y_dir * 5
            if self.y > self.bg.h - 150 or self.y < 150:
                self.y_dir *= -1

        elif self.dribble_state == 2:
            self.x = soccer.anemy.x + 20 * soccer.anemy.xdir
            self.y = soccer.anemy.y - 5

        if self.shoot_range == 0:
            self.shoot_range = 400
            self.dribble_state = 0
            self.shoot = 0
            self.anemy_shoot, self.player_shoot = 0, 0
        self.x = clamp(110, self.x, self.bg.w - 150)
        self.y = clamp(140, self.y, self.bg.h - 100)

        if (self.x == 110 or self.x == self.bg.w - 150) and self.y > 350 and self.y < 550:

            if self.x == 110:
                soccer.score.anemy_score += 1
                soccer.player.x, soccer.player.y = 800, 420
                soccer.anemy.x, soccer.anemy.y = 1000, 420

            if self.x == self.bg.w - 150:
                soccer.score.player_score += 1
                soccer.anemy.x, soccer.anemy.y = 900, 420
                soccer.player.x, soccer.player.y = 600, 420

            self.x = self.bg.w // 2
            self.y = self.bg.h // 2
            soccer.player.stop = 1
            soccer.field.window_left = int(self.x) - soccer.field.cw // 2
            soccer.field.window_bottom = int(self.y) - soccer.field.ch // 2

            self.dribble_state = 0
            self.shoot = 0
            self.shoot_range = 400
            self.x_dir, self.y_dir = 0, 0
            self.player_shoot = 0
            self.anemy_shoot = 0
            self.frame = 0
            self.x_move = 0
            self.y_move = 0


        if self.x < self.x_move:
            self.frame = (self.frame + 1) % 4
        elif self.x == self.x_move and self.y_move == self.y:
            pass
        else:
            self.frame = (self.frame - 1) % 4
        self.x_move = self.x
        self.y_move = self.y


    def handle_event(self, event):
        pass
    def draw(self):
        sx, sy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        self.image.clip_draw(self.frame * 27, 0, 21, 21, sx, sy)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        sx, sy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        return sx - 10, sy - 10, sx + 10, sy + 10


    def set_background(self, bg):
        # fill here
        self.bg = bg
        self.x = self.bg.w//2
        self.y = self.bg.h//2
        pass

    def handle_collision(self, group, other):

        if group == 'anemy:ball':
            if self.dribble_state != 2 and self.anemy_shoot == 0:
                self.dribble_state = 2
                self.shoot_range = 300
                self.shoot = 0
                self.player_shoot = 0

        if group == 'player:ball':
            if self.dribble_state != 1 and self.player_shoot == 0:
                self.dribble_state = 1
                self.shoot_range = 300
                self.shoot = 0
                self.anemy_shoot = 0
            pass