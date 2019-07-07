import stone

class Field:
    def __init__(self):
        self.is_empty = True
        self.stone = stone.Stone("empty", 0)
    def put_stone(self, stone):
        self.stone = stone
        self.is_empty = False
        if stone.is_on_board:
            stone.coordinate = self.coordinate
        else:
            stone.set_coordinate(self.coordinate)
    def remove_stone(self, stone):
        stone.coordinate = (-1,-1)
        self.is_empty = True
        self.stone = stone("empty", 0)
    def set_coordinate(self, coordinate):
        self.coordinate = coordinate