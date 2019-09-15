#computer player

import player

class Computer_Player(player.Player):
    
    
    
    
    #this method will get called in window_computer. here the evaluation goes on, whether stone 
    #shall be put or moved, and which strategy of action is chosen
    def computer_reaction(self):
        pass
    
    
    def random_put_insect(self):
        insects = [insect for insect in self.side_stones.keys() if self.side_stones_numbers[insect] > 0]
        return self.side_stones[insects.pop()]
    
    def random_put_field(self, fields):
        return fields.pop()