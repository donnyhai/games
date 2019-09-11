
#note that this graph objects gets the board matrix as input, and depending on the situation get set
#his points and edges
class Hexagon_Graph:
    def __init__(self, board, locator):
        self.board = board #board object
        self.locator = locator
    
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
    
    #intention is to move a stone from coord. return of this function is the set
    #of all empty neighbours of nonempty fields, where coord was removed
    def calculate_all_empty_neighbours(self, coord):
        points = []
        adapt_nonempty_neighbours = self.board.nonempty_fields.copy()
        adapt_nonempty_neighbours.remove(coord) #remove coord 
        for coords in adapt_nonempty_neighbours: #just iterate over this adapted nonempty_fields list
            for neigh in self.board.get_neighbours(coords).values():
                if self.board.board[neigh[0]][neigh[1]].is_empty:
                    points.append(neigh)
        points.append(coord) #as board is not empty on coord, append this to the list 
        return points
    
    #here points should be all empty neighbours of nonempty_fields. edges: edge from 
    #point to point2 iff a stone can move on the ground from point to point2
    def calculate_ground_moving_edges(self):
        edges = []
        for point in self.points:
            for point2 in self.points:
                if self.locator.can_move_to_neighbour_on_ground(point, point2, self.board):
                    edges.append((point, point2))
        return edges
            
    
    #for a point in the graph calculate all connected neighbours                
    def get_graph_neighbours(self, point):
        graph_neighbours = []
        for point2 in self.points:
            if (point, point2) in self.edges:
                graph_neighbours.append(point2)
        return graph_neighbours
    
    #algorithm depth-first search to check connectedness of the graph (source: internet)
    def depth_first_search(self, point):
        self.markings[self.points.index(point)] = 1
        relevant_points = [point2 for point2 in self.get_graph_neighbours(point) if self.markings[self.points.index(point2)] == 0]
        for point2 in relevant_points:
            self.depth_first_search(point2)
    
    #check whether the graph is connected        
    def is_connected(self):
        if len(self.calculate_connected_component(self.points[0])) == len(self.points):
            return True
        else: return False
        
    #return all points of the connected component of point
    def calculate_connected_component(self, point):
        points = []
        self.markings = [0] * len(self.points) #reset markings
        self.depth_first_search(point) #run algo
        for k in range(len(self.points)):
            if self.markings[k] == 1:
                points.append(self.points[k])
        return points
        
                
        
    