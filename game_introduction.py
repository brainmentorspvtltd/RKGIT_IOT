import pygame
pygame.init()

SIZE = WIDTH, HEIGHT = 1500, 700
SCREEN = pygame.display.set_mode(SIZE)

BLACK = 0,0,0
WHITE = 255,255,255
RED = 255,0,0
BLUE = 0,0,255

SCREEN.fill(RED)

while True:
    pygame.display.flip()