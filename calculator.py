import hexagon_stone as hs
import hexagon_graph as hg

class Calculator:
    def __init__(self, locator):
        self.locator = locator
        self.players = self.locator.players
        self.board = self.locator.board #note that the locator always contains the board object of the actual game
        #matrix has the sime size as board, is 1 in i,j iff we consider this field to be part 
        #of the set of fields we want to include at the moment (initialized with all fields, therefore all 1). 
        #the matrix will be helpful to get easier structural insides
        self.matrix = self.all_fields()
        self.empty_help_stone = hs.hexagon_stone(self.board.hexagon_size, "empty", 99)
        
        self.graph = hg.Hexagon_Graph(self.board, self.locator) #doesnt contain points or edges yet
        
        
    def all_fields(self):
        return [[1] * self.board.size for i in range(self.board.size)]
    
    #are the stones connected after taking away stone on coord ? use hexagon_graph object
    def board_keeps_connected(self, coord):
        nonempty_fields = self.board.nonempty_fields.copy()
        nonempty_fields.remove(coord)
        self.graph.set_points(nonempty_fields)
        self.graph.set_edges(self.graph.calculate_standard_edges())
        return self.graph.is_connected()
    
    #define winning condition: player wins if opposite bee is surrounded
    def winning_condition(self, color):
        if color == "white":    opp_color = "black"
        else:   opp_color = "white"
        color_bee = list(self.players[color].stones["bee"].values())[0]
        opp_color_bee = list(self.players[opp_color].stones["bee"].values())[0]
        color_bee_surr = False
        opp_color_bee_surr = False
        if color_bee.is_on_board:   
            color_bee_surr = True
            for neigh in self.board.get_neighbours(color_bee.board_pos).values():
                if self.board.board[neigh[0]][neigh[1]].is_empty:   color_bee_surr = False
        if opp_color_bee.is_on_board:
            opp_color_bee_surr = True
            for neigh in self.board.get_neighbours(opp_color_bee.board_pos).values():
                if self.board.board[neigh[0]][neigh[1]].is_empty:   opp_color_bee_surr = False
        return [color_bee_surr, opp_color_bee_surr]
    
    
    #input is the color of a stone which wants to be put onto the board from the side.
    #return is a list of board coords where this stone can be legally put to 
    def get_possible_put_fields(self, color):
        sol_fields = []
        for coord in self.board.nonempty_fields:
            for neigh in list(self.board.get_neighbours(coord).values()):
                #neigh must be empty
                if self.board.board[neigh[0]][neigh[1]].is_empty:
                    if color == "white":    opp_color = "black"
                    else:   opp_color = "white"
                    #neigh shall not have neighbours with different color as color
                    cond = True
                    for neigh2 in list(self.board.get_neighbours(neigh).values()):
                        if self.board.board[neigh2[0]][neigh2[1]].color == opp_color:   cond = False
                    if cond:    sol_fields.append(neigh)
        return sol_fields
    
    #move_hexagon wants to be moved, where can it move ? return is a list of board coords
    def get_possible_move_fields(self, move_hexagon):
        stone_type = move_hexagon.type
        board_pos = move_hexagon.board_pos
        if stone_type == "ant":     return self.get_ant_fields(board_pos)
        elif stone_type == "hopper":    return self.get_hopper_fields(board_pos)
        elif stone_type == "spider":    return self.get_spider_fields(board_pos)
        elif stone_type == "bee":   return self.get_bee_fields(board_pos)
        
    
    #event click at event_pos. in which hexagon is it ? return is a list containing exactly one hexagon 
    #iff the clicked was in this hexagon. look for empty or nonempty hexagons on the board, and for side_stones                
    def get_clicked_hexagon(self, event_pos):
        #look for both players
        for player in self.players.values():
            #look in player.side_stones for a clicked hexagon
            for hstone in player.side_stones.values():
                if hstone.point_in_hexagon(event_pos):
                    return hstone
            #look in player.stones for a clicked hexagon
            for hstone1 in player.stones.values():
                for hstone2 in hstone1.values():
                    if hstone2.is_drawn:
                        if hstone2.point_in_hexagon(event_pos):
                            return hstone2
        #look on the board
        for row in self.board.board:
            for hstone in row:
                if hstone.point_in_hexagon(event_pos):
                    return hstone
        return self.empty_help_stone
    
    #a ground walking stone is on coord. where can it physically move ?
    #this function returns all possible ground fields, especially for the ant.
    #with the help of the locator, which simulates all moving possibilities in forward, this function
    #checks whether on the way of one empty field to another a stone (ant) has to pass a too small gap 
    #for a stone to pass, which therefore does make the move impossible. As the locator saves his fields 
    #on the way, it is like a spion which goes first and checks the situation, then returns all fields 
    #which are ok, that means physically reachable on the ground. function can_move_to_neighbour_on_ground
    #of locator is helpful. 
    def get_ground_move_fields(self, coord):
        self.graph.set_points(self.graph.calculate_all_empty_neighbours(coord))
        self.graph.set_edges(self.graph.calculate_ground_moving_edges())
        ground_move_fields = self.graph.calculate_connected_component(coord)
        ground_move_fields.remove(coord) #remove this coord, as stone should not be able to move there
        return ground_move_fields
    
    #bee is on coord. where can it move ?
    def get_bee_fields(self, coord):
        return [coord1 for coord1 in self.get_ground_move_fields(coord) if self.locator.can_move_to_neighbour_on_ground(coord, coord1, self.board)]
    
    
    #ant is on coord. where can it move ?
    def get_ant_fields(self, coord):
        return self.get_ground_move_fields(coord)
    
    
    #hopper is on coord. where can it move ?
    def get_hopper_fields(self, coord):
        neighbours = self.board.get_neighbours(coord)
        hopper_fields = []
        #loop all the neighbours of coord and look for nonempty neighbours, 
        #and get the first empty field in every "direction"
        for i in range(6):
            neigh = neighbours[i]
            if not self.board.board[neigh[0]][neigh[1]].is_empty:
                while not self.board.board[neigh[0]][neigh[1]].is_empty:
                    neigh = self.board.get_neighbours(neigh)[i]
                hopper_fields.append(neigh)
        return hopper_fields

    #spider is on coord. where can she move ?
    def get_spider_fields(self, coord):
        self.graph.set_points(self.graph.calculate_all_empty_neighbours(coord))
        self.graph.set_edges(self.graph.calculate_ground_moving_edges())
        self.graph.set_edges(self.graph.calculate_spider_move_edges())
        spider_fields = self.graph.get_graph_neighbours(coord)
        if coord in spider_fields:
            spider_fields.remove(coord)
        return spider_fields
        
    #bug is on coord. where can it move ?
    def get_bug_fields(self, coord):
        return self.board.get_neighbours(coord).values()
        
        
    #marienbug is on coord. where can it move ?
    def get_marienbug_fields(self, coord):
        pass

    

            








