import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatables,drawables)
    Asteroid.containers = (asteroids_group,updatables,drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(clock.get_fps())
                return
        screen.fill([0,0,0])
        updatables.update(dt)
        for drawable in drawables:
            drawable.draw(screen)
        for asteroid in asteroids_group:
            if player.check_collision(asteroid):
                print("GAME OVER!")
                return
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()