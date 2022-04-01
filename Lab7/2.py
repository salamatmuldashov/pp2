import pygame

pygame.init()
W,H = 960,576
pygame.mixer.init()
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("Salamat")

pygame.mixer.music.load('123.mp3')
image = pygame.image.load('1.jpg')
pygame.mixer.music.play(-1)
x = 1

clock = pygame.time.Clock()
running = True


while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        pygame.mixer.music.pause()
    if pressed[pygame.K_p]:
        pygame.mixer.music.unpause()
    if pressed[pygame.K_RIGHT]:
        pygame.mixer.music.load('1234.mp3')
        pygame.mixer.music.play()
        
    if pressed[pygame.K_LEFT]:
        pygame.mixer.music.load('123.mp3')
        pygame.mixer.music.play()
    
    screen.blit(image,(0,0))
    pygame.display.flip()


pygame.quit()

