import pygame
import os
from AssetLoader import AssetLoader

pygame.font.init()

class Renderer():

	main_font = pygame.font.SysFont("comicsans",50)
	lost_font = pygame.font.SysFont("comicsans",60)
	WIDTH = AssetLoader.WIDTH
	HEIGHT = AssetLoader.HEIGHT

	WIN = pygame.display.set_mode((WIDTH, HEIGHT))

	pygame.display.set_caption("Space Shooter Tutorial")
	
	def __init__(self, gameWorld):
		self.gameWorld = gameWorld

	def redraw_window(self):

		self.WIN.blit(AssetLoader.BG, (0,0))

		#draw text
		lives_label = self.main_font.render("Lives: {lives}".format(lives = self.gameWorld.getLives()), 1, (255,255,255))
		level_label = self.main_font.render("Level: {level}".format(level = self.gameWorld.getLevel()), 1, (255,255,255))
		lost_label = self.lost_font.render("You Lost!!!", 1, (255,255,255))

		self.WIN.blit(lives_label, (10,10))
		self.WIN.blit(level_label, (self.WIDTH - level_label.get_width() - 10,10))

		if self.gameWorld.getGameMode() == 1:

			self.gameWorld.getPlayer().draw(self.WIN)
			self.gameWorld.getEnemyManager().drawEnemies(self.WIN)

		if self.gameWorld.getGameMode() == 2:

			self.WIN.blit(lost_label, (self.WIDTH/2 - lost_label.get_width()/2, self.HEIGHT/2 - lost_label.get_height()/2))



		pygame.display.update()
