import hexagon_stone as hs

class Board:
    def __init__(self, board_size, surfaces):
        self.size = board_size
        self.surfaces = surfaces
        self.hexagon_size = int(0.03 * self.surfaces["surface_full"].get_width())
        self.draw_position = (0, -self.hexagon_size) #where on the surface shall the hexagon matrix be drawn ? 
        #(reference point is upper left corner of upper left hexagon)
        
        self.board = self.calculate_empty_hexagon_board() #quadratic matrix of hexagons
        self.empty_board = self.calculate_empty_hexagon_board() #save matrix with empty hexagons, for later using them to make a field
        #empty again, for example when a stone moves from that field away
        self.set_board_hexagons_positions(self.board, self.draw_position)
        self.set_board_hexagons_positions(self.empty_board, self.draw_position)
        
        self.nonempty_fields = [] #will contain matrix coordinates
        self.drawn_hexagons = [] #will contain hexagon_stone objects (if used)
        
    
    #get neighbour coordinates of (i,j) starting from top going clockwise, number them from 0 to 5
    def get_neighbours(self, coord):
        i = coord[0]
        j = coord[1]
        if i % 2 == 1:
            return {0: (i-2,j), 1: (i-1,j+1), 2: (i+1,j+1), 3: (i+2,j), 4: (i+1,j), 5: (i-1,j)} 
        else:
            return {0: (i-2,j), 1: (i-1,j), 2: (i+1,j), 3: (i+2,j), 4: (i+1,j-1), 5: (i-1,j-1)} 
    
    def get_nonempty_neighbours (self, coord):
        nonempty_neigh = []
        for neigh in self.get_neighbours(coord).values():
            if not self.board[neigh[0]][neigh[1]].is_empty: nonempty_neigh.append(neigh)
        return nonempty_neigh
    
    def get_empty_neighbours(self, coord):
        return [neigh for neigh in self.get_neighbours(coord).values() if neigh not in self.get_nonempty_neighbours(coord)]
    
    #create a quadratic board of hexagons as a matrix of hexagon objects with respective correct positions    
    def calculate_empty_hexagon_board(self):
        def create_hexagon_row():
            hexagon_chain = []
            for i in range (self.size): hexagon_chain.append(hs.hexagon_stone(self.hexagon_size))
            return hexagon_chain
        hexagon_board = []
        for i in range(self.size):  hexagon_board.append(create_hexagon_row())
        #set board coordinates for each hexagon
        for i in range(self.size):
            for j in range(self.size):  hexagon_board[i][j].set_board_pos((i,j))
        return hexagon_board
    
    
    def set_board_hexagons_positions(self, board, draw_position):
        even_numbers = [i for i in range(self.size) if i % 2 == 0]
        odd_numbers = [i for i in range(self.size) if i % 2 == 1]
        for i in even_numbers:
            position = (draw_position[0], draw_position[1] + i/2 * 3**(1/2) * self.hexagon_size)
            for k in range(self.size):
                board[i][k].set_pixel_pos((position[0] + k * 3 * self.hexagon_size, position[1]))
        for i in odd_numbers:
            start_position = (draw_position[0] + 3/2 * self.hexagon_size, draw_position[1] + 3**(1/2)/2 * self.hexagon_size)
            position = (start_position[0], start_position[1] + (i-1)/2 * 3**(1/2) * self.hexagon_size)
            for k in range(self.size):
                board[i][k].set_pixel_pos((position[0] + k * 3 * self.hexagon_size, position[1]))
    
    #board pixel size wants to be adapted with this function. multiply ratio with stone_size
    def scale_board(self, ratio):
        for row in self.board:
            for hstone in row:
                hstone.size = int(ratio * hstone.size)
        self.hexagon_size = int(ratio * self.hexagon_size)
        self.set_board_hexagons_positions(self.board, self.board[0][0].pixel_pos)
        self.draw_position = self.board[0][0].pixel_pos
        
    
    
    def add_hexagons_pos_offset(self, offset):
        for row in self.board:
            for hstone in row:
                hstone.set_pixel_pos((hstone.pixel_pos[0] + offset[0], hstone.pixel_pos[1] + offset[1]))
    
    

