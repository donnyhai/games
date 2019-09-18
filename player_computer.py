#computer player

import player
import random


class Computer_Player(player.Player):
    
    def __init__(self, color, surface, locator, interactor):
        super().__init__(color, surface)
        self.locator = locator
        self.interactor = interactor
        self.calculator = self.interactor.calculator
        
    
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
    
    def random_move_stone_selection(self, fields):
        pass
    
    def random_move_fields_selection(self, fields):
        pass
    
    
    #move_hexagon wants to be moved to dir_coord. what is the evaluation of this turn ?
    def evaluate_turn(self, move_hexagon, dir_coord):
        
        ###low evaluation points
        #spider is 3 steps away from opp bee +1
        #hopper is put next to own bee in the first 6 moves +1
        #opponent has few places to put stone +1
        #bug or hopper next to own bee +1/-1 (depends)
        #mosquito is moved next to only a spider -1
        
        
        ###middle evaluation points 
        #spider is blocked at own bee -1
        #opponent ant is blocked by own non-ant stone +2
        #mosquito is moved next to ant, bug or marienbug +2
        
        
        ###high evualuation points
        #bee can move out of a not anymore blocked situation +4
        #ant is blocked at own bee -3
        #spider next to opposite bee +3
        #bug is on opp bee with one possible place to put own stone +3
        #bug is on opp bee with at least two possible places to put own stone +4
        #own bee has one place left to fill, opp dangerous walking stone gets blocked by:
            #spider +700
            #hopper +600
            #bug  +500
            #marienbug  +400
            #ant +300
        #win move +1000
        pass
    
    #consider all (most) possible turns, which are the top number of turns ?
    def get_best_turns(self, number):
        pass
        






















        