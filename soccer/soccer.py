from pico2d import *
import world
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
    global player

    running = True
    ball = Ball()
    player = Player()
    world.add_object(player, 1)
    world.add_object(ball, 0)
    world.add_collision_pair('player:ball',player,ball)
def finish():
    pass

def update():
        world.update()
        world.handle_collisions()


def draw():
    clear_canvas()
    world.render()
    update_canvas()

