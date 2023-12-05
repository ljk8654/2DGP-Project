from pico2d import load_image, clear_canvas, update_canvas, get_events, get_time,SDL_QUIT,SDL_KEYDOWN,SDLK_ESCAPE
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
        soccer.score.timer = 0
        soccer.score.time = 180
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
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()

    pass