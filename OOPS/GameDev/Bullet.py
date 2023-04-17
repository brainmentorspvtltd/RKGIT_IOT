import pygame, random
pygame.init()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # calling parent class constructor
        super(Bullet, self).__init__()
        self.width = 10
        self.height = 10
        self.image = pygame.Surface((self.width, self.height))
        self.color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.moveY = 4

    def update(self):
        self.rect.y -= self.moveY
