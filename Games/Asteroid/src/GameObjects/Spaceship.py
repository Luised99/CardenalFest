from pygame.math import Vector2 as vector
from src.utilities.load_model import GameObject
from src.utilities.load_sprite import load_sprite
from pygame.transform import rotozoom
from src.GameObjects.Bullet import Bullet

class Spaceship(GameObject):
    
    MANEUVERABILITY = 3
    ACCELERATION = 0.05
    BULLET_SPEED = 3

    def __init__(self, position, create_bullet_callback, size=1):
        self.create_bullet_callback = create_bullet_callback
        self.direction = vector(super().UP)
        size_to_scale = { 1 : 0.25}
        scale = size_to_scale[size]
        sprite = rotozoom(load_sprite("spaceship"), 0, scale)
        super().__init__(position, sprite, vector(0))

    def rotate(self, clockwise=True):
        sign = 1 if clockwise else -1
        angle = self.MANEUVERABILITY * sign
        self.direction.rotate_ip(angle)

    def draw(self, surface):
        angle = self.direction.angle_to(super().UP)
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = vector(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)

    def accelerate(self):
        self.velocity += self.direction * self.ACCELERATION

    def shoot(self):
        bullet_velocity = self.direction * self.BULLET_SPEED + self.velocity
        bullet = Bullet(self.position, bullet_velocity)
        self.create_bullet_callback(bullet)