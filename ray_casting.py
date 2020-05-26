import pygame
from settings import *
from map import world_map
from math import sin, cos
from numba import njit

def ray_casting(sc, player_pos, player_angle):
	cur_angle = player_angle - HALF_FOV
	xo, yo = player_pos
	for ray in range(NUM_RAYS):
		sin_a = sin(cur_angle)
		cos_a = cos(cur_angle)
		for depth in range(1, MAX_DEPTH):
			x = xo + depth * cos_a
			y = yo + depth * sin_a
			# pygame.draw.line(sc, DARK_GRAY, player_pos, (x, y))
			if (x // TILE * TILE, y // TILE * TILE) in world_map:
				depth *= cos(player_angle - cur_angle)
				proj_height = PROJ_COEFF / depth
				c = 255 / (1 + depth * depth * 0.00001)
				pygame.draw.rect(sc, (c, c, c), (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
				break
		cur_angle += DELTA_ANGLE