import pygame, sys
pygame.init()
pygame.display.init()

window_size = (200, 100)

surface = pygame.display.set_mode(window_size,0,32)

#actions

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
                
    pygame.display.update()