from pico2d import *

import  soccer

open_canvas()
soccer.init()
# game loop
while soccer.running:
    soccer.handle_events()
    soccer.update()
    soccer.draw()
    delay(0.05)
# finalization code
soccer.finish()

close_canvas()