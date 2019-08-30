import pygame, sys, buttons

pygame.init()
pygame.display.init()

#Set window and button sizes
window_x_size =  1920
window_y_size = int(window_x_size*9/16)
window_size = (window_x_size, window_y_size)
button_x_size = 200
button_y_size = 120


#creating showable  start_window on display with, set name and set background color
showed_display = pygame.display.set_mode(window_size,0,32)
#showed_display = pygame.display.set_mode((1920, 1080),pygame.RESIZABLE, 32)
pygame.display.set_caption("Spiel-Menue")
showed_display.fill((100,100,100))



#initialize class buttons.Button as name Button
Button = buttons.Button()


#try showing an image on screen AFTER pressing left mousekey
test_image = pygame.image.load("ant.png")
test_image = pygame.transform.scale(test_image, (100, 150))
test_image_position = (test_image.get_width(), test_image.get_height())

#colors
white = (255,255,255)
black = (0,0,0)
background_color1 = (255,211,155)
background_color2 = (244,164,96)
background_color3 = (238,197,145)

def white_background(surface):
    s1 = pygame.Surface(window_size)  # the size of your rect
    s1.fill((255,255,255))           # this fills the entire surface
    surface.blit(s1, (0,0))    # (0,0) are the top-left coordinates
    
def color_background(surface, color, alpha_value):
    white_background(surface)
    s = pygame.Surface(window_size)  # the size of your rect
    s.set_alpha(alpha_value)                # alpha level
    s.fill(color)           # this fills the entire surface
    surface.blit(s, (0,0))    # (0,0) are the top-left coordinates

def set_ingame_frame(surface):
    surface_width = surface.get_width()
    surface_height = surface.get_height()
    line_width = 10 
    pygame.draw.line(surface, black, (int(surface_width*0.1),0),(int(surface_width*0.1), surface_height), line_width  )
    pygame.draw.line(surface, black, (int(surface_width*0.9),0),(int(surface_width*0.9), surface_height), line_width  )
    pygame.draw.line(surface, black, (0, int(surface_height*0.8)), (int(surface_width*0.1), int(surface_height*0.8)), line_width)
    pygame.draw.line(surface, black, (int(surface_width*0.9), int(surface_height*0.8)), (int(surface_width), int(surface_height*0.8)), line_width)



#set a centered "Spiel Starten" - Button
start_game_button = Button.create_button(showed_display, (200,200,200),
                                         (pygame.Surface.get_size(showed_display)[0]-button_x_size)*0.5,
                                         (pygame.Surface.get_size(showed_display)[1]-button_y_size)*0.5,
                                         button_x_size,    button_y_size,
                                         0,       "Spiel Starten", (255,255,255))
start_game_mode = True


#run the window and wait for mouseclicks or quit
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif start_game_mode == True:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if Button.pressed(event.pos) == True:
                    Text = "Spiel wird gestartet"
                    print(Text)
                    pygame.display.set_caption("Spielbrett")
                    color_background(showed_display, background_color2, 128)
                    set_ingame_frame(showed_display)
                    start_game_mode = False
                else:
                    print("Spiel wird nicht gestartet")
    pygame.display.update()
    
    
    