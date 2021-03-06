import pygame, os

#Colours (R, G, B)
GREEN = (0, 255, 0)

class BrickCollider:

	def main(self):
		
		clock = pygame.time.Clock()
		running = True
		
		#Create objects
		ball = Ball()
		
		#Create Sprite Groups
		b_group = pygame.sprite.Group()
		
		#Add Objects to Sprite Groups
		b_group.add(ball)
		
		#Game Loop
		while running:
			clock.tick(60) #Refresh screen
			screen.fill(GREEN) #Colour Screen
			
			#Draw Sprite Groups
			b_group.draw(screen)
			
			pygame.display.flip() #Update(flip) display
			
			#Move ball(s)
			for balls in b_group:
				balls.move()
			
			#Check for events 
			for event in pygame.event.get():
				pause = False
				if event.type == pygame.QUIT: #X at top right
					running = False
				if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: #Escape key press
					running = False
				if event.type == pygame.KEYDOWN and event.key == pygame.K_p: #Pause game
					pause = True
				#Paused Game and event
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

class Ball(pygame.sprite.Sprite):

	def __init__(self):
		super(Ball, self).__init__() #Set Ball as the super class of Sprite
		#Create the Ball image
		self.image = pygame.Surface((25, 25))
		self.image = pygame.image.load("ball.png")
		self.rect = self.image.get_rect()
		self.rect.x = 150 #Start Position for Ball on x-axis
		self.rect.y = 300 #Start Position for Ball on y-axis
		self.dirx = 1 #Movement for ball along x-axis
		self.diry = 1 #Movement for ball along y-axis
		
	def move(self):
		#If right or left sides of the Ball touch the sides of the screen
		if self.rect.right >= 500 or self.rect.left <= 0:
			self.dirx = -self.dirx
		#If the bottom or top of Ball touch the bottom or top of screen
		if self.rect.bottom >= 600 or self.rect.top <= 0:
			self.diry = -self.diry
		#Add movement to the current values of rect x and y
		self.rect.x += self.dirx
		self.rect.y += self.diry
		
if __name__ == '__main__':
	os.environ["SDL_VIDEO_CENTERED"] = "1" #Sets up for center of OS display
	pygame.init() #Initalise Pygame
	screen = pygame.display.set_mode((500, 600)) #Create a screen for game
	BrickCollider().main() #Create game and run main