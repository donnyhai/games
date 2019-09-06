import pygame, os, hexagon_stone as hs

class stones:
    def __init__(self, surface):
        self.surface = surface
        self.hexa_size = int(self.surface.get_width()*0.03)
        self.ant = hs.hexagon_stone(self.hexa_size, self.surface, hs.Stone("ant", 1))
        self.hopper = hs.hexagon_stone(self.hexa_size, self.surface, hs.Stone("hopper", 1))
        self.spider = hs.hexagon_stone(self.hexa_size, self.surface, hs.Stone("spider", 1))
        self.bee = hs.hexagon_stone(self.hexa_size, self.surface, hs.Stone("bee", 1))


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
    line_width = surface_width // 200
    pygame.draw.line(surface, (0,0,0), (int(surface_width*0.1),0),(int(surface_width*0.1), surface_height), line_width  )
    pygame.draw.line(surface, (0,0,0), (int(surface_width*0.9),0),(int(surface_width*0.9), surface_height), line_width  )
    pygame.draw.line(surface, (0,0,0), (0, int(surface_height*0.8)), (int(surface_width*0.1), int(surface_height*0.8)), line_width)
    pygame.draw.line(surface, (0,0,0), (int(surface_width*0.9), int(surface_height*0.8)), (int(surface_width), int(surface_height*0.8)), line_width)
    

hive_paths = [os.path.join("pictures", "ant.png"), os.path.join("pictures", "hopper.png"),
               os.path.join("pictures", "spider.png"), os.path.join("pictures", "bee.png")]

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
    
    stones = hs.get_stones(surface)
    
    stones.ant.set_pixel_pos(ant_position)
    stones.hopper.set_pixel_pos(hopper_position)
    stones.spider.set_pixel_pos(spider_position)
    stones.bee.set_pixel_pos(bee_position)
    
    stones.ant.stone.set_color(color)
    stones.hopper.stone.set_color(color)
    stones.spider.stone.set_color(color)
    stones.bee.stone.set_color(color)
       
    #draw the hexagons
    stones.ant.draw_stone(ant_position)
    stones.hopper.draw_stone(hopper_position)
    stones.spider.draw_stone(spider_position)
    stones.bee.draw_stone(bee_position)
    
    return [color, stones]
    
def draw_insects_images(surface, color):
    surface_width = surface.get_width()
    frame_height = surface.get_height()*0.8
    frame_x_size = surface_width*0.1
    hexa_size = int(frame_x_size*0.3)
    y_distance = (frame_height - 4 * hexa_size * 3**(0.5)) // 5
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
    
#draw all insects
def create_all_stones(surface, white_color, black_color):
    white_stones = draw_insects_hexa(surface, white_color)
    draw_insects_images(surface, white_color)
    black_stones = draw_insects_hexa(surface, black_color)
    draw_insects_images(surface, black_color)
    
    return [white_stones, black_stones]
    
#draw number of insects

def write_text(surface, text, text_color, length, height, x, y):
    font_size = 2*int(length//len(text))
    myFont = pygame.font.SysFont("Calibri", font_size)
    myText = myFont.render(text, 1, text_color)
    surface.blit(myText, ((x+length/2) - myText.get_width()/2, (y+height/2) - myText.get_height()/2))
    return surface

def draw_number_text(surface, text_color, text):
    pass





