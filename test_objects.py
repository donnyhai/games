import board
import player



class Test_Board(board.Board):
    
    def copy_board(self, board):
        self.board = board.board.copy()
        self.nonempty_fields = board.nonempty_fields.copy()
        
    #Note, the move_stone_condition and move_stone is different as in Board (less restrictive, 
    #to allow easier test moves)
    def move_stone_condition(self, stone, coord):
        #stone is on board
        cond2 = stone.is_on_board
        #i,j is empty
        cond3 = self.board[coord[0]][coord[1]].is_empty 
        #boardstones are connected after taking away stone
        nonempty_fields = self.nonempty_fields.copy()
        cond4 = self.is_connected(nonempty_fields.remove(stone.coordinate))
        return cond2 and cond3 and cond4
    
    def move_stone(self, stone, coord):
        if self.move_stone_condition(stone, coord):
            self.board[stone.coordinate[0]][stone.coordinate[1]].remove_stone(stone)
            self.board[coord[0]][coord[1]].put_stone(stone)



class Test_Player(player.Player):
    pass

