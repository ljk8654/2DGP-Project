from pico2d import *

import random
import math
import game_framework
import world
from behavior_tree import BehaviorTree, Action, Sequence, Condition, Selector
import soccer


# zombie Run Speed
PIXEL_PER_METER = (14.8 / 0.1)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 5.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
print(RUN_SPEED_PPS)
# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10.0

animation_names = ['Walk', 'Idle']


class Anemy:

    def load_image(self):
        Anemy.font = load_font('ENCR10B.TTF', 30)
        Anemy.image = load_image('soccer_character_blue.png')
        pass

    def __init__(self, name='Noname', x=1000, y=420, size=1.0):
        self.name, self.x, self.y, self.size = name, x, y, size
        self.load_image()
        self.dir = 0.0      # radian 값으로 방향을 표시
        self.xdir = -1
        self.ydir = 0
        self.speed = RUN_SPEED_PPS
        self.state = 'Idle'
        self.frame = 1
        self.tx, self.ty = 0, 0
        self.build_behavior_tree()
        self.action =0
    def __getstate__(self):
        state = {'name': self.name, 'x': self.x, 'y': self.y, 'size': self.size}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)



    def get_bb(self):
        sx, sy = self.x - soccer.field.window_left, self.y - soccer.field.window_bottom
        return sx - 20, sy - 20, sx + 20, sy + 20


    def update(self):
        self.frame = (self.frame + 1) % 4
        self.bt.run()


    def draw(self):
        draw_rectangle(*self.get_bb())
        sx, sy = self.x - soccer.field.window_left, self.y - soccer.field.window_bottom
        if self.xdir > 0:
            self.image.clip_composite_draw(self.frame * 35, 43, 35, 43, 0, 'h', sx, sy, 40, 43)
        else:
            self.image.clip_draw(self.frame * 35, 43, 35, 43, sx, sy)

    # draw name
        # draw target location

    def handle_event(self, event):
        pass

    def handle_collision(self, group, other):
        pass


    def distance_less_than(self, x1, y1, x2, y2, r):
        distance2 = (x1 - x2) ** 2 + (y1 - y2) ** 2
        return distance2 < (PIXEL_PER_METER * r) ** 2

    def move_slightly_to(self, tx, ty):
        self.dir = math.atan2(ty - self.y, tx - self.x)
        if(tx - self.x < 0):
            self.xdir = -1
        else:
            self.xdir = 1
        if (ty - self.y < 0):
            self.ydir = -1
        else:
            self.ydir = 1
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time


    def chase_ball (self, r=0.1):
        self.state = 'Walk'
        self.move_slightly_to(soccer.ball.x, soccer.ball.y)
        if self.distance_less_than(soccer.ball.x, soccer.ball.y, self.x, self.y, r):
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING

    def ball_owner(self):
        if soccer.ball.dribble_state == 2:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL
    def move_goalpost(self, r= 0.1):
        self.state = 'RUN'
        self.speed = RUN_SPEED_PPS * 2
        self.move_slightly_to(300, 420)
        if self.distance_less_than(300, 420, self.x, self.y, r):
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING
    def ball_shoot(self):
        soccer.ball.x_dir = self.xdir
        soccer.ball.y_dir = self.ydir
        print(self.xdir)
        soccer.ball.dribble_state = 0
        soccer.ball.shoot = 2
        soccer.ball.anemy_shoot = 1
        return BehaviorTree.SUCCESS
    def is_run(self, r= 0.1):
        print(777777777777777777777777777777)
        self.speed = RUN_SPEED_PPS * 2

        self.state = 'Walk'
        self.move_slightly_to(soccer.ball.x, soccer.ball.y)
        if self.distance_less_than(soccer.ball.x, soccer.ball.y, self.x, self.y, r):
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING


    def is_walk(self, r = 0.1):
        self.state = 'Walk'
        self.speed = RUN_SPEED_PPS
        self.move_slightly_to(soccer.ball.x, soccer.ball.y)
        if self.distance_less_than(soccer.ball.x, soccer.ball.y, self.x, self.y, r):
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING


    def is_ball_nearby(self, r = 1):
        print(8888888888888888888888)
        if self.distance_less_than(soccer.ball.x, soccer.ball.y, self.x, self.y, r):
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL


    def build_behavior_tree(self):
        a1 = Action('chase ball', self.chase_ball)
        c1 = Condition('볼 소유', self.ball_owner)
        a2 = Action('상대방 골대로 간다', self.move_goalpost)
        a3 = Action('공을 찬다', self.ball_shoot)
        a4 = Action('달린다',self.is_run)
        a5 = Action('걷는다', self.is_walk)
        c2 = Condition('공이 근처에 있는가?', self.is_ball_nearby)
        SEQ_nearly_run = Sequence('공이 근처에 있으면 뛴다', c2, a4)
        SEL_run_or_walk = Selector('뛰거나 걷는다',SEQ_nearly_run, a5)
        SEQ_OWNER_GOALPOST = Sequence('공을 가지고 있으면 상대방 골대로 간다', c1, a2)
        SEL_ball_chase_or_move = Selector('공이 없으면 공을 추적, 있으면 골대로', SEQ_OWNER_GOALPOST, SEL_run_or_walk)
        root = SEQ_OWNER_GOAL = Sequence(' 골대근처에 있으면 공을 찬다', SEL_ball_chase_or_move, a3)
        self.bt = BehaviorTree(root)