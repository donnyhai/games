import board
import player
import hexagon_stone as hs
import copy

class Test_Board(board.Board):
    
    #aim is to copy the board matrix of an board object, and also make copies of all hexagons inside the matrix
    #use copy_hexagon. input is an board object
    def copy_board(self, board): 
        
        #input is a matrix (list of lists)
        def copy_board_matrix(board_matrix):
            copied_board = {}
            for hstone in board_matrix.values():
                hexagon_copy = hs.hexagon_stone(hstone.size)
                hexagon_copy.copy_hexagon(hstone)
                copied_board[hstone.board_pos] = hexagon_copy
            return copied_board
        
        self.board = copy_board_matrix(board.board)
        self.nonempty_fields = board.nonempty_fields.copy()
        
    def copy_board2(self, board):
        return copy.deepcopy(board)
        
class Test_Player(player.Player):
    pass

