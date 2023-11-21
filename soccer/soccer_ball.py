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

class Shoot:

    def enter(ball, e):
        ball.ball_range = 200

        pass
    @staticmethod
    def exit(ball, e):
        pass

    @staticmethod
    def do(ball):
        if ball.ball_range > 0:
            ball.x += ball.x_dir * RUN_SPEED_PPS * game_framework.frame_time
            ball.y += ball.y_dir * RUN_SPEED_PPS * game_framework.frame_time
            ball.x = clamp(25, ball.x, 1280 - 25)
            ball.y = clamp(25, ball.y, 1024 - 25)

            if ball.x < 115 or ball.x > 640:
                ball.x_dir *= -1
                ball.y_dir *= -1

            ball.ball_range -= 10
            print(ball.ball_range)
        if ball.ball_range == 0:
            ball.state_mashine = ball_state(ball)
            ball.dribble_state =0
            print(2)
        pass

    @staticmethod
    def draw(ball):
        ball.image.draw(ball.x, ball.y)

class Move:
    @staticmethod
    def enter(ball, e):
        if right_down(e) or left_up(e):
            ball.x = soccer.player.x + 20
            ball.y = soccer.player.y
            ball.x_dir, ball.y_dir = 1, 0
        elif left_down(e) or right_up(e):
            ball.x = soccer.player.x - 20
            ball.y = soccer.player.y
            ball.x_dir, ball.y_dir = -1, 0
        elif up_down(e) or up_up(e):
            ball.x = soccer.player.x + 5
            ball.y = soccer.player.y + 20
            ball.y_dir, ball.x_dir = 1, 0
        elif down_down(e) or down_up(e):
            ball.x = soccer.player.x + 5
            ball.y = soccer.player.y - 20
            ball.y_dir, ball.x_dir = -1, 0

    @staticmethod
    def exit(ball, e):
        pass

    @staticmethod
    def do(ball):
        ball.x += ball.x_dir * RUN_SPEED_PPS * game_framework.frame_time
        ball.y += ball.y_dir * RUN_SPEED_PPS * game_framework.frame_time
        ball.x = clamp(25, ball.x, 1280 - 25)
        ball.y = clamp(25, ball.y, 1024 - 25)

    pass

    @staticmethod
    def draw(ball):
        ball.image.draw(ball.x, ball.y)


class Idle:
    @staticmethod
    def enter(ball, e):
        pass
    @staticmethod
    def exit(ball, e):
        pass

    @staticmethod
    def do(ball):

        pass

    @staticmethod
    def draw(ball):
        ball.image.draw(ball.x, ball.y)


class StateMachine:
    def __init__(self, ball):
        self.cur_state = Move
        self.ball = ball
        self.transitions = {
            Idle: {right_down: Move, right_up: Move, left_down: Move, left_up: Move, down_down: Move, down_up: Move,
                   up_down: Move, up_up: Move},
            Move: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle, down_down: Idle, up_down: Idle,
                   up_up: Idle, down_up: Idle, space_down: Shoot},
            Shoot: {right_down: Idle}
        }

    def start(self):
        self.cur_state.enter(self.ball, ('NONE', 0))

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.ball, e)
                self.cur_state = next_state
                self.cur_state.enter(self.ball, e)
                return True
        return False

    def update(self):
        self.cur_state.do(self.ball)
        pass

    def draw(self):
        self.cur_state.draw(self.ball)

class ball_state:
    def __init__(self, ball):
        self.ball = ball

    def start(self):
        pass
    def handle_event(self, e):
        pass
    def update(self):
        pass

    def draw(self):
        self.ball.image.draw(self.ball.x,self.ball.y)

class Ball:

    def __init__(self):
        self.x, self. y = 400, 300
        Ball.image = load_image('ball21x21.png')
        self.dribble_state = 0
        self.x_dir = 0
        self.y_dir = 0
        self.state_mashine = ball_state(self)

    def update(self):
        self.state_mashine.update()

    def handle_event(self, event):
        self.state_mashine.handle_event(('INPUT', event))

    def draw(self):
        self.state_mashine.draw()
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x-10, self.y-10,self.x+10,self.y+10


    def handle_collision(self, group, other):
        if group == 'player:ball':
            print(1)
            if self.dribble_state == 0:
                self.dribble_state = 1
                self.state_mashine = StateMachine(self)
                self.state_mashine.start()
                print(2)
            pass