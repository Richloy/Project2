import pygame, os

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
screen = pygame.display.set_mode((500, 600))
clock = pygame.time.Clock()
running = True

while running:
	clock.tick(60)
	screen.fill((0, 255, 0))
	pygame.display.flip()
	
	for event in pygame.event.get():
		pause = False
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			running = False
		if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
			pause = True
		while pause:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pause = False
					running = False
				if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
					pause = False
					running = False
				if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
					pause = False
