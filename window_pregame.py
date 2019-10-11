import pygame
import variables as v
import button
import colors as c
import window_hvsh_basic
pygame.init()
clock = pygame.time.Clock()

 
class Pregame:
    def __init__(self):
        self.running = False
        self.buttons = None
        self.display = None
 
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
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.buttons["hvsh_basic_button"].pressed(event.pos):
                hvsh_basic_game = window_hvsh_basic.App()
                hvsh_basic_game.on_execute()
                #execute corresponding method
                self.running = False
            elif self.buttons["hvsh_extended_button"].pressed(event.pos):
                #execute corresponding method
                self.running = False
            elif self.buttons["hvsc_basic_button"].pressed(event.pos):
                #execute corresponding method
                self.running = False
            elif self.buttons["hvsc_extended_button"].pressed(event.pos):
                #execute corresponding method
                self.running = False
            elif self.buttons["cvsc_basic_button"].pressed(event.pos):
                #execute corresponding method
                self.running = False
            elif self.buttons["cvsc_extended_button"].pressed(event.pos):
                #execute corresponding method
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
        hvsh_basic_button = button.Button(self.display, "hvsh_basic", 25, 
                                          (v.window_x_size * 2 // 12, v.window_y_size * 7 // 20), 
                                          (v.button_x_size, v.button_y_size),
                                          c.button_color, (0,0,0))
        
        hvsh_extended_button = button.Button(self.display, "hvsh_extended", 25, 
                                             (v.window_x_size * 2 // 12, v.window_y_size * 3 // 5), 
                                             (v.button_x_size, v.button_y_size),
                                             c.button_color, (0,0,0))
        hvsc_basic_button = button.Button(self.display, "hvsc_basic", 25, 
                                          (v.window_x_size * 5 // 12, v.window_y_size * 7 // 20), 
                                          (v.button_x_size, v.button_y_size),
                                          c.button_color, (0,0,0))
        hvsc_extended_button = button.Button(self.display, "hvsc_extended", 25, 
                                             (v.window_x_size * 5 // 12, v.window_y_size * 3 // 5), 
                                             (v.button_x_size, v.button_y_size),
                                             c.button_color, (0,0,0))
        cvsc_basic_button = button.Button(self.display, "cvsc_basic", 25, 
                                          (v.window_x_size * 8 // 12, v.window_y_size * 7 // 20), 
                                          (v.button_x_size, v.button_y_size),
                                          c.button_color, (0,0,0))
        cvsc_extended_button = button.Button(self.display, "cvsc_extended", 25, 
                                             (v.window_x_size * 8 // 12, v.window_y_size * 3 // 5), 
                                             (v.button_x_size, v.button_y_size),
                                             c.button_color, (0,0,0))
        return {"hvsh_basic_button": hvsh_basic_button, "hvsh_extended_button": hvsh_extended_button,
                "hvsc_basic_button": hvsc_basic_button, "hvsc_extended_button": hvsc_extended_button,
                "cvsc_basic_button": cvsc_basic_button, "cvsc_extended_button": cvsc_extended_button}



 
if __name__ == "__main__" :
    window_pregame = Pregame()
    window_pregame.on_execute()