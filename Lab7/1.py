import pygame
import datetime

pygame.init()
image = pygame.image.load('mickey.jpg')
screen = pygame.display.set_mode((1400,1100))
right_hand = pygame.image.load('righthand1.png')
left_hand = pygame.image.load('lefthand1.png')
pygame.display.set_caption('Clock')
clock = pygame.time.Clock()
c = datetime.datetime.now()
seconds = c.second
minutes = c.minute
running =  True


def Rotate(surf,image,topleft,angle):
    rotated_image = pygame.transform.rotate(image,-1*angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    surf.blit(rotated_image,new_rect.topleft)

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.pygame.K_ESCAPE:
            running = False
    c = datetime.datetime.now()
    seconds = c.second
    minutes = c.minute
    angle_1 = (2 * seconds) + 500
    angle_2 = (minutes*6 + ((seconds*6)/ 60)) + 26
    screen.blit(image,(0,0))
    Rotate(screen,left_hand, (680,0), angle_1)
    Rotate(screen,right_hand, (300,300), angle_2)
    pygame.display.flip()
    
pygame.quit()
