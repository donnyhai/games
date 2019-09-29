import board
import player as plh
import player_extended as ple
import player_computer as plc
import locator
import calculator as cal
import calculator_extended as cal_ex
import interactor
import painter
import pygame
import buttons
import colors as c

class Game:
    def __init__(self, surface):
        self.board_size = 30
        self.surfaces = {"surface_full": surface, 
                         "surface_board": surface.subsurface(pygame.Rect(0.1 * surface.get_width(), 0, 0.8 * surface.get_width(), surface.get_height())),
                         "surface_stones": {"white": surface.subsurface(pygame.Rect(0, 0, 0.1 * surface.get_width(), 0.8 * surface.get_height())),
                                            "black": surface.subsurface(pygame.Rect(0.9 * surface.get_width(), 0, 0.1 * surface.get_width(), 0.8 * surface.get_height()))},
                         "surface_text": {"white": surface.subsurface(pygame.Rect(0, 0.8 * surface.get_height(), 0.1 * surface.get_width(), 0.2 * surface.get_height())),
                                          "black": surface.subsurface(pygame.Rect(0.9 * surface.get_width(), 0.8 * surface.get_height(), 0.1 * surface.get_width(), 0.2 * surface.get_height()))}}
        self.painter = painter.Painter()
        self.board = board.Board(self.board_size, self.surfaces)
        self.locator = locator.Locator(self.board, 100)
        self.turn = ("white", 1)
        
#        self.center_button = buttons.Button(self.surfaces["surface_board"], c.center_button_color, x,y, int(self.surfaces["surfaces_board"].get_width() / 30), int(self.surfaces["surfaces_board"].get_width() / 30))
        
    def turn_up(self):
        if self.turn[0] == "white": self.turn = ("black", self.turn[1])
        else:   self.turn = ("white", self.turn[1] + 1)

    
class HvsH_Game(Game):
    def __init__(self, surface):
        super().__init__(surface)
        self.players = {"white": plh.Human_Player("white", self.surfaces), 
                        "black": plh.Human_Player("black", self.surfaces)}
        self.interactor = interactor.Interactor(self.painter, cal_ex.Calculator_Extended(self.locator, self.players), self.turn)
        
    

class HvsH_Game_Extended(Game):
    def __init__(self, surface):
        super().__init__(surface)
        self.players = {"white": ple.Human_Player_Extended("white", self.surfaces), 
                        "black": ple.Human_Player_Extended("black", self.surfaces)}
        self.interactor = interactor.Interactor(self.painter, cal_ex.Calculator_Extended(self.locator, self.players), self.turn)
        


#In this game against the computer, the human player is white and begins the game        
class HvsC_Game(Game):
    def __init__(self, surface):
        super().__init__(surface)
        self.com_calculator = cal.Calculator(self.locator)
        self.players = {"white": plh.Human_Player("white", self.surfaces), 
                        "black": plc.Computer_Player("black", self.surfaces, self.com_calculator)}
        self.calculator = cal_ex.Calculator_Extended(self.locator, self.players)
        self.interactor = interactor.Interactor(self.painter, self.calculator, self.turn)
        
        







