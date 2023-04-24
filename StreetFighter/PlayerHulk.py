import pygame, random
from LoadSprite import *
from Constants import *
pygame.init()

class Hulk(pygame.sprite.Sprite):
    idleFrames = []
    walkingFrames = []
    punchFrames = []
    kickFrames = []
    def __init__(self):
        super(Hulk, self).__init__()
        self.sprite = pygame.image.load("hulk.png")
        spritesheet = SpriteSheet(self.sprite)
        self.w = 300
        self.h = 400
        self.image = spritesheet.getImage(32, 37, 65, 86)
        self.idleFrames.append(self.image)
        self.image = spritesheet.getImage(422, 167, 60, 84)
        self.idleFrames.append(self.image)
        self.image = spritesheet.getImage(550, 165, 58, 86)
        self.idleFrames.append(self.image)
        self.image = spritesheet.getImage(678, 181, 57, 72)
        self.idleFrames.append(self.image)
        self.image = spritesheet.getImage(803, 181, 56, 72)
        self.idleFrames.append(self.image)
        self.image = spritesheet.getImage(935, 171, 56, 81)
        self.idleFrames.append(self.image)

        self.image = spritesheet.getImage(140, 37, 92, 86)
        self.walkingFrames.append(self.image)
        self.image = spritesheet.getImage(299, 37, 53, 86)
        self.walkingFrames.append(self.image)
        self.image = spritesheet.getImage(421, 37, 55, 86)
        self.walkingFrames.append(self.image)
        self.image = spritesheet.getImage(535, 37, 89, 86)
        self.walkingFrames.append(self.image)
        self.image = spritesheet.getImage(811, 37, 52, 86)
        self.walkingFrames.append(self.image)

        self.rect = self.image.get_rect()
        self.ground = HEIGHT - 200
        self.rect.x = 200
        self.rect.y = self.ground
        self.moveX = 0
        self.index = 0


    def update(self):
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_RIGHT]:
            self.moveX = 1
            self.showWalking()
        elif keypressed[pygame.K_LEFT]:
            self.moveX = -1
            self.showWalking()
        else:
            self.showIdle()

        self.rect.x += self.moveX

    def showIdle(self):
        if self.index == len(self.idleFrames):
            self.index = 0
        self.image = self.idleFrames[self.index]
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.index += 1

    def showWalking(self):
        if self.index == len(self.walkingFrames):
            self.index = 0
        self.image = self.walkingFrames[self.index]
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.index += 1
