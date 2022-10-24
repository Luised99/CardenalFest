import random
from pygame.image import load
from pygame.math import Vector2 as vector
from pygame import Color

def load_sprite(name, with_alpha=True):
    path = f"Asteroid/src/assets/sprites/{name}.png"
    loaded_sprite = load(path)

    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()

def wrap_position(position, surface):
    x, y = position
    w, h = surface.get_size()
    return vector(x % w, y % h)

def get_random_position(surface):
    return vector(
        random.randrange(surface.get_width()),
        random.randrange(surface.get_height()),
    )

def get_random_velocity(min_speed, max_speed):
    speed = random.randint(min_speed, max_speed)
    angle = random.randrange(0, 360)
    return vector(speed, 0).rotate(angle)

def print_text(surface, text, font, color=Color("tomato")):
    text_surface = font.render(text, True, color)

    rect = text_surface.get_rect()
    rect.center = vector(surface.get_size()) / 2

    surface.blit(text_surface, rect)