from src.utilities.load_model import GameObject
from src.utilities.load_sprite import load_sprite

class Bullet(GameObject):
    def __init__(self, position, velocity):
        super().__init__(position, load_sprite("laserBullet"), velocity)

    def move(self, surface):
        self.position = self.position + self.velocity