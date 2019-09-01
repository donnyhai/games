import pygame, os, hexagon_stone as hs


def white_background(surface, window_size):
    s1 = pygame.Surface(window_size)  # the size of the surface
    s1.fill((255,255,255))           # fill the entire surface
    surface.blit(s1, (0,0))    # (0,0) are the top-left coordinates
    
def color_background(surface, color, alpha_value, window_size):
    white_background(surface, window_size)
    s = pygame.Surface(window_size)
    s.set_alpha(alpha_value)
    s.fill(color)
    surface.blit(s, (0,0))
    
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



hive_paths = [os.path.join("pictures", "ant.png"), os.path.join("pictures", "bee.png"),
               os.path.join("pictures", "hopper.png"), os.path.join("pictures", "spider.png")]

def draw_insects_hexa(surface, color):
    
    #calculating constants relativly to surface size
    surface_width = surface.get_width()
    surface_height = surface.get_height()*0.8
    frame_x_size = surface_width*0.1
    hexa_size = int(frame_x_size*0.3)
    y_distance = int((surface_height-4*hexa_size*3**(0.5))/5)
    right_frame_translate = (surface_width*0.9, 0)
    
    ant_position = (frame_x_size*0.25, y_distance)
    hopper_position = (frame_x_size/4, 2*y_distance + hexa_size*3**(0.5))
    spider_position = (frame_x_size/4, 3*y_distance + 2*hexa_size*3**(0.5))
    bee_position = (frame_x_size/4, 4*y_distance + 3*hexa_size*3**(0.5))
    
    if len(color) >= 4 and (sum(color) - color[3] <= 350):
        ant_position = (ant_position[0] + right_frame_translate[0], ant_position[1] + right_frame_translate[1])
        hopper_position = (hopper_position[0] + right_frame_translate[0], hopper_position[1] + right_frame_translate[1])
        spider_position = (spider_position[0] + right_frame_translate[0], spider_position[1] + right_frame_translate[1])
        bee_position = (bee_position[0] + right_frame_translate[0], bee_position[1] + right_frame_translate[1])
    elif sum(color) <= 350:
        ant_position = (ant_position[0] + right_frame_translate[0], ant_position[1] + right_frame_translate[1])
        hopper_position = (hopper_position[0] + right_frame_translate[0], hopper_position[1] + right_frame_translate[1])
        spider_position = (spider_position[0] + right_frame_translate[0], spider_position[1] + right_frame_translate[1])
        bee_position = (bee_position[0] + right_frame_translate[0], bee_position[1] + right_frame_translate[1])
    
    #create/initialize one stone of each type
    ant = hs.hexagon_stone(hexa_size, surface, ant_position, "ant", color)
    hopper = hs.hexagon_stone(hexa_size , surface,hopper_position, "hopper", color)
    spider = hs.hexagon_stone(hexa_size , surface, spider_position, "spider", color)
    bee = hs.hexagon_stone(hexa_size, surface,bee_position , "bee", color)
    
    #draw the hexagons
    ant.draw_stone(ant_position)
    hopper.draw_stone(hopper_position)
    spider.draw_stone(spider_position)
    bee.draw_stone(bee_position)
    
def draw_insects_images(surface, color):
    surface_width = surface.get_width()
    surface_height = surface.get_height()*0.8
    frame_x_size = surface_width*0.1
    hexa_size = int(frame_x_size*0.3)
    y_distance = int((surface_height-4*hexa_size*3**(0.5))/5)
    right_frame_translate = (surface_width*0.9, 0)
    
    ant_position = (frame_x_size*0.25, y_distance)
    hopper_position = (frame_x_size/4, 2*y_distance + hexa_size*3**(0.5))
    spider_position = (frame_x_size/4, 3*y_distance + 2*hexa_size*3**(0.5))
    bee_position = (frame_x_size/4, 4*y_distance + 3*hexa_size*3**(0.5))
    
    #Translate the positions of the images/hexas if they are black
    if len(color) >= 4 and (sum(color) - color[3] <= 350):
        ant_position = (ant_position[0] + right_frame_translate[0], ant_position[1] + right_frame_translate[1])
        hopper_position = (hopper_position[0] + right_frame_translate[0], hopper_position[1] + right_frame_translate[1])
        spider_position = (spider_position[0] + right_frame_translate[0], spider_position[1] + right_frame_translate[1])
        bee_position = (bee_position[0] + right_frame_translate[0], bee_position[1] + right_frame_translate[1])
    elif sum(color) <= 350:
        ant_position = (ant_position[0] + right_frame_translate[0], ant_position[1] + right_frame_translate[1])
        hopper_position = (hopper_position[0] + right_frame_translate[0], hopper_position[1] + right_frame_translate[1])
        spider_position = (spider_position[0] + right_frame_translate[0], spider_position[1] + right_frame_translate[1])
        bee_position = (bee_position[0] + right_frame_translate[0], bee_position[1] + right_frame_translate[1])
    
    #loading the images
    ant_image = pygame.image.load(hive_paths[0])
    hopper_image = pygame.image.load(hive_paths[1])
    spider_image = pygame.image.load(hive_paths[2])
    bee_image = pygame.image.load(hive_paths[3])
    
    #scale them for fitting in hexagon
    ant_image = pygame.transform.scale(ant_image, (hexa_size, int(hexa_size * 3**(0.5))))
    hopper_image = pygame.transform.scale(hopper_image, (hexa_size, int(hexa_size * 3**(0.5))))
    spider_image = pygame.transform.scale(spider_image, (hexa_size, int(hexa_size * 3**(0.5))))
    bee_image = pygame.transform.scale(bee_image, (hexa_size, int(hexa_size * 3**(0.5))))
   
    #blit them to the screen
    surface.blit(ant_image, ant_position)
    surface.blit(hopper_image, hopper_position)
    surface.blit(spider_image, spider_position)
    surface.blit(bee_image, bee_position)
    

def create_all_stones(surface, white_color, black_color):
    draw_insects_hexa(surface, white_color)
    draw_insects_images(surface, white_color)
    draw_insects_hexa(surface, black_color)
    draw_insects_images(surface, black_color)