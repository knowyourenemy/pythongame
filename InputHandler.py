import pygame
from GameWorld import GameWorld
from AssetLoader import AssetLoader

class InputHandler():

	WIDTH = AssetLoader.WIDTH
	HEIGHT = AssetLoader.HEIGHT

	def __init__(self, gameWorld):
		self.gameWorld = gameWorld

	def update(self):

		keys = pygame.key.get_pressed()

		if self.gameWorld.getGameMode() == 1:

			player = self.gameWorld.getPlayer()
			velocity = player.getVelocity()

			if keys[pygame.K_a] and player.getX() - velocity > 0: # left
				player.moveLeft()

			if keys[pygame.K_d] and player.getX() + velocity + player.getWidth() < self.WIDTH: # right
				player.moveRight()

			if keys[pygame.K_w] and player.getY() - velocity > 0: # up
				player.moveUp()

			if keys[pygame.K_s] and player.getY() + velocity + player.getHeight() < self.HEIGHT: #down
				player.moveDown()

			if keys[pygame.K_SPACE]:
				player.shoot()

		if self.gameWorld.getGameMode() == 2 :

			if keys[pygame.K_RETURN]:
				self.gameWorld.restart()


