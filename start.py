import pygame
import pygame.mixer
from config import *

# Initialize Pygame and the mixer module
pygame.init()
pygame.mixer.init()

# Load the music file
pygame.mixer.music.load("assets/sounds/snake_music.mp3")

# Set the volume of the music
pygame.mixer.music.set_volume(0.5)

# Play the music
pygame.mixer.music.play(-1)  # Loop indefinitely

# Load the image file
image = pygame.image.load("assets/images/snake.jpg")

# Set the dimensions of the start screen window

screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the start screen window
pygame.display.set_caption("Snake Game")

# Create the start screen background
bg_color = (0, 0, 0)  # Black
screen.fill(bg_color)

# Display instructions on how to play the game
font = pygame.font.Font(None, 36)
text = font.render("Use arrow keys to move the snake", True, (255, 255, 255))  # White
text_rect = text.get_rect()
text_rect.center = (screen_width // 2, screen_height // 2)
screen.blit(text, text_rect)

# Create a button to start the game
button_color = (255, 0, 0)  # Red
button_rect = pygame.Rect((screen_width // 2) - 50, (screen_height // 2) + 50, 100, 50)
pygame.draw.rect(screen, button_color, button_rect)

font = pygame.font.Font(None, 24)
text = font.render("Start Game", True, (255, 255, 255))
text_rect = text.get_rect()
text_rect.center = (screen_width // 2, (screen_height // 2) + 75)
screen.blit(text, text_rect)
# Display the image on the start screen
screen.blit(image, (screen_width//2-250 ,screen_height//80))

# Update the start screen
pygame.display.update()

# Run the start screen loop
running = True
while running:
    for event in pygame.event.get():
        # Handle mouse events to detect button clicks
        if event.type == pygame.MOUSEBUTTONDOWN :
            # Get the mouse position
            mouse_pos = pygame.mouse.get_pos()
            # Check if the mouse position is within the button rect
            if button_rect.collidepoint(mouse_pos):
                # Start the game
                running = False
        # Handle quit events
        if event.type == pygame.QUIT:
            running = False
            # Stop the music when the game starts
            pygame.mixer.music.stop()

# Start the game
print("Starting game...")
import game