import pygame

class hexagon_stone:
    
    def __init__(self, seize, position, surface, stone):
        self.seize = seize
        self.position = position
        self.surface = surface
        self.stone = stone
           
    
    def getting_hexa(scaling_ratio, start_vector):    
        hex_coords = [(0,0), (1,0), (1.5, 3**(1/2)/2), (1, 3**(1/2)), (0,3**(1/2)), (-0.5, 3**(1/2)/2)]
        scaled_coords = []
        for x,y in hex_coords:
            scaled_coords.append([x*scaling_ratio, y*scaling_ratio])
        points = []
        for x,y in scaled_coords:
            points.append([x+start_vector[0], y + start_vector[1]])
            return points

    def hexa_stone_draw(self):
        pygame.draw.lines(self.surface, (100,100,100), True, self.getting_hexa(self.seize, self.position))