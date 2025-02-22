import pygame
from circleshape import CircleShape
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.space_pressed = False
        self.shooting = False
    
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

        if keys[pygame.K_q]:
            self.rotate(-dt)

        if keys[pygame.K_e]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(-dt)
        
        if keys[pygame.K_s]:
            self.move(dt)

        if keys[pygame.K_d]:
            self.move_horizontal(dt)

        if keys[pygame.K_a]:
            self.move_horizontal(-dt)
        
        # Toggle shooting on/off
        space_pressed_now = keys[pygame.K_SPACE]
        if space_pressed_now and not self.space_was_pressed:
            self.shooting = not self.shooting  # Toggle between True/False
        self.space_was_pressed = space_pressed_now

        # If shooting is enabled, create shots
        if self.shooting:
            self.shoot(dt)
        
    def move(self,dt):
        forward = pygame.Vector2(0, 1)
        self.position += forward * PLAYER_SPEED * dt

    def move_horizontal(self,dt):
        forward = pygame.Vector2(1, 0)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self,dt):
        shot = Shot(self.position)
        shot.velocity = pygame.Vector2(0,1)
        shot.velocity = shot.velocity.rotate(self.rotation)
        shot.velocity *= PLAYER_SHOOT_SPEED