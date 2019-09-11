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
        self.graph.set_points(self.graph.calculate_all_empty_neighbours())
        self.graph.set_edges(self.graph.calculate_ground_moving_edges())
        return self.graph.calculate_connected_component(coord)
    
    
    #NOT YET WORKING
    #alternative way with locator. advantage: locator movements may be useful for interpretations
    def get_ground_move_fields2(self, coord):
        
        if not self.board.board[coord[0]][coord[1]].is_empty:
        
            #return neighbours of coord in test_board which are ground-reachably and which arent in seen_by_locator
            def get_right_neighbours(coord):
                seen_by_locator = [self.locator.locations[k][1] for k in range(start_key - 1, self.locator.new_key)]
                neighbours3 = list(self.locator.test_board.get_neighbours(coord).values())
                right_neighbours = []
                for neigh in neighbours3:
                    cond1 = self.locator.can_move_to_neighbour_on_ground(coord, neigh, self.locator.test_board)
                    cond2 = neigh in seen_by_locator
                    if cond1 and not cond2:  right_neighbours.append(neigh)
                return right_neighbours
            
            #this function just gets applied on coordinates which are "right neighbours"
            def add_neigh_to_locator(dir_coord):
                actual_stone = self.locator.get_position()[0] #possible error source
                dir_stone = self.locator.test_board.board[dir_coord[0]][dir_coord[1]]
                self.locator.test_board.move_stone(actual_stone, dir_stone) #first move stone
                self.locator.move_to_position(dir_coord, self.locator.test_board) #then put locator there,
                #so he doesnt sit on an empty stone
                right_neighbours2 = get_right_neighbours(dir_coord)
                if len(right_neighbours2) == 0: return
                else:   add_neigh_to_locator(right_neighbours2[0]) #possible error source, 
                #as just ONE neighbour is considered, but should be enough
            
            self.locator.test_board.copy_board(self.board)
            self.locator.move_to_position(coord, self.locator.test_board)
            start_key = self.locator.new_key
            
            right_neighbours = get_right_neighbours(coord)
            
            for neigh in right_neighbours:
                #copy the actual board constellation into test_board
                self.locator.test_board.copy_board(self.board)
                #move locator back to the "starting" coordinate
                self.locator.move_to_position(coord, self.locator.test_board)
                #run the recursive function
                add_neigh_to_locator(neigh)
            
            #all relevant fields were saved in locator since key start_key
            ground_move_fields = [self.locator.locations[k][1] for k in range(start_key, self.locator.new_key)]    
            
            #set indicator matrix
            for i in range(self.board.size):
                for j in range(self.board.size):
                    if (i,j) in ground_move_fields: self.matrix[i][j] = 1 
                    else: self.matrix[i][j] = 0
            
            return ground_move_fields
    
    
    #bee is on coord. where can it move ?
    def get_bee_fields(self, coord):
        return set(self.board.get_neighbours(coord).values()).intersection(self.get_ground_move_fields(coord))
    
    
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
    
    
    #spider is on coord. where can it move ?
    def get_spider_fields(self, coord): 
        
        #function to simulate the moving of the spider. rule: the spider cannot return
        #to a field she was coming from, unless it is the only possible field to walk. 
        #when she has walked three fields with this rule, she has to stop
        def func(sour_coord, dir_coord, start_key):
            self.locator.move_to_position(dir_coord, self.locator.test_board)
            if self.locator.new_key - start_key == 3:
                spider_fields.append(dir_coord)
                #why is there a problem with start_key ???
                start_key += 1 #in case that next_neighbours contains more than one field, 
                #because then we would count to more than 3 unwantedly
                return
            else:
                neighbours = set(self.locator.test_board.get_neighbours(dir_coord).values())
                right_neighbours = neighbours.intersection(ground_move_fields)
                right_neighbours.remove(sour_coord) #dont consider sour_coord
                if len(right_neighbours) == 0: #sour_coord only neighbour ?
                    func(dir_coord, sour_coord)
                else:
                    for neigh in right_neighbours:
                        func(dir_coord, neigh)
        
        ground_move_fields = self.get_ground_move_fields(coord)
        spider_fields = []
        
        #actualize test_board and move locator to coord on test_board
        self.locator.test_board.copy_board(self.board)
        self.locator.move_to_position(coord, self.locator.test_board)
        
        neighbours = set(self.locator.test_board.get_neighbours(coord).values())
        right_neighbours = neighbours.intersection(ground_move_fields)
        
        for neigh in right_neighbours:
            #copy the actual board constellation into test_board
            self.locator.test_board.copy_board(self.board)
            #move locator back to the "starting" coordinate
            self.locator.move_to_position(coord, self.locator.test_board)
            #start_key to be able to count to 3 for the steps taken by locator
            start_key = self.locator.new_key
            #run the recursive function
            func(coord, neigh, start_key)
        
        #set indicator matrix
        for i in range(self.board.size):
            for j in range(self.board.size):
                if (i,j) in spider_fields: self.matrix[i][j] = 1 
                else: self.matrix[i][j] = 0
        
        return spider_fields


    #bug is on coord. where can it move ?
    def get_bug_fields(self, coord):
        return self.board.get_neighbours(coord).values()
        
        
    #marienbug is on coord. where can it move ?
    def get_marienbug_fields(self, coord):
        pass

    

            








