from pico2d import *
import game_framework
PIXEL_PER_METER = (1480.0 / 10)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
import soccer

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



class RunRight:
    @staticmethod
    def enter(player, e):
        player.action = 3
        player.speed = RUN_SPEED_PPS
        player.dir = 0
        player.x_dir = 1
        player.y_dir = 0

    @staticmethod
    def exit(player, e):
        if space_down(e):
            player.shoot()
    @staticmethod
    def do(player):
        player.x += math.cos(player.dir) * player.speed * game_framework.frame_time
        player.y += math.sin(player.dir) * player.speed * game_framework.frame_time
        player.frame = (player.frame + 1) % 4

    def draw(player):
        sx, sy = player.x - soccer.field.window_left, player.y - soccer.field.window_bottom
        player.image.clip_composite_draw(player.frame * 40, 43, 40, 43, 0, 'h', sx, sy, 40, 43)

class RunRightUp:
    @staticmethod
    def enter(player, e):
        player.action = 3
        player.speed = RUN_SPEED_PPS
        player.dir = math.pi / 4.0
        player.x_dir = 1
        player.y_dir = 1

    @staticmethod
    def exit(player, e):

        if space_down(e):
            player.shoot()
        pass

    @staticmethod
    def do(player):
        player.x += math.cos(player.dir) * player.speed * game_framework.frame_time
        player.y += math.sin(player.dir) * player.speed * game_framework.frame_time
        player.frame = (player.frame + 1) % 4

    def draw(player):
        sx, sy = player.x - soccer.field.window_left, player.y - soccer.field.window_bottom
        player.image.clip_composite_draw(player.frame * 40, 43, 40, 43, 0, 'h', sx, sy, 40, 43)


class RunRightDown:
    @staticmethod
    def enter(player, e):
        player.action = 3
        player.speed = RUN_SPEED_PPS
        player.dir = -math.pi / 4.0
        player.x_dir = 1
        player.y_dir = -1

    @staticmethod
    def exit(player, e):

        if space_down(e):
            player.shoot()
        pass

    @staticmethod
    def do(player):
        player.x += math.cos(player.dir) * player.speed * game_framework.frame_time
        player.y += math.sin(player.dir) * player.speed * game_framework.frame_time
        player.frame = (player.frame + 1) % 4

    def draw(player):
        sx, sy = player.x - soccer.field.window_left, player.y - soccer.field.window_bottom
        player.image.clip_composite_draw(player.frame * 40, 43, 40, 43, 0, 'h', sx, sy, 40, 43)


class RunLeft:
    @staticmethod
    def enter(player, e):
        player.action = 1
        player.speed = RUN_SPEED_PPS
        player.dir = math.pi
        player.x_dir = -1
        player.y_dir = 0

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        player.x += math.cos(player.dir) * player.speed * game_framework.frame_time
        player.y += math.sin(player.dir) * player.speed * game_framework.frame_time

        player.frame = (player.frame + 1) % 4

    def draw(player):
        sx, sy = player.x - soccer.field.window_left, player.y - soccer.field.window_bottom
        player.image.clip_draw(player.frame * 40, player.action * 43, 40, 43, sx, sy)


class RunLeftUp:
    @staticmethod
    def enter(player, e):
        player.action = 1
        player.speed = RUN_SPEED_PPS
        player.dir = math.pi * 3.0 / 4.0
        player.x_dir = -1
        player.y_dir = 1

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        player.x += math.cos(player.dir) * player.speed * game_framework.frame_time
        player.y += math.sin(player.dir) * player.speed * game_framework.frame_time
        player.frame = (player.frame + 1) % 4

    def draw(player):
        sx, sy = player.x - soccer.field.window_left, player.y - soccer.field.window_bottom
        player.image.clip_draw(player.frame * 40, player.action * 43, 40, 43, sx, sy)
class RunLeftDown:
    @staticmethod
    def enter(player, e):
        player.action = 1
        player.speed = RUN_SPEED_PPS
        player.dir = - math.pi * 3.0 / 4.0
        player.x_dir = -1
        player.y_dir = -1

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        player.x += math.cos(player.dir) * player.speed * game_framework.frame_time
        player.y += math.sin(player.dir) * player.speed * game_framework.frame_time
        player.frame = (player.frame + 1) % 4

    def draw(player):
        sx, sy = player.x - soccer.field.window_left, player.y - soccer.field.window_bottom
        player.image.clip_draw(player.frame * 40, player.action * 43, 40, 43, sx, sy)
class RunUp:
    @staticmethod
    def enter(player, e):
        player.action = 2
        player.speed = RUN_SPEED_PPS
        player.dir = math.pi / 2.0
        player.x_dir = 0
        player.y_dir = 1

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        player.x += math.cos(player.dir) * player.speed * game_framework.frame_time
        player.y += math.sin(player.dir) * player.speed * game_framework.frame_time
        player.frame = (player.frame + 1) % 4

    def draw(player):
        sx, sy = player.x - soccer.field.window_left, player.y - soccer.field.window_bottom
        player.image.clip_draw(player.frame * 40, player.action * 43, 40, 43, sx, sy)
class RunDown:
    @staticmethod
    def enter(player, e):
        player.action = 0
        player.speed = RUN_SPEED_PPS
        player.dir = - math.pi / 2.0
        player.x_dir = 0
        player.y_dir = -1

        pass

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        player.x += math.cos(player.dir) * player.speed * game_framework.frame_time
        player.y += math.sin(player.dir) * player.speed * game_framework.frame_time
        player.frame = (player.frame + 1) % 4

        pass

    def draw(player):
        sx, sy = player.x - soccer.field.window_left, player.y - soccer.field.window_bottom
        player.image.clip_draw(player.frame * 40, player.action * 43, 40, 43, sx, sy)

class Idle:
    @staticmethod
    def enter(player, e):
        if player.action == 0:
            player.action = 0
        elif player.action == 1:
            player.action = 1

    @staticmethod
    def exit(player, e):

        if space_down(e):
            player.shoot()
            print(1)
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1) % 4
        pass

    @staticmethod
    def draw(player):
        sx, sy = player.x - soccer.field.window_left, player.y - soccer.field.window_bottom
        if player.action == 3:
            player.image.clip_composite_draw(player.frame * 40, 43, 40, 43, 0, 'h', sx, sy, 40, 43)
        else:
            player.image.clip_draw(player.frame * 40, player.action * 43, 40, 43, sx, sy)

class StateMachine:
    def __init__(self, player):
        self.cur_state = Idle
        self.player = player
        self.transitions = {
            Idle: {right_down: RunRight, left_down: RunLeft, left_up: RunRight, right_up: RunLeft, up_down: RunUp,
                   down_down: RunDown, up_up: RunDown, down_up: RunUp},
            RunRight: {right_up: Idle, left_down: Idle, up_down: RunRightUp, up_up: RunRightDown,
                       down_down: RunRightDown, down_up: RunRightUp},
            RunRightUp: {up_up: RunRight, right_up: RunUp, left_down: RunUp, down_down: RunRight},
            RunUp: {up_up: Idle, left_down: RunLeftUp, down_down: Idle, right_down: RunRightUp,
                    left_up: RunRightUp, right_up: RunLeftUp},
            RunLeftUp: {right_down: RunUp, down_down: RunLeft, left_up: RunUp, up_up: RunLeft},
            RunLeft: {left_up: Idle, up_down: RunLeftUp, right_down: Idle, down_down: RunLeftDown,
                      up_up: RunLeftDown, down_up: RunLeftUp},
            RunLeftDown: {left_up: RunDown, down_up: RunLeft, up_down: RunLeft, right_down: RunDown},
            RunDown: {down_up: Idle, left_down: RunLeftDown, up_down: Idle, right_down: RunRightDown,
                      left_up: RunRightDown, right_up: RunLeftDown},
            RunRightDown: {right_up: RunDown, down_up: RunRight, left_down: RunDown, up_down: RunRight}     }

    def start(self):
        self.cur_state.enter(self.player, ('NONE', 0))

    def handle_event(self, e):
        if space_down(e) and soccer.ball.dribble_state == 1:
            soccer.ball.shoot = 1
            soccer.ball.dribble_state = 2
            soccer.ball.x_dir = self.player.x_dir
            soccer.ball.y_dir = self.player.y_dir
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.player, e)
                self.cur_state = next_state
                self.cur_state.enter(self.player, e)
                return True
        return False

    def update(self):
        self.cur_state.do(self.player)

        pass

    def draw(self):
        self.cur_state.draw(self.player)


class Player:
    def __init__(self):
        self.x, self.y = 800, 600
        self.frame = 0
        self.x_dir = 0
        self.y_dir = 0
        self.action = 1
        self.image = load_image('soccer_character_red.png')
        self.state_mashine = StateMachine(self)
        self.state_mashine.start()

    def update(self):
        self.state_mashine.update()

    def handle_event(self, event):
        self.state_mashine.handle_event(('INPUT', event))
        pass

    def draw(self):
        self.state_mashine.draw()
        draw_rectangle(*self.get_bb())


    def get_bb(self):
        sx, sy = self.x - soccer.field.window_left, self.y - soccer.field.window_bottom
        return sx -20, sy - 20, sx+20,sy+20

    def handle_collision(self, group, other):
        if group == 'player:ball':
            pass

    def shoot(self):
        soccer.ball.shoot =1
        soccer.ball.dribble_state = 2

