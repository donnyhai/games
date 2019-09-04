import pygame, os
from math import sqrt

hive_paths = {"ant": os.path.join("pictures", "ant.png"), "hopper": os.path.join("pictures", "hopper.png"),
              "spider": os.path.join("pictures", "spider.png"), "bee": os.path.join("pictures", "bee.png")}

class Painter:
    def __init__(self, surface):
        self.surface = surface
    
    #fill background with color
    def draw_background(self, color, alpha_value = 255):
#        s = pygame.Surface((self.surface.get_width(), self.surface.get_height()))
#        s.set_alpha(alpha_value)
#        s.fill(color)
#        self.surface.blit(s, (0,0))
        self.surface.fill(color)
    
    #draw the frame of an hexagon in color with respect to mark_mode (mark_mode = 0 is normal thin line) 
    def draw_hexagon_frame(self, hexagon, subsurface, color = (0,0,0), mark_mode = 0):
        if mark_mode == 0:
            pygame.draw.aalines(subsurface, color , True, hexagon.points, 2) 
        elif mark_mode > 0:
            scaling_ratio = hexagon.size + 2 * mark_mode / sqrt(3) - 2
            start_vector = (int(hexagon.pixel_position[0] - mark_mode / sqrt(3)) + 1, 
                            int(hexagon.pixel_position[1] - mark_mode)) 
            points = hexagon.getting_hexa(scaling_ratio, start_vector) 
            pygame.draw.aalines(subsurface, color, True, points, int(mark_mode) + 1)
            hexagon.is_marked = True
    
    #draw hexagon frame and fill it with color
    def fill_hexagon_frame(self, hexagon, color, alpha_value = 1):
        pygame.draw.polygon(self.surface, color, hexagon.points)
        
    #draw set of hexagons with respective color and mark_mode, for example when drawing all possible 
    #hexagons a stone can move to 
    def draw_set_of_hexagon_frames(self, hexagon_list, subsurface, color, mark_mode = 0):
        for hexagon in hexagon_list:
            self.draw_hexagon_frame(hexagon, subsurface, color, mark_mode)
    
    #draw the whole board of hexagons on surface
    def draw_board(self, board, subsurface):
        for row in board.board:
            for hexagon in row:
                self.draw_hexagon_frame(hexagon, subsurface)
    
    #draw hexagon_stone at pixel_position with image according to stone_type
    def draw_insect_hexagon(self, hexagon):
        insect = hexagon.stone.type #type should not be "empty"
        insect_image = pygame.image.load(hive_paths[insect])
        insect_image = pygame.transform.scale(insect_image, (hexagon.size, int(hexagon.size * 3**(0.5))))
        if hexagon.stone.color == "white":
            self.fill_hexagon_frame(hexagon, (255,255,230)) #creme white
        elif hexagon.stone.color == "black":
            self.fill_hexagon_frame(hexagon, (60,60,60)) #creme black
        self.surface.blit(insect_image, hexagon.pixel_position)
    
    #draw standard game frame (left and right side areas with text fields at the bottom and middle board area)
    def draw_ingame_frame(self):
        surface_width = self.surface.get_width()
        surface_height = self.surface.get_height()
        line_width = 10 
        pygame.draw.line(self.surface, (0,0,0), (int(surface_width*0.1),0),(int(surface_width*0.1), surface_height), line_width  )
        pygame.draw.line(self.surface, (0,0,0), (int(surface_width*0.9),0),(int(surface_width*0.9), surface_height), line_width  )
        pygame.draw.line(self.surface, (0,0,0), (0, int(surface_height*0.8)), (int(surface_width*0.1), int(surface_height*0.8)), line_width)
        pygame.draw.line(self.surface, (0,0,0), (int(surface_width*0.9), int(surface_height*0.8)), (int(surface_width), int(surface_height*0.8)), line_width)
    
    #draw a list of hexagons with insect on them (for example for the side stones in the beginning)
    def draw_set_of_insect_stones(self, hstone_list):
        for hstone in hstone_list:
            self.draw_insect_hexagon(hstone)
    
