import pygame,time,random
pygame.init()
pygame.mixer.init()
n = 10
FPS = 60
clock = pygame.time.Clock()
W,H = 400,600
SPEED = 7
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
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, W - 40), 0)
    
class Money(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('1.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(150,W-20),random.randint(150,H-20))

    def update(self):
        self.rect.center = (random.randint(150,W-20),random.randint(150,H-20))
        
            

class Money2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('2.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(150,W-20),random.randint(150,H-20))
    
    def update(self):
        self.rect.center = (random.randint(150,W-20),random.randint(150,H-20))
        



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
C2 = Money2()
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
coins2 = pygame.sprite.Group()
coins2.add(C2)
allcoins = pygame.sprite.Group()
allcoins.add(C1)
allcoins.add(C2)
allsprites = pygame.sprite.Group()
allsprites.add(P1)
allsprites.add(E1)
  
# INC_SPEED = pygame.USEREVENT + 1
# pygame.time.set_timer(INC_SPEED, 1000)
cnt = 0
while True:
    for event in pygame.event.get():
        # if event.type == INC_SPEED:
        #     SPEED += 0.1     
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()

    if SCORE >= n and cnt == 0:
        SPEED+=3
        cnt+=1

    SURF.blit(bg,(0,0))
    scores = font_1.render(str(SCORE), True, (0,0,0))
    SURF.blit(scores,(10,10))
    spd = font_1.render(str(SPEED),True,(255,0,0))
    SURF.blit(spd,(300,10))
    for entity in allsprites:
        SURF.blit(entity.image, entity.rect)
        entity.move()
    for coin in allcoins:
        SURF.blit(coin.image,coin.rect)
        
    

    if pygame.sprite.spritecollideany(P1,enemies):
        pygame.mixer.music.stop()
        SURF.fill((255,0,0))
        SURF.blit(go,(30,250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
   

    if pygame.sprite.spritecollideany(P1,coins):
        SCORE+=1
        pygame.display.update()
        C1.update()

    if pygame.sprite.spritecollideany(P1,coins2):
        SCORE+=3
        pygame.display.update()
        C2.update()
         

    pygame.display.update()
    clock.tick(FPS)
    

    