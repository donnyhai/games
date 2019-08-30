import pygame, sys, buttons,  creating_board as cb

pygame.init()
pygame.display.init()

#Set window and button sizes
window_x_size =  1920
window_y_size = int(window_x_size*9/16)
window_size = (window_x_size, window_y_size)
button_x_size = 200
button_y_size = 120


#creating showable  start_window on display with, set name and set background color
showed_display = pygame.display.set_mode(window_size,0,32)
#showed_display = pygame.display.set_mode((1920, 1080),pygame.RESIZABLE, 32)
pygame.display.set_caption("Spiel-Menue")
showed_display.fill((100,100,100))

#initialize class buttons.Button as name Button
Button = buttons.Button()


#colors
white = (255,255,255)
black = (0,0,0)
background_color1 = (255,211,155)
background_color2 = (244,164,96)
background_color3 = (238,197,145)

#set a centered "Spiel Starten" - Button
start_game_button = Button.create_button(showed_display, (200,200,200),
                                         (pygame.Surface.get_size(showed_display)[0]-button_x_size)*0.5,
                                         (pygame.Surface.get_size(showed_display)[1]-button_y_size)*0.5,
                                         button_x_size,    button_y_size,
                                         0,       "Spiel Starten", (255,255,255))

start_game_mode = True

#run the window and wait for mouseclicks or quit
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif start_game_mode == True:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if Button.pressed(event.pos) == True:
                    Text = "Spiel wird gestartet"
                    print(Text)
                    pygame.display.set_caption("Spielbrett")
                    cb.color_background(showed_display, background_color2, 128, window_size)
                    cb.set_ingame_frame(showed_display)
                    cb.draw_insects(showed_display,(255,255,230))
                    start_game_mode = False 
                else:
                    print("Spiel wird nicht gestartet")
    pygame.display.update()
    
    
    