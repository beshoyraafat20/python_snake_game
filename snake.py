import pygame
class Snake:
	def __init__(self, position, body, direction ,speed):
		self.position = position
		self.body = body
		self.direction = direction
		self.speed = speed
		self.ChangedDirection = direction
        
	def move(self):
		# handling key events
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			self.ChangedDirection = 'UP'
		if keys[pygame.K_DOWN]:
			self.ChangedDirection = 'DOWN'
		if keys[pygame.K_LEFT]:
			self.ChangedDirection = 'LEFT'
		if keys[pygame.K_RIGHT]:
			self.ChangedDirection = 'RIGHT'

		# If two keys pressed simultaneously
		# we don't want snake to move into two
		# directions simultaneously
		if self.ChangedDirection == 'UP' and self.direction != 'DOWN':
			self.direction = 'UP'
		if self.ChangedDirection == 'DOWN' and self.direction != 'UP':
			self.direction = 'DOWN'
		if self.ChangedDirection == 'LEFT' and self.direction != 'RIGHT':
			self.direction = 'LEFT'
		if self.ChangedDirection == 'RIGHT' and self.direction != 'LEFT':
			self.direction = 'RIGHT'
  		# Moving the snake 	
		if self.direction == 'UP':
			self.position[1] -= 10
		if self.direction == 'DOWN':
			self.position[1] += 10
		if self.direction == 'LEFT':
			self.position[0] -= 10
		if self.direction == 'RIGHT':
			self.position[0] += 10