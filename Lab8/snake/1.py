import pygame,time,random
from pygame.locals import *
pygame.init()
pygame.mixer.init()
SIZE = 40
BACKGROUND_COLOR = (110, 110, 5)
W,H = 1000,800
surf = pygame.display.set_mode((1000, 800))
class Apple:
    def __init__(self, surf):
        self.surface = surf
        self.image = pygame.image.load("apple.jpg")
        self.x = 120
        self.y = 120

    def draw(self):
        self.surface.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def randompos(self):
        self.x = random.randint(1,24)*SIZE
        self.y = random.randint(1,19)*SIZE

class Snake:
    def __init__(self, surf):
        self.surface = surf
        self.image = pygame.image.load("block.jpg")
        self.direction = 'Salamat'
        self.score = 0
        self.level = 1
        self.length = 1
        self.x = [40]
        self.y = [40]
    
    def render_background(self):
        bg = pygame.image.load('background.jpg')
        self.surface.blit(bg, (0,0))
        pygame.display.flip()

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def show_game_over(self):
        # self.surface.fill(BACKGROUND_COLOR)
        self.render_background()
        font = pygame.font.SysFont('Verdana', 30)
        line1 = font.render(f"Game is over! Your score is {self.score}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        pygame.display.flip()

    def walk(self):
        # update body
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        if self.level == 1:
            if self.direction == "left":
                if self.x[0] < 0:  # when level is 1 and when the snake leaves the area, it exits from the opposite side
                    self.x[0] = W  # self.x[0],self.y[0] - head of the snake
                else:
                    self.x[0]-=SIZE
            if self.direction == "right":
                if self.x[0] > W:
                    self.x[0] = 0
                else:
                    self.x[0]+=SIZE
            if self.direction == "up":
                if self.y[0] < 0:
                    self.y[0] = H
                else:
                    self.y[0]-=SIZE
            if self.direction == "down":
                if self.y[0] > H:
                    self.y[0] = 0
                else:
                    self.y[0]+=SIZE

        if self.level == 2:
            if self.direction == "left":
                if self.x[0] < 0:   # when level is 2 and when snake leaves the area game will be over , self.x[0],self.y[0] - head of the snake
                    self.show_game_over()
                    time.sleep(1)
                    pygame.quit()
                else:
                    self.x[0]-=SIZE
            if self.direction == "right":
                if self.x[0] > W:
                    self.show_game_over()
                    time.sleep(1)
                    pygame.quit()
                else:
                    self.x[0]+=SIZE
            if self.direction == "up":
                if self.y[0] < 0:
                    self.show_game_over()
                    time.sleep(1)
                    pygame.quit()
                else:
                    self.y[0]-=SIZE
            if self.direction == "down":
                if self.y[0] > H:
                    self.show_game_over()
                    time.sleep(1)
                    pygame.quit()
                else:
                    self.y[0]+=SIZE
            
        self.draw()

    def draw(self):
        # self.surface.fill(BACKGROUND_COLOR)
        for i in range(self.length):
            self.surface.blit(self.image, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def increase_score(self):
        self.score+=1

    def increase_level(self):
        self.level+=1
        

class Game:
    def __init__(self,surf):
        pygame.display.set_caption("Snake")
        self.surface = surf
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
        self.cnt = 0
        self.sleep = 0.25
        self.play_background_music()
        

    def play_background_music(self):
        pygame.mixer.music.load('bgmusic.mp3')
        pygame.mixer.music.play(-1)

    # def render_background(self):
    #     bg = pygame.image.load('background.jpg')
    #     self.surface.blit(bg, (0,0))
    #     pygame.display.flip()

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 <  y2 + SIZE:
                return True
        return False

    def play(self):
        self.snake.render_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        self.display_level()
        pygame.display.flip()
        time.sleep(self.sleep)

        if self.snake.score == 4 and self.cnt == 0:
            self.sleep = 0.1
            self.cnt = 1
            self.snake.increase_level()

        # snake eating apple
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.snake.increase_score()
            self.apple.randompos()

        # snake colliding with itself
        for i in range(1, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.snake.show_game_over()
                time.sleep(1)
                pygame.quit()   

    def display_score(self):
        font = pygame.font.SysFont('Verdana',30)
        score = font.render(f"Score: {self.snake.score}",True,(200,200,200))
        self.surface.blit(score,(850,10))

    def display_level(self):
        font = pygame.font.SysFont('Verdana',30)
        level = font.render(f"Level: {self.snake.level}", True, (200,200,200))
        self.surface.blit(level,(20,20))
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                if event.type == QUIT:
                    running = False
            self.play()
            # self.render_background()
    
if __name__ == '__main__':
    game = Game(surf)
    game.run()

