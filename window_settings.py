import pygame, sys, buttons
import game
import start_menu

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
display.fill((100,100,100))


#some colors
white = (255,255,255)
black = (0,0,0)
background_color1 = (255,211,155)
background_color2 = (244,164,96)
background_color3 = (238,197,145)
button_color = (200,200,200)
creme_white = (255,255,230)
creme_black = (60,60,60)

#set a "Einstellungen" Button
settings_x = window_x_size * 5 // 12
settings_y = window_y_size * 7 // 20
settings_button = buttons.Button(display, button_color, settings_x,settings_y ,
                                         button_x_size,    button_y_size,
                                         0,       "Einstellungen", (0,0,0))

#set a "Spiel Starten" - Button
start_game_x = window_x_size * 5 // 12
start_game_y = window_y_size * 3 // 5
start_game_button = buttons.Button(display, button_color, start_game_x, start_game_y,
                                         button_x_size,    button_y_size,
                                         0,       "Spiel Starten", (0,0,0))

#"save" the standard showed image
pygame.display.update()
start_window = display.copy()

#write the settings from above to settings.txt


start_game_mode = True
settings_window_shown = False
marked_hexagons = []
current_player_color = "white"
game_over = False

#create game object here firstly not encounter problems
game = game.HvsH_Game(display)

full_surface = display
game_surface = full_surface.subsurface(pygame.Rect(window_x_size * 0.1 , 0, window_x_size * 0.8 , window_y_size))
white_surface = full_surface.subsurface(pygame.Rect(0, 0, window_x_size // 10, (window_y_size * 4) // 5))
black_surface = full_surface.subsurface(pygame.Rect((window_x_size * 9) // 10, 0, window_x_size  // 10, (window_y_size * 4) // 5))
white_text_surface = full_surface.subsurface(pygame.Rect(0, (4 * window_y_size) // 5, window_x_size  // 10, window_y_size // 5))
black_text_surface = full_surface.subsurface(pygame.Rect((9 * window_x_size) // 10, (4 * window_y_size) // 5, window_x_size  // 10, window_y_size // 5))

#run the window and wait for mouseclicks or quit
while True:
    if not game_over:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
# settings menue            
            elif start_game_mode:
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
                        pygame.transform.scale(display, (300,100))
                        pygame.display.set_caption("Spielbrett")
                        
                        game.painter.draw_background(display, background_color2, 128)
    
                        game.painter.draw_set_of_hexagons(game.players["white"].side_stones.values(), display)
                        game.painter.draw_set_of_hexagons(game.players["black"].side_stones.values(), display)
                        game.painter.write_start_side_numbers(game.players["white"], display)
                        game.painter.write_start_side_numbers(game.players["black"], display)
                        
                        
                        game.painter.draw_ingame_frame(display)
                        
                        game.interactor.set_game_surface(game_surface) #add game_surface as a attribute in interactor
                        
                        
                        start_game_mode = False 
                        
    pygame.display.update()
    clock.tick(FPS)
    
pygame.quit()
   
    






