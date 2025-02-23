import pygame
from circleshape import CircleShape
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.Timer = 0
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen,color=[255,255,255],points=self.triangle(),width=2)

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED*dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.Timer > 0:
            self.Timer -= dt

        if keys[pygame.K_q]:
            self.rotate(-dt)

        if keys[pygame.K_e]:
            self.rotate(dt)

        if keys[pygame.K_w] and keys[pygame.K_a]:
            self.rotation = 135
            self.move(dt)
        elif keys[pygame.K_a] and keys[pygame.K_s]:
            self.rotation = 45
            self.move(dt)
        elif keys[pygame.K_s] and keys[pygame.K_d]:
            self.rotation = -45
            self.move(dt)
        elif keys[pygame.K_d] and keys[pygame.K_w]:
            self.rotation = -135
            self.move(dt)
        elif keys[pygame.K_w]:
            self.rotation = 180
            self.move(dt)
        elif keys[pygame.K_a]:
            self.rotation = 90
            self.move(dt)
        elif keys[pygame.K_s]:
            self.rotation = 0
            self.move(dt)
        elif keys[pygame.K_d]:
            self.rotation = -90
            self.move(dt)

        if keys[pygame.K_SPACE]:
            if self.Timer <= 0:
                self.shoot(dt)
                self.Timer = PLAYER_SHOOT_COOLDOWN
        
    def move(self,dt):
        forward = pygame.Vector2(0, 1)
        self.position += forward.rotate(self.rotation) * PLAYER_SPEED * dt

    def shoot(self,dt):
        shot = Shot(self.position)
        shot.velocity = pygame.Vector2(0,1)
        shot.velocity = shot.velocity.rotate(self.rotation)
        shot.velocity *= PLAYER_SHOOT_SPEED