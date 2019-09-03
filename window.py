import pygame, sys, buttons,  creating_board as cb
import game

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
window_x_size =  2440
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

#"save" the standard showed image
pygame.display.update()
start_window = showed_display.copy()

start_game_mode = True
settings_window_shown = False
first_turn= False
some_stone_clicked = False

#run the window and wait for mouseclicks or quit
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif start_game_mode == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if settings_window_shown == True:
                    showed_display.blit(start_window, (0,0))
                    settings_window_shown = False                    
                elif settings_button.pressed(event.pos) == True:
                    if settings_window_shown == False:
                        pygame.draw.rect(showed_display, (230,230,240), pygame.Rect(event.pos[0],
                                         event.pos[1]- button_y_size, button_x_size, button_y_size))
                        settings_window_shown = True
                elif start_game_button.pressed(event.pos) == True:
                    pygame.display.set_caption("Spielbrett")
                    cb.color_background(showed_display, background_color2, 128, window_size)
                    cb.set_ingame_frame(showed_display)
                    stones = cb.create_all_stones(showed_display, (255,255,230), (60,60,60))
                    
                    game_surface = showed_display.subsurface(pygame.Rect(int(window_x_size*0.1)+5, 0, int(window_x_size*0.8)-10, window_y_size))
                    Game = game.HvsH_Game(game_surface, stones)
                    gstones_list = Game.frame_stones.stones_list
                    Game.interactor.draw_board()
                                        
                    start_game_mode = False 
                    first_turn = True
        elif start_game_mode == False and first_turn == True and event.type== pygame.MOUSEBUTTONDOWN:
            if some_stone_clicked == False:
                clicked_on_list = Game.frame_stones.click_on_frame_stone(gstones_list, event.pos)
                #print(clicked_on_list)
                if True in clicked_on_list:
                    display_before = showed_display.copy()
                    index = clicked_on_list.index(True)
                    gstones_list[index].hexa_stone_draw_frame(gstones_list[index].pixel_position , (255,0,0), 3)
                    some_stone_clicked = True
            else:
                showed_display.blit(display_before, (0,0))
                some_stone_clicked = False
    pygame.display.update()
    
    
    