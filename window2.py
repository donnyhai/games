import pygame, sys, button
import game
import texts as t, colors as c
import start_menu
import window_methods as wm

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
                        
                        game = game.HvsH_Game_Extended(display) #create game
                        
                        pygame.display.set_caption("Spielbrett")
                        
                        game.painter.draw_background(game.surfaces["surface_board"], c.background_board)
                        game.painter.draw_background(game.surfaces["surface_stones"]["white"], c.background_side_stones)
                        game.painter.draw_background(game.surfaces["surface_stones"]["black"], c.background_side_stones)
                        game.painter.draw_background(game.surfaces["surface_text"]["white"], c.background_text_box)
                        game.painter.draw_background(game.surfaces["surface_text"]["black"], c.background_text_box)
    
                        game.painter.draw_set_of_hexagons(game.players["white"].side_stones.values(), game.surfaces["surface_stones"]["white"])
                        game.painter.draw_set_of_hexagons(game.players["black"].side_stones.values(), game.surfaces["surface_stones"]["black"])
                        game.painter.draw_all_stone_numbers(game.players["white"], game.surfaces)
                        game.painter.draw_all_stone_numbers(game.players["black"], game.surfaces)
                        
                        game.painter.draw_board(game.board, game.surfaces, game.buttons)
                        
                        game.painter.draw_ingame_frame(game.surfaces["surface_full"])
                        
                        start_game_mode = False  
                        
                        #print a text claiming that white begins
                        game.painter.write_box_text(game.surfaces, t.welcome_text, "white")
                        game.painter.write_box_text(game.surfaces, t.welcome_text, "black")
# start game            
            elif not start_game_mode:
                
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if wm.point_in_surface(game.surfaces["surface_board"], event.pos):
                        if event.button == 1: #button 1: left mouse click
                            if not drag:
                                drag = True
                                pos = (event.pos, event.pos)
                                counter = 0
                        elif event.button == 5: #button 4: scroll in 
                            #the following if check ensures that you do not zoom to much out, as for some reason you cannot zoom in again 
                            #(why does this happen ? is there a better factor than 100 ?)
                            if game.board.hexagon_size > game.surfaces["surface_full"].get_width() // 80: 
                                ratio = 0.85 #zoom out
                                ep, dp = event.pos, game.board.draw_position
                                #make the event.pos the center of zooming
                                if game.board.scroll_is_inside_board(ep):   offset = ((1 - ratio) * (ep[0] - dp[0]), (1 - ratio) * (ep[1] - dp[1]))
                                else:   offset = (0,0)
                                game.interactor.scale_board(ratio)
                                game.interactor.translate_board(offset)
                                game.painter.draw_board(game.board, game.surfaces, game.buttons, mark_size)
                        elif event.button == 4: #button 5: scroll out
                            ratio = 1.18 #zoom in
                            ep, dp = event.pos, game.board.draw_position
                            #make the event.pos the center of zooming
                            if game.board.scroll_is_inside_board(ep):   offset = ((1 - ratio) * (ep[0] - dp[0]), (1 - ratio) * (ep[1] - dp[1]))
                            else:   offset = (0,0)
                            game.interactor.scale_board(ratio)
                            game.interactor.translate_board(offset)
                            game.painter.draw_board(game.board, game.surfaces, game.buttons, mark_size)
                        
                elif event.type == pygame.MOUSEMOTION and drag:
                    if counter == 2: #makes the clicking nicer (there should not be dragging, just because a click was not completely precise)
                        moved = True
                        pos = pos[1], event.pos #save actual and one mousepos before to always add a new draw offset from pixel to pixel
                        if wm.point_in_surface(game.surfaces["surface_board"], pos[1]):
                            game.interactor.translate_board((pos[1][0] - pos[0][0], pos[1][1] - pos[0][1]))
                            game.painter.draw_board(game.board, game.surfaces, game.buttons, mark_size)
                    else: counter += 1  
                
                if event.type== pygame.MOUSEBUTTONUP and event.button == 1:
                    drag = False
                    if moved:   moved = False
                    else:
                        
                        if game.buttons["center_button"].pressed(event.pos):
                            game.board.draw_position = game.board.inital_pixel_pos
                            game.interactor.scale_board(game.board.initial_hexagon_size / game.board.hexagon_size)
                            game.painter.draw_board(game.board, game.surfaces, game.buttons, mark_size)
                        else:
                        
                        
                            #note, this is a list it shall contain exactly one nonempty hexagon iff the click was on this hexagon
                            clicked_hexagon = game.interactor.calculator.get_clicked_hexagon(event.pos)
                            
                            if clicked_hexagon.number != 99: #special condition, see calculator.get_clicked_hexagon and calculator.empty_help_stone
            
        # (white, 1)                
                                if game.turn == ("white", 1):
                                    dir_hexagon = game.board.board[first_stone_board_pos] #shall be middle hexagon of the empty board
                                    if not marked_hexagons:
                                        if clicked_hexagon.color == "white":
                                            src_hexagon = clicked_hexagon
                                            marked_hexagons = [src_hexagon, dir_hexagon]
                                            wm.mark_hexagons(game, marked_hexagons, mark_size)
                                    #in this case stone put will be executed and the turn goes one up
                                    elif clicked_hexagon == dir_hexagon:
                                        wm.unmark_hexagons(game, game.players["white"], marked_hexagons)
                                        game.interactor.execute_stone_put(game.players["white"], src_hexagon, dir_hexagon)
                                        game.turn = ("black", 1)
                                    #unmark marked hexagons
                                    else:
                                        if marked_hexagons: wm.unmark_hexagons(game, game.players["white"], marked_hexagons)
        # (black, 1)                         
                                elif game.turn == ("black", 1):
                                    neigh_coords = game.board.get_neighbours(first_stone_board_pos).values()
                                    dir_hexagons = [game.board.board[coord] for coord in neigh_coords] #all empty neighbours of the middle hexagon
                                    if not marked_hexagons:
                                        if clicked_hexagon.color == "black":
                                            src_hexagon = clicked_hexagon
                                            marked_hexagons = dir_hexagons + [src_hexagon]
                                            wm.mark_hexagons(game, marked_hexagons, mark_size)
                                    #in this case stone put will be executed and the turn goes one up
                                    elif clicked_hexagon in dir_hexagons:
                                        wm.unmark_hexagons(game, game.players["black"], marked_hexagons)
                                        game.interactor.execute_stone_put(game.players["black"], src_hexagon, clicked_hexagon)
                                        game.turn = ("white", 2)
                                        dir_hexagons.clear() #reset dir_hexagons so it wont cause problems in the following turns
                                    #unmark marked hexagons
                                    else:
                                        if marked_hexagons: wm.unmark_hexagons(game, game.players["black"], marked_hexagons)
        # turn 2 - 4                    
                                #at least one white and one black stone are put now. now be has to be put until 4. turn
                                elif game.turn[1] in {2,3,4}:
                                    current_player_color = game.turn[0]
                                    bee_stone = list(game.players[current_player_color].stones["bee"].values())[0]
            #bee not put
                                    #putting phase: bee is not yet on board
                                    if not bee_stone.is_on_board:
                                        if not marked_hexagons:
                                            
                                            #mark put
                                            if clicked_hexagon in game.players[current_player_color].side_stones.values():
                                                src_hexagon = clicked_hexagon
                                                if src_hexagon in game.players[current_player_color].putable_hexagons:
                                                    #check whether clicked hexagon is bee in the case that it is turn 4 now
                                                    #note: we are in the case that the bee is not yet put
                                                    if game.turn[1] < 4 or clicked_hexagon.type == "bee": 
                                                        dir_hexagons_coords = game.interactor.calculator.get_possible_put_fields(current_player_color)
                                                        dir_hexagons = [game.board.board[coords] for coords in dir_hexagons_coords]
                                                        marked_hexagons = dir_hexagons + [src_hexagon]
                                                        wm.mark_hexagons(game, marked_hexagons, mark_size)
                                                    
                                        #execute put
                                        elif clicked_hexagon in dir_hexagons:
                                            wm.unmark_hexagons(game, game.players[current_player_color], marked_hexagons)
                                            game.interactor.execute_stone_put(game.players[current_player_color], src_hexagon, clicked_hexagon)
                                            game.turn_up() #set new turn
                                            #check whether opponent has any possible put or move, if not put turn up 
                                            opponent_player = game.players[game.turn[0]]
                                            opponent_player.set_action_hexagons(game.interactor.calculator)
                                            if not opponent_player.moveable_hexagons and not opponent_player.putable_hexagons: game.turn_up()
                                            #check winning condition
                                            game_over = wm.check_winner(game.painter, game.surfaces, current_player_color, game.interactor.calculator.winning_condition(current_player_color), game_over)
                                            dir_hexagons.clear()
                                            
                                            #put bee reminder:
                                            if current_player_color == "white":
                                                if not game.players["black"].stones["bee"][1].is_on_board:
                                                    game.painter.write_box_text(game.surfaces, t.bee_reminder, "black")
                                            else:
                                                if not game.players["white"].stones["bee"][1].is_on_board:
                                                    game.painter.write_box_text(game.surfaces, t.bee_reminder, "white")
                                        
                                        else:
                                            if marked_hexagons: wm.unmark_hexagons(game, game.players[current_player_color], marked_hexagons)
            #bee already put                          
                                    else:
                                        if not marked_hexagons:
                                            
                                            #mark put
                                            if clicked_hexagon in game.players[current_player_color].side_stones.values():
                                                src_hexagon = clicked_hexagon
                                                if src_hexagon in game.players[current_player_color].putable_hexagons:
                                                    dir_hexagons_coords = game.interactor.calculator.get_possible_put_fields(current_player_color)
                                                    dir_hexagons = [game.board.board[coords] for coords in dir_hexagons_coords]
                                                    marked_hexagons = dir_hexagons + [src_hexagon]
                                                    wm.mark_hexagons(game, marked_hexagons, mark_size)
                                            
                                            #mark move
                                            elif clicked_hexagon in game.players[current_player_color].stones_list:
                                                src_hexagon = clicked_hexagon
                                                if src_hexagon in game.players[current_player_color].moveable_hexagons:
                                                    dir_hexagons_coords = game.interactor.calculator.get_possible_move_fields(src_hexagon)
                                                    dir_hexagons = [game.board.board[coords] for coords in dir_hexagons_coords]
                                                    marked_hexagons = dir_hexagons + [src_hexagon]
                                                    wm.mark_hexagons(game, marked_hexagons, mark_size)
                                        
                                        #execute put
                                        elif src_hexagon in game.players[current_player_color].side_stones.values():
                                            if clicked_hexagon in dir_hexagons:
                                                wm.unmark_hexagons(game, game.players[current_player_color], marked_hexagons)
                                                game.interactor.execute_stone_put(game.players[current_player_color], src_hexagon, clicked_hexagon)
                                                game.turn_up() #set new turn
                                                #check whether opponent has any possible put or move, if not put turn up 
                                                opponent_player = game.players[game.turn[0]]
                                                opponent_player.set_action_hexagons(game.interactor.calculator)
                                                if not opponent_player.moveable_hexagons and not opponent_player.putable_hexagons: game.turn_up()
                                                #check winning condition
                                                game_over = wm.check_winner(game.painter, game.surfaces, current_player_color, game.interactor.calculator.winning_condition(current_player_color), game_over)
                                                dir_hexagons.clear()
                                                
                                                #put bee reminder:
                                                if current_player_color == "white":
                                                    if not game.players["black"].stones["bee"][1].is_on_board:
                                                        game.painter.write_box_text(game.surfaces, t.bee_reminder, "black")
                                                else:
                                                    if not game.players["white"].stones["bee"][1].is_on_board:
                                                        game.painter.write_box_text(game.surfaces, t.bee_reminder, "white")
                                            else: 
                                                if marked_hexagons: wm.unmark_hexagons(game, game.players[current_player_color], marked_hexagons)
                                        
                                        #execute move
                                        elif src_hexagon in game.players[current_player_color].stones_list:
                                            if clicked_hexagon in dir_hexagons and clicked_hexagon.board_pos != src_hexagon.board_pos: 
                                                wm.unmark_hexagons(game, game.players[current_player_color], marked_hexagons)
                                                if src_hexagon.type in {"bug", "mosquito"}:
                                                    if not clicked_hexagon.is_empty or len(src_hexagon.underlaying_stones) > 0:
                                                        game.interactor.move_bug_on_nonempty_stone(game.players[current_player_color], src_hexagon, clicked_hexagon)
                                                    else: game.interactor.execute_stone_move(game.players[current_player_color], src_hexagon, clicked_hexagon)
                                                else: game.interactor.execute_stone_move(game.players[current_player_color], src_hexagon, clicked_hexagon)
                                                game.turn_up() #set new turn
                                                #check whether opponent has any possible put or move, if not put turn up 
                                                opponent_player = game.players[game.turn[0]]
                                                opponent_player.set_action_hexagons(game.interactor.calculator)
                                                if not opponent_player.moveable_hexagons and not opponent_player.putable_hexagons: game.turn_up()
                                                #check winning condition
                                                game_over = wm.check_winner(game.painter, game.surfaces, current_player_color, game.interactor.calculator.winning_condition(current_player_color), game_over)
                                                dir_hexagons.clear()
                                                
                                                #put bee reminder:
                                                if current_player_color == "white":
                                                    if not game.players["black"].stones["bee"][1].is_on_board:
                                                        game.painter.write_box_text(game.surfaces, t.bee_reminder, "black")
                                                else:
                                                    if not game.players["white"].stones["bee"][1].is_on_board:
                                                        game.painter.write_box_text(game.surfaces, t.bee_reminder, "white")
                                            else: 
                                                if marked_hexagons: wm.unmark_hexagons(game, game.players[current_player_color], marked_hexagons)
                                        
                                        else: 
                                            if marked_hexagons: wm.unmark_hexagons(game, game.players[current_player_color], marked_hexagons)
                                    
                                    
        # turn > 4                        
                                elif game.turn[1] > 4:           
                                    current_player_color = game.turn[0]
                                    
                                    if not marked_hexagons:
                                        
                                        #mark put
                                        if clicked_hexagon in game.players[current_player_color].side_stones.values():
                                            src_hexagon = clicked_hexagon
                                            if src_hexagon in game.players[current_player_color].putable_hexagons:
                                                dir_hexagons_coords = game.interactor.calculator.get_possible_put_fields(current_player_color)
                                                dir_hexagons = [game.board.board[coords] for coords in dir_hexagons_coords]
                                                marked_hexagons = dir_hexagons + [src_hexagon]
                                                wm.mark_hexagons(game, marked_hexagons, mark_size)
                                        
                                        #mark move
                                        elif clicked_hexagon in game.players[current_player_color].stones_list:
                                            src_hexagon = clicked_hexagon
                                            if src_hexagon in game.players[current_player_color].moveable_hexagons:
                                                dir_hexagons_coords = game.interactor.calculator.get_possible_move_fields(src_hexagon)
                                                dir_hexagons = [game.board.board[coords] for coords in dir_hexagons_coords]
                                                marked_hexagons = dir_hexagons + [src_hexagon]
                                                wm.mark_hexagons(game, marked_hexagons, mark_size)
                                        
                                    #execute put
                                    elif src_hexagon in game.players[current_player_color].side_stones.values():
                                        if clicked_hexagon in dir_hexagons:
                                            wm.unmark_hexagons(game, game.players[current_player_color], marked_hexagons)
                                            game.interactor.execute_stone_put(game.players[current_player_color], src_hexagon, clicked_hexagon)
                                            game.turn_up() #set new turn
                                            #check whether opponent has any possible put or move, if not put turn up 
                                            opponent_player = game.players[game.turn[0]]
                                            opponent_player.set_action_hexagons(game.interactor.calculator)
                                            if not opponent_player.moveable_hexagons and not opponent_player.putable_hexagons: game.turn_up()
                                            #check winning condition
                                            game_over = wm.check_winner(game.painter, game.surfaces, current_player_color, game.interactor.calculator.winning_condition(current_player_color), game_over)
                                            dir_hexagons.clear()
                                        else: 
                                            if marked_hexagons: wm.unmark_hexagons(game, game.players[current_player_color], marked_hexagons)
                                    
                                    #execute move
                                    elif src_hexagon in game.players[current_player_color].stones_list:
                                        if clicked_hexagon in dir_hexagons and clicked_hexagon.board_pos != src_hexagon.board_pos:
                                            wm.unmark_hexagons(game, game.players[current_player_color], marked_hexagons)
                                            if src_hexagon.type in {"bug", "mosquito"}:
                                                if not clicked_hexagon.is_empty or len(src_hexagon.underlaying_stones) > 0:
                                                    game.interactor.move_bug_on_nonempty_stone(game.players[current_player_color], src_hexagon, clicked_hexagon)
                                                else: game.interactor.execute_stone_move(game.players[current_player_color], src_hexagon, clicked_hexagon)
                                            else: game.interactor.execute_stone_move(game.players[current_player_color], src_hexagon, clicked_hexagon)
                                            game.turn_up() #set new turn
                                            #check whether opponent has any possible put or move, if not put turn up 
                                            opponent_player = game.players[game.turn[0]]
                                            opponent_player.set_action_hexagons(game.interactor.calculator)
                                            if not opponent_player.moveable_hexagons and not opponent_player.putable_hexagons: game.turn_up()
                                            #check winning condition
                                            game_over = wm.check_winner(game.painter, game.surfaces, current_player_color, game.interactor.calculator.winning_condition(current_player_color), game_over)
                                            dir_hexagons.clear()
                                        
                                        else:
                                            if marked_hexagons: wm.unmark_hexagons(game, game.players[current_player_color], marked_hexagons)
                                    else:
                                        if marked_hexagons: wm.unmark_hexagons(game, game.players[current_player_color], marked_hexagons)
                            else:
                                if marked_hexagons: wm.unmark_hexagons(game, game.players[current_player_color], marked_hexagons)

    pygame.display.update()
    clock.tick(FPS)
    
pygame.quit()
   
    






