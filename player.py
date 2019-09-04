import hexagon_stone as hs

class Player:
    def __init__(self, color, surface):
        self.color = color
        self.surface = surface
        self.stone_size = int(0.03 * self.surface.get_width())
        self.stones = self.create_stones(self.stone_size)
        self.side_stones = self.create_side_stones(self.stone_size)
        self.set_side_positions() #side positions for the side stones
        
        
    def create_stones(self, stone_size):
        hstones = {"bee": {1: hs.hexagon_stone(stone_size, hs.Stone("bee", 1))},
                   "ant": {1: hs.hexagon_stone(stone_size, hs.Stone("ant", 1)),
                           2: hs.hexagon_stone(stone_size, hs.Stone("ant", 2)),
                           3: hs.hexagon_stone(stone_size, hs.Stone("ant", 3))},
                   "hopper": {1: hs.hexagon_stone(stone_size, hs.Stone("hopper", 1)),
                              2: hs.hexagon_stone(stone_size, hs.Stone("hopper", 2)),
                              3: hs.hexagon_stone(stone_size, hs.Stone("hopper", 3))},
                   "spider": {1: hs.hexagon_stone(stone_size, hs.Stone("spider", 1)),
                              2: hs.hexagon_stone(stone_size, hs.Stone("spider", 2))}}
        for hstones in hstones.values():
            for hstone in hstones.values():
                hstone.stone.set_color(self.color)
        return hstones
    
    def create_side_stones(self, stone_size):
        #the numbers in these side_stones shall display how many of these stone types are not yet on the board
        hstones = {"bee": hs.hexagon_stone(stone_size, hs.Stone("bee", 1)),
                "ant": hs.hexagon_stone(stone_size, hs.Stone("ant", 3)),
                "hopper": hs.hexagon_stone(stone_size, hs.Stone("hopper", 3)),
                "spider": hs.hexagon_stone(stone_size, hs.Stone("spider", 2))}
        for hstone in hstones.values():
            hstone.stone.set_color(self.color)
        return hstones
    
    #calculate positions of hexagons laying at the side depending on player white or black and set them 
    #for self.stones
    def set_side_positions(self):
        
        surface_width = self.surface.get_width()
        surface_height = self.surface.get_height()*0.8
        frame_x_size = surface_width*0.1
        hexa_size = int(frame_x_size*0.3)
        y_distance = int((surface_height-4*hexa_size*3**(0.5))/5)
        right_frame_translate = (surface_width*0.9, 0)
        
        ant_position = (frame_x_size*0.25, y_distance)
        hopper_position = (frame_x_size/4, 2*y_distance + hexa_size*3**(0.5))
        spider_position = (frame_x_size/4, 3*y_distance + 2*hexa_size*3**(0.5))
        bee_position = (frame_x_size/4, 4*y_distance + 3*hexa_size*3**(0.5))
        
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
    
    def set_side_stones_numbers(self):
        for insect in self.stones:
            pass
        
class Human_Player(Player):
    pass

class Computer_player(Player):
    pass
        
