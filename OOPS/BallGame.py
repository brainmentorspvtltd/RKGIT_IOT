import pygame, random
pygame.init()

SIZE = WIDTH, HEIGHT = 1200, 700
SCREEN = pygame.display.set_mode(SIZE)

WHITE = 255,255,255
BLACK = 0,0,0

class Ball:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.radius = 50
        self.move_x = random.random()
        self.move_y = random.random()
        self.color = random.randint(0,255),random.randint(0,255),random.randint(0,255)

    def update(self):
        self.x += self.move_x
        self.y += self.move_y

        if self.x > WIDTH - self.radius:
            self.move_x = -random.randint(0, 1)
        elif self.x < self.radius:
            self.move_x = random.randint(0, 1)

        if self.y > HEIGHT - self.radius:
            self.move_y = -random.randint(0, 1)
        elif self.y < self.radius:
            self.move_y = random.randint(0, 1)


# ball_1 = Ball()
# ball_2 = Ball()

num = 5000
balls = []
for i in range(num):
    ballObj = Ball()
    balls.append(ballObj)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    SCREEN.fill(BLACK)

    # pygame.draw.circle(SCREEN, ball_1.color, (ball_1.x, ball_1.y), ball_1.radius)
    # ball_1.update()
    #
    # pygame.draw.circle(SCREEN, ball_2.color, (ball_2.x, ball_2.y), ball_2.radius)
    # ball_2.update()

    for ball in balls:
        pygame.draw.circle(SCREEN, ball.color, (ball.x, ball.y), ball.radius)
        ball.update()


    pygame.display.flip()