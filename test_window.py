import pygame, sys, buttons
import game
import start_menu

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
display = pygame.display.set_mode(window_size, pygame.RESIZABLE, 0 ,32)
#showed_display = pygame.display.set_mode((1920, 1080),pygame.RESIZABLE, 32)
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
creme_black = (60,60,60 )

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

start_game_mode = True
settings_window_shown = False
some_stone_marked = False

#run the window and wait for mouseclicks or quit
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif start_game_mode:
            if event.type == pygame.MOUSEBUTTONUP:
                ####NC: settings_window still has to be implemented functionally
                if settings_window_shown == True: 
                    display.blit(start_window, (0,0))
                    settings_window_shown = False                    
                elif settings_button.pressed(event.pos) == True:
                    settings_window  = start_menu.settings_window(display, (220,230,220, 128), event.pos, (1.5 * button_x_size, 1.5 * button_y_size))
                    settings_window.draw_settings_window()
                    settings_window.write_settings(settings_window.settings, (0,0,0), 15)
                    settings_window_shown = True
                ####
                elif start_game_button.pressed(event.pos) == True:
                    
                    pygame.display.set_caption("Spielbrett")
                    game = game.HvsH_Game(display)
                    
                    game.painter.draw_background(background_color2, 127)
                    game.painter.draw_ingame_frame()
                    game.painter.draw_set_of_insect_stones(game.players["white"].side_stones.values())
                    game.painter.draw_set_of_insect_stones(game.players["black"].side_stones.values())
                    
                    game_surface = display.subsurface(pygame.Rect(int(window_x_size*0.1)+5, 0, int(window_x_size*0.8)-10, window_y_size))
                    game.painter.draw_board(game.board, game_surface)
                    
                    start_game_mode = False 
                    
                    #print a text claiming that white begins
            
        elif not start_game_mode:
            if event.type== pygame.MOUSEBUTTONDOWN:
                clicked_hexagon = game.interactor.calculator.get_clicked_hexagon(event.pos) #note, this is a list
                #it shall contain exactly one hexagon iff the click was on this hexagon
                
                if game.turn == ("white", 1):
                    dir_hexagon = game.board.board[10][4] #shall be middle hexagon of the empty board
                    if not some_stone_marked:
                        display_before = display.copy()
                        if len(clicked_hexagon) == 1 and clicked_hexagon[0].stone.color == "white":
                            src_hexagon = clicked_hexagon[0]
                            game.painter.draw_hexagon_frame(src_hexagon, display, (255,0,0), mark_mode = 5)
                            game.painter.draw_hexagon_frame(dir_hexagon, game_surface, (0,255,0), mark_mode = 5)
                            some_stone_marked = True
                    #in this case stone put will be executed and the turn goes one up
                    elif dir_hexagon.point_in_hexagon(event.pos) == True and dir_hexagon.is_marked:
                        display.blit(display_before, (0,0))
                        game.interactor.execute_stone_put(game.players["white"], src_hexagon, dir_hexagon)
                        game.turn = ("black", 1)
                        some_stone_marked = False
                    else:
                        display.blit(display_before, (0,0))
                        some_stone_marked = False
                        #unmark both hexagons which were marked during the process (in painter.draw_hexagon_frame)
                        src_hexagon.is_marked = False
                        dir_hexagon.is_marked = False
                        
                        
                elif game.turn == ("black", 1):
                    neigh_coords = game.board.get_neighbours((10,4)).values()
                    dir_hexagons = [game.board.board[i][j] for i,j in neigh_coords] #all empty neighbours of the middle hexagon
                    if not some_stone_marked:
                        display_before = display.copy()
                        if len(clicked_hexagon) == 1 and clicked_hexagon[0].stone.color == "black":
                            game.painter.draw_hexagon_frame(clicked_hexagon[0], display, (255,0,0), mark_mode = 5)
                            game.painter.draw_set_of_hexagon_frames(dir_hexagons, game_surface, (0,255,0), mark_mode = 5)
                            src_hexagon = clicked_hexagon[0]
                            some_stone_clicked = True
                    elif clicked_hexagon[0] in dir_hexagons and clicked_hexagon[0].is_marked:
                        display.blit(display_before, (0,0))
                        game.interactor.execute_stone_put(game.players["black"], src_hexagon, clicked_hexagon[0])
                        game.turn = ("white", 2)
                        some_stone_clicked = False
                    else:
                        display.blit(display_before, (0,0))
                        some_stone_clicked = False
                
                #at least one white and one black stone are put now. now bee has to be put until 4. turn or in informatical speech 3rd turn
                elif game.turn[1] in {2,3,4}:
                    pass
                    
    pygame.display.update()
    
    
    