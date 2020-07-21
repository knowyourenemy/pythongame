import pygame
from Bullet import Bullet

class Ship():

	def __init__(self, x, y, health=100, velocity=5, bulletVelocity = 20):
		self.x = x
		self.y = y
		self.health = health
		self.velocity = velocity
		self.ship_img = None
		self.laser_img = None
		self.bullets = []
		self.cool_down_counter = 0
		self.coolDown = 30
		self.bulletVelocity = bulletVelocity

	

	def moveLeft(self):
		self.x -= self.velocity

	def moveRight(self):
		self.x += self.velocity

	def moveUp(self):
		self.y -= self.velocity

	def moveDown(self):
		self.y += self.velocity

	def cooldown(self):
		if self.cool_down_counter >= self.coolDown:
			self.cool_down_counter = 0
		elif self.cool_down_counter > 0:
			self.cool_down_counter += 1

	def move_lasers(self):
		self.cooldown()
		if self.bullets != None:
			for bullet in self.bullets:
				bullet.move()
				if bullet.offScreen():
					self.bullets.remove(bullet)

	def shoot(self):
		if self.cool_down_counter == 0 and self.y > 0:
			bullet = Bullet(self.x + self.ship_img.get_width()/2 - self.laser_img.get_width()/2, self.y, self.laser_img, self.bulletVelocity)
			self.bullets.append(bullet)
			self.cool_down_counter = 1
			#print("bullet was shot")


	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def getVelocity(self):
		return self.velocity

	def getWidth(self):
		return self.ship_img.get_width()

	def getHeight(self):
		return self.ship_img.get_height()

	def getHealth(self):
		return self.health

	def getBullets(self):
		return self.bullets

	def setBullets(self, bullets):
		self.bullets = bullets

	def setX(self, x):
		self.x = x

	def setY(self, y):
		self.y = y

	def setVelocity(self, velocity):
		self.velocity = velocity

	def setHealth(self, health):
		self.health = health

