import random
import pygame
import time
visited = []
stack1 = []
#  12 < cellsize < ∞
cellSize = 30
gridSize = 25

EDGE_LENGHT = cellSize*gridSize
EDGE = round(cellSize/2)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

def is_inbounds(x,y):
    inbounds= True
    if(x < EDGE or y < EDGE or x> EDGE_LENGHT or y > EDGE_LENGHT):
        inbounds = False
    return inbounds

def drawGrid():
    for i in range(1,gridSize):
        pygame.draw.line(screen,WHITE,((i*cellSize)+EDGE,EDGE),((i*cellSize)+EDGE,EDGE_LENGHT+EDGE),round(cellSize*0.04))
        pygame.draw.line(screen,WHITE,(EDGE,(i*cellSize)+EDGE),(EDGE_LENGHT+EDGE,(i*cellSize)+EDGE),round(cellSize*0.04))
#------------Movement---------------------------
def m_North(x,y):
    #                      |inicial: X          Y     | Width       Height     |
    pygame.draw.rect(screen,BLACK,[x+(round(cellSize*0.04)), y+(round(cellSize*0.04))-cellSize, cellSize-(round(cellSize*0.04)), cellSize*2-((round(cellSize*0.04))*2)])
    #pygame.draw.rect(screen,BLACK,[x, y-cellSize, cellSize, cellSize*2])
    pygame.display.update()
def m_South(x,y):
    pygame.draw.rect(screen,BLACK,[x+(round(cellSize*0.04)), y+(round(cellSize*0.04)), cellSize-(round(cellSize*0.04)), (cellSize*2)-((round(cellSize*0.04))*2)])
    #pygame.draw.rect(screen,BLACK,[x, y, cellSize, cellSize*2])
    pygame.display.update()
def m_East(x,y):
    pygame.draw.rect(screen,BLACK,[x+(round(cellSize*0.04)), y+(round(cellSize*0.04)), (cellSize*2)-((round(cellSize*0.04))*2), cellSize-(round(cellSize*0.04))])
    #pygame.draw.rect(screen,BLACK,[x, y, cellSize*2, cellSize])
    pygame.display.update()
def m_West(x,y):
    pygame.draw.rect(screen,BLACK,[x+(round(cellSize*0.04))-cellSize, y+(round(cellSize*0.04)), (cellSize*2)-((round(cellSize*0.04))*2), cellSize-(round(cellSize*0.04))])  
    #pygame.draw.rect(screen,BLACK,[x-cellSize, y, cellSize*2, cellSize]) 
    pygame.display.update()

"""def cellHighlight():
    pygame.draw.rect(screen, )"""
def maze_creator(x,y):
    stack1.append((x,y))
    visited.append((x,y))
    while len(stack1) > 0:
        #time.sleep(1)
        directions = []
        if(is_inbounds(x,y-cellSize) and (x,y-cellSize) not in visited):
            directions.append("N")
        if(is_inbounds(x,y+cellSize) and (x,y+cellSize) not in visited):
            directions.append("S")
        if(is_inbounds(x+cellSize,y) and (x+cellSize,y) not in visited):
            directions.append("E")
        if(is_inbounds(x-cellSize,y) and (x-cellSize,y) not in visited):
            directions.append("W")
        
        if len(directions) > 0:
            random_direction = (random.choice(directions))

            if random_direction == "N":
                m_North(x, y)
                y = y - cellSize
                visited.append((x, y))
                stack1.append((x, y))
            elif random_direction == "S":
                m_South(x, y)
                y = y + cellSize
                visited.append((x, y))
                stack1.append((x, y))
            elif random_direction == "E":
                m_East(x, y)
                x = x + cellSize
                visited.append((x, y))
                stack1.append((x, y))
            elif random_direction == "W":
                m_West(x, y)
                x = x - cellSize
                visited.append((x, y))
                stack1.append((x, y))
        else:
            #time.sleep(1)
            x, y = stack1.pop()

def main():
    global screen
    pygame.init()

    logo = pygame.image.load("laberinth.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
     
    screen = pygame.display.set_mode((EDGE_LENGHT+(EDGE*2),EDGE_LENGHT+(EDGE*2)))
    pygame.draw.rect(screen,WHITE,[EDGE,EDGE,(EDGE_LENGHT+(cellSize*.04)),(EDGE_LENGHT+(cellSize*.04))],3)
    drawGrid()
    maze_creator(EDGE,EDGE)
    pygame.draw.rect(screen,BLACK,[EDGE-10,EDGE+(cellSize*.04),cellSize-(cellSize*.04),cellSize-(cellSize*.04)])
    pygame.draw.rect(screen,BLACK,[EDGE_LENGHT-EDGE/2,EDGE_LENGHT+EDGE-cellSize+(cellSize*.04),cellSize-(cellSize*0.04),cellSize-(cellSize*0.04)])
    running = True

    print(is_inbounds(24,EDGE_LENGHT))
     
    # main loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

if __name__=="__main__":
    main()