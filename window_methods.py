#methods for window

def unmark_hexagons(display, display_before, marked_hexagons):
    display.blit(display_before, (0,0))
    for hexagon in marked_hexagons:
        hexagon.is_marked = False
    marked_hexagons.clear()  
    
def mark_hexagons(game, marked_hexagons, mark_width):
    game.painter.draw_set_of_hexagon_markings(marked_hexagons, (0,255,0), mark_mode = mark_width)
    
def check_winner(color, surr, game_over):
    if color == "white":    opp_color = "black"
    else:   opp_color = "white"
    color_surr = surr[0]
    opp_color_surr = surr[1]
    if color_surr and opp_color_surr:   
        print("unentschieden") #NOTE: has to be printed in window left/right bottom corner
        game_over = True
    elif color_surr:    
        print(opp_color +  " wins")
        game_over = True
    elif opp_color_surr:    
        print(color + " wins")
        game_over = True
    return game_over

def check_opponent_options(player, calculator):
    player.set_action_hexagons(calculator)
    return player.moveable_hexagons or player.putable_hexagons
