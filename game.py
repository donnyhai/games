import board
import player
import locator

class Game:
    board_size = 50
    board = board.Board(board_size)
        
class HvsH_Game(Game):
    def __init__(self):
        self.players = [player.Human_Player("white"), player.Human_Player("black")]
        self.locator = locator.Locator(board.Board(Game.board_size), self.players, look_into_past = 100)
        
class HvsC_Game(Game):
    def __init__(self):
        self.players = [player.Human_Player("white"), player.Computer_player("black")]
        self.locator = locator.Locator(board.Board(Game.board_size), self.players, look_into_past = 100)
        
    

game = Game()

hgame = HvsH_Game()



if __name__ == "main":
    pass