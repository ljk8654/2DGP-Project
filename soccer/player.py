from pico2d import *


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



class Move:
    @staticmethod
    def enter(player, e):
        if right_down(e) or left_up(e):
            player.x_dir, player.action, player.y_dir = 1, 3, 0
        elif left_down(e) or right_up(e):
            player.x_dir, player.action, player.y_dir = -1, 1, 0
        elif up_down(e) or up_up(e):
            player.y_dir, player.action, player.x_dir = 1, 2, 0
        elif down_down(e) or down_up(e):
            player.y_dir, player.action, player.x_dir = -1, 0, 0

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1) % 4
        player.x += player.x_dir * 5
        player.y += player.y_dir * 5
        pass

    @staticmethod
    def draw(player):
        if player.action == 3:
            player.image.clip_composite_draw(player.frame * 40, 43, 40, 43, 0,'h', player.x, player.y,40,43)
        else:
            player.image.clip_draw(player.frame * 40, player.action * 43, 40, 43, player.x, player.y)
        


class Idle:
    @staticmethod
    def enter(player, e):
        if player.action == 0:
            player.action = 0
        elif player.action == 1:
            player.action = 1

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + 1) % 4
        pass

    @staticmethod
    def draw(player):
        if player.action == 3:
            player.image.clip_composite_draw(player.frame * 40, 43, 40, 43, 0,'h', player.x, player.y,40,43)
        else:
            player.image.clip_draw(player.frame * 40, player.action * 43, 40, 43, player.x, player.y)

        pass


class StateMachine:
    def __init__(self, player):
        self.cur_state = Idle
        self.player = player
        self.transitions = {
            Idle: {right_down: Move, right_up: Move, left_down: Move, left_up: Move, down_down: Move, down_up: Move, up_down: Move, up_up: Move},
            Move: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle, down_down: Idle, up_down: Idle, up_up: Idle, down_up: Idle}
        }

    def start(self):
        self.cur_state.enter(self.player, ('NONE', 0))

    def handle_event(self, e):
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
        self.x, self.y = 400, 90
        self.frame = 0
        self.x_dir = 0
        self.y_dir = 0
        self.action = 1
        self.image = load_image('soccer_character_red.png')
        self.state_mashine = StateMachine(self)
        self.state_mashine.start()

    def update(self):
        self.frame = (self.frame + 1) % 4
        self.state_mashine.update()

    def handle_event(self, event):
        self.state_mashine.handle_event(('INPUT', event))
        pass

    def draw(self):
        self.state_mashine.draw()
        draw_rectangle(*self.get_bb())


    def get_bb(self):
        return self.x -20, self.y - 20, self.x+20,self.y+20

    def handle_collision(self, group, other):
        if group == 'player:ball':
            pass