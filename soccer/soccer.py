from pico2d import *
import world
import end_mode
from player import Player
from field import Field
from soccer_ball import Ball
import game_framework
from anemy import Anemy
from score import Score
from goal import Goal
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
    global score
    global player
    global ball
    global field
    global anemy
    global score
    field = Field()
    goal = Goal()
    ball = Ball()
    player = Player()
    anemy = Anemy()
    score = Score()
    world.add_object(field, 0)
    ball.set_background(field)
    world.add_object(anemy, 2)
    world.add_object(goal, 2)
    world.add_object(score, 2)
    world.add_object(player, 2)
    world.add_object(ball, 1)
    world.add_collision_pair('player:ball',player,ball)

    world.add_collision_pair('anemy:ball', anemy, ball)

def finish():
    world.clear()
    pass

def update():
        if player.stop == 0:
            world.update()
            world.handle_collisions()

        if  score.timer - score.time > 0:
             game_framework.change_mode(end_mode)


def draw():
    clear_canvas()
    world.render()
    update_canvas()

