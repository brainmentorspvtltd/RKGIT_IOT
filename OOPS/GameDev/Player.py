import pygame, random
from Constants import *
from Bullet import *
pygame.init()

# inherit Sprite class of pygame
class Player(pygame.sprite.Sprite):
    def __init__(self):
        # calling parent class constructor
        super(Player, self).__init__()
        self.width = 50
        self.height = 50
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH/2 - self.width/2
        self.rect.y = HEIGHT - self.height - 10
        self.SPEED = 6
        self.moveX = 0
        self.playerHealth = 200

    def update(self):
        keyPressed = pygame.key.get_pressed()
        if keyPressed[pygame.K_RIGHT]:
            self.moveX = self.SPEED
        elif keyPressed[pygame.K_LEFT]:
            self.moveX = -self.SPEED
        else:
            self.moveX = 0

        self.rect.x += self.moveX

