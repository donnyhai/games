import pygame, sys, button
import game
import texts as t, colors as c
import start_menu
import window_methods as wm
import experimentals

pygame.init()
pygame.display.init()

#Set window and button sizes
window_x_size =  1020
window_y_size = window_x_size * 9 // 16
window_size = (window_x_size, window_y_size)
button_x_size = window_x_size // 6
button_y_size = window_y_size // 6
frame_size = window_x_size // 250
mark_size = window_x_size // 400
first_stone_board_pos = (10,4)

#while-loop timing
clock = pygame.time.Clock()
FPS = 30


#creating showable start_window on display with, set name and set background color
display = pygame.display.set_mode(window_size, 0, 32)
pygame.display.set_caption("Spiel-Menue")
display.fill(c.settings_background_color)


#set a "Einstellungen" Button
settings_x = window_x_size * 5 // 12
settings_y = window_y_size * 7 // 20
settings_button = button.Button(display, "Einstellungen", 25, 
                                 (settings_x, settings_y), (button_x_size, button_y_size),
                                 c.button_color, (0,0,0))

#set a "Spiel Starten" - Button
start_game_x = window_x_size * 5 // 12
start_game_y = window_y_size * 3 // 5
start_game_button = button.Button(display, "Spiel Starten", 25, 
                                 (start_game_x, start_game_y), (button_x_size, button_y_size),
                                 c.button_color, (0,0,0))

#"save" the standard showed image
pygame.display.update()
start_window = display.copy()

#write the settings from above to settings.txt


start_game_mode = True
settings_window_shown = False
marked_hexagons = []
current_player_color = "white"
game_over = False
drag = False
moved = False

#run the window and wait for mouseclicks or quit
while True:
    if not game_over:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
# settings menue            
            elif start_game_mode:
                
                settings_button.draw_button()
                start_game_button.draw_button()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    ####NC: settings_window still has to be implemented functionally
                    if settings_window_shown: 
                        display.blit(start_window, (0,0))
                        settings_window_shown = False                    
                    elif settings_button.pressed(event.pos): 
                        settings_window  = start_menu.settings_window(display, (220,230,220, 128), event.pos, (2 * button_x_size, 1.5 * button_y_size))
                        settings_window.write_settings(settings_window.settings, (0,0,0))
                        settings_window_shown = True
                    ####
                    elif start_game_button.pressed(event.pos):
                        
                        experimentals.go_window()
                        
                        
                        
    pygame.display.update()
    clock.tick(FPS)
    
pygame.quit()
   
    






