import pygame, sys
pygame.init()
pygame.display.init()

#INFORMATION
#Run this file and mix your colors. 
#With dragging the left mouse click you move on the colors of the actual color screen. 
#With dragging the right mouse click you change the red_value by going dragging left or right.
#Note, that by dragging the left mouse click you do not change the red_value.
#You can see the actual chosen color on the left side with the corresponding RGBA value. 

def set_palette(red_value):
    surface.fill((0,0,0))
    #set palette with one color bit constant (here red)
    for i in range(256):
        for j in range(256):
            surface.set_at((i + 220,j + 20), (red_value, i, j))
            
def write_text(surface, text, font_size = 20, color = (0,0,0), position = (28, 255)):
    myText = pygame.font.SysFont("Arial", font_size).render(text, 1, color)
    surface.blit(myText, position)
        
window_size = (496, 296)
surface = pygame.display.set_mode(window_size,0,32)
color_surface = surface.subsurface(pygame.Rect(0, 0, 200, 296))            
set_palette(150)
drag1, drag3 = False, False

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 220 <= event.pos[0] < 476 and 20 <= event.pos[1] < 276:
                if event.button == 1:
                    drag1 = True
                    color_surface.fill(surface.get_at(event.pos))
                    write_text(color_surface, str(surface.get_at(event.pos)))
                
                if event.button == 3:
                    drag3 = True
                    set_palette(event.pos[0] - 220)
                    color_surface.fill(surface.get_at(event.pos))
                    write_text(color_surface, str(surface.get_at(event.pos)))
            
        elif event.type == pygame.MOUSEMOTION and (drag1 or drag3):
            if 220 <= event.pos[0] < 476 and 20 <= event.pos[1] < 276:
                if drag1:
                    color_surface.fill(surface.get_at(event.pos))
                    write_text(color_surface, str(surface.get_at(event.pos)))
                elif drag3:
                    set_palette(event.pos[0] - 220)
                    color_surface.fill(surface.get_at(event.pos))
                    write_text(color_surface, str(surface.get_at(event.pos)))
        
        elif event.type == pygame.MOUSEBUTTONUP and (event.button == 1 or event.button == 3):
            drag1, drag3 = False, False
            if event.pos[0] < 200:  print(color_surface.get_at(event.pos))
                
    pygame.display.update()

