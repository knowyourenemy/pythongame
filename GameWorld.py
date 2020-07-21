import pygame
import os
import time
import random
from Player import Player
from EnemyManager import EnemyManager


class GameWorld():
	

	def __init__(self):
		self.player = Player(300,400)
		self.enemyManager = EnemyManager()
		self.level = 0
		self.lives = 500
		self.gameMode = 1

	def collide(self, obj1, obj2):
		offset_x = obj2.getX() - obj1.getX()
		offset_y = obj2.getY() - obj1.getY()
		return obj1.getMask().overlap(obj2.getMask(), (int(offset_x), int(offset_y))) != None

	def update(self):

		if self.gameMode == 1:

			self.player.move_lasers()

			self.enemyManager.update()

			if self.enemyManager.getEnemiesLength() == 0:
				self.level += 1
				self.enemyManager.nextLevel()

			if self.enemyManager.getEscapedEnemies() > 0:
				self.lives -= self.enemyManager.getEscapedEnemies()
				self.enemyManager.setEscapedEnemies(0)

			#collision between player bullet and enemy
			enemies = self.enemyManager.getEnemies()
			playerBullets = self.player.getBullets()


			for enemy in enemies:

				enemyBullets = enemy.getBullets()

				for bullet in enemyBullets:
					if self.collide(bullet, self.player):
						enemyBullets.remove(bullet)
						enemy.setBullets(enemyBullets)
						self.player.setHealth(self.player.getHealth() - 10)


					

				for bullet in playerBullets:

					if self.collide(bullet, enemy):
						playerBullets.remove(bullet)
						enemies.remove(enemy)
						self.player.setBullets(playerBullets)
						self.enemyManager.setEnemies(enemies)


				if self.collide(enemy, self.player):
					enemies.remove(enemy)
					self.player.setHealth(self.player.getHealth() - 10)


			if self.lives == 0 or self.player.getHealth() == 0:
				self.gameMode = 2

		if self.gameMode == 2:

			next


	def restart(self):
		self.gameMode = 1
		self.enemyManager.restart()
		self.level = 0
		self.lives = 5
		
	

	def getLevel(self):
		return self.level

	def getLives(self):
		return self.lives

	def getPlayer(self):
		return self.player

	def getEnemyManager(self):
		return self.enemyManager

	def getGameMode(self):
		return self.gameMode

	def setGameMode(self, gameMode):
		self.gameMode = gameMode

					

