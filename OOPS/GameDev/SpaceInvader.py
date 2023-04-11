import pygame, random
pygame.init()

SIZE = WIDTH, HEIGHT = 1200, 700
SCREEN = pygame.display.set_mode(SIZE)

WHITE = 255,255,255
BLACK = 0,0,0
RED = 255,0,0


# inherit Sprite class of pygame
class Player(pygame.sprite.Sprite):
    def __init__(self):
        # calling parent class constructor
        super(Player, self).__init__()
        self.width = 50
        self.height = 50
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH/2 - self.width/2
        self.rect.y = HEIGHT - self.height - 10
        self.SPEED = 1
        self.moveX = 0

    def update(self):
        keyPressed = pygame.key.get_pressed()
        if keyPressed[pygame.K_RIGHT]:
            self.moveX = self.SPEED
        elif keyPressed[pygame.K_LEFT]:
            self.moveX = -self.SPEED
        else:
            self.moveX = 0

        self.rect.x += self.moveX

class Enemy:
    def __init__(self):
        pass


class Bullet:
    def __init__(self):
        pass


sprite_group = pygame.sprite.Group()
player = Player()
sprite_group.add(player)

playerGroup = pygame.sprite.Group()
playerGroup.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    SCREEN.fill(BLACK)
    sprite_group.draw(SCREEN)
    sprite_group.update()
    pygame.display.flip()