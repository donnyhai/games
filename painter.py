import pygame, os
from math import sqrt

hive_paths = {"ant": os.path.join("pictures", "ant.png"), "hopper": os.path.join("pictures", "hopper.png"),
              "spider": os.path.join("pictures", "spider.png"), "bee": os.path.join("pictures", "bee.png"),
              "bug": os.path.join("pictures", "beetle.png")}

class Painter:
    
    #fill background with color
    def draw_background(self, surface, color, alpha_value = 255):
        s1 = pygame.Surface((surface.get_width(),surface.get_height()) )
        s1.fill((255,255,255))
        surface.blit(s1, (0,0))
        s = pygame.Surface((surface.get_width(),surface.get_height()) )
        s.set_alpha(alpha_value)
        s.fill(color)
        surface.blit(s, (0,0))
    
    
    #draw full hexagon (shall a frame with mark_mode = 0 also be drawn ?)
    def draw_hexagon(self, hexagon, surface):
        hexagon.is_drawn = True
        hexagon.set_drawn_surface(surface)
        #as the hexagon gets drawn, we can calculate the global pixel pos
        hexagon.calculate_global_pixel_pos()
        
#        #draw the frame aswell:
#        self.draw_hexagon_marking(hexagon, mark_mode = 2) #note that if mark_mode > 0, stone gets marked
#        hexagon.is_marked = False #delete marking
        
        
        if hexagon.type == "empty":
            empty_color = (5,90,3)
            pygame.draw.polygon(surface, empty_color, hexagon.points)
        else:
            if hexagon.color == "white":
                pygame.draw.polygon(surface, (255,255,230), hexagon.points) #creme white
            elif hexagon.color == "black":
                pygame.draw.polygon(surface, (60,60,60), hexagon.points) #creme black
            #blit insect on the polygon
            insect = hexagon.type
            insect_image = pygame.image.load(hive_paths[insect])
            insect_image = pygame.transform.scale(insect_image, (hexagon.size, int(hexagon.size * 3**(0.5))))
            surface.blit(insect_image, hexagon.pixel_pos)
    
    
    #draw a list of full hexagons 
    def draw_set_of_hexagons(self, hstone_list, surface):
        for hstone in hstone_list:
            self.draw_hexagon(hstone, surface)
    
    #draw the whole board of hexagons on surface
    def draw_board(self, board, surface):
        for row in board.board:
            for hexagon in row:
                self.draw_hexagon(hexagon, surface)
                
    def draw_hexagon_frame(self, hexagon, color = (0,0,0), width = 1):
        #scaling_ratio = hexagon.size + 2 * width / sqrt(3) - (width // 2)
        points = hexagon.getting_hexa(hexagon.size, hexagon.pixel_pos)
        pygame.draw.lines(hexagon.drawn_surface, color, True, points, int(width))

    #draw the frame of an hexagon in color with respect to mark_mode (mark_mode = 0 is normal thin line) 
    def draw_hexagon_marking(self, hexagon, color = (0,0,0), mark_mode = 0):
        #if just a marking with mark_mode = 0 is drawn, hexagon shall not be considered as marked, 
        #therefore is_marked = False
        if mark_mode == 0:
            pygame.draw.lines(hexagon.drawn_surface, color , True, hexagon.points, 2)
        elif mark_mode > 0:
            scaling_ratio = hexagon.size + 2 * mark_mode / sqrt(3) - (mark_mode // 2)
            start_vector = (int(hexagon.pixel_pos[0] - mark_mode / sqrt(3)) + (mark_mode // 2), 
                            int(hexagon.pixel_pos[1] - mark_mode) + (mark_mode // 2) ) 
            points = hexagon.getting_hexa(scaling_ratio, start_vector)
            #points[2][0] -= scaling_ratio // 10
            points[3][1] -= scaling_ratio // 20
            points[4][1] -= scaling_ratio // 20
            points[4][0] += scaling_ratio // 30
            points[5][0] += scaling_ratio // 25
            pygame.draw.lines(hexagon.drawn_surface, color, True, points, int(mark_mode) + 1)
            hexagon.is_marked = True
                   
    #draw set of hexagons with respective color and mark_mode, for example when drawing all possible 
    #hexagons a stone can move to 
    def draw_set_of_hexagon_markings(self, hexagon_list, color, mark_mode = 0):
        for hexagon in hexagon_list:
            self.draw_hexagon_marking(hexagon, color, mark_mode)
    
    #draw standard game frame (left and right side areas with text fields at the bottom and middle board area)
    def draw_ingame_frame(self, surface):
        surface_width = surface.get_width()
        surface_height = surface.get_height()
        line_width = surface_width // 250
        pygame.draw.line(surface, (0,0,0), (int(surface_width*0.1 + 0.5 * line_width),0),(int(surface_width*0.1 + 0.5 * line_width), surface_height), line_width)
        pygame.draw.line(surface, (0,0,0), (int(surface_width*0.9),0),(int(surface_width*0.9), surface_height), line_width)
        pygame.draw.line(surface, (0,0,0), (0, int(surface_height*0.8)), (int(surface_width*0.1), int(surface_height*0.8)), line_width)
        pygame.draw.line(surface, (0,0,0), (int(surface_width*0.9), int(surface_height*0.8)), (int(surface_width), int(surface_height*0.8)), line_width)
        
    def write_text(self, surface, text, font_size, color, position):
        myText = pygame.font.SysFont("Arial", font_size).render(text, 1, color)
        surface.blit(myText, position)
    
    def write_start_side_numbers(self, player, surface):
        stone_size = player.stone_size
        text_size = int (1.2 * player.stone_size)
        test_font = pygame.font.SysFont("Arial", text_size)
        (width, height) = test_font.size("0")
        
        self.write_text(surface, str(player.side_stones_numbers["ant"]), text_size, (0,0,0),
                        (int(player.side_stones["ant"].pixel_pos[0] - 13 * stone_size / 18 - width),
                         int(player.side_stones["ant"].pixel_pos[1] + sqrt(3) * 0.5 * stone_size - 0.5 * height)))
        self.write_text(surface, str(player.side_stones_numbers["hopper"]), text_size, (0,0,0),
                        (int(player.side_stones["hopper"].pixel_pos[0] - 13 * stone_size / 18 - width),
                         int(player.side_stones["hopper"].pixel_pos[1] + sqrt(3) * 0.5 * stone_size - 0.5 * height)))
        self.write_text(surface, str(player.side_stones_numbers["spider"]), text_size, (0,0,0),
                        (int(player.side_stones["spider"].pixel_pos[0] - 13 * stone_size / 18 - width),
                         int(player.side_stones["spider"].pixel_pos[1] + sqrt(3) * 0.5 * stone_size - 0.5 * height)))
        self.write_text(surface, str(player.side_stones_numbers["bee"]), text_size, (0,0,0),
                        (int(player.side_stones["bee"].pixel_pos[0] - 13 * stone_size / 18 - width),
                         int(player.side_stones["bee"].pixel_pos[1] + sqrt(3) * 0.5 * stone_size - 0.5 * height)))
        self.write_text(surface, str(player.side_stones_numbers["bug"]), text_size, (0,0,0),
                        (int(player.side_stones["bug"].pixel_pos[0] - 13 * stone_size / 18 - width),
                         int(player.side_stones["bug"].pixel_pos[1] + sqrt(3) * 0.5 * stone_size - 0.5 * height)))
    
    




#nothing    