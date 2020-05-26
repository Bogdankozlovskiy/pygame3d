from settings import *
import pygame
from math import sin, cos
from cmath import phase, rect, pi


class Player:
	def __init__(self):
		self.player_pos = player_pos
		self.player_speed = player_speed
		self.angle = player_angle

	@property
	def x(self):
		return int(self.player_pos.real)

	@property
	def y(self):
		return int(self.player_pos.imag)

	@property
	def pos(self):
		return self.x, self.y

	def movement(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			self.player_pos += rect(self.player_speed, self.angle)
		elif keys[pygame.K_s]:
			self.player_pos += rect(self.player_speed, self.angle + pi)
		elif keys[pygame.K_a]:
			self.player_pos += rect(self.player_speed, self.angle - pi / 2)
		elif keys[pygame.K_d]:
			self.player_pos += rect(self.player_speed, self.angle + pi / 2)
		if keys[pygame.K_LEFT]:
			self.angle -= 0.02
		elif keys[pygame.K_RIGHT]:
			self.angle += 0.02