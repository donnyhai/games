import pygame

pygame.init()

#find out, if a value is convertible to int
def maybe_int(value):
  try:
    int(value)
    return True
  except ValueError:
    return False

class start_menu:
    def __init__ (self, surface):
        self.surface = surface
        
    

class settings_window:
    def __init__(self, surface, color, location, size):
        self.surface = surface
        self.color = color
        self.location = location
        self.settings = open("settings.txt", "r").read()
        self.size = size
        self.x_size = size[0]
        self.y_size = size[1]
        
    def draw_settings_window(self):
        pygame.draw.rect(self.surface, self.color, pygame.Rect(self.location[0] + 5, self.location[1] - self.y_size -5, self.x_size, self.y_size))
        pygame.draw.rect(self.surface, (25,25,25), pygame.Rect(self.location[0] + 5, self.location[1] - self.y_size- 5, self.x_size, self.y_size), 3)
        
    def write_settings(self, text, color):
        linewise_settings = text.split("\n")
        lines_number = len(linewise_settings)
        length = max([len(s) for s in linewise_settings])
        font_size = 2 * int((0.9 * self.x_size) / length)        
        height = pygame.font.SysFont("Arial", font_size).render(linewise_settings[0],1, (0,0,0)).get_height()
        y_distance = max ( 10 , (self.y_size- lines_number * height) // (lines_number +1))
        
        if self.y_size < (lines_number + 1) * y_distance + lines_number * height:
           self.y_size = (lines_number + 1) * y_distance + lines_number * height 
        
        pygame.draw.rect(self.surface, self.color, pygame.Rect(self.location[0] + 5, self.location[1] - self.y_size -5, self.x_size, self.y_size))
        pygame.draw.rect(self.surface, (25,25,25), pygame.Rect(self.location[0] + 5, self.location[1] - self.y_size- 5, self.x_size, self.y_size), 3)
        
        counter =  1
        for line in linewise_settings:
            myFont = pygame.font.SysFont("Arial", font_size)
            myText = myFont.render(line, 1, color)
            print(self.location[1]- self.y_size - 5 + (counter-1) * height + counter * y_distance)
            self.surface.blit(myText, (self.location[0]+ 10, self.location[1]- self.y_size - 5 + (counter-1) * height + counter * y_distance))
            counter += 1
        #return self.surface