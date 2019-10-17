import pygame
import variables as v
import button
import colors as c
import window_hvsh_basic, window_hvsh_extended, window_hvsc_basic
import window_settings
import game as g
pygame.init()
clock = pygame.time.Clock()

 
# Welcome to hive !

# for insights of processing times use the follwing pattern to check code for its needed processing time:
#import time
#t = time.clock()
# ##code##
#print(time.clock() - t)


class Menu:
    def __init__(self, settings = None):
        self.running = False
        self.buttons = None
        self.display = None
        self.settings = None
        if settings is None:
            self.settings = {"music": False, "sound": True, "version": "basic", "mode": "hvsh", "resolution": (1152,664)} #default settings
        else:
            self.settings = settings
 
    def on_init(self):
        
        #create display and set display attr
        pygame.display.init()
        self.display = pygame.display.set_mode(v.window_size, 0, 32)
        pygame.display.set_caption("Spiel-Menue")
        self.display.fill((100,100,100))
        
        #create buttons and draw them
        self.buttons = self.create_buttons()
        for button0 in self.buttons.values():
            button0.draw_button()
        
        pygame.display.update()

 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.buttons["settings"].pressed(event.pos):
                ws = window_settings.Window_Settings()
                ws.on_execute()
                self.running = False
            elif self.buttons["start_game"].pressed(event.pos):
                game = g.Game(self.settings)
                if self.settings["mode"] == "hvsh":
                    if self.settings["version"] == "basic":
                        wg = window_hvsh_basic.Window_HvsH_Basic(game)
                    elif self.settings["version"] == "extended":
                        wg = window_hvsh_extended.Window_HvsH_Extended(game)
                elif self.settings["mode"] == "hvsc":
                    if self.settings["version"] == "basic":
                        wg = window_hvsc_basic.Window_HvsC_Basic(game)
                    elif self.settings["version"] == "extended":
                        #wg = window_hvsc_extended.Window_HvsC_Extended(game)
                        pass
                wg.on_execute()
                self.running = False
        clock.tick(v.FPS)
            
    def on_loop(self):
        pass
    def on_render(self):
        pass
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if not self.running:
            self.on_init()
            self.running = True
 
        while self.running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
        
    def create_buttons(self):
        settings_button = button.Button(self.display, "Settings", 25, 
                                          (v.window_x_size * 2 // 12, v.window_y_size * 7 // 20), 
                                          (v.button_x_size, v.button_y_size),
                                          c.button_color, (0,0,0))
        
        start_game_button = button.Button(self.display, "Start Game", 25, 
                                             (v.window_x_size * 2 // 12, v.window_y_size * 3 // 5), 
                                             (v.button_x_size, v.button_y_size),
                                             c.button_color, (0,0,0))
        return {"settings": settings_button, "start_game": start_game_button}



 
if __name__ == "__main__":
    window_menu = Menu()
    window_menu.on_execute()
