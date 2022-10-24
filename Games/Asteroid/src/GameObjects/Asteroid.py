from pygame.math import Vector2 as vector
from src.utilities.load_model import GameObject
from src.utilities.load_sprite import load_sprite, get_random_velocity
from pygame.transform import rotozoom

class Asteroid(GameObject):

    def __init__(self, position, create_asteroid_callback, size=3):
        self.create_asteroid_callback = create_asteroid_callback
        self.size = size

        size_to_scale = {
            3: 1,
            2: 0.5,
            1: 0.25,
        }
        scale = size_to_scale[size]
        sprite = rotozoom(load_sprite("asteroid"), 0, scale)

        super().__init__(
            position, sprite, get_random_velocity(1, 3)
        )

    def split(self):
        if self.size > 1:
            for _ in range(2):
                asteroid = Asteroid(
                    self.position, self.create_asteroid_callback, self.size - 1
                )
                self.create_asteroid_callback(asteroid)