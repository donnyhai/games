import hexagon_stone as hs
from math import sqrt

class Player:
    def __init__(self, color, surface):
        self.color = color
        self.surface = surface
        self.stone_size = int(0.03 * self.surface.get_width())
        
        self.stones = self.create_stones(self.stone_size)
        self.stones_list = self.get_stones_list() #all stones in one list
        self.side_stones = self.create_side_stones(self.stone_size)
        self.set_side_stones_positions() #side positions for the side stones
        #side_stone_numbers shall display how many of each insect type are not yet on the board
        self.side_stones_numbers = {"bee": 1, "ant": 3, "hopper": 3, "spider": 2}
        

    def create_stones(self, stone_size):
        hstones = {"bee": {1: hs.hexagon_stone(stone_size, "bee", 1)},
                   "ant": {1: hs.hexagon_stone(stone_size, "ant", 1),
                           2: hs.hexagon_stone(stone_size, "ant", 2),
                           3: hs.hexagon_stone(stone_size, "ant", 3)},
                   "hopper": {1: hs.hexagon_stone(stone_size, "hopper", 1),
                              2: hs.hexagon_stone(stone_size, "hopper", 2),
                              3: hs.hexagon_stone(stone_size, "hopper", 3)},
                   "spider": {1: hs.hexagon_stone(stone_size, "spider", 1),
                              2: hs.hexagon_stone(stone_size, "spider", 2)}}
        for hstones1 in hstones.values():
            for hstone in hstones1.values():
                hstone.set_color(self.color)
                hstone.is_empty = False
        return hstones
    
    def create_side_stones(self, stone_size):
        hstones = {"bee": hs.hexagon_stone(stone_size, "bee"),
                "ant": hs.hexagon_stone(stone_size, "ant"),
                "hopper": hs.hexagon_stone(stone_size, "hopper"),
                "spider": hs.hexagon_stone(stone_size, "spider")}
        for hstone in hstones.values():
            hstone.set_color(self.color)
            hstone.is_empty = False
        return hstones
    
    #calculate positions of hexagons laying at the side depending on player white or black and set them 
    #for self.stones
    def set_side_stones_positions(self):
        
        surface_width = self.surface.get_width()
        surface_height = self.surface.get_height()*0.8
        frame_x_size = surface_width*0.1
        hexa_size = int(frame_x_size*0.3)
        sqrt_3 = sqrt(3)
        y_distance = (surface_height - 4 * hexa_size*sqrt_3) // 5
        right_frame_translate = (surface_width*0.9, 0)
        
        ant_position = ((frame_x_size * 21) // 40 , y_distance)
        hopper_position = ((frame_x_size * 21) // 40, 2*y_distance + hexa_size*sqrt_3)
        spider_position = ((frame_x_size * 21) // 40, 3*y_distance + 2*hexa_size * sqrt_3)
        bee_position = ((frame_x_size * 21) // 40, 4*y_distance + 3*hexa_size * sqrt_3)
        
        #translate stones to the right side if they are black
        if self.color == "black":
            ant_position = (ant_position[0] + right_frame_translate[0], ant_position[1] + right_frame_translate[1])
            hopper_position = (hopper_position[0] + right_frame_translate[0], hopper_position[1] + right_frame_translate[1])
            spider_position = (spider_position[0] + right_frame_translate[0], spider_position[1] + right_frame_translate[1])
            bee_position = (bee_position[0] + right_frame_translate[0], bee_position[1] + right_frame_translate[1])
            
        #set positions of self.stones
        self.side_stones["bee"].set_pixel_pos(bee_position)
        self.side_stones["ant"].set_pixel_pos(ant_position)
        self.side_stones["hopper"].set_pixel_pos(hopper_position)
        self.side_stones["spider"].set_pixel_pos(spider_position)
    
    #set the number attribute of side_stones to display how many of each insect type are not on the board
    #for example after each stone put this function has to be called
    def set_side_stones_numbers(self):
        for insect in self.stones:
            counter = 0
            for hstone in self.stones[insect].values():
                if not hstone.is_on_board:
                    counter += 1
            self.side_stones_numbers[insect] = counter
            
    def draw_stone_numbers_text(self, surface):
        self.side_stones["ant"].pixel_pos
        self.side_stones["hopper"].pixel_pos
        self.side_stones["spider"].pixel_pos
        self.side_stones["bee"].pixel_poss
        
    def get_stones_list(self):
        stones_list = []
        for stones in self.stones.values():
            for stone in stones:
                stones_list.append(stone)
        return stones_list

class Human_Player(Player):
    pass

class Computer_player(Player):
    pass
        
