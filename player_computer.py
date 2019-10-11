#computer player

import player
import random


class Computer_Player(player.Player):
    
    def __init__(self, color, surfaces, calculator):
        super().__init__(color, surfaces)
        self.calculator = calculator
        self.locator = self.calculator.locator
        
    
    random.seed()
    
    
    #input are the board constellations (you can find them aswell in self.calculator.board.past_boards) 
    #and the decision type (eg random, score_fct, etc)
    #return is tuple containing the hstone which wants to be moved, the direction stone it wants to be moved to
    #and the type of action (put or move)
    def get_action_decision(self, constellations, decision_type):
        # set and look at moveable, putable hexagons
        if decision_type == "random":
            #randomly choose put or move, and select random put resp. move stone
            #set them as src resp dir_hexagon and return action type aswell as below
            pass
        
        # how many stones has opponent player left ?
        # calculate relevant movings (src_hex, dir_hex)
        # maximize score_fct
        return (src_hexagon, dir_hexagon, action_type)
    
    def score_fct(self, constellation, src_hexagon, dir_hexagon):
        pass
    
    
    
    
    #for now: random 
    def get_action_decision2(self):
        action_type = random.choice(["put", "move"])
        if action_type == "put":
            src_hexagon = self.random_put_hexagon()
            dir_hexagons = self.calculator.get_possible_put_fields(self.color)
        elif action_type == "move":
            src_hexagon = self.random_move_hexagon()
            dir_hexagons = self.calculator.get_possible_move_fields(src_hexagon)
        field = self.random_field(dir_hexagons)
        dir_hexagon = self.calculator.board.board[field[0]][field[1]]
        return (src_hexagon, dir_hexagon, action_type)
        
    def random_move_hexagon(self):
        return random.choice(self.calculator.get_movable_hexagons(self.color))
    
    def random_put_hexagon(self):
        insects = [insect for insect in self.side_stones.keys() if self.side_stones_numbers[insect] > 0]
        return self.side_stones[random.choice(insects)]
    
    def random_field(self, fields):
        return random.choice(fields)
    
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
        






















        