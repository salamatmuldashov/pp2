import pygame

pygame.init()
W,H = 1000,800
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("Salamat")
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
x,y = 100,100
R = 25
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y - R > 0:
        y-=20
    if pressed[pygame.K_DOWN] and y + R < H:
        y+=20
    if pressed[pygame.K_LEFT] and x - R > 0:
        x-=20
    if pressed[pygame.K_RIGHT] and x + R < W:
        x+=20

    pygame.draw.circle(screen, RED, (x,y), R)
    pygame.display.flip()

pygame.quit()

