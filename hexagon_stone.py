from math import sqrt
import pygame

class Stone:
    def __init__(self, stone_type, number):
        self.type = stone_type
        self.number = number
        self.is_on_board = False
        self.has_bug_on = False
        self.is_mosquito = False
        
    def set_color(self, color):
        self.color = color

class hexagon_stone:
    
    def __init__(self, size, surface, stone = Stone("empty",1), pixel_position = (0,0)):
        #surface and pixel attributes
        self.size = size
        self.surface = surface
        self.pixel_position = pixel_position
        self.points = self.getting_hexa(self.size, pixel_position)
        self.is_drawed = False
        
        #stone and board attributes
        self.stone = stone
        self.board_position = (-1,-1)
        self.is_empty = True
        
    # like always, the postion is the coordinate of the top left corner    
    def set_pixel_pos(self, new_pixel_pos):
        self.pixel_position = new_pixel_pos
        self.points = self.getting_hexa(self.size, new_pixel_pos)
        
    #calculate the six hexagon points with starting point start_vector (point top left) and side size scaling    
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

    def hexa_stone_draw_frame(self, position, color, mark_mode = 0):
        if mark_mode == 0:
            pygame.draw.lines(self.surface, color , True, self.getting_hexa(self.size, position), 2 )
        elif mark_mode > 0:
            pygame.draw.lines(self.surface, color, True, self.getting_hexa(self.size + 2* mark_mode / sqrt(3) - 2,
                                        (int(self.pixel_position[0]- mark_mode / sqrt(3)) + 1, int(self.pixel_position[1]- mark_mode))  ) , int(mark_mode)+1 )
        
    def draw_stone(self, position):
        pygame.draw.polygon(self.surface, self.stone.color , self.getting_hexa(self.size, position))
        
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
    
    #change stone on this hexagon
    def change_stone(self, new_stone):
        self.stone = new_stone
        if new_stone.stone_type == "empty":
            self.is_empty = True
            self.board_position = (-1,-1)
        else:
            self.is_empty = False
        
class get_stones:
    def __init__(self, surface):
        self.surface = surface
        self.hexa_size = int(self.surface.get_width()*0.03)
        self.ant = hexagon_stone(self.hexa_size, self.surface, Stone("ant", 1))
        self.hopper = hexagon_stone(self.hexa_size, self.surface, Stone("hopper", 1))
        self.spider =hexagon_stone(self.hexa_size, self.surface,Stone("spider", 1))
        self.bee = hexagon_stone(self.hexa_size, self.surface, Stone("bee", 1))
        
