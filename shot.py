from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
       
    def draw(self, screen):
        pygame.draw.circle(screen, (140, 43, 41), self.position, self.radius)

    def update(self, dt):
        self.position += (self.velocity * 1.25) * dt