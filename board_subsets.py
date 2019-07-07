

class Board_subset:
    def __init__(self, board, locator):
        self.board = board
        self.size = self.board.size
        #matrix has the sime size as board, is 1 in i,j iff we consider this field to be part 
        #of the set of fields we want to include at the moment (initialized with all fields, therefore all 1)
        self.matrix = self.all_fields()
        
    def all_fields(self):
        return [[1] * self.size for i in range(self.size)]
    
    
    #ant is on coordinate. where can it move ?
    def ant_move_fields(self, coord):
        pass
    
   
        


















        