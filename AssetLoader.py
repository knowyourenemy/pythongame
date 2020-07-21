import pygame
import os

class AssetLoader():

	RED_SPACE_SHIP = None
	GREEN_SPACE_SHIP = None
	BLUE_SPACE_SHIP = None
	YELLOW_SPACE_SHIP = None
	RED_LASER = None
	GREEN_LASER = None
	BLUE_LASER = None
	YELLOW_LASER = None
	BG = None
	WIDTH = 700
	HEIGHT = 700

	@classmethod
	def load(cls):
		
		# Load images
		cls.RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
		cls.GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
		cls.BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

		# Player player
		cls.YELLOW_SPACE_SHIP = pygame.transform.scale(pygame.image.load(os.path.join("assets", "viennaaa.png")), (80,120))

		# Lasers
		cls.RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
		cls.GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
		cls.BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
		cls.YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

		# Background
		cls.BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (cls.WIDTH, cls.HEIGHT))