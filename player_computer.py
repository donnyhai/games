#computer player

import player

class Computer_player(player.Player):
    
    
    
    ##########FIRST PUT: which stone shall computer firstly put ?
    
    def random_first_put(self):
        insect = ["bee", "ant", "spider", "hopper", "bug"].pop()
        return self.side_stones[insect]