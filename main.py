import pygame
from settings import *
from player import Player
from math import cos, sin
from map import world_map
from ray_casting import ray_casting


pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()

while True:
	for even in pygame.event.get():
		if even.type == pygame.QUIT:
			exit()

	player.movement()
	sc.fill(BLACK)

	ray_casting(sc, player.pos, player.angle)

	pygame.display.update()
	clock.tick(FPS)