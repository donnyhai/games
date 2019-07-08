class Stone:
    def __init__(self, stone_type, number):
        self.type = stone_type
        self.number = number
        self.is_on_board = False
        self.coordinate = (-1,-1)
    def set_color(self, color):
        self.color = color
    def set_coordinate(self, coordinate):
        self.coordinate = coordinate