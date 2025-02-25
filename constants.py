from math import pi

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

TIME_SCORE_MULTIPLYER = 100

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 300
PLAYER_SPEED = 200
PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN = 0.1
PLAYER_SPRINT_TIME = 0.07
PLAYER_SPRINT_MODIFIER = 10
PLAYER_SPRINT_COOLDOWN = 2

SHOT_RADIUS = 5
SCORE_PER_SHOT = 1000
BULLET_ENERGY = 0.5*pi*(SHOT_RADIUS**2)*(PLAYER_SHOOT_SPEED**2)