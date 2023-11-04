from GlobalScope import *
import pygame
from pygame.locals import *
pygame.init()

# [DEFAULT VARIABLES]
screen_width: int = 500
screen_height: int = 500
screen_size: tuple = (screen_width, screen_height)

running: bool = True

# Color Library
WHITE: tuple = (255, 255, 255)
BLACK: tuple = (0, 0, 0)
GREY: tuple = (127, 127, 127)
RED: tuple = (255, 0, 0)
BLUE: tuple = (0, 0, 255)
YELLOW: tuple = (255, 255, 0)
GREEN: tuple = (0, 255, 0)

background: tuple = GREY
icon = Texture("icon.gif").get_data()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Pygame Program")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
fps: int = 60

# [YOUR VARIABLES]
rect = Rect(50, 20, 120, 100)

while running:
    # Inner Processing
    clock.tick(fps)
    
    # Process Events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == KEYDOWN:
            pass
    
    # Perform Actions
    

    # Render Graphics
    screen.fill(background)
    
    rect = Rect(50, 20, 120, 100)
    
    pygame.display.flip()

pygame.quit()