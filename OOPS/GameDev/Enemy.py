import pygame, random
from Constants import *
pygame.init()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        # calling parent class constructor
        super(Enemy, self).__init__()
        self.width = 50
        self.height = 50
        self.image = pygame.Surface((self.width, self.height))
        self.color = random.randint(0,255),random.randint(0,255),random.randint(0,255)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.width)
        self.rect.y = random.randint(-HEIGHT, 0)
        self.SPEED = random.random()
        self.moveY = random.randint(1,3)

    def update(self, *args, **kwargs):
        self.rect.y += self.moveY
        if self.rect.y > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - self.width)
            self.rect.y = random.randint(-HEIGHT, 0)
