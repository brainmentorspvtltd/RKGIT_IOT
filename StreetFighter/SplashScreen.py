import pygame, random
from Constants import *
import Game
pygame.init()

SCREEN = pygame.display.set_mode(SIZE)

def main():
    bgImage = pygame.image.load("splash_bg.jpg")
    bgImage = pygame.transform.scale(bgImage, SIZE)
    bgMusic = pygame.mixer.Sound("bg_theme.mp3")
    bgMusic.play(-1)

    clock = pygame.time.Clock()
    FPS = 10

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bgMusic.set_volume(0.5)
                    Game.main()

        SCREEN.blit(bgImage, (0, 0))

        pygame.display.flip()
        clock.tick(FPS)

main()