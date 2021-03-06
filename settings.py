from math import pi, tan


# game setting
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60
TILE = 100

# player settings
player_pos = complex(HALF_WIDTH, HALF_HEIGHT)
player_speed = 2
player_angle = 0

#ray casting settings
FOV = pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 1200
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * tan(HALF_FOV)) # растояние от глаза до проекции
PROJ_COEFF = DIST * TILE
SCALE = WIDTH // NUM_RAYS

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 220)
DARK_GRAY = (110, 110, 110)
PURPLE = (120, 0, 120)