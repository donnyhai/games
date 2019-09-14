import pygame, sys, buttons
import game
import start_menu
import window_methods as wm

pygame.init()
pygame.display.init()

#Set window and button sizes
window_x_size =  1100
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
display = pygame.display.set_mode(window_size,0,32)
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
game_finished = False

#create game object here firstly not encounter problems
game = game.HvsH_Game(display)

full_surface = display
game_surface = full_surface.subsurface(pygame.Rect(window_x_size * 0.1 , 0, window_x_size * 0.8 , window_y_size))
white_surface = full_surface.subsurface(pygame.Rect(0, 0, window_x_size // 10, (window_y_size * 4) // 5))
black_surface = full_surface.subsurface(pygame.Rect((window_x_size * 9) // 10, 0, window_x_size  // 10, (window_y_size * 4) // 5))
white_text_surface = full_surface.subsurface(pygame.Rect(0, (4 * window_y_size) // 5, window_x_size  // 10, window_y_size // 5))
black_text_surface = full_surface.subsurface(pygame.Rect((9 * window_x_size) // 10, (4 * window_y_size) // 5, window_x_size  // 10, window_y_size // 5))

human_color = "white"

#run the window and wait for mouseclicks or quit
while True:
    if not game_finished:
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
                    clicked_hexagon = game.interactor.calculator.get_clicked_hexagon(event.pos)
                    
                    if clicked_hexagon.number != 99: #special condition, see calculator.get_clicked_hexagon and calculator.empty_help_stone
    
# (white, 1)                
                        if game.turn == ("white", 1):
                            dir_hexagon = game.board.board[first_stone_board_pos[0]][first_stone_board_pos[1]] #shall be middle hexagon of the empty board
                            if not marked_hexagons:
                                display_before = display.copy()
                                if clicked_hexagon.color == "white":
                                    src_hexagon = clicked_hexagon
                                    marked_hexagons = [src_hexagon, dir_hexagon]
                                    wm.mark_hexagons(game, marked_hexagons, mark_size)
                            #in this case stone put will be executed and the turn goes one up
                            elif clicked_hexagon == dir_hexagon:
                                wm.unmark_hexagons(display, display_before, marked_hexagons)
                                game.interactor.execute_stone_put(game.players["white"], src_hexagon, dir_hexagon)
                                game.turn = ("black", 1)
                            #unmark marked hexagons
                            else:
                                if marked_hexagons: wm.unmark_hexagons(display, display_before, marked_hexagons)
# (black, 1)                         
                        elif game.turn == ("black", 1):
                            neigh_coords = game.board.get_neighbours(first_stone_board_pos).values()
                            dir_hexagons = [game.board.board[i][j] for i,j in neigh_coords] #all empty neighbours of the middle hexagon
                            if not marked_hexagons:
                                display_before = display.copy()
                                if clicked_hexagon.color == "black":
                                    src_hexagon = clicked_hexagon
                                    marked_hexagons = dir_hexagons + [src_hexagon]
                                    wm.mark_hexagons(game, marked_hexagons, mark_size)
                            #in this case stone put will be executed and the turn goes one up
                            elif clicked_hexagon in dir_hexagons:
                                wm.unmark_hexagons(display, display_before, marked_hexagons)
                                game.interactor.execute_stone_put(game.players["black"], src_hexagon, clicked_hexagon)
                                game.turn = ("white", 2)
                                dir_hexagons.clear() #reset dir_hexagons so it wont cause problems in the following turns
                            #unmark marked hexagons
                            else:
                                if marked_hexagons: wm.unmark_hexagons(display, display_before, marked_hexagons)
# turn 2 - 4                    
                        #at least one white and one black stone are put now. now be has to be put until 4. turn
                        elif game.turn[1] in {2,3,4}:
                            current_player_color = game.turn[0]
                            bee_stone = list(game.players[current_player_color].stones["bee"].values())[0]
    #bee not put
                            #putting phase: bee is not yet on board
                            if not bee_stone.is_on_board:
                                if not marked_hexagons:
                                    display_before = display.copy()
                                    
                                    #mark put
                                    if clicked_hexagon in game.players[current_player_color].side_stones.values():
                                        if game.players[current_player_color].side_stones_numbers[clicked_hexagon.type] > 0:
                                            #check whether clicked hexagon is bee in the case that it is turn 4 now
                                            #note: in this if case (10 lines up) we are in the case that the bee is not yet put
                                            if game.turn[1] < 4 or clicked_hexagon.type == "bee": 
                                                dir_hexagons_coords = game.interactor.calculator.get_possible_put_fields(current_player_color)
                                                dir_hexagons = [game.board.board[coords[0]][coords[1]] for coords in dir_hexagons_coords]
            
                                                src_hexagon = clicked_hexagon
                                                marked_hexagons = dir_hexagons + [src_hexagon]
                                                wm.mark_hexagons(game, marked_hexagons, mark_size)
                                            
                                #execute put
                                elif clicked_hexagon in dir_hexagons:
                                    wm.unmark_hexagons(display, display_before, marked_hexagons)
                                    game.interactor.execute_stone_put(game.players[current_player_color], src_hexagon, clicked_hexagon)
                                    #set new turn
                                    if current_player_color == "white":
                                        game.turn = ("black", game.turn[1])
                                    else:
                                        game.turn = ("white", game.turn[1] + 1)
                                    dir_hexagons.clear()
                                    wm.check_winner(current_player_color, game.interactor.calculator.winning_condition(current_player_color), game_finished)
                                
                                else:
                                    if marked_hexagons: wm.unmark_hexagons(display, display_before, marked_hexagons)
    #bee already put                          
                            else:
                                if not marked_hexagons:
                                    display_before = display.copy()
                                    
                                    #mark put
                                    if clicked_hexagon in game.players[current_player_color].side_stones.values():
                                        if game.players[current_player_color].side_stones_numbers[clicked_hexagon.type] > 0:
                                            dir_hexagons_coords = game.interactor.calculator.get_possible_put_fields(current_player_color)
                                            dir_hexagons = [game.board.board[coords[0]][coords[1]] for coords in dir_hexagons_coords]
        
                                            src_hexagon = clicked_hexagon
                                            marked_hexagons = dir_hexagons + [src_hexagon]
                                            wm.mark_hexagons(game, marked_hexagons, mark_size)
                                    
                                    #mark move
                                    elif clicked_hexagon in game.players[current_player_color].stones_list:
                                        src_hexagon = clicked_hexagon
                                        bug_cond = src_hexagon.type == "bug"
                                        if bug_cond:
                                            bug_cond = len(src_hexagon.underlaying_stones) > 0
                                        if game.interactor.calculator.board_keeps_connected(src_hexagon.board_pos) or bug_cond:
                                            dir_hexagons_coords = game.interactor.calculator.get_possible_move_fields(src_hexagon)
                                            dir_hexagons = [game.board.board[coords[0]][coords[1]] for coords in dir_hexagons_coords]
                                            
                                            marked_hexagons = dir_hexagons + [src_hexagon]
                                            wm.mark_hexagons(game, marked_hexagons, mark_size)
                                
                                #execute put
                                elif src_hexagon in game.players[current_player_color].side_stones.values():
                                    if clicked_hexagon in dir_hexagons:
                                        wm.unmark_hexagons(display, display_before, marked_hexagons)
                                        game.interactor.execute_stone_put(game.players[current_player_color], src_hexagon, clicked_hexagon)
                                        #set new turn
                                        if current_player_color == "white":
                                            game.turn = ("black", game.turn[1])
                                        else:
                                            game.turn = ("white", game.turn[1] + 1)
                                        dir_hexagons.clear()
                                        wm.check_winner(current_player_color, game.interactor.calculator.winning_condition(current_player_color), game_finished)
                                    else:
                                        if marked_hexagons: wm.unmark_hexagons(display, display_before, marked_hexagons)
                                
                                #execute move
                                elif src_hexagon in game.players[current_player_color].stones_list:
                                    if clicked_hexagon in dir_hexagons and clicked_hexagon.board_pos != src_hexagon.board_pos: 
                                        wm.unmark_hexagons(display, display_before, marked_hexagons)
                                        if src_hexagon.type == "bug":
                                            if not clicked_hexagon.is_empty or len(src_hexagon.underlaying_stones) > 0:
                                                game.interactor.move_bug_on_nonempty_stone(game.players[current_player_color], src_hexagon, clicked_hexagon)
                                        else:
                                            game.interactor.execute_stone_move(game.players[current_player_color], src_hexagon, clicked_hexagon)
                                        #set new turn
                                        if current_player_color == "white":
                                            game.turn = ("black", game.turn[1])
                                        else:
                                            game.turn = ("white", game.turn[1] + 1)
                                        dir_hexagons.clear()
                                        wm.check_winner(current_player_color, game.interactor.calculator.winning_condition(current_player_color), game_finished)
                                    else:
                                        if marked_hexagons: wm.unmark_hexagons(display, display_before, marked_hexagons)
                                
                                else:
                                    if marked_hexagons: wm.unmark_hexagons(display, display_before, marked_hexagons)
                            
                            
# turn > 4                        
                        elif game.turn[1] > 4:           
                            current_player_color = game.turn[0]
                            
                            if not marked_hexagons:
                                display_before = display.copy()
                                
                                #mark put
                                if clicked_hexagon in game.players[current_player_color].side_stones.values():
                                    if game.players[current_player_color].side_stones_numbers[clicked_hexagon.type] > 0:
                                        dir_hexagons_coords = game.interactor.calculator.get_possible_put_fields(current_player_color)
                                        dir_hexagons = [game.board.board[coords[0]][coords[1]] for coords in dir_hexagons_coords]
    
                                        src_hexagon = clicked_hexagon
                                        marked_hexagons = dir_hexagons + [src_hexagon]
                                        wm.mark_hexagons(game, marked_hexagons, mark_size)
                                    
                                #mark move
                                elif clicked_hexagon in game.players[current_player_color].stones_list:
                                    src_hexagon = clicked_hexagon
                                    bug_cond = src_hexagon.type == "bug"
                                    if bug_cond:
                                        bug_cond = len(src_hexagon.underlaying_stones) > 0
                                    if game.interactor.calculator.board_keeps_connected(src_hexagon.board_pos) or bug_cond:
                                        dir_hexagons_coords = game.interactor.calculator.get_possible_move_fields(src_hexagon)
                                        dir_hexagons = [game.board.board[coords[0]][coords[1]] for coords in dir_hexagons_coords]
        
                                        marked_hexagons = dir_hexagons + [src_hexagon]
                                        wm.mark_hexagons(game, marked_hexagons, mark_size)
                                
                            #execute put
                            elif src_hexagon in game.players[current_player_color].side_stones.values():
                                if clicked_hexagon in dir_hexagons:
                                    wm.unmark_hexagons(display, display_before, marked_hexagons)
                                    game.interactor.execute_stone_put(game.players[current_player_color], src_hexagon, clicked_hexagon)
                                    #set new turn
                                    if current_player_color == "white":
                                        game.turn = ("black", game.turn[1])
                                    else:
                                        game.turn = ("white", game.turn[1] + 1)
                                    dir_hexagons.clear()
                                    wm.check_winner(current_player_color, game.interactor.calculator.winning_condition(current_player_color), game_finished)
                                else:
                                    if marked_hexagons: wm.unmark_hexagons(display, display_before, marked_hexagons)
                            
                            #execute move
                            elif src_hexagon in game.players[current_player_color].stones_list:
                                if clicked_hexagon in dir_hexagons and clicked_hexagon.board_pos != src_hexagon.board_pos:
                                    wm.unmark_hexagons(display, display_before, marked_hexagons)
                                    if src_hexagon.type == "bug":
                                        if not clicked_hexagon.is_empty or len(src_hexagon.underlaying_stones) > 0:
                                            game.interactor.move_bug_on_nonempty_stone(game.players[current_player_color], src_hexagon, clicked_hexagon)
                                    else:
                                        game.interactor.execute_stone_move(game.players[current_player_color], src_hexagon, clicked_hexagon)
                                    #set new turn
                                    if current_player_color == "white":
                                        game.turn = ("black", game.turn[1])
                                    else:
                                        game.turn = ("white", game.turn[1] + 1)
                                    dir_hexagons.clear()
                                    wm.check_winner(current_player_color, game.interactor.calculator.winning_condition(current_player_color), game_finished)
                                else:
                                    if marked_hexagons: wm.unmark_hexagons(display, display_before, marked_hexagons)
                            else:
                                if marked_hexagons: wm.unmark_hexagons(display, display_before, marked_hexagons)
                    else:
                        if marked_hexagons: wm.unmark_hexagons(display, display_before, marked_hexagons)

    pygame.display.update()
    clock.tick(FPS)
    
pygame.quit()
   
    






