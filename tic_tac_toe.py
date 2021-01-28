import pygame
import sys
from pygame.locals import *



pygame.init()


surface = pygame.display.set_mode((300,300))
chanceNo=0
color = (255,255,255)
red = (255,0,0)
pygame.display.set_caption('TIC TAC TOE')
checkPlace={}


def draw_line():
        pygame.draw.line(surface, color, (0, 100), (300, 100), 1)
        pygame.draw.line(surface, color, (0, 200), (300, 200), 1)
        pygame.draw.line(surface, color, (100, 0), (100, 300), 1)
        pygame.draw.line(surface, color, (200, 0), (200, 300), 1)

font = pygame.font.SysFont(None,150)
endFont = pygame.font.SysFont(None,50)

def xory(msg,color,x,y): # this function is for alligining the x and o in the board

        X = (x*100)+50
        Y = (y*100)+50
        text = font.render(msg,True,color)
        textrect= text.get_rect()
        textrect.center=(X,Y)
        surface.blit(text,textrect)

def OnClick(pos):
        global checkPlace
        global color
        global chanceNo

        x,y = pos
        X =x // 100
        Y =y // 100
        if checkPlace.get((X, Y), True) == True:

                chanceNo += 1
                if chanceNo % 2 == 0:
                        checkPlace[(X, Y)] = "X"
                        xory('X',color,X,Y)
                else:
                        checkPlace[(X, Y)] = "O"
                        xory('O',color,X,Y)
                pygame.display.update()
        for i in range (3):
               if ((checkPlace.get((i,0),False) == checkPlace.get((i,1),False)) and (checkPlace.get((i,1),False) == checkPlace.get((i,2),False))):
                        if checkPlace.get((i,0),False) != False:
                                surface.fill(red)
                                text = endFont.render("GAME OVER", True, color)
                                textrect = text.get_rect()
                                textrect.center = (150,150)
                                surface.blit(text, textrect)
                                pygame.display.update()


        for i in range (3):
               if ((checkPlace.get((0,i),False) == checkPlace.get((1,i),False)) and (checkPlace.get((1,i),False) == checkPlace.get((2,i),False))):
                        if checkPlace.get((0,i),False) != False:
                                surface.fill(red)
                                text = endFont.render("GAME OVER", True, color)
                                textrect = text.get_rect()
                                textrect.center = (150, 150)
                                surface.blit(text, textrect)
                                pygame.display.update()
draw_line()




pygame.display.update()

while True:
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                        MousePosition = pygame.mouse.get_pos()
                        OnClick(MousePosition)


