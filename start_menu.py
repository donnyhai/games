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
        
    def draw_settings_window(self):
        x_size = self.size[0]
        y_size = self.size[1]
        pygame.draw.rect(self.surface, self.color, pygame.Rect(self.location[0] + 5, self.location[1] - y_size -5, x_size, y_size))
        pygame.draw.rect(self.surface, (25,25,25), pygame.Rect(self.location[0] + 5, self.location[1] - y_size- 5, x_size, y_size), 3)
        
    def write_settings(self, text, color, size):
        linewise_settings = text.split("\n")
        lines_number = len(linewise_settings)
        length = max([len(s) for s in linewise_settings])*size
        height = (2 * lines_number + 1) * size
        font_size = 2*int(length//len(text))
        
        for line in linewise_settings:
            myFont = pygame.font.SysFont("Comic Sans MS", font_size)
            myText = myFont.render(line, 1, color)
            self.surface.blit(myText, ((self.location[0]+length/2) - myText.get_width()/2, (self.location[1]-height/2) - myText.get_height()/2))
        return self.surface