import field

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[field.Field() for i in range(self.size)] for j in range(self.size)]
        self.set_fields_coordinates()
        self.nonempty_fields = [] #will contain coordinates
    
    #set coordinates for field objects on the board
    def set_fields_coordinates(self):
        {self.board[i][j].set_coordinate((i,j)) for i in range(self.size) for j in range(self.size)}
    
    #get neighbour coordinates of (i,j) starting from top going clockwise, number them from 0 to 5
    def get_neighbours(self, coord):
        i = coord[0]
        j = coord[1]
        return {0: (i-1,j), 1: (i-1,j+1), 2: (i,j+1), 3: (i+1,j+1), 4: (i+1,j), 5: (i,j-1)} 
    
    #check if coord is part of the board (if board is big enough and game starts in the middle, 
    #this function should not be necessary in a human two-player game)
    def is_inside(self, coord):
        pass
    
    #check, whether indexset is connected
    def is_connected(self, indexset):
        if len(indexset) in {0,1}:
            return True
        else:
            for i,j in indexset:
                if len(indexset.intersection(self.get_neighbours(i,j).values())) == 0:
                    return False
            return True
    
