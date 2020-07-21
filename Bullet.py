import pygame
from AssetLoader import AssetLoader

class Bullet():

	WIDTH = AssetLoader.WIDTH
	HEIGHT = AssetLoader.HEIGHT

	def __init__(self, x, y, img, velocity = 20):
		self.x = x
		self.y = y
		self.img = img
		self.mask = pygame.mask.from_surface(self.img)
		self.velocity = velocity

	def draw(self, window):
		window.blit(self.img, (self.x, self.y))

	def move(self):
		self.y += self.velocity

	def offScreen(self):
		return self.y > self.HEIGHT

	def getMask(self):
		return self.mask

	def getX(self):
		return self.x

	def getY(self):
		return self.y

