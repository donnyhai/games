
#Note, that some of the following are field sets in general, others depend on a given field coordinate


class Field_sets:
    def __init__(self, board):
        self.board = board
        self.size = self.board.size
        #matrix has the sime size as board, is 1 in i,j iff we consider this field to be part 
        #of the set of fields we want to include at the moment (initialized with all fields, therefore all 1)
        self.matrix = self.all_fields()
        
    def all_fields(self):
        return [[1] * self.size for i in range(self.size)]
    
   
        

class Nonempty_fields(All_fields):
    def __init__(self):
        super().__init__(self)
        self.matrix = self.calculate_matrix()
    def calculate_matrix(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j].is_empty:
                    self.matrix[i][j] = 0
            
class Empty_fields(Nonempty_fields):
    def __init__(self):
        super().__init__(self)
        self.matrix = self.calculate_matrix()
    def calculate_matrix(self):
        #make zeros to ones and ones to zeros (complementary to nonemtpy_fields)
        return [[(self.matrix[i][j] + 1) % 2 for i in range(self.size)] for j in range(self.size)]
    
class Hopper_fields(All_fields):
    def __init__(self, coordinate):
        super().__init__(self)
        self.matrix = self.calculate_matrix()
    def calculate_matrix(self):
        pass
    


















        