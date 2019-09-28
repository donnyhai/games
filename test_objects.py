import board
import player
import hexagon_stone as hs

class Test_Board(board.Board):
    
    
    #aim is to copy the board matrix of an board object, and also make copies of all hexagons inside the matrix
    #use copy_hexagon. input is an board object
    def copy_board(self, board): 
        
        #input is a matrix (list of lists)
        def copy_board_matrix(board_matrix):
            copied_board_matrix = [0] * board.size
            for k in range(board.size):
                new_row = []
                for hexagon in board_matrix[k]:
                    hexagon_copy = hs.hexagon_stone(hexagon.size)
                    hexagon_copy.copy_hexagon(hexagon)
                    new_row.append(hexagon_copy)
                copied_board_matrix[k] = new_row
            return copied_board_matrix
        
        self.board = copy_board_matrix(board.board)
        self.nonempty_fields = board.nonempty_fields.copy()

#NOTE: you can find this function in hexagon_stone (similar)    
#    #aim is to copy a hexagon, means here to make a new hexagon with new id but same attributes     
#    def copy_hexagon(self, hexagon):
#        hexagon_copy = hs.hexagon_stone(hexagon.size)
#        for attr in list(hexagon.__dict__.keys()):
#            hexagon_copy.__dict__[attr] = hexagon.__dict__[attr]
#        return hexagon_copy
        
    #this function evaluates and executes a stone move on the test board. input are two hexagons.
    #there are no conditions for the move, the testboard can just move a stone (conditions have to be
    #applied elsewhere)
    def move_stone(self, fhex, shex):
        
        old_board_pos = fhex.board_pos
        old_pixel_pos = fhex.pixel_pos
        fhex.set_board_pos(shex.board_pos)
        fhex.set_pixel_pos(shex.pixel_pos)
        
        #refill "old" place with empty stone
        new_empty_stone = self.empty_board[old_board_pos[0]][old_board_pos[1]]
        self.board[old_board_pos[0]][old_board_pos[1]] = new_empty_stone
        new_empty_stone.set_pixel_pos(old_pixel_pos)
        
        #fill "new" place with fhex
        self.board[fhex.board_pos[0]][fhex.board_pos[1]] = fhex
            
    
    
class Test_Player(player.Player):
    pass

