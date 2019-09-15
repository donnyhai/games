#computer player

import player
import random


class Computer_Player(player.Player):
    
    random.seed()
    
    #this method will get called in window_computer. here the evaluation goes on, whether stone 
    #shall be put or moved, and which strategy of action is chosen
    def computer_reaction(self):
        pass
    

    def random_put_insect(self):
        insects = [insect for insect in self.side_stones.keys() if self.side_stones_numbers[insect] > 0]
        index = random.choice(insects)
        return self.side_stones[index]
    
    def random_put_field(self, fields):
        index = random.choice(fields)
        return index