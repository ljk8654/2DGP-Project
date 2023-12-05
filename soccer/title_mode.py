from pico2d import load_image, clear_canvas, update_canvas, get_events, get_time, load_font,SDL_QUIT
from sdl2 import SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE
import soccer
import game_framework

def init():
    global image
    global font
    font = load_font('ENCR10B.TTF', 40)
    image = load_image("title.jpg")


def finish():
    pass

def update():
    pass

def draw():
    clear_canvas()
    image.draw(400,300)
    font.draw(400, 100, 'Press Any Key', (255, 255, 255))
    update_canvas()
    pass
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            game_framework.change_mode(soccer)

    pass

