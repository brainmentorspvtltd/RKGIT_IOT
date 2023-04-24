import pygame, random
from LoadSprite import *
from Constants import *
pygame.init()

class Hulk(pygame.sprite.Sprite):

    def __init__(self):
        super(Hulk, self).__init__()
        self.sprite = pygame.image.load("hulk.png")
        spritesheet = SpriteSheet(self.sprite)
        self.w = 300
        self.h = 400
        self.image = spritesheet.getImage(32, 37, 65, 86)
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.rect = self.image.get_rect()
        self.ground = HEIGHT - self.h - 100
        self.rect.x = 200
        self.rect.y = self.ground

