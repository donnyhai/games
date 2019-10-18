import calculator_extended
import random



#this class makes calculations for a computer player. therefore expressions like opp_color or opp_player refer
#to the opponent player (human or computer)
class Computer_Action(calculator_extended.Calculator_Extended):
    def __init__(self, locator, players, opp_color = "white"):
        super().__init__(locator, players)
        self.opp_player = self.players[opp_color]
        self.cplayer = self.players[[color for color in ["white", "black"] if color != opp_color].pop()] #computer player
    
    random.seed()
    
    #input are the board constellations (you can find them aswell in self.calculator.board.past_boards) 
    #and the decision type (eg random, score_fct, etc)
    #return is tuple containing the hstone which wants to be moved, the direction stone it wants to be moved to
    #and the type of action (put or move)
    def get_action_decision(self, decision_type = "random"):
        
        #random computer player: decides to randomly put or move a random hstone
        if decision_type == "random":
            self.set_action_hexagons(self.cplayer)
            if self.cplayer.putable_hexagons:
                if self.cplayer.moveable_hexagons:
                    action_type = random.choice(["move", "put"])
                    if action_type == "move":
                        src_hexagon = self.random_move_hexagon(self.cplayer)
                        dir_coord = random.choice(self.get_possible_move_fields(src_hexagon))
                        dir_hexagon = self.board.board[dir_coord]
                    else:
                        src_hexagon = self.random_put_hexagon(self.cplayer)
                        dir_coord = random.choice(self.get_possible_put_fields(src_hexagon.color))
                        dir_hexagon = self.board.board[dir_coord]
                else:
                    action_type = "put"
                    src_hexagon = self.random_put_hexagon(self.cplayer)
                    dir_coord = random.choice(self.get_possible_put_fields(src_hexagon.color))
                    dir_hexagon = self.board.board[dir_coord]
            else:
                action_type = "move"
                src_hexagon = self.random_move_hexagon(self.cplayer)
                dir_coord = random.choice(self.get_possible_move_fields(src_hexagon))
                dir_hexagon = self.board.board[dir_coord]
        

        #computer player which evaluates according to a score function
        elif decision_type == "score_fct":
            pass
        
        return (src_hexagon, dir_hexagon, action_type)
    
    
    
    def random_move_hexagon(self, player):
        return random.choice(player.moveable_hexagons)
    
    def random_put_hexagon(self, player):
        put_hstone = random.choice(player.putable_hexagons)
        return player.side_stones[put_hstone.type]
    
    def random_element(self, elements):
        return random.choice(elements)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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
        
    def score_fct(self, constellation, src_hexagon, dir_hexagon):
        pass

    
    