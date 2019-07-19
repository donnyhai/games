import pygame

pygame.init()

class Button():
    def __init__(self, x_pos, y_pos, x_lenght, y_lenght):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_lenght = x_lenght
        self.y_lenght = y_lenght
        
    def draw_button(self, surface, color):
        pygame.draw.rectangle(surface, color, (self.x_pos, self.ypos, self.x_lenght, self.y_lenght), widht = 0 )