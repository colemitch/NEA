#importing pygame module
import pygame
from pygame.locals import *

pygame.init()
running = True
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("window")
while running == True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            running = False
        
        

