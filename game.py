import board
import player
import locator
import calculator
import interactor
import frame_stones

class Game:
    
    board_size = 30
    
class HvsH_Game(Game):
    def __init__(self, surface, stones_from_cb):
        self.surface = surface
        self.board = board.Board(Game.board_size, self.surface)
        self.players = [player.Human_Player("white", self.surface), player.Human_Player("black", self.surface)]
        self.locator = locator.Locator(self.board, self.players, 100, self.surface)
        self.interactor = interactor.Interactor(self.board, self.surface, calculator.Calculator(self.locator))
        self.frame_stones = frame_stones.frame_stones(stones_from_cb)
        
        
#class HvsC_Game(Game):
#    def __init__(self, surface):
#        self.surface = surface
#        self.board = board.Board(Game.board_size, self.surface)
#        self.players = [player.Human_Player("white", self.surface), player.Computer_player("black", self.surface)]
#        self.locator = locator.Locator(self.board, self.players, look_into_past = 100, self.surface)
#        self.interactor = interactor.Interactor(self.board, calculator.Calculator(self.locator))
    
def start_game(surface):
    pass

#accept here only the stones_set created like in window.py resp. you return from creating_board.create_all_stones()
#def click_on_frame_stone (surface, stones_set, position):
#    white_frame_ant = stones_set[0][1].ant
#    white_frame_hopper = stones_set[0][1].hopper
#    white_frame_spider = stones_set[0][1].spider
#    white_frame_bee = stones_set[0][1].bee
#    
#    black_frame_ant = stones_set[1][1].ant
#    black_frame_hopper = stones_set[1][1].hopper
#    black_frame_spider = stones_set[1][1].spider
#    black_frame_bee = stones_set[1][1].bee
#    
#    clicked_on_list = []
#    clicked_on_list.append(white_frame_ant.point_in_hexagon(white_frame_ant.points, position))
#    clicked_on_list.append(white_frame_hopper.point_in_hexagon(white_frame_hopper.points, position))
#    clicked_on_list.append(white_frame_spider.point_in_hexagon(white_frame_spider.points, position))
#    clicked_on_list.append(white_frame_bee.point_in_hexagon(white_frame_bee.points, position))
#    clicked_on_list.append(black_frame_ant.point_in_hexagon(black_frame_ant.points, position))
#    clicked_on_list.append(black_frame_hopper.point_in_hexagon(black_frame_hopper.points, position))
#    clicked_on_list.append(black_frame_spider.point_in_hexagon(black_frame_spider.points, position))
#    clicked_on_list.append(black_frame_bee.point_in_hexagon(black_frame_bee.points, position))
#    
#    return clicked_on_list
