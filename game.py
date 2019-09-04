import board
import player
import locator
import calculator
import interactor
import painter

class Game:
    
    board_size = 30
    
class HvsH_Game(Game):
    def __init__(self, surface):
        self.surface = surface
        self.painter = painter.Painter(self.surface)
        
        self.turn = ("white", 1)
        
        self.board = board.Board(Game.board_size, self.surface)
        self.players = {"white": player.Human_Player("white", self.surface), 
                        "black": player.Human_Player("black", self.surface)}
        self.locator = locator.Locator(self.board, self.players, 100)
        self.interactor = interactor.Interactor(self.painter, calculator.Calculator(self.locator), self.turn)
        
        
#class HvsC_Game(Game):
#    def __init__(self, surface):
#        self.surface = surface
#        self.board = board.Board(Game.board_size, self.surface)
#        self.players = [player.Human_Player("white", self.surface), player.Computer_player("black", self.surface)]
#        self.locator = locator.Locator(self.board, self.players, look_into_past = 100, self.surface)
#        self.interactor = interactor.Interactor(self.board, calculator.Calculator(self.locator))
    
def start_game(surface):
    pass
