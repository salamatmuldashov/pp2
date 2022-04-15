import pygame
from random import randint
pygame.init()
W,H = 800,600
screen = pygame.display.set_mode((W,H))
colors = []
for i in range(20):
    colors.append((randint(0,255), randint(0,255), randint(0,255)))
    
class R_Triangle:
    def __init__(self):
        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0
        

class Paint:
    def __init__(self,screen,colors):
        pygame.display.set_caption("Paint")
        self.surface = screen
        self.surface.fill((255,255,255))
        self.x = 0
        self.y = 0
        self.colors = colors
        self.color = (0,0,0)
        self.position = None
        self.startdraw = False
        self.mode = 1
        self.start_pos = None
        self.end_pos = None
        self.W = 800
        self.H = 600
        self.rad = 30
        self.rtriangle = R_Triangle()

    
   
    def display_colors(self):
        for i, col in enumerate(self.colors):
            pygame.draw.rect(self.surface, col, (20 + (i * 35), 20, 35, 20))
        
    
    def r_triangle(self): 
        self.rtriangle.x1 = [0]
        self.rtriangle.x2 = self.x[0]
        self.r_triangle.y1 = self.y[1]
        self.r_triangle.y2 = self.x[1]
        # x1=[0]                 
        # x2=x[0]                 
        # y1=z[1]
        # y2=x[1]
        pygame.draw.line(self.surface,self.color,self.x,self.y,2)
        pygame.draw.line(self.surface,self.color,(self.r_triangle.x1,self.r_triangle.y1),(self.r_triangle.x1,self.r_triangle.y2),2)
        pygame.draw.line(self.surface,self.color,(self.r_triangle.x1,self.r_triangle.y2),(self.r_triangle.x2,self.r_triangle.y2),2)
    # def drawRhombus(screen, start, end, width, color):
    #     x1 = start[0]
    #     x2 = end[0]
    #     y1 = start[1]
    #     y2 = end[1]
    #     pygame.draw.lines(screen, pygame.Color(color), True, (((x1 + x2) / 2, y1), (x1, (y1 + y2) / 2), ((x1 + x2) / 2, y2), (x2, (y1 + y2) / 2)), width)
     
    def run(self):
        while True:
            self.position = pygame.mouse.get_pos()
            self.display_colors()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.startdraw = True
                    self.start_pos = self.position
                    if self.position[0] > 20 and self.position[0] < 720 and self.position[1] > 20 and self.position[1] < 40:
                        self.color = self.surface.get_at(self.position)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.startdraw = False
                    self.end_pos = self.position
                    self.x = abs(self.start_pos[0] - self.end_pos[0])
                    self.y = abs(self.start_pos[1] - self.end_pos[1])
            
                    if self.mode == 0:   #square
                        self.drawSquare()
                    if self.mode == 1:  #R triangle
                        self.drawRightTriangle()
                    if self.mode == 2:  #equ triangle
                        self.drawETriangle()
                    if self.mode == 3:  #romb
                        self.drawRhombus()
        
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0: 
                        self.mode = 0 
                    if event.key == pygame.K_1:
                        self.mode = 1 
                    if event.key == pygame.K_2:
                        self.mode = 2 
                    if event.key == pygame.K_3:
                        self.mode = 3
            pygame.display.update()
           
    
if __name__ == '__main__':
    paint = Paint(screen,colors)
    paint.run()
    pygame.display.flip()