import pygame

points = [(1,1), (2,1), (1.5, 1+3**(1/2)/2), (2, 1+3**(1/2)), (1,1+3**(1/2)), (0.5, 1+3**(1/2)/2)]

size = (50, 50)
RED = pygame.Color(255, 0, 0) 

polygon = pygame.Surface(size)
pygame.draw.polygon(polygon, RED, points, 10)

polygon_filled = pygame.Surface(size)
pygame.draw.polygon(polygon_filled, RED, points)