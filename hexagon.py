import stone

class Hexagon:
    def __init__(self, position, size):
        #surface attributes
        self.surface_position = position #position on the surface
        self.size = size
        self.points = self.calculate_hexagon_points(self.surface_position, self.size)
        self.is_drawed = False
        #board attributes
        self.stone = stone.Stone("empty", 0)
        self.is_empty = True
        self.coordinate = (-1,-1)
    
    def put_stone(self, stone):
        self.stone = stone
        self.is_empty = False
        stone.coordinate = self.coordinate
    def remove_stone(self, stone):
        stone.coordinate = (-1,-1)
        self.is_empty = True
        self.stone = stone("empty", 0)
    
    #the board coordinate is the "matrix" coordinate on the board, compare with Board object    
    def set_board_coordinate(self, coord):
        self.board_coord = coord
    
    #calculate the six hexagon points with starting point start_vector (point top left) and side size scaling
    def calculate_hexagon_points(self, start_vector, scaling):    
        hex_coords = [(0,0), (1,0), (1.5, 3**(1/2)/2), (1, 3**(1/2)), (0,3**(1/2)), (-0.5, 3**(1/2)/2)]
        scaled_coords = []
        for x,y in hex_coords:
            scaled_coords.append((x*scaling + start_vector[0], y*scaling + start_vector[1]))
        return scaled_coords
    
    #is point in this hexagon ?        
    def point_is_in_hexagon(self, point):
        
        def euclidean_metric(vector):
            squared = [x*x for x in vector]
            return sum(squared)**(1/2)
        
        boundary_vectors = []
        connection_vectors = []
        for i in range(len(self.points)):
            boundary_vectors.append((self.points[(i+1)%len(self.points)][0]-self.points[i][0],self.points[(i+1)%len(self.points)][1]-self.points[i][1]))
            connection_vectors.append((point[0]-self.points[i][0], point[1]-self.points[i][1]))
        test = True
        angles = []
        for i in range(len(self.points)):
            angles.append((boundary_vectors[i][0]*connection_vectors[i][0]+boundary_vectors[i][1]*connection_vectors[i][1])
                          /(euclidean_metric(boundary_vectors[i])*euclidean_metric(connection_vectors[i])))
            if angles[i] <= -0.5:
                test = False
        return test