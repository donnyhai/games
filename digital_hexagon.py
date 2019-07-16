
def getting_hexa(scaling_ratio, start_vector):    
    hex_coords = [(0,0), (1,0), (1.5, 3**(1/2)/2), (1, 3**(1/2)), (0,3**(1/2)), (-0.5, 3**(1/2)/2)]
    scaled_coords = []
    for x,y in hex_coords:
        scaled_coords.append([x*scaling_ratio, y*scaling_ratio])
    points = []
    for x,y in scaled_coords:
        points.append([x+start_vector[0], y + start_vector[1]])
    return points


        
import pygame, sys

pygame.init()

showed_display = pygame.display.set_mode((750, 750), 0, 32)
pygame.display.set_caption('WindowName')
showed_display.fill((255,255,255))
pygame.draw.lines(showed_display, (100,100,100), True,  getting_hexa(50, (20,20)))
pygame.draw.lines(showed_display, (100,100,100), True,  getting_hexa(80, (200,200)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()