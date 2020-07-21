import pygame
from Enemy import Enemy
import random
from AssetLoader import AssetLoader


class EnemyManager():

	WIDTH = AssetLoader.WIDTH
	HEIGHT = AssetLoader.HEIGHT


	def __init__(self):

		self.enemies = []
		self.wave_length = 5
		self.escapedEnemies = 0


	def update(self):
			
		if self.enemies != None:

			for enemy in self.enemies[:]:
				enemy.move()
				enemy.move_lasers()
				enemy.shoot()
				if enemy.getY() + enemy.getHeight() > self.WIDTH:
					self.escapedEnemies += 1
					self.enemies.remove(enemy)



	def nextLevel(self):

		self.wave_length += 5

		for i in range(self.wave_length):
			enemy = Enemy(random.randrange(0, self.WIDTH - 50), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
			self.enemies.append(enemy)
			




	def drawEnemies(self, WIN):

		if self.enemies != None:


			for enemy in self.enemies:
				enemy.draw(WIN)


	def restart(self):

		self.enemies = []
		self.wave_length = 5
		self.escapedEnemies = 0		

	def getLives(self):
		return self.lives

	def getEnemiesLength(self):
		return len(self.enemies)

	def getEscapedEnemies(self):
		return self.escapedEnemies

	def getEnemies(self):
		return self.enemies

	def setEnemies(self, enemies):
		self.enemies = enemies

	def setEscapedEnemies(self, escapedEnemies):
		self.escapedEnemies = escapedEnemies


