import pygame, random
from Constants import *
from PlayerHulk import *
from PlayerThor import *
pygame.init()

SCREEN = pygame.display.set_mode(SIZE)
# SCREEN = pygame.display.set_mode()

sprite_group = pygame.sprite.Group()
hulk = Hulk()
sprite_group.add(hulk)

thor = Thor()
sprite_group.add(thor)

hulkSprite = pygame.sprite.Group()
hulkSprite.add(hulk)

thorSprite = pygame.sprite.Group()
thorSprite.add(thor)

def main():
    bgImage = pygame.image.load("bg.jpg")

    clock = pygame.time.Clock()
    FPS = 10

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        SCREEN.blit(bgImage, (0, -120))

        if pygame.sprite.groupcollide(hulkSprite, thorSprite, False, False):
            if hulk.isAttacking:
                thor.currentMove = HIT
            print("Collision Detection")
            hulk.moveX = False
            hulk.SPEED = 0

        sprite_group.draw(SCREEN)
        sprite_group.update()
        pygame.display.flip()
        clock.tick(FPS)

# main()