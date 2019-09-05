from math import sqrt

class Stone:
    def __init__(self, stone_type, number):
        self.type = stone_type
        self.number = number
        self.is_on_board = False #note that this attribute makes more sense for actual playing stones.
        #for side_stones (see player) this attributes just claims, whether a certain kind of stone is still 
        #available at the side or not. for example, if a side_stone "ant" has this attribute on is_on_board = True,
        #than there is no ant on the side anymore and therefore all three ants were already put on the board. 
        self.has_bug_on = False
        self.is_mosquito = False
        self.color = ""
        
    def set_color(self, color):
        self.color = color

class hexagon_stone:
    
    def __init__(self, size, stone = Stone("empty",1), pixel_position = (0,0)):
        #surface and pixel attributes
        self.size = size
        self.pixel_position = pixel_position #note, that depending on the surface the hex_stone was drawn,
        #this attribute does not display the position in the full surface
        self.points = self.getting_hexa(self.size, pixel_position)
        self.is_drawn = False
        self.is_marked = False
        
        #stone and board attributes
        self.stone = stone
        self.board_position = (-1,-1)
        self.is_empty = True
    
    # like always, the postion is the coordinate of the top left corner    
    def set_pixel_pos(self, new_pixel_pos):
        self.pixel_position = new_pixel_pos
        self.points = self.getting_hexa(self.size, new_pixel_pos)
        
    #calculate the six hexagon points with starting point start_vector (point top left) and side size scaling    
    def getting_hexa(self, scaling_ratio, start_vector):    
        hex_coords = [(0,0), (1,0), (1.5, 3**(1/2)/2), (1, 3**(1/2)), (0,3**(1/2)), (-0.5, 3**(1/2)/2)]
        scaled_coords = []
        for x,y in hex_coords:
            scaled_coords.append([x*scaling_ratio + start_vector[0], y*scaling_ratio + start_vector[1]])
        return scaled_coords
    
    def hexagon_center(self, hexagon_points):
        return hexagon_points[0]+((hexagon_points[1]-hexagon_points[0])*0.5, (hexagon_points[1]-hexagon_points[0])* 3**(0.5)*0.5)

    
    
    #hex_stone was drawn on subsurface, and click was on global pixel_coords. is it inside the hex_stone ? 
    def point_in_hexagon(self, pixel_coords, subsurface):
        
        #save actual pixel_position and translate hex_stone to its actual global position
        save_pixel_position = self.pixel_position
        subsurface_translation = subsurface.get_offset()
        self.set_pixel_pos((save_pixel_position[0] + subsurface_translation[0],
                            save_pixel_position[1] + subsurface_translation[1]))
        
        def euclidean_metric(vector):
            squared = [x*x for x in vector]
            return sqrt(sum(squared))
        
        boundary_vectors = []
        connection_vectors = []
        for i in range(len(self.points)):
            boundary_vectors.append((self.points[(i+1)%len(self.points)][0]-self.points[i][0],self.points[(i+1)%len(self.points)][1]-self.points[i][1]))
            connection_vectors.append((pixel_coords[0]-self.points[i][0], pixel_coords[1]-self.points[i][1]))
        test = True
        angles = []
        for i in range(len(self.points)):
            angles.append((boundary_vectors[i][0]*connection_vectors[i][0]+boundary_vectors[i][1]*connection_vectors[i][1])
                          /(euclidean_metric(boundary_vectors[i])*euclidean_metric(connection_vectors[i])))
            if angles[i] <= -0.5:
                test = False
                
        #reset pixel_pos to the save_pixel_pos 
        self.set_pixel_pos(save_pixel_position)
        return test
    
    
    #change stone on this hexagon
    def change_stone(self, new_stone):
        self.stone = new_stone
        if new_stone.stone_type == "empty":
            self.is_empty = True
            self.board_position = (-1,-1)
        else:
            self.is_empty = False
