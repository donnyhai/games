import board
import player
import locator

class Game:
    def __init__(self, game_type = "two-player", board_size = 50):
        self.game_type = game_type
        self.board = board.Board(board_size)
        self.players = self.make_players()
        self.locator = locator.Locator(self.board, self.players, look_into_past = 50)
        
    #create players according to the game_type
    def make_players(self):
        if self.game_type == "two-player":
            player_1 = player.Player(color = "white")
            player_2 = player.Player(color = "black")
            return {"h1": player_1, "h2": player_2}
    
    
game = Game()
board = game.board

if __name__ == "main":
    game = Game()