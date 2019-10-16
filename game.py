import board
import player as plh
import player_extended as ple
import player_computer as plc
import locator
import calculator_extended as cal_ex
import interactor
import painter
import pygame
import button
import colors as c
import backgrounds as bg
import computer_action as ca



class Game:
    def __init__(self, surface):
        self.board_size = 30
        self.surfaces = {"surface_full": surface, 
                         "surface_board": surface.subsurface(pygame.Rect(0.1 * surface.get_width(), 0, 0.8 * surface.get_width(), surface.get_height())),
                         "surface_stones": {"white": surface.subsurface(pygame.Rect(0, 0, 0.1 * surface.get_width(), 0.8 * surface.get_height())),
                                            "black": surface.subsurface(pygame.Rect(0.9 * surface.get_width(), 0, 0.1 * surface.get_width(), 0.8 * surface.get_height()))},
                         "surface_text": {"white": surface.subsurface(pygame.Rect(0, 0.8 * surface.get_height(), 0.1 * surface.get_width(), 0.2 * surface.get_height())),
                                          "black": surface.subsurface(pygame.Rect(0.9 * surface.get_width(), 0.8 * surface.get_height(), 0.1 * surface.get_width(), 0.2 * surface.get_height()))}}
        self.backgrounds = {self.surfaces["surface_board"]: bg.tickled_color(self.surfaces["surface_board"], c.background_color2, c.background_color3),
                            self.surfaces["surface_stones"]["white"]: bg.standard_color(self.surfaces["surface_stones"]["white"], c.background_side_stones),
                            self.surfaces["surface_stones"]["black"]: bg.standard_color(self.surfaces["surface_stones"]["black"], c.background_side_stones),
                            self.surfaces["surface_text"]["white"]: bg.standard_color(self.surfaces["surface_text"]["white"], c.background_text_box),
                            self.surfaces["surface_text"]["black"]: bg.standard_color(self.surfaces["surface_text"]["black"], c.background_text_box)}
        self.painter = painter.Painter(self.backgrounds)
        self.board = board.Board(self.board_size, self.surfaces)
        self.locator = locator.Locator(self.board, 100)
        self.turn = ("white", 1)
        
        self.buttons = self.create_buttons()
        
    def turn_up(self):
        if self.turn[0] == "white": self.turn = ("black", self.turn[1])
        else:   self.turn = ("white", self.turn[1] + 1)
        self.board.past_boards[len(self.board.past_boards) - 1]["turn"] = self.turn #save the new turn in the actual board constellation
        
    def create_buttons(self):
        center_button = button.Button(self.surfaces["surface_board"], "center",
                                      int(1/30 * self.surfaces["surface_board"].get_height()),
                                      (int(4/9 * self.surfaces["surface_board"].get_width()), int(12/13 * self.surfaces["surface_board"].get_height())),
                                      (int(1/9 * self.surfaces["surface_board"].get_width()), int(1/20 * self.surfaces["surface_board"].get_height())),
                                      c.center_button_color, (0,0,0))
        back_button = button.Button(self.surfaces["surface_board"], "back",
                                      int(1/30 * self.surfaces["surface_board"].get_height()),
                                      (int(1/9 * self.surfaces["surface_board"].get_width()), int(12/13 * self.surfaces["surface_board"].get_height())),
                                      (int(1/9 * self.surfaces["surface_board"].get_width()), int(1/20 * self.surfaces["surface_board"].get_height())),
                                      c.center_button_color, (0,0,0))
        restart_button = button.Button(self.surfaces["surface_board"], "restart",
                                      int(1/30 * self.surfaces["surface_board"].get_height()),
                                      (int(7/9 * self.surfaces["surface_board"].get_width()), int(12/13 * self.surfaces["surface_board"].get_height())),
                                      (int(1/9 * self.surfaces["surface_board"].get_width()), int(1/20 * self.surfaces["surface_board"].get_height())),
                                      c.center_button_color, (0,0,0))
        return {"center_button": center_button, "back_button": back_button, "restart_button": restart_button}




   
class HvsH_Game_Basic(Game):
    def __init__(self, surface, mode = "basic"):
        super().__init__(surface)
        self.players = {"white": plh.Human_Player("white", self.surfaces), 
                        "black": plh.Human_Player("black", self.surfaces)}
        self.interactor = interactor.Interactor(self.painter, cal_ex.Calculator_Extended(self.locator, self.players), self.turn, self.buttons)
        self.mode = mode
    

class HvsH_Game_Extended(Game):
    def __init__(self, surface, mode = "extended"):
        super().__init__(surface)
        self.players = {"white": ple.Human_Player_Extended("white", self.surfaces), 
                        "black": ple.Human_Player_Extended("black", self.surfaces)}
        self.interactor = interactor.Interactor(self.painter, cal_ex.Calculator_Extended(self.locator, self.players), self.turn, self.buttons)
        self.mode = mode


#In this game against the computer, the human player is white and begins the game        
class HvsC_Game_Basic(Game):
    def __init__(self, surface, mode = "basic"):
        super().__init__(surface)
        self.players = {"white": plh.Human_Player("white", self.surfaces), 
                        "black": plc.Computer_Player("black", self.surfaces)}
        self.com_action = ca.Computer_Action(self.locator, self.players)
        self.calculator = cal_ex.Calculator_Extended(self.locator, self.players)
        self.interactor = interactor.Interactor(self.painter, self.calculator, self.turn, self.buttons)
        self.mode = mode
        
        







