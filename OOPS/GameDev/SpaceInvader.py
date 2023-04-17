import pygame, random
from Constants import *
from Player import *
from Enemy import *
pygame.init()

SCREEN = pygame.display.set_mode(SIZE)

sprite_group = pygame.sprite.Group()
player = Player()
sprite_group.add(player)

playerGroup = pygame.sprite.Group()
playerGroup.add(player)

enemyGroup = pygame.sprite.Group()
num_enemy = 20
for i in range(num_enemy):
    enemy = Enemy()
    sprite_group.add(enemy)
    enemyGroup.add(enemy)

bulletGroup = pygame.sprite.Group()

def fireBullet():
    bullet = Bullet(player.rect.x + player.width // 2, player.rect.y)
    sprite_group.add(bullet)
    bulletGroup.add(bullet)


def showHealth():
    playerHealth = player.playerHealth
    pygame.draw.rect(SCREEN, WHITE, (10, 10, playerHealth, 30))
    font = pygame.font.SysFont(None, 30)
    text = font.render("Health : {}".format(playerHealth), True, GREEN)
    SCREEN.blit(text, (240, 20))

def main():
    clock = pygame.time.Clock()
    FPS = 60

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    fireBullet()

        pygame.sprite.groupcollide(enemyGroup, bulletGroup, True, True)
        hit = pygame.sprite.groupcollide(enemyGroup, playerGroup, True, False)
        if hit:
            player.playerHealth -= 20

        SCREEN.fill(BLACK)

        showHealth()
        sprite_group.draw(SCREEN)
        sprite_group.update()
        pygame.display.flip()
        clock.tick(FPS)

main()