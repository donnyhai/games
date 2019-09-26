# -*- coding: cp1252 -*-
#/usr/bin/env python
#Simon H. Larsen
#Buttons
#Project startet: d. 26. august 2012
import pygame

pygame.init()

class Button:
    def __init__(self, surface, color, x, y, length, height, width, text, text_color):
        self.button = self.draw_button(surface, color, length, height, x, y, width)
        self.button = self.write_text(surface, text, text_color, length, height, x, y)
        self.rect = pygame.Rect(x,y, length, height)

    def write_text(self, surface, text, text_color, length, height, x, y):
        font_size = 2*int(length//len(text))
        myFont = pygame.font.SysFont("Comic Sans MS", font_size)
        myText = myFont.render(text, 1, text_color)
        surface.blit(myText, ((x+length/2) - myText.get_width()/2, (y+height/2) - myText.get_height()/2))
        return surface
    
    

    def draw_button(self, surface, color, length, height, x, y, width = 0):           
        for i in range(1,10):
            s = pygame.Surface((length+(i*2),height+(i*2)))
            s.fill(color)
            alpha = (255/(i+2))
            if alpha <= 0:
                alpha = 1
            s.set_alpha(alpha)
            pygame.draw.rect(s, color, (x-i,y-i,length+i,height+i), width)
            surface.blit(s, (x-i,y-i))
        pygame.draw.rect(surface, color, (x,y,length,height), 0)
        pygame.draw.rect(surface, (190,190,190), (x,y,length,height), 1)  
        return surface

    def pressed(self, position):
        if position[0] > self.rect.topleft[0]:
            if position[1] > self.rect.topleft[1]:
                if position[0] < self.rect.bottomright[0]:
                    if position[1] < self.rect.bottomright[1]:
                        #print ("Some button was pressed!")
                        return True
                    else: return False
                else: return False
            else: return False
        else: return False
