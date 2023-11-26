from pico2d import *
import world

from player import Player
from field import Field
from soccer_ball import Ball
import game_framework
# Game object class here


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            player.handle_event(event)
            ball.handle_event(event)


def init():
    global player
    global ball
    global field
    field = Field()
    ball = Ball()
    player = Player()
    world.add_object(field, 0)
    ball.set_background(field)

    world.add_object(player, 2)
    world.add_object(ball, 1)
    world.add_collision_pair('player:ball',player,ball)

def finish():
    world.clear()
    pass

def update():
        world.update()
        world.handle_collisions()


def draw():
    clear_canvas()
    world.render()
    update_canvas()

