import pygame
import texts as t
pygame.init()


class Interactor:
    def __init__(self, painter, calculator, turn):
        self.painter = painter
        self.calculator = calculator
        self.players = self.calculator.players
        self.board = self.calculator.board
        self.surfaces = self.board.surfaces
        self.turn = turn
    
    #this function evaluates and executes a potential stone put. input is the player and both clicked hexagons, 
    #first the hexagon at the side, second a hexagon on the board   
    def execute_stone_put(self, player, fhex, shex):
        cond1, cond2 = True, True
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
            
            ##then execute drawing aspects
            self.painter.draw_stone_number(player, fhex, self.surfaces)
            self.painter.draw_hexagon(draw_hexagon, self.surfaces["surface_board"])
            #self.painter.draw_hexagon_marking(shex, (50,50,50), max((player.stone_size//20),1))
            self.painter.draw_hexagon_frame(shex, (50,50,50), player.stone_size // 15)
            self.painter.write_box_text(self.surfaces, t.insect_put_texts[fhex.type], fhex.color)
    
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
    
    
    
    #this function evaluates and executes a potential stone move on ground. input is the player and both clicked hexagons, 
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
            
            self.painter.draw_board(self.board, self.surfaces["surface_board"])
            
            #write texts
            self.painter.write_box_text(self.surfaces, t.insect_move_texts[fhex.type], fhex.color)
            
    
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
        if not fhex.type in {"bug", "mosquito"}:
            cond3 = shex.is_empty 
        return cond00 and cond0 and cond1 and cond2 and cond3
    
    

    #player wants to move the bug fhex onto a nonempty stone shex, or bug is already on a nonempty stone
    #and wants to fall down onto an empty field
    def move_bug_on_nonempty_stone(self, player, fhex, shex):
        
        cond1 = self.move_stone_condition(player, fhex, shex)
        cond2 = shex.board_pos in self.calculator.get_possible_move_fields(fhex)
        if cond1 and cond2: 
            
            old_board_pos = fhex.board_pos
            old_pixel_pos = fhex.pixel_pos
            fhex.set_board_pos(shex.board_pos)
            fhex.set_pixel_pos(shex.pixel_pos)
            
            if fhex.underlaying_stones: #case: fhex sits on at least one stone
                #get stone which lies directly under the bug
                last_stone = fhex.underlaying_stones[-1]
                fhex.underlaying_stones.clear()
                #define new stones under the bug
                if shex.type == "bug":
                    fhex.underlaying_stones = shex.underlaying_stones.copy()
                if not shex.is_empty:
                    fhex.underlaying_stones.append(shex)
                    shex.has_bug_on = True
                if shex.is_empty:
                    self.board.nonempty_fields.append(fhex.board_pos)
                last_stone.has_bug_on = False
                #check whether fhex is mosquito. if it is and shex.is_empty then reput "mosquito" type
                if fhex.is_mosquito and shex.is_empty: fhex.type = "mosquito"
                #refill old place with last_stone and new place with fhex
                self.board.board[old_board_pos[0]][old_board_pos[1]] = last_stone
                self.board.board[fhex.board_pos[0]][fhex.board_pos[1]] = fhex
                #no adaptation for nonempty_fields needed
                #draw last_stone and fhex 
                self.painter.draw_hexagon(last_stone, self.surfaces["surface_board"])
                self.painter.draw_hexagon(fhex, self.surfaces["surface_board"])
            else: #case: bug will certainly move from an empty field onto a nonempty field
                fhex.underlaying_stones.append(shex)
                shex.has_bug_on = True
                #check mosquito.
                if fhex.is_mosquito: fhex.type = "bug"
                #refill "old" place with empty stone
                new_empty_stone = self.board.empty_board[old_board_pos[0]][old_board_pos[1]]
                self.board.board[old_board_pos[0]][old_board_pos[1]] = new_empty_stone
                new_empty_stone.set_pixel_pos(old_pixel_pos)
                
                #fill "new" place with fhex
                self.board.board[fhex.board_pos[0]][fhex.board_pos[1]] = fhex
                
                #actualize board.nonempty_fields
                self.board.nonempty_fields.remove(old_board_pos)
                
                self.painter.draw_hexagon(new_empty_stone, self.surfaces["surface_board"])
                self.painter.draw_hexagon(fhex, self.surfaces["surface_board"])










# ending