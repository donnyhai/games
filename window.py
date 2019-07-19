import pygame, sys, buttons

pygame.init()

showed_display = pygame.display.set_mode((1920, 1080),0, 32)
#showed_display = pygame.display.set_mode((1920, 1080),pygame.RESIZABLE, 32)
pygame.display.set_caption('Spielfeld')
showed_display.fill((250,200,255))


test_image = pygame.image.load('ant.png')
test_image = pygame.transform.scale(test_image, (40, 50))
test_image_position = (test_image.get_width(), test_image.get_height())
start_game_button = buttons.Button.create_button(showed_display, (107,142,35),225,135,200,100,0, "Example", (255,255,255))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(), sys.exit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                showed_display.blit(test_image,test_image_position)
        pygame.display.update()