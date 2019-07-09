
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
    

#get empty fields of the board, enter empty_type "extern", "outer" or "inner"
    #"extern" means empty fields with number of nonempty neighbours in {0}
    #"outer" means empty fields with number of nonempty neighbours in {1,2,3,4}
    #"inner" means empty fields with number of nonempty neighbours in {5,6}
    def get_empty_fields(self, empty_type):
        #set possible numbers for nonempty neighbours according to empty_type
        if empty_type == "extern":
            numbers_nonempty_neigh = {0}
        elif empty_type == "outer":
            numbers_nonempty_neigh = {1,2,3,4}
        elif empty_type == "inner":
            numbers_nonempty_neigh = {5,6}
        else:
            print("no such empty_type")
        #find respective empty fields 
        indexset = {}
        for row in self.board:
            for field in row:
                coord = field.coordinate
                neigh = set(self.get_neighbours(coord[0], coord[1]).values())
                if field.is_empty and len(neigh.intersection(self.nonempty_fields)) in numbers_nonempty_neigh:
                    indexset.append(coord)
        return indexset
















        