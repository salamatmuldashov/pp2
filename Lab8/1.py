from cProfile import run
import pygame,time,random,sys
pygame.init()
pygame.mixer.init()
FPS = 60
clock = pygame.time.Clock()
W,H = 400,600
SPEED = 5
SCORE = 0
SURF = pygame.display.set_mode((W,H))
bg=pygame.image.load('AnimatedStreet.png')
music = pygame.mixer.music.load('1.mp3')
pygame.mixer.music.play(-1)
pygame.display.set_caption("Racer")
font = pygame.font.SysFont("Verdana", 60)
font_1 = pygame.font.SysFont("Verdana", 20)
go = font.render("Game Over", True, (0,0,0))

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,W-40),0) 
 
      def move(self):
        self.rect.move_ip(0,5)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, W - 40), 0)
    
class Money(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('2.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,W-40),0)

    def move(self):
        global SCORE
        self.rect.move_ip(0,3)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center(random.randint(40,W-40),0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
 
    def move(self):
        pressed = pygame.key.get_pressed()
        if self.rect.top > 0:
            if pressed[pygame.K_UP]:
                self.rect.move_ip(0,-6)
        if self.rect.bottom < H:
            if pressed[pygame.K_DOWN]:
                self.rect.move_ip(0,6)
        if self.rect.left > 0:
            if pressed[pygame.K_LEFT]:
                self.rect.move_ip(-6, 0)
        if self.rect.right < W:        
            if pressed[pygame.K_RIGHT]:
                self.rect.move_ip(6, 0)
         
P1 = Player()
E1 = Enemy()
C1 = Money()
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
allsprites = pygame.sprite.Group()
allsprites.add(P1)
allsprites.add(E1)
allsprites.add(C1)

# INC_SPEED = pygame.USEREVENT + 1
# pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        # if event.type == INC_SPEED:
        #     SPEED += 0.1     
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
    SURF.blit(bg,(0,0))
    scores = font_1.render(str(SCORE), True, (0,0,0))
    SURF.blit(scores,(10,10))
    for entity in allsprites:
        SURF.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P1,coins):
        SCORE+=1
        pygame.display.update()
        C1.__init__()
         
    if pygame.sprite.spritecollideany(P1,enemies):
        pygame.mixer.music.stop()
        SURF.fill((255,0,0))
        SURF.blit(go,(30,250))
        pygame.display.update()
        for entity in allsprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()

    pygame.display.update()
    clock.tick(FPS)
    

    