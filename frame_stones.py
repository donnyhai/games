
# a frame_stones object has to be initialized with a stones_set of type you'll get from window.py resp. you return from creating_board.create_all_stones()
# but for better handling all these stones will directly be written just in one list
class frame_stones:
    
    def __init__(self, stones_set):
        self.stones_set = stones_set
        self.stones_list = self.change_list_type(self.stones_set)
    
    def change_list_type(self, stones_set):
        lis0 = []
        lis0.append(stones_set[0][1].ant)
        lis0.append(stones_set[0][1].hopper)
        lis0.append(stones_set[0][1].spider)
        lis0.append(stones_set[0][1].bee)
        lis0.append(stones_set[1][1].ant)
        lis0.append(stones_set[1][1].hopper)
        lis0.append(stones_set[1][1].spider)
        lis0.append(stones_set[1][1].bee)
        return lis0
    
    def click_on_frame_stone(self, stones_list, position):
        white_frame_ant = self.stones_list[0]
        white_frame_hopper = self.stones_list[1]
        white_frame_spider = self.stones_list[2]
        white_frame_bee = self.stones_list[3]
        
        black_frame_ant = self.stones_list[4]
        black_frame_hopper = self.stones_list[5]
        black_frame_spider = self.stones_list[6]
        black_frame_bee = self.stones_list[7]
        
        clicked_on_list = []
        clicked_on_list.append(white_frame_ant.point_in_hexagon(white_frame_ant.points, position))
        clicked_on_list.append(white_frame_hopper.point_in_hexagon(white_frame_hopper.points, position))
        clicked_on_list.append(white_frame_spider.point_in_hexagon(white_frame_spider.points, position))
        clicked_on_list.append(white_frame_bee.point_in_hexagon(white_frame_bee.points, position))
        clicked_on_list.append(black_frame_ant.point_in_hexagon(black_frame_ant.points, position))
        clicked_on_list.append(black_frame_hopper.point_in_hexagon(black_frame_hopper.points, position))
        clicked_on_list.append(black_frame_spider.point_in_hexagon(black_frame_spider.points, position))
        clicked_on_list.append(black_frame_bee.point_in_hexagon(black_frame_bee.points, position))
        
        return clicked_on_list
