import pygame
from settings import *
from map import world_map
from math import sin, cos


def ray_casting(sc, player_pos, player_angle):
	cur_angle = player_angle - HALF_FOV
	xo, yo = player_pos
	for ray in range(NUM_RAYS):
		sin_a = sin(cur_angle)
		cos_a = cos(cur_angle)
		for depth in range(0, MAX_DEPTH, 3):
			x = xo + depth * cos_a
			y = yo + depth * sin_a
			pygame.draw.line(sc, DARK_GRAY, player_pos, (x, y))
			if (x // TILE * TILE, y // TILE * TILE) in world_map:
				break
		cur_angle += DELTA_ANGLE