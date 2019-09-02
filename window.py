import pygame, sys, buttons,  creating_board as cb

pygame.init()
pygame.display.init()

#with open("settings.txt", "r") as f:
#    settings = ""
#    for line in f:
#        settings = settings + line
#     
#settings_split = settings.split()
#
#if settings_split[0] == "resolution" and settings_split[2] == settings_split[3]

#Set window and button sizes
window_x_size =  1920
window_y_size = window_x_size*9//16
window_size = (window_x_size, window_y_size)
button_x_size = window_x_size//6
button_y_size = window_y_size//6


#creating showable start_window on display with, set name and set background color
showed_display = pygame.display.set_mode(window_size,0,32)
#showed_display = pygame.display.set_mode((1920, 1080),pygame.RESIZABLE, 32)
pygame.display.set_caption("Spiel-Menue")
showed_display.fill((100,100,100))


#some colors
white = (255,255,255)
black = (0,0,0)
background_color1 = (255,211,155)
background_color2 = (244,164,96)
background_color3 = (238,197,145)
button_color = (200,200,200)


#set a "Einstellungen" Button
settings_x = window_x_size * 5 // 12
settings_y = window_y_size * 7 // 20
settings_button = buttons.Button(showed_display, button_color, settings_x,settings_y ,
                                         button_x_size,    button_y_size,
                                         0,       "Einstellungen", (0,0,0))

#set a "Spiel Starten" - Button
start_game_x = window_x_size * 5 // 12
start_game_y = window_y_size * 3 // 5
start_game_button = buttons.Button(showed_display, button_color, start_game_x, start_game_y,
                                         button_x_size,    button_y_size,
                                         0,       "Spiel Starten", (0,0,0))

start_window = showed_display.copy()


start_game_mode = True
settings_window_shown = False
first_turn= False

#run the window and wait for mouseclicks or quit
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif start_game_mode == True:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if settings_window_shown == True:
                    pygame.Surface.blit(start_window, (0,0))
#                    showed_display.fill((100,100,100))
#                    settings_button.draw_button(showed_display, button_color, button_x_size, button_y_size, settings_x, settings_y)
#                    settings_button.write_text(showed_display, "Einstellungen", (0,0,0), button_x_size, button_y_size, settings_x, settings_y)
#                    start_game_button.draw_button(showed_display, button_color, button_x_size, button_y_size, start_game_x, start_game_y)
#                    start_game_button.write_text(showed_display, "Spiel Starten", (0,0,0),button_x_size, button_y_size, start_game_x, start_game_y)
                    settings_window_shown = False                    
                elif settings_button.pressed(event.pos) == True:
                    print("Einstellungsmenue wird geöffnet")
                    if settings_window_shown == False:
                        print(type(start_window))
                        pygame.draw.rect(showed_display, (230,230,240), pygame.Rect(event.pos[0], event.pos[1]- button_y_size, button_x_size, button_y_size))
                        settings_window_shown = True
                elif start_game_button.pressed(event.pos) == True:
                    pygame.display.set_caption("Spielbrett")
                    cb.color_background(showed_display, background_color2, 128, window_size)
                    cb.set_ingame_frame(showed_display)
                    cb.create_all_stones(showed_display, (255,255,230), (60,60,60))
                    start_game_mode = False 
                    first_turn = True
    pygame.display.update()
    
    
    