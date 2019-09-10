import pygame
#import hexagon_stone as hs
from math import sqrt
pygame.init()


class Interactor:
    def __init__(self, painter, calculator, turn):
        self.painter = painter
        self.calculator = calculator
        self.players = self.calculator.locator.players
        self.board = self.calculator.board
        self.surface = self.board.surface
        self.turn = turn
    
    def set_game_surface(self, game_surface):
        self.game_surface = game_surface
    
    #this function evaluates and executes a potential stone put. input is the player and both clicked hexagons, 
    #first the hexagon at the side, second a hexagon on the board   
    def execute_stone_put(self, player, first_clicked_hex, second_clicked_hex):
        fhex = first_clicked_hex
        shex = second_clicked_hex
        cond1 = True
        cond2 = True
        
        if self.turn[1] >= 2:
            possible_put_fields = self.calculator.get_possible_put_fields(fhex.color)
            cond1 = self.put_stone_condition(player, fhex, shex)
            cond2 = shex.board_pos in possible_put_fields
            
        if cond1 and cond2:
            ##first execute logical aspects
            stone_type = fhex.type
            #find stone in player.stones which is not yet on the board
            for hstone in player.stones[stone_type].values():
                if not hstone.is_on_board:
                    draw_hexagon = hstone
                    break
            #set the corresponding side_stone_number one down
            player.side_stones_numbers[stone_type] -= 1
            #set new pixel_pos and board_pos
            draw_hexagon.set_pixel_pos(shex.pixel_pos)
            draw_hexagon.set_board_pos(shex.board_pos)
            #put the hexagon abstractly on the board at the corresponding position and adapt board attributes
            self.board.board[draw_hexagon.board_pos[0]][draw_hexagon.board_pos[1]] = draw_hexagon
            self.board.nonempty_fields.append(draw_hexagon.board_pos)
            self.board.drawn_hexagons.append(draw_hexagon)
            #set is_on_board
            draw_hexagon.is_on_board = True
            
            ##then excute drawing aspects
            self.draw_new_stone_number(str(player.side_stones_numbers[stone_type]), stone_type, player)
            self.painter.draw_hexagon(draw_hexagon, self.game_surface)
            #self.painter.draw_hexagon_marking(shex, (50,50,50), max((player.stone_size//20),1))
            self.painter.draw_hexagon_frame(shex, (50,50,50), player.stone_size // 15)
    
    #player want to put src_hstone on dir_stone. is that a legal ?
    def put_stone_condition(self, player, src_hstone, dir_hstone):
        coord = dir_hstone.board_pos
        
        #there are still stones of the src_hstone type left at the side
        cond0 = player.side_stones_numbers[src_hstone.type] != 0
        if not cond0:
            print("cond0 nicht erfüllt")
        #stone belongs to player
        cond1 = src_hstone.color == player.color 
        if not cond1:
            print("cond1 nicht erfüllt")
        #field at coord is empty
        cond3 = self.board.board[coord[0]][coord[1]].is_empty 
        if not cond3:
            print("cond3 nicht erfüllt")
        #at least one same color neighbour, no other color neighbour.
        #watch the cases, that no or just one stone is on the board
        cond4 = False
        neighbours = self.board.get_neighbours(coord).values()
        if len(self.board.nonempty_fields) == 0:
            cond4 = True
        elif len(self.board.nonempty_fields) == 1:
            cond4 = coord in neighbours
        else:
            for neigh in neighbours:
                field = self.board.board[neigh[0]][neigh[1]]
                if not field.is_empty:
                    if field.color != src_hstone.color:
                        cond4 = False
                        break
                    else:
                        cond4 = True
        if not cond4:
            print("cond4 nicht erfüllt")
        #bee has been put until 4. stoneput
        cond5 = True
        if self.turn[1] == 4 and not player.stones["bee"].values()[0].is_on_board:
            cond5 = src_hstone.type == "bee"
        if not cond5:
            print("cond5 nicht erfüllt")
        return cond0 and cond1 and cond3  and cond4 and cond5
    
    
    
    #this function evaluates and executes a potential stone move. input is the player and both clicked hexagons, 
    #first the hexagon where a stone wants to be moved, second the hexagon the stone wants to be moved to
    def execute_stone_move(self, player, fhex, shex):
        
        cond1 = self.move_stone_condition(player, fhex, shex)
        cond2 = shex.board_pos in self.calculator.get_possible_move_fields(fhex)
        if cond1 and cond2: 
            
            old_board_pos = fhex.board_pos
            old_pixel_pos = fhex.pixel_pos
            fhex.set_board_pos(shex.board_pos)
            fhex.set_pixel_pos(shex.pixel_pos)
            
            #refill "old" place with empty stone
            new_empty_stone = self.board.empty_board[old_board_pos[0]][old_board_pos[1]]
            self.board.board[old_board_pos[0]][old_board_pos[1]] = new_empty_stone
            new_empty_stone.set_pixel_pos(old_pixel_pos)
            
            #fill "new" place with fhex
            self.board.board[fhex.board_pos[0]][fhex.board_pos[1]] = fhex
            
            #actualize board.nonempty_fields
            self.board.nonempty_fields.append(fhex.board_pos)
            self.board.nonempty_fields.remove(old_board_pos)
            
            self.painter.draw_hexagon(new_empty_stone, self.game_surface)
            self.painter.draw_hexagon(fhex, self.game_surface)
            
    
    #player wants to move fhex to shex. is that generally possible ? that means independently of 
    #the stone type ? note that this game is yet without the "assel" stone    
    def move_stone_condition(self, player, fhex, shex):
        #different board_pos
        cond00 = fhex.board_pos != shex.board_pos
        #bee is on board
        cond0 = list(player.stones["bee"].values())[0].is_on_board
        #stone belongs to player
        cond1 = fhex.color == player.color
        #stone is on board
        cond2 = fhex.is_on_board
        #coord is empty (just for stone.type != "bug")
        cond3 = True
        if fhex.type != "bug":
            cond3 = shex.is_empty 
        #boardstones are connected after taking away stone
        nonempty_fields = self.board.nonempty_fields.copy()
        nonempty_fields.remove(fhex.board_pos) 
        cond4 = self.board.is_connected(nonempty_fields)
        return cond00 and cond0 and cond1 and cond2 and cond3 and cond4
            
    
    ###### shall be in painter
    #HAS TO BE ADAPTED, should use painter to draw       
    def write_text(self, surface, text, text_color, length, height, x, y):
        font_size = 2*int(length//len(text))
        myFont = pygame.font.SysFont("Calibri", font_size)
        myText = myFont.render(text, 1, text_color)
        surface.blit(myText, ((x+length/2) - myText.get_width()/2, (y+height/2) - myText.get_height()/2))
        return surface
    
    #draw side_numbers at corresponding position depending on insect_type
    def draw_new_stone_number0(self, text, insect_type, player, text_color = (0,0,0)):
        stone_size = player.stone_size
        height_rect = 1.5 * pygame.font.SysFont("Arial", stone_size).render("1", 1, text_color).get_height()
        width = 1.3 * pygame.font.SysFont("Arial", stone_size).render("1", 1, text_color).get_width()
        position = (player.side_stones[insect_type].pixel_pos[0] + 1.5 * stone_size + 5,
                  int(player.side_stones[insect_type].pixel_pos[1] + sqrt(3) * 0.5 * stone_size - 0.5 * height_rect))
        rect_subsurface = self.surface.subsurface(pygame.Rect(position, (width, height_rect)))
        rect_subsurface.fill(self.surface.get_at_mapped((1,1)))       
        height_text = pygame.font.SysFont("Arial", stone_size).render("1", 1, (0,0,0)).get_height()
        self.painter.write_text(rect_subsurface, str(player.side_stones_numbers[insect_type]), stone_size, (0,0,0), (5, 0.5 * (height_rect - height_text)))

    def draw_new_stone_number(self, text, insect_type, player, text_color = (0,0,0)):
        stone_size = player.stone_size
        text_size = int (1.2 * stone_size)
        test_font = pygame.font.SysFont("Arial", text_size)
        (width, height) = test_font.size("0")
        
        position =  (int(player.side_stones[insect_type].pixel_pos[0] - 13 * stone_size / 18 - width),
                         int(player.side_stones[insect_type].pixel_pos[1] + sqrt(3) * 0.5 * stone_size - 0.5 * height))
        
        rect_subsurface = self.surface.subsurface(pygame.Rect(position, (width, height)))
        rect_subsurface.fill(self.surface.get_at_mapped((1,1)))
        
        self.painter.write_text(rect_subsurface, str(player.side_stones_numbers[insect_type]),
                                text_size, (0,0,0), (0,0) )












# ending