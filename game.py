import board
import player as hpl
import player_computer as cpl
import locator
import calculator
import interactor
import painter


class Game:
    
    board_size = 30
    
class HvsH_Game(Game):
    def __init__(self, surface):
        self.surface = surface
        self.painter = painter.Painter()
        
        self.turn = ("white", 1)
        
        self.board = board.Board(Game.board_size, self.surface)
        self.players = {"white": hpl.Human_Player("white", self.surface), 
                        "black": hpl.Human_Player("black", self.surface)}
        self.locator = locator.Locator(self.board, self.players, 100)
        self.interactor = interactor.Interactor(self.painter, calculator.Calculator(self.locator), self.turn)
        
        
class HvsC_Game(Game):
    def __init__(self, surface):
        self.surface = surface
        self.painter = painter.Painter()
        
        self.turn = ("white", 1)
        
        self.board = board.Board(Game.board_size, self.surface)
        self.players = {"white": hpl.Human_Player("white", self.surface), 
                        "black": cpl.Computer_Player("black", self.surface)}
        self.locator = locator.Locator(self.board, self.players, 100)
        self.interactor = interactor.Interactor(self.painter, calculator.Calculator(self.locator), self.turn)
    









