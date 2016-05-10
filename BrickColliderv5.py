import pygame, os

#Colours (R, G, B)
GREEN  = (0, 255, 0)
BLUE   = (0, 0, 255)
GOLD   = (201, 137, 16)
SILVER = (168, 168, 168)
AQUA   = (0, 255, 255)
WHITE  = (255, 255, 255)
BLACK  = (0, 0, 0)

#Levels 
LEVEL1 = [
		"BBBBBBBBB",
		"BBBBBBBBB",
		"BBBBBBBBB",
		"BBBBBBBBB"]
		
LEVEL2 = [
		"BBBBBBBBB",
		"BBBBXBBBB",
		"BBBXBXBBB",
		"BBBBXBBBB",
		"BBBBBBBBB"]
		
LEVEL3 = [
		"BBBBBBBBB",
		"BBBBBBBBB",
		"GGGGGGGGG",
		"BBBBBBBBB",
		"BBBBBBBBB"]

class BrickCollider:

	def main(self):
		
		clock = pygame.time.Clock()
		running = True
		lvl = 1 #Starting Level
		
		#Create objects
		ball = Ball()
		paddle = Paddle()
		
		#Create Sprite Groups
		b_group = pygame.sprite.Group()
		p_group = pygame.sprite.Group()
		bl_group = pygame.sprite.Group()
		
		#Add Objects to Sprite Groups
		b_group.add(ball)
		p_group.add(paddle)
		
		#Game Loop
		while running:
			clock.tick(60) #Refresh screen
			screen.fill(GREEN) #Colour Screen
			
			#Create Blocks and add to sprite group
			if not bl_group:
				self.create_level(bl_group, lvl)
				lvl += 1
				ball.set_pos()
		
			#Draw Sprite Groups
			b_group.draw(screen)
			p_group.draw(screen)
			bl_group.draw(screen)
			
			pygame.display.flip() #Update(flip) display
			
			#Move ball(s)
			for balls in b_group:
				balls.move()
				balls.pad_colllide(paddle)
				balls.block_collide(bl_group)
			
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
			#Move Paddle
			key = pygame.key.get_pressed()
			if key[pygame.K_LEFT]:
				paddle.move_left()
			if key[pygame.K_RIGHT]:
				paddle.move_right()
				
	def create_level(self, bl_group, lvl):
		
		#Select LEVEL based on lvl
		if lvl == 1:
			level = LEVEL1
		elif lvl == 2:
			level = LEVEL2
		else:
			level = LEVEL3
		#Start x & y position for blocks
		b_x = 5
		b_y = 55
		#Create blocks and add to group
		for row in level:
			for col in row:
				if col == "B":
					block = Block(b_x, b_y)
					bl_group.add(block)
					b_x += 55 #increment start x for next block
				if col == "X":
					b_x += 55 #increment start x for next block
				if col == "G":
					block = Block(b_x, b_y, GOLD)
					bl_group.add(block)
					b_x += 55 #increment start x for next block
			b_x = 5 #Reset x for next row
			b_y += 45 #increment start y for next row	
	
			
class Ball(pygame.sprite.Sprite):

	def __init__(self):
		super(Ball, self).__init__() #Set Ball as the super class of Sprite
		#Create the Ball image
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
	
	def set_pos(self):
		#Reset Ball position
		self.rect.x = 150 #Start Position for Ball on x-axis
		self.rect.y = 300 #Start Position for Ball on y-axis
		self.dirx = 1 #Movement for ball along x-axis
		self.diry = 1 #Movement for ball along y-axis
		
	def pad_colllide(self, paddle):
		# Ball hits the top of the paddle
		if self.rect.bottom == paddle.rect.top:
			if self.rect.right > paddle.rect.left and self.rect.left < paddle.rect.right:
				self.diry = -self.diry
				
		# Ball hits the bottom of the paddle
		if self.rect.top == paddle.rect.bottom:
			if self.rect.right > paddle.rect.left and self.rect.left < paddle.rect.right:
				self.diry = -self.diry
				
		# Ball hits the sides of the paddle
		if self.rect.bottom > paddle.rect.top and self.rect.top < paddle.rect.bottom:
			if self.rect.right > paddle.rect.left and self.rect.left < paddle.rect.right:
				self.dirx = -self.dirx

	def block_collide(self, sprite_group):
		if pygame.sprite.spritecollide(self, sprite_group, True):
			self.diry =-self.diry
				
class Paddle(pygame.sprite.Sprite):

	def __init__(self):
		super(Paddle, self).__init__() #Set Paddle as the super class of Sprite
		#Create the Paddle image
		self.image = pygame.image.load("paddle.png")
		self.rect = self.image.get_rect()
		self.rect.x = 200 #Start Position for Paddle on x-axis
		self.rect.y = 450 #Start Position for Paddle on y-axis		
	
	def move_left(self):
		if self.rect.left > 0:
			self.rect.x += -3
		
	def move_right(self):
		if self.rect.right < 500:
			self.rect.x += 3

class Block(pygame.sprite.Sprite):
	def __init__(self, b_x, b_y, b_colour = BLUE, b_w = 50, b_h = 20):
		super(Block, self).__init__()
		self.image = pygame.Surface((b_w, b_h))
		self.image.fill(b_colour)
		self.rect = self.image.get_rect()
		self.rect.x = b_x
		self.rect.y = b_y
			
if __name__ == '__main__':
	os.environ["SDL_VIDEO_CENTERED"] = "1" #Sets up for center of OS display
	pygame.init() #Initalise Pygame
	screen = pygame.display.set_mode((500, 600)) #Create a screen for game
	BrickCollider().main() #Create game and run main