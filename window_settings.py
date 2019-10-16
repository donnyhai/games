import pygame
import variables as v
import button
import colors as c
import window_hvsh_basic, window_hvsh_extended, window_hvsc_basic
import painter as pt
import window_menu as menu

pygame.init()
clock = pygame.time.Clock()

 
class Window_Settings:
    def __init__(self):
        self.running = False
        self.buttons = None
        self.display = None             #surface
        self.values = {"music":False, "sound":True, "version":"basic", "mode":"hvsh", "resolution":(1152, 864)}
 
    def on_init(self):
        
        #create display and set display attr
        pygame.display.init()
        self.display = pygame.display.set_mode(v.window_size, 0, 32)
        pygame.display.set_caption("Einstellungen")
        self.display.fill((50,50,200))
        
        #create buttons and draw them
        self.buttons = self.create_buttons()
        for button0 in self.buttons.values():
            button0.draw_button()
        pt.Painter().write_text(self.display, "Settings", 50, (255,255,255), (v.window_x_size * 0.42, v.window_y_size * 0.05))
        
        pt.Painter().write_text(self.display, "music:", 20, (255,255,255), (v.window_x_size * 0.1, v.window_y_size * 0.25))
        pt.Painter().write_text(self.display, "sound:", 20, (255,255,255), (v.window_x_size * 0.5, v.window_y_size * 0.25))
        pt.Painter().write_text(self.display, "version:", 20, (255,255,255), (v.window_x_size * 0.1, v.window_y_size * 0.5))
        pt.Painter().write_text(self.display, "mode:", 20, (255,255,255), (v.window_x_size * 0.5, v.window_y_size * 0.5))
        pt.Painter().write_text(self.display, "resolution:", 20, (255,255,255), (v.window_x_size * 0.35, v.window_y_size * 0.75))
        pygame.display.update()

 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.buttons["back_button"].pressed(event.pos):
                men = menu.Menu(self.values)
                men.on_execute()
                self.running = False
            if self.buttons["hvsh_basic_button"].pressed(event.pos):
                whhb = window_hvsh_basic.Window_HvsH_Basic()
                whhb.on_execute()
                self.running = False
            elif self.buttons["hvsh_extended_button"].pressed(event.pos):
                whhe = window_hvsh_extended.Window_HvsH_Extended()
                whhe.on_execute()
                self.running = False
            elif self.buttons["hvsc_basic_button"].pressed(event.pos):
                whcb = window_hvsc_basic.Window_HvsC_Basic()
                whcb.on_execute()
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
        back_button = button.Button(self.display, "Back", 25, 
                                             (v.window_x_size * 0, v.window_y_size * 0), 
                                             (v.button_x_size, v.button_y_size),
                                             c.button_color, (0,0,0))
        return {"back_button": back_button, "hvsh_basic_button": hvsh_basic_button, "hvsh_extended_button": hvsh_extended_button,
                "hvsc_basic_button": hvsc_basic_button, "hvsc_extended_button": hvsc_extended_button,
                "cvsc_basic_button": cvsc_basic_button, "cvsc_extended_button": cvsc_extended_button}



 
if __name__ == "__main__" :
    window_pregame = Window_Settings()
    window_pregame.on_execute()