#methods for window
import texts as t

def unmark_hexagons(display, display_before, marked_hexagons):
    display.blit(display_before, (0,0))
    for hexagon in marked_hexagons:
        hexagon.is_marked = False
    marked_hexagons.clear()  
    
def mark_hexagons(game, marked_hexagons, mark_width):
    game.painter.draw_set_of_hexagon_markings(marked_hexagons, (0,255,0), mark_mode = mark_width)
    
def check_winner(painter, surfaces, color, surr, game_over):
    if color == "white":    opp_color = "black"
    else:   opp_color = "white"
    color_surr = surr[0]
    opp_color_surr = surr[1]
    if color_surr and opp_color_surr:   
        painter.write_box_text(surfaces, t.win_text["tied"], "white")
        painter.write_box_text(surfaces, t.win_text["tied"], "black")
        game_over = True
    elif color_surr:    
        painter.write_box_text(surfaces, t.win_text[opp_color], "white")
        painter.write_box_text(surfaces, t.win_text[opp_color], "black")
        game_over = True
    elif opp_color_surr:  
        painter.write_box_text(surfaces, t.win_text[color], "white")
        painter.write_box_text(surfaces, t.win_text[color], "black")
        game_over = True
    return game_over

