import pygame, os
from math import sqrt

hive_paths = {"ant": os.path.join("pictures", "ant.png"), "hopper": os.path.join("pictures", "hopper.png"),
              "spider": os.path.join("pictures", "spider.png"), "bee": os.path.join("pictures", "bee.png"),
              "bug": os.path.join("pictures", "beetle.png"), "mosquito": os.path.join("pictures", "mosquito.png"),
              "ladybug": os.path.join("pictures", "ladybug.png")}

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
        
        if hexagon.type == "empty": pygame.draw.polygon(surface, (5,90,3), hexagon.points)
        else:
            if hexagon.color == "white": pygame.draw.polygon(surface, (255,255,230), hexagon.points) #creme white
            elif hexagon.color == "black":  pygame.draw.polygon(surface, (60,60,60), hexagon.points) #creme black
            #blit insect on the polygon
            if hexagon.is_mosquito:  insect = "mosquito"
            else:   insect = hexagon.type
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
        frame_width = 3 * mark_mode // 5
        if frame_width == 0:
            pygame.draw.lines(hexagon.drawn_surface, color , True, hexagon.points, 2)
        elif frame_width > 0:
            scaling_ratio = hexagon.size + frame_width / sqrt(3)
            start_vector = (int(hexagon.pixel_pos[0] - frame_width / (2*sqrt(3))), 
                            int(hexagon.pixel_pos[1] - frame_width) + (frame_width // 2) ) 
            points = hexagon.getting_hexa(scaling_ratio, start_vector)
            #points = hexagon.getting_hexa(scaling_ratio, hexagon.pixel_pos)
            pygame.draw.lines(hexagon.drawn_surface, color, True, points, int(1.5* mark_mode))
            hexagon.is_marked = True
                   
    #draw set of hexagons with respective color and mark_mode, for example when drawing all possible 
    #hexagons a stone can move to 
    def draw_set_of_hexagon_markings(self, hexagon_list, color, mark_mode = 0):
        for hexagon in hexagon_list:
            self.draw_hexagon_marking(hexagon, color, mark_mode)
    
    #draw standard game frame (left and right side areas with text fields at the bottom and middle board area)
    def draw_ingame_frame(self, surface):
        width = surface.get_width()
        height = surface.get_height()
        line_width = width // 250
        pygame.draw.line(surface, (0,0,0), (0.1 * width + 0.5 * line_width, 0), (0.1 * width + 0.5 * line_width, height), line_width)
        pygame.draw.line(surface, (0,0,0), (0.9 * width, 0),(0.9 * width, height), line_width)
        pygame.draw.line(surface, (0,0,0), (0, 0.8 * height), (0.1 * width, 0.8 * height), line_width)
        pygame.draw.line(surface, (0,0,0), (0.9 * width, 0.8 * height), (width, 8.8 * height), line_width)
        
    def write_text(self, surface, text, font_size, color, position):
        myText = pygame.font.SysFont("Arial", font_size).render(text, 1, color)
        surface.blit(myText, position)
        
    def write_box_text(self, surfaces, text, player_color):
        font_size = 0.1 * surfaces["surface_white_text"].get_height()
        color = (0,0,0)
        position = (0.1 * surfaces["surface_white_text"].get_width(), 0.1 * surfaces["surface_white_text"].get_height())
        if player_color == "white":
            surface = surfaces["surface_white_text"]
        else:
            surface = surfaces["surface_black_text"]
        self.write_text(surface, text, font_size, color, position)
    
    def write_start_side_numbers(self, player, surface):
        stone_size = player.stone_size
        text_size = int (1.2 * player.stone_size)
        test_font = pygame.font.SysFont("Arial", text_size)
        (width, height) = test_font.size("0")
        
        for insect in player.side_stones.keys():
            self.write_text(surface, str(player.side_stones_numbers[insect]), text_size, (0,0,0),
                        (int(player.side_stones[insect].pixel_pos[0] - 13 * stone_size / 18 - width),
                         int(player.side_stones[insect].pixel_pos[1] + sqrt(3) * 0.5 * stone_size - 0.5 * height)))
    
    def draw_new_stone_number(self, surfaces, text, insect_type, player, text_color = (0,0,0)):
        stone_size = player.stone_size
        text_size = int(1.2 * stone_size)
        test_font = pygame.font.SysFont("Arial", text_size)
        (width, height) = test_font.size("0")
        
        position =  (player.side_stones[insect_type].pixel_pos[0] - 13 * stone_size / 18 - width,
                     player.side_stones[insect_type].pixel_pos[1] + sqrt(3) * 0.5 * stone_size - 0.5 * height)
        
        rect_subsurface = surfaces["surface_stones"][player.color].subsurface(pygame.Rect(position, (width, height)))
        rect_subsurface.fill(surfaces["surface_stones"][player.color].get_at_mapped((1,1)))
        
        self.write_text(rect_subsurface, str(player.side_stones_numbers[insect_type]),
                                text_size, (0,0,0), (0,0) )


#nothing    