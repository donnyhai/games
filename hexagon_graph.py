
#note that this graph objects gets the board matrix as input, and depending on the situation get set
#his points and edges
class Hexagon_Graph:
    def __init__(self, board):
        self.board = board #board object

    
    def set_points(self, points):
        self.points = points
        #help structure for depth first search algorithm
        self.markings = [0] * len(self.points) 
        
    def set_edges(self, edges):
        self.edges = edges
    
    #here points should be nonempty_fields of board, and edges will contain to nonempty fields, if they are neighbours 
    def calculate_standard_edges(self):
        edges = []
        for point in self.points:
            for point2 in self.points:
                if point in self.board.get_neighbours(point2).values():
                    edges.append((point, point2))
        return edges
    
    #for a point in the graph calculate all connected neighbours                
    def get_graph_neighbours(self, point):
        graph_neighbours = []
        for point2 in self.points:
            if (point, point2) in self.edges:
                graph_neighbours.append(point2)
        return graph_neighbours
    
    #algorithm depth-first search to check connectedness of the graph (see internet)
    def depth_first_search(self, point):
        self.markings[self.points.index(point)] = 1
        relevant_points = [point2 for point2 in self.get_graph_neighbours(point) if self.markings[self.points.index(point2)] == 0]
        for point2 in relevant_points:
            self.depth_first_search(point2)
    
    #check whether the graph is connected        
    def is_connected(self):
        self.markings = [0] * len(self.points) #reset markings
        self.depth_first_search(self.points[0]) #run algo
#        if self.markings.count(1) == len(self.points):
#            return True
#        else: return False
        
        #check markings. all points are marked iff graph is connected
        try:
            self.markings.index(0)
            return False
        except ValueError:
            return True
        
                
        
    