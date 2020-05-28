import pygame
from settings import *
from map import world_map
from math import sin, cos
from numba import njit
from numba.typed import List
from numpy import arange
import numpy as np


@njit()
def get_ray(player_pos, player_angle, world_map, TILE, HALF_FOV, SCALE, HALF_HEIGHT):
	xo, yo = player_pos
	angles = np.arange(player_angle - HALF_FOV, player_angle + HALF_FOV, DELTA_ANGLE)
	angles_sin_a = np.sin(angles)
	angles_cos_a = np.cos(angles)
	depth_fish_eye = np.cos(-angles + player_angle)
	depthes_for_index = np.arange(MAX_DEPTH)
	depthes_for_angles = depthes_for_index.astype(angles_sin_a.dtype).reshape((1, -1))
	yes = (angles_sin_a.reshape((-1, 1)) @ depthes_for_angles + yo) // TILE * TILE
	xes = (angles_cos_a.reshape((-1, 1)) @ depthes_for_angles + xo) // TILE * TILE


	out = List()
	for ray in arange(NUM_RAYS):
		for depth in depthes_for_index:
			x = xes[ray][depth]
			y = yes[ray][depth]
			if (x, y) in world_map:
				depth *= depth_fish_eye[ray]
				proj_height = PROJ_COEFF / depth
				c = 255 / (1 + depth * depth * 0.00005)
				out.append(((c, c, c), (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height)))
				break
	return out




def ray_casting(sc, *args):
	out = get_ray(*args, world_map, TILE, HALF_FOV, SCALE, HALF_HEIGHT)
	tuple(map(lambda x: pygame.draw.rect(sc, *x), out))