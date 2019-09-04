import pygame
import hexagon_stone as hs
pygame.init()


class Interactor:
    def __init__(self, painter, calculator):
        self.painter = painter
        self.calculator = calculator
        self.players = self.calculator.locator.players
        self.board = self.calculator.board
        self.surface = self.painter.surface
    
    #NOT COMPLETE, 
    #this function evaluates and executes a potential stone put. input is the player and both clicked hexagons, 
    #first the hexagon at the side, second a hexagon on the board   
    def execute_stone_put(self, player, first_clicked_hex, second_clicked_hex):
        fhex = first_clicked_hex
        shex = second_clicked_hex
        cond1 = self.put_stone_condition(player, fhex.stone, shex.board_position)
        cond2 = shex.board_position in self.get_possible_put_hexagons(fhex.color)
        if cond1 and cond2:
            stone_type = fhex.stone.type

    
    #player want to put stone on coord. is that a legal move ?
    def put_stone_condition(self, player, stone, coord):
        #stone belongs to player
        cond1 = stone.color == player.color 
        #stone is not on board
        cond2 = not stone.is_on_board 
        #field at coord is empty
        cond3 = self.board.board[coord[0]][coord[1]].is_empty 
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
                    if field.stone.color != stone.color:
                        cond4 = False
                        break
                    else:
                        cond4 = True
        #bee has been put until 4. stoneput
        cond5 = True
        if len(self.board.nonempty_fields) in {6,7} and not player.stones["bee"].is_on_board:
            cond5 = stone.type == "bee"
        return cond1 and cond2 and cond3  and cond4 and cond5
    
    #player want to move stone to coord. is that generally possible ? that means independently of 
    #the stone type ? note that this game is yet without the "assel" stone    
    def move_stone_condition(self, player, stone, coord):
        #stone.coordinate != coord, tm the board has to change with the move
        cond00 = stone.coordinate != coord
        #bee is on board
        cond0 = player.stones["bee"].is_on_board
        #stone belongs to player
        cond1 = stone.color == player.color
        #stone is on board
        cond2 = stone.is_on_board
        #coord is empty (just for stone.type != "bug")
        cond3 = True
        if stone.type != "bug":
            cond3 = self.board.board[coord[0]][coord[1]].is_empty 
        #boardstones are connected after taking away stone
        nonempty_fields = self.board.nonempty_fields.copy()
        cond4 = self.board.is_connected(nonempty_fields.remove(stone.coordinate))
        return cond00 and cond0 and cond1 and cond2 and cond3 and cond4
            
    #HAS TO BE ADAPTED
    #player puts stone on coord (if possible)
    def put_stone(self, player, stone, coord):
        if  not self.put_stone_condition(player, stone, coord):
            print("stoneput not possible") #ADD surface print etc #######################################
        else:
            self.board[coord[0]][coord[1]].put_stone(stone) #first put stone on hexagon
            self.draw_hexagon(self.board[coord[0]][coord[1]]) #then draw hexagon on surface
            stone.is_on_board = True
            self.board.nonempty_fields.append(coord)
    
    #HAS TO BE ADAPTED
    #move stone of player to coord (if possible)       
    def move_stone(self, player, stone, coord):
        def move(stone, coord):
            self.board.board[stone.coordinate[0]][stone.coordinate[1]].remove_stone(stone)
            self.board.board[coord[0]][coord[1]].put_stone(stone)
        
        if not self.move_stone_condition(player, stone, coord):
            print("stone move not possible")
        else:
            if stone.type == "bee":
                if coord in self.board_subset.get_bee_fields(coord): move(stone, coord)
                else: print("bee move not possible")
            elif stone.type == "ant":
                if coord in self.board_subset.get_ant_fields(coord): move(stone, coord)
                else: print("ant move not possible")
            elif stone.type == "hopper":
                if coord in self.board_subset.get_hopper_fields(coord): move(stone, coord)
                else: print("hopper move not possible")
            elif stone.type == "spider":
                if coord in self.board_subset.get_spider_fields(coord): move(stone, coord)
                else: print("spider move not possible")
            elif stone.type == "bug":
                if coord in self.board_subset.get_bug_fields(coord): move(stone, coord)
                else: print("bug move not possible") 
                    
    #NOT COMPLETE, 
    #this function evaluates and executes a potential stone move. input is the player and both clicked hexagons, 
    #first the hexagon where a stone wants to be moved, second the hexagon the stone wants to be moved to
    def execute_stone_move(self, player, first_clicked_hexagon, second_clicked_hexagon):
        cond1 = self.move_stone_condition(player, first_clicked_hexagon.stone, second_clicked_hexagon.board_position)
        cond2 = second_clicked_hexagon in self.get_possible_move_hexagons(first_clicked_hexagon)
        if cond1 and cond2: #############################################INCOMPLETE
            first_hexagon = first_clicked_hexagon
            second_hexagon = second_clicked_hexagon
            
            old_position = first_hexagon.pixel_position
            first_hexagon.pixel_position = second_hexagon.pixel_position
            #if not bug:
            self.board.board[first_hexagon.board_position[0]][first_hexagon.board_position[1]].change_stone(hs.Stone("empty",1))
            self.board.board[second_hexagon.board_position[0]][second_hexagon.board_position[1]].change_stone(first_hexagon.stone)
            
            self.draw_insect_image(first_hexagon)
            #if not bug:
            self.draw_empty_hexagon(old_position)
        else:
            print("not possible") ##############################################print in surface
        
   
    def print_text_for_player(self):
        pass
            
    def write_text(surface, text, text_color, length, height, x, y):
        font_size = 2*int(length//len(text))
        myFont = pygame.font.SysFont("Calibri", font_size)
        myText = myFont.render(text, 1, text_color)
        surface.blit(myText, ((x+length/2) - myText.get_width()/2, (y+height/2) - myText.get_height()/2))
        return surface

    def draw_number_text(surface, text_color, text):
        pass
            
            
        
    #clicked_hexagon was clicked. return list of all possible hexagons to move
    def get_possible_move_hexagons(self, clicked_hexagon):
        return self.calculator.get_possible_fields(clicked_hexagon.coordinate, clicked_hexagon.stone.type)
    
    #clicked_hexagon was clicked (side stone). return list of all possible hexagons on the board to put this hexagon
    def get_possible_put_hexagons(self, clicked_hexagon):
        self.calculator.get_possible_put_fields(clicked_hexagon.stone.color)
    
    #which hexagon was clicked ? return is a hexagon pertaining to one of the players (no empty hexagon)
    def get_clicked_hexagon(self, event_pos):
        for player in self.players.values():
            for hstone in player.side_stones.values():
                if hstone.point_in_hexagon(event_pos) == True:
                    return [hstone]
            for hstone in player.stones.values():
                if hstone.point_in_hexagon(event_pos) == True and hstone.is_drawn:
                    return [hstone]
        return []

















