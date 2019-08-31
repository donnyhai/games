import board
import player
import locator
import board_subset
import interactor

class Game:
    
    board_size = 50
    board = board.Board(board_size)
    
class HvsH_Game(Game):
    def __init__(self, surface):
        self.surface = surface
        self.players = [player.Human_Player("white", self.surface), player.Human_Player("black", self.surface)]
        self.locator = locator.Locator(Game.board, self.players, look_into_past = 100)
        self.interactor = interactor.Interactor(Game.board, board_subset.Board_Subset(self.locator))
        
class HvsC_Game(Game):
    def __init__(self, surface):
        self.surface = surface
        self.players = [player.Human_Player("white", self.surface), player.Computer_player("black", self.surface)]
        self.locator = locator.Locator(Game.board, self.players, look_into_past = 100)
        self.interactor = interactor.Interactor(Game.board, board_subset.Board_Subset(self.locator))
    
def start_game(surface):
    pass