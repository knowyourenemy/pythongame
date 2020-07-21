import pygame
from Ship import Ship
from AssetLoader import AssetLoader

class Player(Ship):

	def __init__(self, x, y, health = 100):
		super().__init__(x, y, health)
		self.ship_img = AssetLoader.YELLOW_SPACE_SHIP
		self.laser_img = AssetLoader.YELLOW_LASER
		self.mask = pygame.mask.from_surface(self.ship_img)
		self.max_health = health
		self.bulletVelocity = -20
		self.coolDown = 15


	def draw(self, window):
		window.blit(self.ship_img, (self.x, self.y))
		if self.bullets != None:

			for bullet in self.bullets:
				bullet.draw(window)

	def getMask(self):
		return self.mask


		