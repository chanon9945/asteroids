import pygame
from constants import *
from circleshape import CircleShape
import random
import math

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.just_born = False
        self.Timer = 0
        self.mass = math.pi*(radius**2)


    def draw(self, screen):
        if self.just_born:
            pygame.draw.circle(screen,color=[0,0,255],center=self.position,radius=self.radius,width=2)
        else:
            pygame.draw.circle(screen,color=[255,255,255],center=self.position,radius=self.radius,width=2)

    def update(self, dt):
        self.position += self.velocity*dt
        if self.Timer > 0:
            self.Timer -= dt
        if self.Timer <= 0:
            self.just_born = False

    def split(self,bullet,energy,dt):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        total_energy = 0.5*self.mass*self.velocity.magnitude()**2 + energy

        split_vector = self.position - bullet.position
        split_vector = split_vector.normalize().rotate(90)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid_1.just_born = True
        asteroid_2 = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid_2.just_born = True
        asteroid_1.velocity = split_vector*asteroid_1.calc_speed(total_energy)
        asteroid_2.velocity = -split_vector*asteroid_2.calc_speed(total_energy)
        asteroid_1.Timer = asteroid_1.radius/asteroid_1.velocity.magnitude()
        asteroid_2.Timer = asteroid_2.radius/asteroid_2.velocity.magnitude()

    def bounce(self,other):
        if not (self.just_born or other.just_born):
            total_energy = 0.9*0.5*(self.mass*(self.velocity.magnitude())**2 + other.mass*(other.velocity.magnitude())**2)
            bounce_vector = self.position - other.position
            bounce_vector = bounce_vector.normalize()
            self.velocity = self.calc_speed(total_energy)*(bounce_vector)
            other.velocity = other.calc_speed(total_energy)*(-bounce_vector)

    def calc_speed(self,energy):
        return math.sqrt((2*energy)/self.mass)


        