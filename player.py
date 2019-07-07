import stone as s

class Player:
    def __init__(self, color):
        self.color = color
        self.stones = self.create_stones()
    def create_stones(self):
        stones = {"bee": s.Stone("bee", 1),
                "ant1": s.Stone("ant",1),
                "ant2": s.Stone("ant",2),
                "ant3": s.Stone("ant",3),
                "hopper1": s.Stone("hopper", 1),
                "hopper2": s.Stone("hopper", 2),
                "hopper3": s.Stone("hopper", 3),
                "spider1": s.Stone("spider", 1),
                "spider2": s.Stone("spider", 2)}
        for stone in stones.values():
            stone.set_color(self.color)
        return stones
    

        
