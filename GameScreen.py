import pygame
from GameRenderer import Renderer
from GameWorld import GameWorld
from AssetLoader import AssetLoader
from InputHandler import InputHandler

def main():

	run = True
	FPS = 60
	clock = pygame.time.Clock()
	AssetLoader.load()
	gameWorld = GameWorld()
	renderer = Renderer(gameWorld)
	inputHandler = InputHandler(gameWorld)
	

	while run:

		clock.tick(FPS)

		inputHandler.update()
		gameWorld.update()
		renderer.redraw_window()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

main()