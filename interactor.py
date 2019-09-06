import pygame
import hexagon_stone as hs
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
            #set new position for the stone which wants to be drawn
            draw_hexagon.set_pixel_pos(shex.pixel_pos)
            #set new board_position
            new_board_pos = shex.board_pos
            draw_hexagon.board_pos = new_board_pos
            #put the hexagon abstractly on the board at the corresponding position and adapt board attributes
            self.board.board[new_board_pos[0]][new_board_pos[1]] = draw_hexagon
            self.board.nonempty_fields.append(new_board_pos)
            self.board.drawn_hexagons.append(draw_hexagon)
            #set is_on_board
            draw_hexagon.is_on_board = True
            
            ##then excute drawing aspects
            self.draw_new_stone_number0(str(player.side_stones_numbers[stone_type]), stone_type, player)
            self.painter.draw_hexagon(draw_hexagon, self.game_surface)
    
    
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
    #NOTE: this method shall work with board.empty_board. when a stone get moved, put the empty stone
    #on the position where the moved stone was. this empty stone shall be taken out of empty_board, which consists
    #of the init matrix of empty stones when board was init
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
        
    ###### shall be in painter
    #HAS TO BE ADAPTED, should use painter to draw       
    def write_text(self, surface, text, text_color, length, height, x, y):
        font_size = 2*int(length//len(text))
        myFont = pygame.font.SysFont("Calibri", font_size)
        myText = myFont.render(text, 1, text_color)
        surface.blit(myText, ((x+length/2) - myText.get_width()/2, (y+height/2) - myText.get_height()/2))
        return surface
    
    #draw side_numbers at corresponding position depending on insect_type
    def draw_new_stone_number(self, text, insect_type, player, text_color = (0,0,0)):
        stone_size = player.stone_size
        height_rect = 1.5 * pygame.font.SysFont("Arial", stone_size).render("1", 1, text_color).get_height()
        width = 1.3 * pygame.font.SysFont("Arial", stone_size).render("1", 1, text_color).get_width()
        position = (player.side_stones[insect_type].pixel_pos[0] + 1.5 * stone_size + 5,
                  int(player.side_stones[insect_type].pixel_pos[1] + sqrt(3) * 0.5 * stone_size - 0.5 * height_rect))
        rect_subsurface = self.surface.subsurface(pygame.Rect(position, (width, height_rect)))
        rect_subsurface.fill(self.surface.get_at_mapped((1,1)))       
        height_text = pygame.font.SysFont("Arial", stone_size).render("1", 1, (0,0,0)).get_height()
        self.painter.write_text(rect_subsurface, str(player.side_stones_numbers[insect_type]), stone_size, (0,0,0), (5, 0.5 * (height_rect - height_text)))

    def draw_new_stone_number0 (self, text, insect_type, player, text_color = (0,0,0)):
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