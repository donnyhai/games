import hexagon_stone as hs

class Board:
    def __init__(self, board_size, surface):
        self.size = board_size
        self.surface = surface
        self.hexagon_size = int(0.03 * self.surface.get_width()*5/4)
        self.draw_position = (0,0) #where on the surface shall the hexagon matrix be drawn ? 
        #(reference point is upper left corner of upper left hexagon)
        self.board = self.calculate_hexagon_board() #quadratic matrix of hexagons
        self.nonempty_fields = [] #will matrix contain coordinates
        self.drawed_hexagons = [] #will contain hexagon_stone objects (if used)
        
    
    #get neighbour coordinates of (i,j) starting from top going clockwise, number them from 0 to 5
    def get_neighbours(self, coord):
        i = coord[0]
        j = coord[1]
        return {0: (i-2,j), 1: (i-1,j+1), 2: (i+1,j+1), 3: (i+2,j), 4: (i+1,j), 5: (i-1,j)} 
    
    #create a quadratic board of hexagons as a matrix of hexagon objects with respective correct positions    
    def calculate_hexagon_board(self):
        
        #function to create a horizontal connected chain of hexagons, return is a list
        def create_horizontal_hexagon_chain(start_position):
            hexagon_chain = []
            for i in range (self.size):
                position = (start_position[0] + i * 3 * self.hexagon_size, start_position[1])
                hexagon_chain.append(hs.hexagon_stone(self.hexagon_size, self.surface, pixel_position = position))
            return hexagon_chain
        
        hexagon_board = [0] * self.size
        even_numbers = [i for i in range(self.size) if i % 2 == 0]
        odd_numbers = [i for i in range(self.size) if i % 2 == 1]
        
        #fill hexagon_board with the correct horizontal chains, first even than odd rows
        for i in even_numbers:
            position = (self.draw_position[0], self.draw_position[1] + i/2 * 3**(1/2) * self.hexagon_size)
            hexagon_board[i] = create_horizontal_hexagon_chain(position)
        for i in odd_numbers:
            start_position = (self.draw_position[0] + 3/2 * self.hexagon_size, self.draw_position[1] + 3**(1/2)/2 * self.hexagon_size)
            position = (start_position[0], start_position[1] + (i-1)/2 * 3**(1/2) * self.hexagon_size)
            hexagon_board[i] = create_horizontal_hexagon_chain(position)
            
        #set board coordinates for each hexagon
        for i in range(self.size):
            for j in range(self.size):
                hexagon_board[i][j].stone.coordinate = (i,j)
                
        return hexagon_board
    
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
    
