

class Board_subset:
    def __init__(self, board, locator):
        self.board = board
        self.locator = locator
        self.size = self.board.size
        #matrix has the sime size as board, is 1 in i,j iff we consider this field to be part 
        #of the set of fields we want to include at the moment (initialized with all fields, therefore all 1). 
        #the matrix will be helpful to get structural insides
        self.matrix = self.all_fields()
        
    def all_fields(self):
        return [[1] * self.size for i in range(self.size)]
    
    #a ground walking stone is on coord. where can it physically move ?
    #this function returns all possible ground fields, especially for the ant.
    #for the spider and bee conditions have to be added then at another code location.
    #with the help of the locator, which simulates all moving possibilities in forward, this function
    #checks whether on the way of one empty field to another a stone (ant) has to pass a too small gap 
    #for a stone to pass, which therefore does make the move impossible. As the locator saves his fields 
    #on the way, it is like a spion which goes first and checks the situation, then returns all fields 
    #which are ok, that means physically reachable on the ground. function can_move_to_neighbour_on_ground
    #of locator is helpful. 
    def ground_move_fields(self, coord):
        self.locator.move_to_position(coord)
        start_key = self.locator.new_key
        
        #calculate ground reachable neighbours of coord (right_neighbours). later we will run function 
        #add_ground_fields_to_locator for all those neighbours, to be sure to get all wished fields
        right_neighbours = list(self.board.get_neighbours(coord).values())
        for neigh in right_neighbours:
            if not self.locator.can_move_to_neighbour_on_ground(coord, neigh):
                right_neighbours.remove(neigh)
                
        #use test_objects
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        def func(coord2):
            seen_by_locator = [self.locator[k].coordinate for k in range(start_key, self.locator.new_key)]
            if not coord2 in seen_by_locator:
                self.locator.move_to_stone(coord2)
                self.locator.test_board.move_stone()
            neighbours = list(self.board.get_neighbours(coord2).values())
            
        
        
        
        
        
        if len(right_neighbours) == 0:
            return []
        else:
            for neigh in right_neighbours:
                func(neigh)
         
        
    
            
    
        
        
        def add_ground_fields_to_locator(coord):
            neighbours = list(self.board.get_neighbours(coord).values())
            #seen_by_locator contains all positions the locator has been on since starting this function,
            #excluding the actual position
            seen_by_locator = [self.locator[k].coordinate for k in range(start_key, self.locator.new_key)]
            #just consider neighbours which can be physically reached on the ground and which have not been 
            #seen by the locator
            for neigh in neighbours:
                cond1 = self.locator.can_move_to_neighbour_on_ground(coord, neigh)
                cond2 = not neigh in seen_by_locator
                if not cond1 or not cond2:
                    neighbours.remove(neigh)
            #when theres no neighbour left with the above conditions, then return.
            #the locator should now contain all ground reachable fields from position coord, 
            #saved from start_key to the actual maximum key
            if len(neighbours) == 0:
                return
            else:
                right_neigh = neighbours.pop() #take any "right" neighbour
                self.locator.move_to_stone(right_neigh)
                add_ground_fields_to_locator(right_neigh) #recursive calculation
        
        return [self.locator[k].coordinate for k in range(start_key, self.locator.new_key)] 
        
















        