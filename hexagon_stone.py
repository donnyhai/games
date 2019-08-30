from math import sqrt
import pygame


class hexagon_stone:
    
    def __init__(self, size, surface, position, stone, color):
        self.size = size
        self.surface = surface
        self.position = position
        self.stone = stone
        self.color = color
           
    
    def getting_hexa(self, scaling_ratio, start_vector):    
        hex_coords = [(0,0), (1,0), (1.5, 3**(1/2)/2), (1, 3**(1/2)), (0,3**(1/2)), (-0.5, 3**(1/2)/2)]
        scaled_coords = []
        for x,y in hex_coords:
            scaled_coords.append([x*scaling_ratio, y*scaling_ratio])
        points = []
        for x,y in scaled_coords:
            points.append([x+start_vector[0], y + start_vector[1]])
        return points
    
    def hexagon_center(self, hexagon_points):
        return hexagon_points[0]+((hexagon_points[1]-hexagon_points[0])*0.5, (hexagon_points[1]-hexagon_points[0])* 3**(0.5)*0.5)

    def hexa_stone_draw_frame(self, position= self.position):
        pygame.draw.aalines(self.surface, self.color , True, self.getting_hexa(self.size, position), 2)
        
    def draw_stone(self, position = self.position):
        pygame.draw.polygon(self.surface, self.color , self.getting_hexa(self.size, position))
        
    def euclidean_metric(self, vector):
        squared = [x*x for x in vector]
        return sqrt(sum(squared))
    
    def point_in_hexagon(self, hexa_points, coords):
        boundary_vectors = []
        connection_vectors = []
        for i in range(len(hexa_points)):
            boundary_vectors.append((hexa_points[(i+1)%len(hexa_points)][0]-hexa_points[i][0],hexa_points[(i+1)%len(hexa_points)][1]-hexa_points[i][1]))
            connection_vectors.append((coords[0]-hexa_points[i][0], coords[1]-hexa_points[i][1]))
        test = True
        angles = []
        for i in range(len(hexa_points)):
            angles.append((boundary_vectors[i][0]*connection_vectors[i][0]+boundary_vectors[i][1]*connection_vectors[i][1])
                          /(self.euclidean_metric(boundary_vectors[i])*self.euclidean_metric(connection_vectors[i])))
            if angles[i] <= -0.5:
                test = False
        return test
    

