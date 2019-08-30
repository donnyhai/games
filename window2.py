import pygame, sys, buttons, display
pygame.init()

#Set window and button sizes
window_x_size =  1050
window_y_size = int(405*1050/720)
button_x_size = 200
button_y_size = 120

#create start window
start_window = display.Display(window_x_size, window_y_size, "Spiel-Menü")
start_window_showed = start_window.display.set_mode((start_window.x_size, start_window.y_size), pygame.RESIZABLE, 0, 32)
start_window_showed.fill((100,100,100))

#create a button object button and create a start_game_button
button = buttons.Button()
start_game_button = button.create_button(start_window, (200,200,200),
                                         (pygame.Surface.get_size(start_window)[0]-button_x_size)*0.5,
                                         (pygame.Surface.get_size(start_window)[1]-button_y_size)*0.5,
                                         button_x_size, button_y_size,
                                         0, "Spiel Starten", (255,255,255))

#update the window so that the button is shown
pygame.display.update()

#gamebackground
background = pygame.image.load("images/wiese.jpg")
background_position = (background.get_width(), background.get_height())

#run the window and wait for mouseclicks or quit
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if button.pressed(event.pos) == True:
                    Text = "Spiel wird gestartet"
                    print(Text)
                    #creating board_window
                    board_window = pygame.display.set_mode(background_position, pygame.RESIZABLE, 0, 32)
                    pygame.display.set_caption("Spielbrett")
                    board_window.fill((255,255,255))
                    start_window.blit(background,(0,0))
                    #create board object
                    #draw left (white)/right (black) areas for the stones of two players, middle area stays empty
                    #a text field (down left for white, down right for black) is seeable, displaying for both players, how many moves are left for the player
                    #to lay his bee. as soon as one player puts his bee, the text field gets empty for this player
                    
                    #in general: text areas display information for both players (like error moves etc)
                    #in general: index of stone moves one down, if stone was put onto field
                    
                    ###first phase (white puts one stone, black puts one stone, move 1)
                    #begin phase, white begins
                    #white selects one of his stones, one shadowed hexagon appears in the middle of the middle area
                    #white clicks on the shadowed hexagon and stone moves there and lays there
                    #index number of the stone decreases by one.
                    #black selects one of his stones, all neighbour hexagons of the already laying white stone get shaded
                    #black clicks on one shaded hexagon and stone moves there
                    
                    ###second phase (players put stones until bee is put, move 1 to 4)
                    #both players continue to put stones until both bees are put, if bee isnt put until 4. move
                    #again a text field appears, as discribed above
                    
                    ###third phase
                    #players put stones, until the condition is satisfied that at least one bee is surrounded by stones
                    #when this happens, depending on which bee (or both bees) is surrounded, a finish text appears to 
                    #claim the winner. a question appears whether a new game wants to be played, if pressed no,
                    #either the window closes, or something else funny happens, waiting the user to close the window in x
                    
                    
                    
                else:
                    print("Spiel wird nicht gestartet")
        pygame.display.update()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        