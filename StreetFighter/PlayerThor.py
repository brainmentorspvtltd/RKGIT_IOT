import pygame, random
from Constants import *
from LoadSprite import *
pygame.init()

class Thor(pygame.sprite.Sprite):
    idleFrames = []
    walkingFrames = []
    punchFrames = []
    kickFrames = []

    def __init__(self):
        super(Thor, self).__init__()
        self.sprite = pygame.image.load("thor_flip.png").convert_alpha()
        self.spritesheet = SpriteSheet(self.sprite)
        self.w = 250
        self.h = 300

        self.loadIdle()
        self.loadWalking()

        self.image = pygame.Surface((self.w, self.h))
        self.rect = self.image.get_rect()
        self.ground = HEIGHT
        self.rect.x = WIDTH - 400
        self.rect.y = self.ground - self.h - 60
        self.moveX = False
        self.SPEED = 40
        self.move = 0
        self.index = 0

    def update(self):
        self.showIdle()

    def loadIdle(self):
        self.image = self.spritesheet.getImage(3398, 56, 142, 143)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(3253, 56, 146, 143)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(3104, 56, 150, 143)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(2943, 56, 161, 143)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(2770, 56, 172, 143)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(2604, 56, 168, 143)
        self.idleFrames.append(self.image)

    def loadWalking(self):
        pass

    def showIdle(self):
        if self.index >= len(self.idleFrames):
            self.index = 0
        self.image = self.idleFrames[self.index]
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.index += 1
