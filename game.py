import board
import player as hpl
import player_computer as cpl
import locator
import calculator as cal
import calculator_extended as cal_ex
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
        self.locator = locator.Locator(self.board, 100)
        self.interactor = interactor.Interactor(self.painter, cal_ex.Calculator_Extended(self.locator, self.players), self.turn)
        
        
class HvsC_Game(Game):
    def __init__(self, surface):
        self.surface = surface
        self.painter = painter.Painter()
        
        self.turn = ("white", 1)
        
        self.board = board.Board(Game.board_size, self.surface)
        self.locator = locator.Locator(self.board, 100)
        self.com_calculator = cal.Calculator(self.locator)
        self.players = {"white": hpl.Human_Player("white", self.surface), 
                        "black": cpl.Computer_Player("black", self.surface, self.com_calculator)}

        
        self.calculator = cal_ex.Calculator_Extended(self.locator, self.players)
        self.interactor = interactor.Interactor(self.painter, self.calculator, self.turn)
        
        
        








