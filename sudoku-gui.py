import pygame,time
from newfile import Disp
pygame.init()
gameDisplay=pygame.display.set_mode((800,700))
pygame.display.set_caption('SUDOKU')
clock= pygame.time.Clock()
color=(255,255,255)
black=(0,0,0)
red =(255,0,0)
gameDisplay.fill(color)
x=50
y=550
for i in range(10):
    c=1
    if i==0 or i%3==0:
        c=2
    pygame.draw.line(gameDisplay,black, (x,x+(i*50)), (y-50,x+(i*50)),c)
    pygame.draw.line(gameDisplay,black, (x+(i*50),x), (x+(i*50),y-50), c)
pygame.draw.rect(gameDisplay, red,(50,560,60,30), 1)
font = pygame.font.Font('freesansbold.ttf', 15)  
text = font.render('Submit', True, black, color) 
textRect = text.get_rect()  
textRect.center = (80,575)
gameDisplay.blit(text, textRect)
crashed = False
disp =[[5,7,9,'','',2,'','',''],
              [8,2,'','','',3,'','',''],
              ['',6,3,'','','','','',8],
              ['','','',1,5,4,9,'',''],
              ['','',7,'','','',4,'',''],
              ['','',1,7,8,6,'','',''],
              [2,'','','','','',8,9,''],
              ['','','',4,'','','',1,5],
              ['','','',5,'','',2,4,3]
              ]
def board(display):
    for i in range(9):
        for j in range(9):
            font = pygame.font.Font('freesansbold.ttf', 32) 
            text = font.render(str(display[i][j]), True, red, color) 
            textRect = text.get_rect()  
            textRect.center = (75+(j*50),75+(i*50))
            gameDisplay.blit(text, textRect)
board(disp)
while not crashed:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            continue
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 50<=mouse[0]<=110 and 560<=mouse[1]<=590:
                display = Disp.design(disp)
                board(display)
        pygame.display.update()
pygame.quit()
