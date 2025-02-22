import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, position):
        super().__init__(position.x, position.y, SHOT_RADIUS)

    def draw(self,screen):
        pygame.draw.circle(screen,color=[255,255,255],center=self.position,radius=self.radius,width=1)

    def update(self,dt):
        self.position += self.velocity*dt