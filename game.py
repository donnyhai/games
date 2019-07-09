import board
import player
import locator
import board_subset
import interactor

class Game:
    board_size = 50
    board = board.Board(board_size)
        
class HvsH_Game(Game):
    def __init__(self):
        self.players = [player.Human_Player("white"), player.Human_Player("black")]
        self.locator = locator.Locator(Game.board, self.players, look_into_past = 100)
        self.interactor = interactor.Interactor(Game.board, board_subset.Board_Subset(self.locator))
        
class HvsC_Game(Game):
    def __init__(self):
        self.players = [player.Human_Player("white"), player.Computer_player("black")]
        self.locator = locator.Locator(Game.board, self.players, look_into_past = 100)
        self.interactor = interactor.Interactor(Game.board, board_subset.Board_Subset(self.locator))
    

game = Game()

hgame = HvsH_Game()



if __name__ == "main":
    pass