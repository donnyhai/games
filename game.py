import board
import player
import locator
import board_subset

class Game:
    board_size = 50
        
class HvsH_Game(Game):
    def __init__(self):
        self.players = [player.Human_Player("white"), player.Human_Player("black")]
        self.locator = locator.Locator(board.Board(Game.board_size), self.players, look_into_past = 100)
        self.board = board.Board(Game.board_size, board_subset.Board_Subset(self.locator))
        
class HvsC_Game(Game):
    def __init__(self):
        self.players = [player.Human_Player("white"), player.Computer_player("black")]
        self.locator = locator.Locator(board.Board(Game.board_size), self.players, look_into_past = 100)
        self.board = board.Board(Game.board_size, board_subset.Board_Subset(self.locator))
    

game = Game()

hgame = HvsH_Game()



if __name__ == "main":
    pass