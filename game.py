import board
import player as plh
import player_extended as ple
import player_computer as plc
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
        self.players = {"white": plh.Human_Player("white", self.surface), 
                        "black": plh.Human_Player("black", self.surface)}
        self.locator = locator.Locator(self.board, 100)
        self.interactor = interactor.Interactor(self.painter, cal_ex.Calculator_Extended(self.locator, self.players), self.turn)
        
    def turn_up(self):
        if self.turn[0] == "white":
            self.turn = ("black", self.turn[1])
        else:
            self.turn = ("white", self.turn[1] + 1)


#In this game against the computer, the human player is white and begins the game        
class HvsC_Game(Game):
    def __init__(self, surface):
        self.surface = surface
        self.painter = painter.Painter()
        
        self.turn = ("white", 1)
        
        self.board = board.Board(Game.board_size, self.surface)
        self.locator = locator.Locator(self.board, 100)
        self.com_calculator = cal.Calculator(self.locator)
        self.players = {"white": plh.Human_Player("white", self.surface), 
                        "black": plc.Computer_Player("black", self.surface, self.com_calculator)}

        
        self.calculator = cal_ex.Calculator_Extended(self.locator, self.players)
        self.interactor = interactor.Interactor(self.painter, self.calculator, self.turn)
        
        
class HvsH_Game_Extended(Game):
    def __init__(self, surface):
        self.surface = surface
        self.painter = painter.Painter()
        self.turn = ("white", 1)
        self.board = board.Board(Game.board_size, self.surface)
        self.players = {"white": ple.Human_Player_Extended("white", self.surface), 
                        "black": ple.Human_Player_Extended("black", self.surface)}
        self.locator = locator.Locator(self.board, 100)
        self.interactor = interactor.Interactor(self.painter, cal_ex.Calculator_Extended(self.locator, self.players), self.turn)
        
    def turn_up(self):
        if self.turn[0] == "white":
            self.turn = ("black", self.turn[1])
        else:
            self.turn = ("white", self.turn[1] + 1)






