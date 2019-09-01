import pygame
pygame.init()

class Display:
    def __init__(self, x_size = 200, y_size = 100, caption = "Hello New Window!"):
        self.display = pygame.display
        self.display.set_caption(caption)
        self.x_size = x_size
        self.y_size = y_size
        
dis = Display()
#dis.fill((100,100,100))
dis2 = pygame.display
dis2.fill((100,100,100))