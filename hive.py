class player:
    def __init__(self, color):
        self.color = color
        self.stones = self.create_stones()
    def create_stones(self):
        stones = {"bee": stone("bee", 1),
                "ant1": stone("ant",1),
                "ant2": stone("ant",2),
                "ant3": stone("ant",3),
                "hopper1": stone("hopper", 1),
                "hopper2": stone("hopper", 2),
                "hopper3": stone("hopper", 3)}
        for i in stones.values():
            i.set_color(self.color)
        return stones
    
        
    
class stone:
    def __init__(self, stone_type, number):
        self.type = stone_type
        self.number = number
        self.is_on_board = False
    def set_color(self, color):
        self.color = color
    def set_coordinate(self, coordinate):
        self.coordinate = coordinate


class field:
    def __init__(self):
        self.is_empty = True
        self.stone = stone("blank", 0)
    def put_stone(self, stone):
        self.stone = stone
        self.is_emtpy = False
        if stone.is_on_board:
            stone.coordinate = self.coordinate
        else:
            stone.set_coordinate(self.coordinate)
    def remove_stone(self, stone):
        stone.coordinate = (-1,-1)
        self.is_empty = True
        self.stone = stone("blank")
    def set_coordinate(self, coordinate):
        self.coordinate = coordinate
        
        

class board:
    def __init__(self, size):
        self.size = size
        self.board = [[field() for i in range(self.size)] for i in range(self.size)]
        self.set_field_coordinates()
        self.nonempty_fields = [] #will contain coordinates
    
    #set coordinates for field objects on the board
    def set_field_coordinates(self):
        {self.board[i][j].set_coordinate((i,j)) for i in range(self.size) for j in range(self.size)}
    
    #get neighbour coordinates of (i,j) starting from top going clockwise
    def get_neighbours(self, i, j):
        return [(i-1,j), (i-1,j+1), (i,j+1), (i+1,j+1), (i+1,j), (i,j-1)] 
    
    #check if (i,j) is part of the board (if board is big enough and game starts in the middle, 
    #this function should not be necessary)
    def is_inside(self, i, j):
        pass
    
    #check, whether indexset is connected
    def is_connected(self, indexset):
        if len(indexset) in {0,1}:
            return True
        else:
            for i,j in indexset:
                if len(indexset.intersection(self.get_neighbours(i,j))) == 0:
                    return False
            return True
    
    def put_stone_condition(self, player, stone, i, j):
        #stone belongs to player
        cond1 = stone.color == player.color 
        #stone is not on board
        cond2 = not stone.is_on_board 
        #field i,j is empty
        cond3 = self.board[i][j].is_empty 
        #at least one same color neighbour, no other color neighbour.
        #watch the cases, that no or just one stone is on the board
        cond4 = False
        neigh = self.get_neighbours(i,j)
        if len(self.nonempty_fields) == 0:
            cond4 = True
        elif len(self.nonempty_fields) == 1:
            cond4 = (i,j) in neigh
        else:
            for i,j in neigh:
                field = self.board[i][j]
                if not field.is_empty:
                    if field.stone.color != stone.color:
                        cond4 = False
                        break
                    else:
                        cond4 = True
        #bee has been put until 4. stoneput
        cond5 = True
        if len(self.nonempty_fields) in {6,7} and not player.stones["bee"].is_on_board:
            cond5 = stone.type == "bee"
        return cond1 and cond2 and cond3  and cond4 and cond5
        
    def move_stone_condition(self, player, stone, i, j):
        if stone.type in {"bug", "assel"}:
            pass
        else:
            #bee is on board
            cond0 = player.stones["bee"].is_on_board
            #stone belongs to player
            cond1 = stone.color == player.color
            #stone is on board
            cond2 = stone.is_on_board
            #i,j is empty
            cond3 = self.board[i][j].is_empty 
            #boardstones are connected after taking away stone
            nonempty_fields = self.nonempty_fields.copy()
            cond4 = self.is_connected(nonempty_fields.remove(stone.coordinate))
            return cond0 and cond1 and cond2 and cond3 and cond4
            
    
    def put_stone(self, player, stone, i, j):
        if  not self.put_stone_condition(player, stone, i, j):
            print("stoneput not possible")
            pass
        else:
            self.board[i][j].put_stone(stone)
            stone.is_on_board = True
            self.nonempty_fields.append((i,j))
    
    #get empty fields of the board, enter empty_type "extern", "outer" or "inner"
    #"extern" means empty fields with number of nonempty neighbours in {0}
    #"outer" means empty fields with number of nonempty neighbours in {1,2,3,4}
    #"inner" means empty fields with number of nonempty neighbours in {5,6}
    def get_empty_fields(self, empty_type):
        #set possible numbers for nonempty neighbours according to empty_type
        if empty_type == "extern":
            numbers_nonempty_neigh = {0}
        elif empty_type == "outer":
            numbers_nonempty_neigh = {1,2,3,4}
        elif empty_type == "inner":
            numbers_nonempty_neigh = {5,6}
        else:
            print("no such empty_type")
        #find respective empty fields 
        indexset = {}
        for row in self.board:
            for field in row:
                coord = field.coordinate
                neigh = self.get_neighbours(coord[0], coord[1])
                if field.is_empty and len(neigh.intersection(self.nonempty_fields)) in numbers_nonempty_neigh:
                    indexset.append(coord)
        return indexset
    
    def get_hopper_fields(self, i,j):
        pass
        
    
    #move stone of player to i,j (if possible)       
    def move_stone(self, player, stone, i, j):
        def move(stone, i, j):
            self.board[stone.coordinate[0]][stone.coordinate[1]].remove_stone(stone)
            self.board[i][j].put_stone(stone)
        
        if not self.move_stone_condition(player, stone, i, j):
            print("stone move not possible")
        else:
            outerempty_fields = self.get_empty_fields("outer")
            innerempty_fields = self.get_empty_fields("inner")
            neigh = self.get_neighbours(i,j)
            nonempty_neigh = neigh.intersection(self.nonempty_fields)
            if stone.type == "bee":
                if (i,j) in neigh.intersection(outerempty_fields):
                    move(stone, i, j)
                else:
                    print("bee move not possible")
            elif stone.type == "ant":
                if (i,j) in outerempty_fields:
                    move(stone, i, j)
                else:
                    print("ant move not possible")
            elif stone.type == "hopper":
                pass
                    
                    
                    
                    
b = board(10)
p1 = player(1)
p2 = player(2)
        
st = p1.stones["ant1"]
b.put_stone(p1,st,5,5)