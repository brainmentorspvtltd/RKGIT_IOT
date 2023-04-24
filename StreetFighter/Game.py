import pygame, random
from Constants import *
from PlayerHulk import *
from PlayerThor import *
pygame.init()

# SCREEN = pygame.display.set_mode(SIZE)
SCREEN = pygame.display.set_mode()

sprite_group = pygame.sprite.Group()
hulk = Hulk()
sprite_group.add(hulk)

def main():
    bgImage = pygame.image.load("bg.jpg")

    clock = pygame.time.Clock()
    FPS = 5

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        SCREEN.blit(bgImage, (0, -100))

        sprite_group.draw(SCREEN)
        sprite_group.update()
        pygame.display.flip()
        clock.tick(FPS)

main()