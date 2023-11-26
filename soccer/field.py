from pico2d import *
import soccer
class Field:
    def __init__(self):
        self.image = load_image('field.png')
        # fill here
        self.cw = get_canvas_width()  # 화면 너비
        self.ch = get_canvas_height()  # 화면 높이
        self.w = self.image.w  # 배경의 너비
        self.h = self.image.h  # 배경의 높이

        pass

    def draw(self):
        # fill here
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom,
                                       self.cw, self.ch, 0, 0)
        pass

    def update(self):
        # fill here
        self.window_left = int(soccer.ball.x) - self.cw // 2
        self.window_left = clamp(0, self.window_left, self.w - self.cw - 1)

        self.window_bottom = int(soccer.ball.y) - self.ch // 2
        self.window_bottom = clamp(0, self.window_bottom, self.h - self.ch - 1)
        pass

    def handle_event(self, event):
        pass


