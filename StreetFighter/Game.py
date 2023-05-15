import pygame, random
from Constants import *
from PlayerHulk import *
from PlayerThor import *
from PlayerHealth import *
from pygame.locals import *
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
healthWidth = WIDTH//2 - 100
hulkHealth = Health("Hulk", 10, 10, healthWidth, 50)
thorHealth = Health("Thor", WIDTH - healthWidth - 10, 10, healthWidth, 50)
def drawHealth():
    hulkHealth.showHealth(SCREEN)
    hulkHealth.showName(SCREEN)

    thorHealth.showHealth(SCREEN)
    thorHealth.showName(SCREEN)

def showTimer(time_left):
    font = pygame.font.SysFont(None, 100)
    text = font.render(f"{time_left}", True, RED)
    SCREEN.blit(text, (WIDTH//2 - 40, 10))

def main():
    bgImage = pygame.image.load("bg.jpg")

    clock = pygame.time.Clock()
    FPS = 10

    pygame.time.set_timer(USEREVENT + 1, 1000)
    seconds = 45

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == USEREVENT + 1:
                seconds -= 1

        SCREEN.blit(bgImage, (0, -120))


        if pygame.sprite.groupcollide(hulkSprite, thorSprite, False, False):
            if hulk.isAttacking:
                thor.currentMove = HIT
                thorHealth.rect_2.w += 10
            print("Collision Detection")
            hulk.moveX = False
            hulk.SPEED = 0

        drawHealth()
        showTimer(seconds)
        sprite_group.draw(SCREEN)
        sprite_group.update()
        pygame.display.flip()
        clock.tick(FPS)

# main()