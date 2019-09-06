import pygame, sys, buttons
import game
import start_menu
import window_methods as wm

pygame.init()
pygame.display.init()

#Set window and button sizes
window_x_size =  1020
window_y_size = window_x_size*9//16
window_size = (window_x_size, window_y_size)
button_x_size = window_x_size//6
button_y_size = window_y_size//6


#creating showable start_window on display with, set name and set background color
display = pygame.display.set_mode(window_size,0,32)
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
marked_hexagons = []

#create game object here firstly not encounter problems
game = game.HvsH_Game(display)



#run the window and wait for mouseclicks or quit
while True:
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
                    
                    pygame.display.set_caption("Spielbrett")
                    
                    game.painter.draw_background(display, background_color2, 128)

                    game.painter.draw_set_of_hexagons(game.players["white"].side_stones.values(), display)
                    game.painter.draw_set_of_hexagons(game.players["black"].side_stones.values(), display)
                    game.painter.write_start_side_numbers(game.players["white"], display)
                    game.painter.write_start_side_numbers(game.players["black"], display)
                    
                    game_surface = display.subsurface(pygame.Rect(int(window_x_size*0.1), 0, int(window_x_size*0.8), window_y_size))
                    game.painter.draw_board(game.board, game_surface)
                    
                    game.painter.draw_ingame_frame(display)
                    
                    game.interactor.set_game_surface(game_surface) #add game_surface as a attribute in interactor
                    
                    start_game_mode = False 
                    
                    #print a text claiming that white begins
# start game            
        elif not start_game_mode:
            #game.painter.write_start_side_numbers(game.players["white"], display)
            #game.painter.write_start_side_numbers(game.players["black"], display)
            if event.type== pygame.MOUSEBUTTONDOWN:
                #note, this is a list it shall contain exactly one nonempty hexagon iff the click was on this hexagon
                clicked_hexagon_l = game.interactor.calculator.get_clicked_hexagon(event.pos)
                
                if len(clicked_hexagon_l) == 1:
                    clicked_hexagon = clicked_hexagon_l[0]

# (white, 1)                
                    if game.turn == ("white", 1):
                        dir_hexagon = game.board.board[10][4] #shall be middle hexagon of the empty board
                        if not marked_hexagons:
                            display_before = display.copy()
                            if clicked_hexagon.color == "white":
                                src_hexagon = clicked_hexagon
                                game.painter.draw_hexagon_marking(src_hexagon, display, (255,0,0), mark_mode = 5)
                                game.painter.draw_hexagon_marking(dir_hexagon, game_surface, (0,255,0), mark_mode = 5)
                                marked_hexagons = [src_hexagon, dir_hexagon]
                        #in this case stone put will be executed and the turn goes one up
                        elif clicked_hexagon == dir_hexagon:
                            wm.unmark_hexagons(marked_hexagons, display, display_before, marked_hexagons)
                            game.interactor.execute_stone_put(game.players["white"], src_hexagon, dir_hexagon)
                            game.turn = ("black", 1)
                        #unmark marked hexagons
                        else:
                            if marked_hexagons:
                                wm.unmark_hexagons(marked_hexagons, display, display_before, marked_hexagons)
# (black, 1)                         
                    elif game.turn == ("black", 1):
                        neigh_coords = game.board.get_neighbours((10,4)).values()
                        dir_hexagons = [game.board.board[i][j] for i,j in neigh_coords] #all empty neighbours of the middle hexagon
                        if not marked_hexagons:
                            display_before = display.copy()
                            if clicked_hexagon.color == "black":
                                wm.draw_markings(game, display, game_surface, clicked_hexagon, dir_hexagons)
                                src_hexagon = clicked_hexagon
                                marked_hexagons = dir_hexagons + [src_hexagon]
                        #in this case stone put will be executed and the turn goes one up
                        elif clicked_hexagon in dir_hexagons:
                            wm.unmark_hexagons(marked_hexagons, display, display_before, marked_hexagons)
                            game.interactor.execute_stone_put(game.players["black"], src_hexagon, clicked_hexagon)
                            game.turn = ("white", 2)
                            dir_hexagons = [] #reset dir_hexagons so it wont cause problems in the following turns
                        #unmark marked hexagons
                        else:
                            if marked_hexagons:
                                wm.unmark_hexagons(marked_hexagons, display, display_before, marked_hexagons)
# turn 2 - 4                    
                    #at least one white and one black stone are put now. now be has to be put until 4. turn
                    elif game.turn[1] in {2,3,4}:
                        
                        current_player_color = game.turn[0]
                        bee_stone = list(game.players[current_player_color].stones["bee"].values())[0]
                        
                        #putting phase: bee is not yet on board
                        if not bee_stone.is_on_board:
                            if not marked_hexagons:
                                display_before = display.copy()
                                if clicked_hexagon in game.players[current_player_color].side_stones.values():
                                    dir_hexagons_coords = game.interactor.calculator.get_possible_put_fields(current_player_color)
                                    dir_hexagons = [game.board.board[coords[0]][coords[1]] for coords in dir_hexagons_coords]
                                    
                                    wm.draw_markings(game, display, game_surface, clicked_hexagon, dir_hexagons)
                                    
                                    src_hexagon = clicked_hexagon
                                    marked_hexagons = dir_hexagons + [src_hexagon]
                                    
                            elif clicked_hexagon in dir_hexagons:
                                wm.unmark_hexagons(marked_hexagons, display, display_before, marked_hexagons)
                                game.interactor.execute_stone_put(game.players[current_player_color], src_hexagon, clicked_hexagon)
                                #set new turn
                                if current_player_color == "white":
                                    game.turn[0] = "black"
                                else:
                                    game.turn[0] = "white"
                                    game.turn[1] += 1
                            
                            else:
                                if marked_hexagons:
                                    wm.unmark_hexagons(marked_hexagons, display, display_before, marked_hexagons)
                        
                else:
                    if marked_hexagons:
                        wm.unmark_hexagons(marked_hexagons, display, display_before, marked_hexagons)


















              
    pygame.display.update()
   
    
    
    
    
    
#saved for maybe use
#if marked_hexagons:
#    display.blit(display_before, (0,0))
#    #unmark marked hexagons which were marked during the process (in painter.draw_hexagon_frame)
#    for hexagon in marked_hexagons:
#        hexagon.is_marked = False
#        hexagon.is_marked = False
#    marked_hexagons = []