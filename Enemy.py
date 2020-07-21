import pygame
from Ship import Ship
from AssetLoader import AssetLoader

class Enemy(Ship):

	

	def __init__(self, x, y, colour, health = 100):
		super().__init__(x, y, health)
		self.COLOUR_MAP = {
			"red": (AssetLoader.RED_SPACE_SHIP, AssetLoader.RED_LASER),
			"green": (AssetLoader.GREEN_SPACE_SHIP, AssetLoader.GREEN_LASER),
			"blue": (AssetLoader.BLUE_SPACE_SHIP, AssetLoader.BLUE_LASER)
		}
		self.ship_img, self.laser_img = self.COLOUR_MAP[colour]
		self.mask = pygame.mask.from_surface(self.ship_img)
		self.velocity = 10

	def draw(self, window):
		window.blit(self.ship_img, (self.x, self.y))
		for bullet in self.bullets:
			bullet.draw(window)

	def move(self):
		self.y += self.velocity

	def getMask(self):
		return self.mask

