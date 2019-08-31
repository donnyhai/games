import pygame, os, hexagon_stone as hs


hive_paths = [os.path.join("hive", "pictures", "ant.png"), os.path.join("hive", "pictures", "bee.png"),
               os.path.join("hive", "pictures", "hopper.png"), os.path.join("hive", "pictures", "spider.png")]

def white_background(surface, window_size):
    s1 = pygame.Surface(window_size)  # the size of rect rect
    s1.fill((255,255,255))           # this fills the entire surface
    surface.blit(s1, (0,0))    # (0,0) are the top-left coordinates
    
def color_background(surface, color, alpha_value, window_size):
    white_background(surface, window_size)
    s = pygame.Surface(window_size)  # the size of your rect
    s.set_alpha(alpha_value)                # alpha level
    s.fill(color)           # this fills the entire surface
    surface.blit(s, (0,0))    # (0,0) are the top-left coordinates
    
def set_ingame_frame(surface):
    surface_width = surface.get_width()
    surface_height = surface.get_height()
    line_width = 10 
    pygame.draw.line(surface, (0,0,0), (int(surface_width*0.1),0),(int(surface_width*0.1), surface_height), line_width  )
    pygame.draw.line(surface, (0,0,0), (int(surface_width*0.9),0),(int(surface_width*0.9), surface_height), line_width  )
    pygame.draw.line(surface, (0,0,0), (0, int(surface_height*0.8)), (int(surface_width*0.1), int(surface_height*0.8)), line_width)
    pygame.draw.line(surface, (0,0,0), (int(surface_width*0.9), int(surface_height*0.8)), (int(surface_width), int(surface_height*0.8)), line_width)
    
#def initialize_insects(surface, player_color):
#    surface_width = surface.get_width()
#    surface_height = surface.get_height()
#    frame_x_size = surface_width*0.1
#    hexa_size = int(frame_x_size*0.5)
#    y_distance = int((surface_height-4*hexa_size*3**(1/2)))
#    ant1 = hs.hexagon_stone(hexa_size, (frame_x_size/3, y_distance ) , surface, "ant", player_color)
#    ant2 = hs.hexagon_stone(hexa_size, (frame_x_size/3, y_distance ) , surface, "ant", player_color)
#    ant3 = hs.hexagon_stone(hexa_size, (frame_x_size/3, y_distance ) , surface, "ant", player_color)
#    hopper1 = hs.hexagon_stone(hexa_size, (frame_x_size/3, 2*y_distance + hexa_size) , surface, "hopper", player_color)
#    hopper2 = hs.hexagon_stone(hexa_size, (frame_x_size/3, 2*y_distance + hexa_size) , surface, "hopper", player_color)
#    hopper3 = hs.hexagon_stone(hexa_size, (frame_x_size/3, 2*y_distance + hexa_size) , surface, "hopper", player_color)
#    spider1 = hs.hexagon_stone(hexa_size, (frame_x_size/3, 3*y_distance + 2*hexa_size) , surface, "spider", player_color)
#    spider2 = hs.hexagon_stone(hexa_size, (frame_x_size/3, 3*y_distance + 2*hexa_size) , surface, "spider", player_color)
#    bee = hs.hexagon_stone(hexa_size, (frame_x_size/3, 4*y_distance + 3*hexa_size) , surface, "bee", player_color)

def draw_insects(surface, color):
    surface_width = surface.get_width()
    surface_height = surface.get_height()*0.8
    frame_x_size = surface_width*0.1
    hexa_size = int(frame_x_size*0.3)
    y_distance = int((surface_height-4*hexa_size*3**(0.5))/5)
    ant = hs.hexagon_stone(hexa_size, surface,(frame_x_size/4, y_distance), "ant", color)
    hopper = hs.hexagon_stone(hexa_size , surface,(frame_x_size/4, 2*y_distance + hexa_size*3**(0.5)), "hopper", color)
    spider = hs.hexagon_stone(hexa_size , surface,(frame_x_size/4, 3*y_distance + 2*hexa_size*3**(0.5)), "spider", color)
    bee = hs.hexagon_stone(hexa_size, surface,(frame_x_size/4, 4*y_distance + 3 * hexa_size*3**(0.5)), "bee", color)
    
    ant.draw_stone((frame_x_size/4, y_distance))
    hopper.draw_stone((frame_x_size/4, 2*y_distance + hexa_size*3**(0.5)))
    spider.draw_stone((frame_x_size/4, 3*y_distance + 2*hexa_size*3**(0.5)))
    bee.draw_stone((frame_x_size/4, 4*y_distance + 3 * hexa_size*3**(0.5)))
    
#try showing an image on screen AFTER pressing left mousekey
#test_image = pygame.image.load(os.path.join("hive", "pictures", "ant.png"))
#test_image = pygame.transform.scale(test_image, (100, 150))
#test_image_position = (test_image.get_width(), test_image.get_height())

    
