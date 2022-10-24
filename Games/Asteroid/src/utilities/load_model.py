from pygame.math import Vector2 as vector
from src.utilities.load_sprite import wrap_position

class GameObject:
    
    UP = vector(0, -1)

    def __init__(self, position, sprite, velocity):
        self.position = vector(position)
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.velocity = vector(velocity)

    def draw(self, surface):
        blit_position = self.position - vector(self.radius)
        surface.blit(self.sprite, blit_position)

    def move(self, surface):
        self.position = wrap_position(self.position + self.velocity, surface)

    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius