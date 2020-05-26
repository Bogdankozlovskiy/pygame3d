from settings import *
import pygame
from math import sin, cos


class Player:
	def __init__(self):
		self.x, self.y = player_pos
		self.angle = player_angle

	@property
	def pos(self):
		return int(self.x), int(self.y)

	def movement(self):
		keys = pygame.key.get_pressed()
		sin_a = sin(self.angle)
		cos_a = cos(self.angle)
		if keys[pygame.K_w]:
			self.x += player_speed * cos_a
			self.y += player_speed * sin_a
		elif keys[pygame.K_s]:
			self.x -= player_speed * cos_a
			self.y -= player_speed * sin_a
		elif keys[pygame.K_a]:
			self.x += player_speed * cos_a
			self.y -= player_speed * sin_a
		elif keys[pygame.K_d]:
			self.x -= player_speed * cos_a
			self.y += player_speed * sin_a
		if keys[pygame.K_LEFT]:
			self.angle -= 0.02
		elif keys[pygame.K_RIGHT]:
			self.angle += 0.02