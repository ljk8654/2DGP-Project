from pico2d import load_image, clear_canvas, update_canvas, get_events, get_time
import game_framework
import soccer
def init():
    global running
    global image
    global anemy_image
    global logo_start_time
    running = True
    image = load_image("player_win.png")
    anemy_image = load_image("player_lose.png")
    logo_start_time = get_time()
    pass

def finish():
    pass

def update():
    global running
    if get_time() - logo_start_time >= 2.0:
        game_framework.change_mode(soccer)
    pass

def draw():
    clear_canvas()
    if soccer.score.player_score >= soccer.score.anemy_score:
        image.draw(400,300)
    else:
        anemy_image.draw(400,300)
    update_canvas()
    pass
def handle_events():
    events = get_events()
    pass