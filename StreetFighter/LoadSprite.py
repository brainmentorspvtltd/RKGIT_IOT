import pygame
from Constants import *
pygame.init()

class SpriteSheet:
    def __init__(self, file_name):
        pygame.sprite.Sprite.__init__(self)
        self.spritesheet = file_name

    def getImage(self, x, y, w, h):
        image = pygame.Surface((w,h))
        image.blit(self.spritesheet, (0,0), (x,y,w,h))
        image.set_colorkey(BLACK)
        return image