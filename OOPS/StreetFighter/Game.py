import pygame, random
from Constants import *
pygame.init()

SCREEN = pygame.display.set_mode(SIZE)

sprite_group = pygame.sprite.Group()

def main():
    bgImage = pygame.image.load("bg.jpg")

    clock = pygame.time.Clock()
    FPS = 60

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        SCREEN.blit(bgImage, (0, -425))

        sprite_group.draw(SCREEN)
        sprite_group.update()
        pygame.display.flip()
        clock.tick(FPS)

main()