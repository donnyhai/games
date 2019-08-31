import hexagon_stone as hs
import stone as s

class Player:
    def __init__(self, color, surface):
        self.color = color
        self.surface = surface
        self.stone_size = 0 ####################################edit, example: 0.05 * surface
        self.stones = self.create_stones(self.stone_size)
        
    def create_stones(self, stone_size):
        hstones = {"bee": hs.Hexagon_Stone(stone_size, self.surface, s.Stone("bee", 1)),
                "ant1": hs.Hexagon_Stone(stone_size, self.surface, s.Stone("ant",1)),
                "ant2": hs.Hexagon_Stone(stone_size, self.surface, s.Stone("ant",2)),
                "ant3": hs.Hexagon_Stone(stone_size, self.surface, s.Stone("ant",3)),
                "hopper1": hs.Hexagon_Stone(stone_size, self.surface, s.Stone("hopper", 1)),
                "hopper2": hs.Hexagon_Stone(stone_size, self.surface, s.Stone("hopper", 2)),
                "hopper3": hs.Hexagon_Stone(stone_size, self.surface, s.Stone("hopper", 3)),
                "spider1": hs.Hexagon_Stone(stone_size, self.surface, s.Stone("spider", 1)),
                "spider2": hs.Hexagon_Stone(stone_size, self.surface, s.Stone("spider", 2))}
        for hstone in hstones.values():
            hstone.stone.set_color(self.color)
        return hstones
    
class Human_Player(Player):
    pass

class Computer_player(Player):
    pass
        
