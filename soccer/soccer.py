from pico2d import *

from player import Player

from soccer_ball import Ball

# Game object class here


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            player.handle_event(event)


def init():
    global running
    global grass
    global team
    global world
    global player

    running = True
    world = []
    ball = Ball()
    player = Player()
    world.append(player)
    world.append(ball)

def finish():
    pass

def update():
    for o in world:
        o.update()
    pass


def draw():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

def collide(a,b):
    left_a,bottom_a,right_a,top_a = a.get_bb()
    left_b,bottom_b,right_b,top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True