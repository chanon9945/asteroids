import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

try:
    with open("high_score.txt", "r") as file:
        content = file.read().strip()
        high_score = int(content) if content else 0
except (FileNotFoundError, ValueError):
    high_score = 0
    with open("high_score.txt", "w") as file:
        file.write("0")

def main():
    playing = True
    while playing:
        print("Starting Asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")

        pygame.init()
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 30)
        clock = pygame.time.Clock()
        dt = 0
        score = 0
        line_spacing = 50

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
        game_on = True

        while game_on:
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
                    print(f"Your score: {round(score)}")
                    game_on = False
                    break
            for asteroid in asteroids_group:
                for bullet in shots:
                    if bullet.check_collision(asteroid):
                        bullet.kill()
                        asteroid.split(bullet,BULLET_ENERGY,dt)
                        score += SCORE_PER_SHOT
            for asteroid in asteroids_group:
                asteroid_temp = asteroids_group.copy()
                asteroid_temp.remove(asteroid)
                for asteroid_other in asteroid_temp:
                    if asteroid_other.check_collision(asteroid):
                        asteroid_other.bounce(asteroid)
            score_text = font.render(f'Score: {round(score)}', True, (255, 255, 255))  # White colors
            screen.blit(score_text, (10, 10))  # Position in top-left corner
            score += dt*TIME_SCORE_MULTIPLYER
            pygame.display.flip()
            dt = clock.tick(60)/1000
        
        while not game_on:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print(clock.get_fps())
                    return
            pygame.display.flip()
            screen.fill([0,0,0])
            game_over_text = font.render(f"GAME OVER", True, (255, 0, 0))
            if score >= high_score:
                with open("high_score.txt", "w") as file:  # Open file to write
                    file.write(str(round(score)))
                score_game_over_text = font.render(f"NEW HIGH SCORE! = {round(score)}", True, (255, 255, 255))
            else:
                score_game_over_text = font.render(f"SCORE = {round(score)}", True, (255, 255, 255))
            try_again_text = font.render(f"Press ENTER to try again.", True, (0, 255, 0))
            exit_text = font.render(f"Press ESC to exit.", True, (255, 0, 0))
            screen.blit(game_over_text, (600,SCREEN_HEIGHT / 2))
            screen.blit(score_game_over_text, (600,SCREEN_HEIGHT / 2 + line_spacing))
            screen.blit(try_again_text, ((600,SCREEN_HEIGHT / 2 + 2*line_spacing)))
            screen.blit(exit_text, ((600,SCREEN_HEIGHT / 2 + 3*line_spacing)))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                break
            if keys[pygame.K_ESCAPE]:
                playing = False
                break

if __name__ == "__main__":
    main()