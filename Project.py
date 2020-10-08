#importing pygame module
import pygame, sys
from pygame.locals import *

pygame.init()
running = True
window = pygame.display.set_mode((500, 500))
white = [255,255,255]
pygame.display.set_caption("window")
FPS = 10

class Stickman(pygame.sprite.Sprite):
    def __init__(self):
        super(Stickman, self).__init__()
        self.images =[]
        self.images.append(pygame.image.load('C:/colem/Documents/Test1/stickman.png'))
        self.index = 0
        self.image = self.images[0]
    def update(self):
        self.index += 1
        
        if self.index >= len(self.images()):
            self.index = 0
        self.image = self.images[self.index]

while running == True:
    window.fill(white)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            running = False


#test change 2