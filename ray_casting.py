import pygame
from settings import *
from map import world_map
from math import sin, cos
from numba import njit

@njit()
def get_ray(player_pos, player_angle, world_map, TILE, HALF_FOV, SCALE, HALF_HEIGHT):
	cur_angle = player_angle - HALF_FOV
	xo, yo = player_pos
	out = []
	for ray in range(NUM_RAYS):
		sin_a = sin(cur_angle)
		cos_a = cos(cur_angle)
		for depth in range(1, MAX_DEPTH):
			x = xo + depth * cos_a
			y = yo + depth * sin_a
			if (x // TILE * TILE, y // TILE * TILE) in world_map:
				depth *= cos(player_angle - cur_angle)
				proj_height = PROJ_COEFF / depth
				c = 255 / (1 + depth * depth * 0.00001)
				out.append(((c, c, c), (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height)))
				break
		cur_angle += DELTA_ANGLE
	return out


def ray_casting(sc, *args):
	out = get_ray(*args, world_map, TILE, HALF_FOV, SCALE, HALF_HEIGHT)
	tuple(map(lambda x: pygame.draw.rect(sc, *x), out))