import pygame
from Constants import *

class Health:
    def __init__(self, p_name, x, y, w, h):
        self.image = pygame.Surface((w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_color = GREEN
        self.player_name = p_name
        self.rect_2 = self.image.get_rect()
        self.rect_2_color = RED
        self.rect_2.w = 0
        self.rect_2.x = x
        self.rect_2.y = y

    def showHealth(self, SCREEN):
        pygame.draw.rect(SCREEN, self.rect_color, self.rect)
        pygame.draw.rect(SCREEN, self.rect_2_color, self.rect_2)

    def showName(self, SCREEN):
        font = pygame.font.SysFont(None, 80)
        text = font.render(self.player_name, True, BLACK)
        SCREEN.blit(text, (self.rect.x, 70))