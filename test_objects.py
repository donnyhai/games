import board
import player

class Test_Board(board.Board):
    
    def copy_board(self, board): 
        #note: only .copy() is not enough for eg the board, as the hexagons in the board dont get copied
        #copy board matrix, such that hexagons in the matrix get copied too:
        def copy_board_matrix(board_matrix):
            copied_board_matrix = [0] * board.size
            for k in copied_board_matrix:
                k = []
                for hexagon in board_matrix[k]:
                    k.append(hexagon.copy())
        
        self.board = copy_board_matrix(board.board)
        self.empty_board = copy_board_matrix(board.empty_board)
        self.nonempty_fields = board.nonempty_fields.copy()
        
    #this function evaluates and executes a stone move on the test board. input are two hexagons.
    #there are no conditions for the move, the testboard can just move a stone (conditions have to be
    #applied elsewhere)
    def move_stone(self, fhex, shex):
        
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
            
    
    
class Test_Player(player.Player):
    pass

