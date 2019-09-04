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
    def __init__(self, surface, color, location):
        self.surface = surface
        self.color = color
        self.location = location
        
    def draw_settings_window(self, x_size, y_size):
        pygame.draw.rect(self.surface, self.color , pygame.Rect(self.location[0], self.location[1] - y_size, x_size, y_size))
        