import board
import player
import locator
import calculator
import interactor
import frame_stones

class Game:
    
    board_size = 30
    
class HvsH_Game(Game):
    def __init__(self, surface, stones_from_cb):
        self.surface = surface
        self.board = board.Board(Game.board_size, self.surface)
        self.players = [player.Human_Player("white", self.surface), player.Human_Player("black", self.surface)]
        self.locator = locator.Locator(self.board, self.players, 100, self.surface)
        self.interactor = interactor.Interactor(self.board, self.surface, calculator.Calculator(self.locator))
        self.frame_stones = frame_stones.frame_stones(stones_from_cb)
        self.turn = 0
        
        
#class HvsC_Game(Game):
#    def __init__(self, surface):
#        self.surface = surface
#        self.board = board.Board(Game.board_size, self.surface)
#        self.players = [player.Human_Player("white", self.surface), player.Computer_player("black", self.surface)]
#        self.locator = locator.Locator(self.board, self.players, look_into_past = 100, self.surface)
#        self.interactor = interactor.Interactor(self.board, calculator.Calculator(self.locator))
    
def start_game(surface):
    pass
