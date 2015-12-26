import sys
import pygame
from pygame.locals import QUIT

def setup ():
    pygame.init()
    size = 500
    DISPLAYSURF = pygame.display.set_mode((size,size))
    pygame.display.set_caption('Hello World!')
    while True: # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if '__main__' == __name__:
    setup()
