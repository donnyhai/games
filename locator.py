import test_objects as test

#A locator object corresponds to a board and and saves stones the locator is or was looking at in the past in 
#a dict .locations (init with key = 0, and value = the stone in the middle of the board and its coordinate)
#note that the values of locations shall represent the location the locator was on, which consists of the stone 
#and its coordinate the moment the locator landed on this stone. it may happen that the stones coordinate
#changes with time, but the coordinate which gets saved in locator is (should be) fixed and gives the information
#of the "location" of the locator. 
#note that empty fields formally have a stone of type "empty" on it.  
#the maximum number of stones the locator is saving in .locations is set by int .look_into_past 
#to create a locator board and players have to be given, then a test_board and test_players are 
#set to give the possibility to test out moves etc
class Locator:
    def __init__(self, board, players, look_into_past):
        #board, test_board and players
        self.board = board #this is a Board object
        self.test_board = test.Test_Board(self.board.size, self.board.surface) 
        self.players = players #this is a list of Player objects
        
        self.look_into_past = look_into_past
        
        self.initial_stone = self.board.board[round(self.board.size / 2)][round(self.board.size / 2)]
        self.locations = {0: (self.initial_stone, self.initial_stone.board_pos)} #potential error source
        self.new_key = 1
    
    #move locator to position coord, add the stone there to the locator. 
    #.new_key will always go up by one, to generally count the number of stones in total the locator
    #has been looking at since created, and to not have double keys accidently 
    #note, that you have to give the board on which the locator shall move its position (board or test_board), 
    #it then may land on a different stone
    def move_to_position(self, coord, which_board):
        if self.get_position()[1] != coord:
            stone = which_board.board[coord[0]][coord[1]]
            if len(self.locations) == self.look_into_past:
                self.remove_stone()
            self.locations[self.new_key] = (stone, stone.board_pos) #add stone with key new_key 
            self.new_key += 1
    
    #get actual position, return stone
    def get_position(self):
        return self.locations[self.new_key - 1]
    
    #remove stone with lowest key
    def remove_stone(self):
        self.locations.__delitem__(min(self.locations.keys()))
        
    #clear locations and initialize as in __init__, set new_key to 1
    def clear_stones(self):
        self.locations = {0: (self.initial_stone, self.initial_stone.board_pos)}
        self.new_key = 1
        
    #is it possible to move from coord1 to coord2 on the ground?
    #coord1 and coord2 have to be neighbour coordinates
    #helpful for all stones moving on the ground. 
    #yet this function doesnt check connectness of the board stones
    #again note that you have to give the board (board or test_board)
    def can_move_to_neighbour_on_ground(self, coord1, coord2, which_board):
        neighbours1 = set(which_board.get_neighbours(coord1).values())
        neighbours2 = set(which_board.get_neighbours(coord2).values())
        #conditions to make the move on the ground from coord1 to coord2 possible:
        #coord1 and coord2 are neighbours
        cond1 = coord1 in neighbours2
        #field at coord2 is empty
        cond2 = which_board.board[coord2[0]][coord2[1]].is_empty
        #stone can physically "pass" from coord1 to coord2 (consider neighbour stones)
        #and there exists min one neighbour in the intersection -> exactly one neighbour
        #Note that the intersectino of neigh1 and neigh2 contains 0,1 or 2 nonempty stones
        cond3 = len(neighbours1.intersection(neighbours2)) == 1
        #coord2 is not lying "outside" nonempty fields (that means at least "two" steps away of them)
        cond4 = len(neighbours2) >= 1 if which_board.board[coord1[0]][coord1[1]].is_empty else len(neighbours2) >= 2
        return cond1 and cond2 and cond3 and cond4
    
