import pygame, sys, buttons

pygame.init()

#Set window and button sizes
window_x_size =  1050
window_y_size = int(405*1050/720)
button_x_size = 200
button_y_size = 120


#creating showable  start_window on display with, set name and set background color
start_showed_display = pygame.display.set_mode((window_x_size,window_y_size),0,32)
#showed_display = pygame.display.set_mode((1920, 1080),pygame.RESIZABLE, 32)
pygame.display.set_caption("Spiel-Menü")
start_showed_display.fill((100,100,100))



#initialize class buttons.Button as name Button
Button = buttons.Button()


#try showing an image on screen AFTER pressing left mousekey
test_image = pygame.image.load("ant.png")
test_image = pygame.transform.scale(test_image, (100, 150))
test_image_position = (test_image.get_width(), test_image.get_height())

#gamebackground
background = pygame.image.load("background1.jpg")
background_position = (background.get_width(), background.get_height())


#set a centered "Spiel Starten" - Button
start_game_button = Button.create_button(start_showed_display, (200,200,200),
                                         (pygame.Surface.get_size(start_showed_display)[0]-button_x_size)*0.5,
                                         (pygame.Surface.get_size(start_showed_display)[1]-button_y_size)*0.5,
                                         button_x_size,    button_y_size,
                                         0,       "Spiel Starten", (255,255,255))


#update the window so that the button is shown
pygame.display.update()


#run the window and wait for mouseclicks or quit
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                start_showed_display.blit(test_image,test_image_position)
                if Button.pressed(event.pos) == True:
                    start_showed_display.fill
                    Text = "Spiel wird gestartet"
                    print(Text)
                    #creating board_window
                    #board_window = pygame.display.set_mode(background_position, 0, 32)
                    #pygame.display.set_caption("Spielbrett")
                    #board_window.fill((255,255,255))
                    #start_showed_display.blit(background,(0,0))
                    
                else:
                    print("Spiel wird nicht gestartet")
        pygame.display.update()