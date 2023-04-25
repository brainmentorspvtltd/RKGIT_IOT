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
        self.spritesheet = SpriteSheet(self.sprite)
        self.w = 200
        self.h = 250

        self.loadIdle()
        self.loadWalking()
        self.loadPunch()

        self.image = pygame.Surface((self.w, self.h))
        self.rect = self.image.get_rect()
        self.ground = HEIGHT
        self.rect.x = 300
        self.rect.y = self.ground - self.h - 60
        self.moveX = True
        self.SPEED = 40
        self.move = 0
        self.index = 0


    def update(self):
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_d]:
            self.moveX = True
            self.move = self.SPEED
            self.showWalking()
        elif keypressed[pygame.K_a]:
            self.moveX = True
            self.SPEED = 40
            self.move = -self.SPEED
            self.showWalking()
        elif keypressed[pygame.K_z]:
            self.showPunch()
        else:
            self.move = 0
            self.showIdle()

        if self.moveX:
            self.rect.x += self.move

    def loadIdle(self):
        self.image = self.spritesheet.getImage(32, 37, 65, 86)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(422, 167, 60, 84)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(550, 165, 58, 86)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(678, 181, 57, 72)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(803, 181, 56, 72)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(935, 171, 56, 81)
        self.idleFrames.append(self.image)

    def loadWalking(self):
        self.image = self.spritesheet.getImage(140, 37, 92, 86)
        self.walkingFrames.append(self.image)
        self.image = self.spritesheet.getImage(299, 37, 53, 86)
        self.walkingFrames.append(self.image)
        self.image = self.spritesheet.getImage(421, 37, 55, 86)
        self.walkingFrames.append(self.image)
        self.image = self.spritesheet.getImage(535, 37, 89, 86)
        self.walkingFrames.append(self.image)
        self.image = self.spritesheet.getImage(811, 37, 52, 86)
        self.walkingFrames.append(self.image)
        self.image = self.spritesheet.getImage(935, 37, 55, 84)
        self.walkingFrames.append(self.image)
        self.image = self.spritesheet.getImage(1043, 37, 87, 84)
        self.walkingFrames.append(self.image)

    def loadPunch(self):
        self.image = self.spritesheet.getImage(20, 528, 73, 107)
        self.punchFrames.append(self.image)
        self.image = self.spritesheet.getImage(154, 528, 67, 107)
        self.punchFrames.append(self.image)
        self.image = self.spritesheet.getImage(283, 528, 65, 107)
        self.punchFrames.append(self.image)
        self.image = self.spritesheet.getImage(416, 528, 91, 107)
        self.punchFrames.append(self.image)
        self.image = self.spritesheet.getImage(537, 566, 99, 69)
        self.punchFrames.append(self.image)
        self.image = self.spritesheet.getImage(670, 566, 87, 69)
        self.punchFrames.append(self.image)

    def showIdle(self):
        if self.index >= len(self.idleFrames):
            self.index = 0
        self.image = self.idleFrames[self.index]
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.index += 1

    def showWalking(self):
        if self.index >= len(self.walkingFrames):
            self.index = 0
        self.image = self.walkingFrames[self.index]
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.index += 1

    def showPunch(self):
        if self.index >= len(self.punchFrames):
            self.index = 0
        self.image = self.punchFrames[self.index]
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.index += 1
